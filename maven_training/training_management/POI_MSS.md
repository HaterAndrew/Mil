# PROGRAM OF INSTRUCTION
## Maven Smart System (MSS) Training Program
### USAREUR-AF Operational Data Team — C2DAO

| | |
|---|---|
| **Program Designation** | MSS-POI-001 |
| **Proponent** | USAREUR-AF C2DAO |
| **Effective Date** | March 2026 |
| **Review Cycle** | Annual or upon major platform update |
| **Authority** | C2DAO Data Governance Directive |
| **Classification** | — |

---

## CHAPTER 1 — AUTHORITY, PURPOSE, AND SCOPE

### 1-1. Authority

Published under authority of the USAREUR-AF C2DAO. Establishes the official curriculum, evaluation standards, and resource requirements for all MSS training within the USAREUR-AF AOR.

### 1-2. Purpose

Defines course content, instructional methods, evaluation criteria, and resource requirements for each training level. Serves as the authoritative reference for course scheduling, instructor preparation, student enrollment, and program assessment.

### 1-3. Scope

This POI covers twenty-five courses in six tiers, plus the Senior Leader course (EXEC), the Foundry Bootcamp (FBC) event program, and two Train-the-Trainer (T3) courses:

| Tier | Courses | Notes |
|---|---|---|
| 1 — Foundation | SL 1 | Required for all USAREUR-AF personnel |
| 2 — Builder | SL 2 | All staff building or maintaining data products |
| 3 — Advanced Builder | SL 3 | Data-adjacent specialists and unit data leads |
| 4a — WFF Functional | SL 4A through SL 4F | Warfighting function staff; prereq SL 3 |
| 4b — Specialist | SL 4G through SL 4O | Role-specific specialist training; prereq SL 3 |
| 5 — Advanced Specialist | SL 5G through SL 5O | Advanced role-specific training; prereq corresponding SL 4 |
| — | EXEC (Senior Leader) | **Outside TM chain.** 1 day; O-5/E-9+ personnel. Replaces SL 1 for senior leaders. No further progression. |
| — | Foundry Bootcamp (FBC) | **Outside TM chain.** Quarterly applied build event; prereq SL 2 + validated project; no TM credit. See FBC-SOP-001. |
| — | T3-I (Instructor Certification) | **Outside TM chain.** 5 days classroom + supervised practicum; prereq SL 3 + C2DAO selection. |
| — | T3-F (MSC Force Multiplier) | **Outside TM chain.** Half day; prereq SL 2 + CDR nomination. Produces Unit Data Trainers. |

### 1-4. Prerequisite Chain

```
EXEC (senior leaders — O-5/E-9+ — terminal, no further progression)

SL 1 (all personnel)
  └── SL 2 (builders)
  │     └── T3-F (MSC Force Multiplier — Unit Data Trainer; + CDR nomination)
  │
  └── SL 2 (builders)
        └── SL 3 (advanced builders / data-adjacent / WFF functional staff)
              ├── T3-I (Instructor Certification; + C2DAO selection)
              ├── SL 4A through SL 4F (WFF functional tracks — INT/FIRES/M2/SUST/PROT/MC staff)
              ├── SL 4G (ORSA) → SL 5G (Advanced ORSA)
              ├── SL 4H (AI Engineer) → SL 5H (Advanced AI Engineer)
              ├── SL 4J (Program Manager) → SL 5J (Advanced Program Manager)
              ├── SL 4K (Knowledge Manager) → SL 5K (Advanced Knowledge Manager)
              ├── SL 4L (Software Engineer) → SL 5L (Advanced Software Engineer)
              ├── SL 4M (ML Engineer) → SL 5M (Advanced ML Engineer)
              ├── SL 4N (UI/UX Designer) → SL 5N (Advanced UI/UX Designer)
              └── SL 4O (Platform Engineer) → SL 5O (Advanced Platform Engineer)
```

### 1-5. Security Clearance Requirements

No security clearance is required for course enrollment or participation. Training materials are marked CUI where indicated.

> **NOTE:** Trainees who will apply MSS skills to classified data environments post-graduation must hold appropriate clearances per their unit's security manager. Clearance verification is the responsibility of the sponsoring unit, not the MSS training program.

> **NOTE:** Practical exercises use synthetic data within the MSS Training Environment. Where exercise materials carry CUI markings, trainees and instructors will handle, store, and dispose of those materials IAW AR 25-22 (*The Army Privacy Program*) and DoDI 5200.48 (*Controlled Unclassified Information*). CUI-marked exercise materials will not be removed from the training environment or transmitted via unencrypted channels.

### 1-6. Authoritative References

| Publication | Title | Relevance |
|---|---|---|
| AR 350-1 | Army Training and Leader Development | Master regulation for Army training policy; governs all institutional training programs |
| TR 350-70 | Army Learning Policy and Systems | TRADOC master regulation governing POI standards, course administration, and learning products |
| TP 350-70-14 | Training Development in Institutional Domain | TRADOC pamphlet governing POI construction, course design, and instructional system development |
| TP 350-70-7 | Army Educational Processes | TRADOC pamphlet governing curriculum development, assessment design, and evaluation methodology |
| ADP 7-0 | Training | Army training doctrine; establishes principles for training management across the force |
| FM 7-0 | Training | Unit training management procedures; provides commander guidance for planning, executing, and assessing training |

> **NOTE:** TR 350-70 and TP 350-70-x publications are published by TRADOC at adminpubs.tradoc.army.mil, not DA APD.

### 1-7. Training Environment

All MSS training is conducted in the **MSS Training Environment** — a dedicated Foundry instance with synthetic operational data. No training is conducted in the production MSS environment. Trainees do not ingest, modify, or export production operational data during training.

---

## CHAPTER 2 — PROGRAM OVERVIEW

### 2-1. Course Summary

| Course | Title | Tier | Duration | Hours | Prerequisite |
|---|---|---|---|---|---|
| SL 1 | Maven User | Foundation | 1 day | 8 | None |
| SL 2 | Builder | Builder | 5 days | 40 | SL 1 |
| SL 3 | Advanced Builder | Advanced | 5 days | 40 | SL 1, SL 2 |
| SL 4A | Intelligence WFF | WFF Functional | 3 days | 24 | SL 1, SL 2, SL 3 (Required) |
| SL 4B | Fires WFF | WFF Functional | 3 days | 24 | SL 1, SL 2, SL 3 (Required) |
| SL 4C | Movement & Maneuver WFF | WFF Functional | 3 days | 24 | SL 1, SL 2, SL 3 (Required) |
| SL 4D | Sustainment WFF | WFF Functional | 3 days | 24 | SL 1, SL 2, SL 3 (Required) |
| SL 4E | Protection WFF | WFF Functional | 3 days | 24 | SL 1, SL 2, SL 3 (Required) |
| SL 4F | Mission Command WFF | WFF Functional | 3 days | 24 | SL 1, SL 2, SL 3 (Required) |
| SL 4G | ORSA Specialist | Specialist | 5 days | 40 | SL 1, SL 2, SL 3 (Required) |
| SL 4H | AI Engineer | Specialist | 5 days | 40 | SL 1, SL 2, SL 3 (Required) |
| SL 4M | ML Engineer | Specialist | 5 days | 40 | SL 1, SL 2, SL 3 (Required) |
| SL 4J | Program Manager | Specialist | 4 days | 32 | SL 1, SL 2, SL 3 (Required) |
| SL 4K | Knowledge Manager | Specialist | 4 days | 32 | SL 1, SL 2, SL 3 (Required) |
| SL 4L | Software Engineer | Specialist | 5 days | 40 | SL 1, SL 2, SL 3 (Required) |
| SL 4N | UI/UX Designer | Specialist | 5 days | 40 | SL 1, SL 2, SL 3 (Required) |
| SL 4O | Platform Engineer | Specialist | 5 days | 40 | SL 1, SL 2, SL 3 (Required) |
| SL 5G | Advanced ORSA | Advanced Specialist | 5 days | 40 | SL 4G (Required) |
| SL 5H | Advanced AI Engineer | Advanced Specialist | 5 days | 40 | SL 4H (Required) |
| SL 5M | Advanced ML Engineer | Advanced Specialist | 5 days | 40 | SL 4M (Required) |
| SL 5J | Advanced Program Manager | Advanced Specialist | 3 days | 24 | SL 4J (Required) |
| SL 5K | Advanced Knowledge Manager | Advanced Specialist | 3 days | 24 | SL 4K (Required) |
| SL 5L | Advanced Software Engineer | Advanced Specialist | 5 days | 40 | SL 4L (Required) |
| SL 5N | Advanced UI/UX Designer | Advanced Specialist | 3 days | 24 | SL 4N (Required) |
| SL 5O | Advanced Platform Engineer | Advanced Specialist | 3 days | 24 | SL 4O (Required) |

