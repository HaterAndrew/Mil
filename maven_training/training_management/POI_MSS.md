# PROGRAM OF INSTRUCTION
## Maven Smart System (MSS) Training Program
### USAREUR-AF Operational Data Team — C2DAO

---

| | |
|---|---|
| **Program Title** | Maven Smart System (MSS) Training Program |
| **Proponent** | USAREUR-AF C2DAO (Command and Control Data and Analytics Office) |
| **Program Designation** | MSS-POI-001 |
| **Effective Date** | March 2026 |
| **Supersedes** | N/A (initial publication) |
| **Review Cycle** | Annual or upon major platform update |
| **Authority** | USAREUR-AF G6/G9 Data Governance Directive |
| **Classification** | UNCLASSIFIED |

---

## CHAPTER 1 — AUTHORITY, PURPOSE, AND SCOPE

### 1-1. Authority

This Program of Instruction is published under the authority of the USAREUR-AF C2DAO. It establishes the official curriculum, evaluation standards, and resource requirements for all MSS training within the USAREUR-AF AOR.

### 1-2. Purpose

This POI establishes the approved training program for the Maven Smart System (MSS), built on the Palantir Foundry platform, operated by USAREUR-AF. It defines course content, instructional methods, evaluation criteria, and resource requirements for each training level. It serves as the authoritative reference for course scheduling, instructor preparation, student enrollment, and program assessment.

### 1-3. Scope

This POI covers ten courses organized in four tiers:

- **Tier 1 (Foundation):** TM-10 — required for all USAREUR-AF personnel
- **Tier 2 (Builder):** TM-20 — all staff assigned to build or maintain data products
- **Tier 3 (Advanced Builder):** TM-30 — data-adjacent specialists and unit data leads
- **Tier 4 (Specialist Tracks):** TM-40A through TM-40F — role-specific specialist training

### 1-4. Prerequisite Chain

```
TM-10 (all personnel)
  └── TM-20 (builders)
        └── TM-30 (advanced builders / data-adjacent)
              ├── TM-40A (ORSA)
              ├── TM-40B (AI Engineer)
              ├── TM-40C (ML Engineer)
              └── TM-40F (Software Engineer)
        └── TM-40D (Program Manager) [TM-10/20 required; TM-30 recommended]
        └── TM-40E (Knowledge Manager) [TM-10/20 required; TM-30 recommended]
```

### 1-5. Training Environment

All MSS training is conducted in the **MSS Training Environment** — a dedicated Foundry instance with synthetic operational data. No training is conducted in the production MSS environment. All training exercises use provided synthetic data; trainees do not ingest, modify, or export production operational data during training.

---

## CHAPTER 2 — PROGRAM OVERVIEW

### 2-1. Course Summary

| Course | Title | Tier | Duration | Hours | Prerequisite |
|---|---|---|---|---|---|
| TM-10 | Maven User | Foundation | 1 day | 8 | None |
| TM-20 | Builder | Builder | 5 days | 40 | TM-10 |
| TM-30 | Advanced Builder | Advanced | 5 days | 40 | TM-10, TM-20 |
| TM-40A | ORSA Specialist | Specialist | 5 days | 40 | TM-10, TM-20, TM-30 |
| TM-40B | AI Engineer | Specialist | 5 days | 40 | TM-10, TM-20, TM-30 |
| TM-40C | ML Engineer | Specialist | 5 days | 40 | TM-10, TM-20, TM-30 |
| TM-40D | Program Manager | Specialist | 3 days | 24 | TM-10, TM-20 |
| TM-40E | Knowledge Manager | Specialist | 3 days | 24 | TM-10, TM-20 |
| TM-40F | Software Engineer | Specialist | 5 days | 40 | TM-10, TM-20, TM-30 |

**Total program hours (full progression to any single specialist track):** 133 hours (TM-10 through TM-40A/B/C/F)

### 2-2. Training Philosophy

MSS training is competency-based, not time-based. A trainee completes a course when they demonstrate the ability to perform specified tasks independently and to standard — not when they have attended the required hours. The Go/No-Go evaluation at the end of each course is the authoritative measure of completion.

