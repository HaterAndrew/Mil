# Curriculum Tracker

Track curriculum document versions, review cycles, and content freshness across the maven_training/ corpus. Supports the CURRICULUM_MAINTENANCE_SOP.

## Quick Start

```bash
# From repo root

# 1. Seed demo data (scans real maven_training/ directory)
python -m apps.curriculum_tracker.seed

# 2. Start API (port 8013)
uvicorn apps.curriculum_tracker.api:app --reload --port 8013

# 3. Start dashboard (port 8513) — in a separate terminal
streamlit run apps/curriculum_tracker/dashboard.py --server.port 8513
```

## API Docs

With the API running: http://localhost:8013/docs

## Key Features

- **Directory scanning** — hashes all .md files in maven_training/, detects new/changed/unchanged
- **Review tracking** — SCHEDULED, AD_HOC, POST_EXERCISE review cycles with status tracking
- **Freshness reporting** — avg days since last review by document type
- **Change history** — SHA-256-based change detection with full audit trail
- **Stale document alerts** — flags docs not reviewed in N days (default 90)

## Notes

- The `.db` file is gitignored and never committed
- Scan uses SHA-256 to detect content changes independent of file timestamps
- Document types auto-classified from file paths: TM, SYLLABUS, EXERCISE, EXAM, DOCTRINE, ADMIN
