# ENVIRONMENT SETUP — EX-40C Movement & Maneuver (TM-40C)

**Companion resources:** TM_40C_MOVEMENT_MANEUVER.md | SYLLABUS_TM40C | EXAM_TM40C_PRE / EXAM_TM40C_POST

## Environment Type

MSS training instance. Standard user access only — no Pipeline Builder, Python Transforms, or build permissions required for participants.

## Required Access

| Account | Role |
|---------|------|
| Training accounts | Viewer + Workshop create (for task org and COP product configuration) |
| Evaluator account | Editor (to inject the data staleness event, verify participant submissions, and test Task 6 share as a liaison officer) |

## Pre-Load Instructions

### 1. Synthetic Maneuver Dataset

Load `EX-40C_BCT_Maneuver_Training_Data/` package (from training data package):

| File | Description | Notes |
|------|-------------|-------|
| `battalion_positions.geojson` | 3 maneuver battalions with notional grid positions, updated at 30-min intervals | 1-67 AR, 2-67 AR, 3-67 AR — all south of LD pre-attack; 2-67 AR feed paused at T+90 |
| `route_corridors.geojson` | MSR VIKING and two axis-of-advance corridors | Static layer |
| `obstacle_overlay.geojson` | Obstacle belt, minefield boundary, restricted terrain zones | Static layer |
| `ccir_test_event.geojson` | Single 2nd Bn position record north of PL AMBER | Used for CCIR verification, Task 3 |

Place all files in: `[Training Project]/EX-40C/source/`

Verify all three battalion position layers show current timestamps before the exercise begins.

### 2. Graphic Control Measure List

Print and hand to participant at exercise start (Tasks 2 and 3):

```
GRAPHIC CONTROL MEASURES — EX-40C TRAINING
Classification: UNCLASSIFIED // TRAINING

LD — LINE OF DEPARTURE
  Grid: 48.200N / 008.300E (east-west line)
  Label: LD

PL AMBER — PHASE LINE AMBER
  Grid: 48.450N / 008.300E (east-west line, 25 km north of LD)
  Label: PL AMBER

PL BLACK — PHASE LINE BLACK
  Grid: 48.650N / 008.300E (east-west line, 45 km north of LD)
  Label: PL BLACK

OBJECTIVE IRON
  Grid: 48.730N / 008.350E (500m x 500m box)
  Label: OBJ IRON
```

### 3. Commander's CCIR Guidance Card

Print and hand to participant at exercise start (Task 3):

```
COMMANDER'S CCIR GUIDANCE — EX-40C TRAINING
Classification: UNCLASSIFIED // TRAINING

CCIR 1 — MANEUVER PHASE LINE CROSSING
  Trigger: Any maneuver battalion position report places unit on or north of PL AMBER
           (Grid reference: 48.450N / 008.300E or north)
  Data source: Battalion Position feed
  Notify: S3, Battle Captain

NOTE: Configure trigger as a geographic boundary alert aligned to PL AMBER.
      Do not configure as a threshold-based alert — this is a location-based trigger.
```

### 4. OPORD Task Org Annex

Print and hand to participant at exercise start (Task 4):

```
TASK ORGANIZATION — EX-40C TRAINING (ATTACK ORDER)
Classification: UNCLASSIFIED // TRAINING

BCT MAIN:
  ASSIGNED:
    1-67 AR (Main Effort — Axis HAWK)
    3-67 AR (Supporting Effort — Axis FALCON)
  OPCON:
    2-67 AR (Breach Force — Axis HAWK; transitions to supporting effort after LD+2)
  ATTACHED:
    1-25 FA BN (direct support; fires on call for all maneuver elements)
    B/40 EN BN (attached to 2-67 AR for breach operations)

SYNCHRONIZATION NOTE:
  2-67 AR transitions from BCT OPCON to 1-67 AR OPCON at PL AMBER crossing.
  Position feed for 2-67 AR must be visible under both BCT and 1-67 AR layers
  until transition is confirmed — verify layer configuration reflects this.
```

### 5. CCIR Test Dataset

To verify CCIR configuration (Task 3):
- Load `ccir_test_event.geojson` (2nd Bn position at 48.520N / 008.310E — north of PL AMBER)
- CCIR 1 should trigger; S3 and Battle Captain notification should fire
- If geographic CCIR is not supported, substitute with a position-field-based filter on battalion designation and note the deviation on the evaluation form

### 6. Data Staleness Inject (Task 5 — at T+90 min)

1. Navigate to: `[Training Project]/EX-40C/source/battalion_positions` dataset
2. Change the 2-67 AR position feed `last_updated` field to 90 minutes prior (do not change position coordinates — the point remains on the map but becomes stale)
3. If direct timestamp manipulation is not possible, disconnect the 2-67 AR position feed from the COP layer using the evaluator account
4. Confirm the participant's COP shows 2-67 AR data as stale or stops refreshing before they respond

**Expected participant response:**
- Identify that 2-67 AR position data is stale (last reported 90 minutes ago)
- Add a caveat annotation to the 2-67 AR COP layer indicating position is not current
- Brief (four required elements): what is affected (2nd Bn position going into LD; CCIR 1 cannot fire for 2nd Bn while feed is stale), what is still current (1st and 3rd Bn feeds), what will/will not be briefed to the commander (brief gap, caveat last known position), and resolution action (escalate to S6; contact 2nd Bn TOC for spot report as backup)
- Do NOT attempt to fix the pipeline — that is the S6's role at this level

## Environment URL

```
[Insert training MSS tenant URL here]
```

## Notes

- This exercise has no coding or pipeline component — all tasks use the MSS UI
- If geographic CCIR boundary configuration is not available (Task 3), substitute with a position-report-field-based trigger and note the deviation on the evaluation form
- The evaluator must have a second account to test the Task 6 Viewer share (simulating the liaison officer's account)
- The obstacle overlay and route corridors are static layers — they do not require a live feed and do not need timestamp verification; brief participants accordingly if they spend time on static layer timestamps