Training emphasizes:
- **Build, break, recover** — lab time is structured so trainees encounter and recover from common errors before the evaluation
- **Design before tool** — at TM-30 and above, trainees document their design before opening the tool
- **Operational context** — all scenarios use operationally plausible data and mission contexts
- **Governed practice** — data governance, naming conventions, and access control are not separate topics; they are integrated into every lab

### 2-3. Instructional Methods Used

| Method Code | Method | Description |
|---|---|---|
| LEC | Lecture | Instructor-delivered presentation; students in listening/note-taking role |
| LAB | Laboratory | Hands-on tool exercise; students build or operate on a workstation |
| DIS | Discussion | Structured facilitated discussion; student contributions required |
| SEM | Seminar | Small-group intensive; used for safety blocks and design critique |
| BRF | Brief | Short instructor-led overview or scenario introduction |
| REV | Review | Structured review of prior day's material; student Q&A focused |
| EVAL | Evaluation | Practical exercise; graded; no instructor assistance permitted |
| WKS | Workshop | Design workshop; student product reviewed by instructor/peers |

---

## CHAPTER 3 — BLOCKS OF INSTRUCTION

### 3-1. TM-10: Maven User

**Course length:** 1 day (8 hours)
**Evaluation method:** Practical exercise (6 tasks, Go/No-Go)

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

### 3-2. TM-20: Builder

**Course length:** 5 days (40 hours)
**Evaluation method:** Practical exercise (11 tasks, Go/No-Go)

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
| 24 | Full-Stack Review: Trace Product from Raw File to Access Control | 1.0 | REV | TM-20 All Chapters |
| 25 | Practical Exercise (Evaluated) | 4.0 | EVAL | TM-20 Practical Exercise Guide |
| | **Day 5 Subtotal** | **7.75** | | |
| | **TM-20 Total** | **40.0** | | |

---

### 3-3. TM-30: Advanced Builder

**Course length:** 5 days (40 hours)
**Evaluation method:** Practical exercise (6 tasks, including a reviewed design document; Go/No-Go)

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
| 12 | Design Critique: Peer Presentations, Class Review Against 6-Item Rubric | 2.0 | WKS | TM-30 Design Rubric |
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
| 20 | Full-Stack Review: Raw Source → Pipeline → Ontology → Workshop → Governance | 1.0 | REV | TM-30 All Chapters |
| 21 | Practical Exercise Scenario Brief and Design Planning Time | 1.25 | BRF | — |
| 22 | Practical Exercise (Evaluated) | 4.0 | EVAL | TM-30 Practical Exercise Guide |
| | **TM-30 Total** | **40.0** | | |

---

### 3-4. TM-40A: ORSA Specialist

**Course length:** 5 days (40 hours)
**Evaluation method:** Practical exercise (6 tasks); evaluated commander brief; Go/No-Go