> **NOTE:** SL 4A–F (WFF functional tracks) require SL 1, SL 2, and SL 3 as hard prerequisites. SL 4G–O (specialist tracks) and SL 5G–O (advanced specialist tracks) also require SL 3 as a hard prerequisite. There are NO SL 5A–F tracks.

**Total program hours (full progression to any single WFF or specialist track):** 128 hours (SL 1 through SL 4G–O); 112 hours (SL 1 through SL 4A–F)
**Total program hours (full progression to any single advanced specialist track):** 168 hours (SL 1 through SL 5G–O)

### 2-2. Training Philosophy

MSS training is competency-based, not time-based. Go/No-Go evaluation at the end of each course is the authoritative measure of completion. Training emphasizes:

| Principle | Description |
|---|---|
| Build, break, recover | Lab time includes structured error-recovery before evaluation |
| Design before tool | SL 3+: trainees document design before opening the tool |
| Operational context | All scenarios use operationally plausible data and mission contexts |
| Governed practice | Data governance, naming, and access control are integrated into every lab |

### 2-3. Instructional Methods

| Code | Method | Description |
|---|---|---|
| LEC | Lecture | Instructor-delivered; students in listening/note-taking role |
| LAB | Laboratory | Hands-on tool exercise at workstation |
| DIS | Discussion | Structured facilitated discussion; student contributions required |
| SEM | Seminar | Small-group intensive; used for safety blocks and design critique |
| BRF | Brief | Short instructor-led overview or scenario introduction |
| REV | Review | Structured review of prior material; student Q&A focused |
| EVAL | Evaluation | Practical exercise; graded; no instructor assistance permitted |
| WKS | Workshop | Design workshop; student product reviewed by instructor/peers |
| SPRINT | Foundry Bootcamp | Self-directed applied build with SME consultation available; used exclusively in FBC events; no instructor delivery |

---

## CHAPTER 3 — BLOCKS OF INSTRUCTION

### 3-1. SL 1: Maven User

**Course length:** 1 day (8 hours) | **Evaluation:** Practical exercise (6 tasks, Go/No-Go)

| Block | Title | Hours | Method | Reference |
|---|---|---|---|---|
| 1 | MSS Overview and Data Literacy Fundamentals | 1.0 | LEC | TM-10 Ch 1; Data Literacy Technical Reference Ch 1 |
| 2 | Login and Navigation: CAC Authentication, Project Access | 1.0 | LAB | TM-10 Ch 2 |
| 3 | Workshop Applications: Tables, Filters, Dashboards | 1.0 | LAB | TM-10 Ch 3 |
| 4 | Actions: Executing Status Updates and Form Submissions | 1.0 | LAB | TM-10 Ch 4 |
| 5 | Contour: Building a Basic Chart and Applying a Filter | 1.0 | LAB | TM-10 Ch 5 |
| 6 | Quiver: Exploring Object Types, Filters, and Exporting Views | 1.0 | LAB | TM-10 Ch 6 |
| 7 | AIP Interface: Submitting a Query; Understanding AI Output Limitations | 0.5 | LAB | TM-10 Ch 7 |
| 8 | Classification Markings and Authorized Export Procedures | 0.5 | LEC | TM-10 Ch 8 |
| 9 | Practical Exercise (Evaluated) | 1.0 | EVAL | TM-10 Practical Exercise Guide |
| | **Total** | **8.0** | | |

---

### 3-2. SL 2: Builder

**Course length:** 5 days (40 hours) | **Evaluation:** Practical exercise (11 tasks, Go/No-Go)

**Day 1 — Project Fundamentals and File Ingestion**

| Block | Title | Hours | Method | Reference |
|---|---|---|---|---|
| 1 | Project Creation: Naming Conventions, Markings, Folder Structure | 1.5 | LAB | TM-20 Ch 2 |
| 2 | File Ingestion: Upload CSV, Inspect Schema, Types, Row Count | 0.75 | LAB | TM-20 Ch 3 Sec 3-1 |
| 3 | Dataset Explorer: Column Profiling, Null Detection, Type Mismatches | 1.0 | LAB | TM-20 Ch 3 Sec 3-2 |
| 4 | Pipeline Builder Orientation: Canvas, Step Library, I/O Config | 2.0 | LAB | TM-20 Ch 3 Sec 3-3 |
| 5 | C2DAO Naming Conventions: Datasets, Pipelines, Object Types | 0.5 | DIS | Standards Ch 1-2 |
| 6 | Individual Practice: Second Project, Ingest Provided Dataset | 1.5 | LAB | TM-20 Ch 2-3 |

**Day 2 — Pipeline Builder: Clean and Transform**

| Block | Title | Hours | Method | Reference |
|---|---|---|---|---|
| 7 | Pipeline: Filter Step, Rename Step, CAST for Type Correction | 2.0 | LAB | TM-20 Ch 3 Sec 3-4 |
| 8 | Pipeline: Calculated Columns — String Functions, Conditional Logic, COALESCE | 1.25 | LAB | TM-20 Ch 3 Sec 3-5 |
| 9 | Pipeline: Date and Time Functions — DATEDIFF, DATE_TRUNC, CURRENT_DATE | 2.0 | LAB | TM-20 Ch 3 Sec 3-6 |
| 10 | End-to-End Pipeline Practice: Raw Input to Typed Filtered Output | 1.75 | LAB | TM-20 Ch 3 |

**Day 3 — Pipeline Builder: Joins; Ontology Manager**

| Block | Title | Hours | Method | Reference |
|---|---|---|---|---|
| 11 | Pipeline: Join Step — Inner/Left Join, Key Selection, Deduplication | 2.0 | LAB | TM-20 Ch 3 Sec 3-7 |
| 12 | Pipeline: Group-By Aggregation, Union Step, Output Mode Configuration | 1.25 | LAB | TM-20 Ch 3 Sec 3-8 |
| 13 | Ontology Manager: Create Object Type — Properties, PK, Display Name | 2.0 | LAB | TM-20 Ch 4 Sec 4-1 |
| 14 | Ontology Manager: Create Link Type — Cardinality, Directionality | 0.75 | LAB | TM-20 Ch 4 Sec 4-2 |
| 15 | Pipeline: Ontology Write Step — Property Mapping, Run and Verify | 1.0 | LAB | TM-20 Ch 4 Sec 4-3 |

