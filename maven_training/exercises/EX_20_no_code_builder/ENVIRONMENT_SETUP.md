# ENVIRONMENT SETUP — EX_20 No-Code Builder

## Environment Type
MSS training instance with Pipeline Builder and Workshop build permissions enabled.

## Required Access

| Account | Role |
|---------|------|
| Training accounts | Viewer on source dataset; Builder on EX_20 project folder |
| Evaluator account | Editor on EX_20 project (to review submitted dashboards) |

Training accounts must NOT have publisher rights on the production project.

## Pre-Load Instructions

### 1. Dataset
Load `EX_20_Vehicle_Availability_Training_Data.csv` (from training data package):

| Field | Type | Values |
|-------|------|--------|
| `date` | YYYY-MM-DD | 90-day range ending on exercise date |
| `company` | string | A, B, C, D |
| `vehicle_class` | string | wheeled, tracked |
| `availability_pct` | float | 0–100 |

Place in: `[Training Project]/EX_20/source/`

Regenerate date range if exercise date changes significantly.

### 2. Naming Standards Reference
Ensure NAMING_AND_GOVERNANCE_STANDARDS.md is accessible to trainees during the exercise.

Expected output dataset name: `[UNIT]-EX20-VehicleAvailability-[YYYYMMDD]`
Accept reasonable variations that follow conventions (hyphen-separated, unit prefix, date suffix).

## Environment URL
```
[Insert training MSS tenant URL here]
```

## Evaluator Verification Checklist
After participant submits:
- [ ] Output dataset exists with correct schema: `date`, `company`, `avg_availability`
- [ ] Row count matches expected: 30 days × 4 companies = 120 rows
- [ ] Dashboard renders chart with 4 company series
- [ ] Company filter widget affects chart display
- [ ] Last-updated widget is present
- [ ] Evaluator account has Viewer (not Editor) access to the published dashboard
