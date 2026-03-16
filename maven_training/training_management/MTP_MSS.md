# MISSION TRAINING PLAN (MTP)
## MAVEN SMART SYSTEM (MSS) — USAREUR-AF

**HEADQUARTERS, UNITED STATES ARMY EUROPE AND AFRICA**
Wiesbaden, Germany | 2026

**AUTHORITY:** Issued under authority of USAREUR-AF C2DAO; implements USAREUR-AF Command Training Guidance. Provides planning and evaluation guidance for commanders and training managers responsible for MSS training across the formation.

**DISTRIBUTION:** Distribution authorized to U.S. Government agencies and their contractors only. Other requests must be referred to Headquarters, USAREUR-AF, C2DAO, Wiesbaden, Germany.

---


## 1. PURPOSE AND SCOPE

### 1-1. Purpose

This MTP provides the USAREUR-AF unit commander and training manager a structured framework to plan, resource, execute, and assess Maven Smart System (MSS) training across all personnel levels. It operationalizes the MSS training curriculum (TM-10 through TM-40 series) by defining tasks, conditions, standards, time requirements, and evaluation criteria.

### 1-2. Training Philosophy

MSS training is progressive and role-based. Bypassing foundational training (TM-10) to accelerate to TM-30 produces personnel who can operate tools without understanding what they are doing — a data governance and analytical risk.

| Principle | Implication |
|---|---|
| Prerequisites are not suggestions | Commanders must verify completion before assigning personnel to advanced levels |
| Role determines training level | Assign based on actual job function, not desire or seniority |
| Practical exercise is the standard | Training is complete only when the task is performed to standard |
| Sustainment is required | MSS proficiency degrades within 6 months without use or refresher training |

### 1-3. Training Levels Summary

| Level | Publication | Audience | Days | Prerequisite |
|---|---|---|---|---|
| TM-10 | Maven User | All personnel | 1 | None |
| TM-20 | Builder | All staff | 5 | TM-10 |
| TM-30 | Advanced Builder | Data-adjacent specialists | 5 | TM-20 |
| TM-40A | Intelligence WFF | G2/S2 Intel staff | 3 | TM-30 (Required) |
| TM-40B | Fires WFF | Fires/FSCOORD staff | 3 | TM-30 (Required) |
| TM-40C | Movement & Maneuver WFF | G3/S3 M2 staff | 3 | TM-30 (Required) |
| TM-40D | Sustainment WFF | G4/S4 SUST staff | 3 | TM-30 (Required) |
| TM-40E | Protection WFF | Protection staff | 3 | TM-30 (Required) |
| TM-40F | Mission Command WFF | MC/G6/S6 staff | 3 | TM-30 (Required) |
| TM-40G | ORSA | ORSA analysts | 5 | TM-30 (Required) + quant background |
| TM-40H | AI Engineer | AI/ML specialists | 5 | TM-30 (Required) + coding background |
| TM-40I | ML Engineer | MLEs | 5 | TM-30 (Required) + coding background |
| TM-40J | Program Manager | PMs, G8/S8 | 4 | TM-30 (Required) |
| TM-40K | Knowledge Manager | KMOs, 37F | 4 | TM-30 (Required) |
| TM-40L | Software Engineer | SWEs | 5 | TM-30 (Required) + coding background |
| TM-50G | Advanced ORSA | Senior ORSA analysts | 5 | TM-40G (Required) |
| TM-50H | Advanced AI Engineer | Senior AI engineers | 5 | TM-40H (Required) |
| TM-50I | Advanced ML Engineer | Senior MLEs | 5 | TM-40I (Required) |
| TM-50J | Advanced Program Manager | Senior PMs | 3 | TM-40J (Required) |
| TM-50K | Advanced Knowledge Manager | Senior KMOs | 3 | TM-40K (Required) |
| TM-50L | Advanced Software Engineer | Senior SWEs | 5 | TM-40L (Required) |

> **NOTE:** TM-40A–F (WFF functional tracks) require TM-10, TM-20, and TM-30 as hard prerequisites. TM-40G–L (specialist tracks) also require TM-30 as a hard prerequisite. TM-50G–L (advanced specialist tracks) require the corresponding TM-40G–L. There are NO TM-50A–F tracks.

> **NOTE:** "Training days" reflects initial qualification training with instructor support. Self-paced completion may require more time. Refresher/sustainment training is shorter — see Section 11.

> **BUILDER SPRINT (BSP):** A quarterly 5-day applied build event that operates **outside** the TM-10 through TM-50 training chain. Prereq: TM-20 Go on file + command-validated project. Does not grant TM-30 credit. Does not unlock TM-40 enrollment. Governed by BSP-SOP-001 (training_management/BUILDER_SPRINT_SOP.md). Appears in training records as a separate event type, not as a TM course completion.

---

## Authoritative References

| Publication | Title | Relevance |
|---|---|---|
| AR 350-1 | Army Training and Leader Development | Master regulation for Army training policy; governs all institutional training programs |
| TR 350-70 | Army Learning Policy and Systems | TRADOC master regulation governing training program design, course administration, and learning products |
| ADP 7-0 | Training | Army training doctrine; establishes principles for training management across the force |
| FM 7-0 | Training | Unit training management procedures; provides commander guidance for planning, executing, and assessing training |

> **NOTE:** TR 350-70 is published by TRADOC at adminpubs.tradoc.army.mil, not DA APD.

---

## 2. TRAINING OBJECTIVES BY LEVEL

### 2-1. TM-10 — Maven User

**TLO:** Access, navigate, and consume data products on MSS in support of operational requirements.

| ELO | Description | Evaluation Method |
|---|---|---|
| 10-01 | Log in via CAC authentication and navigate to unit projects | Practical: observer validates login and navigation |
| 10-02 | Locate and view a dataset in a Workshop application | Practical: open designated application, filter to unit data |
| 10-03 | Execute an authorized Action in a Workshop application | Practical: submit status update via designated Action |
| 10-04 | Use Contour to build a basic chart and filter | Practical: create filtered bar chart from provided dataset |
| 10-05 | Use Quiver to explore an Object Type | Practical: navigate to assigned Object Type, apply filter, export view |
| 10-06 | Access and interact with an AIP Logic workflow or Agent interface | Practical: submit query to designated AIP interface |
| 10-07 | Identify classification markings and state authorized export procedures | Written/verbal: answer 3 of 4 classification scenario questions correctly |
| 10-08 | Troubleshoot at least 2 common access issues using TM-10 procedures | Practical: diagnose seeded access problem from troubleshooting annex |

### 2-2. TM-20 — Builder

**TLO:** Build, configure, and publish Foundry data products on MSS using visual (no-code) platform tools.

| ELO | Description | Evaluation Method |
|---|---|---|
| 20-01 | Create a Foundry project with correct naming, markings, and folder structure | Practical: inspector validates against naming convention checklist |
| 20-02 | Build a Pipeline Builder pipeline that ingests and transforms a provided dataset | Practical: pipeline runs; output schema validated |
| 20-03 | Create an Object Type and populate it via pipeline output | Practical: Object Type in Ontology Manager with correct properties |
| 20-04 | Create a Link Type connecting two Object Types | Practical: link traversable in Quiver |
| 20-05 | Configure a basic Action that writes to an Object Type property | Practical: execute Action; verify property updated |
| 20-06 | Build and publish a Workshop application with table, filter, and Action button | Practical: application accessible to test users; table and filter functional |
| 20-07 | Manage project access (grant Viewer role to test user) | Practical: test user confirms Viewer access; cannot edit |
| 20-08 | Create a Foundry branch, make a change, and submit for promotion | Practical: branch created; change visible; promotion request submitted |

### 2-3. TM-30 — Advanced Builder

**TLO:** Design and build complex, multi-source data products on MSS using advanced platform capabilities in accordance with C2DAO governance standards.

