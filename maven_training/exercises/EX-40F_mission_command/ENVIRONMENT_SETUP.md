# ENVIRONMENT SETUP — EX-40F Mission Command

## Environment Type
MSS training instance. Standard user access only — no Pipeline Builder, Python Transforms, or build permissions required for participants.

## Required Access
- Training accounts: Viewer + Workshop create (for BUA product build)
- Evaluator account: Editor (to inject the data staleness event and verify participant submissions)

## Pre-Load Instructions

### 1. Synthetic Operational Dataset
Load synthetic BCT operational data:
- File: `EX-40F_BCT_Ops_Training_Data/` package (from training data package)
- Contents:
  - `unit_positions.geojson` — 3 subordinate battalions (1-1, 1-2, 1-3) with notional grid positions
  - `readiness_status.csv` — daily readiness % per battalion, 30 days; schema: `date`, `battalion`, `personnel_pct`, `equip_pct`
    - 1-1 Bn: readiness ~80% (within threshold)
    - 1-2 Bn: readiness ~67% (below 70% threshold — CCIR 1 should trigger)
    - 1-3 Bn: readiness ~91% (within threshold)
  - `operational_events.csv` — synthetic SIGACT-analog events, 30 days; schema: `event_id`, `date`, `lat`, `lon`, `event_type`
    - At least one event within the defined sensitivity area grid (CCIR 2 should trigger)
  - `personnel_strength.csv` — daily strength % per battalion; 1-3 Bn at 82% (below 85% — CCIR 3 should trigger)
- Place all files in: `[Training Project]/EX-40F/source/`
- All three CCIRs should trigger on the provided dataset — verify before the exercise

### 2. Commander's CCIR Guidance Card
Print and hand to participant at exercise start:

```
COMMANDER'S CCIR GUIDANCE — EX-40F TRAINING
Classification: UNCLASSIFIED // TRAINING

CCIR 1 — READINESS THRESHOLD
  Trigger: Any subordinate battalion equipment readiness below 70%
  Data source: Readiness Status feed
  Notify: Battle Captain, S3

CCIR 2 — EVENT IN SENSITIVITY AREA
  Trigger: Any operational event with coordinates within grid:
           [Lat 48.5 to 49.5 N, Lon 8.0 to 9.0 E] (training AOR)
  Data source: Operational Events feed
  Notify: Battle Captain, S3

CCIR 3 — PERSONNEL STRENGTH
  Trigger: Any subordinate battalion personnel strength below 85%
  Data source: Personnel Strength feed
  Notify: Battle Captain, S3
```

### 3. CCIR Test Dataset
To verify CCIR configuration (Task 2), have the following values ready:
- CCIR 1 test: 1-2 Bn at 67% — should trigger
- CCIR 2 test: Event at Lat 49.0, Lon 8.5 — should trigger
- CCIR 3 test: 1-3 Bn at 82% — should trigger

### 4. Data Staleness Inject (Task 5 — at T+90 min)
To inject the data staleness event at T+90 min:
1. Navigate to: `[Training Project]/EX-40F/source/readiness_status` dataset
2. Change the 1-1 Bn readiness feed timestamp to 6 hours prior (do not change the data values, only the `last_updated` field)
3. If direct timestamp manipulation is not possible, disconnect the 1-1 Bn readiness feed from the COP layer using the evaluator account
4. Confirm the participant's COP shows 1-1 Bn data as stale before they respond

**Expected participant response:**
- Identify that 1-1 Bn readiness data is stale
- Add a caveat to the BUA product for affected sections
- Brief: what is affected, what is still current, what will/will not be briefed, resolution action (escalate to S6)
- Do NOT attempt to fix the pipeline — that is the S6's role at this level

## Environment URL
```
[Insert training MSS tenant URL here]
```

## Battle Rhythm Event List
Provide to participant at exercise start for Task 3:

```
WEEKLY BATTLE RHYTHM — EX-40F TRAINING (Mon–Sun)
UNCLASSIFIED // TRAINING

DAILY
  0700 — Commander's Battle Update Assessment (BUA) — CDR, XO, S3, S2
  1500 — Operations Update Brief (OUB) — S3-led

WEEKLY
  MON 0800 — Weekly Planning Synchronization — XO-led
  TUE 1300 — Fires and Targeting Board — FSO, S2, S3
  WED 1400 — Sustainment Synchronization — S4, G4 rep
  THU 0900 — Warfighter Forum (theater VTC) — CDR or XO required

DECISION GATES (next 14 days)
  D+5:  LOGSTAT submission to theater (deadline)
  D+7:  OPORD amendment publish (CDR approval required)
  D+12: Readiness certification submission (G4 deadline)
```

## Notes
- This exercise has no coding or pipeline component — all tasks use the MSS UI
- If the training environment does not support geographic CCIR configuration (Task 2, CCIR 2), substitute with an event-type-based trigger and note the deviation on the evaluation form
- The evaluator must have a second account to test the Task 6 read-only share (simulating the commander's account)
