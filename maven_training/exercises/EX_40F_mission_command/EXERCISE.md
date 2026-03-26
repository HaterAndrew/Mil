# EX_40F — Mission Command
## Practical Exercise — SL 4F Proficiency

| Field | Value |
|-------|-------|
| **Version** | 1.0 — March 2026 |
| **Prerequisite** | SL 1, SL 2, SL 3 (required); SL 4F and CONCEPTS_GUIDE_TM40F_MISSION_COMMAND (current track) |
| **Duration** | 3–4 hours |
| **Environment** | MSS training instance, standard user access — see ENVIRONMENT_SETUP.md |
| **Companion TM** | TM_40F_MISSION_COMMAND.md |
| **Syllabus** | SYLLABUS_TM40F |
| **Exams** | EXAM_TM40F_PRE / EXAM_TM40F_POST |

## SCENARIO

You are the battle captain at a BCT HQ during a force projection exercise. The commander requires a fully configured MSS common operating picture, CCIR alerts active, battle rhythm dashboard, and a Battle Update Assessment (BUA) read-ahead product — all before a theater-level VTC in four hours.

At T+90 min, the evaluator injects a data staleness event: the readiness data feed for 1st Battalion stops updating.

Training environment: pre-loaded synthetic operational data (readiness, SIGACT-analog events, personnel status). No real operational data.

## TASK LIST

### Task 1 — Configure the Common Operating Picture (45 min)

- [ ] Add and configure: unit positions (3 subordinate battalions), equipment readiness status overlay, and operational event markers
- [ ] Verify the data-as-of timestamp for each layer is within the training data's current period
- [ ] Identify any layer with a stale or missing data source and note it for the evaluator

| Standard | Criteria |
|----------|----------|
| **Go** | All three layers configured and displaying; at least one timestamp noted and verified; stale feeds identified (if any) |
| **No-Go** | Layers missing or timestamps not verified; no awareness of data currency |

### Task 2 — Configure CCIR Alerts (30 min)

*Evaluator provides Commander's CCIR Guidance Card at exercise start.*

- [ ] Using the provided Commander's CCIR Guidance Card, configure:
  - CCIR 1: Any battalion readiness below 70% (threshold-based)
  - CCIR 2: Any operational event within the defined sensitivity area (geographic-based)
  - CCIR 3: Personnel strength below 85% for any subordinate battalion (threshold-based)
  - Notify: Battle Captain and S3
- [ ] Set notification routing to Battle Captain and S3 positions
- [ ] Verify CCIRs fire using the provided test dataset values

| Standard | Criteria |
|----------|----------|
| **Go** | All three CCIRs configured with correct thresholds; routing set; at least 2 of 3 fire correctly on test data |
| **No-Go** | Threshold values do not match guidance card; routing absent; fewer than 2 CCIRs fire on test data |

### Task 3 — Build the Battle Rhythm Dashboard (30 min)

- [ ] Using the provided weekly event list, build a battle rhythm dashboard in Workshop showing: today's scheduled events with status (complete/pending/upcoming), this week's events, and key decision gates in the next 14 days
- [ ] Link the readiness summary widget to the live readiness dataset (not a static text widget)
- [ ] Confirm the dashboard updates when the underlying data changes

| Standard | Criteria |
|----------|----------|
| **Go** | All three components present; readiness widget is live-linked; dashboard updates on data change |
| **No-Go** | Static data used instead of live dataset; missing components; dashboard does not update |

### Task 4 — Produce BUA Read-Ahead Product (45 min)

- [ ] Build a BUA read-ahead package containing: overall readiness summary (current vs. threshold), CCIR status (active/triggered/clear), operational outlook (key events next 24 hours), and data-as-of timestamps on every data element
- [ ] Format for an O-5/CG audience — no jargon, no raw data, no unexplained abbreviations
- [ ] Ensure the product is correctly marked per OPSEC classification guidance for training data

| Standard | Criteria |
|----------|----------|
| **Go** | All four sections present; timestamps on all data elements; formatting appropriate for commander audience; OPSEC marking present |
| **No-Go** | Missing timestamps on any data element; raw data exposed without summary; OPSEC marking absent |

### Task 5 — Data Staleness Inject Response (30 min)

*Evaluator injects at T+90 min. Do not brief participants in advance.*

**Inject:** The 1st Battalion readiness data feed has stopped updating — data is now 6 hours old.

- [ ] Identify which COP elements and BUA sections are affected by the stale feed
- [ ] Update the BUA product to reflect the data gap with an explicit caveat on affected elements
- [ ] Brief the evaluator (as S3): what is affected, what is still current, what you will/will not brief to the commander, and what action you are taking to resolve the feed

| Standard | Criteria |
|----------|----------|
| **Go** | Affected elements correctly identified; BUA updated with caveat; verbal brief covers all four elements |
| **No-Go** | Stale data presented as current; no caveat added; brief to S3 misses the impact or the resolution action |

### Task 6 — OPSEC and Distribution (15 min)

- [ ] Apply correct classification marking to the final BUA product
- [ ] Configure the BUA Workshop view to share with the commander's personal device account (read-only) and restrict edit access
- [ ] Confirm the evaluator (as the commander) can view but not edit the product

| Standard | Criteria |
|----------|----------|
| **Go** | Marking correct; read-only share confirmed; evaluator account cannot edit |
| **No-Go** | Marking absent or incorrect; evaluator account has edit access |

## EVALUATOR NOTES

**Scoring:** 6 tasks. Go on 5 of 6 = overall Go. No-Go on Task 2 or Task 5 = automatic No-Go.

### Pre-Exercise Checklist

- [ ] Confirm training accounts have standard MSS access (no build/pipeline permissions needed)
- [ ] Pre-load the synthetic operational dataset; confirm all three COP layers have data
- [ ] Prepare Commander's CCIR Guidance Card — hand to participant at exercise start
- [ ] Know the exact threshold values on the card to verify Task 2 CCIR configurations
- [ ] Prepare test dataset values for CCIR verification (Task 2)
- [ ] At T+90 min, pause the readiness feed for 1st Battalion (see ENVIRONMENT_SETUP.md)

### Common Failure Modes

| Task | Common Failure | Evaluator Guidance |
|------|---------------|--------------------|
| Task 1 | Timestamps not checked | Ask: "How do you know the data is current?" — if no timestamp, No-Go for that element |
| Task 2 | Threshold matches card but wrong feed selected | CCIR with wrong data source will not fire — ask participant to show the CCIR definition |
| Task 2 | Notification routed to personal account not position | Position-based routing required; personal account routing = coaching note but not No-Go if both are set |
| Task 3 | Battle rhythm dashboard uses static text | Ask participant to change one underlying value — if dashboard does not update, No-Go |
| Task 4 | BUA lacks data-as-of timestamps | Most common failure; ask participant to show one timestamp before grading — if none present, No-Go |
| Task 5 | Participant tries to fix the pipeline | Wrong response at this level; if more than 5 min spent trying to fix the feed, prompt: "What do you need to brief right now?" |
| Task 6 | Evaluator has edit access | Sharing step was done wrong; mark Task 6 No-Go |