| ELO | Description | Evaluation Method |
|---|---|---|
| 30-01 | Build a multi-page Workshop application with conditional logic and variable passing | Practical: application behaves as designed across 3+ pages; evaluator tests 5 conditional scenarios |
| 30-02 | Build a Pipeline Builder pipeline with multi-source join and computed aggregation | Practical: output validated against known-answer dataset |
| 30-03 | Design an Ontology schema (Object Types, Link Types, Actions) — documented design | Design review: evaluated against 6-item rubric (see Appendix C) |
| 30-04 | Conduct advanced Contour analysis: pivot, calculated columns, and saved view | Practical: Contour workbook reproduces provided reference output |
| 30-05 | Build a multi-object Quiver dashboard with linked views | Practical: filters propagate across linked views; evaluated by observer |
| 30-06 | Configure an AIP Logic workflow (configure inputs/outputs/triggers, not author) | Practical: workflow triggers correctly; routes output to designated dataset |
| 30-07 | Interpret a data lineage graph for a provided dataset | Verbal/written: correctly identify upstream sources, transforms, and consumers |
| 30-08 | Complete the full C2DAO promotion workflow: branch, test, submit, receive approval | Practical: evaluator plays data steward; trainee executes end-to-end |

### 2-4. TM-40A through TM-40F — WFF Functional Tracks

**TLO (common):** Apply MSS data products to support warfighting function mission requirements; build and operate WFF-specific dashboards, pipelines, and ontology-backed tracking systems.

> Each WFF track shares a common task structure adapted to WFF-specific data and mission context. Prerequisite: TM-10, TM-20, and TM-30 (all required).

| Track | WFF | Audience | Key Focus Areas |
|---|---|---|---|
| TM-40A | Intelligence | G2/S2 Intel staff | PMESII analysis, ISR tracking, threat object ontology |
| TM-40B | Fires | Fires/FSCOORD staff | Target tracking, fire mission pipelines, effects dashboards |
| TM-40C | Movement & Maneuver | G3/S3 M2 staff | FRAGORD tracking, battle rhythm apps, unit disposition |
| TM-40D | Sustainment | G4/S4 SUST staff | Class IX tracking, maintenance dashboards, logistics pipelines |
| TM-40E | Protection | Protection staff | Risk assessment tracking, force protection dashboards |
| TM-40F | Mission Command | MC/G6/S6 staff | Battle rhythm management, comms status, commander's dashboard |

**Common ELOs for all WFF tracks:**

| ELO | Description | Evaluation Method |
|---|---|---|
| 40WFF-01 | Build a WFF-specific Pipeline Builder pipeline from provided exercise data | Practical: pipeline runs; output schema correct for WFF use case |
| 40WFF-02 | Create WFF Object Types and populate via pipeline | Practical: Object Types visible in Ontology Manager; properties correctly typed |
| 40WFF-03 | Configure a Workshop application with WFF-specific filters and status indicators | Practical: application displays correct data; filters functional |
| 40WFF-04 | Configure an Action to support a WFF workflow (e.g., status update, submission) | Practical: Action executes; correct property updated |
| 40WFF-05 | Build a multi-page WFF dashboard (summary → unit detail) | Practical: variable passing works; Page 2 filters by Page 1 selection |
| 40WFF-06 | Apply data governance: classification, naming, branching, and promotion workflow | Practical: product meets C2DAO naming and marking standards; promotion submitted |

### 2-5. TM-40J — Program Manager

**TLO:** Design and operate program management data products on MSS that support commander decision-making for schedule, resource, and portfolio health.

| ELO | Description | Evaluation Method |
|---|---|---|
| 40J-01 | Design a program data architecture (4 Object Types) for a provided scenario | Design review: evaluated against PM data model rubric |
| 40J-02 | Build a milestone tracking pipeline from a provided IMS spreadsheet | Practical: pipeline output validates against known-answer milestone set |
| 40J-03 | Build a Workshop milestone dashboard with RAG status and data-as-of timestamp | Practical: dashboard displays correct status; timestamp present |
| 40J-04 | Build a budget execution Quiver visualization showing obligation rate vs. target | Practical: chart displays correctly with reference line at quarterly target |
| 40J-05 | Configure a snapshot pipeline in Append mode for historical trend analysis | Practical: run pipeline 2× and verify cumulative records |
| 40J-06 | Produce an IPR product from MSS meeting the PM Dashboard Standards Checklist | Product review: evaluated against TM-40J Appendix A |

### 2-6. TM-40K — Knowledge Manager

**TLO:** Design and operate knowledge management systems on MSS that capture, organize, and deliver institutional knowledge in support of unit continuity and mission effectiveness.

| ELO | Description | Evaluation Method |
|---|---|---|
| 40K-01 | Design a knowledge ontology (5+ Object Types) for a provided unit KM scenario | Design review: evaluated against knowledge architecture checklist |
| 40K-02 | Configure a Workshop AAR submission form that writes to the AAR Object Type | Practical: submitter test confirms form writes correctly; required fields enforced |
| 40K-03 | Configure a lessons-learned intake pipeline with tagging and distribution logic | Practical: pipeline run with provided test data; output reviewed for accuracy |
| 40K-04 | Configure an AIP Logic summarization workflow for document intake | Practical: workflow processes a provided document; output reviewed by SME |
| 40K-05 | Build a knowledge browser application with search, filter, and drill-down | Practical: evaluator submits 5 test queries; application returns correct results |
| 40K-06 | Build and demonstrate a PCS knowledge transfer package for a specific role | Product review: package contains complete documentation per TM-40K Ch 9 |

### 2-7. TM-40G — ORSA

**TLO:** Conduct operations research and systems analysis on MSS, producing quantitatively rigorous decision support products meeting commander and ORSA product standards.

| ELO | Description | Evaluation Method |
|---|---|---|
| 40G-01 | Configure a Code Workspace with required packages and verify Foundry dataset connectivity | Practical: workspace runs provided test script without errors |
| 40G-02 | Build and validate a regression model for a provided readiness dataset | Practical: model results reviewed against reference solution; validation statistics correct |
| 40G-03 | Build a time series forecast with documented assumptions and confidence bounds | Practical: forecast output reviewed; uncertainty quantification present |
| 40G-04 | Run a Monte Carlo simulation for a provided COA comparison scenario | Practical: output distribution and confidence intervals reviewed by ORSA evaluator |
| 40G-05 | Formulate and solve a linear programming resource allocation problem | Practical: LP solution reviewed; constraint formulation documented |
| 40G-06 | Produce a commander brief including point estimates with uncertainty bounds | Product review: brief reviewed against ORSA product standards checklist |

### 2-8. TM-40H — AI Engineer

**TLO:** Author, test, and deploy AI-enabled capabilities on MSS using AIP Logic, Agent Studio, and LLM integration patterns in compliance with USAREUR-AF AI safety requirements.

| ELO | Description | Evaluation Method |
|---|---|---|
| 40H-01 | Author an AIP Logic workflow with prompt engineering, conditional chain logic, and structured JSON output | Practical: workflow runs against provided dataset; output schema validates |
| 40H-02 | Configure and test an AIP Agent Studio agent with at least two tools and defined memory scope | Practical: agent responds correctly to 5 evaluator queries; tool calls logged |
| 40H-03 | Build an LLM integration pipeline with ontology grounding and RAG | Practical: pipeline retrieves correct ontology context; evaluator validates output grounding |
| 40H-04 | Implement human-in-the-loop checkpoints for all write-capable Actions in a workflow | Practical: evaluator confirms no Action executes without a visible review/confirm step |
| 40H-05 | Write Python transforms that extract and format Ontology data for AIP Logic context | Practical: transform output matches expected schema; runs without error |
| 40H-06 | Complete the AIP Authorization Checklist (TM-40H Appendix A) for a proposed workflow; identify prohibited use cases | Written review: evaluator scores checklist completion and prohibited-use identification |

### 2-9. TM-40I — Machine Learning Engineer

**TLO:** Build, evaluate, deploy, and govern machine learning models on MSS using Foundry Code Workspaces and MLOps tooling in compliance with USAREUR-AF model governance standards.

| ELO | Description | Evaluation Method |
|---|---|---|
| 40I-01 | Configure Code Workspace with required packages, GPU allocation, and Foundry dataset connectivity | Practical: provided test script runs without errors; dataset connection confirmed |
| 40I-02 | Build a feature engineering pipeline for a provided Foundry dataset meeting documented feature standards | Practical: output dataset reviewed against feature specification; no null leakage |
| 40I-03 | Train and evaluate a supervised model meeting defined accuracy, precision/recall, and calibration thresholds | Practical: evaluation metrics reviewed by technical evaluator against acceptance criteria |
| 40I-04 | Deploy a trained model to a Foundry model serving endpoint and verify live inference | Practical: inference endpoint returns predictions for 10 test records; latency within spec |
| 40I-05 | Implement a model monitoring pipeline with drift detection and alert configuration | Practical: pipeline detects seeded drift event; alert routes correctly |
| 40I-06 | Complete a model governance document meeting USAREUR-AF model documentation standards | Product review: document reviewed against TM-40I governance checklist |

