# Exam Analytics Dashboard

Analyze pre/post exam results, compute gain scores, and identify question difficulty.

## Quick Start

```bash
# From repo root

# 1. Seed demo data
python -m apps.exam_analytics.seed

# 2. Start API (port 8002)
uvicorn apps.exam_analytics.api:app --reload --port 8002

# 3. Start dashboard (port 8502) — in a separate terminal
streamlit run apps/exam_analytics/dashboard.py --server.port 8502
```

## API Docs

With the API running: http://localhost:8002/docs

## CSV Format

**Results CSV** (upload to a session):
```
trainee_id,q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14,q15,q16,q17,q18,q19,q20
1234567890,2,0,2,2,0,2,2,0,2,0,2,2,0,2,2,4,5,3,6,2
```

- q1–q15: MC questions (0 or 2 points)
- q16–q20: SA questions (0–6 points)
- Total possible: 60 points (30 MC + 30 SA)
- POST passing: 70% (42/60)
- PRE exams are automatically marked DIAGNOSTIC

## Gain Score Calculations

- **Absolute gain:** POST% - PRE%
- **Normalized gain:** (POST% - PRE%) / (100% - PRE%) × 100
  - Avoids ceiling effect for high pre-scorers
  - Flagged if below configurable threshold (default 5%)
