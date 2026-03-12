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

**Scoring:** 4 tasks. Go on 3 of 4 = overall Go. No-Go on Task 2 = automatic No-Go (core build competency).

**Pre-exercise checklist:**
- Confirm "EX-20 Vehicle Availability Training Data" dataset is visible to training accounts
- Verify training accounts have Pipeline Builder and Workshop build permissions
- Confirm naming standards reference is accessible ([NAMING_AND_GOVERNANCE_STANDARDS.md](../../standards/NAMING_AND_GOVERNANCE_STANDARDS.md))

**Common failure modes:**

| Task | Common Failure | Evaluator Guidance |
|------|---------------|--------------------|
| Task 1 | Cannot locate dataset | Direct participant to the training project folder — one prompt is allowed without penalty |
| Task 2 | Output dataset name does not follow naming standards | Mark as No-Go; cite specific standard violated; coach after evaluation |
| Task 2 | Transform runs but row count is wrong | Verify the 30-day filter is applied correctly; common error is off-by-one on date boundary |
| Task 3 | Filter widget present but has no effect on chart | This is a wiring issue (widget not connected to chart variable) — automatic No-Go; very common first-time failure |
| Task 4 | Evaluator has edit access | Participant shared with wrong role; mark Task 4 No-Go, note the specific sharing error |

**Timing notes:**
- Task 2 is the critical path — budget up to 45 min for participants with no prior Pipeline Builder experience
- Task 3 (Workshop) averages 25 min; participants who have used Workshop before will finish faster
- If participant finishes early, ask them to explain their naming choice for the output dataset (verbal check)

---

## ENVIRONMENT SETUP

See [ENVIRONMENT_SETUP.md](ENVIRONMENT_SETUP.md) for full setup instructions.
