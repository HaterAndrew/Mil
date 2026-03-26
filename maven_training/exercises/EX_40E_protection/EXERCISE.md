# EX_40E — Protection
## Practical Exercise — SL 4E Proficiency

| Field | Value |
|-------|-------|
| **Version** | 1.0 — March 2026 |
| **Prerequisite** | SL 1, SL 2, SL 3 (required); SL 4E and CONCEPTS_GUIDE_TM40E_PROTECTION (current track) |
| **Duration** | 3–4 hours |
| **Environment** | MSS training instance, standard user access — see ENVIRONMENT_SETUP.md |
| **Companion TM** | TM_40E_PROTECTION.md |
| **Syllabus** | SYLLABUS_TM40E |
| **Exams** | EXAM_TM40E_PRE / EXAM_TM40E_POST |

## SCENARIO

You are the force protection officer at a BCT HQ during a training rotation. The commander requires threat tracking active, force protection CCIRs configured, and a PERSTAT display ready before the protection working group in four hours.

**Required products:**
- Threat display covering three sectors (NORTH, CENTRAL, SOUTH) with IED reporting
- Threat trending heat map
- Force protection CCIRs for threat events in restricted areas and casualties above threshold
- PERSTAT display for all organic battalions

At T+90 min, the evaluator injects a data staleness event: threat reporting from Sector SOUTH stops updating.

**Training environment:** Pre-loaded synthetic threat incident data and PERSTAT feed. No real operational data.

## TASK LIST

### Task 1 — Configure Threat Data Layers (35 min)

- [ ] Add and configure: threat incident layer (all three sectors — NORTH, CENTRAL, SOUTH), IED reporting overlay (filtered to past 30 days), and threat trending heat map
- [ ] Verify the data-as-of timestamp for each threat layer is within the training data's current reporting period
- [ ] Note the geographic coverage of each layer and confirm all three sectors have data

| Standard | Criteria |
|----------|----------|
| **Go** | All three threat layers configured and displaying; all three sectors confirmed; at least one timestamp noted and verified per layer |
| **No-Go** | One or more threat layers missing; sectors not all covered; timestamps not verified; geographic coverage not noted |

### Task 2 — Configure Force Protection CCIRs (30 min)

*Evaluator provides Commander's Force Protection CCIR Guidance Card at exercise start.*

Configure the following two CCIRs using the provided guidance card:

| CCIR | Trigger | Routing |
|------|---------|---------|
| CCIR 1 | Any threat event within designated restricted area (geographic-based; coordinates on guidance card) | Force Protection Officer, S3 |
| CCIR 2 | BCT casualty count exceeds threshold (15 WIA or 5 KIA per 72-hour period) | Force Protection Officer, S3 |

- [ ] Set notification routing to the Force Protection Officer and S3 positions
- [ ] Verify both CCIRs fire correctly using the provided test dataset values

| Standard | Criteria |
|----------|----------|
| **Go** | Both CCIRs configured with correct triggers and correct data sources; routing set to Force Protection Officer and S3; both fire on test data |
| **No-Go** | Geographic boundary does not match restricted area coordinates; casualty threshold does not match guidance card; routing absent; fewer than one CCIR fires on test data |

### Task 3 — Build PERSTAT Display (25 min)

- [ ] Configure the PERSTAT display showing personnel accountability (assigned vs. present for duty) by unit for all organic battalions
- [ ] Apply a data-as-of timestamp to the PERSTAT display — do not display PERSTAT without a clear indication of when data was last reported
- [ ] Identify any unit where PERSTAT has not been submitted within the last 24 hours and note it for the evaluator

| Standard | Criteria |
|----------|----------|
| **Go** | PERSTAT visible for all organic battalions; timestamps present; any overdue submissions identified |
| **No-Go** | PERSTAT display has no timestamp; one or more units missing; participant presents PERSTAT without noting its as-of date during review |

### Task 4 — Build Vulnerability Assessment Display (30 min)

- [ ] Configure a vulnerability assessment display overlaying MSR route segments, installation perimeters, and supply route overlays with the threat incident layer
- [ ] Identify at least one vulnerability visible in the combined overlay (e.g., an MSR segment with multiple threat incidents in the past 14 days, or an installation perimeter within a threat cluster)
- [ ] Document the identified vulnerability in the product (annotate the map or add a text note) for the protection working group

| Standard | Criteria |
|----------|----------|
| **Go** | Route and installation overlays present on same view as threat layer; at least one vulnerability identified and documented in the product |
| **No-Go** | Overlays present but threat layer not combined in same view; no vulnerability identified or documented; display configured but no usable assessment produced |

