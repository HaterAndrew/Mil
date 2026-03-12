# EX-20 — No-Code Builder
## Practical Exercise — TM-20 Proficiency

**Version 1.0 | March 2026**
**Prerequisite:** TM-20, No-Code Builder Technical Manual (and TM-10)
**Duration:** 90–120 minutes
**Environment:** MSS training instance with workshop build permissions (see ENVIRONMENT_SETUP.md)

---

## SCENARIO

Your battalion S6 has asked you to build a simple Workshop dashboard showing daily vehicle availability by company for the past 30 days. A raw dataset has been pre-loaded into the training MSS environment. You must ingest it, build a basic pipeline, and produce a usable dashboard — no code required.

**Training dataset:** Synthetic vehicle readiness data, LOGSTAT-format, 90 days, 4 companies.

---

## TASK LIST

### Task 1 — Locate and Preview the Dataset (15 min)
- [ ] Find the pre-loaded dataset: "EX-20 Vehicle Availability Training Data"
- [ ] Preview the schema — identify date field, unit field, and availability percentage field
- [ ] Note any obvious data quality issues (nulls, unexpected values)
- **Go:** Correctly identifies all three fields; notes at least one quality observation
- **No-Go:** Cannot locate dataset or misidentifies schema fields

### Task 2 — Build a Pipeline Transform (30 min)
- [ ] Create a new Pipeline Builder transform
- [ ] Filter to the last 30 days using the date field
- [ ] Group by company, aggregate average availability per day
- [ ] Output to a new dataset named per governance standards (see NAMING_AND_GOVERNANCE_STANDARDS.md)
- **Go:** Transform runs successfully; output dataset contains correct columns and row count
- **No-Go:** Transform fails or output schema is incorrect

### Task 3 — Build a Workshop Dashboard (30 min)
- [ ] Create a new Workshop application
- [ ] Add a line chart: x-axis = date, y-axis = avg availability, series = company
- [ ] Add a filter widget for company selection
- [ ] Add a last-updated text widget
- **Go:** Dashboard renders with chart and functional filter; last-updated timestamp visible
- **No-Go:** Chart does not render or filter has no effect

### Task 4 — Publish and Share (15 min)
- [ ] Set the dashboard to read-only for your training cohort group
- [ ] Share the link with your evaluator
- [ ] Confirm the evaluator can view without edit permissions
- **Go:** Evaluator can open and view; cannot edit
- **No-Go:** Evaluator cannot access or has unintended edit permissions

---

## EVALUATOR NOTES

> **TODO:** Complete after dry run. Confirm dataset is pre-loaded and permissions are correct. Note timing — Task 2 commonly runs long for first-time builders.

Scoring: 4 tasks. Go on 3 of 4 = overall Go. No-Go on Task 2 = automatic No-Go (core build competency).

---

## ENVIRONMENT SETUP

> **TODO:** Pre-load synthetic vehicle availability dataset into training MSS environment. Assign build permissions to training accounts. Document environment URL and dataset path in `ENVIRONMENT_SETUP.md`.
