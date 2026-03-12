# COURSE SYLLABUS
## TM-40D — PROGRAM MANAGER
### Maven Smart System (MSS) — USAREUR-AF

| | |
|---|---|
| **Level** | TM-40D (Program Manager Specialist Track) |
| **Duration** | 3 days (24 hours) |
| **Prerequisites** | TM-10 and TM-20 (both Go evaluations on file). TM-30 recommended but not required. |
| **Audience** | Program managers, resource managers, G8/S8 staff officers, acquisition professionals |
| **Format** | Instructor-led lab + practical exercise |
| **Location** | MSS Training Environment |

---

## What This Course Does for You

After this course you can replace your unit's manual PowerPoint IPR deck with a live MSS dashboard. You will design the program data model, ingest milestone and budget data from GFEBS and IMS exports, build Workshop milestone trackers with RAG status, visualize obligation rates against quarterly targets, and produce commander-ready portfolio health products from MSS.

The goal is a dashboard that refreshes from data — not one that someone updates by hand before every brief.

Three days provides the time to build each component, complete a full supervised practice run, and then execute the evaluated practical exercise without shortcuts. Day 3 morning is a build-from-scratch practice run — the same scenario type as the evaluation, ungraded, with instructor coaching available. The afternoon is the evaluation.

---

## Learning Objectives

By the end of training, you will be able to:

1. Design a program data architecture with Program, Milestone, Resource, and Risk Object Types and document it before building
2. Build a Pipeline Builder pipeline that ingests an IMS spreadsheet and computes milestone variance and RAG status with a visible data-as-of timestamp
3. Build a Pipeline Builder pipeline for GFEBS obligation data in Append mode for historical obligation rate tracking
4. Build a Workshop milestone tracking dashboard with RAG status conditional formatting and a data-as-of timestamp widget
5. Build a Quiver budget execution visualization showing obligation rate vs. quarterly target with a reference line
6. Build a Contour portfolio health matrix with cross-program status roll-up sorted by worst overall health
7. Configure a scheduled pipeline refresh with build failure notification
8. Produce an IPR product from MSS that meets all items on the PM Dashboard Standards Checklist

---

## Before You Attend: Pre-Course Checklist

Complete **5+ duty days before Day 1:**
- [ ] Request **Builder access** in the MSS Training Environment from your unit MSS Administrator
- [ ] Coordinate with your G8/S8 POC for sample GFEBS training data export before Day 1
- [ ] Read TM-40D, Chapter 1 (Introduction) and complete the prerequisite check — 20 min
- [ ] Read TM-40D, Chapter 2 (Program Data Architecture) — the data model section before the Ontology lab

---

## Daily Schedule

**Day 1 — Data Architecture and Ingestion**

| Time | Block | Method | Content |
|---|---|---|---|
| 0800–0830 | —  | Brief    | PM role on MSS; why dashboards fail; the data-as-of timestamp requirement and why it is non-negotiable |
| 0830–1000 | 1  | Lab      | Program data architecture: Program, Milestone, Resource, Risk Object Types — design on paper before opening Ontology Manager |
| 1000–1015 | —  | Break    | |
| 1015–1200 | 2  | Lab      | Ontology: create PM Object Types, Link Types (Program↔Milestone, Program↔Risk), Action configuration |
| 1200–1300 | —  | Lunch    | |
| 1300–1500 | 3  | Lab      | Pipeline Builder: IMS ingestion, date arithmetic (`DATEDIFF`), milestone variance computed column, RAG status calculated column, data-as-of timestamp |
| 1500–1515 | —  | Break    | |
| 1515–1700 | 4  | Lab      | Pipeline Builder: GFEBS obligation data ingestion; Append mode snapshot pipeline — run twice, verify two distinct snapshot records |

**Evening reading:** TM-40D, Chapter 3 (Milestone Tracking) — review the RAG computation logic; TM-40D, Chapter 4 (Resource and Budget) — review the obligation rate threshold table.

---

**Day 2 — Dashboards, Portfolio, and Reporting**

| Time | Block | Method | Content |
|---|---|---|---|
| 0800–0830 | —  | Review   | Day 1 questions; Append mode pipeline verification — confirm two snapshot records before moving on |
| 0830–1030 | 5  | Lab      | Workshop: milestone dashboard — table with RAG conditional formatting, data-as-of timestamp widget, slipped milestones filtered page |
| 1030–1045 | —  | Break    | |
| 1045–1200 | 6  | Lab      | Quiver: obligation rate chart, reference line at quarterly target (Q2 = 50%), at-risk program identification |
| 1200–1300 | —  | Lunch    | |
| 1300–1500 | 7  | Lab      | Contour: portfolio health matrix — cross-program status roll-up, sort by `overall_status` ascending (RED items at top) |
| 1500–1515 | —  | Break    | |
| 1515–1630 | 8  | Lab      | Reporting: scheduled pipeline refresh configuration; build failure notification setup; PDF snapshot export procedure |
| 1630–1700 | 9  | Discuss  | PM Dashboard Standards Checklist walk-through: every checklist item, what evaluators look for, common failures |

