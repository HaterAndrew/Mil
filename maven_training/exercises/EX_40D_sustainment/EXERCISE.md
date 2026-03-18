# EX_40D — Sustainment
## Practical Exercise — TM-40D Proficiency

| Field | Value |
|-------|-------|
| **Version** | 1.0 — March 2026 |
| **Prerequisite** | TM-10, TM-20, TM-30 (required); TM-40D and CONCEPTS_GUIDE_TM40D_SUSTAINMENT (current track) |
| **Duration** | 3–4 hours |
| **Environment** | MSS training instance, standard user access — see ENVIRONMENT_SETUP.md |
| **Companion TM** | TM_40D_SUSTAINMENT.md |
| **Syllabus** | SYLLABUS_TM40D |
| **Exams** | EXAM_TM40D_PRE / EXAM_TM40D_POST |

## SCENARIO

You are the S4 section at a BCT HQ during a sustainment exercise. The commander requires a logistics status dashboard and sustainment CCIRs active before the sustainment synchronization meeting in four hours.

**Required products:**
- Readiness dashboard showing current status versus threshold for all subordinate units
- CCIRs alerting on readiness below 75% and critical supply below three days of supply (DOS)
- Supply status product covering Class I, III, and V by unit
- Data-as-of timestamps on every displayed element

At T+90 min, the evaluator injects a data staleness event: the LOGSTAT feed from 1st Battalion FSC stops updating.

**Training environment:** Pre-loaded synthetic logistics data (LOGSTAT, readiness, transportation status). No real operational data.

## TASK LIST

### Task 1 — Configure Logistics Data Layers (35 min)

- [ ] Add and configure: unit readiness feed (all subordinate units), supply-on-hand status feed (Class I, III, V), and transportation status overlay
- [ ] Verify the data-as-of timestamp for each layer is within the training data's current reporting period
- [ ] Identify any feed with a stale or missing data source and note it for the evaluator

| Standard | Criteria |
|----------|----------|
| **Go** | All three layers configured and displaying; at least one timestamp noted and verified; stale feeds identified (if any) |
| **No-Go** | One or more layers missing; timestamps not verified; no awareness of data currency for any layer |

### Task 2 — Build Readiness Dashboard (35 min)

- [ ] Build a Workshop readiness dashboard showing current readiness percentage versus the 75% threshold for all five subordinate units
- [ ] Link the readiness widget to the live readiness dataset — do not use a static text widget or manually entered values
- [ ] Apply timestamps to all readiness elements displayed on the dashboard
- [ ] Confirm the dashboard updates when the underlying readiness data changes

| Standard | Criteria |
|----------|----------|
| **Go** | Dashboard shows readiness versus threshold for all five units; readiness widget is live-linked; timestamps present on all elements; dashboard updates on data change |
| **No-Go** | Static or manually entered values used; one or more units missing; no timestamps; dashboard does not update on data change |

### Task 3 — Configure Sustainment CCIRs (30 min)

*Evaluator provides Commander's Sustainment CCIR Guidance Card at exercise start.*

Configure the following two CCIRs using the provided guidance card:

| CCIR | Trigger | Routing |
|------|---------|---------|
| CCIR 1 | Any subordinate unit readiness falls below 75% (threshold-based) | S4, XO |
| CCIR 2 | Any subordinate unit critical supply (Class III or Class V) falls below 3 DOS (threshold-based) | S4, XO |

- [ ] Set notification routing to S4 and XO positions
- [ ] Verify both CCIRs fire correctly using the provided test dataset values

| Standard | Criteria |
|----------|----------|
| **Go** | Both CCIRs configured with correct thresholds and correct data sources; routing set to S4 and XO; both fire on test data |
| **No-Go** | Threshold values do not match guidance card; wrong data source selected; routing absent; fewer than one CCIR fires on test data |

### Task 4 — Build Supply Status Product for Sustainment Sync (30 min)

- [ ] Build a supply status product showing Class I, III, and V levels by subordinate unit
- [ ] Include data-as-of timestamps on every data element displayed
- [ ] Format for an O-5 audience — no raw data, no unexplained abbreviations, clear thresholds labeled
- [ ] Ensure the product is correctly marked per OPSEC classification guidance for training data

