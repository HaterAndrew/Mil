# EX-40B — Fires
## Practical Exercise — TM-40B Proficiency

| Field | Value |
|-------|-------|
| **Version** | 1.0 — March 2026 |
| **Prerequisite** | TM-10, TM-20, TM-30 (required); TM-40B and CONCEPTS_GUIDE_TM40B_FIRES (current track) |
| **Duration** | 3–4 hours |
| **Environment** | MSS training instance, standard user access — see ENVIRONMENT_SETUP.md |
| **Companion TM** | TM_40B_FIRES.md |
| **Syllabus** | SYLLABUS_TM40B |
| **Exams** | EXAM_TM40B_PRE / EXAM_TM40B_POST |

## SCENARIO

You are the FSE at a BCT HQ during an exercise. The commander requires FSCMs on the COP, a current targeting data product, and fires CCIRs active before a targeting working group in four hours.

At T+90 min, the evaluator injects a data staleness event: the BDA reporting feed from one fires element stops updating.

**Training environment:** Pre-loaded synthetic fires data (target list with confirmed/suspected entries, FSCM overlay, BDA reporting feed). No real fires or targeting data.

## TASK LIST

### Task 1 — Configure Fires Data Layers (40 min)

- [ ] Add and configure: FSCM overlay (using the pre-loaded synthetic FSCMs), active target list layer (15 entries), and BDA status overlay
- [ ] Verify the data-as-of timestamp for each layer; confirm the FSCM overlay is sourced from an authoritative data source, not manually drawn
- [ ] Identify any layer with a stale or missing data source and note it for the evaluator

| Standard | Criteria |
|----------|----------|
| **Go** | All three layer types configured and displaying; FSCM overlay sourced to data (not manual); timestamps verified; stale feeds identified if present |
| **No-Go** | Any layer type absent; FSCM overlay manually drawn without data source; timestamps not verified |

### Task 2 — Build Targeting Data Product (40 min)

- [ ] Build a targeting data product using the synthetic target list (15 entries, mix of confirmed and suspected)
- [ ] Code each target as confirmed or suspected using visual distinction (not just a column label); attribute each entry to its reporting source (SIGINT, HUMINT, or ISR)
- [ ] Display data-as-of timestamps for the target list as a whole and for each reporting source feed
- [ ] Format for the targeting working group (S3, FSO, CDR, S2)

| Standard | Criteria |
|----------|----------|
| **Go** | Product clearly distinguishes confirmed from suspected targets visually; source attribution present per entry; timestamps on product and by source; formatting appropriate for command audience |
| **No-Go** | Confirmed and suspected targets visually indistinguishable; attribution absent; timestamps missing from any section; format not suitable for targeting board |

### Task 3 — Configure Fires CCIRs (30 min)

*Evaluator hands the Commander's Fires CCIR Guidance Card to the participant at exercise start.*

Configure the following three CCIRs using the provided guidance card:

| CCIR | Trigger Type | Routing |
|------|-------------|---------|
| Fires CCIR 1 | Target engaged — any target changes status to "engaged" (status-based) | FSE, S3 |
| Fires CCIR 2 | Effects confirmed — any target achieves "BDA confirmed" status from BDA feed (status-based) | FSE, S3 |
| Fires CCIR 3 | FSCM violation — any friendly fires solution plots within a restricted fire area (geographic, FSCM layer boundary) | FSE, S3 |

- [ ] Set notification routing for each CCIR to FSE and S3 positions
- [ ] Verify at least 2 of the 3 CCIRs fire correctly using the provided test data values

| Standard | Criteria |
|----------|----------|
| **Go** | All three CCIRs configured with correct trigger types matching the guidance card; routing set; at least 2 of 3 fire on test data |
| **No-Go** | CCIR trigger types do not match guidance card; routing absent; fewer than 2 CCIRs fire on test data |

### Task 4 — Build Effects Assessment Display (20 min)

