# ENVIRONMENT SETUP — EX-40G ORSA

**Track:** EX-40G — ORSA (TM-40G) | **Prerequisite:** TM-30 REQUIRED | **Continuation:** TM-50G — Advanced ORSA
**Companion exams:** EXAM_TM40G_PRE (administer before exercise), EXAM_TM40G_POST (administer after exercise)

## Environment Type
MSS with Python Transforms (or R Transforms) enabled, Quiver and Contour access, Workshop build permissions.

## Required Access

| Account | Role |
|---------|------|
| Training accounts | Python Transform create/edit, Quiver create, Workshop create/publish |
| Evaluator account | Viewer on participant Transform builds (to review code and metrics) |

## Pre-Load Instructions

### 1. Dataset
Load `EX-40G_PMCS_Training_Data.csv` (from training data package):

| Field | Type | Notes |
|-------|------|-------|
| `date` | YYYY-MM-DD | 180-day range of daily records |
| `battalion` | string | A, B, C |
| `equipment_class` | string | wheeled, tracked, aviation, comms |
| `readiness_pct` | float | 0–100 |

Designed trends:

| Battalion | Trend | Notes |
|-----------|-------|-------|
| A | Improving | ~+0.3%/week |
| B | Flat/stable | High variance; poor model fit — R² expected < 0.5 |
| C | Degrading | ~−0.2%/week, obscured by noise |

Place in: `[Training Project]/EX-40G/source/`

### 2. Python/R Transform Environment
- Python ≥ 3.9 with packages: `pandas`, `numpy`, `scikit-learn`, `matplotlib`/`plotly`
- If R is available: `tidyverse`, `forecast`, `broom`
- Confirm participants can import these packages without admin intervention

### 3. Answer Key

| Item | Answer |
|------|--------|
| Task 1 highest-variance equipment class | **aviation** (verify from dataset before each exercise run) |
| Task 2 trend directions | A = improving, B = stable/flat, C = degrading |
| Task 3 poor-fit battalion | **Battalion B** (R² expected ~0.15–0.30 depending on model) |

## Environment URL
```
[Insert training MSS tenant URL here]
```

## Notes
- Participants should not have access to the answer key during the exercise
- If Battalion trend values shift due to data regeneration, update the answer key above before use
