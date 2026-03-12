# ENVIRONMENT SETUP — EX-40B Fires

## Environment Type

MSS training instance. Standard user access only — no Pipeline Builder, Python Transforms, or build permissions required for participants.

## Required Access

| Account | Role |
|---------|------|
| Training accounts | Viewer + Workshop create (for targeting product and effects assessment display build) |
| Evaluator account | Editor (to inject the data staleness event, verify participant submissions, and test Task 6 read-only share as S3) |

## Pre-Load Instructions

### 1. Synthetic Fires Dataset

Load `EX-40B_BCT_Fires_Training_Data/` package (from training data package):

| File | Description | Schema |
|------|-------------|--------|
| `target_list.csv` | 15 synthetic target entries in AOR | `target_id`, `date`, `lat`, `lon`, `target_type`, `status` (confirmed/suspected), `source` (SIGINT/HUMINT/ISR), `bda_status` (confirmed/estimated/no_bda), `fires_element` |
| `fscm_overlay.geojson` | Synthetic FSCMs for training AOR | `fscm_id`, `fscm_type`, `authority`, `effective_from`, `effective_to`, `geometry` |
| `bda_reporting.csv` | BDA feed from two fires elements | `bda_id`, `target_id`, `fires_element`, `bda_status`, `report_dtg`, `last_updated` |

**Dataset design requirements:**

| Attribute | Specification |
|-----------|--------------|
| `target_list.csv` | 8 confirmed, 7 suspected; 6 SIGINT, 5 HUMINT, 4 ISR; BDA: 5 confirmed, 4 estimated, 6 no BDA; at least 4 targets sourced to the fires element whose BDA feed will be paused at T+90 |
| `fscm_overlay.geojson` | At least one NFA, one RFA, one FFA |
| `bda_reporting.csv` | Element ALPHA — 6 BDA entries, all current; Element BRAVO — 4 BDA entries (will go stale at T+90) |

Place all files in: `[Training Project]/EX-40B/source/`

### 2. Commander's Fires CCIR Guidance Card

Print and hand to participant at exercise start:

```
COMMANDER'S FIRES CCIR GUIDANCE — EX-40B TRAINING
Classification: UNCLASSIFIED // TRAINING

FIRES CCIR 1 — TARGET ENGAGED
  Trigger: Any target in the active target list changes status to "engaged"
  Data source: Target List feed (field: status = "engaged")
  Notify: FSE, S3

FIRES CCIR 2 — EFFECTS CONFIRMED
  Trigger: Any target achieves BDA confirmed status in the BDA reporting feed
  Data source: BDA Reporting feed (field: bda_status = "confirmed")
  Notify: FSE, S3

FIRES CCIR 3 — FSCM VIOLATION
  Trigger: Any friendly fires solution plots within the Restrictive Fire Area (RFA)
           boundary defined in the FSCM overlay
  Data source: FSCM Overlay (RFA boundary) — geographic trigger
  Notify: FSE, S3
```

### 3. Fires CCIR Test Dataset

| CCIR | Test Value | Expected Result |
|------|-----------|-----------------|
| Fires CCIR 1 | Set TGT-07 status to "engaged" | Should trigger |
| Fires CCIR 2 | Set TGT-03 BDA status to "confirmed" in the BDA feed | Should trigger |
| Fires CCIR 3 | Plot a test point inside the RFA boundary | Should trigger; confirm participant's CCIR fires before grading |

### 4. Data Staleness Inject (Task 5 — at T+90 min)

1. Navigate to: `[Training Project]/EX-40B/source/bda_reporting` dataset
2. Change the `last_updated` timestamp for all Element BRAVO entries to 3 hours prior (do not alter BDA status values — only the currency timestamp)
3. If direct timestamp manipulation is not possible, disconnect the Element BRAVO BDA feed from the effects assessment display using the evaluator account
4. Confirm the participant's effects assessment display shows Element BRAVO BDA entries as stale before they begin the response

**Expected participant response:**
- Identify that all Element BRAVO BDA entries are stale — affects 4 targets in the effects assessment display and targeting product
- Add data currency caveats to the targeting product for Element BRAVO-sourced BDA entries
- Brief (four required elements): what is affected (Element BRAVO BDA data for 4 targets), what is still current (Element ALPHA BDA data remains valid), what the targeting working group will and will not receive as current BDA (ALPHA data current; BRAVO data flagged), and resolution action (notify Element BRAVO and escalate to S3 and S6)
- Do NOT attempt to fix the pipeline — that is the S6's role at this level

## Environment URL

```
[Insert training MSS tenant URL here]
```

## Scoring Sheet Reference

Evaluators record task Go/No-Go on standard EX-40B Evaluation Form (available from training NCO). Record specific failure modes in the notes column for post-exercise AAR. Overall Go/No-Go, participant name, evaluator name, and date required for training record submission.

## Notes

- This exercise has no coding or pipeline component — all tasks use the MSS UI
- If the training environment does not support geographic CCIR configuration (Task 3, Fires CCIR 3), substitute with an event-type-based trigger using a "restricted area" event type and note the deviation on the evaluation form
- The evaluator must have a second account to test the Task 6 read-only share (simulating the S3 account)
- All fires, targeting, and BDA data are entirely synthetic — no real fires data or targeting information is used in this exercise
