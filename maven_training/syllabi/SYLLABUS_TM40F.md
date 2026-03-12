# COURSE SYLLABUS
## TM-40F — MISSION COMMAND WARFIGHTING FUNCTION
### Maven Smart System (MSS) — USAREUR-AF

| | |
|---|---|
| **Level** | TM-40F (Mission Command WFF Track) |
| **Duration** | 3 days (24 hours) |
| **Prerequisites** | TM-10, TM-20 (Go evaluations on file); CONCEPTS_GUIDE_TM40F_MISSION_COMMAND (required reading before Day 1). No coding, pipeline development, or transform experience required or assumed. |
| **Audience** | G3/S3 staff, battle captains, FSOs, XOs, CDRs, and all personnel who configure, maintain, or brief from MSS Commander Products in a Mission Command role |
| **Format** | Instructor-led seminar + demonstration + tabletop exercise + practical evaluation |
| **Location** | MSS Training Environment (standard user access sufficient) |

---

## What This Course Does for You

Mission Command staff use MSS to maintain the COP, configure CCIR alerts, build battle rhythm products, and support commander decisions with current, integrated operational data. This course teaches you to do that work correctly — understanding not just how to use the platform buttons, but when and why each product type should be used in the context of the operations process (ADP 5-0).

TM-40F does not teach general staff skills or MDMP. It teaches you to integrate MSS capabilities into the staff work you already know — accelerating battle rhythm execution and improving the fidelity of commander products.

Three days allows one day for COP and CCIR configuration, one day for battle rhythm and reporting products, and one day for a full tabletop evaluation in a realistic operational scenario.

---

## Learning Objectives

By the end of training, you will be able to:

1. Configure and maintain a Common Operating Picture (COP) layer in MSS appropriate to your echelon and function, including data freshness verification and source attribution
2. Build and configure CCIR alerts with correct thresholds, data sources, and notification routing for a given commander's guidance
3. Construct and maintain a battle rhythm dashboard that supports daily/weekly meeting cycle products (BUA, SYNC, ADVON, planning cycle gate reviews)
4. Build a formatted commander assessment product integrating readiness, operational, and intelligence data with explicit data-as-of timestamps
5. Configure CP displacement data continuity procedures in MSS: handoff, snapshot, and restoration
6. Identify and respond to data staleness, source pipeline failures, and CCIR false-positive triggers before they reach the commander
7. Apply MSS OPSEC procedures: export handling, classification label placement, and distribution controls for all commander products
8. Distinguish between reported status (what MSS shows) and assessed status (what the commander judges), and communicate that distinction explicitly in briefings

---

## Before You Attend: Pre-Course Checklist

Complete **5+ duty days before Day 1:**
- [ ] Read CONCEPTS_GUIDE_TM40F_MISSION_COMMAND in full — this is not optional. Day 1 builds directly on it.
- [ ] Confirm your MSS training account is active and you can log in to the training environment
- [ ] Bring one current (or recent) Battle Rhythm from your unit — a real or notional weekly event list you can use during the tabletop on Day 3

---

## Daily Schedule

**Day 1 — COP Configuration and CCIR Management**

| Time | Block | Method | Content |
|---|---|---|---|
| 0800–0900 | 1  | Brief    | Doctrinal context: ADP 6-0, FM 6-0, and how MSS supports the operations process; role of the COP in command and control |
| 0900–1100 | 2  | Demo/Lab | COP configuration: adding layers, setting data sources, configuring display standards by echelon; data freshness indicators |
| 1100–1115 | —  | Break    | |
| 1115–1200 | 3  | Lab      | Verifying data currency: reading timestamps, tracing data source pipelines, identifying stale feeds and escalation path |
| 1200–1300 | —  | Lunch    | |
| 1300–1500 | 4  | Lab      | CCIR configuration: translating commander's published CCIR into MSS alert thresholds; routing notifications to correct staff; setting review cadence |
| 1500–1515 | —  | Break    | |
| 1515–1700 | 5  | Exercise | CCIR scenario: given a set of commander priorities and a sample dataset, configure 3 CCIRs and verify they trigger correctly |

**Evening reading:** TM-40F, Chapter 6 (CCIR and Decision Support Management) — pay particular attention to the false-trigger mitigation procedures.

---

**Day 2 — Battle Rhythm Products and Commander Assessments**

