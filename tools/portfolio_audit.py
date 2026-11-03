#!/usr/bin/env python3
"""Offline portfolio checks. Never prints secret values or contacts outside services."""
import ast
import os
from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import unquote

ROOT = Path.cwd()
ASSET_EXT = {".csv", ".tsv", ".xlsx", ".xlsm", ".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp", ".pdf", ".pptx", ".docx", ".parquet", ".pbix", ".twbx"}
SKIP_SCAN_EXT = ASSET_EXT | {".zip", ".7z", ".gz", ".tar", ".db", ".sqlite", ".sqlite3", ".lock"}
SECRET_PATTERNS = {
    "private key header": re.compile(rb"-----BEGIN (?:RSA |EC |DSA |OPENSSH |ENCRYPTED )?PRIVATE KEY-----"),
    "AWS access key": re.compile(rb"(?<![A-Z0-9])(?:AKIA|ASIA)[A-Z0-9]{16}(?![A-Z0-9])"),
    "GitHub token": re.compile(rb"(?<![A-Za-z0-9])(?:ghp_|gho_|ghu_|ghs_|ghr_)[A-Za-z0-9_]{36,}"),
    "GitHub fine-grained token": re.compile(rb"github_pat_[A-Za-z0-9_]{60,}"),
    "Stripe live secret": re.compile(rb"sk_live_[A-Za-z0-9]{16,}"),
    "Google API key": re.compile(rb"AIza[0-9A-Za-z_-]{35}"),
}
LINK = re.compile(r"!?\[[^\]]*\]\((<[^>]+>|[^)\n]+)\)")
NOTICES = {"ASSET_SOURCES.md", "DATA_SOURCES.md", "THIRD_PARTY_NOTICES.md",
           "THIRD_PARTY_MATERIALS.md", "ATTRIBUTION.md", "NOTICE", "NOTICE.md"}
issues, warnings = [], []

def tracked():
    proc = subprocess.run(["git", "ls-files", "-z"], capture_output=True)
    if proc.returncode:
        issues.append("Cannot list tracked Git files")
        return []
    return [x.decode("utf-8", "replace") for x in proc.stdout.split(b"\0") if x]

paths = tracked()
for required in ("README.md", "LICENSE"):
    if required not in paths:
        issues.append(f"Required root file missing: {required}")

for name in paths:
    p = ROOT / name
    if not p.is_file():
        continue
    base = p.name.lower()
    if (base in (".env", "credentials.json", "id_rsa", "id_ed25519")
            or (base.startswith(".env.") and not base.endswith((".example", ".sample")))
            or p.suffix.lower() in (".p12", ".pfx", ".pem", ".key")):
        issues.append(f"Potential credential file committed: {name}")
    if p.stat().st_size > 1_000_000 or p.suffix.lower() in SKIP_SCAN_EXT:
        continue
    try:
        data = p.read_bytes()
    except OSError:
        warnings.append(f"Could not read: {name}")
        continue
    if b"\0" in data[:4096]:
        continue
    for label, pattern in SECRET_PATTERNS.items():
        if pattern.search(data):
            issues.append(f"Possible {label} in tracked file: {name} (value redacted)")
    if p.suffix.lower() == ".py":
        try:
            ast.parse(data.decode("utf-8-sig"), filename=name)
        except (SyntaxError, UnicodeError) as exc:
            issues.append(f"Python syntax/encoding issue in {name}: {getattr(exc, 'lineno', '?')}")

readme = ROOT / "README.md"
if readme.exists():
    try:
        markdown = readme.read_text(encoding="utf-8")
        checked = set()
        for found in LINK.finditer(markdown):
            href = found.group(1).strip().strip("<>").split(maxsplit=1)[0]
            if not href or href.startswith(("#", "//")) or re.match(r"^[A-Za-z][A-Za-z0-9+.-]*:", href):
                continue
            target = unquote(href.split("#", 1)[0].split("?", 1)[0])
            if not target or target in checked:
                continue
            checked.add(target)
            if not (ROOT / target).exists():
                warnings.append(f"README local link could not be resolved: {target[:160]}")
    except (OSError, UnicodeError):
        warnings.append("README could not be checked for links")

assets = [p for p in paths if Path(p).suffix.lower() in ASSET_EXT]
have_attribution = any(p in paths for p in NOTICES)
if assets and not have_attribution:
    warnings.append(f"{len(assets)} tracked data/visual/document assets; confirm their source and license in an attribution inventory")
if not any("/tests/" in ("/" + p) or p.startswith("tests/") or Path(p).name.startswith("test_") for p in paths):
    warnings.append("No obvious automated test directory/files found (may be documentation-only)")

print(f"Tracked files: {len(paths)} | Reviewable assets: {len(assets)} | Findings: {len(issues)} errors, {len(warnings)} advisory")
for item in issues[:40]:
    print("::error::" + item.replace("\n", " "))
for item in warnings[:40]:
    print("::warning::" + item.replace("\n", " "))
if len(issues) > 40 or len(warnings) > 40:
    print("Additional findings truncated; do not treat this as a full audit")

summary = os.environ.get("GITHUB_STEP_SUMMARY")
if summary:
    with open(summary, "a", encoding="utf-8") as f:
        f.write("## Repository audit (default branch checkout)\n\n")
        f.write(f"- Tracked files inspected: {len(paths)}\n- Tracked asset candidates: {len(assets)}\n")
        f.write(f"- High-confidence credential/file and Python syntax findings: {len(issues)}\n")
        f.write(f"- Advisory findings: {len(warnings)} (output may be capped)\n")
        f.write("- Relative README links checked locally; external URLs, historical credentials and licensing rights require independent review.\n")
if issues:
    sys.exit(1)