### 2-10. TM-40L — Software Engineer

**TLO:** Build, test, and deploy production-quality software applications and integrations on MSS using OSDK, Platform SDK, TypeScript Functions on Objects, and Slate, following USAREUR-AF code review and deployment standards.

| ELO | Description | Evaluation Method |
|---|---|---|
| 40L-01 | Authenticate to Foundry Ontology via OSDK; execute a paginated, filtered object query | Practical: query returns correct records; pagination handles >1 page |
| 40L-02 | Execute an Action via OSDK with full validation logic and structured error handling | Practical: valid Action executes; invalid input triggers correct error response |
| 40L-03 | Build a TypeScript Function on Objects implementing a computed property | Practical: computed property returns correct values for 10 test objects; edge cases handled |
| 40L-04 | Write and test a TypeScript Action validator with at least 3 distinct validation conditions | Practical: evaluator tests 5 scenarios; validator passes/blocks correctly in all cases |
| 40L-05 | Build a Slate application integrated with the Foundry API displaying live ontology data | Practical: application renders correctly; data refreshes on state change |
| 40L-06 | Complete a C2DAO code review and deployment workflow for a provided OSDK application | Practical: PR created, review comments addressed, deployment checklist completed end-to-end |

> **NOTE:** Developer track evaluations (TM-40H, 40I, 40L, 50H, 50I, 50L) require a qualified technical reviewer: TM-40 certified instructor, C2DAO data engineer, or equivalent. Do not evaluate developer track ELOs using a non-technical observer.

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
| MSS-20-T05 | Build a Workshop application (table + filter + Action) | Application published; filter works; Action accessible to authorized role |
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

### 3-4. TM-40A–F Tasks (WFF Functional Tracks — common task set, WFF-adapted scenarios)

| Task ID | Task | Go Standard |
|---|---|---|
| MSS-40WFF-T01 | Build a WFF-specific pipeline from provided exercise data | Pipeline runs without error; output schema correct |
| MSS-40WFF-T02 | Create WFF Object Types and populate via pipeline write step | Object Types populated; properties correctly typed; row count matches |
| MSS-40WFF-T03 | Configure a Workshop application with WFF filters and status indicators | Application displays live data; filters functional; classification marking present |
| MSS-40WFF-T04 | Configure an Action to support a WFF workflow | Action executes; correct Object property updated; access restriction enforced |
| MSS-40WFF-T05 | Build a multi-page WFF dashboard | Page 1 → Page 2 variable passing works; Page 2 data filtered by Page 1 selection |
| MSS-40WFF-T06 | Apply C2DAO governance: naming, marking, branching, and promotion | Product meets naming standards; promotion request submitted with complete description |

---

## 4. TRAINING STANDARDS AND GO/NO-GO CRITERIA

### 4-1. Go/No-Go Standard

| Training Level | Go Standard |
|---|---|
| TM-10 | Pass 6 of 7 tasks (T01–T07); pass classification questions (3 of 4) |
| TM-20 | Pass 6 of 7 tasks (T01–T07); Pipeline Builder pipeline runs without error |
| TM-30 | Pass 5 of 6 tasks (T01–T06); Ontology design document reviewed and approved |
| TM-40A–F (WFF) | Pass all 6 WFF tasks (T01–T06); WFF dashboard meets standard; data governance requirements met |
| TM-40G | Pass 5 of 6 ELOs; ORSA product brief reviewed by qualified ORSA evaluator |
| TM-40H/I/L | Pass developer track practical exercise; evaluated by TM-40 certified technical reviewer |
| TM-40J | Pass 5 of 6 ELOs; IPR product meets all PM Dashboard Standards Checklist items |
| TM-40K | Pass 5 of 6 ELOs; PCS transfer package reviewed and approved by instructor |

### 4-2. No-Go Actions

A trainee who does not meet the Go standard:
1. Receives specific written feedback on which task(s) failed and what was deficient.
2. Receives a remediation assignment (specific TM section, specific procedure to practice).
3. Completes a re-evaluation on the failed task(s) within 5 duty days.
4. May not advance to the next TM level until the current level Go standard is met.

> **NOTE:** No-Go at TM-10 often indicates an access provisioning issue (CAC enrollment, account not created) — not a training failure. Distinguish between access failures and competency failures. Fix access issues before assessing competency.

### 4-3. Evaluation Documentation

Training evaluations are documented in the Unit Training Status Matrix (Appendix A). Record at minimum:

| Field | Description |
|---|---|
| Trainee name and unit | — |
| TM level evaluated | — |
| Date of evaluation | — |
| Go/No-Go result | — |
| Evaluator name and TM certification level | — |
| Re-evaluation date (if applicable) | — |

---

## 5. BLOCKS OF INSTRUCTION — TIME REQUIREMENTS

### 5-1. TM-10 — 1 Training Day (8 hours)

| Block | Time | Content | Method |
|---|---|---|---|
| 1 | 0800–0900 | MSS overview; data literacy fundamentals (Data Literacy Technical Reference Ch 1 summary) | Lecture/discussion |
| 2 | 0900–1000 | MSS login, navigation, project access | Instructor-led lab |
| 3 | 1000–1100 | Workshop applications: consuming data, tables, filters | Instructor-led lab |
| 4 | 1100–1200 | Actions: executing status updates and form submissions | Instructor-led lab |
| — | 1200–1300 | Lunch | — |
| 5 | 1300–1400 | Contour: basic chart and filter | Guided practice |
| 6 | 1400–1500 | Quiver: exploring Object Types | Guided practice |
| 7 | 1500–1530 | AIP interface overview and demonstration | Demonstration |
| 8 | 1530–1600 | Classification markings and export procedures | Lecture/scenario |
| 9 | 1600–1700 | Practical exercise (all tasks) | Evaluation |

### 5-2. TM-20 — 5 Training Days (40 hours)

**Day 1 — Project Fundamentals and File Ingestion**

| Block | Time | Content | Method |
|---|---|---|---|
| — | 0800–0830 | TM-20 overview; what trainees will build by Day 5; course standards and Go criteria | Brief |
| 1 | 0830–1000 | Project creation: naming conventions, classification markings, folder structure | Instructor-led lab |
| — | 1000–1015 | Break | — |
| 2 | 1015–1100 | File ingestion: upload a CSV; inspect schema, types, and row count | Instructor-led lab |
| 3 | 1100–1200 | Dataset explorer: column profiling, null detection, type mismatches | Instructor-led lab |
| — | 1200–1300 | Lunch | — |
| 4 | 1300–1500 | Pipeline Builder orientation: canvas layout, step library, input/output dataset config | Instructor-led lab |
| 5 | 1500–1530 | C2DAO naming conventions: datasets, pipelines, Object Types | Lecture/discussion |
| 6 | 1530–1700 | Individual practice: create a second project, ingest a provided dataset, confirm naming compliance | Guided practice |

**Day 2 — Pipeline Builder: Clean and Transform**

| Block | Time | Content | Method |
|---|---|---|---|
| — | 0800–0830 | Review: Day 1 questions; confirm all trainees have projects and ingested data | Review |
| 7 | 0830–1030 | Pipeline: filter step, rename step, CAST for type correction | Instructor-led lab |
| — | 1030–1045 | Break | — |
| 8 | 1045–1200 | Pipeline: calculated columns — string functions, conditional logic (IF/CASE), COALESCE for nulls | Instructor-led lab |
| — | 1200–1300 | Lunch | — |
| 9 | 1300–1500 | Pipeline: date and time functions — DATEDIFF, DATE_TRUNC, CURRENT_DATE; test with known-answer records | Instructor-led lab |
| — | 1500–1515 | Break | — |
| 10 | 1515–1700 | End-to-end pipeline practice: build a complete clean-and-transform pipeline from raw input to typed filtered output; run and verify | Guided practice |

**Day 3 — Pipeline Builder: Joins and Ontology Manager**

