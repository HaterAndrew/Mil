# COURSE SYLLABUS — TM-40D: SUSTAINMENT WARFIGHTING FUNCTION
## Maven Smart System (MSS) — USAREUR-AF

| Field | Detail |
|---|---|
| **Level** | TM-40D — Sustainment WFF Track |
| **Duration** | 3 days (24 hours) |
| **Prerequisites** | TM-10, TM-20, TM-30 (Go evaluations on file); CONCEPTS_GUIDE_TM40D_SUSTAINMENT (required reading before Day 1) |
| **Audience** | G4/S4 staff, FSB/BSB logistics officers, supply chain managers, property book officers, and transportation officers at BCT echelon and below |
| **Format** | Instructor-led seminar + demonstration + tabletop exercise + practical evaluation |
| **Location** | MSS Training Environment (standard user access sufficient) |

---

**BLUF:** TM-40D teaches G4/S4 staff to integrate MSS into sustainment workflows — maintaining logistics visibility, integrating LOGSTAT data, building supply chain analytics, and tracking readiness status. Course applies MSS capabilities to processes in ADP 4-0, FM 4-0, and ATP 4-0.1. No coding or pipeline experience required.

---

## Learning Objectives

| # | Objective |
|---|---|
| 1 | Configure logistics data layers on the COP — readiness status overlays, supply class distribution, transportation network displays — with data-as-of timestamps |
| 2 | Build readiness dashboards integrating LOGSTAT data with explicit data currency indicators distinguishing current from delayed reporting |
| 3 | Configure sustainment-relevant CCIR alerts — readiness-below-threshold triggers and critical supply shortage notifications |
| 4 | Build a supply chain status product for the sustainment synchronization brief: unit readiness summary, supply class status by supported element, distribution status |
| 5 | Verify LOGSTAT pipeline currency; identify reporting unit gaps, delayed submissions, and data source failures |
| 6 | Identify and respond to LOGSTAT data staleness affecting readiness or supply displays before a sustainment synchronization brief |
| 7 | Apply OPSEC procedures to sustainment products: classification markings, handling instructions for readiness data, distribution controls |
| 8 | Distinguish reported readiness (what LOGSTAT submissions show) from estimated readiness (S4 calculation when reporting is delayed or incomplete) and communicate that distinction explicitly |

---

## Pre-Course Checklist

Complete **5+ duty days before Day 1:**

- [ ] Read CONCEPTS_GUIDE_TM40D_SUSTAINMENT in full — Day 1 builds directly on it
- [ ] Confirm MSS training account is active
- [ ] Bring your unit's current LOGSTAT format or a recent sustainment sync slide deck — used as a reference during the Day 3 tabletop
- [ ] Review your unit's readiness reporting thresholds (C1–C4 equivalents or local standards) — Day 1 asks you to configure them as CCIR thresholds in MSS

---

## Daily Schedule

### Day 1 — Logistics Data Layers, LOGSTAT Pipeline, and Readiness Display

| Time | Block | Method | Content |
|---|---|---|---|
| 0800–0900 | 1 | Brief | Doctrinal context: ADP 4-0, FM 4-0; how MSS supports sustainment visibility; role of logistics data integration in the operations center |
| 0900–1100 | 2 | Demo/Lab | Logistics COP configuration: readiness overlays, supply status layers, transportation network displays; data sources and display standards by echelon |
| 1100–1115 | — | Break | |
| 1115–1200 | 3 | Lab | LOGSTAT pipeline verification: reading submission timestamps, identifying reporting gaps, tracing data sources, distinguishing current from stale LOGSTAT data |
| 1200–1300 | — | Lunch | |
| 1300–1500 | 4 | Lab | CCIR configuration for sustainment: translating readiness thresholds and supply CCIR guidance into MSS alert configuration; setting notification routing for S4 and XO |
| 1500–1515 | — | Break | |
| 1515–1700 | 5 | Exercise | CCIR drill: given sustainment CCIRs and a sample LOGSTAT dataset, configure 3 sustainment CCIRs and verify they trigger correctly |

**Evening reading:** TM-40D, Chapter 2 (Supply Chain Management in MSS) — data currency indicators and what constitutes a valid vs. stale LOGSTAT submission.

---

### Day 2 — Supply Analytics, Distribution Data, and Sustainment CCIR

| Time | Block | Method | Content |
|---|---|---|---|
| 0800–0830 | — | Review | Day 1 questions; CCIR configuration review — common threshold configuration errors for readiness data |
| 0830–1030 | 6 | Demo/Lab | Supply chain status product build: supply class status display, linking to LOGSTAT feeds, coding shortfall and surplus status by unit |
| 1030–1045 | — | Break | |
| 1045–1200 | 7 | Lab | Distribution data layers: transportation route overlays, convoy status feeds, distribution node displays; tracking movement of supply classes |
| 1200–1300 | — | Lunch | |
| 1300–1500 | 8 | Demo/Lab | Readiness dashboard build: integrated readiness display combining LOGSTAT data with data-as-of timestamps; format for sustainment sync and BUA |
| 1500–1515 | — | Break | |
| 1515–1700 | 9 | Exercise | Sustainment sync product drill: build readiness summary and supply chain status product from a provided LOGSTAT dataset; evaluator reviews for timestamp placement, reported vs. estimated readiness distinction, and OPSEC marking |

**Evening reading:** TM-40D, Chapter 4 (Transportation and Distribution Operations) and Chapter 9 (Echelon-Specific Sustainment Operations).

---

### Day 3 — Reporting Gaps, Degraded Procedures, and Practical Exercise

