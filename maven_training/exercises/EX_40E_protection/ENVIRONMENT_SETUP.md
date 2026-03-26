# ENVIRONMENT SETUP — EX_40E Protection (SL 4E)

**Companion resources:** TM_40E_PROTECTION.md | SYLLABUS_TM40E | EXAM_TM40E_PRE / EXAM_TM40E_POST

## Environment Type

MSS training instance. Standard user access only — no Pipeline Builder, Python Transforms, or build permissions required for participants.

## Required Access

| Account | Role |
|---------|------|
| Training accounts | Viewer + Workshop create (for vulnerability assessment and PERSTAT display builds) |
| Evaluator account | Editor (to inject the data staleness event, verify participant submissions, and test the Task 6 read-only share as a protection working group attendee) |

## Pre-Load Instructions

### 1. Synthetic Threat and PERSTAT Dataset

Load `EX_40E_BCT_Protection_Training_Data/` package (from training data package):

| File | Description | Schema |
|------|-------------|--------|
| `threat_incidents.geojson` | 25 synthetic threat events (IED finds, hostile activity, indirect fire) across three sectors | `event_id`, `date`, `sector`, `lat`, `lon`, `event_type`, `description` |
| `perstat_feed.csv` | Personnel accountability by battalion, daily | `date`, `unit`, `assigned`, `present_for_duty`, `pfd_pct` |
| `route_vulnerability_overlay.geojson` | MSR VIKING and MSR BRONZE segments with historical incident density; FOB KESTREL installation perimeter | — |
| `ccir_test_event.geojson` | Single threat event within the restricted area | Used for CCIR 1 verification |
| `ccir_test_casualty.csv` | Single record with WIA count at 18 | Used for CCIR 2 verification |

**Threat incident design values:**
- Sector NORTH: 8 events (1 within the designated restricted area — CCIR 1 should trigger)
- Sector CENTRAL: 10 events
- Sector SOUTH: 7 events (feed will be paused at T+90)

**PERSTAT design values:**

| Unit | PFD |
|------|-----|
| 1-67 AR | 98% |
| 2-67 AR | 94% |
| 3-67 AR | 91% |
| BSB | 97% |
| HHC | 100% |

Place all files in: `[Training Project]/EX_40E/source/`

Verify all three sector feeds show current timestamps and all organic battalions appear in the PERSTAT feed before the exercise.

### 2. Commander's Force Protection CCIR Guidance Card

Print and hand to participant at exercise start (Task 2):

```
COMMANDER'S FORCE PROTECTION CCIR GUIDANCE — EX_40E TRAINING

CCIR 1 — THREAT EVENT IN RESTRICTED AREA
  Trigger: Any threat incident reported within the following restricted area boundary:
           [Lat 48.60 to 48.75 N, Lon 008.50 to 008.70 E] — FOB KESTREL 5km exclusion zone
  Data source: Threat Incidents feed
  Notify: Force Protection Officer, S3

CCIR 2 — CASUALTY ABOVE THRESHOLD
  Trigger: BCT WIA exceeds 15 personnel OR KIA exceeds 5 personnel
           within any rolling 72-hour period
  Data source: Casualty Reporting feed
  Notify: Force Protection Officer, S3

NOTE: CCIR 1 is a geographic trigger. Verify the boundary matches the exclusion zone
      boundary above — do not use a default or approximate boundary.
      CCIR 2 uses casualty data, not PERSTAT — confirm correct data source is selected.
```

### 3. CCIR Test Dataset

| CCIR | Test Value | Expected Result |
|------|-----------|-----------------|
| CCIR 1 | `ccir_test_event.geojson` — event at Lat 48.67, Lon 008.61 (within restricted area) | Should trigger |
| CCIR 2 | `ccir_test_casualty.csv` — WIA count at 18 | Should trigger |

### 4. Data Staleness Inject (Task 5 — at T+90 min)

1. Navigate to: `[Training Project]/EX_40E/source/threat_incidents` dataset
2. Change the `last_updated` field on all Sector SOUTH records to 2 hours prior (do not delete records — the points remain on the map but the feed shows as stale)
3. If direct timestamp manipulation is not possible, disconnect the Sector SOUTH filter from the threat incidents layer using the evaluator account
4. Confirm the participant's COP shows Sector SOUTH threat data as stale or stops refreshing before they respond

**Expected participant response:**
- Identify that Sector SOUTH threat data is stale (last report 2 hours ago)
- Add a caveat annotation to the Sector SOUTH threat layer indicating data is not current
- Brief S3 (four required elements): what is still current (Sector NORTH and CENTRAL threat feeds; all PERSTAT data), what is not current (Sector SOUTH — unknown threat activity for past 2 hours), what will/will not be briefed at the protection working group (brief Sector SOUTH as unconfirmed/no update — do not present last-known as current; caveat all Sector SOUTH trend analysis), and resolution action (escalate to S2/S6 to restore feed; request a spot report from Sector SOUTH patrol element as backup)
- Do NOT speculate about threat activity in Sector SOUTH based on the data gap
- Do NOT attempt to troubleshoot the feed — characterize and escalate

## Environment URL

```
[Insert training MSS tenant URL here]
```

## Notes

- This exercise has no coding or pipeline component — all tasks use the MSS UI
- The route vulnerability overlay (Task 4) is a static layer — it does not require a live feed and does not need timestamp verification; coach participants accordingly if they spend time on static overlay timestamps
- The evaluator must have a second account to test the Task 6 Viewer share (simulating a protection working group attendee from a subordinate unit)
- If the training environment does not support geographic CCIR boundary configuration (Task 2, CCIR 1), substitute with an event-type-based filter on the restricted area and note the deviation on the evaluation form
- Threat incidents, PERSTAT, and vulnerability overlays together constitute a sensitive aggregate — remind evaluators to treat the exercise dataset with appropriate handling even in the training environment