| Block | Time | Content | Method |
|---|---|---|---|
| — | 0800–0830 | Review: Day 2 questions; pipeline troubleshooting — error messages, schema mismatches | Review |
| 11 | 0830–1030 | Pipeline: join step — inner/left join, key selection, handling duplicates post-join, output column selection | Instructor-led lab |
| — | 1030–1045 | Break | — |
| 12 | 1045–1200 | Pipeline: group-by aggregation; union step basics; output dataset configuration (overwrite vs. append) | Instructor-led lab |
| — | 1200–1300 | Lunch | — |
| 13 | 1300–1500 | Ontology Manager: create an Object Type — properties, types, Primary Key, display name expression | Instructor-led lab |
| — | 1500–1515 | Break | — |
| 14 | 1515–1630 | Ontology Manager: create a Link Type — connecting two Object Types, cardinality, directionality | Instructor-led lab |
| 15 | 1630–1700 | Ontology practice: design a second Object Type from a provided scenario; verify naming compliance | Guided practice |

**Day 4 — Ontology Write Step, Actions, and Workshop Applications**

| Block | Time | Content | Method |
|---|---|---|---|
| — | 0800–0845 | Review: Day 3 questions; access control model: Viewer vs. Editor roles | Review/discussion |
| 16 | 0845–0945 | Pipeline: Ontology write step — connect pipeline output to Object Type; configure property mapping; run and verify | Instructor-led lab |
| — | 0945–1000 | Break | — |
| 17 | 1000–1130 | Actions: create a basic Action — parameter, write rule, access restriction; test from Ontology Manager | Instructor-led lab |
| — | 1130–1145 | Break | — |
| 18 | 1145–1300 | Workshop orientation: canvas, widget library, Object Type binding — table widget with live data | Instructor-led lab |
| — | 1300–1400 | Lunch | — |
| 19 | 1400–1530 | Workshop: filter widget, metric widget, bar chart widget — layout and data source configuration | Instructor-led lab |
| — | 1530–1545 | Break | — |
| 20 | 1545–1700 | Workshop: connecting an Action button — trigger, confirmation prompt, post-action refresh | Instructor-led lab |

**Day 5 — Publishing, Governance, and Practical Exercise**

| Block | Time | Content | Method |
|---|---|---|---|
| — | 0800–0845 | Review: Day 4 questions; Workshop publishing and access configuration | Review |
| 21 | 0845–1000 | Workshop: publishing, access control — grant Viewer and Editor roles; confirm role behavior | Instructor-led lab |
| — | 1000–1015 | Break | — |
| 22 | 1015–1130 | Foundry branching: create, make change, submit for data steward promotion with complete description | Instructor-led lab |
| — | 1130–1200 | Review: C2DAO governance standards and Go/No-Go criteria for practical exercise | Review |
| — | 1200–1300 | Lunch | — |
| 23 | 1300–1700 | Practical exercise (all TM-20 tasks) | Evaluation |

### 5-3. TM-30 — 5 Training Days (40 hours)

**Day 1 — Advanced Workshop**

| Block | Time | Content | Method |
|---|---|---|---|
| — | 0800–0830 | TM-30 overview; what trainees will build by Day 5; design-first methodology | Brief |
| 1 | 0830–1030 | Multi-page Workshop: page navigation, parameter configuration, URL deep links | Instructor-led lab |
| — | 1030–1045 | Break | — |
| 2 | 1045–1200 | Conditional logic: show/hide panels, conditional formatting on tables, dynamic widget visibility rules | Instructor-led lab |
| — | 1200–1300 | Lunch | — |
| 3 | 1300–1500 | Variable passing: passing object selections between pages; filtered detail views driven by page-1 selection | Instructor-led lab |
| — | 1500–1515 | Break | — |
| 4 | 1515–1700 | Design exercise: build a 3-page operations dashboard (portfolio → unit detail → historical trend); instructor critique | Guided practice |

**Day 2 — Advanced Pipeline Builder**

| Block | Time | Content | Method |
|---|---|---|---|
| — | 0800–0830 | Review: Day 1 questions; Workshop design critique debrief | Review |
| 5 | 0830–1030 | Multi-source joins: inner/left/outer, handling fan-out after join, post-join deduplication patterns | Instructor-led lab |
| — | 1030–1045 | Break | — |
| 6 | 1045–1200 | Union transforms: combining datasets with compatible schemas, handling schema mismatches | Instructor-led lab |
| — | 1200–1300 | Lunch | — |
| 7 | 1300–1500 | Group-by aggregations: count, sum, min/max, computed aggregation columns; aggregate-then-join patterns | Instructor-led lab |
| — | 1500–1515 | Break | — |
| 8 | 1515–1630 | Output configuration: overwrite vs. append mode; append mode for snapshot pipelines and historical records | Instructor-led lab |
| 9 | 1630–1700 | Scheduled pipeline configuration: schedule expression, build failure alert setup | Instructor-led lab |

**Day 3 — Ontology Design**

| Block | Time | Content | Method |
|---|---|---|---|
| — | 0800–0900 | Review: Day 2 questions; common pipeline errors from the lab | Review |
| 10 | 0900–1000 | Ontology design methodology: domain analysis, entity identification, relationship mapping, Action design | Lecture |
| — | 1000–1015 | Break | — |
| 11 | 1015–1200 | Individual design exercise: translate a provided mission requirement to a documented Ontology schema (Object Types, Link Types, cardinality, Actions) | Guided practice |
| — | 1200–1300 | Lunch | — |
| 12 | 1300–1500 | Design critique: each trainee presents schema; class critiques against the 6-item design rubric; instructor facilitates | Workshop |
| — | 1500–1515 | Break | — |
| 13 | 1515–1700 | Build the approved design: create the Ontology from the Day 3 design exercise; connect pipeline output via Ontology write step | Instructor-led lab |

**Day 4 — Analytics Tools and AIP Logic**

| Block | Time | Content | Method |
|---|---|---|---|
| — | 0800–0830 | Review: Day 3 questions; common Ontology build errors | Review |
| 14 | 0830–1030 | Contour: pivot tables, calculated columns, parameter controls, workbook structure, saving and sharing analysis views | Instructor-led lab |
| — | 1030–1045 | Break | — |
| 15 | 1045–1200 | Quiver: multi-object analysis, linked views, cross-filter propagation, drilling between Object Types | Instructor-led lab |
| — | 1200–1300 | Lunch | — |
| 16 | 1300–1430 | AIP Logic configuration: connecting triggers, inputs, outputs; human review queue design | Instructor-led lab |
| — | 1430–1445 | Break | — |
| 17 | 1445–1600 | Data lineage: reading a lineage graph; identifying upstream sources, transforms, and downstream consumers; using lineage to diagnose pipeline issues | Instructor-led lab |
| 18 | 1600–1700 | C2DAO production standards: what constitutes a production-ready data product; quality gates | Lecture/discussion |

**Day 5 — Governance and Practical Exercise**

| Block | Time | Content | Method |
|---|---|---|---|
| 19 | 0800–0900 | Full C2DAO promotion workflow: branch → change → description → submit → respond to feedback → approval | Instructor-led lab |
| 20 | 0900–1000 | Full-stack review: trace raw source → pipeline → Ontology → Workshop → governance; identify production-readiness gaps | Review |
| — | 1000–1015 | Break | — |
| — | 1015–1100 | Practical exercise scenario brief; design planning time — document Ontology schema on paper before touching the platform | Brief |
| — | 1100–1130 | Design review: evaluator reviews Ontology design against 6-item rubric; trainees with fatal design flaws correct before proceeding | Evaluation |
| — | 1130–1200 | Buffer: open lab — resolve any tool access or environment issues | Buffer |
| — | 1200–1300 | Lunch | — |
| 21 | 1300–1700 | Practical exercise (all TM-30 tasks) | Evaluation |

### 5-4. TM-40A–F — WFF Functional Tracks (3 Days each; prereq: TM-30)

> Each WFF track runs 3 days (24 hours). The schedule below applies to all 6 tracks (A–F). Scenario content and Object Type design vary by WFF; the instructional sequence and evaluation structure are identical.

**Day 1 — Data Architecture and Pipeline Fundamentals**

| Block | Time | Content | Method |
|---|---|---|---|
| 1 | 0800–0900 | WFF role on MSS; WFF-specific data products and use cases; course overview | Lecture/discussion |
| 2 | 0900–1100 | WFF Object Type design: key entities, properties, primary keys; document before building | Instructor-led lab |
| 3 | 1100–1200 | Pipeline Builder: ingest provided WFF dataset; clean and transform | Instructor-led lab |
| — | 1200–1300 | Lunch | — |
| 4 | 1300–1500 | Pipeline: join step, computed status columns, RAG logic, Ontology write step | Instructor-led lab |
| 5 | 1500–1700 | Individual practice: second pipeline build using alternate provided dataset | Guided practice |

