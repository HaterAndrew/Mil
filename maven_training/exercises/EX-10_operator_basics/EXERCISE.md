# EX-10 — MSS Operator Basics
## Practical Exercise — TM-10 Proficiency

| | |
|---|---|
| **Version** | 1.0 — March 2026 |
| **Prerequisite** | TM-10 |
| **Duration** | 45–60 min |
| **Environment** | MSS training instance or sandbox — see ENVIRONMENT_SETUP.md |

## SCENARIO

You are a staff officer at a BCT HQ. Your S2 needs current equipment readiness for three subordinate battalions for the daily SITREP. Navigate, filter, and export data from an existing readiness dashboard.

Unclassified training data simulates LOGSTAT/readiness report formats.

## TASK LIST

### Task 1 — Log In and Orient (10 min)
- [ ] Log in to MSS using CAC credentials
- [ ] Locate the training dashboard: "BCT Readiness — EX-10 Training"
- [ ] Identify the data owner and last-updated timestamp
- **Go:** Locates dashboard and reads metadata without assistance
- **No-Go:** Cannot find dashboard or misidentifies data owner

### Task 2 — Apply Filters (15 min)
- [ ] Filter the readiness view to show only **1st Battalion** data
- [ ] Change the date range to show the last 7 days
- [ ] Reset filters to show all units
- **Go:** Filters apply correctly; data refreshes; reset without help
- **No-Go:** Cannot locate filter controls or filters do not apply

### Task 3 — Identify Anomalies (10 min)
- [ ] Find the unit with the lowest reported readiness percentage
- [ ] Note the equipment category driving the low readiness
- [ ] Record the data steward contact for that data product
- **Go:** Correctly identifies the lowest unit and dominant category; records steward
- **No-Go:** Identifies wrong unit or cannot locate steward information

### Task 4 — Export a View (10 min)
- [ ] Export the current filtered view (all units, current week) as a PDF
- [ ] Verify the export includes the "Last updated" timestamp
- [ ] Handle the export per unit classification SOP
- **Go:** Export completes; timestamp visible in output
- **No-Go:** Export fails or timestamp is absent

### Task 5 — Navigate and Bookmark (5 min)
- [ ] Find one additional dashboard relevant to your role
- [ ] Bookmark it to your MSS home
- **Go:** Bookmark appears on home screen after navigation
- **No-Go:** Cannot locate secondary dashboard or bookmark fails

## EVALUATOR NOTES

**Scoring:** 5 tasks. Go on 4 of 5 = overall Go. No-Go on Task 2 or Task 4 = automatic No-Go.

**Pre-exercise checklist:**
- Confirm all training accounts can access "BCT Readiness — EX-10 Training"
- Verify dashboard shows data for at least 3 units with clearly different readiness values
- Confirm data steward contact field is populated in dashboard metadata
- Note Task 3 correct answer — see ENVIRONMENT_SETUP.md answer key

**Common failure modes:**

| Task | Common Failure | Evaluator Guidance |
|------|---------------|--------------------|
| Task 1 | Cannot find the dashboard | Note navigation path taken; searching by name is acceptable; browsing wrong project is No-Go |
| Task 2 | Filters applied but not reset | Page reload to reset = Go with coaching note; clicking Reset correctly = Go |
| Task 3 | Identifies wrong low-readiness unit | Check against answer key; any incorrect unit = No-Go |
| Task 4 | Export missing timestamp | Most common cause: CSV instead of PDF; note format used |
| Task 5 | Bookmark does not appear on home | If correct action is demonstrated, retest after cache clear before marking No-Go |

**Timing notes:**
- Task 3 runs 5–15 min depending on analytical background; do not prompt within first 10 min
- If Task 2 exceeds 15 min, ask participant to narrate approach (do not guide)
- Total exercise rarely exceeds 50 min for participants current on TM-10