**Day 4 — Actions and Workshop Applications**

| Block | Title | Hours | Method | Reference |
|---|---|---|---|---|
| 16 | Actions: Create Basic Action — Parameter, Write Rule, Access Restriction | 1.5 | LAB | TM-20 Ch 4 Sec 4-4 |
| 17 | Workshop Orientation: Canvas, Widget Library, Object Type Binding, Table Widget | 1.75 | LAB | TM-20 Ch 5 Sec 5-1 |
| 18 | Workshop: Filter Widget, Metric Widget, Bar Chart Widget | 2.0 | LAB | TM-20 Ch 5 Sec 5-2 |
| 19 | Workshop: Connecting Action Button — Trigger, Confirmation, Post-Action Refresh | 1.25 | LAB | TM-20 Ch 5 Sec 5-3 |
| 20 | Access Control Model: Viewer vs. Editor Roles | 0.5 | DIS | TM-20 Ch 6 Sec 6-1 |

**Day 5 — Publishing, Governance, and Practical Exercise**

| Block | Title | Hours | Method | Reference |
|---|---|---|---|---|
| 21 | Workshop Publishing: Visibility, Viewer Access, Confirm Viewer Cannot Edit | 1.0 | LAB | TM-20 Ch 6 Sec 6-2 |
| 22 | Branching: Create Branch, Make Change on Branch, Verify Branch-Only | 1.0 | LAB | TM-20 Ch 7 Sec 7-1 |
| 23 | Promotion Workflow: Write Description, Submit to Steward, Respond to Rejection | 0.75 | LAB | TM-20 Ch 7 Sec 7-2 |
| 24 | Full-Stack Review: Trace Product from Raw File to Access Control | 1.0 | REV | SL 2 All Chapters |
| 25 | Practical Exercise (Evaluated) | 4.0 | EVAL | TM-20 Practical Exercise Guide |
| | **SL 2 Total** | **40.0** | | |

---

### 3-3. SL 3: Advanced Builder

**Course length:** 5 days (40 hours) | **Evaluation:** Practical exercise (6 tasks, including reviewed design document; Go/No-Go)

**Day 1 — Advanced Workshop**

| Block | Title | Hours | Method | Reference |
|---|---|---|---|---|
| 1 | Multi-Page Workshop: Navigation, Page Parameters, URL Deep Links | 2.0 | LAB | TM-30 Ch 2 Sec 2-1 |
| 2 | Conditional Logic: Show/Hide Panels, Conditional Formatting, Dynamic Visibility | 1.25 | LAB | TM-30 Ch 2 Sec 2-2 |
| 3 | Variable Passing: Object Selections Between Pages, Filtered Detail Views | 2.0 | LAB | TM-30 Ch 2 Sec 2-3 |
| 4 | Design Exercise: 3-Page Operations Dashboard (Portfolio→Unit→Trend); Instructor Critique | 1.75 | WKS | TM-30 Ch 2 |

**Day 2 — Advanced Pipeline Builder**

| Block | Title | Hours | Method | Reference |
|---|---|---|---|---|
| 5 | Multi-Source Joins: Inner/Left/Outer, Fan-Out Handling, Post-Join Deduplication | 2.0 | LAB | TM-30 Ch 3 Sec 3-1 |
| 6 | Union Transforms: Compatible Schemas, Handling Mismatches | 1.25 | LAB | TM-30 Ch 3 Sec 3-2 |
| 7 | Group-By Aggregations: Count/Sum/Min/Max, Aggregate-Then-Join Patterns | 2.0 | LAB | TM-30 Ch 3 Sec 3-3 |
| 8 | Output Mode: Overwrite vs. Append; Append for Snapshot Pipelines | 1.25 | LAB | TM-30 Ch 3 Sec 3-4 |
| 9 | Scheduled Pipeline: Schedule Expression, Build Failure Email Alert | 0.5 | LAB | TM-30 Ch 3 Sec 3-5 |

**Day 3 — Ontology Design**

| Block | Title | Hours | Method | Reference |
|---|---|---|---|---|
| 10 | Ontology Design Methodology: Domain Analysis, Entity ID, Relationship Mapping, Action Design | 1.0 | LEC | TM-30 Ch 4 Sec 4-1 |
| 11 | Individual Design Exercise: Mission Requirement → Documented Ontology Schema | 1.75 | LAB | TM-30 Ch 4 Sec 4-2 |
| 12 | Design Critique: Peer Presentations, Class Review Against 6-Item Rubric | 2.0 | WKS | SL 3 Design Rubric |
| 13 | Build the Approved Design: Create Ontology, Connect Pipeline via Write Step | 2.25 | LAB | TM-30 Ch 4 Sec 4-3 |

**Day 4 — Analytics Tools and AIP Logic**

| Block | Title | Hours | Method | Reference |
|---|---|---|---|---|
| 14 | Contour: Pivot Tables, Calculated Columns, Parameter Controls, Saved Views | 2.0 | LAB | TM-30 Ch 5 |
| 15 | Quiver: Multi-Object Analysis, Linked Views, Cross-Filter Propagation, Drilling | 1.25 | LAB | TM-30 Ch 6 |
| 16 | AIP Logic Configuration: Triggers, Inputs, Outputs; Human Review Queue Design | 1.5 | LAB | TM-30 Ch 7 Sec 7-1 |
| 17 | Data Lineage: Reading Lineage Graphs, Identifying Sources and Consumers | 1.25 | LAB | TM-30 Ch 8 |
| 18 | C2DAO Production Standards: Quality Gates for Production-Ready Data Products | 1.0 | DIS | Standards Ch 3 |

**Day 5 — Governance and Practical Exercise**

| Block | Title | Hours | Method | Reference |
|---|---|---|---|---|
| 19 | Full C2DAO Promotion Workflow: Branch → Change → Submit → Respond → Approval | 1.0 | LAB | TM-30 Ch 9 |
| 20 | Full-Stack Review: Raw Source → Pipeline → Ontology → Workshop → Governance | 1.0 | REV | SL 3 All Chapters |
| 21 | Practical Exercise Scenario Brief and Design Planning Time | 1.25 | BRF | — |
| 22 | Practical Exercise (Evaluated) | 4.0 | EVAL | TM-30 Practical Exercise Guide |
| | **SL 3 Total** | **40.0** | | |

---

### 3-4. SL 4G: ORSA Specialist

**Course length:** 5 days (40 hours) | **Evaluation:** Practical exercise (6 tasks); evaluated commander brief; Go/No-Go

