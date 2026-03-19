# Training Readiness Tracker

Track soldier/unit completion across the MSS TM-10 → TM-50L prereq chain.

## Quick Start

```bash
# From repo root

# 1. Seed demo data
python -m apps.readiness_tracker.seed

# 2. Start API (port 8001)
uvicorn apps.readiness_tracker.api:app --reload --port 8001

# 3. Start dashboard (port 8501) — in a separate terminal
streamlit run apps/readiness_tracker/dashboard.py --server.port 8501
```

## API Docs

With the API running: http://localhost:8001/docs

## CSV Formats

**Roster CSV:**
```
dodid,last_name,first_name,rank,unit,mos
1234567890,KELLY,JAMES,SGT,2-1 BN,17C
```

**Completions CSV:**
```
dodid,course_id,result,evaluation_date,evaluator_name
1234567890,TM-10,GO,2026-01-15,MAJ SMITH
```

## Notes

- DODID is PII — the `.db` file is gitignored and never committed
- Prereq enforcement is **hard**: cannot record a GO for TM-40 without TM-30 GO
- FBC is a parallel track off TM-20; does NOT satisfy TM-30 prereq
