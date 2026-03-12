# COURSE SYLLABUS
## TM-20 — BUILDER
### Maven Smart System (MSS) — USAREUR-AF

| | |
|---|---|
| **Level** | TM-20 (Builder — all staff) |
| **Duration** | 5 days (40 hours) |
| **Prerequisite** | TM-10 complete (Go evaluation on file) |
| **Audience** | All staff assigned to build or maintain MSS data products |
| **Format** | Instructor-led lab + practical exercise |
| **Location** | MSS Training Environment |

---

## What This Course Does for You

TM-20 teaches you to build. After this course you can create Foundry projects, ingest data through Pipeline Builder, define Object Types and Link Types, configure Actions, and publish Workshop applications that your unit can use. Everything is visual — no code required.

The products you build at TM-20 are real, deployable data products. Unit SITREP trackers, readiness dashboards, equipment status boards, and personnel accountability tools are all TM-20-level builds. If you need more complex work — multi-source joins, advanced Ontology design, Contour workbooks for analysis — that is TM-30.

Five days provides the time to build each component correctly, break things, recover, and build them again. Repetition is the standard here. By Day 5 you are not following steps — you are building from memory.

---

## Learning Objectives

By the end of training, you will be able to:

1. Create a Foundry project with correct naming, markings, and folder structure per USAREUR-AF C2DAO conventions
2. Ingest a file into Foundry and verify data quality (row count, type validation, null check)
3. Build a Pipeline Builder pipeline with filter, rename, type-cast, and calculated-column steps that produces a clean, typed output dataset
4. Build a Pipeline Builder pipeline that joins two datasets on a shared key and computes derived columns
5. Create an Object Type with typed properties, a Primary Key, and a display name expression
6. Create a Link Type connecting two Object Types with correct cardinality
7. Configure a Pipeline Builder Ontology write step that populates an Object Type from pipeline output
8. Configure an Action that writes to an Object Type property, with a parameter, a description, and an access-control rule
9. Build a Workshop application with a table, filter, metric widget, and bar chart — connected to live Ontology data
10. Connect an Action button to a Workshop widget; confirm the Action executes and the UI refreshes
11. Manage project access: grant Viewer and Editor roles; confirm role behavior with a test account
12. Create a Foundry branch, make a change on the branch, and submit for data steward promotion with a complete description

---

## Before You Attend: Pre-Course Checklist

Complete **5+ duty days before Day 1:**
- [ ] Request **Builder access** in the MSS Training Environment from your unit MSS Administrator. Standard Viewer access (from TM-10) is not sufficient. Builder access is required to create projects and pipelines.
- [ ] Confirm your CAC and PIV PIN work on the MSS-connected workstation.
- [ ] Read TM-20, Chapter 1 (Introduction, Safety Summary, Prerequisite Review) — 20 min.
- [ ] Read TM-20, Chapter 2 (Project Setup and Naming Conventions) — 15 min.

Do not arrive without Builder access. Without it you cannot complete any lab in this course.

---

## Daily Schedule

**Day 1 — Project Fundamentals and File Ingestion**

| Time | Block | Method | Content |
|---|---|---|---|
| 0800–0830 | —    | Brief    | TM-20 overview; what you will build by Day 5; course standards and Go criteria |
| 0830–1000 | 1    | Lab      | Project creation: naming conventions, classification markings, folder structure |
| 1000–1015 | —    | Break    | |
| 1015–1100 | 2    | Lab      | File ingestion: upload a CSV; inspect schema, types, and row count in Foundry |
| 1100–1200 | 3    | Lab      | Dataset explorer: column profiling, null detection, type mismatches — building QC habits |
| 1200–1300 | —    | Lunch    | |
| 1300–1500 | 4    | Lab      | Pipeline Builder orientation: canvas layout, step library, input/output dataset config |
| 1500–1530 | 5    | Discuss  | C2DAO naming conventions: datasets, pipelines, Object Types — the standard you will follow all week |
| 1530–1700 | 6    | Lab      | Individual practice: create a second project, ingest a provided dataset, confirm naming compliance |

**Evening reading:** TM-20, Chapter 3 (Pipeline Builder — overview and filter/rename/cast sections).

---

**Day 2 — Pipeline Builder: Clean and Transform**