| Day | Block | Title | Hours | Method | Reference |
|---|---|---|---|---|---|
| 1 | 1 | ORSA Role on MSS; Analytical Product Standards; Foundry Data Model | 1.0 | BRF | TM-40A Ch 1-2 |
| 1 | 2 | Code Workspace Setup: Package Install, GPU/CPU Allocation, Reproducibility | 2.0 | LAB | TM-40A Ch 2 Sec 2-3 |
| 1 | 3 | Foundry Dataset Connectivity: Reading via Spark/Pandas, Schema Inspection | 0.75 | LAB | TM-40A Ch 2 Sec 2-4 |
| 1 | 4 | Writing Outputs to Foundry: Transaction Pattern for Results to Curated Datasets | 2.0 | LAB | TM-40A Ch 2 Sec 2-5 |
| 1 | 5 | Data Profiling: Null Distributions, Outlier Detection, Feature Distributions | 1.75 | LAB | TM-40A Ch 3 Sec 3-1 |
| 2 | 6 | Regression: Linear Regression for Readiness Forecasting, Validation Statistics | 2.0 | LAB | TM-40A Ch 3 Sec 3-2 |
| 2 | 7 | Classification Models: Logistic Regression, Decision Trees, Cross-Validation | 1.25 | LAB | TM-40A Ch 3 Sec 3-3 |
| 2 | 8 | Model Validation Standards: Residual Analysis, Documenting Assumptions | 2.0 | LAB | TM-40A Ch 3 Sec 3-4 |
| 2 | 9 | Practice Build: Regression → Foundry Output → Quiver Visualization | 1.75 | LAB | TM-40A Ch 3 |
| 3 | 10 | Time Series: Stationarity, ACF/PACF, ARIMA Model Identification | 2.0 | LAB | TM-40A Ch 4 Sec 4-1 |
| 3 | 11 | ARIMA/SARIMA Build: Readiness Trend with 90% Confidence Bounds | 1.25 | LAB | TM-40A Ch 4 Sec 4-2 |
| 3 | 12 | Monte Carlo: COA Comparison, Distribution Selection, 1,000-Trial Simulation | 2.0 | LAB | TM-40A Ch 5 |
| 3 | 13 | Sensitivity Analysis; Logistics Stockage Risk Modeling | 1.75 | LAB | TM-40A Ch 5 Sec 5-3 |
| 4 | 14 | Linear Programming: Resource Allocation Formulation, scipy/lpSolve | 2.0 | LAB | TM-40A Ch 6 |
| 4 | 15 | Scheduling Optimization: Maintenance vs. Operational Commitments | 1.25 | LAB | TM-40A Ch 6 Sec 6-3 |
| 4 | 16 | Wargame/Exercise Data Architecture: Collection Templates, Analysis Pipeline | 2.0 | LAB | TM-40A Ch 7 |
| 4 | 17 | Quiver/Contour for ORSA: Forecast Dashboard, COA Comparison, Uncertainty Bounds | 1.75 | LAB | TM-40A Ch 8 |
| 5 | 18 | Communicating Uncertainty: Confidence Intervals, Briefing Posture, Translation | 1.0 | LEC | TM-40A Ch 9 |
| 5 | 19 | Common ORSA Brief Failures: Point Estimates Without Bounds, Methods-Paper Language | 1.0 | DIS | TM-40A Ch 9 |
| 5 | 20 | Practical Exercise Scenario Brief and ORSA Product Standards Review | 1.5 | BRF | — |
| 5 | 21 | Practical Exercise (Evaluated): Regression + Time Series + Commander Brief | 4.0 | EVAL | TM-40A Practical Exercise Guide |
| | | **TM-40A Total** | **40.0** | | |

---

### 3-5. TM-40B: AI Engineer

**Course length:** 5 days (40 hours)
**Day 1 Block 1 (AI Safety Seminar) is mandatory — no exceptions, no rescheduling.**
**Evaluation method:** Practical exercise (7 tasks); AIP Authorization Checklist review; Go/No-Go