### Task 5 — Data Staleness Inject Response (30 min)

*Evaluator injects at T+90 min. Do not brief participants in advance.*

**Inject:** Threat reporting from Sector SOUTH has stopped updating — the last report is from 2 hours ago.

- [ ] Identify which threat layers and COP elements are affected by the Sector SOUTH reporting gap
- [ ] Update the threat display to reflect the data gap with an explicit caveat on the Sector SOUTH layer
- [ ] Brief the evaluator (as S3) covering all four required elements: what threat data is still current, what is not current, what you will and will not brief to the protection working group regarding Sector SOUTH, and what action you are taking to restore or characterize the reporting gap

| Standard | Criteria |
|----------|----------|
| **Go** | Affected layers correctly identified; caveat annotation added to Sector SOUTH threat data; verbal brief covers all four elements |
| **No-Go** | Sector SOUTH threat data presented as current without caveat; no annotation added; participant speculates about cause or threat conditions in Sector SOUTH rather than characterizing the uncertainty; brief to S3 omits resolution action |

### Task 6 — OPSEC and Distribution (15 min)

- [ ] Apply correct classification marking to the threat display, PERSTAT display, and vulnerability assessment product
- [ ] Configure all three products: read-only (Viewer) access for protection working group attendees who are not in the force protection section; edit access restricted to force protection section only
- [ ] Confirm the evaluator (as a working group attendee from a subordinate unit) can view but not edit any product
- [ ] Verbalize to the evaluator: threat data, PERSTAT data, and vulnerability data in combination reveal security posture and must not be exported without authorization

| Standard | Criteria |
|----------|----------|
| **Go** | Marking correct on all products; read-only share confirmed for non-force-protection attendees; evaluator account cannot edit; participant verbalizes the export restriction |
| **No-Go** | Marking absent on any product; attendee account has edit access; evaluator account can modify a product; participant does not address export restriction when prompted |

## EVALUATOR NOTES

**Scoring:** 6 tasks. Go on 5 of 6 = overall Go. No-Go on Task 2 or Task 5 = automatic No-Go.

### Pre-Exercise Checklist

- [ ] Confirm training accounts have standard MSS access (no build/pipeline permissions required)
- [ ] Pre-load synthetic threat incident data and PERSTAT feed; confirm all three sectors have data and all organic battalions appear in the PERSTAT feed
- [ ] Prepare Commander's Force Protection CCIR Guidance Card — hand to participant at exercise start
- [ ] Know the restricted area coordinates and casualty thresholds on the card to verify Task 2 CCIR configurations
- [ ] Have test dataset values ready for CCIR verification (Task 2)
- [ ] At T+90 min, pause the Sector SOUTH threat reporting feed (see ENVIRONMENT_SETUP.md)

### Common Failure Modes

| Task | Common Failure | Evaluator Guidance |
|------|---------------|--------------------|
| Task 1 | Threat heat map covers wrong time window | Ask: "What time period does this heat map reflect?" — if participant cannot answer, ask them to verify the filter setting |
| Task 1 | IED reporting layer is unfiltered — all historical incidents with no date range | Ask: "How old is the oldest incident on this layer?" — unfiltered historical data without context is not operationally useful; coach on applying the 30-day filter |
| Task 2 | CCIR 1 geographic boundary set too broadly | Most common Task 2 failure; a boundary too large generates false positives; ask participant to show the boundary and compare to guidance card coordinates |
| Task 2 | CCIR 2 casualty threshold applied to wrong data source (personnel strength instead of casualty feed) | Verify the data source field; wrong source = CCIR will not fire correctly — No-Go if not corrected |
| Task 3 | PERSTAT displayed without data-as-of timestamp | Most common Task 3 failure; ask: "When was this PERSTAT submitted?" — if no timestamp on the display, No-Go |
| Task 4 | Vulnerability noted verbally but not documented in the product | Verbal identification is not sufficient; the product must contain the annotation or note for the working group — if absent, No-Go |
| Task 5 | Participant speculates about threat activity in Sector SOUTH | Speculation about threat conditions from a data gap is not appropriate; prompt: "What do you actually know versus what is the data telling you?" |
| Task 5 | Participant attempts to troubleshoot the Sector SOUTH reporting feed | Wrong response at this level; if more than 5 minutes spent troubleshooting, prompt: "What does the S3 need to know for the protection working group?" |
| Task 6 | Combined threat/PERSTAT/vulnerability products exported without authorization check | OPSEC failure; if participant exports without noting the distribution restriction, mark No-Go and debrief the aggregate sensitivity of these products |
