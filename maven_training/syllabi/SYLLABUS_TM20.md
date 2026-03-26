# COURSE SYLLABUS — SL 2: BUILDER
## Maven Smart System (MSS) — USAREUR-AF

| Field | Detail |
|---|---|
| **Level** | SL 2 (Builder — all staff) |
| **Duration** | 5 days (40 hours) |
| **Prerequisite** | SL 1 complete (Go evaluation on file) |
| **Audience** | All staff assigned to build or maintain MSS data products |
| **Format** | Instructor-led lab + practical exercise |
| **Location** | MSS Training Environment |

---

**BLUF:** SL 2 teaches you to build real, deployable data products — SITREP trackers, readiness dashboards, equipment status boards. After this course you can create Foundry projects, ingest data through Pipeline Builder, define Object Types and Link Types, configure Actions, and publish Workshop applications. By Day 5 you are building from memory, not following steps.

---

## Learning Objectives

| # | Objective |
|---|---|
| 1 | Create a Foundry project with correct naming, markings, and folder structure per USAREUR-AF C2DAO conventions |
| 2 | Ingest a file into Foundry; verify data quality (row count, type validation, null check) |
| 3 | Build a Pipeline Builder pipeline with filter, rename, type-cast, and calculated-column steps producing a clean typed output |
| 4 | Build a Pipeline Builder pipeline joining two datasets on a shared key with derived columns |
| 5 | Create an Object Type with typed properties, a Primary Key, and a display name expression |
| 6 | Create a Link Type connecting two Object Types with correct cardinality |
| 7 | Configure a Pipeline Builder Ontology write step that populates an Object Type from pipeline output |
| 8 | Configure an Action that writes to an Object Type property, with a parameter, description, and access-control rule |
| 9 | Build a Workshop application with table, filter, metric widget, and bar chart connected to live Ontology data |
| 10 | Connect an Action button to a Workshop widget; confirm execution and UI refresh |
| 11 | Manage project access: grant Viewer and Editor roles; confirm role behavior with a test account |
| 12 | Create a Foundry branch, make a change on the branch, and submit for data steward promotion with a complete description |

---

## Pre-Course Checklist

Complete **5+ duty days before Day 1:**

- [ ] Request **Builder access** in the MSS Training Environment from your unit MSS Administrator (standard Viewer access from SL 1 is insufficient)
- [ ] Confirm CAC and PIV PIN work on the MSS-connected workstation
- [ ] Read TM-20, Chapter 1 (Introduction, Safety Summary, Prerequisite Review) — 20 min
- [ ] Read TM-20, Chapter 2 (Project Setup and Naming Conventions) — 15 min

**Do not arrive without Builder access. You cannot complete any lab without it.**

---

## Daily Schedule

### Day 1 — Project Fundamentals and File Ingestion

| Time | Block | Method | Content |
|---|---|---|---|
| 0800–0830 | — | Brief | SL 2 overview; what you will build by Day 5; course standards and Go criteria |
| 0830–1000 | 1 | Lab | Project creation: naming conventions, classification markings, folder structure |
| 1000–1015 | — | Break | |
| 1015–1100 | 2 | Lab | File ingestion: upload a CSV; inspect schema, types, and row count |
| 1100–1200 | 3 | Lab | Dataset explorer: column profiling, null detection, type mismatches |
| 1200–1300 | — | Lunch | |
| 1300–1500 | 4 | Lab | Pipeline Builder orientation: canvas layout, step library, input/output dataset config |
| 1500–1530 | 5 | Discuss | C2DAO naming conventions: datasets, pipelines, Object Types |
| 1530–1700 | 6 | Lab | Individual practice: create a second project, ingest a provided dataset, confirm naming compliance |

**Evening reading:** TM-20, Chapter 3 (Pipeline Builder — overview and filter/rename/cast sections).

---

### Day 2 — Pipeline Builder: Clean and Transform

| Time | Block | Method | Content |
|---|---|---|---|
| 0800–0830 | — | Review | Day 1 questions; confirm all trainees have projects and ingested data |
| 0830–1030 | 7 | Lab | Pipeline: filter step, rename step, CAST for type correction |
| 1030–1045 | — | Break | |
| 1045–1200 | 8 | Lab | Pipeline: calculated columns — string functions, conditional logic (`IF/CASE`), `COALESCE` for nulls |
| 1200–1300 | — | Lunch | |
| 1300–1500 | 9 | Lab | Pipeline: date and time functions — `DATEDIFF`, `DATE_TRUNC`, `CURRENT_DATE`; test with known-answer records |
| 1500–1515 | — | Break | |
| 1515–1700 | 10 | Lab | End-to-end pipeline practice: build a complete clean-and-transform pipeline from raw input to typed filtered output; run and verify |

**Evening reading:** TM-20, Chapter 3 (join section); TM-20, Chapter 4 (Ontology Manager — property type guidance). Read the property type table before Day 3.

---

### Day 3 — Pipeline Builder: Joins and Ontology Manager