| Day | Block | Title | Hours | Method | Reference |
|---|---|---|---|---|---|
| 1 | 1 | AI Safety: Human-in-the-Loop, OPSEC, Prohibited Use Cases, Army CIO Policy | 2.0 | SEM | TM-40B Ch 6; Appendix B |
| 1 | 2 | AIP Platform Architecture: Logic, Agent Studio, Code Workspaces, LLM Endpoints | 1.75 | LEC | TM-40B Ch 2 |
| 1 | 3 | AIP Logic: First Workflow — Prompt, Input, Output Binding, Test Run | 2.0 | LAB | TM-40B Ch 3 Sec 3-1 |
| 1 | 4 | AIP Logic: Conditional Chains, Error Handling, Structured JSON Output | 1.75 | LAB | TM-40B Ch 3 Sec 3-2 |
| 2 | 5 | AIP Logic: Multi-Step Chains, Looping, Parallel Branches, Action Integration | 2.0 | LAB | TM-40B Ch 3 Sec 3-3 |
| 2 | 6 | Python Transforms for AIP: Extracting Ontology Data, Context Formatting for Military Terminology | 1.25 | LAB | TM-40B Ch 4 Sec 4-1 |
| 2 | 7 | Context Management: Chunking Strategies, Context Window Limits, Large Dataset Handling | 2.0 | LAB | TM-40B Ch 4 Sec 4-2 |
| 2 | 8 | Ontology Integration: Write AIP Outputs via Actions; Human Review Queue for Uncertain Outputs | 1.75 | LAB | TM-40B Ch 4 Sec 4-3 |
| 3 | 9 | RAG Architecture: Semantic Search, Retrieval from Ontology Objects, Context Construction | 2.0 | LAB | TM-40B Ch 5 Sec 5-1 |
| 3 | 10 | RAG Pipeline Build: Retrieval → Context → Prompt → JSON Output → Ontology Write with Review Gate | 1.25 | LAB | TM-40B Ch 5 Sec 5-2 |
| 3 | 11 | RAG Quality: Retrieval Relevance, Grounding Failures, Hallucination Detection | 2.0 | LAB | TM-40B Ch 5 Sec 5-3 |
| 3 | 12 | End-to-End Workflow Practice: AIP Logic + RAG + Human Review + Ontology Write | 1.75 | LAB | TM-40B Ch 3-5 |
| 4 | 13 | Agent Studio: Architecture, Tool Definition, Tool-Use Authorization, Memory Scope | 2.75 | LAB | TM-40B Ch 7 |
| 4 | 14 | Agent Studio: Testing Tool Use; Confirming Authorization Controls | 1.0 | LAB | TM-40B Ch 7 Sec 7-4 |
| 4 | 15 | Testing AI Outputs: Evaluation Frameworks, Red-Teaming, Adversarial Prompt Testing | 2.0 | LAB | TM-40B Ch 6 Sec 6-5 |
| 4 | 16 | AI Output Validation Framework; AIP Authorization Checklist Completion | 1.75 | LAB | TM-40B Appendix A, C |
| 5 | 17 | Production Deployment: Scheduling, Monitoring, Failure Alerting, Rollback | 1.0 | LAB | TM-40B Ch 8 |
| 5 | 18 | Practical Exercise Scenario Brief and Workflow Design Time | 1.0 | BRF | — |
| 5 | 19 | Authorization Checklist Guidance; Evaluation Criteria Review | 1.5 | BRF | TM-40B Appendix A |
| 5 | 20 | Practical Exercise (Evaluated): Author → Test → Authorize → Deploy AIP Workflow | 4.0 | EVAL | TM-40B Practical Exercise Guide |
| | | **TM-40B Total** | **40.0** | | |

---

### 3-6. TM-40C: ML Engineer

**Course length:** 5 days (40 hours)
**Evaluation method:** Practical exercise (7 tasks); model card review; Go/No-Go

| Day | Block | Title | Hours | Method | Reference |
|---|---|---|---|---|---|
| 1 | 1 | MLE Role on MSS; Model Governance Overview; Responsible AI for Operational Models | 1.0 | BRF | TM-40C Ch 1, 9 |
| 1 | 2 | Code Workspace Setup: GPU Allocation, Package Management, Foundry Connectivity | 2.0 | LAB | TM-40C Ch 2 |
| 1 | 3 | Foundry Write Pattern for ML: Transaction-Based Output Writes from Code Workspace | 0.75 | LAB | TM-40C Ch 2 Sec 2-4 |
| 1 | 4 | Feature Engineering Principles: Null Handling, Encoding, Scaling, Leakage Detection | 2.0 | LEC | TM-40C Ch 3 Sec 3-1 |
| 1 | 5 | Feature Engineering Practice: Apply Standards to Provided Dataset; Document Features | 1.75 | LAB | TM-40C Ch 3 Sec 3-2 |
| 2 | 6 | Feature Pipeline Build: Raw → Feature Matrix (Null, Encoding, Scaling) | 2.75 | LAB | TM-40C Ch 3 Sec 3-3 |
| 2 | 7 | Feature Pipeline: Leakage Audit — Verify No Feature Derived from Label | 0.75 | LAB | TM-40C Ch 3 Sec 3-4 |
| 2 | 8 | Feature Pipeline: Output to Foundry Curated Dataset via Write Transaction | 2.0 | LAB | TM-40C Ch 3 Sec 3-5 |
| 2 | 9 | Experiment Setup: Train/Test Split, Cross-Validation, Baseline Model | 1.75 | LAB | TM-40C Ch 4 Sec 4-1 |
| 3 | 10 | Model Training: scikit-learn/PyTorch in Code Workspace; Cross-Validation; Hyperparameter Tuning | 2.75 | LAB | TM-40C Ch 4 Sec 4-2 |
| 3 | 11 | Model Evaluation: Accuracy/Precision/Recall/ROC-AUC; Acceptance Thresholds; Calibration | 1.0 | LAB | TM-40C Ch 5 |
| 3 | 12 | Model Comparison Exercise: Train Two Models, Select Winner, Document Rationale | 2.0 | LAB | TM-40C Ch 5 Sec 5-3 |
| 3 | 13 | Experiment Tracking: Log Parameters/Metrics to Foundry Model Registry; Versioning | 1.75 | LAB | TM-40C Ch 6 |
| 4 | 14 | Model Deployment: Serving Endpoint, Inference API, Latency/Throughput Verification | 2.0 | LAB | TM-40C Ch 7 Sec 7-1 |
| 4 | 15 | Connecting Deployed Model to Ontology: Actions That Invoke Inference, Write Predictions | 1.25 | LAB | TM-40C Ch 7 Sec 7-2 |
| 4 | 16 | Monitoring Pipeline: Data Drift Detection, Threshold Definition, Alert Routing | 2.0 | LAB | TM-40C Ch 7 Sec 7-3 |
| 4 | 17 | Operational Use Case Patterns: Readiness Prediction, Logistics Forecasting, Anomaly Detection | 1.75 | LAB | TM-40C Ch 8 |
| 5 | 18 | Model Governance: Model Card Completion — Assumptions, Limitations, Responsible AI Declaration | 1.0 | LAB | TM-40C Ch 9 |
| 5 | 19 | Deployment Approval and C2DAO Governance for Deployed Models | 1.0 | BRF | Standards Ch 4 |
| 5 | 20 | Practical Exercise Scenario Brief; Planning Time | 1.5 | BRF | — |
| 5 | 21 | Practical Exercise (Evaluated): Feature Pipeline → Train → Evaluate → Deploy → Monitor → Governance | 4.0 | EVAL | TM-40C Practical Exercise Guide |
| | | **TM-40C Total** | **40.0** | | |

