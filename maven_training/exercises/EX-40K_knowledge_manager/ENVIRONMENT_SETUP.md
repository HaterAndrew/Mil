# ENVIRONMENT SETUP — EX-40K Knowledge Manager

## Environment Type
MSS training instance with Workshop form builder, Pipeline Builder, and AIP Logic access.

## Required Access
- Training accounts: Workshop create/publish, Pipeline Builder create/edit, lessons learned dataset write access
- Evaluator account: Viewer on submitted Workshop applications

## Pre-Load Instructions

### 1. Synthetic AAR Documents
Prepare 20 synthetic after-action reports:
- File: `EX-40K_AAR_Backlog/` directory (20 .txt or structured records) from training data package
- Each record fields: `date`, `unit`, `exercise_name`, `category` (pre-labeled for evaluator reference), `observation` (free text), `recommendation` (free text), `priority` (H/M/L)
- Place in: `[Training Project]/EX-40K/source/`

### 2. Conflicting Recommendations (Task 4)
The dataset MUST contain at least 2 records with conflicting recommendations on the same topic.
Pre-planted conflict:
- Records #7 and #14 both address **radio frequency deconfliction during joint operations**
  - Record #7 recommendation: "Assign frequency blocks by echelon in the OPORD; do not allow ad hoc coordination"
  - Record #14 recommendation: "Allow battalion S6 to coordinate directly with adjacent units for faster deconfliction"
- These directly conflict; the preferred recommendation (for evaluator grading) is **Record #7** (doctrinal, avoids fratricide risk)
- Do not tell participants which records conflict; they must find it

### 3. Lessons Learned Dataset Schema
Pre-create the target dataset with the following schema (empty, participant populates):
- Fields: `submission_date`, `unit`, `exercise_name`, `category` (string, constrained — evaluator checks form), `observation`, `recommendation`, `opr`, `priority`, `source` (manual/form/ingested)
- Place in: `[Training Project]/EX-40K/lessons_learned/`

### 4. Taxonomy (6-Category Controlled Vocabulary)
The 6 category values participants must use:
1. COMMAND_AND_CONTROL
2. SUSTAINMENT
3. FIRES
4. INTELLIGENCE
5. MOVEMENT_AND_MANEUVER
6. PROTECTION

## Environment URL
```
[Insert training MSS tenant URL here]
```

## Answer Key
- Task 4 conflicting records: #7 and #14 (radio frequency deconfliction)
- Preferred recommendation: Record #7 (echelon-assigned frequency blocks per OPORD)
