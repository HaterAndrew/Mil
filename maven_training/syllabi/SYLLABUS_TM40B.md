# COURSE SYLLABUS — TM-40B: FIRES WARFIGHTING FUNCTION
## Maven Smart System (MSS) — USAREUR-AF

| Field | Detail |
|---|---|
| **Level** | TM-40B — Fires WFF Track |
| **Duration** | 3 days (24 hours) |
| **Prerequisites** | TM-10, TM-20 (Go evaluations on file); CONCEPTS_GUIDE_TM40B_FIRES (required reading before Day 1) |
| **Audience** | Fire support officers, FSEs, targeting officers, artillery and mortar officers and NCOs, fire support NCOs at BCT echelon and below |
| **Format** | Instructor-led seminar + demonstration + tabletop exercise + practical evaluation |
| **Location** | MSS Training Environment (standard user access sufficient) |

---

**BLUF:** TM-40B teaches fires staff to integrate MSS into fires and targeting workflows — configuring FSCMs on the COP, managing targeting data, building effects assessment dashboards, and supporting BDA workflows. Course applies MSS capabilities to processes in FM 3-09, ATP 3-09.42, and ATP 3-60. No coding or pipeline experience required.

---

## Learning Objectives

| # | Objective |
|---|---|
| 1 | Configure fires data layers on the COP — FSCMs, active target lists, BDA status overlays — with data freshness verification |
| 2 | Build a targeting data product distinguishing confirmed from suspected targets, with attribution to reporting source and data-as-of timestamps |
| 3 | Configure fires-relevant CCIR alerts — target-engaged status, effects-confirmed status, and FSCM violation triggers |
| 4 | Display and track FSCMs on the MSS COP with correct symbology and authority reference |
| 5 | Build an effects assessment dashboard integrating BDA data from multiple fires elements with explicit data currency indicators |
| 6 | Identify and respond to targeting data staleness or reporting source gaps before a targeting working group |
| 7 | Apply OPSEC procedures to fires products: classification markings, distribution restrictions, export handling for targeting data |
| 8 | Distinguish reported effects (what fires elements transmitted) from assessed effects (what the targeting officer judges) and communicate that distinction explicitly |

---

## Pre-Course Checklist

Complete **5+ duty days before Day 1:**

- [ ] Read CONCEPTS_GUIDE_TM40B_FIRES in full — Day 1 builds directly on it
- [ ] Confirm MSS training account is active
- [ ] Bring one recent or notional target list from your unit, or a published targeting product from a recent exercise — used as a reference during the Day 3 tabletop
- [ ] Review your unit's current FSCMs and FSCM display standards — Day 1 asks you to replicate them in MSS

---

## Daily Schedule

### Day 1 — Fires Data Layers, FSCM Configuration, and COP Setup

| Time | Block | Method | Content |
|---|---|---|---|
| 0800–0900 | 1 | Brief | Doctrinal context: FM 3-09, ATP 3-60; how MSS supports fires and targeting; role of the fires COP in targeting board preparation |
| 0900–1100 | 2 | Demo/Lab | Fires COP configuration: FSCM overlays, target list layers, data sources; display standards by echelon |
| 1100–1115 | — | Break | |
| 1115–1200 | 3 | Lab | Data currency verification: reading FSCM update timestamps, tracing BDA reporting sources, identifying stale feeds |
| 1200–1300 | — | Lunch | |
| 1300–1500 | 4 | Lab | CCIR configuration for fires: translating fires-related CCIRs into MSS alert thresholds; target-engaged and effects-confirmed triggers |
| 1500–1515 | — | Break | |
| 1515–1700 | 5 | Exercise | CCIR drill: given commander priorities and a sample dataset, configure 3 fires CCIRs and verify they trigger correctly |

**Evening reading:** TM-40B, Chapter 5 (Targeting Data Management in MSS) — confirmed vs. suspected target distinction and attribution requirements.

---

### Day 2 — Targeting Data Workflows, BDA Products, and Effects Assessment

| Time | Block | Method | Content |
|---|---|---|---|
| 0800–0830 | — | Review | Day 1 questions; FSCM configuration review — common display errors |
| 0830–1030 | 6 | Demo/Lab | Targeting data product build: structuring the target list in MSS, coding confirmed vs. suspected status, linking attribution to source reports, setting data-as-of timestamps |
| 1030–1045 | — | Break | |
| 1045–1200 | 7 | Lab | BDA data integration: pulling BDA feeds from fires elements into a single effects assessment display; coding BDA status by target; managing multiple reporting sources |
| 1200–1300 | — | Lunch | |
| 1300–1500 | 8 | Demo/Lab | Effects assessment dashboard: building a BDA status product for the targeting board; distinguishing reported from assessed effects; data caveat formatting |
| 1500–1515 | — | Break | |
| 1515–1700 | 9 | Exercise | Targeting product drill: build a targeting data product and effects summary from a provided dataset; evaluator reviews for confirmed/suspected distinction, timestamps, and source attribution |