**Evening reading:** TM-40D, Chapters 5–8 (Portfolio, Pipelines, Commander Briefs, Governance) — reference read; walk through your Day 2 product against the PM Dashboard Standards Checklist before Day 3.

---

**Day 3 — Practice Run and Practical Exercise**

| Time | Block | Method | Content |
|---|---|---|---|
| 0800–0830 | —  | Brief    | Day 3 overview; access management, classification, C2DAO governance for PM applications |
| 0830–1145 | 10 | Lab      | **Supervised practice run (ungraded):** build the full stack from a different provided dataset — IMS ingestion → RAG pipeline → Append snapshot → Workshop milestone dashboard → Quiver obligation chart. Instructor coaching available. |
| 1145–1200 | —  | Brief    | Practical exercise scenario brief; review PM Dashboard Standards Checklist before evaluation |
| 1200–1300 | —  | Lunch    | |
| 1300–1700 | 11 | **Eval** | **Practical exercise (evaluated)** |

---

## Required Reading Summary

| When | Reading |
|---|---|
| Before Day 1 | TM-40D, Ch 1 (Introduction/prereq check) |
| Before Day 1 | TM-40D, Ch 2 (Program Data Architecture) |
| Day 1 evening | TM-40D, Ch 3 (Milestone Tracking — RAG logic) |
| Day 1 evening | TM-40D, Ch 4 (Resource/Budget — threshold table) |
| Day 2 evening | TM-40D, Chs 5–8 (reference read; walk product against checklist) |

---

## Practical Exercise

**Scenario:** Your program office needs an MSS IPR package for a G8 review. Using provided synthetic IMS and GFEBS data:

**Tasks:**
1. Design the program data architecture (Object Types, Link Types) — document before building
2. Build the milestone ingestion pipeline: validate, compute variance and RAG status, include data-as-of timestamp
3. Build a Workshop milestone dashboard: table with RAG conditional formatting, data-as-of timestamp widget, slipped milestones page
4. Build a Quiver obligation rate chart with a reference line at the Q2 target (50%)
5. Configure the snapshot pipeline in Append mode; run twice; verify two distinct snapshot records with different timestamps
6. Build a Contour portfolio matrix; configure sort by `overall_status` ascending; export as PDF
7. Complete the PM Dashboard Standards Checklist; confirm all items pass

**Go standard:** Pass 6 of 7 tasks. IPR product meets all checklist items. Data-as-of timestamp present on dashboard — absence automatically fails that task.

---

## What "Go" Looks Like

The data-as-of timestamp is a hard requirement — a dashboard without it automatically fails that task. Every commander-facing PM product must show when the data was last refreshed. No exceptions.

The Append mode pipeline is a common failure point. Verify after the first run that output mode is set to Append (not Overwrite) by running the pipeline a second time and confirming two records with distinct snapshot dates exist. If you configured Overwrite and ran twice, you have one record.

The Contour portfolio matrix sort is a tested behavior. The evaluator will expect RED items at the top. Configure sort by `overall_status` ascending before submitting.

---

## Tips From Previous Graduates

- Before building anything in Ontology Manager, sketch your data model on paper: what are the 4 Object Types, what properties does each need, which ones link to which. Five minutes of design prevents an hour of rework.
- The IMS pipeline's `DATEDIFF` function requires both date columns to be correctly typed as Date — not String. Excel IMS exports often have dates as text. Add a `CAST` step before `DATEDIFF`. Check column types before building the calculation.
- The obligation rate Quiver chart reference line is the quarterly target for the current date. Hardcoding "50%" works for Q2, but document the hardcoded value so the next builder knows to update it at Q3.
- The PM Dashboard Standards Checklist is not a box-check exercise. Walk through it with your product the evening before the evaluation. If you miss a checklist item, that task is No-Go — no partial credit.
- The Day 3 practice run is not optional prep — it is instruction. Trainees who treat it as optional and spend the time reviewing notes instead of building consistently underperform on the evaluation.

---

*USAREUR-AF Operational Data Team — UNCLASSIFIED*
*Syllabus TM-40D | Version 2.0 | March 2026*
