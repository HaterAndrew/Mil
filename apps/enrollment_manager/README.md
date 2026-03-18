# Enrollment Manager

Manage class enrollment, seat allocation, waitlists, and rosters for scheduled MSS training events. Complements the MTT Scheduler (event scheduling) and ENROLLMENT_SOP (doctrine).

## Quick Start

```bash
# From repo root

# 1. Seed demo data
python -m apps.enrollment_manager.seed

# 2. Start API (port 8012)
uvicorn apps.enrollment_manager.api:app --reload --port 8012

# 3. Start dashboard (port 8512) — in a separate terminal
streamlit run apps/enrollment_manager/dashboard.py --server.port 8512
```

## API Docs

With the API running: http://localhost:8012/docs

## Features

- **Seat allocation**: auto-assigns seat numbers on enrollment
- **Auto-waitlist**: when a class is full, new enrollments go to waitlist
- **Waitlist promotion**: promote top-priority waitlisted students when seats open
- **Student lookup**: find all enrollments for a given DODID
- **CSV export**: download full enrollment data

## Notes

- DODID is PII — the `.db` file is gitignored and never committed
- Waitlist priority: higher number = higher priority; ties broken by request date (FIFO)
