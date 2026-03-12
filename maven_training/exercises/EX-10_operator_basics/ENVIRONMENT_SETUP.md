# ENVIRONMENT SETUP — EX-10 Operator Basics

## Environment Type
MSS training instance or designated sandbox tenant.

## Required Access
- Training account with standard MSS user permissions (read + export)
- Access to the BCT Readiness project

## Pre-Load Instructions

### 1. Dataset
Load the synthetic BCT readiness dataset into the training environment:
- File: `EX-10_BCT_Readiness_Training_Data.csv` (from training data package)
- Contains: unit field, equipment class, readiness percentage, date, data steward contact
- Three units with distinct readiness profiles: Unit A (~85%), Unit B (~62%), Unit C (~91%)
- Unit B / Motor Pool category should be the clear anomaly (lowest readiness)

### 2. Dashboard
Pre-build or restore the "BCT Readiness — EX-10 Training" Workshop dashboard:
- Line chart: readiness % over time, by unit
- Filter widgets: unit selector, date range
- Metadata panel: data owner, last-updated timestamp (must be visible)
- Data steward contact: populate with training POC name and email (not real OPSDATA contacts)

### 3. Permissions
- All training accounts: Viewer role on the dashboard
- Evaluator account: Editor role (to verify export outputs submitted by participants)
- No participant account should have edit permissions

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
If the dashboard is modified during an exercise, restore from the saved template in:
`[Training MSS project path]/EX-10_template_restore`
