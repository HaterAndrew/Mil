# COURSE SYLLABUS — TM-30: ADVANCED BUILDER
## Maven Smart System (MSS) — USAREUR-AF

| Field | Detail |
|---|---|
| **Level** | TM-30 (Advanced Builder — data-adjacent specialists) |
| **Duration** | 5 days (40 hours) |
| **Prerequisite** | TM-10 and TM-20 complete (both Go evaluations on file) |
| **Audience** | 17/25-series, S6/G6, G2/G9, operational data analysts, staff assigned to advanced data product design |
| **Format** | Instructor-led lab + design workshop + practical exercise |
| **Location** | MSS Training Environment |

---

**BLUF:** TM-30 moves you from building components to designing systems. After this course you can architect an Ontology model from a mission requirement, build multi-source pipelines with scheduled refresh, produce multi-page Workshop applications with conditional logic, conduct advanced analysis in Contour and Quiver, and own the full C2DAO governance cycle. TM-30 personnel are the data leads of their formation.

---

## Learning Objectives

| # | Objective |
|---|---|
| 1 | Build a multi-page Workshop application with conditional logic (show/hide, branching), variable passing between pages, and URL-based deep linking |
| 2 | Build a Pipeline Builder pipeline with multi-source joins, union transforms, group-by aggregations, and computed columns derived from multiple sources |
| 3 | Design an Ontology schema (Object Types, Link Types, Actions) from a mission requirement — documented and reviewed against the TM-30 design rubric |
| 4 | Configure a scheduled pipeline with email alerting on build failure |
| 5 | Conduct advanced Contour analysis: pivot tables, calculated columns, parameter controls, saved analysis views |
| 6 | Build a multi-object Quiver dashboard with linked views and cross-object filter propagation |
| 7 | Configure (not author) an AIP Logic workflow — connect inputs, outputs, trigger conditions, and interpret lineage graphs |
| 8 | Execute the full C2DAO promotion workflow from branch creation through data steward approval, including responding to steward feedback |

---

## Pre-Course Checklist

Complete **7+ duty days before Day 1:**

- [ ] Confirm both TM-10 and TM-20 Go evaluations are on file with your unit training coordinator
- [ ] Request **Editor access** in the MSS Training Environment from your unit MSS Administrator
- [ ] Request AIP Logic **configuration access** — may require C2DAO coordination; required for Day 4; confirm active before Day 1
- [ ] Read TM-30, Chapter 1 (Introduction) and complete the prerequisite self-check — 30 min
- [ ] Review TM-20, Chapter 5 (Workshop) — if you cannot independently build a Workshop application with a table, filter, and Action button, resolve that gap before arriving

---

## Daily Schedule

### Day 1 — Advanced Workshop

| Time | Block | Method | Content |
|---|---|---|---|
| 0800–0830 | — | Brief | TM-30 overview; what you will build by Day 5; design-first methodology |
| 0830–1030 | 1 | Lab | Multi-page Workshop: page navigation, parameter configuration, URL deep links |
| 1030–1045 | — | Break | |
| 1045–1200 | 2 | Lab | Conditional logic: show/hide panels, conditional formatting on tables, dynamic widget visibility rules |
| 1200–1300 | — | Lunch | |
| 1300–1500 | 3 | Lab | Variable passing: passing object selections between pages; filtered detail views driven by page-1 selection |
| 1500–1515 | — | Break | |
| 1515–1700 | 4 | Lab | Design exercise: build a 3-page operations dashboard (portfolio → unit detail → historical trend); instructor critique |

**Evening reading:** TM-30, Chapter 3 (Advanced Pipeline Builder — join and aggregation sections).

---

### Day 2 — Advanced Pipeline Builder

| Time | Block | Method | Content |
|---|---|---|---|
| 0800–0830 | — | Review | Day 1 questions; Workshop design critique debrief |
| 0830–1030 | 5 | Lab | Multi-source joins: inner/left/outer, handling fan-out after join, post-join deduplication patterns |
| 1030–1045 | — | Break | |
| 1045–1200 | 6 | Lab | Union transforms: combining datasets with compatible schemas, handling schema mismatches |
| 1200–1300 | — | Lunch | |
| 1300–1500 | 7 | Lab | Group-by aggregations: count, sum, min/max, computed aggregation columns; aggregate-then-join patterns |
| 1500–1515 | — | Break | |
| 1515–1630 | 8 | Lab | Output configuration: overwrite vs. append mode; append mode for snapshot pipelines and historical records |
| 1630–1700 | 9 | Lab | Scheduled pipeline configuration: schedule expression, build failure email alert setup |

**Evening reading:** TM-30, Chapter 4 (Ontology Design — domain analysis and Object Type design methodology). Read before Day 3.

---

### Day 3 — Ontology Design

| Time | Block | Method | Content |
|---|---|---|---|
| 0800–0900 | — | Review | Day 2 questions; common pipeline errors from the lab |
| 0900–1000 | 10 | Lecture | Ontology design methodology: domain analysis, entity identification, relationship mapping, Action design |
| 1000–1015 | — | Break | |
| 1015–1200 | 11 | Lab | Individual design exercise: translate a provided mission requirement to a documented Ontology schema (Object Types, Link Types, cardinality, Actions) |
| 1200–1300 | — | Lunch | |
| 1300–1500 | 12 | Workshop | Design critique: each trainee presents schema; class critiques against the 6-item design rubric; instructor facilitates |
| 1500–1515 | — | Break | |
| 1515–1700 | 13 | Lab | Build the approved design: create the Ontology from the Day 3 design exercise; connect pipeline output via Ontology write step |