**Day 2 — Workshop Applications and Actions**

| Block | Time | Content | Method |
|---|---|---|---|
| 6 | 0800–1000 | Workshop: WFF summary dashboard — table, filter widgets, status indicators | Instructor-led lab |
| 7 | 1000–1200 | Workshop: multi-page application — Page 1 summary → Page 2 unit detail (variable passing) | Instructor-led lab |
| — | 1200–1300 | Lunch | — |
| 8 | 1300–1500 | Actions: configure status update and submission Actions for WFF workflow | Instructor-led lab |
| 9 | 1500–1700 | Access control, classification markings, WFF-specific export procedures | Lecture/discussion |

**Day 3 — Governance and Practical Exercise**

| Block | Time | Content | Method |
|---|---|---|---|
| 10 | 0800–1000 | C2DAO naming conventions, branching, promotion workflow — WFF application context | Instructor-led lab |
| 11 | 1000–1200 | Supervised practice run: rebuild the prior day's dashboard with a new dataset | Guided practice |
| — | 1200–1300 | Lunch | — |
| 12 | 1300–1400 | Practical exercise scenario brief | BRF |
| 13 | 1400–1700 | Practical exercise (all 6 tasks) | Evaluation |

### 5-5. TM-40J — Program Manager (2 Days)

**Day 1 — Data Architecture and Ingestion**

| Block | Time | Content | Method |
|---|---|---|---|
| 1 | 0800–0900 | PM role on MSS; program data model (Program/Milestone/Resource/Risk Object Types) | Lecture/discussion |
| 2 | 0900–1100 | Ontology: creating PM Object Types, Link Types, and properties | Instructor-led lab |
| 3 | 1100–1200 | Pipeline Builder: IMS ingestion, date arithmetic, RAG status computation | Instructor-led lab |
| — | 1200–1300 | Lunch | — |
| 4 | 1300–1500 | Pipeline Builder: GFEBS obligation data; Append mode snapshot pipeline | Instructor-led lab |
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

### 5-6. TM-40K — Knowledge Manager (2 Days)

**Day 1 — Knowledge Architecture, AAR Systems, Lessons Learned**

| Block | Time | Content | Method |
|---|---|---|---|
| 1 | 0800–0900 | KM role on MSS; knowledge architecture design methodology | Lecture/discussion |
| 2 | 0900–1100 | Ontology: Knowledge Object Types (Document, Lesson, AAR, SOP, ExpertiseProfile) | Instructor-led lab |
| 3 | 1100–1200 | Workshop: AAR submission form design, required field validation | Instructor-led lab |
| — | 1200–1300 | Lunch | — |
| 4 | 1300–1500 | Lessons learned pipeline: intake, deduplication, tagging, distribution routing | Instructor-led lab |
| 5 | 1500–1700 | AIP Logic: document summarization and automatic tagging; SME review requirement | Guided lab |

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

### 5-7. TM-40G — ORSA (4 Days)

**Day 1 — Environment Setup and Statistical Modeling**

| Block | Time | Content | Method |
|---|---|---|---|
| 1 | 0800–0900 | ORSA role; analytical product standards; Code Workspace orientation | Lecture/discussion |
| 2 | 0900–1100 | Code Workspace setup: Python/R environment, packages, Foundry dataset connectivity | Instructor-led lab |
| 3 | 1100–1200 | Regression: linear and logistic for readiness forecasting | Instructor-led lab |
| — | 1200–1300 | Lunch | — |
| 4 | 1300–1500 | Classification models: feature selection, training, validation statistics | Instructor-led lab |
| 5 | 1500–1700 | Model validation standards; documenting assumptions; writing outputs to Foundry | Guided practice |

**Day 2 — Time Series and Monte Carlo**

| Block | Time | Content | Method |
|---|---|---|---|
| 6 | 0800–1000 | Time series: stationarity, ACF/PACF, ARIMA for readiness trend forecasting | Instructor-led lab |
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
| 16 | 1300–1700 | Practical exercise: regression + forecast + commander brief | Evaluation |

### 5-8. TM-40H — AI Engineer (4 Days)

**Day 1 — Safety, Architecture, and AIP Logic Fundamentals** *(Block 1 mandatory — no exceptions)*

| Block | Time | Content | Method |
|---|---|---|---|
| 1 | 0800–1000 | AI safety: human-in-the-loop requirements, OPSEC, prohibited use cases (Appendix B) | Lecture — mandatory |
| 2 | 1000–1200 | AIP platform architecture: AIP Logic, Agent Studio, Code Workspaces, LLM endpoints | Lecture/discussion |
| — | 1200–1300 | Lunch | — |
| 3 | 1300–1500 | AIP Logic: first workflow, prompt templates, input/output configuration | Instructor-led lab |
| 4 | 1500–1700 | AIP Logic: conditional chains, error handling, structured JSON output | Guided practice |

**Day 2 — Advanced AIP Logic and Python Transforms**

| Block | Time | Content | Method |
|---|---|---|---|
| 5 | 0800–1000 | AIP Logic: multi-step chains, looping, Action integration | Instructor-led lab |
| 6 | 1000–1200 | Python transforms for AIP: extracting and formatting Ontology data for LLM context | Instructor-led lab |
| — | 1200–1300 | Lunch | — |
| 7 | 1300–1500 | LLM integration patterns: context construction, grounding, RAG architecture | Lecture/lab |
| 8 | 1500–1700 | Ontology integration: connecting AIP Logic outputs to Object properties via Actions | Guided practice |

**Day 3 — Agent Studio and Evaluation**

| Block | Time | Content | Method |
|---|---|---|---|
| 9 | 0800–1100 | Agent Studio: architecture, tool configuration, memory, orchestration | Instructor-led lab |
| 10 | 1100–1200 | Testing AI outputs: red-teaming, adversarial prompts, evaluation frameworks | Lecture/exercise |
| — | 1200–1300 | Lunch | — |
| 11 | 1300–1500 | AI Output Validation Framework (Appendix C): applying to a workflow | Guided practice |
| 12 | 1500–1700 | AIP Authorization Checklist (Appendix A): full authorization walkthrough | Workshop |

**Day 4 — Production Deployment and Practical Exercise**

| Block | Time | Content | Method |
|---|---|---|---|
| 13 | 0800–1000 | Production deployment: pipeline scheduling, monitoring, rollback procedures | Lecture/demo |
| 14 | 1000–1200 | Practical exercise preparation: review scenario, plan design | Individual prep |
| — | 1200–1300 | Lunch | — |
| 15 | 1300–1700 | Practical exercise: author, test, and document AIP Logic workflow end-to-end | Evaluation |

### 5-9. TM-40I — Machine Learning Engineer (4 Days)

**Day 1 — Workspace and Feature Engineering**

| Block | Time | Content | Method |
|---|---|---|---|
| 1 | 0800–0900 | MLE role on MSS; model governance overview; Code Workspace orientation | Lecture |
| 2 | 0900–1100 | Code Workspace setup: GPU allocation, package management, Foundry dataset connectivity | Instructor-led lab |
| 3 | 1100–1200 | Feature engineering: null handling, encoding, scaling, leakage prevention | Lecture/lab |
| — | 1200–1300 | Lunch | — |
| 4 | 1300–1700 | Feature engineering pipeline build: Foundry dataset → feature matrix | Instructor-led lab |

**Day 2 — Model Training and Evaluation**

| Block | Time | Content | Method |
|---|---|---|---|
| 5 | 0800–1100 | Model training: scikit-learn/PyTorch patterns, cross-validation, hyperparameter tuning | Instructor-led lab |
| 6 | 1100–1200 | Evaluation: accuracy, precision/recall, calibration, ROC-AUC; acceptance thresholds | Lecture/lab |
| — | 1200–1300 | Lunch | — |
| 7 | 1300–1700 | Model evaluation exercise: evaluate 2 competing models; select and document | Guided practice |

**Day 3 — Deployment and MLOps**

| Block | Time | Content | Method |
|---|---|---|---|
| 8 | 0800–1000 | Model deployment: serving endpoints, inference API, integration with Ontology Actions | Instructor-led lab |
| 9 | 1000–1200 | MLOps on Foundry: experiment tracking, model registry, versioning | Instructor-led lab |
| — | 1200–1300 | Lunch | — |
| 10 | 1300–1500 | Monitoring: drift detection, data quality alerts, retraining triggers | Instructor-led lab |
| 11 | 1500–1700 | Operational use cases: readiness prediction, logistics demand, anomaly detection | Lecture/case study |