**Evening reading:** TM-40B, Chapter 7 (Effects Assessment and BDA Workflows) and Chapter 9 (OPSEC for Fires Products).

---

### Day 3 — Degraded Reporting, Data Staleness, and Practical Exercise

| Time | Block | Method | Content |
|---|---|---|---|
| 0800–0900 | 10 | Brief | Targeting data staleness: procedures when BDA or target reporting stops updating; manual backup; what to brief when MSS fires data is incomplete |
| 0900–1030 | 11 | Demo/Lab | Degraded BDA scenarios: running a targeting working group with partial or stale fires data; OPSEC for incomplete products; escalation to S3 and S6 |
| 1030–1045 | — | Break | |
| 1045–1100 | 12 | Brief | Practical exercise scenario brief; product standards checklist review; targeting board ground rules |
| 1100–1200 | — | Prep | Practical exercise setup and planning time |
| 1200–1300 | — | Lunch | |
| 1300–1700 | 13 | **Eval** | **Practical exercise:** configure fires COP and FSCMs, build targeting data product, set fires CCIRs, build effects assessment dashboard, respond to a BDA data staleness inject, brief findings to evaluator in role as S3/FSO |

---

## Required Reading

| When | Reading |
|---|---|
| Before Day 1 | CONCEPTS_GUIDE_TM40B_FIRES (complete) |
| Day 1 evening | TM-40B, Ch 5 (Targeting Data Management in MSS) |
| Day 2 evening | TM-40B, Ch 7 (Effects Assessment and BDA Workflows) |
| Day 2 evening | TM-40B, Ch 9 (OPSEC for Fires Products) |
| Day 3 (review) | TM-40B, Ch 11 (Degraded Fires Reporting) — skim before Day 3 brief |

---

## Practical Exercise

**Scenario:** You are the FSE at a BCT headquarters during a combined arms live-fire exercise. The commander requires FSCMs on the COP, a current targeting data product, and fires CCIRs active before a targeting working group in four hours. Mid-exercise, the BDA reporting feed from the supporting fires element stops updating.

| # | Task |
|---|---|
| 1 | Configure fires COP layers — FSCMs, target list, BDA status overlay — and verify data currency for all feeds |
| 2 | Build a targeting data product distinguishing confirmed from suspected targets, with source attribution and data-as-of timestamps |
| 3 | Configure 3 fires CCIRs from the provided commander's fires CCIR guidance card |
| 4 | Build an effects assessment dashboard showing BDA status by target across all active fires elements |
| 5 | Respond to the BDA data staleness inject: identify the affected feed, characterize the gap, and brief the evaluator on what will and will not be briefed to the targeting board |
| 6 | Apply OPSEC procedures to the final targeting product before simulated distribution |

**Go standard:** Pass 5 of 6 tasks. No-Go on Task 2 (targeting data product) or Task 5 (data staleness response) = automatic No-Go regardless of total score.

---

## Go Criteria

| Task | Hard Standard |
|---|---|
| Targeting data product | Confirmed/suspected status must use both visual coding AND source attribution — not just a column header. Grouped confirmed/suspected targets fail |
| Data staleness inject | Characterize which BDA elements are affected vs. current, then brief the targeting board on what they will/will not receive. Attempting to restore the feed instead of characterizing will miss the intent |
| Data-as-of timestamps | Must appear on the targeting product. A product without visible timestamps on the target list and BDA sections fails Task 2 |

---

## Key Tips

| Risk | Guidance |
|---|---|
| FSCM layers | FSCMs displayed but not linked to an authoritative data source fail the data currency check — know how to connect a layer to a source before Day 1 |
| Confirmed/suspected distinction | Every target must have a coded status AND source attribution entry. Bring your unit's target list format as a reference |
| BDA data staleness inject | The targeting board cannot wait for feed recovery — the FSE must tell the board exactly which targets have current BDA and which do not. Practice characterizing the gap out loud before you arrive |

---

*USAREUR-AF Operational Data Team — UNCLASSIFIED*
*Syllabus TM-40B | Version 1.0 | March 2026*
