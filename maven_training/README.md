# Maven Smart System (MSS) — Training Curriculum
## USAREUR-AF Operational Data Team

```
HEADQUARTERS
UNITED STATES ARMY EUROPE AND AFRICA
Wiesbaden, Germany
```

**Distribution:** Approved for public release; distribution is unlimited.

---

## Purpose

This curriculum provides progressive, doctrine-aligned training for all USAREUR-AF personnel who access, build on, or lead with the Maven Smart System (MSS). It is organized into foundational doctrine publications and platform-specific technical manuals following Army publication conventions.

---

## New Here? Start Fast

**[MSS Quick Start](QUICK_START.md)** — Get operational in 30 minutes. Read this before anything else if you just got MSS access.

---

## How to Use This Curriculum

### Step 1 — Know Your Level

| Level | You Are... | Start Here |
|-------|-----------|------------|
| All personnel | A Soldier, officer, or civilian who uses MSS to access operational data | TM-10 |
| All staff, light builders | Building dashboards, forms, or basic pipelines on MSS | TM-20 (after TM-10) |
| Data-adjacent specialists | Assigned to a data/analytical role (17/25-series, S6/G6, G2/G9) | TM-30 (after TM-20) |
| Warfighting function staff | Assigned to INT, FIRES, M2, SUST, PROTECTION, or MC functions | TM-40A through TM-40F (WFF track) |
| Developers / technical specialists | Writing code, building external apps, ML models | TM-40G through TM-40L (technical track) after TM-30 |
| Senior leaders (O-5+, CSM+) | Commanding or directing a data-capable formation | Data Literacy for Senior Leaders |
| All — background reading | Anyone who wants to understand data concepts before touching MSS | Data Literacy Technical Reference |

> **TM-40 Series Disambiguation:** The TM-40 series has two distinct sub-series:
> - **TM-40A through TM-40F** — Warfighting Function (WFF) tracks. Audience: functional staff in the six WFFs. Prerequisite: TM-20. These address how each WFF integrates MSS into its operational domain.
> - **TM-40G through TM-40L** — Technical Specialist tracks. Audience: engineers, analysts, and data professionals writing code or building models. Prerequisite: TM-30. These address platform development and advanced technical capabilities.
>
> Do not assume a track based on letter alone — confirm against your role and the tables below.

### Step 2 — Read the Right Publications

```
Senior Leaders ──────────────────────────► Data Literacy for Senior Leaders
                                                │
                                                ▼
All Personnel ───────────────────────────► Data Literacy Technical Reference [recommended]
                                                │
                                                ▼
All Personnel ───────────────────────────► TM-10 (Maven User)
                                                │
                                                ▼
All Staff ───────────────────────────────► TM-20 (Builder)
                                           │            │
                              ┌────────────┘            └────────────┐
                              ▼                                      ▼
                   WFF Staff (TM-40A–F)              Data-Adjacent Specialists
                   ─────────────────────             ──────────────────────────
                   TM-40A (Intelligence)             TM-30 (Advanced Builder)
                   TM-40B (Fires)                          │
                   TM-40C (M2)                   ┌─────────┴─────────┐
                   TM-40D (Sustainment)           ▼                   ▼
                   TM-40E (Protection)    TM-40G through TM-40L   TM-50 Series
                   TM-40F (Mission Cmd)   (Technical Specialists)  (Advanced)
```

### Step 3 — Reference the Glossary

At any point, consult the [Data & Foundry Glossary](doctrine/GLOSSARY_data_foundry.md) to translate between general data concepts and MSS/Foundry terminology.

---

## Publications Index

### Doctrine Publications

| Publication | File | Audience | Purpose |
|-------------|------|----------|---------|
| **Data Literacy for Senior Leaders** | [doctrine/DATA_LITERACY_senior_leaders.md](doctrine/DATA_LITERACY_senior_leaders.md) | O-5+, CSM+, Senior Civilians | Principles, command responsibilities, evaluating data products |
| **Data Literacy Technical Reference** | [doctrine/DATA_LITERACY_technical_reference.md](doctrine/DATA_LITERACY_technical_reference.md) | All personnel | Comprehensive data literacy reference — platform-agnostic |
| **Glossary** — Data & Foundry Terms | [doctrine/GLOSSARY_data_foundry.md](doctrine/GLOSSARY_data_foundry.md) | All personnel | Equates general data concepts to MSS/Foundry terminology |

