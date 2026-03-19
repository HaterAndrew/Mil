# COURSE SYLLABUS — TM-40F: MISSION COMMAND WARFIGHTING FUNCTION
## Maven Smart System (MSS) — USAREUR-AF

| Field | Detail |
|---|---|
| **Level** | TM-40F — Mission Command WFF Track |
| **Duration** | 3 days (24 hours) |
| **Prerequisites** | TM-10, TM-20, TM-30 (Go evaluations on file); CONCEPTS_GUIDE_TM40F_MISSION_COMMAND (required reading before Day 1) |
| **Audience** | G3/S3 staff, battle captains, FSOs, XOs, CDRs, and all personnel who configure, maintain, or brief from MSS Commander Products in a Mission Command role |
| **Format** | Instructor-led seminar + demonstration + tabletop exercise + practical evaluation |
| **Location** | MSS Training Environment (standard user access sufficient) |

---

**BLUF:** TM-40F teaches Mission Command staff to integrate MSS into the operations process — maintaining the COP, configuring CCIR alerts, building battle rhythm products, and supporting commander decisions with current integrated operational data. Course applies MSS capabilities per ADP 6-0 (Jul 2019) and FM 6-0 (May 2022). No coding or pipeline experience required.

---

## Learning Objectives

| # | Objective |
|---|---|
| 1 | Configure and maintain a COP layer in MSS appropriate to echelon and function, including data freshness verification and source attribution |
| 2 | Build and configure CCIR alerts with correct thresholds, data sources, and notification routing for a given commander's guidance |
| 3 | Construct and maintain a battle rhythm dashboard supporting daily/weekly meeting cycle products (BUA, SYNC, ADVON, planning cycle gate reviews) |
| 4 | Build a formatted commander assessment product integrating readiness, operational, and intelligence data with explicit data-as-of timestamps |
| 5 | Configure CP displacement data continuity procedures in MSS: handoff, snapshot, and restoration |
| 6 | Identify and respond to data staleness, source pipeline failures, and CCIR false-positive triggers before they reach the commander |
| 7 | Apply MSS OPSEC procedures: export handling, classification label placement, and distribution controls for all commander products |
| 8 | Distinguish reported status (what MSS shows) from assessed status (what the commander judges) and communicate that distinction explicitly |

---

## Pre-Course Checklist

Complete **5+ duty days before Day 1:**

- [ ] Read CONCEPTS_GUIDE_TM40F_MISSION_COMMAND in full — this is not optional; Day 1 builds directly on it
- [ ] Confirm MSS training account is active
- [ ] Bring one current (or recent) Battle Rhythm from your unit — a real or notional weekly event list used during the Day 3 tabletop

---

## Daily Schedule

### Day 1 — COP Configuration and CCIR Management

| Time | Block | Method | Content |
|---|---|---|---|
| 0800–0900 | 1 | Brief | Doctrinal context: ADP 6-0 (Jul 2019), FM 6-0 (May 2022); how MSS supports the operations process; role of the COP in command and control |
| 0900–1100 | 2 | Demo/Lab | COP configuration: adding layers, setting data sources, configuring display standards by echelon; data freshness indicators |
| 1100–1115 | — | Break | |
| 1115–1200 | 3 | Lab | Verifying data currency: reading timestamps, tracing data source pipelines, identifying stale feeds and escalation path |
| 1200–1300 | — | Lunch | |
| 1300–1500 | 4 | Lab | CCIR configuration: translating commander's published CCIR into MSS alert thresholds; routing notifications to correct staff; setting review cadence |
| 1500–1515 | — | Break | |
| 1515–1700 | 5 | Exercise | CCIR scenario: given commander priorities and a sample dataset, configure 3 CCIRs and verify they trigger correctly |

**Evening reading:** TM-40F, Chapter 6 (CCIR and Decision Support Management) — false-trigger mitigation procedures.

---

### Day 2 — Battle Rhythm Products and Commander Assessments

| Time | Block | Method | Content |
|---|---|---|---|
| 0800–0830 | — | Review | Day 1 questions; CCIR configuration review — common threshold errors |
| 0830–1030 | 6 | Demo/Lab | Battle rhythm dashboard build: weekly cycle tracker, linking meeting products to data feeds, versioning briefing products |
| 1030–1045 | — | Break | |
| 1045–1200 | 7 | Lab | BUA product build: readiness summary, CCIR status, operational outlook — formatting for O-5/CG audience; data-as-of timestamp placement |
| 1200–1300 | — | Lunch | |
| 1300–1500 | 8 | Demo/Lab | Assessment and reporting: building SITREPs, assessment dashboards, and battle tracking products; distinguishing reported vs. assessed status |
| 1500–1515 | — | Break | |
| 1515–1700 | 9 | Exercise | Commander product drill: build a BUA read-ahead from a provided dataset; evaluator reviews for timestamp, CCIR status, and OPSEC compliance |

**Evening reading:** TM-40F, Chapter 4 (Battle Rhythm Management) and Chapter 8 (Assessment and Reporting).

---

### Day 3 — CP Operations, Degraded Procedures, and Practical Exercise