**Day 4 — Governance and Practical Exercise**

| Block | Time | Content | Method |
|---|---|---|---|
| 12 | 0800–1000 | Model governance: documentation standards, model cards, responsible AI requirements | Lecture/workshop |
| 13 | 1000–1200 | Practical exercise preparation: review scenario, plan pipeline | Individual prep |
| — | 1200–1300 | Lunch | — |
| 14 | 1300–1700 | Practical exercise: feature pipeline → train → evaluate → deploy → governance doc | Evaluation |

### 5-10. TM-40L — Software Engineer (4 Days)

**Day 1 — OSDK Fundamentals**

| Block | Time | Content | Method |
|---|---|---|---|
| 1 | 0800–0900 | SWE role on MSS; USAREUR-AF 5-layer data stack; code review standards | Lecture |
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
| 8 | 1300–1700 | Platform SDK exercise: build a dataset pipeline integration | Guided practice |

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
| 15 | 1300–1700 | Practical exercise: OSDK query → Action validator → Slate UI end-to-end | Evaluation |

---

## 6. TRAINING SCHEDULE TEMPLATES

### 6-1. Individual Integration Training Schedule (New Arrival)

**Week 1 — Foundation**

| Day | Training | Location | Access Requirement |
|---|---|---|---|
| Mon | TM-10 (full day) | MSS training environment | Basic MSS account (provisioned before arrival) |
| Tue | Supervised practice: unit operational MSS environment | G6/data team desk | Read-only access to unit projects |
| Wed | TM-20 Day 1 (if builder role) OR continuation practice | Training environment | Builder access provisioned |
| Thu | TM-20 Day 2 + evaluation | Training environment | Builder access |
| Fri | Review evaluation feedback; remediation if needed | — | — |

**Weeks 2–3 — Specialized Track (if applicable)**

Continue with TM-30 or TM-40 track based on role. No more than one TM level per week for initial qualification.

### 6-2. Unit-Wide Training Event (S6 Shop or Data Team)

**Week 1**

| Day | Training | Audience |
|---|---|---|
| Mon | Commander brief: Data Literacy for Senior Leaders summary (2 hrs); unit data strategy overview | All O-5+, S6 leadership |
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
| Thu | Confirm all TM-40 enrollments; brief functional staff on WFF track options; brief specialists on G–L track options | Training NCO/Officer |
| Fri | TM-40 scheduling coordination complete; access provisioning confirmed for all Week 3+ participants | Training NCO/Officer |

**Week 3 (TM-40 WFF Tracks)**

| Day | Training | Audience |
|---|---|---|
| Mon–Wed | TM-40A (Intel WFF) — 3 days | G2/S2 Intel staff |
| Mon–Wed | TM-40D (Sustainment WFF) — 3 days (parallel session if capacity allows) | G4/S4 staff |
| Thu–Fri or following week | Remaining WFF tracks (B, C, E, F) as scheduled | Applicable WFF functional staff |

> **NOTE:** All TM-40 tracks (A–F WFF and G–L specialist) require TM-30 completion. Ensure all TM-40 participants have TM-30 on file before enrolling. WFF and specialist (G–L) training can run concurrently in separate sessions once TM-30 is complete.

**Week 4 (TM-40 Specialist Tracks — 3-day courses)**

| Day | Training | Audience |
|---|---|---|
| Mon–Wed | TM-40G (ORSA) — 3 days | ORSA personnel |
| Mon–Wed | TM-40H (AI Engineer) — 3 days (parallel session if capacity allows) | AI Engineer personnel |
| Thu–Fri or following week | TM-40I (ML Engineer), TM-40L (Software Engineer) — 3 days each, as scheduled | ML Eng, SWE personnel |

**Week 5 (TM-40 Specialist Tracks — 4-day courses)**

| Day | Training | Audience |
|---|---|---|
| Mon–Thu | TM-40J (Program Manager) — 4 days | G8/S8, Program Managers |
| Mon–Thu | TM-40K (Knowledge Manager) — 4 days (parallel session if capacity allows) | Knowledge Managers, S6 |

> **NOTE:** TM-40J and TM-40K are 4-day courses (32 hours each). Do not schedule these as 3-day events. Access provisioning for TM-40H, TM-40I, and TM-40L requires 10–35 days (GPU workspaces, developer tokens) — initiate immediately after TM-30 enrollment is confirmed.

---

## 7. RESOURCE REQUIREMENTS

### 7-1. Access Requirements by Training Level

> **CAUTION:** Access provisioning is on the critical path for all MSS training. Request access a minimum of 5 duty days before the training start date. Training events that begin without provisioned access will fail. The training officer owns the access request timeline.

| Training Level | Access Required | Who Provisions | Lead Time |
|---|---|---|---|
| TM-10 | Standard MSS user account (Viewer in training project) | Unit MSS Administrator | 3–5 duty days |
| TM-20 | Builder access in training project | Unit MSS Administrator | 3–5 duty days |
| TM-30 | Editor access; AIP Logic configuration access | Unit MSS Admin + C2DAO | 5–7 duty days |
| TM-40A–F (WFF) | Builder access | Unit MSS Administrator | 3–5 duty days |
| TM-40G | Code Workspace (Python/R) | C2DAO | 7–10 duty days |
| TM-40H | AIP Logic authoring + Agent Studio access | C2DAO | 7–10 duty days |
| TM-40I | Code Workspace with GPU; model registry access | C2DAO | 10+ duty days |
| TM-40J | Builder access + GFEBS training data export | Unit MSS Admin + G8 | 5–7 duty days |
| TM-40K | Builder access + AIP Logic configuration | Unit MSS Admin + C2DAO | 5–7 duty days |
| TM-40L | OSDK developer access; TypeScript environment | C2DAO | 10+ duty days |

### 7-2. Training Environment Requirements

All MSS training is conducted in the **USAREUR-AF MSS Training Environment** — not the production environment. The training environment contains:
- Synthetic datasets representative of unit operational data (non-sensitive)
- Pre-configured training projects at each TM level
- Seeded Object Types and pipelines for exercise use
- Test user accounts for access control exercises

If the training environment is unavailable, coordinate with C2DAO for an approved production substitute with restricted permissions.

### 7-3. Instructor Hardware Requirements

| Requirement | Standard |
|---|---|
| Instructor workstation | Laptop with CAC reader, MSS access, projector output |
| Projector/display | Minimum 80" display or projector visible to all trainees |
| Network | Unclassified network with MSS access (confirm connectivity before training day) |
| Trainee workstations | One per trainee; CAC-capable; network access to MSS |
| Backup | Instructor maintains a pre-recorded demo video for each major task in case of MSS outage |

### 7-4. TM-10 Throughput Risk — G-3 Action Required

> **RISK FLAG — FOR G-3 ACTION**

TM-10 (Maven User, 1 day) is mandatory for **all** USAREUR-AF personnel within 30 days of assignment. At current instructor capacity and training iteration frequency, the program cannot process the full formation at the rate required to meet this standard.

**The gap:**
- TM-10 required population: all USAREUR-AF military and civilian personnel (theater-wide)
- Current certified TM-10 instructor pool: insufficient to run concurrent iterations at scale
- Current training frequency: insufficient to process new arrivals within the 30-day window during high-accession periods

**Impact:** Portions of the formation are operating MSS without TM-10 qualification, creating data governance risk (unqualified users making classification and access decisions) and operational risk (untrained users misreading or mishandling MSS data products).

**Options for G-3 consideration:**
1. **Instructor billet increase** — authorize additional C2DAO training billets or detail TM-20/30-certified personnel from units as TM-10 instructors on a rotational basis (qualification standard: Section 8-1)
2. **eLearning conversion of TM-10** — convert TM-10 to a self-paced computer-based training (CBT) that can be completed asynchronously; reserve the practical evaluation (Tasks 4-1, 4-2, and Ch 6 security markings) as the only instructor-administered element; this is the highest-leverage option for throughput
3. **Unit-embedded delivery** — certify one TM-20+ instructor per major subordinate command (MSC) to deliver TM-10 within their formation; C2DAO provides materials and certifies instructors; practical evaluation remains C2DAO-administered

**Recommended G-3 action:** Direct C2DAO to present options 2 and 3 with cost/risk analysis within 30 days. Until resolved, direct unit commanders to report TM-10 completion rates in the monthly Unit MSS Training Status Report (Section 10-2) and flag units below 70% completion for command attention.