### Technical Manuals (Platform-Specific)

| Publication | File | Audience | Prerequisite |
|-------------|------|----------|--------------|
| **TM-10** — Maven User | [tm/TM_10_maven_user/TM_10_MAVEN_USER.md](tm/TM_10_maven_user/TM_10_MAVEN_USER.md) | All staff | None |
| **TM-20** — Builder | [tm/TM_20_builder/TM_20_BUILDER.md](tm/TM_20_builder/TM_20_BUILDER.md) | All staff | TM-10 |
| **TM-30** — Advanced Builder | [tm/TM_30_advanced_builder/TM_30_ADVANCED_BUILDER.md](tm/TM_30_advanced_builder/TM_30_ADVANCED_BUILDER.md) | Data-adjacent specialists | TM-10, TM-20 |

### TM-40A through TM-40F — Warfighting Function Tracks

These tracks address MSS integration within each warfighting function. Audience is functional staff assigned to that WFF. Prerequisite: TM-20.

| Publication | File | Concepts Guide | WFF | Prerequisite |
|-------------|------|----------------|-----|--------------|
| **TM-40A** — Intelligence | [tm/TM_40A_intelligence/TM_40A_INTELLIGENCE.md](tm/TM_40A_intelligence/TM_40A_INTELLIGENCE.md) | [CONCEPTS_GUIDE_TM40A](tm/TM_40A_intelligence/CONCEPTS_GUIDE_TM40A_INTELLIGENCE.md) | Intelligence (INT) | TM-20 |
| **TM-40B** — Fires | [tm/TM_40B_fires/TM_40B_FIRES.md](tm/TM_40B_fires/TM_40B_FIRES.md) | [CONCEPTS_GUIDE_TM40B](tm/TM_40B_fires/CONCEPTS_GUIDE_TM40B_FIRES.md) | Fires | TM-20 |
| **TM-40C** — Movement & Maneuver | [tm/TM_40C_movement_maneuver/TM_40C_MOVEMENT_MANEUVER.md](tm/TM_40C_movement_maneuver/TM_40C_MOVEMENT_MANEUVER.md) | [CONCEPTS_GUIDE_TM40C](tm/TM_40C_movement_maneuver/CONCEPTS_GUIDE_TM40C_MOVEMENT_MANEUVER.md) | Movement & Maneuver (M2) | TM-20 |
| **TM-40D** — Sustainment | [tm/TM_40D_sustainment/TM_40D_SUSTAINMENT.md](tm/TM_40D_sustainment/TM_40D_SUSTAINMENT.md) | [CONCEPTS_GUIDE_TM40D](tm/TM_40D_sustainment/CONCEPTS_GUIDE_TM40D_SUSTAINMENT.md) | Sustainment | TM-20 |
| **TM-40E** — Protection | [tm/TM_40E_protection/TM_40E_PROTECTION.md](tm/TM_40E_protection/TM_40E_PROTECTION.md) | [CONCEPTS_GUIDE_TM40E](tm/TM_40E_protection/CONCEPTS_GUIDE_TM40E_PROTECTION.md) | Protection | TM-20 |
| **TM-40F** — Mission Command | [tm/TM_40F_mission_command/TM_40F_MISSION_COMMAND.md](tm/TM_40F_mission_command/TM_40F_MISSION_COMMAND.md) | [CONCEPTS_GUIDE_TM40F](tm/TM_40F_mission_command/CONCEPTS_GUIDE_TM40F_MISSION_COMMAND.md) | Mission Command (MC) | TM-20 |

### TM-40G through TM-40L — Technical Specialist Tracks

These tracks address advanced technical capabilities by specialty. Each includes a companion **Concepts Guide** covering background theory and doctrine context. Prerequisite: TM-30.