**Evening reading:** TM-30, Chapter 2 (conditional logic review); TM-30, Chapter 4 (re-read design rubric in detail before Day 4).

---

### Day 4 — Analytics Tools and AIP Logic

| Time | Block | Method | Content |
|---|---|---|---|
| 0800–0830 | — | Review | Day 3 questions; common Ontology build errors |
| 0830–1030 | 14 | Lab | Contour: pivot tables, calculated columns, parameter controls, workbook structure, saving and sharing analysis views |
| 1030–1045 | — | Break | |
| 1045–1200 | 15 | Lab | Quiver: multi-object analysis, linked views, cross-filter propagation, drilling between Object Types |
| 1200–1300 | — | Lunch | |
| 1300–1430 | 16 | Lab | AIP Logic configuration: connecting triggers, inputs, outputs; human review queue design |
| 1430–1445 | — | Break | |
| 1445–1600 | 17 | Lab | Data lineage: reading a lineage graph; identifying upstream sources, transforms, and downstream consumers; using lineage to diagnose pipeline issues |
| 1600–1700 | 18 | Discuss | C2DAO production standards: what constitutes a production-ready data product; quality gates |

**Evening reading:** TM-30, Chapters 5–7 (Contour, Quiver, Governance) — review what you covered; read governance chapter fully before Day 5.

---

### Day 5 — Governance and Practical Exercise

| Time | Block | Method | Content |
|---|---|---|---|
| 0800–0900 | 19 | Lab | Full C2DAO promotion workflow: branch → change → description → submit → respond to feedback → approval |
| 0900–1000 | 20 | Review | Full-stack review: trace raw source → pipeline → Ontology → Workshop → governance; identify production-readiness gaps |
| 1000–1015 | — | Break | |
| 1015–1100 | 21 | Brief | Practical exercise scenario brief; planning and design time (document design before building) |
| 1100–1200 | — | Buffer | Questions / open lab — resolve tool access or environment issues before evaluation |
| 1200–1300 | — | Lunch | |
| 1300–1700 | 22 | **Eval** | **Practical exercise (evaluated)** |

---

## Required Reading Summary

| When | Reading |
|---|---|
| Before Day 1 | TM-30, Ch 1 + prerequisite self-check |
| Before Day 1 | TM-20, Ch 5 (Workshop) — prerequisite review |
| Day 1 evening | TM-30, Ch 3 (Pipeline — joins and aggregations) |
| Day 2 evening | TM-30, Ch 4 (Ontology Design — methodology and rubric) |
| Day 3 evening | TM-30, Ch 2 (conditional logic review); TM-30, Ch 4 (rubric detail) |
| Day 4 evening | TM-30, Chs 5–7 (Contour, Quiver, Governance) |

---

## Practical Exercise

**Scenario:** The S3 requires a multi-source readiness dashboard combining personnel and equipment data, with a battalion-level portfolio view and drill-down to unit detail.

| # | Task |
|---|---|
| 1 | Design and document an Ontology schema: `Unit` and `ReadinessReport` Object Types, Link Type, and `UpdateStatus` Action — evaluated against design rubric before build begins |
| 2 | Build a Pipeline Builder pipeline joining two provided datasets on `unit_id`; compute an overall readiness score per unit as a calculated column |
| 3 | Configure pipeline output in Append mode; run it twice; verify two distinct snapshot records |
| 4 | Build a multi-page Workshop application: Page 1 portfolio view (all units, status summary, conditional formatting); Page 2 unit detail linked from Page 1 via object selection |
| 5 | Build a Contour workbook showing readiness by battalion with a calculated column for deviation from standard |
| 6 | Submit pipeline and application through the C2DAO promotion workflow with a complete change description; respond to one round of evaluator feedback |

**Evaluator criteria for Ontology design:** Reviewed against the 6-item design rubric. Go requires ≥75% score with no zero-score item.

**Go standard:** All 6 tasks completed. Pipeline produces correct output with two verifiable snapshot records. Workshop navigation and conditional logic validated. Contour deviation column correct. Promotion request includes complete description and trainee responded to steward feedback.

---

## Go Criteria

Your design document is reviewed before you build — a fatally-flawed schema must be corrected before the build phase starts. The promotion workflow requires defending design choices. "The instructor said to" is not an acceptable answer. Be prepared to explain cardinality choices, property types, and Action scope.

---

## Key Tips

| Risk | Guidance |
|---|---|
| Ontology design | Spend 20 min on paper first: entities, relationships, what users need to do — then open Ontology Manager. Design-first trainees build faster and build it right |
| Multi-source joins | Both datasets must be in the same Foundry project or cross-project referenced. A join on inaccessible data silently returns 0 rows. Check row counts after every join |
| Append mode | Configure Append mode **before** the first run. Running once in Overwrite then switching gives you 3 records after two Append runs, not 2 |
| Contour pivot tables | Different from Excel — read TM-30, Section 5-2 before the Contour lab |
| Quiver linked views | Filter links must be explicitly configured — selecting an object does not automatically filter another view. Most common practical exercise failure point |
| Promotion description | "Updated Workshop application" fails. "Changed unit filter to include inactive units per S3 requirement dated 10MAR26" passes |

---

*USAREUR-AF Operational Data Team — UNCLASSIFIED*
*Syllabus TM-30 | Version 2.0 | March 2026*
