# ENVIRONMENT SETUP — EX_40D Sustainment (TM-40D)

**Companion resources:** TM_40D_SUSTAINMENT.md | SYLLABUS_TM40D | EXAM_TM40D_PRE / EXAM_TM40D_POST

## Environment Type

MSS training instance. Standard user access only — no Pipeline Builder, Python Transforms, or build permissions required for participants.

## Required Access

| Account | Role |
|---------|------|
| Training accounts | Viewer + Workshop create (for readiness dashboard and supply status product builds) |
| Evaluator account | Editor (to inject the data staleness event, verify participant submissions, and test Task 6 read-only share as a sustainment sync attendee) |

## Pre-Load Instructions

### 1. Synthetic LOGSTAT Dataset

Load `EX_40D_BCT_Sustainment_Training_Data/` package (from training data package):

| File | Description | Schema |
|------|-------------|--------|
| `unit_readiness.csv` | Daily readiness % per subordinate unit, 30 days | `date`, `unit`, `personnel_pct`, `equip_pct` |
| `supply_status.csv` | Class I, III, V levels by unit, daily | `date`, `unit`, `class_i_dos`, `class_iii_dos`, `class_v_dos` |
| `transportation_status.csv` | Available vs. mission/maintenance status per motor pool | `date`, `unit`, `vehicle_type`, `available_pct`, `mx_pct` |
| `ccir_test_supply.csv` | Single record for CCIR 2 verification | 2-67 AR FSC Class V at 1.8 DOS |

**Unit readiness design values:**

| Unit | Readiness | Status |
|------|-----------|--------|
| 1-67 AR FSC | 78% | Above 75% threshold |
| 2-67 AR FSC | 68% | Below 75% — CCIR 1 should trigger |
| 3-67 AR FSC | 82% | Above threshold |
| BSB | 91% | Above threshold |
| HHC | 85% | Above threshold |

**Supply status:** 1-67 AR FSC Class III at 2.4 DOS (below 3 DOS — CCIR 2 should trigger); all other units above 3 DOS on all supply classes.

Place all files in: `[Training Project]/EX_40D/source/`

### 2. Commander's Sustainment CCIR Guidance Card

Print and hand to participant at exercise start (Task 3):

```
COMMANDER'S SUSTAINMENT CCIR GUIDANCE — EX_40D TRAINING

CCIR 1 — UNIT READINESS BELOW THRESHOLD
  Trigger: Any subordinate unit equipment or personnel readiness falls below 75%
  Data source: Unit Readiness feed
  Notify: S4, XO

CCIR 2 — CRITICAL SUPPLY BELOW 3 DOS
  Trigger: Any subordinate unit Class III (POL) or Class V (AMMO) supply-on-hand
           falls below 3 days of supply (DOS)
  Data source: Supply Status feed
  Notify: S4, XO

NOTE: Both CCIRs require position-based routing to S4 and XO — not personal accounts.
      Verify data sources are correctly selected before marking CCIRs as active.
```

### 3. CCIR Test Dataset

| CCIR | Test Value | Expected Result |
|------|-----------|-----------------|
| CCIR 1 | 2-67 AR FSC readiness at 68% | Should trigger |
| CCIR 2 | `ccir_test_supply.csv` — 2-67 AR FSC Class V at 1.8 DOS | Should trigger |

### 4. Data Staleness Inject (Task 5 — at T+90 min)

1. Navigate to: `[Training Project]/EX_40D/source/unit_readiness` and `supply_status` datasets
2. Change the 1-67 AR FSC `last_updated` field to 3 hours prior on both datasets (do not change data values — existing records remain but show as stale)
3. If direct timestamp manipulation is not possible, disconnect the 1-67 AR FSC feed from the COP readiness layer and supply status product widget using the evaluator account
4. Confirm the participant's dashboard shows 1-67 AR FSC data as stale or stops refreshing before they respond

**Expected participant response:**
- Identify that 1-67 AR FSC readiness and supply data is stale (feed stopped 3 hours ago)
- Add caveats to the readiness dashboard (1-67 AR FSC element labeled as not current) and supply status product (1-67 AR FSC row annotated with data-as-of caveat)
- Brief XO (four required elements): what is affected (1-67 AR FSC readiness and supply status — primary unit for the upcoming sustainment sync discussion), what is still current (all other unit feeds), what will/will not be briefed at the sustainment sync (brief gap and last-known status; do not brief 1-67 AR FSC data as current), and resolution action (escalate to S6 to restore feed; contact 1-67 AR FSC NCOIC for a verbal spot report as backup)
- Do NOT attempt to fix the LOGSTAT pipeline — characterize the gap and escalate

## Environment URL

```
[Insert training MSS tenant URL here]
```

## Notes

- This exercise has no coding or pipeline component — all tasks use the MSS UI
- Transportation status (Task 1) is a display-only layer — participants configure the layer and verify timestamps only; they are not required to build a transportation dashboard
- The evaluator must have a second account to test the Task 6 Viewer share (simulating a subordinate unit representative at the sustainment sync)
- If the training environment does not support DOS-based threshold CCIRs (Task 3, CCIR 2), substitute with a percentage-based supply threshold (e.g., Class III below 30%) and note the deviation on the evaluation form
