# EX-40A — ORSA
## Practical Exercise — TM-40A Proficiency

**Version 1.0 | March 2026**
**Prerequisite:** TM-40A, ORSA Technical Manual (and TM-10 through TM-30)
**Duration:** 3–4 hours
**Environment:** MSS with Python Transforms enabled; Quiver and Contour access (see ENVIRONMENT_SETUP.md)

---

## SCENARIO

The G3 wants a readiness forecast for the next 30 days based on historical maintenance cycle data for a training brigade (synthetic). You are the ORSA. Produce: a descriptive analysis of current state, a regression-based forecast, and a commander's summary dashboard.

**Training dataset:** Synthetic PMCS/maintenance cycle data, 180 days, 3 battalions, 4 equipment classes.

---

## TASK LIST

### Task 1 — Descriptive Analysis (45 min)
- [ ] Compute mean, median, and standard deviation of readiness percentage per battalion per equipment class
- [ ] Identify the equipment class with the highest variance
- [ ] Produce a summary table suitable for a commander's brief (clean labels, no raw code output)
- **Go:** Statistics are correct; high-variance class identified; table is brief-ready
- **No-Go:** Statistical errors or output is not brief-ready

### Task 2 — Trend Analysis (30 min)
- [ ] Plot readiness trend over time per battalion (line chart in Quiver or Python/plotly)
- [ ] Annotate any clear inflection points (maintenance surges, drops)
- [ ] Identify whether the trend is improving, stable, or degrading for each battalion
- **Go:** Correct trend direction identified for each battalion; inflection points annotated
- **No-Go:** Trend direction wrong for any battalion

### Task 3 — Regression Forecast (60 min)
- [ ] Build a linear regression model (Python Transform) forecasting readiness 30 days out per battalion
- [ ] Report R², RMSE, and a plain-language confidence statement
- [ ] Flag any battalion where the model fit is poor (R² < 0.5) and explain the limitation
- **Go:** Forecast runs; R²/RMSE reported; poor-fit battalions flagged with explanation
- **No-Go:** Forecast errors or metrics not reported

### Task 4 — Commander's Dashboard (45 min)
- [ ] Build a Workshop dashboard with: current readiness summary table, trend chart, and 30-day forecast line
- [ ] Add a data quality note (source, last updated, known limitations)
- [ ] Ensure the dashboard is readable at the O-5/CSM level — no statistical jargon without explanation
- **Go:** All three components present; data quality note visible; jargon-free for senior audience
- **No-Go:** Missing component or dashboard requires statistical background to interpret

---

## EVALUATOR NOTES

> **TODO:** Complete after dry run. Confirm Python Transform environment is configured. Task 3 is the critical gate — confirm evaluator can review model code and metrics.

Scoring: 4 tasks. Go on 3 of 4 = overall Go. No-Go on Task 3 = automatic No-Go.

---

## ENVIRONMENT SETUP

> **TODO:** Pre-load synthetic PMCS dataset. Enable Python Transforms for training accounts. Document in `ENVIRONMENT_SETUP.md`.
