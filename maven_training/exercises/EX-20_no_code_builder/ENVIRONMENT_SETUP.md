# ENVIRONMENT SETUP — EX-20 No-Code Builder

## Environment Type
MSS training instance with Pipeline Builder and Workshop build permissions enabled.

## Required Access
- Training accounts: Pipeline Builder create/edit, Workshop create/publish
- Dataset: read access to EX-20 source dataset

## Pre-Load Instructions

### 1. Dataset
Load synthetic vehicle availability data:
- File: `EX-20_Vehicle_Availability_Training_Data.csv` (from training data package)
- Schema: `date` (YYYY-MM-DD), `company` (A/B/C/D), `vehicle_class` (wheeled/tracked), `availability_pct` (float 0-100)
- Date range: 90 days ending on the exercise date (regenerate if exercise date changes significantly)
- Place in project: `[Training Project]/EX-20/source/`

### 2. Permissions
- Training accounts: Viewer on source dataset, Builder on the EX-20 project folder
- Training accounts must NOT have publisher rights on the production project
- Evaluator account: Editor on EX-20 project (to review submitted dashboards)

### 3. Naming Standards Reference
Ensure `NAMING_AND_GOVERNANCE_STANDARDS.md` is accessible to trainees during the exercise.

The expected output dataset name following standards: `[UNIT]-EX20-VehicleAvailability-[YYYYMMDD]`
(Accept reasonable variations that follow the standard conventions — hyphen-separated, unit prefix, date suffix.)

## Environment URL
```
[Insert training MSS tenant URL here]
```

## Evaluator Verification Checklist
After participant submits:
- [ ] Output dataset exists and has correct schema (date, company, avg_availability)
- [ ] Row count matches expected (30 days × 4 companies = 120 rows)
- [ ] Dashboard renders chart with 4 company series
- [ ] Company filter widget affects chart display
- [ ] Last-updated widget is present
- [ ] Evaluator account has Viewer (not Editor) access to the published dashboard
