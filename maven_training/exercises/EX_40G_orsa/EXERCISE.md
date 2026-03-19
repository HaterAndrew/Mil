# EX_40G — ORSA
## Practical Exercise — TM-40G Proficiency

| | |
|---|---|
| **Version** | 1.0 — March 2026 |
| **Prerequisite** | TM-30 REQUIRED; TM-40G (and TM-10 through TM-20) |
| **Duration** | 3–4 hours |
| **Environment** | MSS with Python Transforms enabled; Quiver and Contour access — see ENVIRONMENT_SETUP.md |

## COMPANION RESOURCES

| Resource | Reference |
|----------|-----------|
| Technical Manual | TM-40G — ORSA |
| Syllabus | SYLLABUS_TM40G |
| Pre-Exercise Exam | EXAM_TM40G_PRE |
| Post-Exercise Exam | EXAM_TM40G_POST |
| Continuation Track | TM-50G — Advanced ORSA |

## WFF AWARENESS

This exercise produces analytical products (forecasts, dashboards) that directly support WFF track personnel (TM-40A–F Intelligence, Fires, Movement & Maneuver, Sustainment, Protection, Mission Command) as end-users and consumers. Evaluators should assess whether outputs are formatted for non-ORSA audiences — a key specialist competency.

## SCENARIO

The G3 wants a readiness forecast for the next 30 days based on historical maintenance cycle data for a training brigade (synthetic). Produce: a descriptive analysis of current state, a regression-based forecast, and a commander's summary dashboard.

Training dataset: synthetic PMCS/maintenance cycle data, 180 days, 3 battalions, 4 equipment classes.

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

## EVALUATOR NOTES

**Scoring:** 4 tasks. Go on 3 of 4 = overall Go. No-Go on Task 3 = automatic No-Go.

**Pre-exercise checklist:**
- Confirm Python Transforms are enabled for training accounts
- Confirm training accounts have access to the synthetic PMCS dataset
- Confirm evaluator can read participant Python Transform code (Viewer access to the build environment)
- Know the expected trend direction for each battalion from the answer key in ENVIRONMENT_SETUP.md

**Common failure modes:**

| Task | Common Failure | Evaluator Guidance |
|------|---------------|--------------------|
| Task 1 | Standard deviation reported but not interpreted | Stats present = Go; interpretation absent = coaching note only |
| Task 2 | Trend direction wrong for one battalion | Battalion C has a non-obvious degrading trend obscured by noise; accept "stable" if participant explains the reasoning |
| Task 3 | R² reported from training set not test set | Ask: "How did you partition your data?" — if no train/test split, No-Go |
| Task 3 | Poor-fit battalion not flagged | Check whether R² < 0.5 for Battalion B (it should be) — failure to flag is No-Go |
| Task 4 | Dashboard uses statistical notation without plain-language explanation | Evaluate against "can a CSM understand this without asking" — if not, No-Go |

**Timing notes:**
- Task 3 is the time sink — budget 75 min total if participant needs to set up the Python Transform environment for the first time
- Task 4 is often underestimated; participants who produce clean visualizations in Tasks 2–3 may still spend 45 min on dashboard layout
- If participant uses R instead of Python for Task 3, that is acceptable — verify R is enabled in the Transform environment

## NEXT STEPS

Participants who receive an overall Go on EX_40G are eligible to enroll in **TM-50G — Advanced ORSA**. TM-50G extends this exercise's competencies into time-series modeling, multi-source fusion, and senior-leader analytical support. TM-50 is G–M only (advanced specialist tracks).