---

## 8. INSTRUCTOR REQUIREMENTS AND CERTIFICATION

### 8-1. Instructor Qualification Standards

| TM Level | Instructor Requirement |
|---|---|
| TM-10 | TM-20 certified or higher; completed TM-10 evaluation as a trainee |
| TM-20 | TM-30 certified or higher |
| TM-30 | TM-40 certified in any track; or C2DAO-certified data engineer |
| TM-40A (Intel WFF) | TM-40A certified; G2/S2 background or Intel functional familiarity; TM-30 proficiency |
| TM-40B (Fires WFF) | TM-40B certified; Fires/FSCOORD background; TM-30 proficiency |
| TM-40C (M2 WFF) | TM-40C certified; G3/S3 movement and maneuver background; TM-30 proficiency |
| TM-40D (SUST WFF) | TM-40D certified; G4/S4 sustainment background; TM-30 proficiency |
| TM-40E (PROT WFF) | TM-40E certified; Protection background; TM-30 proficiency |
| TM-40F (MC WFF) | TM-40F certified; Mission Command/G6 background; TM-30 proficiency |
| TM-40G (ORSA) | Active-duty ORSA (FA49) with Code Workspace proficiency OR C2DAO-approved contractor |
| TM-40H (AI Eng) | C2DAO AI engineer or TM-40H certified individual |
| TM-40I (MLE) | C2DAO ML engineer or TM-40I certified individual |
| TM-40J (PM) | TM-40J certified; PM/resource management background |
| TM-40K (KM) | TM-40K certified; KM background (37F or equivalent) |
| TM-40L (SWE) | C2DAO software engineer or TM-40L certified; TypeScript/Python proficiency |

### 8-2. Instructor Certification Process

1. Complete the TM for the level you will instruct, plus one level above (or a TM-40 track for TM-30 instructors).
2. Pass the practical evaluation for the target level.
3. Co-instruct one full training event at the target level, observed by a C2DAO data engineer or existing certified instructor.
4. Receive written certification from C2DAO.
5. Renew certification annually by completing a TM-level practical exercise review.

### 8-3. Instructor-to-Trainee Ratios

| TM Level | Maximum T:I Ratio |
|---|---|
| TM-10 | 20:1 (lecture); 10:1 (lab) |
| TM-20 | 10:1 (all portions) |
| TM-30 | 8:1 (all portions) |
| TM-40A–F (WFF) | 10:1 (all portions — high-volume functional staff courses) |
| TM-40G/H/I/L | 5:1 (intensive coding/modeling content) |
| TM-40J/K | 10:1 (all portions) |

---

## 9. PRACTICAL EXERCISE DESIGNS

### 9-1. TM-10 — "Unit SITREP Access"

**Scenario:** S3 NCO assigned to unit. Unit uses MSS to track SITREP submissions from subordinate elements. Access the SITREP dashboard, check for missing submissions, and submit a correction.

**Tasks:**
1. Log in to MSS using CAC.
2. Navigate to the `[UNIT]-S3-SITREP-Tracker` application.
3. Filter the table to show only submissions from the last 7 days.
4. Identify which element has not submitted for today.
5. Execute the "Submit SITREP Update" Action to correct a seeded status error.
6. Export the filtered table to CSV.
7. State the classification marking and authorized distribution list for exports.

**Go standard:** All 7 tasks completed; classification question answered correctly.

### 9-2. TM-20 — "Build a Unit Readiness Tracker"

**Scenario:** S4 officer needs a simple equipment readiness tracker. Provided: Excel spreadsheet with equipment identifiers, assigned units, and current C-ratings.

**Tasks:**
1. Create a Foundry project named per unit convention.
2. Upload the provided Excel file; build a Pipeline Builder pipeline that cleans and outputs a validated dataset.
3. Create an `Equipment` Object Type with: `equipment_id`, `unit`, `c_rating`, `last_updated` properties.
4. Configure the pipeline to write Equipment objects.
5. Create an Action that allows an authorized user to update `c_rating`.
6. Build a Workshop application with: table, filter by `unit` and `c_rating`, and the Update Action button.
7. Grant a test user Viewer access; verify they cannot edit.
8. Create a branch, change the application title, and submit for promotion.

**Go standard:** All 8 tasks completed without instructor assistance; pipeline runs without error.

### 9-3. TM-40A–F — WFF Functional Track Practical Exercises

> Instructor selects from the applicable WFF track scenario bank. Scenarios below are representative for each track. All require TM-10, TM-20, and TM-30 completion.

**TM-40A (Intel WFF) — "ISR Status Tracker"**

**Scenario:** G2 analyst requires a dashboard showing ISR asset status across the AOR. Provided: synthetic ISR asset tracking spreadsheet.

**Tasks:**
1. Build a pipeline ingesting the ISR asset dataset; compute availability status per asset.
2. Create ISR Asset Object Type with required properties.
3. Build a Workshop application: table filtered by asset type and status.
4. Configure an "Update Asset Status" Action with appropriate access restriction.
5. Build a multi-page dashboard: Page 1 = AOR summary, Page 2 = unit-level detail.
6. Branch, submit product for promotion with complete description.

**Go standard:** All 6 tasks completed; pipeline runs without error; governance requirements met.

---

**TM-40B (Fires WFF) — "Target Tracking Dashboard"**

**Scenario:** FSCOORD requires a target status and engagement tracking application. Provided: synthetic target tracking dataset.

**Tasks (same structure as 40A — Fires-specific data and Object Types).** Go standard: all 6 tasks.

---

**TM-40C (Movement & Maneuver WFF) — "Unit Disposition Tracker"**

**Scenario:** S3 requires a unit disposition and FRAGORD compliance tracker. Provided: synthetic unit status dataset.

**Tasks (same structure — M2-specific Object Types).** Go standard: all 6 tasks.

---

**TM-40D (Sustainment WFF) — "Class IX Readiness Dashboard"**

**Scenario:** S4 requires a Class IX on-hand vs. requirement dashboard with shortfall flagging.

**Tasks (same structure — SUST-specific data model).** Go standard: all 6 tasks.

---

**TM-40E (Protection WFF) — "Force Protection Status Tracker"**

**Scenario:** Protection officer requires a threat indicator and force protection measure tracking dashboard.

**Tasks (same structure — PROT-specific Object Types).** Go standard: all 6 tasks.

---

**TM-40F (Mission Command WFF) — "Battle Rhythm and Comms Status Dashboard"**

**Scenario:** G6 requires a battle rhythm event tracker and comms system status dashboard for the commander.

**Tasks (same structure — MC/G6-specific data model).** Go standard: all 6 tasks.

---

### 9-4. TM-30 — "Multi-Source Operations Dashboard"

**Scenario:** S3 requires a dashboard combining personnel readiness (one dataset) and equipment readiness (second dataset) at the unit level, with battalion filter and drill-down to individual unit status.

**Tasks:**
1. Build a Pipeline Builder pipeline joining the two provided datasets on `unit_id`; compute overall readiness score per unit.
2. Design (document) the Ontology schema for a `Unit` Object Type and `ReadinessReport` Object Type with appropriate links.
3. Build a multi-page Workshop application: Page 1 = portfolio view (all units), Page 2 = unit detail (linked from Page 1), Page 3 = historical trend.
4. Build a Contour workbook showing readiness by battalion with a calculated deviation-from-standard column.
5. Submit the pipeline and application through the C2DAO promotion workflow.

**Evaluator rubric:** See Appendix C.

---

## 10. TRAINING STATUS TRACKING

### 10-1. Unit Training Status Matrix

The Unit Training Status Matrix (Appendix A) is the primary tracking tool. Maintained by the unit MSS Administrator or designated training NCO; reviewed monthly.

**Required fields per Soldier/civilian:**

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

Monthly one-pager submitted to C2DAO summarizing unit MSS training status.