---

### 3-7. TM-40D: Program Manager

**Course length:** 3 days (24 hours)
**Evaluation method:** Practical exercise (7 tasks); PM Dashboard Standards Checklist review; Go/No-Go

| Day | Block | Title | Hours | Method | Reference |
|---|---|---|---|---|---|
| 1 | 1 | Program Data Architecture: Program/Milestone/Resource/Risk Object Types — Design on Paper First | 1.5 | LAB | TM-40D Ch 2 |
| 1 | 2 | Ontology: PM Object Types, Link Types (Program↔Milestone, Program↔Risk), Action Configuration | 1.75 | LAB | TM-40D Ch 2 Sec 2-4 |
| 1 | 3 | Pipeline Builder: IMS Ingestion, DATEDIFF, Milestone Variance, RAG Status, Data-As-Of Timestamp | 2.0 | LAB | TM-40D Ch 3 |
| 1 | 4 | Pipeline Builder: GFEBS Obligation Data in Append Mode; Run Twice, Verify Two Snapshot Records | 2.0 | LAB | TM-40D Ch 4 Sec 4-1 |
| 2 | 5 | Workshop: Milestone Dashboard — RAG Conditional Formatting, Data-As-Of Timestamp Widget | 2.0 | LAB | TM-40D Ch 3 Sec 3-3 |
| 2 | 6 | Quiver: Obligation Rate Chart, Reference Line at Quarterly Target, At-Risk Program Identification | 1.25 | LAB | TM-40D Ch 4 Sec 4-2 |
| 2 | 7 | Contour: Portfolio Health Matrix — Cross-Program Roll-Up, Sort by overall_status Ascending | 2.0 | LAB | TM-40D Ch 5 |
| 2 | 8 | Reporting: Scheduled Pipeline, Build Failure Notification, PDF Snapshot Export | 1.25 | LAB | TM-40D Ch 6 |
| 2 | 9 | PM Dashboard Standards Checklist Walk-Through: Every Item, Common Failures | 0.5 | DIS | TM-40D Appendix A |
| 3 | 10 | Supervised Practice Run (Ungraded): Full Stack from Different Provided Dataset | 3.25 | LAB | TM-40D All Chapters |
| 3 | 11 | Practical Exercise (Evaluated) | 4.0 | EVAL | TM-40D Practical Exercise Guide |
| | | **TM-40D Total** | **24.0** | | |

---

### 3-8. TM-40E: Knowledge Manager