| Day | Block | Title | Hours | Method | Reference |
|---|---|---|---|---|---|
| 1 | 1 | ORSA Role on MSS; Analytical Product Standards; Foundry Data Model | 1.0 | BRF | TM-40G Ch 1-2 |
| 1 | 2 | Code Workspace Setup: Package Install, GPU/CPU Allocation, Reproducibility | 2.0 | LAB | TM-40G Ch 2 Sec 2-3 |
| 1 | 3 | Foundry Dataset Connectivity: Reading via Spark/Pandas, Schema Inspection | 0.75 | LAB | TM-40G Ch 2 Sec 2-4 |
| 1 | 4 | Writing Outputs to Foundry: Transaction Pattern for Results to Curated Datasets | 2.0 | LAB | TM-40G Ch 2 Sec 2-5 |
| 1 | 5 | Data Profiling: Null Distributions, Outlier Detection, Feature Distributions | 1.75 | LAB | TM-40G Ch 3 Sec 3-1 |
| 2 | 6 | Regression: Linear Regression for Readiness Forecasting, Validation Statistics | 2.0 | LAB | TM-40G Ch 3 Sec 3-2 |
| 2 | 7 | Classification Models: Logistic Regression, Decision Trees, Cross-Validation | 1.25 | LAB | TM-40G Ch 3 Sec 3-3 |
| 2 | 8 | Model Validation Standards: Residual Analysis, Documenting Assumptions | 2.0 | LAB | TM-40G Ch 3 Sec 3-4 |
| 2 | 9 | Practice Build: Regression → Foundry Output → Quiver Visualization | 1.75 | LAB | TM-40G Ch 3 |
| 3 | 10 | Time Series: Stationarity, ACF/PACF, ARIMA Model Identification | 2.0 | LAB | TM-40G Ch 4 Sec 4-1 |
| 3 | 11 | ARIMA/SARIMA Build: Readiness Trend with 90% Confidence Bounds | 1.25 | LAB | TM-40G Ch 4 Sec 4-2 |
| 3 | 12 | Monte Carlo: COA Comparison, Distribution Selection, 1,000-Trial Simulation | 2.0 | LAB | TM-40G Ch 5 |
| 3 | 13 | Sensitivity Analysis; Logistics Stockage Risk Modeling | 1.75 | LAB | TM-40G Ch 5 Sec 5-3 |
| 4 | 14 | Linear Programming: Resource Allocation Formulation, scipy/lpSolve | 2.0 | LAB | TM-40G Ch 6 |
| 4 | 15 | Scheduling Optimization: Maintenance vs. Operational Commitments | 1.25 | LAB | TM-40G Ch 6 Sec 6-3 |
| 4 | 16 | Wargame/Exercise Data Architecture: Collection Templates, Analysis Pipeline | 2.0 | LAB | TM-40G Ch 7 |
| 4 | 17 | Quiver/Contour for ORSA: Forecast Dashboard, COA Comparison, Uncertainty Bounds | 1.75 | LAB | TM-40G Ch 8 |
| 5 | 18 | Communicating Uncertainty: Confidence Intervals, Briefing Posture, Translation | 1.0 | LEC | TM-40G Ch 9 |
| 5 | 19 | Common ORSA Brief Failures: Point Estimates Without Bounds, Methods-Paper Language | 1.0 | DIS | TM-40G Ch 9 |
| 5 | 20 | Practical Exercise Scenario Brief and ORSA Product Standards Review | 1.5 | BRF | — |
| 5 | 21 | Practical Exercise (Evaluated): Regression + Time Series + Commander Brief | 4.0 | EVAL | TM-40G Practical Exercise Guide |
| | | **SL 4G Total** | **40.0** | | |

---

### 3-5. SL 4H: AI Engineer

**Course length:** 5 days (40 hours)

**NOTE:** Day 1 Block 1 (AI Safety Seminar) is mandatory — no exceptions, no rescheduling.

**Evaluation:** Practical exercise (7 tasks); AIP Authorization Checklist review; Go/No-Go

| Day | Block | Title | Hours | Method | Reference |
|---|---|---|---|---|---|
| 1 | 1 | AI Safety: Human-in-the-Loop, OPSEC, Prohibited Use Cases, Army CIO Policy | 2.0 | SEM | TM-40H Ch 6; Appendix B |
| 1 | 2 | AIP Platform Architecture: Logic, Agent Studio, Code Workspaces, LLM Endpoints | 1.75 | LEC | TM-40H Ch 2 |
| 1 | 3 | AIP Logic: First Workflow — Prompt, Input, Output Binding, Test Run | 2.0 | LAB | TM-40H Ch 3 Sec 3-1 |
| 1 | 4 | AIP Logic: Conditional Chains, Error Handling, Structured JSON Output | 1.75 | LAB | TM-40H Ch 3 Sec 3-2 |
| 2 | 5 | AIP Logic: Multi-Step Chains, Looping, Parallel Branches, Action Integration | 2.0 | LAB | TM-40H Ch 3 Sec 3-3 |
| 2 | 6 | Python Transforms for AIP: Extracting Ontology Data, Context Formatting for Military Terminology | 1.25 | LAB | TM-40H Ch 4 Sec 4-1 |
| 2 | 7 | Context Management: Chunking Strategies, Context Window Limits, Large Dataset Handling | 2.0 | LAB | TM-40H Ch 4 Sec 4-2 |
| 2 | 8 | Ontology Integration: Write AIP Outputs via Actions; Human Review Queue for Uncertain Outputs | 1.75 | LAB | TM-40H Ch 4 Sec 4-3 |
| 3 | 9 | RAG Architecture: Semantic Search, Retrieval from Ontology Objects, Context Construction | 2.0 | LAB | TM-40H Ch 5 Sec 5-1 |
| 3 | 10 | RAG Pipeline Build: Retrieval → Context → Prompt → JSON Output → Ontology Write with Review Gate | 1.25 | LAB | TM-40H Ch 5 Sec 5-2 |
| 3 | 11 | RAG Quality: Retrieval Relevance, Grounding Failures, Hallucination Detection | 2.0 | LAB | TM-40H Ch 5 Sec 5-3 |
| 3 | 12 | End-to-End Workflow Practice: AIP Logic + RAG + Human Review + Ontology Write | 1.75 | LAB | TM-40H Ch 3-5 |
| 4 | 13 | Agent Studio: Architecture, Tool Definition, Tool-Use Authorization, Memory Scope | 2.75 | LAB | TM-40H Ch 7 |
| 4 | 14 | Agent Studio: Testing Tool Use; Confirming Authorization Controls | 1.0 | LAB | TM-40H Ch 7 Sec 7-4 |
| 4 | 15 | Testing AI Outputs: Evaluation Frameworks, Red-Teaming, Adversarial Prompt Testing | 2.0 | LAB | TM-40H Ch 6 Sec 6-5 |
| 4 | 16 | AI Output Validation Framework; AIP Authorization Checklist Completion | 1.75 | LAB | TM-40H Appendix A, C |
| 5 | 17 | Production Deployment: Scheduling, Monitoring, Failure Alerting, Rollback | 1.0 | LAB | TM-40H Ch 8 |
| 5 | 18 | Practical Exercise Scenario Brief and Workflow Design Time | 1.0 | BRF | — |
| 5 | 19 | Authorization Checklist Guidance; Evaluation Criteria Review | 1.5 | BRF | TM-40H Appendix A |
| 5 | 20 | Practical Exercise (Evaluated): Author → Test → Authorize → Deploy AIP Workflow | 4.0 | EVAL | TM-40H Practical Exercise Guide |
| | | **SL 4H Total** | **40.0** | | |

---

### 3-6. SL 4M: ML Engineer

**Course length:** 5 days (40 hours) | **Evaluation:** Practical exercise (7 tasks); model card review; Go/No-Go