| Time | Block | Method | Content |
|---|---|---|---|
| 0800–0830 | — | Review | Day 2 questions; pipeline troubleshooting: error messages, schema mismatches |
| 0830–1030 | 11 | Lab | Pipeline: join step — inner/left join, key selection, handling duplicates post-join, output column selection |
| 1030–1045 | — | Break | |
| 1045–1200 | 12 | Lab | Pipeline: group-by aggregation; union step basics; output dataset configuration (overwrite vs. append mode) |
| 1200–1300 | — | Lunch | |
| — | — | **STOP** | **Before opening Ontology Manager:** Review TM-20, Chapter 4 property type table. Property types are immutable after Object Type creation — a wrong type requires deleting and rebuilding the Object Type. Verify your intended property types before creating anything. |
| 1300–1500 | 13 | Lab | Ontology Manager: create an Object Type — properties, types, Primary Key, display name expression |
| 1500–1515 | — | Break | |
| 1515–1630 | 14 | Lab | Ontology Manager: create a Link Type — connecting two Object Types, cardinality, directionality |
| 1630–1700 | 15 | Lab | Ontology practice: design a second Object Type from a provided scenario; verify naming compliance |

**Evening reading:** TM-20, Chapter 3 (Ontology write step section); TM-20, Chapter 4 (Actions section); TM-20, Chapter 5 (Workshop — skim widget overview); TM-20, Chapter 8 (Builder Standards and Governance).

---

### Day 4 — Ontology Write Step, Actions, and Workshop Applications

| Time | Block | Method | Content |
|---|---|---|---|
| 0800–0845 | — | Review + Discuss | Day 3 questions; **access control model: Viewer vs. Editor roles** — what each can and cannot do; why a Viewer triggering an Action is a hard No-Go on the practical exercise |
| 0845–0945 | 16 | Lab | Pipeline: Ontology write step — connect Day 3 pipeline output to Object Type; configure property mapping; run and verify |
| 0945–1000 | — | Break | |
| 1000–1130 | 17 | Lab | Actions: create a basic Action — parameter, write rule, access restriction; test from Ontology Manager |
| 1130–1145 | — | Break | |
| 1145–1300 | 18 | Lab | Workshop orientation: canvas, widget library, Object Type binding — table widget with live data |
| 1300–1400 | — | Lunch | |
| 1400–1530 | 19 | Lab | Workshop: filter widget, metric widget, bar chart widget — layout and data source configuration |
| 1530–1545 | — | Break | |
| 1545–1700 | 20 | Lab | Workshop: connecting an Action button — trigger, confirmation prompt, post-action refresh |

**Evening reading:** TM-20, Chapter 6 (Publishing/Access); TM-20, Chapter 7 (Governance — branching and promotion); TM-20, Chapter 9 (Troubleshooting and Common Errors).

---

### Day 5 — Publishing, Governance, and Practical Exercise

| Time | Block | Method | Content |
|---|---|---|---|
| 0800–0900 | 21 | Lab | Workshop: publishing — set visibility, grant Viewer access, confirm Viewer cannot edit |
| 0900–1000 | 22 | Lab | Branching: create a branch; make a change on the branch; verify the change is branch-only |
| 1000–1015 | — | Break | |
| 1015–1100 | 23 | Lab | Promotion workflow: write a promotion description; submit to data steward; respond to a rejection comment |
| 1100–1200 | 24 | Review | Full-stack review: trace raw file → pipeline → Object Type → Workshop → access control; identify gaps |
| 1200–1300 | — | Lunch | |
| 1300–1700 | 25 | **Eval** | **Practical exercise (evaluated)** |

---

## Required Reading Summary

| When | Reading |
|---|---|
| Before Day 1 | TM-20, Ch 1 (Intro/Safety/Prereq Review) |
| Before Day 1 | TM-20, Ch 2 (Project Setup and Naming) |
| Day 1 evening | TM-20, Ch 3 (Pipeline Builder — overview, filter, rename, cast) |
| Day 2 evening | TM-20, Ch 3 (Pipeline — joins); TM-20, Ch 4 (Ontology — property types) |
| Day 3 evening | TM-20, Ch 4 (Actions); TM-20, Ch 5 (Workshop overview); TM-20, Ch 8 (Builder Standards and Governance) |
| Day 4 evening | TM-20, Ch 6 (Publishing/Access); TM-20, Ch 7 (Governance/Branching); TM-20, Ch 9 (Troubleshooting and Common Errors) |
| After training | TM-20, Chapters 5–9 — full reference read |

---

## Practical Exercise

**Scenario:** Your S4 officer needs an equipment readiness tracker. Provided files: an Excel spreadsheet of equipment IDs, units, and C-ratings; a CSV of unit identifiers and assigned locations.

