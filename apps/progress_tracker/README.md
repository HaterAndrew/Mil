# Progress Tracker

Track individual training timelines, flag stalled progression, generate training records.

## Quick Start

```bash
# From repo root

# 1. Seed readiness_tracker first (if not already done)
python -m apps.readiness_tracker.seed

# 2. Seed progress tracker demo data
python -m apps.progress_tracker.seed

# 3. Start API (port 8004)
uvicorn apps.progress_tracker.api:app --reload --port 8004

# 4. Start dashboard (port 8504) — in a separate terminal
streamlit run apps/progress_tracker/dashboard.py --server.port 8504
```

## API Docs

With the API running: http://localhost:8004/docs

## Notes

- Depends on readiness_tracker DB for soldier roster and completion data
- DODID is PII — the `.db` file is gitignored and never committed
- Milestones are auto-flagged OVERDUE/AT_RISK based on target_date vs today
- Stalled soldiers query uses readiness_tracker completion history
