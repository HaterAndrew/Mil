# EX_40C — Movement & Maneuver
## Practical Exercise — TM-40C Proficiency

| Field | Value |
|-------|-------|
| **Version** | 1.0 — March 2026 |
| **Prerequisite** | TM-10, TM-20, TM-30 (required); TM-40C and CONCEPTS_GUIDE_TM40C_MOVEMENT_MANEUVER (current track) |
| **Duration** | 3–4 hours |
| **Environment** | MSS training instance, standard user access — see ENVIRONMENT_SETUP.md |
| **Companion TM** | TM_40C_MOVEMENT_MANEUVER.md |
| **Syllabus** | SYLLABUS_TM40C |
| **Exams** | EXAM_TM40C_PRE / EXAM_TM40C_POST |

## SCENARIO

You are the S3 at a BCT HQ during a force-on-force exercise. The commander is issuing an attack order in four hours and requires: current unit positions for three maneuver battalions, a designated axis of advance, operational graphics for all phase lines (LD, PL AMBER, PL BLACK, OBJ IRON), a task organization overlay reflecting the OPORD task org, and a CCIR alerting when any battalion crosses PL AMBER.

At T+90 min, the evaluator injects a data staleness event: the position feed for 2nd Battalion stops updating.

**Training environment:** Pre-loaded synthetic maneuver data (unit positions, route corridors, obstacle overlay). No real operational data.

## TASK LIST

### Task 1 — Configure Maneuver COP Layers (40 min)

- [ ] Add and configure: unit position feeds for 1st, 2nd, and 3rd Maneuver Battalions; main supply route (MSR) corridor; and obstacle overlay
- [ ] Verify the data-as-of timestamp for each position layer is within the training data's current period
- [ ] Identify any position feed that is stale or has no data and note it for the evaluator

| Standard | Criteria |
|----------|----------|
| **Go** | All three battalion position layers configured and displaying; route and obstacle overlays visible; at least one timestamp noted and verified; stale feeds identified (if any) |
| **No-Go** | One or more battalion position layers missing; timestamps not verified; no awareness of data currency for any layer |

### Task 2 — Configure Operational Graphics (25 min)

*Evaluator provides the graphic control measure list at exercise start.*

Add the following graphics to the COP using the provided list:

| Graphic | Label | Standard |
|---------|-------|----------|
| Line of Departure | LD | Correct grid; FM 1-02.1 symbology |
| Phase Line AMBER | PL AMBER | Correct grid; FM 1-02.1 symbology |
| Phase Line BLACK | PL BLACK | Correct grid; FM 1-02.1 symbology |
| Objective IRON | OBJ IRON | Correct grid; FM 1-02.1 symbology |

- [ ] Verify each graphic is at the correct grid coordinates per the graphic control measure list
- [ ] Confirm all graphics use standard FM 1-02.1 symbology conventions as supported in MSS

| Standard | Criteria |
|----------|----------|
| **Go** | All four graphics present; labels correct; placed at specified grids; symbology consistent with provided guidance |
| **No-Go** | Any of the four graphics missing; incorrect labels; wrong coordinates; unlabeled or symbology not matching provided guidance |

### Task 3 — Configure CCIR — Battalion Crosses PL AMBER (30 min)

*Evaluator provides the Commander's CCIR Guidance Card at exercise start.*

- [ ] Using the provided Commander's CCIR Guidance Card, configure: CCIR 1 — any maneuver battalion position report places the unit on or north of PL AMBER; data source: battalion position feeds; notify: S3 and Battle Captain
- [ ] Set notification routing to S3 and Battle Captain positions
- [ ] Verify the CCIR fires using the provided test dataset value (2nd Bn position north of PL AMBER)

| Standard | Criteria |
|----------|----------|
| **Go** | CCIR configured with correct geographic trigger aligned to PL AMBER; correct data source; routing set; fires on test data |
| **No-Go** | Boundary not aligned to PL AMBER; wrong data source; routing absent; CCIR does not fire on test data |

### Task 4 — Build Task Organization Display (25 min)

- [ ] Using the provided OPORD task org annex, build a task organization display showing which maneuver units are assigned or attached to which headquarters for the operation
- [ ] Confirm the display reflects the current task org (not a previous or default configuration)
- [ ] Identify at least one synchronization gap visible in the task org affecting the maneuver COP (e.g., an attached unit whose position feed is not under the correct HQ layer)