| Time | Block | Method | Content |
|---|---|---|---|
| 0800–0830 | —  | Review   | Day 1 questions; CCIR configuration review — common threshold errors |
| 0830–1030 | 6  | Demo/Lab | Battle rhythm dashboard build: constructing a weekly cycle tracker, linking meeting products to data feeds, versioning briefing products |
| 1030–1045 | —  | Break    | |
| 1045–1200 | 7  | Lab      | BUA product build: readiness summary, CCIR status, operational outlook — formatting for O-5/CG audience; data-as-of timestamp placement |
| 1200–1300 | —  | Lunch    | |
| 1300–1500 | 8  | Demo/Lab | Assessment and reporting: building situation reports, assessment dashboards, and battle tracking products; distinguishing reported vs. assessed status |
| 1500–1515 | —  | Break    | |
| 1515–1700 | 9  | Exercise | Commander product drill: build a BUA read-ahead from a provided dataset; evaluator reviews for timestamp, CCIR status, and OPSEC compliance |

**Evening reading:** TM-40F, Chapter 4 (Battle Rhythm Management) and Chapter 8 (Assessment and Reporting).

---

**Day 3 — CP Operations, Degraded Procedures, and Practical Exercise**

| Time | Block | Method | Content |
|---|---|---|---|
| 0800–0900 | 10 | Brief    | CP displacement continuity: MSS handoff procedures, snapshot and restoration, data gap identification; coordinating with S6 before displacement |
| 0900–1030 | 11 | Demo/Lab | Degraded operations: running Mission Command without full MSS connectivity; manual data backup; what to brief when MSS data is unavailable |
| 1030–1045 | —  | Break    | |
| 1045–1100 | 12 | Brief    | Practical exercise scenario brief; product standards checklist review; tabletop ground rules |
| 1100–1200 | —  | Prep     | Practical exercise setup and planning time |
| 1200–1300 | —  | Lunch    | |
| 1300–1700 | 13 | **Eval** | **Practical exercise:** full tabletop — configure COP, set CCIRs, build battle rhythm dashboard, produce BUA product, respond to a data staleness inject, brief findings to evaluator |

---

## Required Reading Summary

| When | Reading |
|---|---|
| Before Day 1 | CONCEPTS_GUIDE_TM40F_MISSION_COMMAND (complete) |
| Day 1 evening | TM-40F, Ch 6 (CCIR and Decision Support Management) |
| Day 2 evening | TM-40F, Ch 4 (Battle Rhythm Management) |
| Day 2 evening | TM-40F, Ch 8 (Assessment and Reporting) |
| Day 3 (review) | TM-40F, Ch 10 (Degraded Operations) — skim before Day 3 brief |

---

## Practical Exercise

**Scenario:** You are the battle captain at a BCT headquarters during a force projection exercise. The commander requires a fully configured MSS COP with CCIRs active, a battle rhythm dashboard, and a BUA read-ahead product — all before a theater-level VTC in 4 hours. Mid-exercise, the S6 reports a data pipeline feeding readiness status has gone stale.

**Tasks:**
1. Configure the COP with correct layers and verify data currency for all displayed feeds
2. Build and validate 3 CCIRs from the provided commander's guidance card
3. Construct the weekly battle rhythm dashboard with the provided event list
4. Build the BUA read-ahead product with readiness summary, CCIR status, and operational outlook
5. Respond to the data staleness inject: identify the affected feed, characterize the gap, and brief the evaluator on what you will/will not brief to the commander
6. Apply OPSEC procedures to the final BUA product before simulated distribution

**Go standard:** Pass 5 of 6 tasks. No-Go on Task 2 (CCIR configuration) or Task 5 (data staleness response) = automatic No-Go regardless of total score.

---

## What "Go" Looks Like

CCIRs that are configured with incorrect thresholds — even if syntactically correct — do not pass. The evaluator has a commander guidance card against which CCIR thresholds are checked.

The data staleness inject is designed to require a judgment call. The correct answer is not a specific platform action — it is the ability to characterize what is known, what is unknown, and what the commander needs to know before the briefing. Participants who try to "fix" the pipeline rather than characterize the gap and escalate will miss the intent.

The BUA product must show data-as-of timestamps on every data element. A product without timestamps does not pass that element.

---

## Tips From Previous Graduates

- The CCIR exercise on Day 1 is harder than it sounds. "High-casualty threshold" is not a complete CCIR — it must be tied to a specific data feed, a specific value, and a specific notification path. Bring your unit's current CCIR list and think about how you would configure it before Day 1.
- The data staleness inject on Day 3 surprises most participants. The answer is not to click faster — it is to immediately characterize the gap and communicate it up. Every commander product that relies on the stale feed must be marked with a data currency caveat.
- Battle rhythm dashboards that look good but are disconnected from live data feeds will fail the evaluation. The evaluator will change the underlying data and verify the dashboard updates.

---

*USAREUR-AF Operational Data Team — UNCLASSIFIED*
*Syllabus TM-40F | Version 1.0 | March 2026*