| Day | Block | Title | Hours | Method | Reference |
|---|---|---|---|---|---|
| 1 | 1 | MLE Role on MSS; Model Governance Overview; Responsible AI for Operational Models | 1.0 | BRF | TM-40M Ch 1, 9 |
| 1 | 2 | Code Workspace Setup: GPU Allocation, Package Management, Foundry Connectivity | 2.0 | LAB | TM-40M Ch 2 |
| 1 | 3 | Foundry Write Pattern for ML: Transaction-Based Output Writes from Code Workspace | 0.75 | LAB | TM-40M Ch 2 Sec 2-4 |
| 1 | 4 | Feature Engineering Principles: Null Handling, Encoding, Scaling, Leakage Detection | 2.0 | LEC | TM-40M Ch 3 Sec 3-1 |
| 1 | 5 | Feature Engineering Practice: Apply Standards to Provided Dataset; Document Features | 1.75 | LAB | TM-40M Ch 3 Sec 3-2 |
| 2 | 6 | Feature Pipeline Build: Raw → Feature Matrix (Null, Encoding, Scaling) | 2.75 | LAB | TM-40M Ch 3 Sec 3-3 |
| 2 | 7 | Feature Pipeline: Leakage Audit — Verify No Feature Derived from Label | 0.75 | LAB | TM-40M Ch 3 Sec 3-4 |
| 2 | 8 | Feature Pipeline: Output to Foundry Curated Dataset via Write Transaction | 2.0 | LAB | TM-40M Ch 3 Sec 3-5 |
| 2 | 9 | Experiment Setup: Train/Test Split, Cross-Validation, Baseline Model | 1.75 | LAB | TM-40M Ch 4 Sec 4-1 |
| 3 | 10 | Model Training: scikit-learn/PyTorch in Code Workspace; Cross-Validation; Hyperparameter Tuning | 2.75 | LAB | TM-40M Ch 4 Sec 4-2 |
| 3 | 11 | Model Evaluation: Accuracy/Precision/Recall/ROC-AUC; Acceptance Thresholds; Calibration | 1.0 | LAB | TM-40M Ch 5 |
| 3 | 12 | Model Comparison Exercise: Train Two Models, Select Winner, Document Rationale | 2.0 | LAB | TM-40M Ch 5 Sec 5-3 |
| 3 | 13 | Experiment Tracking: Log Parameters/Metrics to Foundry Model Registry; Versioning | 1.75 | LAB | TM-40M Ch 6 |
| 4 | 14 | Model Deployment: Serving Endpoint, Inference API, Latency/Throughput Verification | 2.0 | LAB | TM-40M Ch 7 Sec 7-1 |
| 4 | 15 | Connecting Deployed Model to Ontology: Actions That Invoke Inference, Write Predictions | 1.25 | LAB | TM-40M Ch 7 Sec 7-2 |
| 4 | 16 | Monitoring Pipeline: Data Drift Detection, Threshold Definition, Alert Routing | 2.0 | LAB | TM-40M Ch 7 Sec 7-3 |
| 4 | 17 | Operational Use Case Patterns: Readiness Prediction, Logistics Forecasting, Anomaly Detection | 1.75 | LAB | TM-40M Ch 8 |
| 5 | 18 | Model Governance: Model Card Completion — Assumptions, Limitations, Responsible AI Declaration | 1.0 | LAB | TM-40M Ch 9 |
| 5 | 19 | Deployment Approval and C2DAO Governance for Deployed Models | 1.0 | BRF | Standards Ch 4 |
| 5 | 20 | Practical Exercise Scenario Brief; Planning Time | 1.5 | BRF | — |
| 5 | 21 | Practical Exercise (Evaluated): Feature Pipeline → Train → Evaluate → Deploy → Monitor → Governance | 4.0 | EVAL | TM-40M Practical Exercise Guide |
| | | **SL 4M Total** | **40.0** | | |

---

### 3-7. SL 4J: Program Manager

**Course length:** 4 days (32 hours) | **Evaluation:** Practical exercise (7 tasks); PM Dashboard Standards Checklist review; Go/No-Go

| Day | Block | Title | Hours | Method | Reference |
|---|---|---|---|---|---|
| 1 | 1 | The Technical PM Role on MSS; How SL 4J Connects Operational Requirements to Technical Execution | 0.5 | BRF | TM-40J Ch 1 |
| 1 | 2 | Agile for Data Projects: Scrum Framework, Sprint Cadence, Backlog Management; Applied Exercise: Story Sizing | 1.5 | LAB | TM-40J Ch 2 |
| 1 | 3 | User Stories and Acceptance Criteria: Format, Quality Standards, Definition of Ready; Applied Exercise: Rewrite Requirements | 1.75 | LAB | TM-40J Ch 2 |
| 1 | 4 | Kanban for Operational Support; Sprint Ceremonies — Military Data Team Execution Standards; Sprint Planning Exercise | 2.0 | LAB | TM-40J Ch 2 |
| 1 | 5 | User Story Quality Workshop: Peer Review Against Definition of Ready; Common Failure Patterns | 1.75 | WKS | TM-40J Ch 2 |
| 2 | 6 | ML/AI Project Lifecycle: Six Phases from Problem Definition Through Sustainment; Gate Criteria; Cross-Track Handoffs | 1.5 | LEC | TM-40J Ch 3 |
| 2 | 7 | Requirements Elicitation from Commanders and Staff: Structured Intake, Translation Problem; Interview Simulation | 1.75 | LAB | TM-40J Ch 4 |
| 2 | 8 | Requirements Document Drill: Problem Statement, Success Criteria, Constraints, Definition of Done; Peer Review | 1.5 | LAB | TM-40J Ch 4 |
| 2 | 9 | Stakeholder Expectations: Delivery Timelines, Scope Tradeoffs, Cross-Track Coordination; PM vs. Technical Authority | 2.25 | LEC | TM-40J Ch 4 |
| 3 | 10 | Project Tracking System Architecture: Project Tracker Ontology Design; Sprint Board Specification; PM Requirements Spec | 2.0 | LAB | TM-40J Ch 5 |
| 3 | 11 | Commander-Facing Project Status Dashboard: Health Roll-Up, Milestone Status, Blocking Issues; Automated Status Alerts | 1.75 | LAB | TM-40J Ch 5 |
| 3 | 12 | Risk Management for Data Projects: Risk Register, Dependency Management, Cross-Track Blockers | 2.0 | LAB | TM-40J Ch 6 |
| 3 | 13 | Dependency Mapping Exercise: Identify Cross-Track Dependencies for Practical Exercise Scenario; Instructor Review | 2.0 | LAB | TM-40J Ch 6 |
| 4 | 14 | Delivery Planning: Scope/Timeline/Quality Tradeoffs, Release Planning, Definition of Done, Production Readiness Review | 1.0 | LEC | TM-40J Ch 7 |
| 4 | 15 | Change Management: User Adoption, Resistance Management, Rollout Sequencing, Platform Governance | 0.75 | LEC | TM-40J Ch 8 |
| 4 | 16 | Practical Exercise Scenario Brief; Environment Check | 0.75 | BRF | — |
| 4 | 17 | Practical Exercise — Phase 1 (Tasks 1–4): Requirements Document, User Stories, Sprint Board Spec, Dashboard Spec | 2.0 | EVAL | TM-40J Practical Exercise Guide |
| 4 | 18 | Practical Exercise — Phase 2 (Tasks 5–7): Dependency/Risk Register, Production Readiness Brief, Change Management Summary | 4.0 | EVAL | TM-40J Practical Exercise Guide |
| | | **SL 4J Total** | **32.0** | | |

---

### 3-8. SL 4K: Knowledge Manager

**Course length:** 4 days (32 hours) | **Evaluation:** Practical exercise (6 tasks); PCS package instructor review (Day 4); Go/No-Go