| Publication | File | Concepts Guide | Audience | Prerequisite |
|-------------|------|----------------|----------|--------------|
| **TM-40G** — ORSA | [tm/TM_40G_orsa/TM_40G_ORSA.md](tm/TM_40G_orsa/TM_40G_ORSA.md) | [CONCEPTS_GUIDE_TM40G](tm/TM_40G_orsa/CONCEPTS_GUIDE_TM40G_ORSA.md) | Operations Research analysts | TM-30 |
| **TM-40H** — AI Engineer | [tm/TM_40H_ai_engineer/TM_40H_AI_ENGINEER.md](tm/TM_40H_ai_engineer/TM_40H_AI_ENGINEER.md) | [CONCEPTS_GUIDE_TM40H](tm/TM_40H_ai_engineer/CONCEPTS_GUIDE_TM40H_AI_ENGINEER.md) | AI/ML specialists | TM-30 |
| **TM-40I** — Machine Learning Engineer | [tm/TM_40I_ml_engineer/TM_40I_ML_ENGINEER.md](tm/TM_40I_ml_engineer/TM_40I_ML_ENGINEER.md) | [CONCEPTS_GUIDE_TM40I](tm/TM_40I_ml_engineer/CONCEPTS_GUIDE_TM40I_ML_ENGINEER.md) | MLEs | TM-30 |
| **TM-40J** — Program Manager | [tm/TM_40J_program_manager/TM_40J_PROGRAM_MANAGER.md](tm/TM_40J_program_manager/TM_40J_PROGRAM_MANAGER.md) | [CONCEPTS_GUIDE_TM40J](tm/TM_40J_program_manager/CONCEPTS_GUIDE_TM40J_PROGRAM_MANAGER.md) | PMs, resource managers, G8/S8 | TM-30 |
| **TM-40K** — Knowledge Manager | [tm/TM_40K_knowledge_manager/TM_40K_KNOWLEDGE_MANAGER.md](tm/TM_40K_knowledge_manager/TM_40K_KNOWLEDGE_MANAGER.md) | [CONCEPTS_GUIDE_TM40K](tm/TM_40K_knowledge_manager/CONCEPTS_GUIDE_TM40K_KNOWLEDGE_MANAGER.md) | KMOs, 37F, S2/S3/S6 KM roles | TM-30 |
| **TM-40L** — Software Engineer | [tm/TM_40L_software_engineer/TM_40L_SOFTWARE_ENGINEER.md](tm/TM_40L_software_engineer/TM_40L_SOFTWARE_ENGINEER.md) | [CONCEPTS_GUIDE_TM40L](tm/TM_40L_software_engineer/CONCEPTS_GUIDE_TM40L_SOFTWARE_ENGINEER.md) | SWEs | TM-30 |

### TM-50 Series — Advanced Technical Specialist Tracks

Each TM-50 track builds directly on its TM-40G–L counterpart. Prerequisite is the corresponding TM-40G–L track.

| Publication | File | Concepts Guide | Audience | Prerequisite |
|-------------|------|----------------|----------|--------------|
| **TM-50G** — Advanced ORSA | [tm/TM_50G_orsa_advanced/TM_50G_ORSA_ADVANCED.md](tm/TM_50G_orsa_advanced/TM_50G_ORSA_ADVANCED.md) | [CONCEPTS_GUIDE_TM50G](tm/TM_50G_orsa_advanced/CONCEPTS_GUIDE_TM50G_ORSA_ADVANCED.md) | Senior ORSA practitioners | TM-40G |
| **TM-50H** — Advanced AI Engineer | [tm/TM_50H_ai_engineer_advanced/TM_50H_AI_ENGINEER_ADVANCED.md](tm/TM_50H_ai_engineer_advanced/TM_50H_AI_ENGINEER_ADVANCED.md) | [CONCEPTS_GUIDE_TM50H](tm/TM_50H_ai_engineer_advanced/CONCEPTS_GUIDE_TM50H_AI_ENGINEER_ADVANCED.md) | Senior AI engineers | TM-40H |
| **TM-50I** — Advanced MLE | [tm/TM_50I_ml_engineer_advanced/TM_50I_ML_ENGINEER_ADVANCED.md](tm/TM_50I_ml_engineer_advanced/TM_50I_ML_ENGINEER_ADVANCED.md) | [CONCEPTS_GUIDE_TM50I](tm/TM_50I_ml_engineer_advanced/CONCEPTS_GUIDE_TM50I_ML_ENGINEER_ADVANCED.md) | Senior ML engineers | TM-40I |
| **TM-50J** — Advanced Program Manager | [tm/TM_50J_program_manager_advanced/TM_50J_PROGRAM_MANAGER_ADVANCED.md](tm/TM_50J_program_manager_advanced/TM_50J_PROGRAM_MANAGER_ADVANCED.md) | [CONCEPTS_GUIDE_TM50J](tm/TM_50J_program_manager_advanced/CONCEPTS_GUIDE_TM50J_PROGRAM_MANAGER_ADVANCED.md) | Senior tech PMs | TM-40J |
| **TM-50K** — Advanced Knowledge Manager | [tm/TM_50K_knowledge_manager_advanced/TM_50K_KNOWLEDGE_MANAGER_ADVANCED.md](tm/TM_50K_knowledge_manager_advanced/TM_50K_KNOWLEDGE_MANAGER_ADVANCED.md) | [CONCEPTS_GUIDE_TM50K](tm/TM_50K_knowledge_manager_advanced/CONCEPTS_GUIDE_TM50K_KNOWLEDGE_MANAGER_ADVANCED.md) | Senior KMOs | TM-40K |
| **TM-50L** — Advanced Software Engineer | [tm/TM_50L_software_engineer_advanced/TM_50L_SOFTWARE_ENGINEER_ADVANCED.md](tm/TM_50L_software_engineer_advanced/TM_50L_SOFTWARE_ENGINEER_ADVANCED.md) | [CONCEPTS_GUIDE_TM50L](tm/TM_50L_software_engineer_advanced/CONCEPTS_GUIDE_TM50L_SOFTWARE_ENGINEER_ADVANCED.md) | Senior SWEs | TM-40L |

