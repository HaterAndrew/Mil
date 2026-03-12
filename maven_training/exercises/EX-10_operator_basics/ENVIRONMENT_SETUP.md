# ENVIRONMENT SETUP — EX-10 Operator Basics

## Environment Type
MSS training instance or designated sandbox tenant.

## Required Access

| Account | Role |
|---------|------|
| Training accounts | Viewer (read + export) on BCT Readiness project |
| Evaluator account | Editor (to verify export outputs) |

## Pre-Load Instructions

### 1. Dataset
Load `EX-10_BCT_Readiness_Training_Data.csv` (from training data package):

| Field | Description |
|-------|-------------|
| `unit` | Unit identifier |
| `equipment_class` | Equipment category |
| `readiness_pct` | Readiness percentage |
| `date` | Report date |
| `data_steward_contact` | Steward name and email |

- Three units: Unit A (~85%), Unit B (~62%), Unit C (~91%)
- Unit B / Motor Pool is the designed anomaly (lowest readiness)

### 2. Dashboard
Pre-build or restore "BCT Readiness — EX-10 Training" Workshop dashboard:
- Line chart: readiness % over time, by unit
- Filter widgets: unit selector, date range
- Metadata panel: data owner and last-updated timestamp (must be visible)
- Data steward contact: populate with training POC name and email (not real OPSDATA contacts)

No participant account should have edit permissions.

## Environment URL
```
[Insert training MSS tenant URL here — obtain from unit data steward]
```

## Answer Key (Task 3)
- Lowest readiness unit: **Unit B**
- Driving equipment category: **Motor Pool (wheeled vehicles)**
- Data steward contact: [Insert training POC]

## Evaluator Account
```
Username: [evaluator training account]
Password: [obtain from training coordinator — do not store in this file]
```

## Restore Instructions
If the dashboard is modified during an exercise, restore from:
`[Training MSS project path]/EX-10_template_restore`
