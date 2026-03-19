# Instructor Certification Manager

Track instructor certifications, course coverage, expiration alerts, and teaching workload for MSS Training.

Supports the FACULTY_DEVELOPMENT_PLAN and INSTRUCTOR_OVERVIEW documents.

## Quick Start

```bash
# From repo root

# 1. Seed demo data
python -m apps.instructor_manager.seed

# 2. Start API (port 8011)
uvicorn apps.instructor_manager.api:app --reload --port 8011

# 3. Start dashboard (port 8511) — in a separate terminal
streamlit run apps/instructor_manager/dashboard.py --server.port 8511
```

## API Docs

With the API running: http://localhost:8011/docs

## Dashboard Tabs

1. **Instructor Overview** — KPIs, full roster with cert counts
2. **Course Coverage Matrix** — RAG heatmap of instructor coverage per course
3. **Expiration Tracker** — Certs expiring in 30/60/90 days
4. **Instructor Detail** — Search by name, view certs and teaching history
5. **Teaching Workload** — Events per instructor (90d), overload flags

## Notes

- The `.db` file is gitignored and never committed
- RAG coverage: GREEN >= 3 certified, AMBER >= 1, RED = 0 (gap)
- Overload threshold: > 5 teaching events in 90 days