---

## Training Level Descriptions

### TM-10 — Maven User (-10 Level)
**Audience:** All personnel
**Competencies upon completion:**
- Access MSS via CAC-based login
- Navigate projects, datasets, and applications
- Use Workshop applications to consume data and submit forms
- Execute authorized Actions
- Use Contour and Quiver for basic no-code analysis
- Interact with AIP Logic and Agent interfaces
- Understand classification markings and authorized export procedures
- Troubleshoot common access and application issues

### TM-20 — Builder (-20 Level)
**Audience:** All staff
**Competencies upon completion:**
- Create and organize Foundry projects via UI
- Ingest data using Pipeline Builder (visual, no code)
- Create basic Object Types and Link Types via Ontology Manager UI
- Create simple Actions via Action Editor UI
- Build and publish Workshop applications with dashboards, forms, and filters
- Manage project access and permissions via UI
- Use Foundry branching to build and promote via UI
- Follow USAREUR-AF naming conventions and builder standards

### TM-30 — Advanced Builder (-30 Level)
**Audience:** Data-adjacent specialists (17/25-series, S6/G6, G2/G9, operational data analysts)
**Competencies upon completion:**
- Design and build complex multi-page Workshop applications with conditional logic and variable passing
- Build advanced Pipeline Builder pipelines with multi-source joins and aggregations (visual)
- Design Ontology structures (Object Types, Link Types, Actions) using the UI — architecture thinking, not coding
- Conduct advanced analysis in Contour (complex aggregations, pivots, calculated columns, saved views)
- Build advanced Quiver dashboards with multi-object analysis and linked views
- Configure AIP Logic workflows (not author them)
- Review and interpret data lineage graphs
- Manage governance workflows with Data Stewards
- Manage branching and production promotion via UI
- Apply USAREUR-AF C2DAO governance standards and naming conventions

### TM-40A through TM-40F — Warfighting Function Tracks

Each WFF track teaches how MSS capabilities are applied within that function's operational and analytical workflows. Prerequisite: TM-20 (not TM-30; these are functional user tracks, not coding tracks).

**TM-40A — Intelligence:** INT staff using MSS for collection management, targeting, and all-source analysis workflows.

**TM-40B — Fires:** Fires personnel using MSS for targeting data, effects assessment, and fire support coordination.

**TM-40C — Movement & Maneuver:** M2 staff using MSS for maneuver tracking, route analysis, and operational visualization.

**TM-40D — Sustainment:** G4/S4 and sustainment staff using MSS for logistics visibility, supply chain analytics, and readiness tracking.

**TM-40E — Protection:** Force protection and CBRN staff using MSS for threat tracking, vulnerability assessment, and protection COA support.

**TM-40F — Mission Command:** C2 and MC staff using MSS for operational dashboards, commander's critical information requirements (CCIR), and battle rhythm products.

### TM-40G — ORSA (-40G Level)
**Audience:** Operations Research/Systems Analysis officers and NCOs, quantitative analysts
**Competencies upon completion:**
- Configure Code Workspaces (Python/R) within Foundry
- Build statistical models: regression, classification, and validation for readiness/logistics applications
- Conduct time series forecasting with ARIMA/SARIMA patterns
- Run Monte Carlo simulation for COA comparison and risk quantification
- Apply linear programming for resource allocation and scheduling optimization
- Design wargame/exercise data collection architecture and aggregation pipelines
- Build analytical decision support products (Quiver/Contour) to commander standard
- Communicate uncertainty: confidence intervals, sensitivity analysis, briefing standards

