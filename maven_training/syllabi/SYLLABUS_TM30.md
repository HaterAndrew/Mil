# COURSE SYLLABUS — TM-30: ADVANCED BUILDER
## Maven Smart System (MSS) — USAREUR-AF

| Field | Detail |
|---|---|
| **Level** | TM-30 (Advanced Builder — data-adjacent specialists) |
| **Duration** | 5 days (40 hours) |
| **Prerequisite** | TM-10 and TM-20 complete (both Go evaluations on file) |
| **Audience** | 17/25-series signal soldiers, S6/G6 staff, G2 intelligence analysts, operational data analysts |
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
| 7 | Configure (not author) an AIP Logic workflow — connect inputs, outputs, trigger conditions, and interpret lineage graphs. **Scope note:** TM-30 covers UI-based configuration of existing AIP Logic workflows only. Authoring AI models, writing prompts, or creating new Agent Studio workflows requires TM-40H (AI Engineer). |
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

> **Supplemental self-study (optional, after evening reading):** Palantir Developers — *Workshop | Creating What If Analyses with Scenarios*, *Workshop | Saving your What If Analyses*, *Workshop | Loading and Applying Scenarios*, *Workshop | How to Preload States in Foundry Workshop Applications*. These four videos cover the Workshop Scenarios feature (what-if analysis and preloaded state) not covered in the Day 1 lab blocks. Instructors with slack time may incorporate one during the Day 1 afternoon design exercise.

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
| 1015–1115 | 11a | Lab | Individual design exercise: translate a provided mission requirement to a documented Ontology schema (Object Types, Link Types, cardinality, Actions) — solo, no instructor guidance |
| 1115–1130 | 11b | Peer check | Structured peer review: each trainee exchanges draft schema with a partner; partner scores against the 6-item rubric; identify any zero-score item and flag to instructor before proceeding. Trainees with a flagged zero-score item revise before Block 12 |
| 1130–1200 | 11c | Lab | Revise and finalize schema based on peer feedback; annotate cardinality and property type choices in writing — these annotations are presented in Block 12 |
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
| 1445–1600 | 17 | Lab | Data lineage diagnostic inject: trainees receive a provided pipeline with a deliberate silent fault (a type mismatch 3 transforms upstream causing a 0-row output). Using only the lineage graph — no error messages — trainees must: (1) trace the lineage to the source of the fault, (2) identify the transform where the type mismatch occurs, and (3) document the fix in writing before opening the transform node. Evaluator confirms diagnosis is correct before trainee clicks. |
| 1600–1700 | 18 | Discuss | C2DAO production standards: what constitutes a production-ready data product; quality gates |

**Evening reading:** TM-30, Chapters 5–7 (Contour and Quiver, AIP Logic, Governance) — review what you covered; read governance chapter fully before Day 5.

---

### Day 5 — Governance and Practical Exercise

| Time | Block | Method | Content |
|---|---|---|---|
| 0800–0900 | 19 | Lab | Full C2DAO promotion workflow: branch → change → description → submit → respond to feedback → approval |
| 0900–1000 | 20 | Review | Full-stack review: trace raw source → pipeline → Ontology → Workshop → governance; identify production-readiness gaps |
| 1000–1015 | — | Break | |
| 1015–1100 | 21 | Brief | Practical exercise scenario brief; **design planning time** — document Ontology schema on paper before touching the platform. Design document submitted to evaluator before build phase begins. |
| 1100–1130 | — | **Design review** | Evaluator reviews Ontology design against 6-item rubric (see Design Rubric section below). Trainees with fatal design flaws correct before proceeding. Clock does not start until design is approved. |
| 1130–1200 | — | Buffer | Open lab — resolve any tool access or environment issues; evaluator available for clarifying questions (no design guidance) |
| 1200–1300 | — | Lunch | |
| 1300–1700 | 22 | **Eval** | **Practical exercise (evaluated)** — build phase begins after lunch; design document already approved |

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
| 5 | Build a Quiver dashboard with linked views: an Object selector (battalion) connected to a bar chart that filters by selection; confirm filter propagation by selecting a battalion and verifying the chart updates to display only that battalion's readiness data |
| 6 | Submit pipeline and application through the C2DAO promotion workflow with a complete change description; respond to one round of evaluator feedback |

**Evaluator criteria for Ontology design:** Reviewed against the 6-item design rubric. Go requires ≥75% score with no zero-score item.

**Go standard:** All 6 tasks completed. Pipeline produces correct output with two verifiable snapshot records. Workshop navigation and conditional logic validated. Quiver linked-view filter propagation demonstrated (selecting a battalion filters the linked bar chart). Promotion request includes complete description and trainee responded to steward feedback.

NOTE: Contour proficiency — Contour analysis (LO 5) is assessed through instructor observation during the Day 4 lab (Blocks 14–15). It is not a separate evaluated task in the practical exercise. Trainees who did not demonstrate Contour proficiency during Day 4 should complete the Contour self-study in TM-30, Chapter 5 before rescheduling.

---

## Ontology Design Rubric — 6-Item Evaluation Criteria

The design document submitted on Day 5 is evaluated against the following six items before build begins. Each item is scored 0 (fail), 1 (partial), or 2 (full). Go requires ≥9/12 with no zero-score item.