| Time | Block | Method | Content |
|---|---|---|---|
| 0800–0830 | —    | Review   | Day 1 question period; confirm all trainees have projects and ingested data |
| 0830–1030 | 7    | Lab      | Pipeline: filter step (row-level conditions), rename step, CAST for type correction |
| 1030–1045 | —    | Break    | |
| 1045–1200 | 8    | Lab      | Pipeline: calculated columns — string functions, conditional logic (`IF/CASE`), `COALESCE` for nulls |
| 1200–1300 | —    | Lunch    | |
| 1300–1500 | 9    | Lab      | Pipeline: date and time functions — `DATEDIFF`, `DATE_TRUNC`, `CURRENT_DATE`; test with known-answer records |
| 1500–1515 | —    | Break    | |
| 1515–1700 | 10   | Lab      | End-to-end pipeline practice: build a complete clean-and-transform pipeline from raw input to typed, filtered output; run and verify |

**Evening reading:** TM-20, Chapter 3 (join section); TM-20, Chapter 4 (Ontology Manager — property type guidance). Read the property type table before Day 3.

---

**Day 3 — Pipeline Builder: Joins and Ontology Manager**

| Time | Block | Method | Content |
|---|---|---|---|
| 0800–0830 | —    | Review   | Day 2 question period; pipeline troubleshooting: reading error messages, schema mismatches |
| 0830–1030 | 11   | Lab      | Pipeline: join step — inner/left join, key selection, handling duplicates post-join, output column selection |
| 1030–1045 | —    | Break    | |
| 1045–1200 | 12   | Lab      | Pipeline: group-by aggregation; union step basics; output dataset configuration (overwrite vs. append mode) |
| 1200–1300 | —    | Lunch    | |
| 1300–1500 | 13   | Lab      | Ontology Manager: create an Object Type — properties, types, Primary Key, display name expression |
| 1500–1515 | —    | Break    | |
| 1515–1600 | 14   | Lab      | Ontology Manager: create a Link Type — connecting two Object Types, cardinality setting, directionality |
| 1600–1700 | 15   | Lab      | Pipeline: Ontology write step — connect pipeline output to Object Type; configure property mapping; run and verify objects are created |

**Evening reading:** TM-20, Chapter 4 (Actions section); TM-20, Chapter 5 (Workshop — skim the widget overview).

---

**Day 4 — Actions and Workshop Applications**

| Time | Block | Method | Content |
|---|---|---|---|
| 0800–0830 | —    | Review   | Day 3 question period; common Ontology write failures: type mismatch, missing Primary Key |
| 0830–1000 | 16   | Lab      | Actions: create a basic Action — parameter, write rule, access restriction; test from Ontology Manager |
| 1000–1015 | —    | Break    | |
| 1015–1200 | 17   | Lab      | Workshop orientation: canvas, widget library, Object Type binding — table widget with live data |
| 1200–1300 | —    | Lunch    | |
| 1300–1500 | 18   | Lab      | Workshop: filter widget, metric widget, bar chart widget — layout and data source configuration |
| 1500–1515 | —    | Break    | |
| 1515–1630 | 19   | Lab      | Workshop: connecting an Action button to the application — trigger, confirmation prompt, post-action refresh |
| 1630–1700 | 20   | Discuss  | Access control model: Viewer vs. Editor roles; what each role can and cannot do |

**Evening reading:** TM-20, Chapter 6 (Workshop — publishing and access control); TM-20, Chapter 7 (Governance — branching and promotion).

---

**Day 5 — Publishing, Governance, and Practical Exercise**

| Time | Block | Method | Content |
|---|---|---|---|
| 0800–0900 | 21   | Lab      | Workshop: publishing — set application visibility, grant Viewer access, confirm Viewer cannot edit |
| 0900–1000 | 22   | Lab      | Branching: create a branch; make a change on the branch (not on main); verify the change is branch-only |
| 1000–1015 | —    | Break    | |
| 1015–1100 | 23   | Lab      | Promotion workflow: write a promotion description; submit to data steward; respond to a rejection comment |
| 1100–1200 | 24   | Review   | Full-stack review: trace your own data product from raw file → pipeline → Object Type → Workshop → access control; identify any gaps |
| 1200–1300 | —    | Lunch    | |
| 1300–1700 | 25   | **Eval** | **Practical exercise (evaluated)** |

---

## Required Reading Summary