### TM-40H — AI Engineer (-40H Level)
**Audience:** AI/ML specialists, data engineers assigned to AI pipeline development
**Competencies upon completion:**
- Author AIP Logic workflows: prompt engineering, chain design, output handling
- Build and configure AIP Agent Studio agents with tools, memory, and orchestration
- Implement LLM integration patterns: ontology data grounding, RAG, context construction
- Apply AI safety requirements: human-in-the-loop gates, output validation, OPSEC for AI products
- Write Python transforms that prepare data for AI consumption
- Connect AIP Logic workflows to Object Types and Actions
- Test and red-team AI outputs; evaluate quality against defined standards
- Deploy and monitor AIP Logic workflows in production

### TM-40I — Machine Learning Engineer (-40I Level)
**Audience:** ML engineers, data scientists building and deploying models on MSS
**Competencies upon completion:**
- Configure Code Workspaces for model development (GPU, packages, environment management)
- Build and evaluate ML models within the Foundry environment
- Manage model versioning, experiment tracking, and reproducibility
- Deploy models to production and integrate with Ontology Objects and Actions
- Implement MLOps patterns: monitoring, drift detection, retraining triggers
- Apply responsible AI practices and model documentation standards for operational use

### TM-40J — Program Manager (Technical) (-40J Level)
**Audience:** Technical project managers leading data, AI, and software capability builds on MSS

> **NOTE — Prerequisite Variance:** The MTP lists TM-20 as the minimum prerequisite for TM-40J. The TM-40J syllabus lists TM-30. Commanders should route technical PMs who will oversee code-writing teams through TM-30 before TM-40J. PMs overseeing no-code or builder-level teams may proceed directly from TM-20.

**Competencies upon completion:**
- Apply Agile project management (Scrum/Kanban) to data and AI projects
- Write user stories and acceptance criteria for data products
- Manage ML/AI project lifecycles from research through production
- Translate between technical staff and operational users/commanders
- Build sprint tracking and project status dashboards on MSS
- Manage technical risk, dependencies, and delivery planning
- Define production readiness and Definition of Done for data products
- Lead change management and user adoption for new MSS capabilities

### TM-40K — Knowledge Manager (-40K Level)
**Audience:** KMOs, 37F, S2/S3/S6 knowledge management roles, unit S3/S6 knowledge officers

> **NOTE — Prerequisite Variance:** The MTP lists TM-20 as the minimum prerequisite for TM-40K. The TM-40K syllabus lists TM-30. KMOs who will be building ingestion pipelines or AIP Logic workflows should complete TM-30 first. KMOs focused on taxonomy design and governance may proceed from TM-20.

**Competencies upon completion:**
- Design knowledge architecture for AAR, lessons learned, doctrine, and SOP repositories on MSS
- Build AAR capture systems using Workshop forms and Object Type pipelines
- Design and operate lessons-learned ingestion and tagging pipelines
- Use AIP Logic for knowledge summarization, search augmentation, and theme extraction
- Build full-text and semantic search systems over knowledge repositories
- Manage doctrine and SOP version control within Foundry
- Build personnel expertise mapping (skills/experience registries)
- Design knowledge transfer and unit continuity processes using MSS

### TM-40L — Software Engineer (-40L Level)
**Audience:** Software engineers building external applications and platform integrations on MSS
**Competencies upon completion:**
- Authenticate and query the Foundry Ontology via OSDK (TypeScript/Python)
- Execute Actions, subscribe to Object changes, and handle pagination and filtering via OSDK
- Use Foundry Platform SDK for dataset operations, file management, and branch management
- Build TypeScript Functions on Objects (computed properties, bulk query patterns)
- Write and test complex Action validators with TypeScript
- Build Slate applications integrated with the Foundry API
- Apply USAREUR-AF code review and deployment standards for MSS applications

---

## Training Management

### Administrative Publications

