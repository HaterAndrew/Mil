# ENVIRONMENT SETUP — EX-40G ORSA

## Environment Type
MSS with Python Transforms (or R Transforms) enabled, Quiver and Contour access, Workshop build permissions.

## Required Access
- Training accounts: Python Transform create/edit, Quiver create, Workshop create/publish
- Evaluator account: Viewer on participant Transform builds (to review code and metrics)

## Pre-Load Instructions

### 1. Dataset
Load synthetic PMCS/maintenance cycle data:
- File: `EX-40G_PMCS_Training_Data.csv` (from training data package)
- Schema: `date` (YYYY-MM-DD), `battalion` (A/B/C), `equipment_class` (wheeled/tracked/aviation/comms), `readiness_pct` (float 0-100)
- Date range: 180 days of daily records
- Designed trends:
  - Battalion A: steady improving trend (~+0.3%/week)
  - Battalion B: flat with high variance (poor model fit — R² expected < 0.5)
  - Battalion C: slow degrading trend obscured by noise (~-0.2%/week)
- Place in: `[Training Project]/EX-40G/source/`

### 2. Python/R Transform Environment
- Python ≥ 3.9 with packages: pandas, numpy, scikit-learn, matplotlib/plotly
- If R is available: tidyverse, forecast, broom
- Confirm participants can import these packages without admin intervention

### 3. Answer Key
- Task 1 highest-variance equipment class: **aviation** (verify from dataset before each exercise)
- Task 2 trend directions: Battalion A = improving, Battalion B = stable/flat, Battalion C = degrading
- Task 3 poor-fit battalion: **Battalion B** (R² expected ~0.15–0.30 depending on model choice)

## Environment URL
```
[Insert training MSS tenant URL here]
```

## Notes
- Participants should not have access to the answer key during the exercise
- If Battalion trend values shift due to data regeneration, update the answer key above before use
