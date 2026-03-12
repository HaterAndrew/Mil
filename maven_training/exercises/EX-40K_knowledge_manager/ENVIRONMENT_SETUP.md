# ENVIRONMENT SETUP — EX-40K Knowledge Manager

## Environment Type

MSS training instance with Workshop form builder, Pipeline Builder, and AIP Logic access.

## Required Access

| Account | Permissions Required |
|---------|---------------------|
| Training accounts | Workshop create/publish, Pipeline Builder create/edit, lessons learned dataset write access |
| Evaluator account | Viewer on submitted Workshop applications |

## Pre-Load Instructions

### 1. Synthetic AAR Documents

| Attribute | Value |
|-----------|-------|
| Package | `EX-40K_AAR_Backlog/` directory (20 .txt or structured records) from training data package |
| Destination | `[Training Project]/EX-40K/source/` |

Each record fields: `date`, `unit`, `exercise_name`, `category` (pre-labeled for evaluator reference), `observation` (free text), `recommendation` (free text), `priority` (H/M/L)

### 2. Conflicting Recommendations (Task 4)

The dataset MUST contain at least 2 records with conflicting recommendations on the same topic.

**Pre-planted conflict:**

| Record | Topic | Recommendation |
|--------|-------|---------------|
| Record #7 | Radio frequency deconfliction during joint operations | Assign frequency blocks by echelon in the OPORD; do not allow ad hoc coordination |
| Record #14 | Radio frequency deconfliction during joint operations | Allow battalion S6 to coordinate directly with adjacent units for faster deconfliction |

These directly conflict. The preferred recommendation (for evaluator grading) is **Record #7** (doctrinal, avoids fratricide risk). Do not tell participants which records conflict — they must find it.

### 3. Lessons Learned Dataset Schema

Pre-create the target dataset with the following schema (empty — participant populates):

| Field | Type | Notes |
|-------|------|-------|
| `submission_date` | Date | |
| `unit` | String | |
| `exercise_name` | String | |
| `category` | String (constrained) | Evaluator checks form enforcement |
| `observation` | String | |
| `recommendation` | String | |
| `opr` | String | |
| `priority` | String | H/M/L |
| `source` | String | manual/form/ingested |

Destination: `[Training Project]/EX-40K/lessons_learned/`

### 4. Taxonomy — 6-Category Controlled Vocabulary

Participants must use these exact category values:

1. `COMMAND_AND_CONTROL`
2. `SUSTAINMENT`
3. `FIRES`
4. `INTELLIGENCE`
5. `MOVEMENT_AND_MANEUVER`
6. `PROTECTION`

## Environment URL

```
[Insert training MSS tenant URL here]
```

## Answer Key

| Item | Value |
|------|-------|
| Task 4 conflicting records | #7 and #14 (radio frequency deconfliction) |
| Preferred recommendation | Record #7 (echelon-assigned frequency blocks per OPORD) |