| When | Reading |
|---|---|
| Before Day 1 | TM-20, Ch 1 (Intro/Safety/Prereq Review) |
| Before Day 1 | TM-20, Ch 2 (Project Setup and Naming) |
| Day 1 evening | TM-20, Ch 3 (Pipeline Builder — overview, filter, rename, cast) |
| Day 2 evening | TM-20, Ch 3 (Pipeline — joins); TM-20, Ch 4 (Ontology — property types) |
| Day 3 evening | TM-20, Ch 4 (Actions); TM-20, Ch 5 (Workshop overview) |
| Day 4 evening | TM-20, Ch 6 (Publishing/Access); TM-20, Ch 7 (Governance/Branching) |
| After training | TM-20, Chapters 5–7 — full reference read |

---

## Practical Exercise

**Scenario:** Your S4 officer needs an equipment readiness tracker. You have two provided files: an Excel spreadsheet of equipment IDs, units, and C-ratings; and a CSV of unit identifiers and assigned locations. Build the full stack from scratch.

**Tasks:**
1. Create a Foundry project with correct naming, markings, and folder structure
2. Ingest both provided files; confirm row counts and types match the source
3. Build a Pipeline Builder pipeline: validate, clean, type-cast, and join the two datasets on `unit_id`; output a clean equipment-with-location dataset
4. Create an `Equipment` Object Type with `equipment_id`, `unit`, `location`, `c_rating`, `last_updated` properties (correctly typed)
5. Create a `Unit` Object Type with `unit_id` and `unit_name`; create a Link Type from `Equipment` to `Unit`
6. Configure the pipeline with an Ontology write step that populates `Equipment` objects
7. Configure an `UpdateCRating` Action: parameter `new_c_rating` (String enum: C1/C2/C3/C4), write rule to `c_rating`, access restricted to Editor role
8. Build a Workshop application: table of all equipment, filter by `unit` and `c_rating`, metric widget showing count of C1 equipment, bar chart of equipment count by C-rating
9. Connect the `UpdateCRating` Action to a button in the Workshop application; execute the Action and verify the table refreshes
10. Grant a test account Viewer access; confirm the test account cannot trigger the Action or modify data
11. Create a branch; change the application header text; submit a promotion request with a complete change description

**Go standard:** All 11 tasks completed without instructor assistance. Pipeline runs to completion without error. Object count in Foundry matches row count in source data. Workshop application loads for a Viewer-role test account with correct filtered data. Action executes and updates the Object property. Branch and promotion request exist in Foundry with a complete description.

---

## What "Go" Looks Like

Your pipeline must run to completion. Your Workshop application must load for a Viewer-role user and display correctly filtered data. The Action must execute and update the Object property. The branch must exist in Foundry with your change visible and the promotion description filled in.

Go does not require design perfection. An Object Type with all required properties correctly typed and a pipeline that produces correct output is Go, even if a naming convention has a minor deviation you'll correct before production. What is not Go: a pipeline with errors you haven't resolved, an Action that errors on execution, or a Viewer-role test account that can modify data.

---

## Tips From Previous Graduates

- Read the property type guidance in Chapter 4 **before** Day 3. Object Type property types are immutable after objects are created. If you type a property as `String` when it should be `Integer`, you must delete the Object Type and rebuild. This costs an hour you don't have on Day 3.
- Pipeline Builder's `DATEDIFF` and date functions behave differently than Excel. Test all date arithmetic with known-answer records before moving on. One wrong date in the type configuration causes every downstream date calculation to fail silently.
- The join step requires both input datasets to be in your project (or cross-project referenced). If you join on datasets you can't access, the output will silently return 0 rows with no error. Check row counts after every join.
- Branching trips most trainees at first: create the branch **before** making changes. A change made on main is already in production. You cannot retroactively branch around a change on main.
- The Viewer/Editor access distinction is tested. If your test Viewer account can trigger the Action or modify data, your access configuration is wrong. Fix it before the evaluator checks — this is a hard No-Go item.
- The data steward promotion workflow requires a description. The evaluator (playing data steward) will reject a submission without a description. This is intentional. Write: what changed, why, and what the downstream impact is.
- On Day 5, you have 4 hours for 11 tasks. That is not much margin. Practice the full stack build on Day 4 evening using a personal dataset. The trainees who pass clean are the ones who built it twice.

---

*USAREUR-AF Operational Data Team — UNCLASSIFIED*
*Syllabus TM-20 | Version 2.0 | March 2026*