| Day | Block | Title | Hours | Method | Reference |
|---|---|---|---|---|---|
| 1 | 1 | KM Role on MSS; Knowledge Architecture Methodology; Why KM Systems Fail and What Makes Them Survive Personnel Turbulence | 1.0 | BRF | TM-40K Ch 1 |
| 1 | 2 | Ontology: Knowledge Object Types — Document, Lesson, AAR, SOP, ExpertiseProfile; Link Types; Design on Paper Before Building | 2.0 | LAB | TM-40K Ch 2 |
| 1 | 3 | Workshop: AAR Submission Form — Required-Field Validation, Submission Confirmation, Routing to AAR Object Type | 0.75 | LAB | TM-40K Ch 3 Sec 3-2 |
| 1 | 4 | Lessons Learned Pipeline: Intake, Deduplication, Tagging Taxonomy Design, Distribution Routing by Unit/Classification/Echelon | 2.0 | LAB | TM-40K Ch 4 |
| 1 | 5 | AIP Logic: Document Summarization; Automatic Theme Extraction; Human Review Queue — All AIP Outputs Begin as Draft | 1.75 | LAB | TM-40K Ch 5 Sec 5-1 |
| 2 | 6 | Workshop: Knowledge Browser — Search by Keyword, Filter by Tag/Unit/Date, Drill-Down to Lesson Detail | 2.0 | LAB | TM-40K Ch 5 Sec 5-4 |
| 2 | 7 | SOP/Doctrine Version Control: Lifecycle Management, Version Tagging, SOP Review Notification Workflow | 1.25 | LAB | TM-40K Ch 7 Sec 7-6 |
| 2 | 8 | AIP Prompt Iteration Lab (Extended): Test Against 5 Documents, Score Extraction Quality, Revise, Retest Minimum 3 Cycles | 2.25 | LAB | TM-40K Ch 5 Sec 5-3 |
| 2 | 9 | Prompt Comparison Debrief: Before/After Sharing, Structural Changes, Common Prompt Failure Patterns | 1.5 | WKS | TM-40K Ch 5 Sec 5-3 |
| 3 | 10 | Personnel Expertise Mapping: ExpertiseProfile Object Type, Skills Taxonomy, SME Directory; Privacy Act Authorities | 2.0 | LAB | TM-40K Ch 8 Sec 8-1 |
| 3 | 11 | PCS Knowledge Transfer Methodology: Key Person Dependency Analysis, Transfer Package Design, Foundry Project Handoff | 1.0 | LAB | TM-40K Ch 9 |
| 3 | 12 | PCS Package Requirements Brief: Chapter 9 Completeness Criteria; What a Passing Package Contains | 0.25 | BRF | TM-40K Ch 9 |
| 3 | 13 | PCS Package Draft Lab (Full Afternoon): Each Trainee Produces Complete Draft; Submitted by 1700 for Instructor Review | 4.0 | LAB | TM-40K Ch 9 |
| 4 | 14 | PCS Package Instructor Review: Written Feedback; Individual Conferral; Revision Against Chapter 9 Criteria | 2.25 | WKS | TM-40K Ch 9 |
| 4 | 15 | Practical Exercise Scenario Brief; Go Criteria Review for AIP Gate and PCS Package | 0.75 | BRF | — |
| 4 | 16 | Practical Exercise (Evaluated) | 4.0 | EVAL | TM-40K Practical Exercise Guide |
| | | **SL 4K Total** | **32.0** | | |

---

### 3-9. SL 4L: Software Engineer

**Course length:** 5 days (40 hours) | **Evaluation:** Practical exercise (6 tasks); validator test suite (8 test cases); deployment checklist review; Go/No-Go

| Day | Block | Title | Hours | Method | Reference |
|---|---|---|---|---|---|
| 1 | 1 | SWE Role on MSS; 5-Layer Data Stack; OSDK Architecture vs. Standard REST | 1.0 | LEC | TM-40L Ch 1 |
| 1 | 2 | OSDK Setup: Auth Architecture, Client Init, Token Handling, First Object Query | 2.0 | LAB | TM-40L Ch 2 Sec 2-1 |
| 1 | 3 | OSDK: Filtering and Sorting — Query Predicates, Sort Expressions, Field Selection | 0.75 | LAB | TM-40L Ch 2 Sec 2-2 |
| 1 | 4 | OSDK: Pagination — ResourceIterator, Iterating All Pages, Multi-Page Result Sets | 2.0 | LAB | TM-40L Ch 2 Sec 2-3 |
| 1 | 5 | OSDK: Link Traversal — Querying Related Objects Across Link Types | 1.75 | LAB | TM-40L Ch 2 Sec 2-4 |
| 2 | 6 | OSDK: Action Execution — Async Response, Task ID Polling for Completion | 2.0 | LAB | TM-40L Ch 3 Sec 3-1 |
| 2 | 7 | OSDK: Error Handling and Retry — Action Failures, Timeout, Structured Error Response | 1.25 | LAB | TM-40L Ch 3 Sec 3-2 |
| 2 | 8 | OSDK: Object Subscriptions — Real-Time Change Notifications via WebSocket | 2.0 | LAB | TM-40L Ch 3 Sec 3-3 |
| 2 | 9 | OSDK: Bulk Operations — Batch Queries, Bulk Action Submissions; Avoid Per-Object Loops | 1.75 | LAB | TM-40L Ch 3 Sec 3-4 |
| 3 | 10 | Platform SDK: Dataset Read Operations, Write Transactions, File Resources, Branch Management | 2.0 | LAB | TM-40L Ch 4 Sec 4-1 |
| 3 | 11 | Platform SDK Exercise: Build Dataset Integration Using Read/Write Transaction Pattern | 1.25 | LAB | TM-40L Ch 4 Sec 4-2 |
| 3 | 12 | TypeScript FOO: Repository Structure, Computed Property Implementation, Function Registration | 2.0 | LAB | TM-40L Ch 5 Sec 5-1 |
| 3 | 13 | FOO: Bulk Query Patterns — Avoiding N+1 Queries; Test with 200+ Object Set | 1.75 | LAB | TM-40L Ch 5 Sec 5-2 |
| 4 | 14 | TypeScript Action Validators: Multi-Condition, Cross-Field Logic, Error Message Standards | 2.0 | LAB | TM-40L Ch 6 Sec 6-1 |
| 4 | 15 | Validator Testing: Test Suite — 4 Valid, 4 Invalid; Each Paired with Expected Error Message | 1.25 | LAB | TM-40L Ch 6 Sec 6-2 |
| 4 | 16 | Slate Applications: Structure, Foundry API Integration, Widget Binding, Initial Data Load | 2.0 | LAB | TM-40L Ch 7 Sec 7-1 |
| 4 | 17 | Slate: State Management on Action Completion; Error State Display for Failed Actions | 1.75 | LAB | TM-40L Ch 7 Sec 7-2 |
| 5 | 18 | CI/CD: Repository Discipline, PR Workflow, Automated Testing, C2DAO Deployment Checklist | 1.0 | LEC | TM-40L Ch 8 |
| 5 | 19 | Security and Compliance: Token Handling, Input Sanitization, OPSEC for App Code | 1.0 | LEC | TM-40L Ch 9 |
| 5 | 20 | Practical Exercise Scenario Brief; Planning Time | 1.5 | BRF | — |
| 5 | 21 | Practical Exercise (Evaluated): OSDK → Validator → Slate UI → Deployment Checklist | 4.0 | EVAL | TM-40L Practical Exercise Guide |
| | | **SL 4L Total** | **40.0** | | |

---

### 3-10. SL 4N: UI/UX Designer

**Course length:** 5 days (40 hours) | **Evaluation:** Practical exercise (6 tasks); design portfolio review; Go/No-Go

