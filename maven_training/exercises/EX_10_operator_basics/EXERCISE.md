# EX_10 — MSS Operator Basics
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
*Reference: TM-10 Chapter 2 (Accessing MSS), Chapter 3 (Navigating the Platform)*
- [ ] Log in to MSS using CAC credentials
- [ ] Locate the training dashboard: "BCT Readiness — EX_10 Training"
- [ ] Identify the data owner and last-updated timestamp
- **Go:** Locates dashboard and reads metadata without assistance
- **No-Go:** Cannot find dashboard or misidentifies data owner

### Task 2 — Apply Filters (15 min) ⚠️ *Critical item*
*Reference: TM-10 Chapter 4 (Using Workshop Applications), sections 4-1 through 4-3*
- [ ] Filter the readiness view to show only **1st Battalion** data
- [ ] Change the date range to show the last 7 days
- [ ] Reset filters to show all units
- **Go:** Filters apply correctly; data refreshes; reset without help
- **No-Go:** Cannot locate filter controls or filters do not apply

### Task 3 — Identify Anomalies (10 min)
*Reference: TM-10 Chapter 5 (Working with Data), sections 5-1 through 5-2*
- [ ] Find the unit with the lowest reported readiness percentage
- [ ] Note the equipment category driving the low readiness
- [ ] Record the data steward contact for that data product
- **Go:** Correctly identifies the lowest unit and dominant category; records steward
- **No-Go:** Identifies wrong unit or cannot locate steward information

### Task 4 — Export a View (10 min) ⚠️ *Critical item*
*Reference: TM-10 Chapter 6 (Security, Classification, and Markings), sections 6-1 through 6-3*
- [ ] Export the current filtered view (all units, current week) as a PDF
- [ ] Verify the export includes the "Last updated" timestamp
- [ ] Handle the export per unit classification SOP
- **Go:** Export completes; timestamp visible in output
- **No-Go:** Export fails or timestamp is absent

### Task 5 — Navigate and Bookmark (5 min)
*Reference: TM-10 Chapter 3 (Navigating the Platform)*
- [ ] Find one additional dashboard relevant to your role
- [ ] Bookmark it to your MSS home
- **Go:** Bookmark appears on home screen after navigation
- **No-Go:** Cannot locate secondary dashboard or bookmark fails

### Task 6 — Classification Marking Identification (5 min) ⚠️ *Critical item*
*Reference: TM-10 Chapter 6 (Security, Classification, and Markings)*
- [ ] When prompted by the evaluator, state the classification marking displayed on the provided dataset
- [ ] State the authorized distribution for that classification level
- [ ] State the authorized export destination (if any) for that marking
- **Go:** Correct classification marking identified; correct authorized distribution stated
- **No-Go:** Incorrect classification identification or incorrect authorization statement

## EVALUATOR NOTES

**Scoring:** 6 tasks. Go on 5 of 6 = overall Go. No-Go on Task 2, Task 4, or Task 6 = automatic No-Go.

**Pre-exercise checklist:**
- Confirm all training accounts can access "BCT Readiness — EX_10 Training"
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
| Task 6 | States wrong classification level | Evaluator shows dataset on screen; trainee responds verbally or in writing; any incorrect marking = automatic No-Go |

**Timing notes:**
- Task 3 runs 5–15 min depending on analytical background; do not prompt within first 10 min
- If Task 2 exceeds 15 min, ask participant to narrate approach (do not guide)
- Task 6 is verbal/written — evaluator asks the question after Task 5 completion
- Total exercise rarely exceeds 55 min for participants current on TM-10

---

## NEXT STEPS

Upon successful completion of EX_10, participants are cleared to proceed to:

- **TM-20 — No-Code Builder** (recommended for all staff who need to build or modify dashboards and pipelines)

After TM-20, all personnel proceed to TM-30. TM-30 is required before any TM-40 track:
- **WFF tracks (TM-40A–F)**: role-specific data application training by Warfighting Function (prereq: TM-30 required)
- **Specialist tracks (TM-40G–O)**: technical specialist tracks (prereq: TM-30 required)