| Standard | Criteria |
|----------|----------|
| **Go** | All three supply classes present for all subordinate units; data-as-of timestamps on all elements; formatted for O-5 audience; OPSEC marking present |
| **No-Go** | Missing supply class or unit; timestamps absent from any element; raw unformatted data exposed; OPSEC marking absent |

### Task 5 — Data Staleness Inject Response (30 min)

*Evaluator injects at T+90 min. Do not brief participants in advance.*

**Inject:** The LOGSTAT feed from 1st Battalion FSC has stopped updating — data is now 3 hours old.

- [ ] Identify which dashboard elements and supply status product sections are affected by the stale 1st Bn LOGSTAT feed
- [ ] Update the readiness dashboard and supply status product to reflect the data gap with explicit caveats on affected elements
- [ ] Brief the evaluator (as XO) covering all four required elements: what is affected, what is still current, what you will and will not brief at the sustainment sync, and what action you are taking to resolve the feed

| Standard | Criteria |
|----------|----------|
| **Go** | Affected readiness and supply elements correctly identified; caveats added to dashboard and supply status product; verbal brief covers all four elements |
| **No-Go** | Stale 1st Bn LOGSTAT data presented as current without caveat; no caveats added; participant attempts to fix the pipeline instead of characterizing the gap; brief to XO misses the impact on the sustainment sync or omits resolution action |

### Task 6 — OPSEC and Distribution (15 min)

- [ ] Apply correct classification marking to the readiness dashboard and supply status product
- [ ] Configure both products: read-only (Viewer) access for sustainment sync attendees who are not S4; edit access restricted to S4 section only
- [ ] Confirm the evaluator (as a sustainment sync attendee from a subordinate unit) can view but not edit either product

| Standard | Criteria |
|----------|----------|
| **Go** | Marking correct on both products; read-only share confirmed for non-S4 attendees; evaluator account cannot edit |
| **No-Go** | Marking absent or incorrect; attendee account has edit access; evaluator account can modify a product |

## EVALUATOR NOTES

**Scoring:** 6 tasks. Go on 5 of 6 = overall Go. No-Go on Task 2 or Task 5 = automatic No-Go.

### Pre-Exercise Checklist

- [ ] Confirm training accounts have standard MSS access (no build/pipeline permissions required)
- [ ] Pre-load synthetic LOGSTAT dataset; confirm all five subordinate units have data in all three layers
- [ ] Prepare Commander's Sustainment CCIR Guidance Card — hand to participant at exercise start
- [ ] Know the exact threshold values on the card to verify Task 3 CCIR configurations
- [ ] Have test dataset values ready for CCIR verification (Task 3)
- [ ] At T+90 min, pause the 1st Battalion FSC LOGSTAT feed (see ENVIRONMENT_SETUP.md)

### Common Failure Modes

| Task | Common Failure | Evaluator Guidance |
|------|---------------|--------------------|
| Task 1 | Timestamps not verified | Ask: "How do you know this readiness data is current?" — if no timestamp, No-Go for that element |
| Task 2 | Readiness widget is static text with manually entered values | Ask participant to change one underlying readiness value — if widget does not update, No-Go |
| Task 2 | Dashboard shows readiness numbers but no threshold reference | Ask: "How can the XO tell which units are below threshold?" — threshold must be visible |
| Task 3 | CCIR 2 uses wrong data source (readiness feed instead of supply feed) | Wrong feed = CCIR will not fire correctly — No-Go if not corrected |
| Task 3 | DOS threshold entered as 3.0 but supply data is in percentage — CCIR never fires | Verify unit and data type match before grading; if participant cannot identify this mismatch, No-Go |
| Task 4 | Supply status product lacks timestamps | Most common Task 4 failure; ask participant to show the data-as-of field for any unit — if absent, No-Go |
| Task 5 | Participant tries to fix the LOGSTAT pipeline | Wrong response at this echelon; if more than 5 minutes spent troubleshooting, prompt: "What does the XO need to know for the sustainment sync?" |
| Task 5 | Participant briefs 1st Bn readiness without caveat | Presenting stale LOGSTAT as current is a No-Go; debrief on operational risk of resupply decisions on 3-hour-old data |
| Task 6 | Evaluator subordinate unit account has edit access | Task 6 No-Go |
