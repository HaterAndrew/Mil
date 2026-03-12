# ENVIRONMENT SETUP — EX-30 Advanced Builder

## Environment Type
MSS training instance with Pipeline Builder, Contour, Quiver, and AIP Logic access.

## Required Access
- Training accounts: Pipeline Builder (branch create/edit), Contour viewer, Quiver create, AIP Logic rule editor

## Pre-Load Instructions

### 1. Dataset
Load synthetic SIGACT-analog event data:
- File: `EX-30_SIGACT_Analog_Training_Data.csv` (from training data package)
- Schema: `event_id` (string, primary key), `date` (YYYY-MM-DD), `lat` (decimal degrees), `lon` (decimal degrees), `event_type` (one of: IED/Patrol Contact/Observation/Cache/Other), `unit` (nullable)
- Deliberately include: 5+ duplicate event_id rows, 3+ null unit values, 2+ null grid coordinates
- Date range: 60 days ending on exercise date
- Place in: `[Training Project]/EX-30/raw/`

### 2. Contour Configuration
- Coordinate projection: WGS84, decimal degrees (lat/lon columns)
- Confirm Contour can render points from this dataset before the exercise
- Load a test record and verify map renders correctly
- If projection fails, see unit data steward for Contour configuration guidance

### 3. AIP Logic
- Confirm AIP Logic rule editor is accessible to training accounts
- The rule in Task 5 should use a simple condition: `grid IS NULL` → set flag field to "INCOMPLETE"
- Pre-create the flag field (`completeness_flag`) in the dataset schema so participants don't need to modify schema

### 4. Answer Key
- Task 1 expected null rates: `unit`: ~5%, `grid (lat/lon)`: ~3%, all other fields: 0%
- Duplicate record count: 5
- Task 4 high-activity week: [Insert correct week_number from dataset — confirm before each exercise run]

## Environment URL
```
[Insert training MSS tenant URL here]
```

## Known Issues
- Contour time filter may require the date field to be explicitly cast as a date type in Pipeline Builder — pre-convert in the dataset if needed
