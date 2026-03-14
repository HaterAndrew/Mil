# EX-20 — No-Code Builder
## Practical Exercise — TM-20 Proficiency

| | |
|---|---|
| **Version** | 1.0 — March 2026 |
| **Prerequisite** | TM-20 (and TM-10) |
| **Duration** | 90–120 min |
| **Environment** | MSS training instance with Workshop build permissions — see ENVIRONMENT_SETUP.md |

## SCENARIO

Your battalion S6 needs a Workshop dashboard showing daily vehicle availability by company for the past 30 days. A raw dataset is pre-loaded. Ingest it, build a basic pipeline, and produce a usable dashboard — no code required.

Training dataset: synthetic vehicle readiness data, LOGSTAT-format, 90 days, 4 companies.

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
- [ ] Group by company; aggregate average availability per day
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

## EVALUATOR NOTES

**Scoring:** 4 tasks. Go on 3 of 4 = overall Go. No-Go on Task 2 = automatic No-Go.

**Pre-exercise checklist:**
- Confirm "EX-20 Vehicle Availability Training Data" is visible to training accounts
- Verify training accounts have Pipeline Builder and Workshop build permissions
- Confirm NAMING_AND_GOVERNANCE_STANDARDS.md is accessible to participants

**Common failure modes:**

| Task | Common Failure | Evaluator Guidance |
|------|---------------|--------------------|
| Task 1 | Cannot locate dataset | Direct to training project folder — one prompt allowed without penalty |
| Task 2 | Output dataset name does not follow naming standards | Mark No-Go; cite specific standard violated; coach after evaluation |
| Task 2 | Transform runs but row count is wrong | Verify 30-day filter applied correctly; common error is off-by-one on date boundary |
| Task 3 | Filter widget present but has no effect on chart | Wiring issue (widget not connected to chart variable) — automatic No-Go |
| Task 4 | Evaluator has edit access | Participant shared with wrong role; mark Task 4 No-Go |

**Timing notes:**
- Task 2 is critical path — budget up to 45 min for participants with no prior Pipeline Builder experience
- Task 3 averages 25 min; participants familiar with Workshop finish faster
- If participant finishes early, ask them to explain their naming choice for the output dataset (verbal check)

---

## NEXT STEPS

Upon successful completion of EX-20, participants may branch based on role:

**All paths require TM-30 before any TM-40 track.** Proceed to TM-30 — Advanced Builder next.

After TM-30, branch based on role:

**WFF tracks — Warfighting Function application (prereq: TM-30 required):**
- TM-40A — Intelligence (G2/S2 staff, targeting officers, all-source analysts)
- TM-40B — Fires (FSE, fire support officers, targeting teams)
- TM-40C — Movement & Maneuver (G3/S3 maneuver staff, operations officers)
- TM-40D — Sustainment (G4/S4, FSB/BSB logistics staff)
- TM-40E — Protection (force protection, CBRN, provost marshal)
- TM-40F — Mission Command (G3/S3 staff, battle captains, XOs, CDRs)

**Specialist tracks — technical/analytical tracks (prereq: TM-30 required):**
- TM-40G through TM-40L per specialist billet assignment
