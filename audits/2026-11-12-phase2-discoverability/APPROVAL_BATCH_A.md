# Phase 2 — first repository-settings approval batch

**Status: prepared for owner review; NOTHING applied.** All values below are proposals. These settings live in the GitHub repository **About** panel; merging this or any other documentation PR does **not** update About metadata.

## Validation and constraints

- Scope: 7 first-batch public repositories from the full [35-repository audit](AUDIT.md) and [24-change proposal manifest](proposed-metadata.json).
- GitHub snapshot cross-check: P0/P1 current description/topic/homepage values match the audit. Proposed topic arrays have no duplicates, contain only lowercase letters, numbers and hyphens, and remain at or below 20 topics.
- Documentation context: product-manager case studies are explicitly simulations; the cybersecurity project uses synthetic reproducible lab data; the data analyst repository documents an offline explorer.
- Existing profile About terms `excel` and `powerbi` are retained in the revised proposed profile topics. The GitHub profile `README.md` is **not** part of these changes.
- Public site `https://jamiechristian22.github.io/` was **not verified reachable** from the review environment. Source HTML, a repository README and site checking instructions were inspected, but those are **not** proof of a deployed public website.
- **Homepage gate:** do not apply **any** proposed homepage change until the public site is independently opened and confirmed to show relevant projects. If not verified, preserve each existing homepage as-is.
- **No changes to project evidence, private repositories, main branches, profile README, permissions, or deployment settings.**

## Approval batch A — exact proposed settings

Approve each repository and field independently; omitted fields are intentionally unchanged.

### 1. [`JamieChristian22`](https://github.com/JamieChristian22/JamieChristian22) — P0

**Proposed now (not applied):**

```json
{
  "description": "Career-focused business and technology portfolio: cloud/platform engineering, cybersecurity, IT support, data/BI, business/systems and financial analysis, product, and project delivery.",
  "topics": [
    "developer-portfolio",
    "cloud-engineering",
    "platform-engineering",
    "devops",
    "cybersecurity",
    "it-support",
    "data-analytics",
    "business-intelligence",
    "business-analysis",
    "business-analyst",
    "systems-analysis",
    "financial-analysis",
    "product-management",
    "project-management",
    "data-operations",
    "excel",
    "powerbi",
    "python",
    "terraform"
  ]
}
```

**Homepage separately deferred:** `https://jamiechristian22.github.io/` — requires live site confirmation; do not change current homepage yet.

### 2. [`jamiechristian22.github.io`](https://github.com/JamieChristian22/jamiechristian22.github.io) — P0

**Proposed now (not applied):**

```json
{
  "description": "Accessible portfolio website showcasing cloud and IT, cybersecurity, data and BI, business analysis, product, and project delivery case studies.",
  "topics": [
    "portfolio",
    "github-pages",
    "web-development",
    "html",
    "css",
    "javascript",
    "accessibility"
  ]
}
```

**Homepage separately deferred:** `https://jamiechristian22.github.io/` — requires live site confirmation; do not change current homepage yet.

### 3. [`cybersecurity-analyst-portfolio`](https://github.com/JamieChristian22/cybersecurity-analyst-portfolio) — P1

**Proposed now (not applied):**

```json
{
  "description": "Reproducible synthetic SOC investigations with Python, SQLite, security detections, incident response evidence, and automated tests."
}
```

**Homepage:** No change proposed in this batch.

### 4. [`data-analyst-portfolio`](https://github.com/JamieChristian22/data-analyst-portfolio) — P1

**Proposed now (not applied):**

```json
{
  "description": "Five reproducible SQL/Python analytics case studies: SaaS, A/B tests, ecommerce, marketplaces, and user journeys, with validated KPIs and an offline explorer."
}
```

**Homepage:** No change proposed in this batch.

### 5. [`cloud-security-operations-platform`](https://github.com/JamieChristian22/cloud-security-operations-platform) — P1

**Proposed now (not applied):**

```json
{
  "topics": [
    "cloud-security",
    "aws",
    "azure",
    "gcp",
    "iam",
    "terraform",
    "security-operations",
    "devsecops"
  ]
}
```

**Homepage:** No change proposed in this batch.

### 6. [`cloud-support-operations-portfolio`](https://github.com/JamieChristian22/cloud-support-operations-portfolio) — P1

**Proposed now (not applied):**

```json
{
  "topics": [
    "cloud-support",
    "aws",
    "azure",
    "gcp",
    "troubleshooting",
    "incident-response",
    "cloud-operations",
    "networking"
  ]
}
```

**Homepage:** No change proposed in this batch.

### 7. [`product-manager-portfolio`](https://github.com/JamieChristian22/product-manager-portfolio) — P1

**Proposed now (not applied):**

```json
{
  "description": "Six simulated product-management case studies featuring PRDs, user flows, experiments, prioritization, KPI dashboards, and technical decision artifacts.",
  "topics": [
    "product-management",
    "product-discovery",
    "product-strategy",
    "product-analytics",
    "user-stories",
    "ab-testing",
    "roadmapping",
    "case-study"
  ]
}
```

**Homepage:** No change proposed in this batch.

## Remaining backlog

The other 17 proposed change sets stay in [proposed-metadata.json](proposed-metadata.json). They require separate review and approval, including all conditional homepage changes and the misspelled `contruction` project-management topic. All 35 original metadata snapshots remain documented in [AUDIT.md](AUDIT.md).

## How to approve

A safe approval should specify **which repositories** and **which fields** (`description`, `topics`; `homepage` remains held). After approval, verify the live metadata has not changed since this review before any settings edit. An available GitHub repository-settings write action or manual owner action is required to apply these fields; this draft PR cannot apply them.

Do **not** merge this PR as a substitute for approving About metadata changes.
