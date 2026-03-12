# USAREUR-AF Operational Data Team

```
HEADQUARTERS
UNITED STATES ARMY EUROPE AND AFRICA
Wiesbaden, Germany
```

**Distribution:** Approved for public release; distribution is unlimited.

---

## Repository Overview

This repository contains the Maven Smart System (MSS) training curriculum, data science reference library, and supporting tools for the USAREUR-AF Operational Data Team.

---

## Contents

### [Maven Training Curriculum](maven_training/)

Doctrine-aligned training for all USAREUR-AF personnel who access, build on, or lead with the Maven Smart System. Organized by audience and role.

| Entry Point | Audience |
|---|---|
| [TM-10 — Maven User](maven_training/tm/TM_10_maven_user/TM_10_MAVEN_USER.md) | All personnel — access and consume data |
| [TM-20 — Builder](maven_training/tm/TM_20_builder/TM_20_BUILDER.md) | All staff — no-code building |
| [TM-30 — Advanced Builder](maven_training/tm/TM_30_advanced_builder/TM_30_ADVANCED_BUILDER.md) | Data-adjacent specialists |
| [TM-40 Series](maven_training/README.md#tm-40-series----technical-specialist-tracks) | Technical specialists (ORSA, AI Eng, MLE, PM, KM, SWE) |
| [TM-50 Series](maven_training/README.md#tm-50-series----advanced-specialist-tracks) | Advanced specialist tracks (post-TM-40, per role) |
| [Data Literacy for Senior Leaders](maven_training/doctrine/DATA_LITERACY_senior_leaders.md) | O-5+, CSM+, senior civilians |
| [Data Literacy Technical Reference](maven_training/doctrine/DATA_LITERACY_technical_reference.md) | All personnel (comprehensive reference) |
| [Glossary](maven_training/doctrine/GLOSSARY_data_foundry.md) | All personnel (data ↔ Foundry term translation) |

Full curriculum index: [maven_training/README.md](maven_training/README.md)

---

### [Data Skills Reference Library](data_skills/)

15-module Python curriculum covering the full data engineering and analytics stack. Used as a reference for TM-30/40-level technical work.

| Module | Topic |
|---|---|
| 01–05 | Python, Pandas, SQL, Visualization, Statistics |
| 06–10 | ML, Time Series, ETL Pipelines, Data Quality, End-to-End |
| 11–12 | FastAPI, Testing (pytest) |
| 13 | Foundry Patterns (runnable shim — transforms, ontology, checks) |
| 14–15 | Streamlit Dashboards, Deployment (Docker) |

Activate venv: `source data_skills/.venv/bin/activate`

---

### [SITREP Tracker](sitrep_tracker/)

Applied CLI project demonstrating SQLite, Click, Rich, and DTG utilities. Reference implementation for TM-20/30 pipeline and reporting patterns.

**Install and run:**

```bash
# Option A — install as a package (recommended, works from any directory)
pip install -e .
sitrep --help

# Option B — run directly from the sitrep_tracker/ directory
cd sitrep_tracker/
python3 cli.py --help
```

**Dev setup — restore data_skills symlink** (required after a fresh clone, since `data_skills/` is gitignored):

```bash
ln -sf "$(pwd)/sitrep_tracker" data_skills/projects/sitrep_tracker
```

---

### [Skills Library](skills/)

Third-party Claude Code skill collections organized for operational data work. Includes Anthropic official skills (pdf, xlsx, docx, pptx), engineering skills, scientific/geospatial skills, and PM toolkits.

See [skills/INDEX.md](skills/INDEX.md) for the full catalog and activation instructions.

---

## Deploying the Training Hub to Foundry Workshop

The [MSS Training Hub](maven_training/mss_info_app/index.html) is a self-contained HTML application suitable for hosting in Palantir Foundry Workshop as an embedded module.

### Option A — Embed via Code Repository (recommended)

1. **Push this repository to a Foundry Code Repository** (or sync an existing one).
2. In Foundry, navigate to the code repo and confirm `maven_training/mss_info_app/index.html` is present.
3. Open or create your **Workshop** application in the MSS Foundry environment.
4. Add a new layout panel and insert an **Embed** widget.
5. Set the embed source to the static file URL for `index.html` served from the code repository. The URL follows the pattern:
   ```
   /static/<repo-rid>/maven_training/mss_info_app/index.html
   ```
   Replace `<repo-rid>` with your code repository's resource identifier (visible in the repo's URL bar).
6. Set the panel to **full-height** / **no padding** for the best viewing experience.
7. Save and publish the Workshop application. Assign access via Foundry's permission panel to the appropriate groups (e.g., `usareur-af-mss-users`).

### Option B — Inline HTML widget

Use this if you cannot serve static files from a code repository.

1. Open your Workshop application.
2. Add an **HTML** widget to the canvas.
3. Paste the full contents of `maven_training/mss_info_app/index.html` into the widget's HTML editor.
4. Note: some browsers may restrict inline `<script>` execution depending on the Foundry tenant's Content Security Policy. Test interactivity before publishing.

### Notes

- The HTML file is fully self-contained — no external CDN calls, no server-side dependencies.
- Links within the hub that point to TM markdown files will not resolve inside Workshop. If live document links are needed, host the PDFs as Foundry media objects and update the `href` values in `index.html` before embedding.
- For access control, do not use the Workshop app's sharing URL as a substitute for Foundry group permissions.

---

## Standards

- [Naming and Governance Standards](maven_training/standards/NAMING_AND_GOVERNANCE_STANDARDS.md) — USAREUR-AF MSS naming conventions referenced throughout the TM series

---

## Security

All work in this repository is governed by [CLAUDE.md](CLAUDE.md). Key requirements:
- Do not commit operational data, credentials, or connection strings
- Parameterize all SQL — never f-string queries
- Validate at ingestion boundaries
- Do not push to remote without explicit instruction

---

*USAREUR-AF Operational Data Team — UNCLASSIFIED*
*Version 3.0 | March 2026*
