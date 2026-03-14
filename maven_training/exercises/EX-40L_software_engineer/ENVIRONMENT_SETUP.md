# ENVIRONMENT SETUP — EX-40L Software Engineer

**Track:** EX-40L — Software Engineer (TM-40L) | **Prerequisite:** TM-30 REQUIRED | **Continuation:** TM-50L — Advanced Software Engineer
**Companion exams:** EXAM_TM40L_PRE (administer before exercise), EXAM_TM40L_POST (administer after exercise)

## Environment Type

MSS with Python Transforms, TypeScript/OSDK Code Workspace, and Ontology edit access.

## Required Access

| Account | Permissions Required |
|---------|---------------------|
| Training accounts | Python Transform create/edit, TypeScript Code Workspace, Ontology Object Type create/edit |
| Account A (data-steward group) | Authorized user for Task 4 testing |
| Account B (not in data-steward group) | Unauthorized user for Task 4 testing |
| Evaluator account | Viewer on all participant Transform builds and Action definitions |

## Pre-Load Instructions

### 1. Dataset

Load synthetic personnel readiness feed:

| Attribute | Value |
|-----------|-------|
| File | `EX-40L_Personnel_Readiness_Feed.csv` (from training data package) |
| Row count | ~1,000 records |
| Destination | `[Training Project]/EX-40L/source/` |

**Schema:** `personnel_id` (string, primary key), `unit` (string, some with trailing spaces), `readiness_status` (READY/PARTIALLY_READY/NOT_READY), `last_updated` (ISO8601 date), `equipment_assigned` (int, some nulls), `medical_flag` (boolean)

**Deliberate data quality issues:**
- ~50 records with validation failures (null `personnel_id`, invalid status values, unparseable dates)
- Mixed-case unit names

### 2. Ontology Setup

Pre-create in the training Ontology:

| Element | Configuration |
|---------|--------------|
| Object Type | `PersonnelRecord` |
| Properties | `personnel_id` (string, primary key), `unit` (string), `readiness_status` (string), `record_hash` (string), `ingested_at` (timestamp) |
| Permission | Training accounts must have permission to write to this Object Type |

### 3. Authorization Groups

| Action | Detail |
|--------|--------|
| Create group | `data-steward` in the training tenant |
| Account A | Add to `data-steward` group |
| Account B | Do NOT add to `data-steward` group |
| Credentials | Share both account credentials with the evaluator for Task 4 testing |

### 4. OSDK / TypeScript

- [ ] Confirm OSDK Python SDK is installed: `pip install foundry-osdk` (or equivalent)
- [ ] Confirm OSDK TypeScript SDK is available in the Code Workspace
- [ ] Confirm the `PersonnelRecord` Object Type is exported to the OSDK namespace before the exercise

## Environment URL

```
[Insert training MSS tenant URL here]
```

## Idempotency Verification (Task 1)

After participant claims idempotency:

1. Note the output dataset row count after first run
2. Trigger a second run without modifying the source
3. Compare row counts — must be identical
4. Check that error dataset row count is also identical between runs

## Notes

- OSDK TypeScript Actions require the Action type to be defined in the Ontology before writing code — confirm the `UpdateReadinessStatus` Action type exists with the correct parameters before the exercise
- If TypeScript environment setup takes > 45 min, allow participant to stub the authorization logic in Python instead, noting the deviation on the evaluation form