**Course length:** 3 days (24 hours)
**Evaluation method:** Practical exercise (6 tasks); PCS package instructor review (Day 3); Go/No-Go

| Day | Block | Title | Hours | Method | Reference |
|---|---|---|---|---|---|
| 1 | 1 | KM Role on MSS; Knowledge Architecture Methodology; Why KM Systems Fail | 1.0 | BRF | TM-40E Ch 1 |
| 1 | 2 | Ontology: Knowledge Object Types — Document, Lesson, AAR, SOP, ExpertiseProfile | 2.0 | LAB | TM-40E Ch 2 |
| 1 | 3 | Workshop: AAR Submission Form — Required-Field Validation, Submission Confirmation | 0.75 | LAB | TM-40E Ch 3 Sec 3-2 |
| 1 | 4 | Lessons Learned Pipeline: Intake, Deduplication, Tagging Taxonomy, Distribution Routing | 2.0 | LAB | TM-40E Ch 4 |
| 1 | 5 | AIP Logic: Document Summarization; Human Review Queue — All AIP Outputs Begin as Draft | 1.75 | LAB | TM-40E Ch 5 Sec 5-1 |
| 2 | 6 | Workshop: Knowledge Browser — Search, Filter by Tag/Unit/Date, Drill-Down | 2.0 | LAB | TM-40E Ch 5 Sec 5-4 |
| 2 | 7 | SOP/Doctrine Version Control: Lifecycle, Version Tagging, Review Notification Workflow | 1.25 | LAB | TM-40E Ch 7 Sec 7-6 |
| 2 | 8 | Personnel Expertise Mapping: ExpertiseProfile, Skills Taxonomy, Privacy Act Authorities | 1.0 | LAB | TM-40E Ch 8 Sec 8-1 |
| 2 | 9 | PCS Knowledge Transfer: Key Person Dependency Analysis, Transfer Package Design | 1.25 | LAB | TM-40E Ch 9 |
| 2 | 10 | AIP Prompt Iteration Lab: Test 5 Documents, Score Extraction, Revise, Retest | 1.5 | LAB | TM-40E Sec 5-3 |
| 3 | 11 | PCS Package Draft Review: Each Trainee Presents; Instructor Reviews; Trainees Revise | 2.25 | WKS | TM-40E Ch 9 |
| 3 | 12 | Practical Exercise Scenario Brief | 0.75 | BRF | — |
| 3 | 13 | Practical Exercise (Evaluated) | 4.0 | EVAL | TM-40E Practical Exercise Guide |
| | | **TM-40E Total** | **24.0** | | |

---

### 3-9. TM-40F: Software Engineer

**Course length:** 5 days (40 hours)
**Evaluation method:** Practical exercise (6 tasks); validator test suite (8 test cases); deployment checklist review; Go/No-Go