- [ ] Build an effects assessment display showing BDA status by target across all active fires elements
- [ ] For each target, display: target identifier, fires element reporting, BDA status (confirmed/estimated/no BDA), and data-as-of timestamp for the BDA entry
- [ ] Link the display to the live BDA reporting feed (not static text)

| Standard | Criteria |
|----------|----------|
| **Go** | BDA status display present for all targets with live data link; all four data elements present per entry; timestamps visible |
| **No-Go** | Display is static text; BDA status not broken out by fires element; timestamps absent |

### Task 5 — Data Staleness Inject Response (30 min)

*Evaluator injects at T+90 min. Do not brief participants in advance.*

**Inject:** The BDA reporting feed from one fires element has stopped updating — BDA entries from that element are now stale.

- [ ] Identify which targets in the effects assessment display and targeting product have BDA sourced from the affected fires element
- [ ] Update the effects assessment display and targeting product to add explicit data currency caveats on all affected BDA entries
- [ ] Brief the evaluator (as S3) covering all four required elements: which BDA entries are affected, which fires elements still have current BDA reporting, what the targeting working group will and will not receive as current BDA, and what resolution action is being taken

| Standard | Criteria |
|----------|----------|
| **Go** | All affected BDA entries correctly identified; caveats added; verbal brief covers all four required elements |
| **No-Go** | Stale BDA presented as current; no caveats added; brief missing any of the four required elements |

### Task 6 — OPSEC and Distribution (15 min)

- [ ] Apply correct classification marking to the final targeting data product
- [ ] Configure the targeting product Workshop view: read-only access for S3 and CDR accounts; edit access restricted to FSE only
- [ ] Confirm the evaluator (as S3) can view but not edit the product

| Standard | Criteria |
|----------|----------|
| **Go** | Classification marking correct; read-only share confirmed; edit access restricted to FSE |
| **No-Go** | Marking absent or incorrect; evaluator account has edit access |

## EVALUATOR NOTES

**Scoring:** 6 tasks. Go on 5 of 6 = overall Go. No-Go on Task 2 or Task 5 = automatic No-Go.

### Pre-Exercise Checklist

- [ ] Confirm training accounts have standard MSS access (no build/pipeline permissions needed)
- [ ] Pre-load synthetic fires dataset; confirm all three COP layer types have data
- [ ] Prepare Commander's Fires CCIR Guidance Card — hand to participant at exercise start
- [ ] Know the exact CCIR trigger types on the card to verify Task 3 configurations
- [ ] Prepare test data values for CCIR verification (Task 3)
- [ ] At T+90 min, pause the BDA reporting feed from the designated fires element (see ENVIRONMENT_SETUP.md)

### Common Failure Modes

| Task | Common Failure | Evaluator Guidance |
|------|---------------|--------------------|
| Task 1 | FSCM overlay manually drawn rather than sourced | Ask participant to show the layer data source; if no source is connected, No-Go for FSCM element |
| Task 1 | BDA status layer displays but timestamps not verified | Ask: "How do you know this BDA is current?" — if no timestamp, No-Go for that element |
| Task 2 | Confirmed and suspected targets visually indistinguishable | Most common Task 2 failure; ask participant to point to a confirmed and a suspected target at a glance — if product does not support this, No-Go |
| Task 2 | Source attribution in notes field only, not per entry | Attribution must be entry-level, not a page-level footnote; coach but not auto No-Go if timestamps are present |
| Task 3 | Fires CCIR 3 uses a manually drawn boundary rather than FSCM layer | FSCM boundary must come from the authoritative FSCM layer; ask participant to show the boundary source |
| Task 4 | Effects assessment display uses static text | Ask participant to change one BDA value — if display does not update, No-Go |
| Task 5 | Participant attempts to restore the BDA feed | Wrong response at this level; prompt: "The targeting working group starts in 30 minutes — what does the S3 need to know right now?" |
| Task 5 | Brief covers affected BDA but omits which elements still have current data | All four brief elements required; partial brief = No-Go on Task 5 |
| Task 6 | S3 evaluator account has edit access | Task 6 No-Go |