```
UNIT MSS TRAINING STATUS REPORT
Unit: [Unit Designation]          Date: [YYYYMMDD]
Reporting Officer: [Name, Rank]   Contact: [Email]

PERSONNEL SUMMARY:
  Total personnel requiring TM-10: [#]     TM-10 Complete: [#] ([%])
  Total personnel requiring TM-20: [#]     TM-20 Complete: [#] ([%])
  Total personnel requiring TM-30: [#]     TM-30 Complete: [#] ([%])
  Total WFF track assignments (TM-40A–F):  [#]  WFF Complete: [#] ([%])
    Breakdown: 40A[#] 40B[#] 40C[#] 40D[#] 40E[#] 40F[#]
  Total specialist track assignments (TM-40G–L): [#]  Specialist Complete: [#] ([%])
    Breakdown: 40G[#] 40H[#] 40I[#] 40J[#] 40K[#] 40L[#]

ISSUES / SHORTFALLS:
  Access provisioning delays: [Y/N — if yes, describe]
  Personnel awaiting remediation: [#]
  Instructor availability: [adequate / insufficient]
  WFF track scheduling conflicts (functional staff unavailability): [describe if any]

NEXT TRAINING EVENT: [Date, Level, # of trainees]
```

---

## 11. SUSTAINMENT TRAINING REQUIREMENTS

### 11-1. Sustainment Standards

| Condition | Sustainment Requirement |
|---|---|
| Active daily MSS user | No formal sustainment; supervisory spot-check quarterly |
| Occasional user (weekly to monthly) | Practical task evaluation every 12 months |
| Infrequent user (<monthly) | Practical task evaluation every 6 months |
| MSS access not used in 6+ months | Re-evaluate at current TM level before resuming independent work |
| PCS arrival with prior MSS training | Re-evaluate TM-10 (access/navigation may differ by theater); waive with supervisor verification |

### 11-2. Sustainment Event Design

A sustainment event does not require a full-day class — design as a practical task check:

| Level | Duration | Method |
|---|---|---|
| TM-10 | 1 hour | Complete one task scenario from the TM-10 practical exercise bank (Appendix C). Evaluated by immediate supervisor or unit MSS Administrator. |
| TM-20/30 | 2–3 hours | Complete one of: build a new pipeline in a test project, modify an existing Workshop application, or complete a branch/promote workflow. Evaluated by TM-30+ certified individual. |
| TM-40 | 4 hours | Complete a representative task from the relevant TM-40 track. TM-40J/K sustainment may include producing a real unit product (PM dashboard update, AAR pipeline run) observed by a supervisor. |

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

**Scenario 10-A:** Access the `[Unit]-Readiness-Dashboard` application. Identify which subordinate element has the lowest C-rating. Export the table filtered to that element. State the classification of the dataset.

**Scenario 10-B:** Navigate to the `[Unit]-SITREP-Tracker`. Submit a SITREP for today using the designated Action. Verify submission appears in the tracker table.

**Scenario 10-C:** Use Contour to build a bar chart showing count of personnel by rank from the provided personnel dataset. Apply a filter for a specific unit. Save the chart.

**Scenario 10-D:** You receive an error message when trying to access a dataset. Using TM-10 troubleshooting procedures, identify the likely cause (one of three seeded scenarios: wrong marking, no project access, dataset moved). State the correct resolution action.

### TM-20 Scenarios (Instructor selects one per evaluation)

**Scenario 20-A:** Readiness Tracker — see Section 9-2.

**Scenario 20-B:** Build a training schedule tracker. Given an Excel file with trainee name, TM level, date, and result, build a Pipeline Builder pipeline, create a TrainingRecord Object Type, configure an Update Status Action, and build a Workshop application showing training completion percentages by unit.

**Scenario 20-C:** Given a logistics dataset (equipment, location, status), build a Pipeline Builder pipeline that filters to RED status items and a Workshop application displaying them with a mark-resolved Action.

### TM-40J Scenarios (PM — Instructor selects one per evaluation)

**Scenario 40J-A:** G8 data builder for a theater sustainment command program. Given a provided IMS spreadsheet (15 milestones) and a GFEBS obligation extract, build the full PM stack: Object Types, ingestion pipelines, milestone RAG dashboard, and obligation rate Quiver chart with a Q2 reference line. Application must display a data-as-of timestamp.

**Scenario 40J-B:** Command has 6 programs across 3 battalions. Using provided synthetic program data, build a Contour portfolio health matrix showing schedule and resource status per program, sorted by overall health descending. Export as PDF formatted for a commander IPR.

**Scenario 40J-C:** An existing PM dashboard has no data-as-of date and uses hardcoded status values in the pipeline. Identify and fix both issues. Document the changes in pipeline description fields and re-run to verify.

### TM-40K Scenarios (KM — Instructor selects one per evaluation)

**Scenario 40K-A:** Brigade KMO needs an AAR capture system. Build the Object Type, Workshop submission form with required-field validation, and a knowledge browser showing submitted AARs filterable by unit and event type.

**Scenario 40K-B:** Configure an AIP Logic summarization workflow that extracts structured lessons from provided documents, creates Draft Lesson objects, and routes them to a KM Review Queue Workshop application. Produce the AIP Authorization checklist for the workflow.

**Scenario 40K-C:** Design a PCS knowledge transfer package for an outgoing S3 operations sergeant who has been the unit MSS builder for 18 months. Using TM-40K Ch 9 procedures, produce the complete transfer package: key person dependency analysis, knowledge transfer artifacts list, and Foundry project handoff documentation.

### TM-40G Scenarios (ORSA — Evaluator selects one per evaluation)

**Scenario 40G-A:** Using a provided readiness dataset (12 months, C-ratings by battalion), build: (1) a linear regression to forecast C2-level probability at 6 months, (2) a time series forecast with 90% confidence intervals, (3) a commander brief showing the forecast with explicit uncertainty bounds. No point estimate without its confidence range.

**Scenario 40G-B:** G3 needs to compare two COAs for a logistics operation. Using provided demand and resource data, run a Monte Carlo simulation for each COA (1,000 trials minimum), produce a probability distribution for on-hand stock at D+30, and brief the comparison with risk characterization.

**Scenario 40G-C:** Given a maintenance schedule constraint problem (20 vehicles, 5 bay slots, maintenance windows, operational commitments), formulate and solve a linear program that maximizes vehicles available during a defined readiness window. Document all constraints; present the solution in language the S4 can brief.

### TM-40H Scenarios (AI Engineer — Evaluator selects one per evaluation)

**Scenario 40H-A:** Build an AIP Logic workflow that accepts unstructured SITREP text, extracts structured fields (unit, date, activity, status, issues), maps them to a SITREP Object Type via an Action, and routes uncertain extractions to a human review queue. Complete the AIP Authorization Checklist.

**Scenario 40H-B:** Configure an Agent Studio agent that answers natural language questions about unit readiness by querying the Readiness Object Type. The agent must refuse questions outside its defined scope and must not take any write Actions without an explicit confirmation step.

### TM-40I Scenarios (ML Engineer — Evaluator selects one per evaluation)

**Scenario 40I-A:** Given a provided equipment failure dataset, build: feature engineering pipeline, binary classifier for failure prediction within 30 days, evaluation report against acceptance thresholds, and a deployed inference endpoint. Produce the model governance document.

**Scenario 40I-B:** An existing model is deployed and showing data drift (evaluator seeds drift into the monitoring dataset). Diagnose the drift, characterize its type, and produce a written recommendation: retrain, adjust thresholds, or investigate data quality issue. Document the decision.

### TM-40L Scenarios (SWE — Evaluator selects one per evaluation)

**Scenario 40L-A:** Build a TypeScript application using OSDK that: (1) queries Unit objects filtered by readiness status, (2) paginates results into a Slate table view, (3) triggers a status update Action on user click with confirmation modal, and (4) handles error states with user-visible error messages. Complete the C2DAO deployment checklist.

**Scenario 40L-B:** Given a provided Action that writes to a Personnel Object Type, write a TypeScript validator enforcing: required field presence, valid rank enumeration, date range validation (no future dates), and cross-field logic (if status = DEPLOYED, location must be non-null). Test with 8 provided test cases (4 valid, 4 invalid).

### TM-30 Scenario Design Rubric (Evaluator Reference)

| Criterion | Description | Weight |
|---|---|---|
| Completeness | Design covers all required Object Types and Link Types | 20% |
| Correctness | Properties correctly typed; links directionally correct | 20% |
| Normalization | No property redundancy; proper use of links vs. embedded data | 15% |
| Naming convention | Follows USAREUR-AF naming convention throughout | 15% |
| Governance | Access model defined; data steward identified | 15% |
| Feasibility | Design is buildable within TM-30 toolset | 15% |

**Go:** Score ≥75% with no zero-score on any criterion.

---

*USAREUR-AF Operational Data Team — UNCLASSIFIED*
*MTP-MSS | Version 1.0 | March 2026*
