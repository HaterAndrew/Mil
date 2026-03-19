# Training Metrics Executive Dashboard

Senior-leader / CG briefing dashboard that aggregates data from all MSS Training apps into a single executive view. Answers four questions: (1) Are we on track? (2) What's at risk? (3) What changed? (4) What do you need from me?

## Quick Start

```bash
# From repo root

# 1. (Optional) Seed other apps first for live data aggregation
python -m apps.readiness_tracker.seed
python -m apps.exam_analytics.seed
python -m apps.aar_aggregator.seed
python -m apps.progress_tracker.seed
python -m apps.mtt_scheduler.seed
python -m apps.data_quality.seed
python -m apps.instructor_manager.seed
python -m apps.enrollment_manager.seed

# 2. Seed this dashboard (generates historical snapshots)
python -m apps.training_metrics.seed

# 3. Start API (port 8015)
uvicorn apps.training_metrics.api:app --reload --port 8015

# 4. Start dashboard (port 8515) — in a separate terminal
streamlit run apps/training_metrics/dashboard.py --server.port 8515
```

## API Docs

With the API running: http://localhost:8015/docs

## Notes

- This is a READ-ONLY aggregation dashboard with no training data of its own
- Most useful when other apps are seeded first; falls back to synthetic data otherwise
- The `.db` file stores only snapshot history and is gitignored
- Briefing export uses BLUF (Bottom Line Up Front) format per Army writing standards