| Day | Block | Title | Hours | Method | Reference |
|---|---|---|---|---|---|
| 1 | 1 | SWE Role on MSS; 5-Layer Data Stack; OSDK Architecture vs. Standard REST | 1.0 | LEC | TM-40F Ch 1 |
| 1 | 2 | OSDK Setup: Auth Architecture, Client Init, Token Handling, First Object Query | 2.0 | LAB | TM-40F Ch 2 Sec 2-1 |
| 1 | 3 | OSDK: Filtering and Sorting — Query Predicates, Sort Expressions, Field Selection | 0.75 | LAB | TM-40F Ch 2 Sec 2-2 |
| 1 | 4 | OSDK: Pagination — ResourceIterator, Iterating All Pages, Multi-Page Result Sets | 2.0 | LAB | TM-40F Ch 2 Sec 2-3 |
| 1 | 5 | OSDK: Link Traversal — Querying Related Objects Across Link Types | 1.75 | LAB | TM-40F Ch 2 Sec 2-4 |
| 2 | 6 | OSDK: Action Execution — Async Response, Task ID Polling for Completion | 2.0 | LAB | TM-40F Ch 3 Sec 3-1 |
| 2 | 7 | OSDK: Error Handling and Retry — Action Failures, Timeout, Structured Error Response | 1.25 | LAB | TM-40F Ch 3 Sec 3-2 |
| 2 | 8 | OSDK: Object Subscriptions — Real-Time Change Notifications via WebSocket | 2.0 | LAB | TM-40F Ch 3 Sec 3-3 |
| 2 | 9 | OSDK: Bulk Operations — Batch Queries, Bulk Action Submissions; Avoid Per-Object Loops | 1.75 | LAB | TM-40F Ch 3 Sec 3-4 |
| 3 | 10 | Platform SDK: Dataset Read Operations, Write Transactions, File Resources, Branch Management | 2.0 | LAB | TM-40F Ch 4 Sec 4-1 |
| 3 | 11 | Platform SDK Exercise: Build Dataset Integration Using Read/Write Transaction Pattern | 1.25 | LAB | TM-40F Ch 4 Sec 4-2 |
| 3 | 12 | TypeScript FOO: Repository Structure, Computed Property Implementation, Function Registration | 2.0 | LAB | TM-40F Ch 5 Sec 5-1 |
| 3 | 13 | FOO: Bulk Query Patterns — Avoiding N+1 Queries; Test with 200+ Object Set | 1.75 | LAB | TM-40F Ch 5 Sec 5-2 |
| 4 | 14 | TypeScript Action Validators: Multi-Condition, Cross-Field Logic, Error Message Standards | 2.0 | LAB | TM-40F Ch 6 Sec 6-1 |
| 4 | 15 | Validator Testing: Test Suite — 4 Valid, 4 Invalid; Each Paired with Expected Error Message | 1.25 | LAB | TM-40F Ch 6 Sec 6-2 |
| 4 | 16 | Slate Applications: Structure, Foundry API Integration, Widget Binding, Initial Data Load | 2.0 | LAB | TM-40F Ch 7 Sec 7-1 |
| 4 | 17 | Slate: State Management on Action Completion; Error State Display for Failed Actions | 1.75 | LAB | TM-40F Ch 7 Sec 7-2 |
| 5 | 18 | CI/CD: Repository Discipline, PR Workflow, Automated Testing, C2DAO Deployment Checklist | 1.0 | LEC | TM-40F Ch 8 |
| 5 | 19 | Security and Compliance: Token Handling, Input Sanitization, OPSEC for App Code | 1.0 | LEC | TM-40F Ch 9 |
| 5 | 20 | Practical Exercise Scenario Brief; Planning Time | 1.5 | BRF | — |
| 5 | 21 | Practical Exercise (Evaluated): OSDK → Validator → Slate UI → Deployment Checklist | 4.0 | EVAL | TM-40F Practical Exercise Guide |
| | | **TM-40F Total** | **40.0** | | |

---

## CHAPTER 4 — TRAINING RESOURCES

### 4-1. Instructor Requirements

| Course | Minimum Instructor Qualification | T:I Ratio |
|---|---|---|
| TM-10 | MSS Builder certified (TM-20 Go on file); familiarity with Foundry platform | 10:1 |
| TM-20 | TM-30 certified; 6+ months Foundry build experience; able to troubleshoot all TM-20 labs | 8:1 |
| TM-30 | TM-40 level (any track) or equivalent technical proficiency; able to conduct design critiques | 6:1 |
| TM-40A | FA49 or equivalent ORSA background; TM-40A certified or C2DAO SME designation | 4:1 |
| TM-40B | AIP Logic authoring experience; C2DAO AI SME designation; TM-40B certified | 4:1 |
| TM-40C | ML production experience; TM-40C certified; C2DAO MLE SME designation | 4:1 |
| TM-40D | Program management background; TM-30 certified; GFEBS/IMS proficiency | 6:1 |
| TM-40E | Knowledge management background; TM-30 certified; AIP Logic configuration proficiency | 6:1 |
| TM-40F | Software engineering background; OSDK/Platform SDK proficiency; TM-40F certified | 4:1 |

### 4-2. Training Environment Requirements

| Course | Access Level Required | Provisioning Lead Time |
|---|---|---|
| TM-10 | MSS Viewer (standard) | 5 duty days |
| TM-20 | MSS Builder | 5 duty days |
| TM-30 | MSS Editor + AIP Logic configuration | 7 duty days |
| TM-40A | Code Workspace (CPU or GPU) + standard Editor | 7–10 duty days |
| TM-40B | AIP Logic authoring + Agent Studio | 7–10 duty days |
| TM-40C | GPU-enabled Code Workspace | 10+ duty days |
| TM-40D | MSS Builder | 5 duty days |
| TM-40E | MSS Builder + AIP Logic configuration | 5–7 duty days |
| TM-40F | OSDK developer access + developer token | 10+ duty days |

