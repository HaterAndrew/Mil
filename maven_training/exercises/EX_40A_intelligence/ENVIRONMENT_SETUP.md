# ENVIRONMENT SETUP — EX_40A Intelligence (SL 4A)

**Companion resources:** TM_40A_INTELLIGENCE.md | SYLLABUS_TM40A | EXAM_TM40A_PRE / EXAM_TM40A_POST

## Environment Type

MSS training instance. Standard user access only — no Pipeline Builder, Python Transforms, or build permissions required for participants.

## Required Access

| Account | Role |
|---------|------|
| Training accounts | Viewer + Workshop create (for targeting product and collection status display build) |
| Evaluator account | Editor (to inject the data staleness event, verify participant submissions, and test Task 6 read-only share as FSO) |

## Pre-Load Instructions

### 1. Synthetic Intelligence Dataset

Load `EX_40A_BCT_Intel_Training_Data/` package (from training data package):

| File | Description | Schema |
|------|-------------|--------|
| `threat_activity_events.csv` | 30 synthetic threat events in AOR | `event_id`, `date`, `lat`, `lon`, `event_type`, `source`, `confidence` (confirmed/suspected) |
| `nai_tai_overlays.geojson` | 4 NAIs and TAIs | `id`, `name`, `type` (NAI/TAI), `associated_pir`, `coverage_asset`, `lat_min`, `lat_max`, `lon_min`, `lon_max` |
| `ipb_terrain_overlay.geojson` | Terrain analysis overlay with threat pattern annotations | — |
| `sigint_reporting.csv` | SIGINT-sourced event subset | mirrors `threat_activity_events.csv` |
| `humint_reporting.csv` | HUMINT-sourced event subset | mirrors `threat_activity_events.csv` |

**Dataset design requirements:**
- Mix of SIGINT-sourced and HUMINT-sourced events
- At least 3 events in grid zone XX (PIR 1 should trigger)
- At least 2 events within 5 km of Phase Line RED (PIR 2 should trigger)
- At least 2 indirect fire events north of grid northing YY (PIR 3 should trigger)

Place all files in: `[Training Project]/EX_40A/source/`

### 2. Commander's PIR Guidance Card

Print and hand to participant at exercise start:

```
COMMANDER'S PIR GUIDANCE — EX_40A TRAINING

PIR 1 — ENEMY ADA IN AOR
  Trigger: Any confirmed enemy ADA asset within grid zone XX
           [Lat 48.8 to 49.2 N, Lon 8.2 to 8.8 E] (training AOR)
  Data source: Threat Activity feed (source = SIGINT or HUMINT; confidence = confirmed)
  Notify: S2, S3

PIR 2 — ENEMY ARMOR NEAR PHASE LINE RED
  Trigger: Any enemy armor element within 5 km of Phase Line RED
           [Phase Line RED: Lat 49.0 N, full AOR width, Lon 8.0 to 9.0 E]
  Data source: Threat Activity feed (event_type = armor)
  Notify: S2, S3

PIR 3 — ENEMY INDIRECT FIRE FROM NORTH
  Trigger: Any enemy indirect fire event originating north of grid northing YY
           [Lat 49.3 N and north, full AOR width]
  Data source: Threat Activity feed (event_type = indirect_fire)
  Notify: S2, S3
```

### 3. PIR Test Dataset

| PIR | Test Value | Expected Result |
|-----|-----------|-----------------|
| PIR 1 | Confirmed ADA event at Lat 49.0, Lon 8.5 | Should trigger |
| PIR 2 | Armor event at Lat 48.97, Lon 8.4 (within 5 km of Phase Line RED at Lat 49.0) | Should trigger |
| PIR 3 | Indirect fire event at Lat 49.4, Lon 8.6 | Should trigger |

### 4. Data Staleness Inject (Task 5 — at T+90 min)

1. Navigate to: `[Training Project]/EX_40A/source/sigint_reporting` dataset
2. Change the SIGINT feed `last_updated` timestamp to 4 hours prior (do not alter data values — only the currency timestamp)
3. If direct timestamp manipulation is not possible, disconnect the SIGINT reporting feed from the threat activity layer using the evaluator account
4. Confirm the participant's COP and targeting product show SIGINT-sourced entries as stale before they begin the response

**Expected participant response:**
- Identify that all SIGINT-sourced entries in the threat activity layer and targeting product are affected
- Add data currency caveats to the targeting product for SIGINT-attributed targets
- Brief (four required elements): what is affected (SIGINT-sourced intelligence), what is still current (HUMINT-sourced entries remain valid), what will/will not be briefed at the targeting working group (HUMINT-sourced targets current; SIGINT-attributed targets flagged as data currency caveat), and resolution action (escalate to S6 and notify collection manager)
- Do NOT attempt to fix the pipeline — that is the S6's role at this level

## Environment URL

```
[Insert training MSS tenant URL here]
```

## Scoring Sheet Reference

Evaluators record task Go/No-Go on standard EX_40A Evaluation Form (available from training NCO). Record specific failure modes in the notes column for post-exercise AAR. Overall Go/No-Go, participant name, evaluator name, and date required for training record submission.

## Notes

- This exercise has no coding or pipeline component — all tasks use the MSS UI
- If the training environment does not support geographic PIR/CCIR configuration (Tasks 2 PIR 1–3), substitute with event-type-based triggers and note the deviation on the evaluation form
- The evaluator must have a second account to test the Task 6 read-only share (simulating the FSO account)
- HUMINT and SIGINT data are entirely synthetic — no real intelligence reporting is used in this exercise