| Resource | Location | Audience |
|----------|----------|---------|
| **Mission Training Plan (MTP)** | [training_management/MTP_MSS.md](training_management/MTP_MSS.md) | Training managers, S3/G6, commanders |
| **Program of Instruction (POI)** | [training_management/POI_MSS.md](training_management/POI_MSS.md) | Training managers, curriculum designers |
| **Course Administrative Data (CAD)** | [training_management/CAD_MSS.md](training_management/CAD_MSS.md) | Training administrators |
| **Training and Evaluation Outline (TEO)** | [training_management/TEO_MSS.md](training_management/TEO_MSS.md) | Instructors, evaluators |
| **Annual Training Schedule** | [training_management/ANNUAL_TRAINING_SCHEDULE.md](training_management/ANNUAL_TRAINING_SCHEDULE.md) | Training managers, S3 |
| **Enrollment SOP** | [training_management/ENROLLMENT_SOP.md](training_management/ENROLLMENT_SOP.md) | Training coordinators |
| **Completion Certificate Template** | [training_management/COMPLETION_CERTIFICATE.md](training_management/COMPLETION_CERTIFICATE.md) | Training administrators |
| **Faculty Development Plan** | [training_management/FACULTY_DEVELOPMENT_PLAN.md](training_management/FACULTY_DEVELOPMENT_PLAN.md) | Instructor cadre, S3 |
| **Training Policy Letter** | [training_management/POLICY_LETTER.md](training_management/POLICY_LETTER.md) | Commanders, training managers |
| **Curriculum Maintenance SOP** | [training_management/CURRICULUM_MAINTENANCE_SOP.md](training_management/CURRICULUM_MAINTENANCE_SOP.md) | Curriculum owner, SMEs, instructors |
| **AAR / Feedback Template** | [training_management/AAR_TEMPLATE.md](training_management/AAR_TEMPLATE.md) | Instructors, evaluators |

The MTP provides: TLOs/ELOs per level, individual task lists, Go/No-Go criteria, hour-by-hour blocks of instruction for all levels, training schedule templates, resource requirements, instructor certification standards, practical exercise scenarios (all levels including TM-40), and sustainment requirements.

### Lesson Plans

| Resource | Location | Notes |
|----------|----------|-------|
| **Lesson Plan Template** | [training_management/lesson_plans/LP_TEMPLATE.md](training_management/lesson_plans/LP_TEMPLATE.md) | Blank template for new courses |
| **TM-20 Lesson Plan Outlines** | [training_management/lesson_plans/TM20_LESSON_PLAN_OUTLINES.md](training_management/lesson_plans/TM20_LESSON_PLAN_OUTLINES.md) | Builder track |
| **TM-30 Lesson Plan Outlines** | [training_management/lesson_plans/TM30_LESSON_PLAN_OUTLINES.md](training_management/lesson_plans/TM30_LESSON_PLAN_OUTLINES.md) | Advanced Builder track |
| **TM-40 Specialist Lesson Plan Outlines** | [training_management/lesson_plans/TM40_SPECIALIST_LESSON_PLAN_OUTLINES.md](training_management/lesson_plans/TM40_SPECIALIST_LESSON_PLAN_OUTLINES.md) | TM-40G through TM-40L technical tracks |

### Course Syllabi (Student/Instructor-Facing)

Hand the appropriate syllabus to each trainee at the start of their course.

| Syllabus | File | Level |
|----------|------|-------|
| TM-10 — Maven User | [syllabi/SYLLABUS_TM10.md](syllabi/SYLLABUS_TM10.md) | All personnel |
| TM-20 — Builder | [syllabi/SYLLABUS_TM20.md](syllabi/SYLLABUS_TM20.md) | All staff |
| TM-30 — Advanced Builder | [syllabi/SYLLABUS_TM30.md](syllabi/SYLLABUS_TM30.md) | Data-adjacent specialists |
| TM-40G — ORSA | [syllabi/SYLLABUS_TM40G.md](syllabi/SYLLABUS_TM40G.md) | ORSA analysts |
| TM-40H — AI Engineer | [syllabi/SYLLABUS_TM40H.md](syllabi/SYLLABUS_TM40H.md) | AI/ML specialists |
| TM-40I — ML Engineer | [syllabi/SYLLABUS_TM40I.md](syllabi/SYLLABUS_TM40I.md) | MLEs |
| TM-40J — Program Manager | [syllabi/SYLLABUS_TM40J.md](syllabi/SYLLABUS_TM40J.md) | PMs, G8/S8 |
| TM-40K — Knowledge Manager | [syllabi/SYLLABUS_TM40K.md](syllabi/SYLLABUS_TM40K.md) | KMOs, 37F |
| TM-40L — Software Engineer | [syllabi/SYLLABUS_TM40L.md](syllabi/SYLLABUS_TM40L.md) | SWEs |

