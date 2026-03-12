# EX-10 — MSS Operator Basics
## Practical Exercise — TM-10 Proficiency

**Version 1.0 | March 2026**
**Prerequisite:** TM-10, Maven Smart System Operator Technical Manual
**Duration:** 45–60 minutes
**Environment:** MSS training instance or sandbox (see ENVIRONMENT_SETUP.md)

---

## SCENARIO

You are a staff officer at a brigade combat team HQ. Your S2 has asked you to pull the current equipment readiness status for three subordinate battalions and produce a summary for the daily SITREP. You have MSS access and need to navigate, filter, and export data from an existing readiness dashboard.

**Unclassified training data simulates LOGSTAT/readiness report formats.**

---

## TASK LIST

### Task 1 — Log In and Orient (10 min)
- [ ] Log in to MSS using your CAC credentials
- [ ] Locate the training dashboard: "BCT Readiness — EX-10 Training"
- [ ] Identify the data owner and last-updated timestamp
- **Go:** Can locate dashboard and read metadata without assistance
- **No-Go:** Cannot find the dashboard or misidentifies the data owner

### Task 2 — Apply Filters (15 min)
- [ ] Filter the readiness view to show only **1st Battalion** data
- [ ] Change the date range to show the last 7 days
- [ ] Reset filters to show all units
- **Go:** Filters apply correctly; data refreshes; can reset without help
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
- **Go:** Export completes; timestamp is visible in output
- **No-Go:** Export fails or timestamp is absent

### Task 5 — Navigate and Bookmark (5 min)
- [ ] Find one additional dashboard relevant to your role
- [ ] Bookmark it to your MSS home
- **Go:** Bookmark appears on home screen after navigation
- **No-Go:** Cannot locate secondary dashboard or bookmark fails

---

## EVALUATOR NOTES

**Scoring:** 5 tasks. Go on 4 of 5 = overall Go. No-Go on Task 2 or Task 4 = automatic No-Go (core operator competency).

**Pre-exercise checklist (evaluator actions before exercise begins):**
- Confirm all training accounts can access the "BCT Readiness — EX-10 Training" dashboard
- Verify the dashboard shows data for at least 3 units with clearly different readiness values
- Confirm the data steward contact field is populated in the dashboard metadata
- Note the correct answer for Task 3 (lowest-readiness unit and driving equipment category) — see ENVIRONMENT_SETUP.md answer key

**Common failure modes:**

| Task | Common Failure | Evaluator Guidance |
|------|---------------|--------------------|
| Task 1 | Cannot find the dashboard | Note navigation path taken; searching by name is acceptable; browsing wrong project is No-Go |
| Task 2 | Filters applied but not reset | Page reload to reset = Go with coaching note; clicking Reset correctly = Go |
| Task 3 | Identifies wrong low-readiness unit | Check against answer key; any incorrect unit identification = No-Go |
| Task 4 | Export missing "Last updated" timestamp | Most common cause: CSV export instead of PDF; note format used |
| Task 5 | Bookmark does not appear on home | Sandbox browser issue — if correct action is demonstrated, retest after cache clear before marking No-Go |

**Timing notes:**
- Task 3 runs 5–15 min depending on analytical background; do not prompt within the first 10 min
- If Task 2 exceeds 15 min, ask participant to narrate their approach (do not guide)
- Total exercise rarely exceeds 50 min for participants current on TM-10

---

## ENVIRONMENT SETUP

See [ENVIRONMENT_SETUP.md](ENVIRONMENT_SETUP.md) for full setup instructions.