| # | Task |
|---|---|
| 1 | Create a Foundry project with correct naming, markings, and folder structure |
| 2 | Ingest both files; confirm row counts and types match source |
| 3 | Build a pipeline: validate, clean, type-cast, join on `unit_id`; output a clean equipment-with-location dataset |
| 4 | Create an `Equipment` Object Type with `equipment_id`, `unit`, `location`, `c_rating`, `last_updated` properties (correctly typed) |
| 5 | Create a `Unit` Object Type with `unit_id` and `unit_name`; create a Link Type from `Equipment` to `Unit` |
| 6 | Configure the pipeline with an Ontology write step that populates `Equipment` objects |
| 7 | Configure an `UpdateCRating` Action: parameter `new_c_rating` (String enum: C1/C2/C3/C4), write rule to `c_rating`, access restricted to Editor role |
| 8 | Build a Workshop application: table of all equipment, filter by `unit` and `c_rating`, metric widget showing count of C1 equipment, bar chart by C-rating |
| 9 | Connect `UpdateCRating` Action to a button; execute it and verify the table refreshes |
| 10 | Grant a test account Viewer access; confirm it cannot trigger the Action or modify data |
| 11 | Create a branch; change the application header text; submit a promotion request with a complete change description |

**Go standard:** All 11 tasks completed without instructor assistance. Pipeline runs without error. Object count matches source row count. Workshop loads for Viewer-role test account with correct filtered data. Action executes and updates Object property. Branch and promotion request exist with complete description.

---

## Go Criteria

Pipeline must run to completion. Workshop must load for a Viewer-role user with correctly filtered data. Action must execute and update the Object property. Branch must exist in Foundry with your change visible and the promotion description filled in.

**Not Go:** pipeline with unresolved errors; Action that errors on execution; Viewer test account that can modify data.

---

## No-Go Remediation

| Outcome | Action |
|---|---|
| **No-Go — pipeline errors** | Review TM-20, Chapter 3 (pipeline troubleshooting). Re-evaluation scheduled through unit training coordinator. |
| **No-Go — Action errors on execution** | Review TM-20, Chapter 4 (Actions). Verify write rule and parameter configuration. Re-evaluation required. |
| **No-Go — Viewer account can modify data** | Critical security finding. Review TM-20, Chapter 6 (access control). Must correct before any re-evaluation attempt. Report to unit data steward. |
| **No-Go — missing promotion description** | Review TM-20, Chapter 7. Same-day retry authorized at instructor discretion for this item only. |

Full re-evaluation requires scheduling through the unit training coordinator. Same-day retry on isolated items is at instructor discretion only — not automatic. SL 2 qualification cannot be self-certified.

---

## Key Tips

| Risk | Guidance |
|---|---|
| Object Type property types | Read Chapter 4 property type guidance **before** Day 3 — property types are immutable after objects are created. Wrong type = delete and rebuild |
| Date functions | Test `DATEDIFF` and date arithmetic with known-answer records before moving on — one wrong type configuration fails all downstream date calculations silently |
| Join step row count | Check row counts after every join — a join on inaccessible data silently returns 0 rows with no error |
| Branching timing | Create the branch **before** making changes — changes made on main are already in production |
| Viewer/Editor access | Viewer triggering the Action is a hard No-Go — fix it before the evaluator checks |
| Promotion description | The data steward will reject a submission without a description. Write: what changed, why, and downstream impact |
| Day 5 time | 4 hours for 11 tasks. Build the full stack once on Day 4 evening. Trainees who build it twice pass clean |

---

## Continuation

SL 2 completion qualifies personnel to advance to SL 3 (Advanced Builder). **All SL 4 tracks — both WFF (A–F) and Specialist (G–O) — require SL 3 completion before enrollment.** SL 3 is a hard prerequisite — no waivers — for every SL 4 track. Confirm completion with your unit training coordinator before registering.

| Path | Track | Prerequisite | Who |
|---|---|---|---|
| **Advanced Builder** | SL 3 | SL 2 (this course) — hard prerequisite, no waivers | All personnel proceeding to any SL 4 track |
| **WFF — Intelligence** | SL 4A | SL 3 (required) | G2/S2 staff, targeting officers, all-source analysts |
| **WFF — Fires** | SL 4B | SL 3 (required) | FSOs, FSEs, targeting officers, fires NCOs |
| **WFF — Movement & Maneuver** | SL 4C | SL 3 (required) | G3/S3 staff, operations officers, maneuver planners |
| **WFF — Sustainment** | SL 4D | SL 3 (required) | G4/S4 staff, logistics officers, supply chain managers |
| **WFF — Protection** | SL 4E | SL 3 (required) | FP officers, CBRN officers, provost marshal staff |
| **WFF — Mission Command** | SL 4F | SL 3 (required) | Battle captains, XOs, CDRs, MC-function staff |
| **Specialist path** | SL 4G–O (via SL 3) | SL 3 (required) | Data analysts, 17/25-series, ORSA, AI/ML, PM, KM, SWE |

All SL 4 tracks — WFF (SL 4A–F) and Specialist (SL 4G–O) — require **SL 3** as a hard prerequisite. Specialist tracks (SL 4G–O) additionally require code-level preparation per their individual syllabi.

---

*USAREUR-AF Operational Data Team*
*Syllabus SL 2 | Version 2.0 | March 2026*