| Time | Block | Method | Content |
|---|---|---|---|
| 0800–0900 | 10 | Brief | LOGSTAT reporting gaps: procedures when a subordinate unit's feed stops updating; estimating readiness with stale data; risk communication to XO and CDR |
| 0900–1030 | 11 | Demo/Lab | Degraded LOGSTAT scenarios: running a sustainment sync with partial reporting; manual readiness estimate procedures; OPSEC for incomplete products |
| 1030–1045 | — | Break | |
| 1045–1100 | 12 | Brief | Practical exercise scenario brief; product standards checklist review; sustainment sync tabletop ground rules |
| 1100–1200 | — | Prep | Practical exercise setup and planning time |
| 1200–1300 | — | Lunch | |
| 1300–1700 | 13 | **Eval** | **Practical exercise:** configure logistics COP, build readiness dashboard and supply chain status product, configure sustainment CCIRs, respond to a LOGSTAT data staleness inject, brief findings to evaluator in role as XO |

---

## Required Reading

| When | Reading |
|---|---|
| Before Day 1 | CONCEPTS_GUIDE_TM40D_SUSTAINMENT (complete) |
| Day 1 evening | TM-40D, Ch 2 (Supply Chain Management in MSS) |
| Day 2 evening | TM-40D, Ch 4 (Transportation and Distribution Operations) |
| Day 2 evening | TM-40D, Ch 9 (Echelon-Specific Sustainment Operations) |
| Day 3 (review) | TM-40D, Ch 10 (Degraded Operations) — skim before Day 3 brief |

---

## Practical Exercise

**Scenario:** You are the S4 section at a BCT headquarters during a logistics exercise. The XO requires a configured readiness dashboard, supply chain status product, and sustainment CCIRs active before a sustainment synchronization brief in four hours. Mid-exercise, the LOGSTAT reporting feed from one forward support company stops updating.

| # | Task |
|---|---|
| 1 | Configure logistics COP layers — readiness overlay, supply class status, transportation network — and verify data currency for all LOGSTAT feeds |
| 2 | Build a readiness dashboard integrating LOGSTAT data from all subordinate elements, with data-as-of timestamps on every section |
| 3 | Configure 3 sustainment CCIRs from the provided commander's guidance card, including a readiness-below-threshold trigger and a critical supply shortage alert |
| 4 | Build a supply chain status product formatted for the sustainment synchronization brief, covering all supply classes with current status by supported element |
| 5 | Respond to the LOGSTAT feed staleness inject: identify the affected unit, characterize the reporting gap, update products with data caveats, and brief the evaluator on impact and resolution action |
| 6 | Apply OPSEC procedures to the final readiness product before simulated distribution |

**Go standard:** Pass 5 of 6 tasks. No-Go on Task 2 (readiness dashboard) or Task 5 (data staleness response) = automatic No-Go regardless of total score.

---

## Go Criteria

| Task | Hard Standard |
|---|---|
| Readiness dashboard | Data-as-of timestamps required at the **element level** — a page-level timestamp only fails Task 2 |
| Reported vs. estimated readiness | Product must explicitly identify which unit's readiness is estimated vs. reported when LOGSTAT is delayed — presenting estimated data as current reported data fails |
| Data staleness inject | Characterize and escalate; do not attempt to restore the LOGSTAT feed. Trainees who attempt feed restoration miss the sustainment sync window |

### Function-Specific Go Criteria — Sustainment

| Criterion | Standard |
|---|---|
| LOGSTAT data currency | Readiness dashboard must display a "LOGSTAT as of:" timestamp sourced from the pipeline ingestion timestamp — a dashboard without this timestamp fails the LOGSTAT currency element |
| Reported vs. estimated readiness | Supply chain product must explicitly label estimated figures (those derived from calculations, not direct reports) — unlabeled estimates treated as reported data is a No-Go for data integrity |
| Sustainment CCIR thresholds | At least one CCIR must be tied to a supply level threshold (days of supply, C-rating, or class of supply percentage) — generic "pipeline failure" alerts do not satisfy the sustainment CCIR requirement |

---

## Key Tips

| Risk | Guidance |
|---|---|
| CCIR data source | Readiness thresholds connected to the wrong data field (personnel vs. equipment readiness) will not fire correctly — verify the specific CCIR data source carefully |
| Supply chain product | Know your supply class designations and which LOGSTAT reporting fields correspond to each before Day 2 |
| Timestamps on briefing products | Every readiness number in a briefing product must have a data-as-of timestamp. Build this habit before Day 1: every number → "As of when?" |
| CCIR troubleshooting | Sustainment CCIRs set to alert on C-rating changes frequently false-trigger when the LOGSTAT feed refreshes and rounds numbers. Use a rolling average or a two-refresh confirmation window rather than a single-value threshold. If the CCIR is triggering every refresh cycle, the threshold is too sensitive to feed noise |

---

## Associated Exercise and Exams

| Item | Reference |
|---|---|
| **Practical Exercise** | EX_40D (EXERCISE.md + ENVIRONMENT_SETUP.md) — `exercises/EX_40D_sustainment/` |
| **Pre-course exam** | EXAM_TM40D_PRE — `exercises/exams/EXAM_TM40D_PRE.md` |
| **Post-course exam** | EXAM_TM40D_POST — `exercises/exams/EXAM_TM40D_POST.md` |

---

## Related WFF Tracks

TM-40D is one of six WFF tracks. All require TM-10, TM-20, and TM-30 as prerequisites.

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
*Syllabus TM-40D | Version 1.0 | March 2026*
