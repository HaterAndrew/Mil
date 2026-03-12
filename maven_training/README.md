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
| Developers / technical specialists | Writing code, building external apps, ML models | TM-40 (track) after TM-30 |
| Senior leaders (O-5+, CSM+) | Commanding or directing a data-capable formation | Data Literacy for Senior Leaders |
| All — background reading | Anyone who wants to understand data concepts before touching MSS | Data Literacy Technical Reference |

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
                                                │
                                                ▼
Data-Adjacent Specialists ───────────────► TM-30 (Advanced Builder)
                                                │
                                    ┌───────────┴────────────┐
                                    ▼                        ▼
                         TM-40A (ORSA)
                         TM-40B (AI Eng)
                         TM-40C (MLE)
                         TM-40D (PM)
                         TM-40E (KM)
                         TM-40F (SWE)
                                    │
                                    ▼
                         TM-50 series (advanced, per track)
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

### TM-40 Series — Technical Specialist Tracks

Each TM-40 track includes a companion **Concepts Guide** covering background theory and doctrine context for that specialty.

| Publication | File | Concepts Guide | Audience | Prerequisite |
|-------------|------|----------------|----------|--------------|
| **TM-40A** — ORSA | [tm/TM_40A_orsa/TM_40A_ORSA.md](tm/TM_40A_orsa/TM_40A_ORSA.md) | [CONCEPTS_GUIDE_TM40A](tm/TM_40A_orsa/CONCEPTS_GUIDE_TM40A_ORSA.md) | Operations Research analysts | TM-30 |
| **TM-40B** — AI Engineer | [tm/TM_40B_ai_engineer/TM_40B_AI_ENGINEER.md](tm/TM_40B_ai_engineer/TM_40B_AI_ENGINEER.md) | [CONCEPTS_GUIDE_TM40B](tm/TM_40B_ai_engineer/CONCEPTS_GUIDE_TM40B_AI_ENGINEER.md) | AI/ML specialists | TM-30 |
| **TM-40C** — Machine Learning Engineer | [tm/TM_40C_ml_engineer/TM_40C_ML_ENGINEER.md](tm/TM_40C_ml_engineer/TM_40C_ML_ENGINEER.md) | [CONCEPTS_GUIDE_TM40C](tm/TM_40C_ml_engineer/CONCEPTS_GUIDE_TM40C_ML_ENGINEER.md) | MLEs | TM-30 |
| **TM-40D** — Program Manager | [tm/TM_40D_program_manager/TM_40D_PROGRAM_MANAGER.md](tm/TM_40D_program_manager/TM_40D_PROGRAM_MANAGER.md) | [CONCEPTS_GUIDE_TM40D](tm/TM_40D_program_manager/CONCEPTS_GUIDE_TM40D_PROGRAM_MANAGER.md) | PMs, resource managers, G8/S8 | TM-30 |
| **TM-40E** — Knowledge Manager | [tm/TM_40E_knowledge_manager/TM_40E_KNOWLEDGE_MANAGER.md](tm/TM_40E_knowledge_manager/TM_40E_KNOWLEDGE_MANAGER.md) | [CONCEPTS_GUIDE_TM40E](tm/TM_40E_knowledge_manager/CONCEPTS_GUIDE_TM40E_KNOWLEDGE_MANAGER.md) | KMOs, 37F, S2/S3/S6 KM roles | TM-30 |
| **TM-40F** — Software Engineer | [tm/TM_40F_software_engineer/TM_40F_SOFTWARE_ENGINEER.md](tm/TM_40F_software_engineer/TM_40F_SOFTWARE_ENGINEER.md) | [CONCEPTS_GUIDE_TM40F](tm/TM_40F_software_engineer/CONCEPTS_GUIDE_TM40F_SOFTWARE_ENGINEER.md) | SWEs | TM-30 |

### TM-50 Series — Advanced Specialist Tracks

Each TM-50 track includes a companion **Concepts Guide** for advanced theory and doctrine.