| Day | Block | Title | Hours | Method | Reference |
|---|---|---|---|---|---|
| 1 | 1 | UI/UX Role on MSS; Design Principles for Operational Data Products; Workshop Design Patterns | 1.0 | BRF | TM-40N Ch 1-2 |
| 1 | 2 | User Research Methods: Stakeholder Interviews, Task Analysis, Persona Development for Military Users | 2.0 | LEC | TM-40N Ch 2 Sec 2-1 |
| 1 | 3 | Information Architecture: Organizing Complex Data for Command Audiences; Navigation Design | 1.25 | LAB | TM-40N Ch 2 Sec 2-2 |
| 1 | 4 | Wireframing Fundamentals: Low-Fidelity Prototyping for Workshop Applications | 2.0 | LAB | TM-40N Ch 3 Sec 3-1 |
| 1 | 5 | Design Critique: Peer Review of Wireframes Against Operational Requirements | 1.25 | WKS | TM-40N Ch 3 |
| 2 | 6 | Accessibility Standards: WCAG Compliance for Government Applications; Color Contrast, Text Sizing | 2.0 | LEC | TM-40N Ch 4 Sec 4-1 |
| 2 | 7 | Responsive Design: Multi-Device Layouts for Field and Garrison Use | 1.25 | LAB | TM-40N Ch 4 Sec 4-2 |
| 2 | 8 | Color Theory and Typography for Data Visualization: RAG Standards, Status Encoding | 2.0 | LAB | TM-40N Ch 5 |
| 2 | 9 | Dashboard Layout Patterns: Summary-Detail, Drill-Down, Comparison; Anti-Patterns to Avoid | 2.25 | LAB | TM-40N Ch 5 Sec 5-3 |
| 3 | 10 | High-Fidelity Prototyping: Workshop Application Design with Real Data Binding | 2.0 | LAB | TM-40N Ch 6 Sec 6-1 |
| 3 | 11 | Interactive Prototyping: Conditional Visibility, State Transitions, User Flow Design | 1.25 | LAB | TM-40N Ch 6 Sec 6-2 |
| 3 | 12 | User Testing Methodology: Test Plan Design, Task Scenarios, Observation Protocols | 2.0 | LEC | TM-40N Ch 7 Sec 7-1 |
| 3 | 13 | Usability Testing Lab: Conduct User Test with Peer; Document Findings; Prioritize Fixes | 2.25 | LAB | TM-40N Ch 7 Sec 7-2 |
| 4 | 14 | Design System Creation: Component Library, Style Guide, Reusable Widget Templates | 2.0 | LAB | TM-40N Ch 8 Sec 8-1 |
| 4 | 15 | Design System: Documenting Components for Developer Handoff; Naming Conventions | 1.25 | LAB | TM-40N Ch 8 Sec 8-2 |
| 4 | 16 | Design-Development Collaboration: Specification Documents, Design Tokens, Handoff Workflow | 2.0 | LAB | TM-40N Ch 9 |
| 4 | 17 | Design Review Process: Submitting Designs for C2DAO Standards Review; Iteration Workflow | 1.75 | DIS | TM-40N Ch 9 Sec 9-3 |
| 5 | 18 | Design Portfolio Standards: What Constitutes a Complete Operational UI/UX Deliverable | 1.0 | LEC | TM-40N Ch 10 |
| 5 | 19 | Practical Exercise Scenario Brief and Design Planning Time | 1.5 | BRF | — |
| 5 | 20 | Practical Exercise (Evaluated): User Research → Wireframe → Prototype → Test → Design System Artifact | 4.0 | EVAL | TM-40N Practical Exercise Guide |
| | | **SL 4N Total** | **40.0** | | |

---

### 3-11. SL 4O: Platform Engineer

**Course length:** 5 days (40 hours) | **Evaluation:** Practical exercise (6 tasks); deployment checklist review; Go/No-Go

| Day | Block | Title | Hours | Method | Reference |
|---|---|---|---|---|---|
| 1 | 1 | Platform Engineering Role on MSS; Infrastructure Architecture Overview; Foundry Deployment Model | 1.0 | BRF | TM-40O Ch 1-2 |
| 1 | 2 | Kubernetes Fundamentals: Cluster Architecture, Namespaces, Resource Quotas, Pod Lifecycle | 2.0 | LAB | TM-40O Ch 2 Sec 2-1 |
| 1 | 3 | Container Management: Image Registry, Build Pipeline, Vulnerability Scanning Basics | 1.25 | LAB | TM-40O Ch 2 Sec 2-2 |
| 1 | 4 | Foundry Infrastructure: Platform Components, Service Dependencies, Health Check Architecture | 2.0 | LAB | TM-40O Ch 3 Sec 3-1 |
| 1 | 5 | Infrastructure-as-Code: Configuration Management Patterns for Repeatable Deployments | 1.25 | LAB | TM-40O Ch 3 Sec 3-2 |
| 2 | 6 | Deployment Strategies: Rolling Updates, Blue-Green, Canary; Rollback Procedures | 2.0 | LAB | TM-40O Ch 4 Sec 4-1 |
| 2 | 7 | Deployment Lab: Execute a Rolling Update; Verify Zero-Downtime; Trigger a Rollback | 1.25 | LAB | TM-40O Ch 4 Sec 4-2 |
| 2 | 8 | Service Mesh and Networking: Ingress, Load Balancing, Service Discovery, TLS Configuration | 2.0 | LAB | TM-40O Ch 5 |
| 2 | 9 | Storage Management: Persistent Volumes, Storage Classes, Backup and Recovery Procedures | 2.25 | LAB | TM-40O Ch 5 Sec 5-3 |
| 3 | 10 | Monitoring Architecture: Metrics Collection, Log Aggregation, Distributed Tracing Setup | 2.0 | LAB | TM-40O Ch 6 Sec 6-1 |
| 3 | 11 | Alerting Configuration: Threshold Alerts, Anomaly Detection, Escalation Routes, PagerDuty Integration | 1.25 | LAB | TM-40O Ch 6 Sec 6-2 |
| 3 | 12 | Observability Dashboard Build: Health Status, Resource Utilization, Error Rates, SLI/SLO Tracking | 2.0 | LAB | TM-40O Ch 6 Sec 6-3 |
| 3 | 13 | Incident Response: Runbook Development, Escalation Procedures, Post-Incident Review Template | 2.25 | LAB | TM-40O Ch 7 |
| 4 | 14 | Security Hardening: Network Policies, RBAC Configuration, Secrets Management, Audit Logging | 2.0 | LAB | TM-40O Ch 8 Sec 8-1 |
| 4 | 15 | Access Control: Service Accounts, Pod Security Standards, Least-Privilege Enforcement | 1.25 | LAB | TM-40O Ch 8 Sec 8-2 |
| 4 | 16 | CI/CD Pipeline Design: GitOps Workflow, Automated Testing Gates, Promotion Environments | 2.0 | LAB | TM-40O Ch 9 Sec 9-1 |
| 4 | 17 | CI/CD Lab: Build a Pipeline with Test, Scan, and Deploy Stages; Verify Gate Enforcement | 1.75 | LAB | TM-40O Ch 9 Sec 9-2 |
| 5 | 18 | C2DAO Infrastructure Standards: Change Management, Deployment Approval, Documentation Requirements | 1.0 | LEC | TM-40O Ch 10 |
| 5 | 19 | Practical Exercise Scenario Brief and Infrastructure Planning Time | 1.5 | BRF | — |
| 5 | 20 | Practical Exercise (Evaluated): Deploy → Monitor → Alert → Secure → CI/CD Pipeline → Deployment Checklist | 4.0 | EVAL | TM-40O Practical Exercise Guide |
| | | **SL 4O Total** | **40.0** | | |

---

## CHAPTER 4 — TRAINING RESOURCES

### 4-1. Instructor Requirements