> **Note:** WFF track syllabi (TM-40A through TM-40F) and TM-50 series syllabi are not yet published. WFF track instruction is managed through the MTP and TEO. TM-50 advanced track instruction is managed through the MTP. Contact training management for scheduling.

---

## Supporting Reference Material

| Resource | Location | Notes |
|----------|----------|-------|
| **MSS Quick Start** | [QUICK_START.md](QUICK_START.md) | 30-minute onboarding for new MSS users |
| **Naming & Governance Standards** | [standards/NAMING_AND_GOVERNANCE_STANDARDS.md](standards/NAMING_AND_GOVERNANCE_STANDARDS.md) | USAREUR-AF MSS naming conventions, governance checklists |
| **MSS Training Hub (web)** | [mss_info_app/index.html](mss_info_app/index.html) | Standalone HTML training hub — open in browser |
| **Practical Exercises** | [exercises/](exercises/) | Hands-on exercise packages for TM-10 through TM-40L |
| Foundry Python Patterns (runnable code) | [data_skills/13_foundry_patterns/](../data_skills/13_foundry_patterns/) | Local shim for offline development and testing |
| Full data science reference library | [data_skills/](../data_skills/) | 15 modules: Python → ML → ETL → deployment |
| SITREP Tracker (applied project) | [sitrep_tracker/](../sitrep_tracker/) | Click + Rich + SQLite — reference implementation |

---

## Quick-Reference Training Paths

### For a New Soldier joining the data team:
1. Read [Data Literacy for Senior Leaders](doctrine/DATA_LITERACY_senior_leaders.md) if O-5+; skip if not
2. Skim [Data Literacy Technical Reference](doctrine/DATA_LITERACY_technical_reference.md) Ch 1-3 and Ch 8
3. Complete [TM-10](tm/TM_10_maven_user/TM_10_MAVEN_USER.md) cover to cover
4. Request MSS access; practice navigation tasks
5. If building: complete [TM-20](tm/TM_20_builder/TM_20_BUILDER.md)
6. If WFF functional staff: proceed to the appropriate TM-40A–F WFF track after TM-20
7. If data specialist: complete [TM-30](tm/TM_30_advanced_builder/TM_30_ADVANCED_BUILDER.md) after TM-20
8. If technical specialist: proceed to the appropriate TM-40G–L track after TM-30

### For an S6 shop standing up MSS capability:
1. Commander reads Data Literacy for Senior Leaders
2. All staff complete TM-10
3. Designate builders: complete TM-20
4. Designate data leads: complete TM-30
5. Reference Glossary throughout
6. Technical specialists proceed to TM-40G–L tracks per role assignment
7. WFF functional staff proceed to TM-40A–F track per function

### By MOS/Role — TM-40 Track Selection:

| Role / MOS | Recommended TM-40 Track |
|---|---|
| All WFF staff | TM-40A through TM-40F per assigned warfighting function |
| 17A/17C — Cyber officer/NCO | TM-40L (SWE) or TM-40H (AI Eng) |
| 25D — IT specialist | TM-40L (SWE) |
| 25U — Signal support | TM-40L (SWE) or TM-40J (PM) |
| FA49 — Operations Research | TM-40G (ORSA) |
| 37F — Psychological Operations | TM-40K (KM) |
| G2/S2 analyst | TM-40G (ORSA) or TM-40K (KM) |
| G6/S6 data officer | TM-40L (SWE) or TM-40H (AI Eng) |
| G8/S8 resource manager | TM-40J (PM) |
| G9/Civil Affairs | TM-40J (PM) or TM-40K (KM) |
| Data scientist (GS/contractor) | TM-40G (ORSA) or TM-40I (MLE) |
| AI/ML engineer (GS/contractor) | TM-40H (AI Eng) or TM-40I (MLE) |
| KMO / Knowledge Officer | TM-40K (KM) |
| PM / Program Manager | TM-40J (PM) |

---

*USAREUR-AF Operational Data Team — UNCLASSIFIED*
*Version 5.0 | March 2026 | TM-40 WFF and Technical Specialist tracks complete; TM-50 series complete | Supersedes v4.0*