| Publication | File | Concepts Guide | Audience | Prerequisite |
|-------------|------|----------------|----------|--------------|
| **TM-50A** — Advanced ORSA | [tm/TM_50A_orsa_advanced/TM_50A_ORSA_ADVANCED.md](tm/TM_50A_orsa_advanced/TM_50A_ORSA_ADVANCED.md) | [CONCEPTS_GUIDE_TM50A](tm/TM_50A_orsa_advanced/CONCEPTS_GUIDE_TM50A_ORSA_ADVANCED.md) | Senior ORSA practitioners | TM-40A |
| **TM-50B** — Advanced AI Engineer | [tm/TM_50B_ai_engineer_advanced/TM_50B_AI_ENGINEER_ADVANCED.md](tm/TM_50B_ai_engineer_advanced/TM_50B_AI_ENGINEER_ADVANCED.md) | [CONCEPTS_GUIDE_TM50B](tm/TM_50B_ai_engineer_advanced/CONCEPTS_GUIDE_TM50B_AI_ENGINEER_ADVANCED.md) | Senior AI engineers | TM-40B |
| **TM-50C** — Advanced MLE | [tm/TM_50C_ml_engineer_advanced/TM_50C_ML_ENGINEER_ADVANCED.md](tm/TM_50C_ml_engineer_advanced/TM_50C_ML_ENGINEER_ADVANCED.md) | [CONCEPTS_GUIDE_TM50C](tm/TM_50C_ml_engineer_advanced/CONCEPTS_GUIDE_TM50C_ML_ENGINEER_ADVANCED.md) | Senior ML engineers | TM-40C |
| **TM-50D** — Advanced Program Manager | [tm/TM_50D_program_manager_advanced/TM_50D_PROGRAM_MANAGER_ADVANCED.md](tm/TM_50D_program_manager_advanced/TM_50D_PROGRAM_MANAGER_ADVANCED.md) | [CONCEPTS_GUIDE_TM50D](tm/TM_50D_program_manager_advanced/CONCEPTS_GUIDE_TM50D_PROGRAM_MANAGER_ADVANCED.md) | Senior tech PMs | TM-40D |
| **TM-50E** — Advanced Knowledge Manager | [tm/TM_50E_knowledge_manager_advanced/TM_50E_KNOWLEDGE_MANAGER_ADVANCED.md](tm/TM_50E_knowledge_manager_advanced/TM_50E_KNOWLEDGE_MANAGER_ADVANCED.md) | [CONCEPTS_GUIDE_TM50E](tm/TM_50E_knowledge_manager_advanced/CONCEPTS_GUIDE_TM50E_KNOWLEDGE_MANAGER_ADVANCED.md) | Senior KMOs | TM-40E |
| **TM-50F** — Advanced Software Engineer | [tm/TM_50F_software_engineer_advanced/TM_50F_SOFTWARE_ENGINEER_ADVANCED.md](tm/TM_50F_software_engineer_advanced/TM_50F_SOFTWARE_ENGINEER_ADVANCED.md) | [CONCEPTS_GUIDE_TM50F](tm/TM_50F_software_engineer_advanced/CONCEPTS_GUIDE_TM50F_SOFTWARE_ENGINEER_ADVANCED.md) | Senior SWEs | TM-40F |

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

### TM-40A — ORSA (-40A Level)
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

### TM-40B — AI Engineer (-40B Level)
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

### TM-40C — Machine Learning Engineer (-40C Level)
**Audience:** ML engineers, data scientists building and deploying models on MSS
**Competencies upon completion:**
- Configure Code Workspaces for model development (GPU, packages, environment management)
- Build and evaluate ML models within the Foundry environment
- Manage model versioning, experiment tracking, and reproducibility
- Deploy models to production and integrate with Ontology Objects and Actions
- Implement MLOps patterns: monitoring, drift detection, retraining triggers
- Apply responsible AI practices and model documentation standards for operational use

### TM-40D — Program Manager (Technical) (-40D Level)
**Audience:** Technical project managers leading data, AI, and software capability builds on MSS
**Competencies upon completion:**
- Apply Agile project management (Scrum/Kanban) to data and AI projects
- Write user stories and acceptance criteria for data products
- Manage ML/AI project lifecycles from research through production
- Translate between technical staff and operational users/commanders
- Build sprint tracking and project status dashboards on MSS
- Manage technical risk, dependencies, and delivery planning
- Define production readiness and Definition of Done for data products
- Lead change management and user adoption for new MSS capabilities

### TM-40E — Knowledge Manager (-40E Level)
**Audience:** KMOs, 37F, S2/S3/S6 knowledge management roles, unit S3/S6 knowledge officers
**Competencies upon completion:**
- Design knowledge architecture for AAR, lessons learned, doctrine, and SOP repositories on MSS
- Build AAR capture systems using Workshop forms and Object Type pipelines
- Design and operate lessons-learned ingestion and tagging pipelines
- Use AIP Logic for knowledge summarization, search augmentation, and theme extraction
- Build full-text and semantic search systems over knowledge repositories
- Manage doctrine and SOP version control within Foundry
- Build personnel expertise mapping (skills/experience registries)
- Design knowledge transfer and unit continuity processes using MSS

