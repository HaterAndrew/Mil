# EX-40A — Intelligence
## Practical Exercise — TM-40A Proficiency

| Field | Value |
|-------|-------|
| **Version** | 1.0 — March 2026 |
| **Prerequisite** | TM-10, TM-20, TM-30 (required); TM-40A and CONCEPTS_GUIDE_TM40A_INTELLIGENCE (current track) |
| **Duration** | 3–4 hours |
| **Environment** | MSS training instance, standard user access — see ENVIRONMENT_SETUP.md |
| **Companion TM** | TM_40A_INTELLIGENCE.md |
| **Syllabus** | SYLLABUS_TM40A |
| **Exams** | EXAM_TM40A_PRE / EXAM_TM40A_POST |

## SCENARIO

You are the S2 at a BCT HQ during an exercise. The commander requires a fully configured intelligence picture — threat activity layers active, NAI/TAI overlays in place, and PIR alerts configured — before a targeting working group in four hours.

At T+90 min, the evaluator injects a data staleness event: the SIGINT reporting feed stops updating.

**Training environment:** Pre-loaded synthetic intelligence data (threat activity events, NAI/TAI overlays, SIGINT and HUMINT reporting layers). No real operational or intelligence data.

## TASK LIST

### Task 1 — Configure Intelligence COP Layers (40 min)

- [ ] Add and configure: threat activity feed (30 synthetic events in AOR), NAI/TAI overlays (4 NAIs and TAIs pre-plotted), and IPB overlay (terrain and threat pattern data)
- [ ] Verify the data-as-of timestamp for each layer is within the training data's current period
- [ ] Identify any layer with a stale or missing data source and note it for the evaluator

| Standard | Criteria |
|----------|----------|
| **Go** | All three layer types configured and displaying; timestamps verified; stale feeds identified and noted |
| **No-Go** | Any layer type absent; no timestamp verification; no awareness of data currency for any feed |

### Task 2 — Configure PIR Alerts (30 min)

*Evaluator hands the Commander's PIR Guidance Card to the participant at exercise start.*

Configure the following three PIRs as CCIR alerts using the provided guidance card:

| PIR | Trigger | Routing |
|-----|---------|---------|
| PIR 1 | Any confirmed enemy ADA asset in grid zone XX (geographic-based) | S2, S3 |
| PIR 2 | Any enemy armor within 5 km of Phase Line RED (geographic threshold) | S2, S3 |
| PIR 3 | Any enemy indirect fire from north of grid northing YY (geographic, indirect fire event type) | S2, S3 |

- [ ] Set notification routing for each PIR to S2 and S3 positions
- [ ] Verify PIR alerts fire using the provided test data values

| Standard | Criteria |
|----------|----------|
| **Go** | All three PIRs configured with correct triggers matching the guidance card; routing set to S2 and S3; at least 2 of 3 fire on test data |
| **No-Go** | Trigger parameters do not match guidance card; routing absent or personal-account-only; fewer than 2 PIRs fire on test data |

### Task 3 — Build Targeting Data Product (40 min)

- [ ] Build a targeting data product using the active target list from the synthetic dataset
- [ ] Code each target as confirmed or suspected; attribute each entry to its reporting source (SIGINT or HUMINT)
- [ ] Display data-as-of timestamps for the target list and for each reporting source feed
- [ ] Format for the targeting working group (S3, FSO, CDR)

| Standard | Criteria |
|----------|----------|
| **Go** | Confirmed vs. suspected visually distinguished; source attribution present per entry; timestamps visible; formatted for command audience |
| **No-Go** | Confirmed and suspected targets combined without distinction; attribution absent; timestamps missing on any section |

### Task 4 — Build Collection Status Display (30 min)

- [ ] Build a collection status display showing NAI coverage assignments, collection asset tasks, and collection gaps mapped to PIRs
- [ ] Identify at least one collection gap — a PIR with insufficient current collection asset coverage — and note it in the display
- [ ] Link the collection status display to the live NAI/TAI dataset (not static text)

| Standard | Criteria |
|----------|----------|
| **Go** | Display present and live-linked to NAI data; at least one collection gap explicitly noted |
| **No-Go** | Display is static text; no collection gaps identified; NAI coverage not linked to PIRs |

### Task 5 — Data Staleness Inject Response (30 min)

*Evaluator injects at T+90 min. Do not brief participants in advance.*

**Inject:** The SIGINT reporting feed has stopped updating — SIGINT-sourced entries in the threat activity layer and targeting product are now stale.

- [ ] Identify which COP layers, targeting product entries, and collection status elements are affected
- [ ] Update the targeting product and threat activity display to add explicit data currency caveats on all SIGINT-sourced entries
- [ ] Brief the evaluator (as S3) covering all four required elements: what intelligence products are affected, which collection layer remains current (HUMINT), what will and will not be briefed at the targeting working group, and what resolution action is being taken

| Standard | Criteria |
|----------|----------|
| **Go** | All SIGINT-sourced elements correctly identified; caveats added; verbal brief covers all four elements |
| **No-Go** | Stale SIGINT data presented as current; no caveats added; brief missing any of the four required elements |

### Task 6 — OPSEC and Distribution (15 min)

- [ ] Apply correct classification marking to the final targeting data product
- [ ] Configure the targeting product Workshop view: read-only access for FSO and CDR accounts; edit access restricted to S2 section only
- [ ] Confirm the evaluator (as FSO) can view but not edit the product

| Standard | Criteria |
|----------|----------|
| **Go** | Classification marking correct; read-only share confirmed; edit access restricted |
| **No-Go** | Marking absent or incorrect; evaluator account has edit access |

## EVALUATOR NOTES

**Scoring:** 6 tasks. Go on 5 of 6 = overall Go. No-Go on Task 2 or Task 5 = automatic No-Go.

### Pre-Exercise Checklist

- [ ] Confirm training accounts have standard MSS access (no build/pipeline permissions needed)
- [ ] Pre-load synthetic intelligence dataset; confirm all three COP layer types have data
- [ ] Prepare Commander's PIR Guidance Card — hand to participant at exercise start
- [ ] Know the exact PIR trigger parameters to verify Task 2 configurations
- [ ] Prepare test data values for PIR verification (Task 2)
- [ ] At T+90 min, pause the SIGINT reporting feed (see ENVIRONMENT_SETUP.md)

### Common Failure Modes

| Task | Common Failure | Evaluator Guidance |
|------|---------------|--------------------|
| Task 1 | Timestamps not verified for all three layer types | Ask: "How do you know this data is current?" — if participant cannot point to a timestamp per layer type, No-Go for that layer |
| Task 2 | PIR geographic boundary not configured — only event type set | A PIR without a geographic component will over-trigger; ask participant to show the full PIR definition before grading |
| Task 2 | Routing set to personal account rather than position | Position-based routing required; personal-only = coaching note, not automatic No-Go if both are set |
| Task 3 | Confirmed and suspected targets visually indistinguishable | Ask participant to point out which entries are confirmed at a glance; if the product does not support this, No-Go |
| Task 3 | No data-as-of timestamps on targeting product | Ask for one timestamp; if none present anywhere, No-Go |
| Task 4 | Collection status display is a manually typed text block | Ask participant to show how the display updates when NAI data changes; if it cannot, No-Go |
| Task 5 | Participant attempts to restore the SIGINT feed | Wrong response at this level; prompt: "What does the targeting working group need to know right now?" |
| Task 5 | Brief covers what's affected but omits resolution action | All four brief elements required; partial brief = No-Go on Task 5 |
| Task 6 | FSO evaluator account has edit access | Task 6 No-Go |