| Standard | Criteria |
|----------|----------|
| **Go** | Task org accurately reflects the provided OPORD task org; at least one synchronization gap identified and noted for the evaluator |
| **No-Go** | Task org does not reflect OPORD task org; no synchronization gaps identified; display is a default/placeholder |

### Task 5 — Data Staleness Inject Response (30 min)

*Evaluator injects at T+90 min. Do not brief participants in advance.*

**Inject:** The 2nd Battalion position feed has stopped updating — last reported position is from 90 minutes ago.

- [ ] Identify which COP layers and products are affected by the stale 2nd Bn position feed
- [ ] Update the maneuver COP to reflect the data gap with an explicit caveat on the 2nd Bn layer
- [ ] Brief the evaluator (as S3) covering all four required elements: what is affected, what is still current, what you will/will not brief to the commander regarding 2nd Bn position prior to LD, and what action you are taking to resolve the feed

| Standard | Criteria |
|----------|----------|
| **Go** | Affected layers correctly identified; caveat annotation added to 2nd Bn layer; verbal brief covers all four elements |
| **No-Go** | Stale 2nd Bn position presented as current without caveat; no annotation added; brief misses the operational impact (commander making an attack decision with unverified position data) or omits resolution action |

### Task 6 — OPSEC and Distribution (15 min)

- [ ] Apply correct classification marking to the maneuver COP view and task org display
- [ ] Configure the maneuver COP Workshop view: Viewer access for non-S3 recipients (e.g., adjacent unit liaison); edit access restricted to S3 section only
- [ ] Confirm the evaluator (as liaison officer) can view but not edit the product

| Standard | Criteria |
|----------|----------|
| **Go** | Classification marking present on all products; Viewer-only share confirmed for non-S3 recipients; evaluator account cannot edit |
| **No-Go** | Classification marking absent; non-S3 account has edit access; evaluator account can modify the COP |

## EVALUATOR NOTES

**Scoring:** 6 tasks. Go on 5 of 6 = overall Go. No-Go on Task 3 or Task 5 = automatic No-Go.

### Pre-Exercise Checklist

- [ ] Confirm training accounts have standard MSS access (no build/pipeline permissions required)
- [ ] Pre-load synthetic maneuver dataset; confirm all three battalion position layers have data
- [ ] Prepare the Graphic Control Measure list and OPORD task org annex — hand to participant at exercise start
- [ ] Prepare the Commander's CCIR Guidance Card — hand to participant at exercise start
- [ ] Know the test dataset value for CCIR verification (Task 3): 2nd Bn position north of PL AMBER
- [ ] At T+90 min, pause the 2nd Battalion position feed (see ENVIRONMENT_SETUP.md)

### Common Failure Modes

| Task | Common Failure | Evaluator Guidance |
|------|---------------|--------------------|
| Task 1 | Timestamps not verified | Ask: "How do you know 2nd Bn's position is current?" — if no timestamp, No-Go for that element |
| Task 2 | PL AMBER/BLACK use incorrect or unlabeled symbology | Ask participant to show how each line is labeled; if unlabeled after one prompt, No-Go |
| Task 2 | OBJ IRON placed at wrong coordinates | Verify coordinates against graphic control measure list before grading |
| Task 3 | CCIR boundary not aligned to PL AMBER | Most common Task 3 failure; ask participant to show the CCIR definition and boundary — confirm it matches PL AMBER grid, not a default or estimated boundary |
| Task 3 | Notification to personal account instead of position | Position-based routing required; personal-only = coaching note, not No-Go if both are set |
| Task 4 | Task org reflects default MSS configuration, not OPORD | Ask participant to show where they updated from the OPORD; if they cannot, No-Go |
| Task 5 | Participant briefs 2nd Bn "at last known position" without caveat | Most common Task 5 failure — presenting stale position before an attack order is an operational risk; No-Go and debrief |
| Task 5 | Participant attempts to fix the position feed | Wrong response; if more than 5 minutes spent troubleshooting, prompt: "What does the S3 need to know right now?" |
| Task 6 | Evaluator liaison account has edit access | Task 6 No-Go |