### TM-40F — Software Engineer (-40F Level)
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
| **TM-40 Specialist Lesson Plan Outlines** | [training_management/lesson_plans/TM40_SPECIALIST_LESSON_PLAN_OUTLINES.md](training_management/lesson_plans/TM40_SPECIALIST_LESSON_PLAN_OUTLINES.md) | All six TM-40 tracks |

### Course Syllabi (Student/Instructor-Facing)

Hand the appropriate syllabus to each trainee at the start of their course.

| Syllabus | File | Level |
|----------|------|-------|
| TM-10 — Maven User | [syllabi/SYLLABUS_TM10.md](syllabi/SYLLABUS_TM10.md) | All personnel |
| TM-20 — Builder | [syllabi/SYLLABUS_TM20.md](syllabi/SYLLABUS_TM20.md) | All staff |
| TM-30 — Advanced Builder | [syllabi/SYLLABUS_TM30.md](syllabi/SYLLABUS_TM30.md) | Data-adjacent specialists |
| TM-40A — ORSA | [syllabi/SYLLABUS_TM40A.md](syllabi/SYLLABUS_TM40A.md) | ORSA analysts |
| TM-40B — AI Engineer | [syllabi/SYLLABUS_TM40B.md](syllabi/SYLLABUS_TM40B.md) | AI/ML specialists |
| TM-40C — ML Engineer | [syllabi/SYLLABUS_TM40C.md](syllabi/SYLLABUS_TM40C.md) | MLEs |
| TM-40D — Program Manager | [syllabi/SYLLABUS_TM40D.md](syllabi/SYLLABUS_TM40D.md) | PMs, G8/S8 |
| TM-40E — Knowledge Manager | [syllabi/SYLLABUS_TM40E.md](syllabi/SYLLABUS_TM40E.md) | KMOs, 37F |
| TM-40F — Software Engineer | [syllabi/SYLLABUS_TM40F.md](syllabi/SYLLABUS_TM40F.md) | SWEs |

> **Note:** TM-50 series syllabi are not yet published. Advanced track instruction is managed through the MTP and TEO. Contact training management for TM-50 course scheduling.

---

## Supporting Reference Material

| Resource | Location | Notes |
|----------|----------|-------|
| **MSS Quick Start** | [QUICK_START.md](QUICK_START.md) | 30-minute onboarding for new MSS users |
| **Naming & Governance Standards** | [standards/NAMING_AND_GOVERNANCE_STANDARDS.md](standards/NAMING_AND_GOVERNANCE_STANDARDS.md) | USAREUR-AF MSS naming conventions, governance checklists |
| **MSS Training Hub (web)** | [mss_info_app/index.html](mss_info_app/index.html) | Standalone HTML training hub — open in browser |
| **Practical Exercises** | [exercises/](exercises/) | Hands-on exercise packages for TM-10 through TM-40F |
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
6. If data specialist: complete [TM-30](tm/TM_30_advanced_builder/TM_30_ADVANCED_BUILDER.md) after TM-20
7. If in a specialized role: proceed to the appropriate TM-40 track (see table above)

### For an S6 shop standing up MSS capability:
1. Commander reads Data Literacy for Senior Leaders
2. All staff complete TM-10
3. Designate builders: complete TM-20
4. Designate data leads: complete TM-30
5. Reference Glossary throughout
6. Technical specialists proceed to TM-40 tracks per role assignment

### By MOS/Role — TM-40 Track Selection:

| Role / MOS | Recommended TM-40 Track |
|---|---|
| 17A/17C — Cyber officer/NCO | TM-40F (SWE) or TM-40B (AI Eng) |
| 25D — IT specialist | TM-40F (SWE) |
| 25U — Signal support | TM-40F (SWE) or TM-40D (PM) |
| FA49 — Operations Research | TM-40A (ORSA) |
| 37F — Psychological Operations | TM-40E (KM) |
| G2/S2 analyst | TM-40A (ORSA) or TM-40E (KM) |
| G6/S6 data officer | TM-40F (SWE) or TM-40B (AI Eng) |
| G8/S8 resource manager | TM-40D (PM) |
| G9/Civil Affairs | TM-40D (PM) or TM-40E (KM) |
| Data scientist (GS/contractor) | TM-40A (ORSA) or TM-40C (MLE) |
| AI/ML engineer (GS/contractor) | TM-40B (AI Eng) or TM-40C (MLE) |
| KMO / Knowledge Officer | TM-40E (KM) |
| PM / Program Manager | TM-40D (PM) |

---

*USAREUR-AF Operational Data Team — UNCLASSIFIED*
*Version 4.0 | March 2026 | TM-40 and TM-50 series complete | Supersedes previous MAVEN_FIELD_MANUAL.md*
