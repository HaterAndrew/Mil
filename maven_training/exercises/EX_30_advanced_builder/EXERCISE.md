# EX_30 — Advanced Builder
## Practical Exercise — SL 3 Proficiency

| | |
|---|---|
| **Version** | 1.0 — March 2026 |
| **Prerequisite** | SL 3 (and SL 1, SL 2) |
| **Duration** | 2–3 hours |
| **Environment** | MSS training instance with Pipeline Builder and Contour/Quiver access — see ENVIRONMENT_SETUP.md |

## SCENARIO

G2 has a raw intelligence summary dataset (synthetic) covering 60 days of SIGACT-type events across a training AOR. Build an analytical pipeline that cleans and enriches the data, produces a Contour geospatial view, and builds a Quiver pivot for pattern-of-life analysis. No code required — Pipeline Builder and no-code tools only.

Training dataset: synthetic SIGACT-analog events with date, grid, event type, and unit fields.

## TASK LIST

### Task 1 — Data Profiling (20 min)
- [ ] Load the raw dataset into a Pipeline Builder branch
- [ ] Identify: null rate per column, duplicate records, date range coverage
- [ ] Produce a written data quality summary (3–5 bullet points) for your evaluator
- **Go:** Summary accurately reflects null rates and duplicates; date range is correct
- **No-Go:** Summary contains factual errors about the dataset

### Task 2 — Clean and Enrich (40 min)
- [ ] Deduplicate records on event ID
- [ ] Fill null unit fields with "UNKNOWN"
- [ ] Add a derived column: `week_number` from the date field
- [ ] Output to a clean dataset following naming standards
- **Go:** Output has no duplicates; no null unit fields; `week_number` present and correct
- **No-Go:** Duplicates remain or derived column is wrong

### Task 3 — Contour Geospatial View (30 min)
- [ ] Connect the clean dataset to Contour
- [ ] Plot events as points using the grid coordinate field
- [ ] Color-code by event type
- [ ] Add a time filter for the past 30 days
- **Go:** Points render on map; color coding correct; time filter functions
- **No-Go:** Map does not render or color coding is absent

### Task 4 — Quiver Pattern-of-Life (30 min)
- [ ] Create a Quiver pivot: rows = `week_number`, columns = event type, values = count
- [ ] Add a heat-map color scale
- [ ] Identify the week with the highest activity (annotate for evaluator)
- **Go:** Pivot is correct; heat map renders; high-activity week identified accurately
- **No-Go:** Pivot counts are incorrect or high-activity week is wrong

### Task 5 — AIP Logic Filter (no-code) (20 min)
- [ ] Build a simple AIP Logic rule in the UI (no code): flag any event with a null grid as "INCOMPLETE"
- [ ] Verify flagged records appear in a filtered view
- **Go:** Rule fires correctly on null grid records
- **No-Go:** Rule does not fire or fires on wrong records

## EVALUATOR NOTES

**Scoring:** 5 tasks. Go on 4 of 5 = overall Go. No-Go on Task 2 = automatic No-Go.

**Pre-exercise checklist:**
- Confirm Contour is enabled and grid projection is configured for WGS84 decimal degrees (see ENVIRONMENT_SETUP.md)
- Verify synthetic dataset contains at least 5 duplicate event IDs and at least 3 null unit fields
- Confirm AIP Logic is available in the training tenant

**Common failure modes:**

| Task | Common Failure | Evaluator Guidance |
|------|---------------|--------------------|
| Task 1 | Null rate reported as zero | Participant likely previewed a cached/clean version; confirm they loaded the raw dataset |
| Task 2 | Deduplication removes wrong records | Ask which field they deduplicated on; only event ID is correct |
| Task 2 | Null fill applied to wrong column | Event type or date filled instead of unit — check output schema directly |
| Task 3 | Map renders but no color coding | Default point style used; color-by-field must be explicitly set |
| Task 3 | Contour projection error | Coordinate format mismatch — see ENVIRONMENT_SETUP.md; environment failure, not participant failure |
| Task 5 | AIP Logic rule fires on wrong field | Show rule definition; null grid vs. null unit is a common confusion |

**Timing notes:**
- Task 3 (Contour) is the most environment-sensitive — budget 45 min total including setup issues
- Task 5 (AIP Logic) often faster than expected (~10 min for participants familiar with rule editors)
- Cohorts with G2/S2 backgrounds typically complete Tasks 3–4 faster than average

---

## NEXT STEPS

Upon successful completion of EX-30, participants are cleared to proceed to SL 4 tracks. SL 3 is a **required** prereq for all TM-40A–O tracks.

**SL 4 Tracks (select by role):**

*WFF Functional Tracks (TM-40A–F):*
- SL 4A — Intelligence (G2/S2 staff, targeting officers, all-source analysts)
- SL 4B — Fires (FSOs, FSEs, targeting officers, fires NCOs)
- SL 4C — Movement & Maneuver (G3/S3 staff, operations officers, maneuver planners)
- SL 4D — Sustainment (G4/S4 staff, logistics officers, supply chain managers)
- SL 4E — Protection (FP officers, CBRN officers, provost marshal staff)
- SL 4F — Mission Command (battle captains, XOs, CDRs, MC-function staff)

*Specialist Tracks (TM-40G–O):*
- SL 4G — ORSA (FA49, quantitative analysts)
- SL 4H — AI Engineer (AI/ML specialists, AIP Logic developers)
- SL 4M — ML Engineer (ML engineers, data scientists)
- SL 4J — Program Manager (technical PMs, G8/S8, resource managers)
- SL 4K — Knowledge Manager (KMOs, 37F, knowledge officers)
- SL 4L — Software Engineer (SWEs, OSDK developers)
- SL 4N — UI/UX Designer (UI/UX designers, Workshop developers)
- SL 4O — Platform Engineer (platform engineers, DevSecOps)

After completing a SL 4 specialist track, participants may continue to the corresponding **SL 5 advanced track** (TM-50G–O). Advanced exercises for SL 5 tracks are available in the EX-50 series directories.