| Course | Minimum Instructor Qualification | T:I Ratio |
|---|---|---|
| SL 1 | SL 2 certified; 90 days active MSS use | 10:1 |
| SL 2 | SL 3 certified; 6+ months Foundry build experience; able to troubleshoot all SL 2 labs | 8:1 |
| SL 3 | SL 4 (any track) or C2DAO SME designation; able to conduct design critiques | 6:1 |
| SL 4A (Intel WFF) | SL 4A certified; G2/S2 Intel functional background; SL 3 proficiency | 8:1 |
| SL 4B (Fires WFF) | SL 4B certified; Fires/FSCOORD functional background; SL 3 proficiency | 8:1 |
| SL 4C (M2 WFF) | SL 4C certified; G3/S3 movement and maneuver background; SL 3 proficiency | 8:1 |
| SL 4D (SUST WFF) | SL 4D certified; G4/S4 sustainment background; SL 3 proficiency | 8:1 |
| SL 4E (PROT WFF) | SL 4E certified; Protection functional background; SL 3 proficiency | 8:1 |
| SL 4F (MC WFF) | SL 4F certified; Mission Command/G6 background; SL 3 proficiency | 8:1 |
| SL 4G | FA49 or equivalent ORSA background; SL 4G certified or C2DAO SME designation | 4:1 |
| SL 4H | AIP Logic authoring experience; C2DAO AI SME designation; SL 4H certified | 4:1 |
| SL 4M | ML production experience; SL 4M certified; C2DAO MLE SME designation | 4:1 |
| SL 4J | Program management background; SL 3 certified; GFEBS/IMS proficiency | 6:1 |
| SL 4K | Knowledge management background; SL 3 certified; AIP Logic configuration proficiency | 6:1 |
| SL 4L | Software engineering background; OSDK/Platform SDK proficiency; SL 4L certified | 4:1 |
| SL 4N | UI/UX design background; Workshop design proficiency; SL 4N certified or C2DAO UX SME designation | 4:1 |
| SL 4O | Platform engineering background; Kubernetes/container proficiency; SL 4O certified or C2DAO infrastructure SME designation | 4:1 |

### 4-2. Training Environment Requirements

| Course | Access Level Required | Provisioning Lead Time |
|---|---|---|
| SL 1 | MSS Viewer (standard) | 5 duty days |
| SL 2 | MSS Builder | 5 duty days |
| SL 3 | MSS Editor + AIP Logic configuration | 7 duty days |
| SL 4A–F (WFF) | MSS Builder | 5 duty days |
| SL 4G | Code Workspace (CPU or GPU) + standard Editor | 7–10 duty days |
| SL 4H | AIP Logic authoring + Agent Studio | 7–10 duty days |
| SL 4M | GPU-enabled Code Workspace | 10+ duty days |
| SL 4J | MSS Builder | 5 duty days |
| SL 4K | MSS Builder + AIP Logic configuration | 5–7 duty days |
| SL 4L | OSDK developer access + developer token | 10+ duty days |
| SL 4N | Workshop design access (Editor + AIP Logic configuration) | 7–10 duty days |
| SL 4O | Kubernetes cluster access + CI/CD pipeline access | 10+ duty days |

### 4-3. Training Aids and Materials

- Instructor presentation slides (per lesson plan)
- Training datasets (synthetic, stored in MSS Training Environment)
- Practical exercise scenario packages (printed + digital; prepared by instructor prior to course)
- TM reference materials (each trainee receives digital copy before Day 1)
- PM Dashboard Standards Checklist, ORSA Product Standards Checklist, C2DAO Deployment Checklist (printed)

---

## CHAPTER 5 — EVALUATION STANDARDS

### 5-1. Go/No-Go Standards

Go requires all three:
1. All critical tasks completed independently (no instructor assistance, no hints)
2. All hard No-Go items passed (see 5-2 below)
3. Minimum task threshold met (see course syllabus)

### 5-2. Hard No-Go Items (Automatic Failure)

| Course | Hard No-Go Item |
|---|---|
| SL 1 | Incorrect classification marking or export procedure |
| SL 2 | Viewer-role test account can trigger Action or modify data |
| SL 3 | Fatally-flawed Ontology design not corrected before build; promotion submitted without description |
| SL 4G | Commander brief presents point estimate without uncertainty bounds |
| SL 4H | Any AIP workflow writes to production Objects without human checkpoint |
| SL 4M | Model calibration not performed; governance document missing required sections |
| SL 4J | Dashboard has no data-as-of timestamp |
| SL 4K | AIP workflow auto-publishes without human review gate |
| SL 4L | Hardcoded credential in application code; validator test suite not fully passing |
| SL 4N | Design delivered without documented accessibility compliance or user testing plan |
| SL 4O | Infrastructure deployed without monitoring or alerting configuration |

### 5-3. No-Go Remediation

A trainee who receives No-Go must:
1. Receive documented counseling within 1 duty day (DA Form 4856 or equivalent)
2. Conduct remediation on failed tasks — minimum 4 hours for SL 1/20/40J/40K; minimum 8 hours for SL 3/40G/40H/40M/40L/40N/40O
3. Be re-evaluated within 10 duty days
4. A second No-Go requires C2DAO approval before a third evaluation

All remediation events are documented on the Individual Training Record.

### 5-4. Course Completion Documentation

Upon successful completion (Go):
1. Instructor updates the Unit Training Status Matrix (Appendix A of MTP)
2. Individual Training Record annotated with: course, date, evaluator name, Go/No-Go
3. For SL 3 and above: trainee's commander receives a completion notification

---

## APPENDIX A — COURSE HOURS SUMMARY MATRIX

| Course | Lecture/Brief | Lab | Discussion/Review | Workshop/Seminar | Evaluation | Total |
|---|---|---|---|---|---|---|
| SL 1 | 1.5 | 5.5 | — | — | 1.0 | 8.0 |
| SL 2 | — | 31.25 | 2.75 | — | 4.0 | 38.0* |
| SL 3 | 1.0 | 26.0 | 1.0 | 4.75 | 4.0 | 36.75* |
| SL 4A–F (each) | 1.0 | 15.0 | 1.0 | — | 3.0 | 20.0* |
| SL 4G | 2.0 | 30.0 | 1.0 | — | 4.0 | 37.0* |
| SL 4H | 3.75 | 28.25 | — | 2.0 | 4.0 | 38.0* |
| SL 4M | 1.0 | 31.0 | — | — | 4.0 | 36.0* |
| SL 4J | 0.5 | 17.75 | 0.5 | — | 4.0 | 22.75* |
| SL 4K | 1.0 | 14.25 | — | 2.25 | 4.0 | 21.5* |
| SL 4L | 2.0 | 30.0 | — | — | 4.0 | 36.0* |
| SL 4N | 4.0 | 22.0 | 1.75 | 1.25 | 4.0 | 33.0* |
| SL 4O | 2.5 | 30.0 | — | — | 4.0 | 36.5* |

*Remainder of scheduled hours are review periods and scenario briefs not separately categorized above.

> **NOTE:** SL 4A–F are 3-day/24-hour courses requiring SL 3 as a prerequisite. The hours summary above reflects approximate method distribution; exact distribution varies by WFF track and is specified in the applicable WFF Syllabus. SL 5G–O course hour breakdowns are specified in the applicable advanced specialist Syllabi and are not reproduced here.

---

## APPENDIX B — AMENDMENT RECORD

| Amendment | Date | Description | Approved By |
|---|---|---|---|
| Initial Publication | March 2026 | Initial POI for MSS Training Program | C2DAO |
| | | | |

---

*USAREUR-AF Operational Data Team*
*POI MSS-POI-001 | Version 1.0 | March 2026*