| Time | Block | Method | Content |
|---|---|---|---|
| 0800–0900 | 10 | Brief | CP displacement continuity: MSS handoff procedures, snapshot and restoration, data gap identification; coordinating with S6 before displacement |
| 0900–1030 | 11 | Demo/Lab | Degraded operations: running Mission Command without full MSS connectivity; manual data backup; what to brief when MSS data is unavailable |
| 1030–1045 | — | Break | |
| 1045–1100 | 12 | Brief | Practical exercise scenario brief; product standards checklist review; tabletop ground rules |
| 1100–1200 | — | Prep | Practical exercise setup and planning time |
| 1200–1300 | — | Lunch | |
| 1300–1700 | 13 | **Eval** | **Practical exercise:** configure COP, set CCIRs, build battle rhythm dashboard, produce BUA product, respond to a data staleness inject, brief findings to evaluator |

---

## Required Reading

| When | Reading |
|---|---|
| Before Day 1 | CONCEPTS_GUIDE_TM40F_MISSION_COMMAND (complete) |
| Day 1 evening | TM-40F, Ch 6 (CCIR and Decision Support Management) |
| Day 2 evening | TM-40F, Ch 4 (Battle Rhythm Management) |
| Day 2 evening | TM-40F, Ch 8 (Assessment and Reporting) |
| Day 3 (review) | TM-40F, Ch 10 (Degraded Operations) — skim before Day 3 brief |

---

## Practical Exercise

**Scenario:** You are the battle captain at a BCT headquarters during a force projection exercise. The commander requires a fully configured MSS COP with CCIRs active, a battle rhythm dashboard, and a BUA read-ahead product before a theater-level VTC in 4 hours. Mid-exercise, the S6 reports a data pipeline feeding readiness status has gone stale.

| # | Task |
|---|---|
| 1 | Configure the COP with correct layers and verify data currency for all displayed feeds; verify MSS snapshot is configured per CP displacement procedures and brief the evaluator on the handoff sequence (source, snapshot, restore — 3 steps, no notes) |
| 2 | Build and validate 3 CCIRs from the provided commander's guidance card |
| 3 | Construct the weekly battle rhythm dashboard with the provided event list |
| 4 | Build the BUA read-ahead product with readiness summary, CCIR status, and operational outlook |
| 5 | Respond to the data staleness inject: identify the affected feed, characterize the gap, and brief the evaluator on what you will/will not brief to the commander |
| 6 | Apply OPSEC procedures to the final BUA product before simulated distribution |

**Go standard:** Pass 5 of 6 tasks. No-Go on Task 2 (CCIR configuration) or Task 5 (data staleness response) = automatic No-Go regardless of total score.

---

## Go Criteria

| Task | Hard Standard |
|---|---|
| CP displacement handoff | Trainee must state the 3-step handoff sequence (source, snapshot, restore) without notes — a checklist read-back is acceptable; inability to name the steps is No-Go for that element of Task 1 |
| CCIR thresholds | Syntactically correct but wrong thresholds do not pass — evaluator checks CCIRs against the commander guidance card |
| Data staleness inject | Correct answer is to characterize what is known/unknown and communicate to commander before briefing — trainees who "fix" the pipeline rather than characterize and escalate will miss the intent |
| BUA product | Data-as-of timestamps required on every data element — a product without timestamps fails that element |
| Battle rhythm dashboard | Dashboard must reflect the trainee's provided event list — not a template. Evaluator will check 3 randomly selected events by name against the provided list. Any missing or wrong event name is No-Go for that element |

---

## Key Tips

| Risk | Guidance |
|---|---|
| CCIR configuration | "High-casualty threshold" is not a complete CCIR — must be tied to a specific data feed, specific value, and specific notification path. Bring your unit's CCIR list and work through configuration before Day 1 |
| Data staleness inject | Do not click faster — immediately characterize the gap and communicate it up. Every commander product relying on the stale feed must be caveated |
| Battle rhythm dashboards | The evaluator will change underlying data and verify the dashboard updates — disconnected from live data fails the evaluation |
| CCIR troubleshooting | Mission command CCIRs that route to "all staff" as a notification path are not correctly configured — each CCIR must route to the specific functional staff section responsible for that decision (e.g., a readiness CCIR routes to S4, not all staff). Evaluator will check routing against the commander guidance card |

---

## Associated Exercise and Exams

| Item | Reference |
|---|---|
| **Practical Exercise** | EX_40F (EXERCISE.md + ENVIRONMENT_SETUP.md) — `exercises/EX_40F_mission_command/` |
| **Pre-course exam** | EXAM_TM40F_PRE — `exercises/exams/EXAM_TM40F_PRE.md` |
| **Post-course exam** | EXAM_TM40F_POST — `exercises/exams/EXAM_TM40F_POST.md` |

---

## Related WFF Tracks

TM-40F is one of six WFF tracks. All require TM-10, TM-20, and TM-30 as prerequisites.

| Track | WFF | Audience |
|---|---|---|
| TM-40A | Intelligence | G2/S2 staff, targeting officers, all-source analysts |
| TM-40B | Fires | FSOs, FSEs, targeting officers, fires NCOs |
| TM-40C | Movement & Maneuver | G3/S3 staff, operations officers, maneuver planners |
| TM-40D | Sustainment | G4/S4 staff, logistics officers, supply chain managers |
| TM-40E | Protection | FP officers, CBRN officers, provost marshal staff |
| TM-40F | Mission Command | Battle captains, XOs, CDRs, MC-function staff |

Personnel completing multiple WFF tracks do not repeat TM-10, TM-20, or TM-30. Enrollment is independent for each track.

---

*USAREUR-AF Operational Data Team*
*Syllabus TM-40F | Version 1.0 | March 2026*