| # | Criterion | Score 0 | Score 1 | Score 2 |
|---|---|---|---|---|
| 1 | **Entity identification** — Object Types match the domain entities in the mission requirement | Object Types are wrong or missing entirely | Object Types identified but conflated or over-scoped | Object Types correctly and minimally represent domain entities |
| 2 | **Relationship mapping** — Link Types reflect real relationships; cardinality is correct | No Link Types defined, or Link Types between wrong Object Types | Link Types identified but cardinality wrong (e.g., many-to-many where one-to-many is correct) | Link Types correct; cardinality correct; direction documented |
| 3 | **Property type correctness** — Each property has the correct Foundry type | Multiple type errors (strings for dates, etc.) | One type error that would not block downstream analytics | All property types correct; no type-as-string workarounds |
| 4 | **Primary Key selection** — PK uniquely identifies each object; natural or synthetic key is appropriate | No PK defined, or PK is non-unique | PK defined but is fragile (composite, user-entered, or non-stable) | PK is stable, unique, and sourced from a reliable field |
| 5 | **Action scope** — Actions are narrowly scoped; write rules touch only required properties | Actions write to properties outside stated requirements | Action scope is too broad but not harmful | Actions narrowly scoped; parameter types appropriate; access restriction defined |
| 6 | **Naming convention compliance** — Object Types, properties, and pipelines follow C2DAO naming standards | Multiple naming violations | One naming violation | Full compliance with USAREUR-AF C2DAO naming standards |

---

## Go Criteria

Your design document is reviewed before you build — a fatally-flawed schema must be corrected before the build phase starts. The promotion workflow requires defending design choices. "The instructor said to" is not an acceptable answer. Be prepared to explain cardinality choices, property types, and Action scope.

---

## No-Go Remediation

| Outcome | Action |
|---|---|
| **No-Go — design rubric score below threshold or zero-score item** | Redesign required. Review TM-30, Chapter 4 (Ontology design methodology). Re-evaluation scheduled through unit training coordinator; full Day 5 re-run required. |
| **No-Go — pipeline produces incorrect output** | Review TM-30, Chapter 3 (multi-source joins and append mode). Re-evaluation required. |
| **No-Go — Workshop navigation or conditional logic fails** | Review TM-30, Chapter 2 (advanced Workshop). Re-evaluation required. |
| **No-Go — Quiver linked views not configured** | Review TM-30, Chapter 5 (Quiver linked views). This is the most common single-task failure — complete the Quiver self-study exercise in TM-30 before rescheduling. |
| **No-Go — promotion description incomplete** | Review TM-30, Chapter 7. Same-day retry authorized at evaluator discretion for this item only. |

Re-evaluation requires full repetition of the practical exercise (all tasks), not just the failed tasks. Schedule through unit training coordinator. TM-30 qualification cannot be self-certified.

---

## Key Tips

| Risk | Guidance |
|---|---|
| Ontology design | Spend 20 min on paper first: entities, relationships, what users need to do — then open Ontology Manager. Design-first trainees build faster and build it right |
| Multi-source joins | Both datasets must be in the same Foundry project or cross-project referenced. A join on inaccessible data silently returns 0 rows. Check row counts after every join |
| Append mode | Configure Append mode **before** the first run. Running once in Overwrite then switching gives you 3 records after two Append runs, not 2 |
| Contour pivot tables | Different from Excel — read TM-30, Section 5-2 before the Contour lab |
| Quiver linked views | **Most common practical exercise No-Go.** Filter links must be explicitly configured — selecting an object does NOT automatically filter another view. Complete the Quiver self-study in TM-30, Chapter 5 the evening before Day 5. Do not skip this. |
| AIP Logic scope | TM-30 covers configuration only — connecting triggers, inputs, outputs on existing workflows. If the scenario asks you to author a new AI model or write prompts, that is out of scope. Raise it immediately rather than attempting it. |
| Promotion description | "Updated Workshop application" fails. "Changed unit filter to include inactive units per S3 requirement dated 10MAR26" passes |

---

## Continuation

TM-30 is the gateway to **all** TM-40 tracks — both WFF (TM-40A–F) and Specialist (TM-40G–O). TM-30 completion is a **hard prerequisite — no waivers** — for every track in the TM-40 series.

**WFF Tracks (TM-40A–F) — prereq: TM-30 (required):**

| Track | WFF | Audience |
|---|---|---|
| TM-40A | Intelligence | G2/S2 staff, targeting officers, all-source analysts |
| TM-40B | Fires | FSOs, FSEs, targeting officers, fires NCOs |
| TM-40C | Movement & Maneuver | G3/S3 staff, operations officers, maneuver planners |
| TM-40D | Sustainment | G4/S4 staff, logistics officers, supply chain managers |
| TM-40E | Protection | FP officers, CBRN officers, provost marshal staff |
| TM-40F | Mission Command | Battle captains, XOs, CDRs, MC-function staff |

**Specialist Tracks (TM-40G–O) — prereq: TM-30 (required):**

| Track | Specialist Role | Advanced Level |
|---|---|---|
| TM-40G | ORSA | TM-50G (Advanced ORSA) |
| TM-40H | AI Engineer | TM-50H (Advanced AI Engineer) |
| TM-40M | ML Engineer | TM-50M (Advanced ML Engineer) |
| TM-40J | Program Manager | TM-50J (Advanced Program Manager) |
| TM-40K | Knowledge Manager | TM-50K (Advanced Knowledge Manager) |
| TM-40L | Software Engineer | TM-50L (Advanced Software Engineer) |
| TM-40N | UX Designer | TM-50N (Advanced UX Designer) |
| TM-40O | Platform Engineer | TM-50O (Advanced Platform Engineer) |

**T3-I (Instructor Certification) — parallel path:**
TM-30 graduates who demonstrate strong instructional aptitude may be nominated for T3-I (Instructor Certification). T3-I is a 5-day course that qualifies graduates to deliver TM-10, TM-20, and TM-30 as certified instructors. See SYLLABUS_T3I for details.

**TM-50A–F do not exist.** The advanced series is TM-50G–O only. Any reference to TM-50A through TM-50F is stale and incorrect.

---

*USAREUR-AF Operational Data Team*
*Syllabus TM-30 | Version 2.0 | March 2026*
