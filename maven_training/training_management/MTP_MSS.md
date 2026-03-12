# MISSION TRAINING PLAN (MTP)
## MAVEN SMART SYSTEM (MSS) — USAREUR-AF

**HEADQUARTERS, UNITED STATES ARMY EUROPE AND AFRICA**
Wiesbaden, Germany

2026

**AUTHORITY:** This MTP is issued under authority of the USAREUR-AF C2 Data and Analytics Office (C2DAO) and implements USAREUR-AF Command Training Guidance. It provides planning and evaluation guidance for commanders and training managers responsible for MSS training across the formation.

**DISTRIBUTION:** Approved for public release; distribution is unlimited.

---

## TABLE OF CONTENTS

1. [Purpose and Scope](#1-purpose-and-scope)
2. [Training Objectives by Level](#2-training-objectives-by-level)
3. [Individual Task List](#3-individual-task-list)
4. [Training Standards and Go/No-Go Criteria](#4-training-standards-and-gono-go-criteria)
5. [Blocks of Instruction — Time Requirements](#5-blocks-of-instruction--time-requirements)
6. [Training Schedule Templates](#6-training-schedule-templates)
7. [Resource Requirements](#7-resource-requirements)
8. [Instructor Requirements and Certification](#8-instructor-requirements-and-certification)
9. [Practical Exercise Designs](#9-practical-exercise-designs)
10. [Training Status Tracking](#10-training-status-tracking)
11. [Sustainment Training Requirements](#11-sustainment-training-requirements)
- Appendix A — Unit Training Status Matrix (Template)
- Appendix B — Individual Training Record (Template)
- Appendix C — Practical Exercise Scenarios by Level

---

## 1. PURPOSE AND SCOPE

### 1-1. Purpose

This Mission Training Plan (MTP) provides the USAREUR-AF unit commander and training manager with a structured framework to plan, resource, execute, and assess Maven Smart System (MSS) training across all personnel levels. It operationalizes the MSS training curriculum (TM-10 through TM-40 series) by defining tasks, conditions, standards, time requirements, and evaluation criteria.

### 1-2. Training Philosophy

MSS training is progressive and role-based. No Soldier, officer, or civilian should attend a higher-level course without completing prerequisites. A unit that attempts to bypass foundational training (TM-10) to accelerate to TM-30 produces personnel who can operate tools without understanding what they are doing — a data governance and analytical risk.

The MTP enforces the following principles:

| Principle | Implication |
|---|---|
| Prerequisites are not suggestions | Commanders must verify completion before assigning personnel to advanced levels |
| Role determines training level | Assign training based on actual job function, not desire or seniority |
| Practical exercise is the standard | Reading is preparation; the training is complete only when the task is performed |
| Sustainment is required | MSS proficiency degrades within 6 months without use or refresher training |

### 1-3. Training Levels Summary

| Level | Publication | Audience | Training Days | Prerequisite |
|---|---|---|---|---|
| TM-10 | Maven User | All personnel | 1 day | None |
| TM-20 | Builder | All staff | 2 days | TM-10 |
| TM-30 | Advanced Builder | Data-adjacent specialists | 3 days | TM-20 |
| TM-40A | ORSA | ORSA analysts | 4 days | TM-30 + quant background |
| TM-40B | AI Engineer | AI/ML specialists | 4 days | TM-30 + coding background |
| TM-40C | ML Engineer | MLEs | 4 days | TM-30 + coding background |
| TM-40D | Program Manager | PMs, G8/S8 | 2 days | TM-20 |
| TM-40E | Knowledge Manager | KMOs, 37F | 2 days | TM-20 |
| TM-40F | Software Engineer | SWEs | 4 days | TM-30 + coding background |

> **NOTE:** "Training days" reflects initial qualification training with instructor support. Self-paced completion using the TM alone may require more time. Refresher/sustainment training is shorter — see Section 11.

---

## 2. TRAINING OBJECTIVES BY LEVEL

### 2-1. TM-10 — Maven User Training Objectives

Upon completing TM-10 training and passing the practical exercise, the trainee will:

**Terminal Learning Objective (TLO):** Access, navigate, and consume data products on the Maven Smart System in support of operational requirements.

**Enabling Learning Objectives (ELOs):**

| ELO | Description | Evaluation Method |
|---|---|---|
| 10-01 | Log in to MSS via CAC-based authentication and navigate to unit projects | Practical: observer validates login and navigation |
| 10-02 | Locate and view a dataset in a Workshop application | Practical: open a designated application, filter to unit data |
| 10-03 | Execute an authorized Action in a Workshop application | Practical: submit a status update via designated Action |
| 10-04 | Use Contour to build a basic chart and filter | Practical: create a filtered bar chart from provided dataset |
| 10-05 | Use Quiver to explore an Object Type | Practical: navigate to assigned Object Type, apply filter, export view |
| 10-06 | Access and interact with an AIP Logic workflow or Agent interface | Practical: submit a query to designated AIP interface |
| 10-07 | Identify classification markings and state authorized export procedures | Written/verbal: answer 3 of 4 classification scenario questions correctly |
| 10-08 | Troubleshoot at least 2 common access issues using TM-10 procedures | Practical: diagnose a seeded access problem from the troubleshooting annex |

### 2-2. TM-20 — Builder Training Objectives

**TLO:** Build, configure, and publish Foundry data products on MSS using visual (no-code) platform tools.

| ELO | Description | Evaluation Method |
|---|---|---|
| 20-01 | Create a Foundry project with correct naming, markings, and folder structure | Practical: inspector validates against naming convention checklist |
| 20-02 | Build a Pipeline Builder pipeline that ingests and transforms a provided dataset | Practical: pipeline runs successfully; output schema validated |
| 20-03 | Create an Object Type and populate it via pipeline output | Practical: Object Type appears in Ontology Manager with correct properties |
| 20-04 | Create a Link Type connecting two Object Types | Practical: link is traversable in Quiver |
| 20-05 | Configure a basic Action that writes to an Object Type property | Practical: execute the Action and verify the property updated |
| 20-06 | Build and publish a Workshop application with at least one table, one filter, and one Action button | Practical: application accessible to designated test users; table and filter functional |
| 20-07 | Manage project access (grant Viewer role to a test user) | Practical: test user confirms Viewer access; cannot edit |
| 20-08 | Create a Foundry branch, make a change, and submit for promotion | Practical: branch created; change visible; promotion request submitted to data steward |

### 2-3. TM-30 — Advanced Builder Training Objectives

**TLO:** Design and build complex, multi-source data products on MSS using advanced platform capabilities in accordance with C2DAO governance standards.

| ELO | Description | Evaluation Method |
|---|---|---|
| 30-01 | Build a multi-page Workshop application with conditional logic and variable passing between pages | Practical: application behaves as designed across 3+ pages; evaluator tests 5 conditional scenarios |
| 30-02 | Build a Pipeline Builder pipeline with a multi-source join and computed aggregation | Practical: output dataset validated against known-answer dataset |
| 30-03 | Design an Ontology schema (Object Types, Link Types, Actions) for a provided scenario — documented in a written design | Design review: evaluated against 6-item design rubric (see Appendix C) |
| 30-04 | Conduct an advanced Contour analysis: pivot, calculated columns, and saved view | Practical: Contour workbook reproduces provided reference output |
| 30-05 | Build a multi-object Quiver dashboard with linked views | Practical: dashboard filters propagate across linked views; evaluated by observer |
| 30-06 | Configure an AIP Logic workflow (do not author — configure inputs/outputs/triggers) | Practical: workflow triggers correctly, routes output to designated dataset |
| 30-07 | Interpret a data lineage graph for a provided dataset | Verbal/written: correctly identify upstream sources, transforms, and downstream consumers |
| 30-08 | Complete the full C2DAO promotion workflow: branch, test, submit, receive approval | Practical: evaluator plays data steward role; trainee executes workflow end-to-end |

### 2-4. TM-40D — Program Manager Training Objectives

**TLO:** Design and operate program management data products on MSS that support commander decision-making for schedule, resource, and portfolio health.

| ELO | Description | Evaluation Method |
|---|---|---|
| 40D-01 | Design a program data architecture (4 Object Types) for a provided program scenario | Design review: evaluated against PM data model rubric |
| 40D-02 | Build a milestone tracking pipeline from a provided IMS spreadsheet | Practical: pipeline output validates against known-answer milestone set |
| 40D-03 | Build a Workshop milestone dashboard with RAG status and data-as-of timestamp | Practical: dashboard displays correct status; timestamp present |
| 40D-04 | Build a budget execution Quiver visualization showing obligation rate vs target | Practical: chart displays correctly with reference line at Q target |
| 40D-05 | Configure a snapshot pipeline in Append mode for historical trend analysis | Practical: run pipeline 2× and verify cumulative records |
| 40D-06 | Produce an IPR product from MSS meeting the PM Dashboard Standards Checklist | Product review: evaluated against Appendix A of TM-40D |

### 2-5. TM-40E — Knowledge Manager Training Objectives

**TLO:** Design and operate knowledge management systems on MSS that capture, organize, and deliver institutional knowledge in support of unit continuity and mission effectiveness.

| ELO | Description | Evaluation Method |
|---|---|---|
| 40E-01 | Design a knowledge ontology (5+ Object Types) for a provided unit KM scenario | Design review: evaluated against knowledge architecture checklist |
| 40E-02 | Configure a Workshop AAR submission form that writes to the AAR Object Type | Practical: submitter test confirms form writes correctly; validator confirms required fields enforced |
| 40E-03 | Configure a lessons-learned intake pipeline with tagging and distribution logic | Practical: pipeline run with provided test data; output reviewed for accuracy |
| 40E-04 | Configure an AIP Logic summarization workflow for document intake | Practical: workflow processes a provided document; output reviewed by SME |
| 40E-05 | Build a knowledge browser application with search, filter, and drill-down | Practical: evaluator submits 5 test queries; application returns correct results |
| 40E-06 | Build and demonstrate a PCS knowledge transfer package for a specific role | Product review: package contains complete documentation per TM-40E, Chapter 9 |

### 2-6. TM-40A — ORSA Training Objectives

**TLO:** Conduct operations research and systems analysis on MSS, producing quantitatively rigorous decision support products that meet commander and ORSA product standards.

| ELO | Description | Evaluation Method |
|---|---|---|
| 40A-01 | Configure a Code Workspace with required packages and verify Foundry dataset connectivity | Practical: workspace runs provided test script without errors |
| 40A-02 | Build and validate a regression model for a provided readiness dataset | Practical: model results reviewed against reference solution; validation statistics correct |
| 40A-03 | Build a time series forecast with documented assumptions and confidence bounds | Practical: forecast output reviewed; uncertainty quantification present |
| 40A-04 | Run a Monte Carlo simulation for a provided COA comparison scenario | Practical: output distribution and confidence intervals reviewed by ORSA evaluator |
| 40A-05 | Formulate and solve a linear programming resource allocation problem | Practical: LP solution reviewed; constraint formulation documented |
| 40A-06 | Produce a commander brief that includes point estimates with uncertainty bounds | Product review: brief reviewed against ORSA product standards checklist |

### 2-7. TM-40B — AI Engineer Training Objectives

**TLO:** Author, test, and deploy AI-enabled capabilities on MSS using AIP Logic, Agent Studio, and LLM integration patterns in compliance with USAREUR-AF AI safety requirements.

| ELO | Description | Evaluation Method |
|---|---|---|
| 40B-01 | Author an AIP Logic workflow with prompt engineering, conditional chain logic, and structured JSON output | Practical: workflow runs against provided dataset; output schema validates |
| 40B-02 | Configure and test an AIP Agent Studio agent with at least two tools and defined memory scope | Practical: agent responds correctly to 5 evaluator queries; tool calls logged |
| 40B-03 | Build an LLM integration pipeline with ontology grounding and retrieval-augmented generation (RAG) | Practical: pipeline retrieves correct ontology context; evaluator validates output grounding |
| 40B-04 | Implement human-in-the-loop checkpoints for all write-capable Actions in a workflow | Practical: evaluator confirms no Action executes without a visible review/confirm step |
| 40B-05 | Write Python transforms that extract and format Ontology data for AIP Logic context | Practical: transform output matches expected schema; runs without error in Code Workspace |
| 40B-06 | Complete the AIP Authorization Checklist (TM-40B, Appendix A) for a proposed workflow and identify any prohibited use case | Written review: evaluator scores checklist completion and prohibited-use identification |

### 2-8. TM-40C — Machine Learning Engineer Training Objectives

**TLO:** Build, evaluate, deploy, and govern machine learning models on MSS using Foundry Code Workspaces and MLOps tooling in compliance with USAREUR-AF model governance standards.

| ELO | Description | Evaluation Method |
|---|---|---|
| 40C-01 | Configure a Code Workspace with required packages, GPU allocation, and Foundry dataset connectivity | Practical: provided test script runs without errors; dataset connection confirmed |
| 40C-02 | Build a feature engineering pipeline for a provided Foundry dataset meeting documented feature standards | Practical: output dataset reviewed against feature specification; no null leakage |
| 40C-03 | Train and evaluate a supervised model meeting defined accuracy, precision/recall, and calibration thresholds | Practical: evaluation metrics reviewed by technical evaluator against provided acceptance criteria |
| 40C-04 | Deploy a trained model to a Foundry model serving endpoint and verify live inference | Practical: inference endpoint returns predictions for 10 provided test records; latency within spec |
| 40C-05 | Implement a model monitoring pipeline with drift detection and alert configuration | Practical: pipeline detects seeded drift event and routes alert correctly |
| 40C-06 | Complete a model governance document meeting USAREUR-AF model documentation standards | Product review: document reviewed against TM-40C governance checklist |

### 2-9. TM-40F — Software Engineer Training Objectives

**TLO:** Build, test, and deploy production-quality software applications and integrations on MSS using the OSDK, Platform SDK, TypeScript Functions on Objects, and Slate, following USAREUR-AF code review and deployment standards.

| ELO | Description | Evaluation Method |
|---|---|---|
| 40F-01 | Authenticate to the Foundry Ontology via OSDK and execute a paginated, filtered object query | Practical: query returns correct records; pagination handles >1 page; evaluator verifies |
| 40F-02 | Execute an Action via OSDK with full validation logic and structured error handling | Practical: valid Action executes correctly; invalid input triggers correct error response |
| 40F-03 | Build a TypeScript Function on Objects implementing a computed property | Practical: computed property returns correct values for 10 test objects; edge cases handled |
| 40F-04 | Write and test a TypeScript Action validator with at least 3 distinct validation conditions | Practical: evaluator tests 5 scenarios; validator passes/blocks correctly in all cases |
| 40F-05 | Build a Slate application integrated with the Foundry API displaying live ontology data | Practical: application renders correctly; data refreshes on state change; evaluator navigates |
| 40F-06 | Complete a C2DAO code review and deployment workflow for a provided OSDK application | Practical: PR created, review comments addressed, and deployment checklist completed end-to-end |

> **NOTE:** Developer track evaluations (TM-40B, 40C, 40F) require a qualified technical reviewer: a TM-40 certified instructor, C2DAO data engineer, or equivalent. Do not evaluate developer track ELOs using a non-technical observer.

---

## 3. INDIVIDUAL TASK LIST

### 3-1. TM-10 Tasks (All Personnel)

| Task ID | Task | Go Standard |
|---|---|---|
| MSS-10-T01 | Access MSS via CAC | Successfully authenticates; navigates to unit project |
| MSS-10-T02 | Navigate to a named dataset in Workshop | Locates dataset within 3 minutes without assistance |
| MSS-10-T03 | Execute an Action | Action executes without error; property updated |
| MSS-10-T04 | Filter a Workshop table and export the result | Filter applied; export completed; data correct |
| MSS-10-T05 | Identify the classification marking on a dataset | States marking correctly; states authorized export procedure |
| MSS-10-T06 | Submit a basic Contour chart | Chart displays correct data per provided parameters |
| MSS-10-T07 | Request access to a missing resource | Submits correct access request to unit MSS administrator |

### 3-2. TM-20 Tasks (Builder Track)

| Task ID | Task | Go Standard |
|---|---|---|
| MSS-20-T01 | Create a Foundry project per naming convention | Project created; naming matches convention; markings applied |
| MSS-20-T02 | Build a Pipeline Builder pipeline (single source → output) | Pipeline runs; output schema and row count validated |
| MSS-20-T03 | Create an Object Type with 5+ properties | Object Type visible in Ontology Manager; properties correctly typed |
| MSS-20-T04 | Build and test an Action | Action executes; writes correct value; audit log confirmed |
| MSS-20-T05 | Build a Workshop application (table + filter + Action) | Application published; filter works; Action accessible to Viewer |
| MSS-20-T06 | Manage project access roles | Viewer access confirmed; Editor cannot elevate to Owner |
| MSS-20-T07 | Execute a branching workflow | Branch created; change made; promotion requested |

### 3-3. TM-30 Tasks (Advanced Builder)

| Task ID | Task | Go Standard |
|---|---|---|
| MSS-30-T01 | Build a multi-page Workshop application | 3+ pages; conditional logic demonstrated; variable passing validated |
| MSS-30-T02 | Build a multi-source Pipeline Builder join | Join produces correct output; row counts validated |
| MSS-30-T03 | Document an Ontology design for a provided scenario | Design document covers all required elements; reviewed by instructor |
| MSS-30-T04 | Build a Contour workbook with pivot and calculated columns | Output matches reference; pivot correct |
| MSS-30-T05 | Build a multi-object Quiver dashboard | Linked views filter correctly; evaluated by observer |
| MSS-30-T06 | Manage the C2DAO promotion workflow | Workflow completed end-to-end with evaluator as data steward |

---

## 4. TRAINING STANDARDS AND GO/NO-GO CRITERIA

### 4-1. Go/No-Go Standard

| Training Level | Go Standard |
|---|---|
| TM-10 | Pass 6 of 7 individual tasks (MSS-10-T01 through T07); pass classification scenario questions (3 of 4) |
| TM-20 | Pass 6 of 7 individual tasks (MSS-20-T01 through T07); Pipeline Builder pipeline runs without error |
| TM-30 | Pass 5 of 6 individual tasks (MSS-30-T01 through T06); Ontology design document reviewed and approved |
| TM-40A | Pass 5 of 6 ELOs; ORSA product brief reviewed by a qualified ORSA evaluator |
| TM-40B/C/F | Pass developer track practical exercise evaluated by TM-40 certified technical reviewer |
| TM-40D | Pass 5 of 6 ELOs; IPR product meets all PM Dashboard Standards Checklist items |
| TM-40E | Pass 5 of 6 ELOs; PCS knowledge transfer package reviewed and approved by instructor |

### 4-2. No-Go Actions

A trainee who does not meet the Go standard:

1. Receives specific written feedback on which task(s) failed and what was deficient.
2. Is given a remediation assignment (specific TM section to review, specific procedure to practice).
3. Completes a re-evaluation on the failed task(s) within 5 duty days.
4. May not advance to the next TM level until the current level Go standard is met.

> **NOTE:** No-Go at TM-10 is a training management flag — most No-Go results at TM-10 indicate an access provisioning issue (CAC enrollment, account not created), not a training failure. Distinguish between access failures and competency failures. Fix access issues before assessing competency.

### 4-3. Evaluation Documentation

Training evaluations are documented in the Unit Training Status Matrix (Appendix A). At minimum, record:
- Trainee name and unit
- TM level evaluated
- Date of evaluation
- Go/No-Go result
- Evaluator name and TM certification level
- Re-evaluation date if applicable

---

## 5. BLOCKS OF INSTRUCTION — TIME REQUIREMENTS

### 5-1. TM-10 — 1 Training Day (8 hours)

| Block | Time | Content | Method |
|---|---|---|---|
| 1 | 0800–0900 | MSS overview, data literacy fundamentals (Data Literacy Technical Reference Ch 1 summary) | Lecture/discussion |
| 2 | 0900–1000 | MSS login, navigation, project access | Instructor-led lab |
| 3 | 1000–1100 | Workshop applications: consuming data, tables, filters | Instructor-led lab |
| 4 | 1100–1200 | Actions: executing status updates and form submissions | Instructor-led lab |
| — | 1200–1300 | Lunch break | — |
| 5 | 1300–1400 | Contour: basic chart and filter | Guided practice |
| 6 | 1400–1500 | Quiver: exploring Object Types | Guided practice |
| 7 | 1500–1530 | AIP interface overview and demonstration | Demonstration |
| 8 | 1530–1600 | Classification markings and export procedures | Lecture/scenario |
| 9 | 1600–1700 | Practical exercise (individual, all tasks) | Evaluation |

### 5-2. TM-20 — 2 Training Days (16 hours)

**Day 1 — Project and Pipeline Fundamentals**

| Block | Time | Content | Method |
|---|---|---|---|
| 1 | 0800–0900 | TM-20 overview; Foundry project structure and naming conventions | Lecture |
| 2 | 0900–1100 | Project creation: naming, markings, folder structure | Instructor-led lab |
| 3 | 1100–1200 | Pipeline Builder: single-source ingestion and transformation | Instructor-led lab |
| — | 1200–1300 | Lunch | — |
| 4 | 1300–1500 | Pipeline Builder: filters, calculated columns, rename, output | Guided practice |
| 5 | 1500–1700 | Ontology Manager: Object Types, Link Types, basic Actions | Instructor-led lab |

**Day 2 — Workshop and Governance**

| Block | Time | Content | Method |
|---|---|---|---|
| 6 | 0800–1000 | Workshop: building applications (table, filter, metric widgets) | Instructor-led lab |
| 7 | 1000–1100 | Workshop: publishing, access control, viewer vs editor | Instructor-led lab |
| 8 | 1100–1200 | Workshop: Action buttons in applications | Guided practice |
| — | 1200–1300 | Lunch | — |
| 9 | 1300–1400 | Foundry branching: create, modify, submit for promotion | Instructor-led lab |
| 10 | 1400–1500 | Naming conventions, data stewardship, C2DAO standards review | Lecture/discussion |
| 11 | 1500–1700 | Practical exercise (all TM-20 tasks) | Evaluation |

### 5-3. TM-30 — 3 Training Days (24 hours)

**Day 1 — Advanced Workshop**

| Block | Time | Content | Method |
|---|---|---|---|
| 1 | 0800–1200 | Multi-page Workshop applications, conditional logic, variable passing | Instructor-led lab |
| — | 1200–1300 | Lunch | — |
| 2 | 1300–1700 | Workshop design exercise: design and build a 3-page application from scenario | Guided practice |

**Day 2 — Advanced Pipelines and Ontology Design**

| Block | Time | Content | Method |
|---|---|---|---|
| 3 | 0800–1100 | Pipeline Builder: multi-source joins, aggregations, advanced transforms | Instructor-led lab |
| — | 1100–1200 | Break | — |
| 4 | 1200–1300 | Ontology design methodology: from requirements to schema | Lecture/design exercise |
| — | 1300–1400 | Lunch | — |
| 5 | 1400–1700 | Ontology design workshop: trainee designs schema for provided scenario | Guided practice |

**Day 3 — Analytics and Governance**

| Block | Time | Content | Method |
|---|---|---|---|
| 6 | 0800–1000 | Contour: pivots, calculated columns, saved views | Instructor-led lab |
| 7 | 1000–1200 | Quiver: multi-object analysis, linked views | Instructor-led lab |
| — | 1200–1300 | Lunch | — |
| 8 | 1300–1400 | AIP Logic configuration (not authoring); data lineage review | Guided demonstration |
| 9 | 1400–1500 | C2DAO governance: promotion workflow, data stewardship review | Lecture/discussion |
| 10 | 1500–1700 | Practical exercise (all TM-30 tasks) | Evaluation |

### 5-4. TM-40D — Program Manager (2 Days)

**Day 1 — Data Architecture and Ingestion**

| Block | Time | Content | Method |
|---|---|---|---|
| 1 | 0800–0900 | PM role on MSS; program data model (Program/Milestone/Resource/Risk Object Types) | Lecture/discussion |
| 2 | 0900–1100 | Ontology: creating PM Object Types, Link Types, and properties | Instructor-led lab |
| 3 | 1100–1200 | Pipeline Builder: IMS ingestion, date arithmetic, RAG status computation | Instructor-led lab |
| — | 1200–1300 | Lunch | — |
| 4 | 1300–1500 | Pipeline Builder: GFEBS obligation data ingestion; Append mode snapshot pipeline | Instructor-led lab |
| 5 | 1500–1700 | Quiver: obligation rate visualization; budget execution charts with reference lines | Guided practice |

**Day 2 — Dashboards, Portfolio, and Governance**

| Block | Time | Content | Method |
|---|---|---|---|
| 6 | 0800–1000 | Workshop: milestone dashboard, RAG status formatting, data-as-of timestamp | Instructor-led lab |
| 7 | 1000–1200 | Contour: portfolio health matrix; cross-program status roll-up | Instructor-led lab |
| — | 1200–1300 | Lunch | — |
| 8 | 1300–1400 | Reporting pipelines: scheduled refresh, failure alerting, PDF export | Guided demonstration |
| 9 | 1400–1500 | Access management, classification, C2DAO governance for PM applications | Lecture/discussion |
| 10 | 1500–1700 | Practical exercise | Evaluation |

### 5-5. TM-40E — Knowledge Manager (2 Days)

**Day 1 — Knowledge Architecture, AAR Systems, Lessons Learned**

| Block | Time | Content | Method |
|---|---|---|---|
| 1 | 0800–0900 | KM role on MSS; knowledge architecture design methodology; domain analysis | Lecture/discussion |
| 2 | 0900–1100 | Ontology: Knowledge Object Types (Document, Lesson, AAR, SOP, ExpertiseProfile) | Instructor-led lab |
| 3 | 1100–1200 | Workshop: AAR submission form design, required field validation | Instructor-led lab |
| — | 1200–1300 | Lunch | — |
| 4 | 1300–1500 | Lessons learned pipeline: intake, deduplication, tagging, distribution routing | Instructor-led lab |
| 5 | 1500–1700 | AIP Logic: document summarization and automatic tagging configuration; SME review requirement | Guided lab |

**Day 2 — Search, Doctrine, Expertise, and Continuity**

| Block | Time | Content | Method |
|---|---|---|---|
| 6 | 0800–1000 | Workshop: knowledge browser application with search, filter, and drill-down | Instructor-led lab |
| 7 | 1000–1100 | SOP/doctrine version control: lifecycle management, review notification workflow | Instructor-led lab |
| 8 | 1100–1200 | Personnel expertise mapping: ExpertiseProfile, SME directory, expertise gap analysis | Guided practice |
| — | 1200–1300 | Lunch | — |
| 9 | 1300–1400 | PCS knowledge transfer package design; knowledge health metrics | Lecture/workshop |
| 10 | 1400–1500 | Access control, Privacy Act considerations, C2DAO governance for KM systems | Lecture/discussion |
| 11 | 1500–1700 | Practical exercise | Evaluation |

### 5-6. TM-40A — ORSA (4 Days)

**Day 1 — Environment Setup and Statistical Modeling**

| Block | Time | Content | Method |
|---|---|---|---|
| 1 | 0800–0900 | ORSA role; analytical product standards; Code Workspace orientation | Lecture/discussion |
| 2 | 0900–1100 | Code Workspace setup: Python/R environment, packages, Foundry dataset connectivity | Instructor-led lab |
| 3 | 1100–1200 | Regression: linear and logistic regression for readiness forecasting | Instructor-led lab |
| — | 1200–1300 | Lunch | — |
| 4 | 1300–1500 | Classification models: feature selection, training, validation statistics | Instructor-led lab |
| 5 | 1500–1700 | Model validation standards; documenting assumptions; writing outputs to Foundry datasets | Guided practice |

**Day 2 — Time Series and Monte Carlo**

| Block | Time | Content | Method |
|---|---|---|---|
| 6 | 0800–1000 | Time series: stationarity, ACF/PACF, ARIMA setup for readiness trend forecasting | Instructor-led lab |
| 7 | 1000–1200 | ARIMA/SARIMA forecast build: readiness trends and logistics demand signals | Guided practice |
| — | 1200–1300 | Lunch | — |
| 8 | 1300–1500 | Monte Carlo simulation: COA comparison under uncertainty; distribution selection | Instructor-led lab |
| 9 | 1500–1700 | Sensitivity analysis; logistics planning risk (Class IX stockage level modeling) | Guided practice |

**Day 3 — Optimization and Wargame Analysis**

| Block | Time | Content | Method |
|---|---|---|---|
| 10 | 0800–1100 | Linear programming: resource allocation formulation, constraint setup, scipy/lpSolve | Instructor-led lab |
| 11 | 1100–1200 | Scheduling optimization: maintenance window scheduling against operational constraints | Guided practice |
| — | 1200–1300 | Lunch | — |
| 12 | 1300–1500 | Wargame/exercise data architecture: collection templates, aggregation pipelines | Instructor-led lab |
| 13 | 1500–1700 | Post-exercise analysis: AAR aggregation pipeline, outcome measurement | Guided practice |

**Day 4 — Decision Support and Commander Brief**

| Block | Time | Content | Method |
|---|---|---|---|
| 14 | 0800–1000 | Quiver/Contour for ORSA: readiness forecast dashboard, COA comparison visualization | Instructor-led lab |
| 15 | 1000–1200 | Communicating uncertainty: confidence intervals, prediction intervals, briefing posture | Lecture/scenario |
| — | 1200–1300 | Lunch | — |
| 16 | 1300–1700 | Practical exercise: build regression + forecast + commander brief from provided dataset | Evaluation |

### 5-7. TM-40B — AI Engineer (4 Days)

**Day 1 — Safety, Architecture, and AIP Logic Fundamentals** *(AI safety module mandatory)*

| Block | Time | Content | Method |
|---|---|---|---|
| 1 | 0800–1000 | AI safety: human-in-the-loop requirements, OPSEC for AI, prohibited use cases (Appendix B) | Lecture — mandatory, no skip |
| 2 | 1000–1200 | AIP platform architecture: AIP Logic, Agent Studio, Code Workspaces, LLM endpoints | Lecture/discussion |
| — | 1200–1300 | Lunch | — |
| 3 | 1300–1500 | AIP Logic: authoring first workflow, prompt templates, input/output configuration | Instructor-led lab |
| 4 | 1500–1700 | AIP Logic: conditional chains, error handling, structured JSON output | Guided practice |

**Day 2 — Advanced AIP Logic and Python Transforms**

| Block | Time | Content | Method |
|---|---|---|---|
| 5 | 0800–1000 | AIP Logic: multi-step chains, looping, action integration | Instructor-led lab |
| 6 | 1000–1200 | Python transforms for AIP: extracting and formatting Ontology data for LLM context | Instructor-led lab |
| — | 1200–1300 | Lunch | — |
| 7 | 1300–1500 | LLM integration patterns: context construction, grounding, RAG architecture | Lecture/lab |
| 8 | 1500–1700 | Ontology integration: connecting AIP Logic outputs to Object properties via Actions | Guided practice |

**Day 3 — Agent Studio and Evaluation**

| Block | Time | Content | Method |
|---|---|---|---|
| 9 | 0800–1100 | Agent Studio: agent architecture, tool configuration, memory, orchestration | Instructor-led lab |
| 10 | 1100–1200 | Testing AI outputs: red-teaming, adversarial prompts, evaluation frameworks | Lecture/exercise |
| — | 1200–1300 | Lunch | — |
| 11 | 1300–1500 | AI Output Validation Framework (Appendix C): applying to a workflow | Guided practice |
| 12 | 1500–1700 | AIP Authorization Checklist (Appendix A): working through a full authorization | Workshop |

**Day 4 — Production Deployment and Practical Exercise**

| Block | Time | Content | Method |
|---|---|---|---|
| 13 | 0800–1000 | Production deployment: pipeline scheduling, monitoring, rollback procedures | Lecture/demo |
| 14 | 1000–1200 | Practical exercise preparation: review scenario, plan design | Individual prep |
| — | 1200–1300 | Lunch | — |
| 15 | 1300–1700 | Practical exercise: author, test, and document an AIP Logic workflow end-to-end | Evaluation |

### 5-8. TM-40C — Machine Learning Engineer (4 Days)

**Day 1 — Workspace and Feature Engineering**

| Block | Time | Content | Method |
|---|---|---|---|
| 1 | 0800–0900 | MLE role on MSS; model governance overview; Code Workspace orientation | Lecture |
| 2 | 0900–1100 | Code Workspace setup: GPU allocation, package management, Foundry dataset connectivity | Instructor-led lab |
| 3 | 1100–1200 | Feature engineering fundamentals: null handling, encoding, scaling, leakage prevention | Lecture/lab |
| — | 1200–1300 | Lunch | — |
| 4 | 1300–1700 | Feature engineering pipeline build: Foundry dataset → feature matrix | Instructor-led lab |

**Day 2 — Model Training and Evaluation**

| Block | Time | Content | Method |
|---|---|---|---|
| 5 | 0800–1100 | Model training: scikit-learn / PyTorch patterns, cross-validation, hyperparameter tuning | Instructor-led lab |
| 6 | 1100–1200 | Evaluation: accuracy, precision/recall, calibration, ROC-AUC; acceptance thresholds | Lecture/lab |
| — | 1200–1300 | Lunch | — |
| 7 | 1300–1700 | Model evaluation exercise: evaluate 2 competing models against acceptance criteria; select and document | Guided practice |

**Day 3 — Deployment and MLOps**

| Block | Time | Content | Method |
|---|---|---|---|
| 8 | 0800–1000 | Model deployment: serving endpoints, inference API, integration with Ontology Actions | Instructor-led lab |
| 9 | 1000–1200 | MLOps on Foundry: experiment tracking, model registry, versioning | Instructor-led lab |
| — | 1200–1300 | Lunch | — |
| 10 | 1300–1500 | Monitoring: drift detection, data quality alerts, retraining triggers | Instructor-led lab |
| 11 | 1500–1700 | Operational use cases: readiness prediction, logistics demand, anomaly detection patterns | Lecture/case study |

**Day 4 — Governance and Practical Exercise**

| Block | Time | Content | Method |
|---|---|---|---|
| 12 | 0800–1000 | Model governance: documentation standards, model cards, responsible AI requirements | Lecture/workshop |
| 13 | 1000–1200 | Practical exercise preparation: review scenario, plan pipeline | Individual prep |
| — | 1200–1300 | Lunch | — |
| 14 | 1300–1700 | Practical exercise: feature pipeline → train → evaluate → deploy → governance doc | Evaluation |

### 5-9. TM-40F — Software Engineer (4 Days)

**Day 1 — OSDK Fundamentals**

| Block | Time | Content | Method |
|---|---|---|---|
| 1 | 0800–0900 | SWE role on MSS; USAREUR-AF 5-layer data stack; code review standards overview | Lecture |
| 2 | 0900–1100 | OSDK setup: authentication, client initialization, first object query | Instructor-led lab |
| 3 | 1100–1200 | OSDK: filtering, sorting, pagination, and ResourceIterator patterns | Instructor-led lab |
| — | 1200–1300 | Lunch | — |
| 4 | 1300–1500 | OSDK: Link traversal; querying related objects | Instructor-led lab |
| 5 | 1500–1700 | OSDK: Action execution; error handling and retry patterns | Guided practice |

**Day 2 — OSDK Advanced and Platform SDK**

| Block | Time | Content | Method |
|---|---|---|---|
| 6 | 0800–1000 | OSDK: Object subscriptions (real-time change notifications); bulk operations | Instructor-led lab |
| 7 | 1000–1200 | Platform SDK: dataset read/write transactions, file resources, branch management | Instructor-led lab |
| — | 1200–1300 | Lunch | — |
| 8 | 1300–1700 | Platform SDK exercise: build a dataset pipeline integration using Platform SDK | Guided practice |

**Day 3 — TypeScript Functions, Action Validators, and Slate**

| Block | Time | Content | Method |
|---|---|---|---|
| 9 | 0800–1000 | TypeScript Functions on Objects: structure, computed properties, bulk query patterns | Instructor-led lab |
| 10 | 1000–1200 | FOO testing patterns; performance considerations | Guided practice |
| — | 1200–1300 | Lunch | — |
| 11 | 1300–1500 | TypeScript Action validators: multi-condition logic, error messages, testing | Instructor-led lab |
| 12 | 1500–1700 | Slate applications: structure, Foundry API integration, widget binding | Instructor-led lab |

**Day 4 — CI/CD, Security, and Practical Exercise**

| Block | Time | Content | Method |
|---|---|---|---|
| 13 | 0800–1000 | CI/CD: code repository discipline, PR workflow, C2DAO deployment checklist | Lecture/demo |
| 14 | 1000–1200 | Security and compliance: OSDK token handling, input sanitization, OPSEC for app code | Lecture/lab |
| — | 1200–1300 | Lunch | — |
| 15 | 1300–1700 | Practical exercise: build OSDK query → Action validator → Slate UI end-to-end | Evaluation |

---

## 6. TRAINING SCHEDULE TEMPLATES

### 6-1. Individual Integration Training Schedule (New Arrival)

For a Soldier joining the unit and requiring rapid MSS integration:

**Week 1 — Foundation**

| Day | Training | Location | Access Requirement |
|---|---|---|---|
| Mon | TM-10 (full day) | MSS training environment | Basic MSS account (provisioned before arrival) |
| Tue | Supervised practice: unit's operational MSS environment | G6 / data team desk | Read-only access to unit projects |
| Wed | TM-20 Day 1 (if builder role) OR continuation practice | Training environment | Builder access provisioned |
| Thu | TM-20 Day 2 + evaluation | Training environment | Builder access |
| Fri | Review evaluation feedback; remediation if needed | — | — |

**Week 2–3 — Specialized Track (if applicable)**

Continue with TM-30 or TM-40 track based on role. No more than one TM level per week for initial qualification.

### 6-2. Unit-Wide Training Event (S6 Shop or Data Team)

For standing up an entire element's MSS capability over 2 weeks:

**Week 1**

| Day | Training | Audience |
|---|---|---|
| Mon | Commander brief: Data Literacy for Senior Leaders summary (2 hrs); Unit data strategy overview | All O-5+, S6 leadership |
| Tue | TM-10 (all staff) | All personnel |
| Wed | TM-10 Evaluation (morning); TM-20 Day 1 (designated builders, afternoon) | Split: all / builders |
| Thu | TM-20 Day 2 | Designated builders |
| Fri | TM-20 Evaluation; TM-30 orientation brief | Builders |

**Week 2**

| Day | Training | Audience |
|---|---|---|
| Mon | TM-30 Day 1 | Data-adjacent specialists |
| Tue | TM-30 Day 2 | Data-adjacent specialists |
| Wed | TM-30 Day 3 + Evaluation | Data-adjacent specialists |
| Thu | TM-40D (PM) Day 1 | G8/S8, PMs |
| Fri | TM-40D Day 2 + Evaluation; Schedule TM-40A/B/C/E/F for specialists | PMs + specialists |

---

## 7. RESOURCE REQUIREMENTS

### 7-1. Access Requirements by Training Level

| Training Level | Access Required | Who Provisions | Lead Time |
|---|---|---|---|
| TM-10 | Standard MSS user account (Viewer in training project) | Unit MSS Administrator | 3–5 duty days |
| TM-20 | Builder access in training project | Unit MSS Administrator | 3–5 duty days |
| TM-30 | Editor access; AIP Logic configuration access | Unit MSS Administrator + C2DAO | 5–7 duty days |
| TM-40A | Code Workspace provisioning (Python/R) | C2DAO | 7–10 duty days |
| TM-40B | AIP Logic authoring access; Agent Studio access | C2DAO | 7–10 duty days |
| TM-40C | Code Workspace with GPU; model registry access | C2DAO | 10+ duty days |
| TM-40D | Builder access + GFEBS training data export | Unit MSS Admin + G8 | 5–7 duty days |
| TM-40E | Builder access + AIP Logic configuration | Unit MSS Admin + C2DAO | 5–7 duty days |
| TM-40F | OSDK developer access; TypeScript environment | C2DAO | 10+ duty days |

> **CAUTION: Access provisioning is on the critical path for all MSS training. Request access a minimum of 5 duty days before the training start date. Training events that begin without provisioned access will fail. The training officer owns the access request timeline — do not assume it will be done automatically.**

### 7-2. Training Environment Requirements

All MSS training should be conducted in the **USAREUR-AF MSS Training Environment**, not in the production environment. The training environment contains:
- Synthetic datasets representative of unit operational data (non-sensitive)
- Pre-configured training projects at each TM level
- Seeded Object Types and pipelines for exercise use
- Test user accounts for access control exercises

If the training environment is unavailable, coordinate with C2DAO for an approved production environment substitute with restricted permissions.

### 7-3. Instructor Hardware Requirements

| Requirement | Standard |
|---|---|
| Instructor workstation | Laptop with CAC reader, MSS access, projector output |
| Projector / large display | Minimum 80" display or projector visible to all trainees |
| Network | Unclassified network with access to USAREUR-AF MSS (confirm connectivity before training day) |
| Trainee workstations | One per trainee; CAC-capable; network access to MSS |
| Backup | Instructor has a pre-recorded demo video for each major task in case of MSS outage |

---

## 8. INSTRUCTOR REQUIREMENTS AND CERTIFICATION

### 8-1. Instructor Qualification Standards

| TM Level | Instructor Requirement |
|---|---|
| TM-10 | TM-20 certified or higher; completed TM-10 evaluation as a trainee |
| TM-20 | TM-30 certified or higher |
| TM-30 | TM-40 certified in any track; or C2DAO-certified data engineer |
| TM-40A (ORSA) | Active-duty ORSA (FA49) with Code Workspace proficiency OR C2DAO-approved contractor |
| TM-40B (AI Eng) | C2DAO AI engineer or TM-40B certified individual |
| TM-40C (MLE) | C2DAO ML engineer or TM-40C certified individual |
| TM-40D (PM) | TM-40D certified individual with PM/resource management background |
| TM-40E (KM) | TM-40E certified individual with KM background (37F or equivalent) |
| TM-40F (SWE) | C2DAO software engineer or TM-40F certified individual with TypeScript/Python proficiency |

### 8-2. Instructor Certification Process

To become a certified MSS instructor at any level:

1. Complete the TM for the level you will instruct, plus one level above (or a TM-40 track for TM-30 instructors).
2. Pass the practical evaluation for the target level.
3. Co-instruct one full training event at the target level, observed by a C2DAO data engineer or existing certified instructor.
4. Receive written certification from the C2DAO.
5. Renew certification annually by completing a TM-level practical exercise review.

### 8-3. Instructor-to-Trainee Ratios

| TM Level | Maximum Trainee-to-Instructor Ratio |
|---|---|
| TM-10 | 20:1 (lecture portions); 10:1 (lab portions) |
| TM-20 | 10:1 (all portions) |
| TM-30 | 8:1 (all portions) |
| TM-40A/B/C/F | 5:1 (intensive coding/modeling content) |
| TM-40D/E | 10:1 (all portions) |

---

## 9. PRACTICAL EXERCISE DESIGNS

### 9-1. TM-10 Practical Exercise — "Unit SITREP Access"

**Scenario:** You are a Soldier assigned to [Unit] S3. Your unit uses MSS to track SITREP submissions from subordinate elements. You need to access the SITREP dashboard, check for missing submissions, and submit a correction to a status field.

**Tasks to complete (evaluated by instructor observer):**
1. Log in to MSS using your CAC.
2. Navigate to the `[UNIT]-S3-SITREP-Tracker` application.
3. Filter the table to show only submissions from the last 7 days.
4. Identify which element has not submitted for today.
5. Execute the "Submit SITREP Update" Action to correct a seeded status error.
6. Export the filtered table to CSV.
7. State the classification marking of the dataset and the authorized distribution list for exports.

**Go standard:** All 7 tasks completed; classification question answered correctly.

### 9-2. TM-20 Practical Exercise — "Build a Unit Readiness Tracker"

**Scenario:** Your S4 officer needs a simple equipment readiness tracker. You have received an Excel spreadsheet with equipment identifiers, assigned units, and current C-ratings. You must ingest this data into MSS and build a dashboard.

**Tasks to complete:**
1. Create a Foundry project named per unit convention.
2. Upload the provided Excel file and build a Pipeline Builder pipeline that cleans and outputs a validated dataset.
3. Create an `Equipment` Object Type with: `equipment_id`, `unit`, `c_rating`, `last_updated` properties.
4. Configure the pipeline to write Equipment objects.
5. Create an `Action` that allows an authorized user to update `c_rating`.
6. Build a Workshop application with: a table of all equipment, a filter by `unit` and `c_rating`, and the Update Action button.
7. Grant a test user Viewer access; verify they cannot edit.
8. Create a branch, change the application title, and submit for promotion.

**Go standard:** All 8 tasks completed without instructor assistance; pipeline runs without error; application is accessible and functional.

### 9-3. TM-30 Practical Exercise — "Multi-Source Operations Dashboard"

**Scenario:** The S3 requires a dashboard that combines personnel readiness data (from one dataset) and equipment readiness data (from a second dataset) at the unit level, with a filter for battalion and a drill-down to individual unit status.

**Tasks to complete:**
1. Build a Pipeline Builder pipeline that joins the two provided datasets on `unit_id` and computes an overall readiness score per unit.
2. Design (document) the Ontology schema for a `Unit` Object Type and a `ReadinessReport` Object Type with appropriate links.
3. Build a multi-page Workshop application: Page 1 = portfolio view (all units), Page 2 = unit detail (linked from Page 1), Page 3 = historical trend (if time-series data available).
4. Build a Contour workbook showing readiness by battalion with a calculated column for deviation from standard.
5. Submit the pipeline and application for promotion through the C2DAO workflow.

**Evaluator rubric:** (See Appendix C for full rubric)

---

## 10. TRAINING STATUS TRACKING

### 10-1. Unit Training Status Matrix

The Unit Training Status Matrix (Appendix A) is the primary tool for the training manager to track MSS training completion across the unit. It is maintained by the unit MSS Administrator or designated training NCO and reviewed monthly.

**Minimum data elements per Soldier/civilian:**

| Field | Description |
|---|---|
| Name | Last, First MI |
| Rank/Grade | E/O/W/GS grade |
| MOS/Position | Assigned role |
| TM-10 Date | Date of Go evaluation (or N/A if not yet completed) |
| TM-20 Date | Date of Go evaluation |
| TM-30 Date | Date of Go evaluation |
| TM-40 Track | Applicable track(s) |
| TM-40 Date | Date of Go evaluation |
| Refresher Due | Date of next sustainment evaluation |
| Notes | Remediation status, access issues, special certifications |

### 10-2. Unit Training Status Report (UTSR)

The UTSR is a monthly one-pager submitted to the C2DAO summarizing unit MSS training status. Format:

```
UNIT MSS TRAINING STATUS REPORT
Unit: [Unit Designation]          Date: [YYYYMMDD]
Reporting Officer: [Name, Rank]   Contact: [Email]

PERSONNEL SUMMARY:
  Total personnel requiring TM-10: [#]     TM-10 Complete: [#] ([%])
  Total personnel requiring TM-20: [#]     TM-20 Complete: [#] ([%])
  Total personnel requiring TM-30: [#]     TM-30 Complete: [#] ([%])
  Total TM-40 track assignments:  [#]     TM-40 Complete: [#] ([%])

ISSUES / SHORTFALLS:
  Access provisioning delays: [Y/N — if yes, describe]
  Personnel awaiting remediation: [#]
  Instructor availability: [adequate / insufficient]

NEXT TRAINING EVENT: [Date, Level, # of trainees]
```

---

## 11. SUSTAINMENT TRAINING REQUIREMENTS

### 11-1. Sustainment Standards

MSS proficiency degrades without regular use. Personnel who do not actively use MSS in their duties require periodic sustainment evaluation.

| Condition | Sustainment Requirement |
|---|---|
| Active daily MSS user | No formal sustainment required; supervisory spot-check quarterly |
| Occasional user (weekly to monthly) | Practical task evaluation every 12 months |
| Infrequent user (<monthly) | Practical task evaluation every 6 months |
| MSS access not used in 6+ months | Re-evaluate at current TM level before resuming independent work |
| PCS arrival with prior MSS training | Re-evaluate TM-10 (access/navigation may differ by theater); waive with supervisor verification |

### 11-2. Sustainment Event Design

A sustainment event does not require a full-day class. Design sustainment as a practical task check:

**TM-10 Sustainment (1 hour):** Complete a single task scenario from the TM-10 practical exercise bank (Appendix C). Evaluated by immediate supervisor or unit MSS Administrator.

**TM-20/30 Sustainment (2–3 hours):** Complete one of the following: build a new pipeline in a test project, modify an existing Workshop application, or complete a branch/promote workflow. Evaluated by a TM-30+ certified individual.

**TM-40 Sustainment (4 hours):** Complete a representative task from the relevant TM-40 track. TM-40D/E sustainment can include producing a real unit product (PM dashboard update, AAR pipeline run) observed by a supervisor.

### 11-3. Access Deactivation Policy

Personnel who have not accessed MSS in 90 days will have their access reviewed by the unit MSS Administrator. Access will be deactivated at 180 days of inactivity per USAREUR-AF access management policy. Reactivation requires:
1. Supervisor endorsement of continued need
2. Completion of TM-10 practical re-evaluation
3. MSS Administrator re-provisioning

---

## APPENDIX A — UNIT TRAINING STATUS MATRIX (TEMPLATE)

```
UNIT MSS TRAINING STATUS MATRIX
Unit: _______________________     As of: ___________
Maintained by: _______________     Reviewed: ________

NAME          | RANK | MOS  | TM-10  | TM-20  | TM-30  | TM-40  | REFRESH
              |      |      | DATE   | DATE   | DATE   | TRK/DT | DUE
--------------+------+------+--------+--------+--------+--------+--------
              |      |      |        |        |        |        |
              |      |      |        |        |        |        |
              |      |      |        |        |        |        |

STATUS CODES: C = Complete (Go)  I = In Progress  N = Not Started
              R = Remediation    W = Waived (supervisor verification)
```

---

## APPENDIX B — INDIVIDUAL TRAINING RECORD (TEMPLATE)

```
MSS INDIVIDUAL TRAINING RECORD

Name: ____________________  Rank/Grade: _______  MOS/Position: __________
Unit: ____________________  Email: ________________________________

TM-10 EVALUATION
  Date: __________  Evaluator: ________________  Result: GO / NO-GO
  Tasks Failed (if any): _________________________________________
  Re-evaluation Date (if applicable): _____________  Result: ________

TM-20 EVALUATION
  Date: __________  Evaluator: ________________  Result: GO / NO-GO
  Tasks Failed: __________________________________________________
  Re-evaluation: _________________________________________________

TM-30 EVALUATION
  Date: __________  Evaluator: ________________  Result: GO / NO-GO
  Tasks Failed: __________________________________________________
  Re-evaluation: _________________________________________________

TM-40 TRACK: _______
  Date: __________  Evaluator: ________________  Result: GO / NO-GO
  Tasks Failed: __________________________________________________
  Re-evaluation: _________________________________________________

SUSTAINMENT EVALUATIONS
  Date: ________  Level: _____  Result: GO / NO-GO  Evaluator: _________
  Date: ________  Level: _____  Result: GO / NO-GO  Evaluator: _________
  Date: ________  Level: _____  Result: GO / NO-GO  Evaluator: _________

INSTRUCTOR CERTIFICATIONS
  TM Level: _____  Certified: ________  Certifying Authority: ___________
  TM Level: _____  Certified: ________  Certifying Authority: ___________
```

---

## APPENDIX C — PRACTICAL EXERCISE SCENARIO BANK

### TM-10 Scenarios (Instructor selects one per evaluation)

**Scenario 10-A:** Access the `[Unit]-Readiness-Dashboard` application and identify which subordinate element has the lowest C-rating. Export the table filtered to that element. State the classification of the dataset.

**Scenario 10-B:** Navigate to the `[Unit]-SITREP-Tracker`. Submit a SITREP for today using the designated Action. Verify submission appears in the tracker table.

**Scenario 10-C:** Use Contour to build a bar chart showing count of personnel by rank from the provided personnel dataset. Apply a filter for a specific unit. Save the chart.

**Scenario 10-D:** You receive an error message when trying to access a dataset. Using TM-10 troubleshooting procedures, identify the likely cause (one of three seeded scenarios: wrong marking, no project access, dataset moved). State the correct resolution action.

### TM-20 Scenarios (Instructor selects one per evaluation)

**Scenario 20-A:** [Readiness Tracker — described in Section 9-2]

**Scenario 20-B:** Build a training schedule tracker. Given an Excel file with trainee name, TM level, date, and result, build a Pipeline Builder pipeline, create a TrainingRecord Object Type, configure an Update Status Action, and build a Workshop application showing training completion percentages by unit.

**Scenario 20-C:** Given a logistics dataset (equipment, location, status), build a Pipeline Builder pipeline that filters to RED status items and a Workshop application that displays them with a mark-resolved Action.

### TM-40D Scenarios (PM — Instructor selects one per evaluation)

**Scenario 40D-A:** You are the G8 data builder for a theater sustainment command program. Given a provided IMS spreadsheet (15 milestones) and a GFEBS obligation extract, build the full PM stack: Object Types, ingestion pipelines, milestone RAG dashboard, and obligation rate Quiver chart with a Q2 reference line. The application must display a data-as-of timestamp.

**Scenario 40D-B:** Your command has 6 programs across 3 battalions. Using provided synthetic program data, build a Contour portfolio health matrix showing schedule and resource status per program, sorted by overall health descending. Export as PDF formatted for a commander IPR.

**Scenario 40D-C:** An existing PM dashboard has no data-as-of date and uses hardcoded status values in the pipeline. Identify and fix both issues. Document the changes in the pipeline description fields and re-run to verify.

### TM-40E Scenarios (KM — Instructor selects one per evaluation)

**Scenario 40E-A:** Your brigade KMO needs an AAR capture system. Given requirements for a structured form (unit, date, event type, observations, discussion, recommendations), build the Object Type, Workshop submission form with required-field validation, and a knowledge browser showing submitted AARs filterable by unit and event type.

**Scenario 40E-B:** You have 30 unstructured after-action reports in PDF. Configure an AIP Logic summarization workflow that extracts structured lessons from each document, creates Draft Lesson objects, and routes them to a KM Review Queue Workshop application. Produce the AIP Authorization checklist for the workflow.

**Scenario 40E-C:** Design a PCS knowledge transfer package for an outgoing S3 operations sergeant who has been the unit MSS builder for 18 months. Using TM-40E Chapter 9 procedures, produce the complete transfer package: key person dependency analysis, knowledge transfer artifacts list, and Foundry project handoff documentation.

### TM-40A Scenarios (ORSA — Evaluator selects one per evaluation)

**Scenario 40A-A:** Using a provided readiness dataset (12 months, C-ratings by battalion), build: (1) a linear regression to forecast C2-level probability at 6 months, (2) a time series forecast with 90% confidence intervals, (3) a commander brief showing the forecast with explicit uncertainty bounds. The brief must not present any point estimate without its confidence range.

**Scenario 40A-B:** Your G3 needs to compare two COAs for a logistics operation. COA 1 uses organic assets; COA 2 adds contracted support. Using provided demand and resource data, run a Monte Carlo simulation for each COA (1,000 trials minimum), produce a probability distribution for on-hand stock at D+30, and brief the comparison with risk characterization.

**Scenario 40A-C:** Given a provided maintenance schedule constraint problem (20 vehicles, 5 bay slots, maintenance windows, operational commitments), formulate and solve a linear program that maximizes vehicles available during a defined readiness window. Document all constraints and present the solution with an explanation the S4 can brief.

### TM-40B Scenarios (AI Engineer — Evaluator selects one per evaluation)

**Scenario 40B-A:** Build an AIP Logic workflow that accepts an unstructured SITREP submission (plain text), extracts structured fields (unit, date, activity, status, issues), maps them to a SITREP Object Type via an Action, and routes uncertain extractions to a human review queue. Complete the AIP Authorization Checklist.

**Scenario 40B-B:** Configure an Agent Studio agent that can answer natural language questions about unit readiness by querying the Readiness Object Type, aggregating by echelon, and returning results with source citations. The agent must refuse to answer questions outside its defined scope and must not take any write Actions without an explicit confirmation step.

### TM-40C Scenarios (ML Engineer — Evaluator selects one per evaluation)

**Scenario 40C-A:** Given a provided equipment failure dataset (equipment type, usage hours, maintenance history, failure binary label), build: feature engineering pipeline, binary classifier for failure prediction within 30 days, evaluation report against defined acceptance thresholds, and a deployed inference endpoint. Produce the model governance document.

**Scenario 40C-B:** An existing model is deployed and showing data drift (evaluator seeds drift into the monitoring dataset). Diagnose the drift using the monitoring pipeline, characterize the type of drift, and produce a written recommendation: retrain, adjust thresholds, or investigate data quality issue. Document the decision.

### TM-40F Scenarios (SWE — Evaluator selects one per evaluation)

**Scenario 40F-A:** Build a TypeScript application using OSDK that: (1) queries Unit objects filtered by readiness status, (2) paginates results into a Slate table view, (3) triggers a status update Action on user click with a confirmation modal, and (4) handles error states gracefully with user-visible error messages. Complete a C2DAO deployment checklist.

**Scenario 40F-B:** Given a provided Action that writes to a Personnel Object Type, write a TypeScript validator that enforces: required field presence, valid rank enumeration, date range validation (no future dates), and cross-field logic (if status = DEPLOYED, location must be non-null). Test with 8 provided test cases (4 valid, 4 invalid).

---

### TM-30 Scenario Design Rubric (Evaluator Reference)

Evaluate trainee designs against these 6 criteria:

| Criterion | Description | Weight |
|---|---|---|
| Completeness | Design covers all required Object Types and Link Types | 20% |
| Correctness | Properties are correctly typed; links are directionally correct | 20% |
| Normalization | No property redundancy; proper use of links vs. embedded data | 15% |
| Naming convention | Follows USAREUR-AF naming convention throughout | 15% |
| Governance | Access model defined; data steward identified | 15% |
| Feasibility | Design is buildable within TM-30 toolset | 15% |

**Go:** Score ≥ 75% with no zero-score on any criterion.

---

*USAREUR-AF Operational Data Team — UNCLASSIFIED*
*MTP-MSS | Version 1.0 | March 2026 | Initial publication*