### 4-3. Training Aids and Materials

- Instructor presentation slides (per lesson plan)
- Training datasets (synthetic, stored in MSS Training Environment)
- Practical exercise scenario packages (printed + digital; prepared by instructor prior to course)
- TM reference materials (each trainee receives digital copy before Day 1)
- PM Dashboard Standards Checklist, ORSA Product Standards Checklist, C2DAO Deployment Checklist (printed)

---

## CHAPTER 5 — EVALUATION STANDARDS

### 5-1. Go/No-Go Standards

Each course concludes with a practical exercise evaluated against Go/No-Go criteria specified in the course syllabus. Go requires:

1. All critical tasks completed independently (no instructor assistance, no hints)
2. All hard No-Go items passed (see 5-2 below)
3. Minimum task threshold met (see course syllabus)

### 5-2. Hard No-Go Items (Automatic Failure)

These items result in automatic No-Go regardless of performance on other tasks:

| Course | Hard No-Go Item |
|---|---|
| TM-10 | Incorrect classification marking or export procedure |
| TM-20 | Viewer-role test account can trigger Action or modify data |
| TM-30 | Fatally-flawed Ontology design not corrected before build; promotion submitted without description |
| TM-40B | Any AIP workflow writes to production Objects without human checkpoint |
| TM-40C | Model calibration not performed; governance document missing required sections |
| TM-40D | Dashboard has no data-as-of timestamp |
| TM-40E | AIP workflow auto-publishes without human review gate |
| TM-40F | Hardcoded credential in application code; validator test suite not fully passing |

### 5-3. No-Go Remediation

A trainee who receives No-Go must:

1. Receive a documented counseling within 1 duty day (DA Form 4856 or equivalent)
2. Conduct remediation training on the failed tasks — minimum 4 hours for TM-10/20/40D/40E; minimum 8 hours for TM-30/40A/40B/40C/40F
3. Be re-evaluated within 10 duty days
4. A trainee who receives No-Go on the second attempt requires C2DAO approval before a third evaluation

All remediation events are documented on the Individual Training Record.

### 5-4. Course Completion Documentation

Upon successful completion (Go):

1. Instructor updates the Unit Training Status Matrix (Appendix A of MTP)
2. Trainee's Individual Training Record is annotated with: course, date, evaluator name, Go/No-Go
3. For TM-30 and above: trainee's commander receives a completion notification

---

## APPENDIX A — COURSE HOURS SUMMARY MATRIX

| Course | Lecture/Brief | Lab | Discussion/Review | Workshop/Seminar | Evaluation | Total |
|---|---|---|---|---|---|---|
| TM-10 | 1.5 | 5.5 | — | — | 1.0 | 8.0 |
| TM-20 | — | 31.25 | 2.75 | — | 4.0 | 38.0* |
| TM-30 | 1.0 | 26.0 | 1.0 | 4.75 | 4.0 | 36.75* |
| TM-40A | 2.0 | 30.0 | 1.0 | — | 4.0 | 37.0* |
| TM-40B | 3.75 | 28.25 | — | 2.0 | 4.0 | 38.0* |
| TM-40C | 1.0 | 31.0 | — | — | 4.0 | 36.0* |
| TM-40D | 0.5 | 17.75 | 0.5 | — | 4.0 | 22.75* |
| TM-40E | 1.0 | 14.25 | — | 2.25 | 4.0 | 21.5* |
| TM-40F | 2.0 | 30.0 | — | — | 4.0 | 36.0* |

*Remainder of scheduled hours are review periods and scenario briefs not separately categorized above.

---

## APPENDIX B — AMENDMENT RECORD

| Amendment | Date | Description | Approved By |
|---|---|---|---|
| Initial Publication | March 2026 | Initial POI for MSS Training Program | C2DAO |
| | | | |

---

*USAREUR-AF Operational Data Team — UNCLASSIFIED*
*POI MSS-POI-001 | Version 1.0 | March 2026*
