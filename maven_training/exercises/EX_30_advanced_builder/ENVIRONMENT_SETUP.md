# ENVIRONMENT SETUP — EX_30 Advanced Builder

## Environment Type
MSS training instance with Pipeline Builder, Contour, Quiver, and AIP Logic access.

## Required Access

| Account | Role |
|---------|------|
| Training accounts | Pipeline Builder (branch create/edit), Contour viewer, Quiver create, AIP Logic rule editor |
| Evaluator account | Editor on EX_30 project |

## Pre-Load Instructions

### 1. Dataset
Load `EX_30_SIGACT_Analog_Training_Data.csv` (from training data package):

| Field | Type | Notes |
|-------|------|-------|
| `event_id` | string | Primary key |
| `date` | YYYY-MM-DD | 60-day range ending on exercise date |
| `lat` | decimal degrees | WGS84 |
| `lon` | decimal degrees | WGS84 |
| `event_type` | string | IED / Patrol Contact / Observation / Cache / Other |
| `unit` | string | Nullable |

Deliberately include: 5+ duplicate `event_id` rows, 3+ null `unit` values, 2+ null grid coordinates.

Place in: `[Training Project]/EX_30/raw/`

### 2. Contour Configuration
- Coordinate projection: WGS84, decimal degrees (lat/lon columns)
- Load a test record and verify map renders before the exercise
- If projection fails, contact unit data steward for Contour configuration guidance

### 3. AIP Logic
- Confirm AIP Logic rule editor is accessible to training accounts
- Task 5 rule condition: `lat IS NULL OR lon IS NULL` → set `completeness_flag` = "INCOMPLETE"
- Pre-create the `completeness_flag` field in the dataset schema (participants do not modify schema)

### 4. Answer Key

| Item | Value |
|------|-------|
| `unit` null rate | ~5% |
| `lat`/`lon` null rate | ~3% |
| Other field null rates | 0% |
| Duplicate record count | 5 |
| Task 4 high-activity week | [Insert correct week_number — confirm before each exercise run] |

## Environment URL
```
[Insert training MSS tenant URL here]
```

## Known Issues
Contour time filter may require the date field to be explicitly cast as a date type in Pipeline Builder — pre-convert in the dataset if needed.
