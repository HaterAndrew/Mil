# Maven Smart System (MSS) — Training Curriculum
## USAREUR-AF Operational Data Team

```
HEADQUARTERS, UNITED STATES ARMY EUROPE AND AFRICA
Wiesbaden, Germany
```

**Distribution:** Distribution authorized to U.S. Government agencies and their contractors only. Other requests must be referred to Headquarters, USAREUR-AF, C2DAO, Wiesbaden, Germany.

---

> **New to MSS?** Read **[QUICK_START.md](QUICK_START.md)** first — operational in 30 minutes.

---

## How to Use This Curriculum

### Step 1 — Know Your Level

| Level | Who You Are | Start Here |
|-------|-------------|------------|
| All personnel | Soldier, officer, or Civilian accessing MSS for data consumption | TM-10 |
| All staff (light builders) | Building dashboards, forms, or basic pipelines | TM-20 (prereq: TM-10) |
| Data-adjacent specialists | 17/25-series, S6/G6, G2, operational data analysts | TM-30 (prereq: TM-20) |
| WFF functional staff | Assigned to INT, FIRES, M2, SUST, PROTECTION, or MC | TM-40A–F (prereq: TM-30) |
| Technical specialists | Writing code, building external apps, ML models | TM-40G–O (prereq: TM-30) |
| Senior leaders (O-5+, CSM+) | Commanding or directing a data-capable formation | Data Literacy for Senior Leaders |
| Instructor candidates | C2DAO-selected, TM-30 certified | T3-I (prereq: TM-30 + C2DAO selection) |
| Unit data trainers | CDR-nominated, TM-20 certified | T3-F (prereq: TM-20 + CDR nomination) |
| All — background reading | Pre-MSS data concepts foundation | Data Literacy Technical Reference |

> **TM-40 Disambiguation:** Two distinct sub-series share the TM-40 designation.
> - **TM-40A–F** — Warfighting Function tracks. Prereq: TM-30. No coding required. Audience: functional WFF staff.
> - **TM-40G–O** — Technical Specialist tracks. Prereq: TM-30. Audience: engineers, analysts, and data professionals.
>
> Confirm your sub-series against your role before enrolling.

### Step 2 — Follow the Learning Path

```
Senior Leaders ──────────────────────────► Data Literacy for Senior Leaders
All Personnel ───────────────────────────► Data Literacy Technical Reference [recommended]
All Personnel ───────────────────────────► TM-10 (Maven User)
                                                │
                                                ▼
All Staff ───────────────────────────────► TM-20 (Builder)
                                           │         │
                                           │         └──► Foundry Bootcamp (FBC) ──────────┐
                                           │              Quarterly. Prereq: TM-20.       │
                                           │              Bring a real problem. Build it. │
                                           │              Outside TM chain; no TM credit. │
                                           ▼                                              │
All proceeding to TM-40 ────────────────► TM-30 (Advanced Builder)                       │
                                           │            │                                 │
                              ┌────────────┘            └────────────┐                   │
                              ▼                                      ▼                   │
                   WFF Staff (TM-40A–F)              Technical Specialists (TM-40G–O) ◄──┘
                   TM-40A  Intelligence               TM-40G  ORSA           (TM-40 requires
                   TM-40B  Fires                      TM-40H  AI Engineer     TM-30; FBC
                   TM-40C  Movement/Maneuver          TM-40M  ML Engineer     does not satisfy
                   TM-40D  Sustainment                TM-40J  Program Manager this prereq)
                   TM-40E  Protection                 TM-40K  Knowledge Manager
                   TM-40F  Mission Command            TM-40L  Software Engineer
                                                            │
                                                            ▼
                                                     TM-50G–50O (Advanced)
```

### Step 3 — Reference the Glossary

Consult the [Data & Foundry Glossary](doctrine/GLOSSARY_data_foundry.md) to translate general data concepts into MSS/Foundry terminology.

---

## Publications Index

### Doctrine Publications

| Publication | File | Audience |
|-------------|------|----------|
| Data Literacy for Senior Leaders | [doctrine/DATA_LITERACY_senior_leaders.md](doctrine/DATA_LITERACY_senior_leaders.md) | O-5+, CSM+, Senior Civilians |
| Data Literacy Technical Reference | [doctrine/DATA_LITERACY_technical_reference.md](doctrine/DATA_LITERACY_technical_reference.md) | All personnel |
| Glossary — Data & Foundry Terms | [doctrine/GLOSSARY_data_foundry.md](doctrine/GLOSSARY_data_foundry.md) | All personnel |
| CDA Constraints and Directives | [doctrine/CDA_CONSTRAINTS_AND_DIRECTIVES.md](doctrine/CDA_CONSTRAINTS_AND_DIRECTIVES.md) | TM-30+, all specialists |

### CDA Doctrine and Enterprise Architecture (TM-30, TM-40G–O)

Reference material supporting TM-30 and specialist tracks. Primarily targeted at TM-40G–O; WFF tracks (TM-40A–F) may use as supplemental reading.

**Enterprise Architecture Series:**

| Publication | File | Supports |
|-------------|------|----------|
| EA Reference Card | [doctrine/enterprise_architecture/EA_00_REFERENCE_CARD.md](doctrine/enterprise_architecture/EA_00_REFERENCE_CARD.md) | TM-30, TM-40K, TM-40L |
| EA Foundation | [doctrine/enterprise_architecture/EA_01_FOUNDATION.md](doctrine/enterprise_architecture/EA_01_FOUNDATION.md) | TM-30 |
| EA Schools of Thought | [doctrine/enterprise_architecture/EA_02_SCHOOLS_OF_THOUGHT.md](doctrine/enterprise_architecture/EA_02_SCHOOLS_OF_THOUGHT.md) | TM-30, TM-40K |
| EA Artifacts and Views | [doctrine/enterprise_architecture/EA_03_ARTIFACTS_AND_VIEWS.md](doctrine/enterprise_architecture/EA_03_ARTIFACTS_AND_VIEWS.md) | TM-40K, TM-40L |
| EA Governance | [doctrine/enterprise_architecture/EA_04_GOVERNANCE.md](doctrine/enterprise_architecture/EA_04_GOVERNANCE.md) | TM-40K |
| EA Military Application | [doctrine/enterprise_architecture/EA_05_MILITARY_APPLICATION.md](doctrine/enterprise_architecture/EA_05_MILITARY_APPLICATION.md) | TM-30, TM-40G–O |

**CDA Doctrine Series:**

| Publication | File | Supports |
|-------------|------|----------|
| Doctrine-Driven Development Overview | [doctrine/cda_doctrine/CDA_DOCTRINE_OVERVIEW.md](doctrine/cda_doctrine/CDA_DOCTRINE_OVERVIEW.md) | TM-40G–O |
| CDA Doctrine Agent | [doctrine/cda_doctrine/CDA_DOCTRINE_AGENT.md](doctrine/cda_doctrine/CDA_DOCTRINE_AGENT.md) | TM-40H, TM-40L |
| AVT25 Assessment Case Study | [doctrine/cda_doctrine/CDA_AVT25_ASSESSMENT.md](doctrine/cda_doctrine/CDA_AVT25_ASSESSMENT.md) | TM-40G, TM-40H |
| Identity vs. Classification | [doctrine/cda_doctrine/CDA_IDENTITY_VS_CLASSIFICATION.md](doctrine/cda_doctrine/CDA_IDENTITY_VS_CLASSIFICATION.md) | TM-30, TM-40K, TM-40L |

### Technical Manuals — Foundational

| Publication | File | Audience | Prereq |
|-------------|------|----------|--------|
| TM-10 — Maven User | [tm/TM_10_maven_user/TM_10_MAVEN_USER.md](tm/TM_10_maven_user/TM_10_MAVEN_USER.md) | All staff | None |
| TM-20 — Builder | [tm/TM_20_builder/TM_20_BUILDER.md](tm/TM_20_builder/TM_20_BUILDER.md) | All staff | TM-10 |
| TM-30 — Advanced Builder | [tm/TM_30_advanced_builder/TM_30_ADVANCED_BUILDER.md](tm/TM_30_advanced_builder/TM_30_ADVANCED_BUILDER.md) | Data-adjacent specialists | TM-10, TM-20 |

### TM-40A–F — Warfighting Function Tracks (Prereq: TM-30)

| Publication | File | Concepts Guide | WFF |
|-------------|------|----------------|-----|
| TM-40A — Intelligence | [tm/TM_40A_intelligence/TM_40A_INTELLIGENCE.md](tm/TM_40A_intelligence/TM_40A_INTELLIGENCE.md) | [CONCEPTS_GUIDE_TM40A](tm/TM_40A_intelligence/CONCEPTS_GUIDE_TM40A_INTELLIGENCE.md) | INT |
| TM-40B — Fires | [tm/TM_40B_fires/TM_40B_FIRES.md](tm/TM_40B_fires/TM_40B_FIRES.md) | [CONCEPTS_GUIDE_TM40B](tm/TM_40B_fires/CONCEPTS_GUIDE_TM40B_FIRES.md) | Fires |
| TM-40C — Movement & Maneuver | [tm/TM_40C_movement_maneuver/TM_40C_MOVEMENT_MANEUVER.md](tm/TM_40C_movement_maneuver/TM_40C_MOVEMENT_MANEUVER.md) | [CONCEPTS_GUIDE_TM40C](tm/TM_40C_movement_maneuver/CONCEPTS_GUIDE_TM40C_MOVEMENT_MANEUVER.md) | M2 |
| TM-40D — Sustainment | [tm/TM_40D_sustainment/TM_40D_SUSTAINMENT.md](tm/TM_40D_sustainment/TM_40D_SUSTAINMENT.md) | [CONCEPTS_GUIDE_TM40D](tm/TM_40D_sustainment/CONCEPTS_GUIDE_TM40D_SUSTAINMENT.md) | Sustainment |
| TM-40E — Protection | [tm/TM_40E_protection/TM_40E_PROTECTION.md](tm/TM_40E_protection/TM_40E_PROTECTION.md) | [CONCEPTS_GUIDE_TM40E](tm/TM_40E_protection/CONCEPTS_GUIDE_TM40E_PROTECTION.md) | Protection |
| TM-40F — Mission Command | [tm/TM_40F_mission_command/TM_40F_MISSION_COMMAND.md](tm/TM_40F_mission_command/TM_40F_MISSION_COMMAND.md) | [CONCEPTS_GUIDE_TM40F](tm/TM_40F_mission_command/CONCEPTS_GUIDE_TM40F_MISSION_COMMAND.md) | MC |

### TM-40G–O — Technical Specialist Tracks (Prereq: TM-30)

| Publication | File | Concepts Guide | Audience |
|-------------|------|----------------|----------|
| TM-40G — ORSA | [tm/TM_40G_orsa/TM_40G_ORSA.md](tm/TM_40G_orsa/TM_40G_ORSA.md) | [CONCEPTS_GUIDE_TM40G](tm/TM_40G_orsa/CONCEPTS_GUIDE_TM40G_ORSA.md) | ORSA analysts |
| TM-40H — AI Engineer | [tm/TM_40H_ai_engineer/TM_40H_AI_ENGINEER.md](tm/TM_40H_ai_engineer/TM_40H_AI_ENGINEER.md) | [CONCEPTS_GUIDE_TM40H](tm/TM_40H_ai_engineer/CONCEPTS_GUIDE_TM40H_AI_ENGINEER.md) | AI/ML specialists |
| TM-40M — ML Engineer | [tm/TM_40M_ml_engineer/TM_40M_ML_ENGINEER.md](tm/TM_40M_ml_engineer/TM_40M_ML_ENGINEER.md) | [CONCEPTS_GUIDE_TM40M](tm/TM_40M_ml_engineer/CONCEPTS_GUIDE_TM40M_ML_ENGINEER.md) | MLEs |
| TM-40J — Program Manager | [tm/TM_40J_program_manager/TM_40J_PROGRAM_MANAGER.md](tm/TM_40J_program_manager/TM_40J_PROGRAM_MANAGER.md) | [CONCEPTS_GUIDE_TM40J](tm/TM_40J_program_manager/CONCEPTS_GUIDE_TM40J_PROGRAM_MANAGER.md) | PMs, G8/S8 |
| TM-40K — Knowledge Manager | [tm/TM_40K_knowledge_manager/TM_40K_KNOWLEDGE_MANAGER.md](tm/TM_40K_knowledge_manager/TM_40K_KNOWLEDGE_MANAGER.md) | [CONCEPTS_GUIDE_TM40K](tm/TM_40K_knowledge_manager/CONCEPTS_GUIDE_TM40K_KNOWLEDGE_MANAGER.md) | KMOs, 37F |
| TM-40L — Software Engineer | [tm/TM_40L_software_engineer/TM_40L_SOFTWARE_ENGINEER.md](tm/TM_40L_software_engineer/TM_40L_SOFTWARE_ENGINEER.md) | [CONCEPTS_GUIDE_TM40L](tm/TM_40L_software_engineer/CONCEPTS_GUIDE_TM40L_SOFTWARE_ENGINEER.md) | SWEs |

### TM-50G–O — Advanced Technical Specialist Tracks

Each TM-50 track builds on its TM-40G–O counterpart. Prereq: corresponding TM-40G–O.

| Publication | File | Concepts Guide | Audience | Prereq |
|-------------|------|----------------|----------|--------|
| TM-50G — Advanced ORSA | [tm/TM_50G_orsa_advanced/TM_50G_ORSA_ADVANCED.md](tm/TM_50G_orsa_advanced/TM_50G_ORSA_ADVANCED.md) | [CONCEPTS_GUIDE_TM50G](tm/TM_50G_orsa_advanced/CONCEPTS_GUIDE_TM50G_ORSA_ADVANCED.md) | Senior ORSA | TM-40G |
| TM-50H — Advanced AI Engineer | [tm/TM_50H_ai_engineer_advanced/TM_50H_AI_ENGINEER_ADVANCED.md](tm/TM_50H_ai_engineer_advanced/TM_50H_AI_ENGINEER_ADVANCED.md) | [CONCEPTS_GUIDE_TM50H](tm/TM_50H_ai_engineer_advanced/CONCEPTS_GUIDE_TM50H_AI_ENGINEER_ADVANCED.md) | Senior AI engineers | TM-40H |
| TM-50M — Advanced MLE | [tm/TM_50M_ml_engineer_advanced/TM_50M_ML_ENGINEER_ADVANCED.md](tm/TM_50M_ml_engineer_advanced/TM_50M_ML_ENGINEER_ADVANCED.md) | [CONCEPTS_GUIDE_TM50M](tm/TM_50M_ml_engineer_advanced/CONCEPTS_GUIDE_TM50M_ML_ENGINEER_ADVANCED.md) | Senior ML engineers | TM-40M |
| TM-50J — Advanced PM | [tm/TM_50J_program_manager_advanced/TM_50J_PROGRAM_MANAGER_ADVANCED.md](tm/TM_50J_program_manager_advanced/TM_50J_PROGRAM_MANAGER_ADVANCED.md) | [CONCEPTS_GUIDE_TM50J](tm/TM_50J_program_manager_advanced/CONCEPTS_GUIDE_TM50J_PROGRAM_MANAGER_ADVANCED.md) | Senior tech PMs | TM-40J |
| TM-50K — Advanced KM | [tm/TM_50K_knowledge_manager_advanced/TM_50K_KNOWLEDGE_MANAGER_ADVANCED.md](tm/TM_50K_knowledge_manager_advanced/TM_50K_KNOWLEDGE_MANAGER_ADVANCED.md) | [CONCEPTS_GUIDE_TM50K](tm/TM_50K_knowledge_manager_advanced/CONCEPTS_GUIDE_TM50K_KNOWLEDGE_MANAGER_ADVANCED.md) | Senior KMOs | TM-40K |
| TM-50L — Advanced SWE | [tm/TM_50L_software_engineer_advanced/TM_50L_SOFTWARE_ENGINEER_ADVANCED.md](tm/TM_50L_software_engineer_advanced/TM_50L_SOFTWARE_ENGINEER_ADVANCED.md) | [CONCEPTS_GUIDE_TM50L](tm/TM_50L_software_engineer_advanced/CONCEPTS_GUIDE_TM50L_SOFTWARE_ENGINEER_ADVANCED.md) | Senior SWEs | TM-40L |

### T3 — Train-the-Trainer (Outside TM Chain)

| Publication | File | Concepts Guide | Audience | Prereq |
|-------------|------|----------------|----------|--------|
| T3-I — Instructor Certification | [tm/T3_I_instructor_certification/T3_I_INSTRUCTOR_CERTIFICATION.md](tm/T3_I_instructor_certification/T3_I_INSTRUCTOR_CERTIFICATION.md) | [CONCEPTS_GUIDE_T3I](tm/T3_I_instructor_certification/CONCEPTS_GUIDE_T3I_INSTRUCTOR_CERTIFICATION.md) | C2DAO-selected instructor candidates | TM-30 + C2DAO selection |
| T3-F — MSC Force Multiplier | [tm/T3_F_msc_force_multiplier/T3_F_MSC_FORCE_MULTIPLIER.md](tm/T3_F_msc_force_multiplier/T3_F_MSC_FORCE_MULTIPLIER.md) | [CONCEPTS_GUIDE_T3F](tm/T3_F_msc_force_multiplier/CONCEPTS_GUIDE_T3F_MSC_FORCE_MULTIPLIER.md) | CDR-nominated unit data trainers | TM-20 + CDR nomination |

---

## Training Level Descriptions

### TM-10 — Maven User
**Audience:** All personnel. **Prereq:** None.

Competencies: CAC-based login; platform navigation; Workshop application use; authorized Action execution; Contour/Quiver no-code analysis; AIP/Agent interfaces; classification handling; access troubleshooting.

### TM-20 — Builder
**Audience:** All staff. **Prereq:** TM-10.

Competencies: Foundry project creation via Compass UI; Pipeline Builder visual ETL; Ontology Manager Object Types and Link Types via UI; Action Editor; Workshop application build and publish; project permissions management; Foundry branching via UI; USAREUR-AF naming conventions.

### TM-30 — Advanced Builder
**Audience:** Data-adjacent specialists (17/25-series, S6/G6, G2). **Prereq:** TM-10, TM-20.

Competencies: Multi-page Workshop with conditional logic and variable passing; advanced Pipeline Builder multi-source joins and aggregations; Ontology design (Object Types, Link Types, Actions) via UI; advanced Contour/Quiver; AIP Logic workflow configuration (not authoring); data lineage review; governance workflows; branching and production promotion; C2DAO governance standards.

### TM-40A–F — Warfighting Function Tracks
**Prereq:** TM-30. No coding required.

| Track | WFF | Audience | Focus |
|-------|-----|----------|-------|
| TM-40A | Intelligence | G2/S2 staff, targeting officers, all-source analysts | Collection management, targeting, all-source analysis workflows |
| TM-40B | Fires | FSE, fire support officers, targeting teams | Targeting data, effects assessment, fire support coordination |
| TM-40C | Movement & Maneuver | G3/S3 maneuver staff | Maneuver tracking, route analysis, operational visualization |
| TM-40D | Sustainment | G4/S4, logistics staff | Logistics visibility, supply chain analytics, readiness tracking |
| TM-40E | Protection | Force protection, CBRN staff | Threat tracking, vulnerability assessment, protection COA support |
| TM-40F | Mission Command | C2/MC staff, battle captains | Operational dashboards, CCIR management, battle rhythm products |

### TM-40G–O — Technical Specialist Tracks
**Prereq:** TM-30.

| Track | Audience | Key Competencies |
|-------|----------|------------------|
| TM-40G ORSA | FA49, quantitative analysts | Code Workspaces (Python/R); regression, classification, time series, Monte Carlo, linear programming; wargame data architecture; analytical decision support products |
| TM-40H AI Engineer | AI/ML specialists | AIP Logic authoring; Agent Studio; LLM integration (RAG, ontology grounding); AI safety gates; Python transforms for AI consumption; production deployment and monitoring |
| TM-40M ML Engineer | MLEs, data scientists | Code Workspace model dev; model versioning and experiment tracking; production deployment and Ontology integration; MLOps patterns; responsible AI documentation |
| TM-40J Program Manager | PMs, G8/S8 | Agile PM (Scrum/Kanban) for data/AI; user stories for data products; ML/AI lifecycle management; sprint tracking dashboards; change management and user adoption |
| TM-40K Knowledge Manager | KMOs, 37F | AAR capture systems; lessons-learned ingestion pipelines; AIP Logic for knowledge summarization; semantic search systems; doctrine/SOP version control; expertise registries |
| TM-40L Software Engineer | SWEs | OSDK (TypeScript/Python); Foundry Platform SDK; TypeScript Functions on Objects; Action validators; Slate applications; USAREUR-AF code review and deployment standards |

> **NOTE — TM-40J/TM-40K Prereq:** TM-30 is required (not recommended) for both TM-40J and TM-40K. Route all PMs and KMOs through TM-30 before enrolling in TM-40J or TM-40K regardless of whether their teams write code. Consult the ENROLLMENT_SOP for waiver procedures.

### T3 — Train-the-Trainer
**Outside the TM-10 to TM-50 numbering chain.** Own T3-I/T3-F designation.

| Track | Prereq | Duration | Audience | Output |
|-------|--------|----------|----------|--------|
| T3-I Instructor Certification | TM-30 + C2DAO selection | 5 days (classroom + practicum) | C2DAO-selected instructor candidates | Certified Instructor |
| T3-F MSC Force Multiplier | TM-20 + CDR nomination | Half day | CDR-nominated unit personnel | Unit Data Trainer (UDT) |

---

## Training Management

### Administrative Publications

| Resource | File | Audience |
|----------|------|----------|
| Mission Training Plan (MTP) | [training_management/MTP_MSS.md](training_management/MTP_MSS.md) | Training managers, S3/G6, commanders |
| Program of Instruction (POI) | [training_management/POI_MSS.md](training_management/POI_MSS.md) | Training managers, curriculum designers |
| Course Administrative Data (CAD) | [training_management/CAD_MSS.md](training_management/CAD_MSS.md) | Training administrators |
| Training and Evaluation Outline (TEO) | [training_management/TEO_MSS.md](training_management/TEO_MSS.md) | Instructors, evaluators |
| Annual Training Schedule | [training_management/ANNUAL_TRAINING_SCHEDULE.md](training_management/ANNUAL_TRAINING_SCHEDULE.md) | Training managers, S3 |
| Enrollment SOP | [training_management/ENROLLMENT_SOP.md](training_management/ENROLLMENT_SOP.md) | Training coordinators |
| Completion Certificate Template | [training_management/COMPLETION_CERTIFICATE.md](training_management/COMPLETION_CERTIFICATE.md) | Training administrators |
| Faculty Development Plan | [training_management/FACULTY_DEVELOPMENT_PLAN.md](training_management/FACULTY_DEVELOPMENT_PLAN.md) | Instructor cadre, S3 |
| Training Policy Letter | [training_management/POLICY_LETTER.md](training_management/POLICY_LETTER.md) | Commanders, training managers |
| Curriculum Maintenance SOP | [training_management/CURRICULUM_MAINTENANCE_SOP.md](training_management/CURRICULUM_MAINTENANCE_SOP.md) | Curriculum owner, SMEs, instructors |
| AAR / Feedback Template | [training_management/AAR_TEMPLATE.md](training_management/AAR_TEMPLATE.md) | Instructors, evaluators |
| Instructor Tier Definitions | [training_management/INSTRUCTOR_TIER_DEFINITIONS.md](training_management/INSTRUCTOR_TIER_DEFINITIONS.md) | T3-I cadre, training managers |
| C2DAO SME Designation Rubric | [training_management/C2DAO_SME_DESIGNATION_RUBRIC.md](training_management/C2DAO_SME_DESIGNATION_RUBRIC.md) | T3-I candidates, C2DAO leadership |
| Unit Data Trainer SOP | [training_management/UNIT_DATA_TRAINER_SOP.md](training_management/UNIT_DATA_TRAINER_SOP.md) | T3-F graduates (UDTs), unit commanders |
| MTT Operations SOP | [training_management/MTT_OPERATIONS_SOP.md](training_management/MTT_OPERATIONS_SOP.md) | T3-I/T3-F graduates, MTT coordinators |
| Successor Planning Guide | [training_management/SUCCESSOR_PLANNING_GUIDE.md](training_management/SUCCESSOR_PLANNING_GUIDE.md) | Training managers, T3 cadre |

### Lesson Plans

| Resource | File |
|----------|------|
| Lesson Plan Template | [training_management/lesson_plans/LP_TEMPLATE.md](training_management/lesson_plans/LP_TEMPLATE.md) |
| TM-20 Lesson Plan Outlines | [training_management/lesson_plans/TM20_LESSON_PLAN_OUTLINES.md](training_management/lesson_plans/TM20_LESSON_PLAN_OUTLINES.md) |
| TM-30 Lesson Plan Outlines | [training_management/lesson_plans/TM30_LESSON_PLAN_OUTLINES.md](training_management/lesson_plans/TM30_LESSON_PLAN_OUTLINES.md) |
| TM-40 Specialist Lesson Plan Outlines | [training_management/lesson_plans/TM40_SPECIALIST_LESSON_PLAN_OUTLINES.md](training_management/lesson_plans/TM40_SPECIALIST_LESSON_PLAN_OUTLINES.md) |
| T3-I Lesson Plan Outlines | [training_management/lesson_plans/T3I_LESSON_PLAN_OUTLINES.md](training_management/lesson_plans/T3I_LESSON_PLAN_OUTLINES.md) |
| T3-F Lesson Plan Outlines | [training_management/lesson_plans/T3F_LESSON_PLAN_OUTLINES.md](training_management/lesson_plans/T3F_LESSON_PLAN_OUTLINES.md) |

### Course Syllabi

Distribute to each trainee at course start.

| Syllabus | File | Audience |
|----------|------|----------|
| TM-10 | [syllabi/SYLLABUS_TM10.md](syllabi/SYLLABUS_TM10.md) | All personnel |
| TM-20 | [syllabi/SYLLABUS_TM20.md](syllabi/SYLLABUS_TM20.md) | All staff |
| TM-30 | [syllabi/SYLLABUS_TM30.md](syllabi/SYLLABUS_TM30.md) | Data-adjacent specialists |
| TM-40A | [syllabi/SYLLABUS_TM40A.md](syllabi/SYLLABUS_TM40A.md) | G2/S2 staff, targeting officers |
| TM-40B | [syllabi/SYLLABUS_TM40B.md](syllabi/SYLLABUS_TM40B.md) | FSE, fire support officers |
| TM-40C | [syllabi/SYLLABUS_TM40C.md](syllabi/SYLLABUS_TM40C.md) | G3/S3 maneuver staff |
| TM-40D | [syllabi/SYLLABUS_TM40D.md](syllabi/SYLLABUS_TM40D.md) | G4/S4, logistics staff |
| TM-40E | [syllabi/SYLLABUS_TM40E.md](syllabi/SYLLABUS_TM40E.md) | Force protection, CBRN, PM staff |
| TM-40F | [syllabi/SYLLABUS_TM40F.md](syllabi/SYLLABUS_TM40F.md) | G3/S3 staff, battle captains, CDRs |
| TM-40G | [syllabi/SYLLABUS_TM40G.md](syllabi/SYLLABUS_TM40G.md) | ORSA analysts |
| TM-40H | [syllabi/SYLLABUS_TM40H.md](syllabi/SYLLABUS_TM40H.md) | AI/ML specialists |
| TM-40M | [syllabi/SYLLABUS_TM40M.md](syllabi/SYLLABUS_TM40M.md) | MLEs |
| TM-40J | [syllabi/SYLLABUS_TM40J.md](syllabi/SYLLABUS_TM40J.md) | PMs, G8/S8 |
| TM-40K | [syllabi/SYLLABUS_TM40K.md](syllabi/SYLLABUS_TM40K.md) | KMOs, 37F |
| TM-40L | [syllabi/SYLLABUS_TM40L.md](syllabi/SYLLABUS_TM40L.md) | SWEs |

> **Note:** TM-50G–O series syllabi are published. TM-50A–F do not exist (WFF tracks are terminal — no advanced continuation). Advanced training is available only for specialist tracks (G–O). Contact training management for scheduling.

---

## Supporting Reference Material

| Resource | File | Notes |
|----------|------|-------|
| MSS Quick Start | [QUICK_START.md](QUICK_START.md) | 30-minute onboarding |
| Naming & Governance Standards | [standards/NAMING_AND_GOVERNANCE_STANDARDS.md](standards/NAMING_AND_GOVERNANCE_STANDARDS.md) | USAREUR-AF MSS naming conventions and governance checklists |
| MSS Training Hub (web) | [mss_info_app/index.html](mss_info_app/index.html) | Standalone HTML training hub — open in browser |
| Practical Exercises | [exercises/](exercises/) | Hands-on packages for TM-10 through TM-40M |
| Enterprise Data Compass | [quick_reference/cda_reference/ENTERPRISE_DATA_COMPASS.md](quick_reference/cda_reference/ENTERPRISE_DATA_COMPASS.md) | Authoritative reference — data architecture, ontology, semantic governance |
| EA vs DA Reference | [quick_reference/cda_reference/EA_VS_DA.md](quick_reference/cda_reference/EA_VS_DA.md) | Enterprise Architecture vs Data Architecture — definitions and distinctions |
| Plan for Success | [quick_reference/cda_reference/PLAN_FOR_SUCCESS.md](quick_reference/cda_reference/PLAN_FOR_SUCCESS.md) | Technology radar + 5-phase program roadmap with approval chains |
| Lessons Learned Reference | [quick_reference/cda_reference/LESSONS_LEARNED.md](quick_reference/cda_reference/LESSONS_LEARNED.md) | AAR format + LL-001 AVT25 assessment tools case study |
| CDA Slide Library (course portal) | [source_material/course_portal/](source_material/course_portal/) | 29 PDF decks — Intro To Data, Data 101, Data 201 — prereq reading for TM tracks |
| CDA Interactive Apps | [source_material/cda_apps/](source_material/cda_apps/) | Browser-based training tools (EA vs DA, Enterprise Data Compass, LL, Plan for Success) |
| CDA Final Exam | [exercises/exams/EXAM_CDA_FINAL.md](exercises/exams/EXAM_CDA_FINAL.md) | Comprehensive 300-pt exam covering all three CDA slide tracks |
| Foundry Python Patterns | [data_skills/13_foundry_patterns/](../skills/data_skills/13_foundry_patterns/) | Local shim for offline development and testing |
| Full data science reference library | [data_skills/](../skills/data_skills/) | 15 modules: Python → ML → ETL → deployment |
| SITREP Tracker (applied project) | [sitrep_tracker/](../sitrep_tracker/) | Click + Rich + SQLite reference implementation |
| Ontologize YouTube Channel (68 videos) | [source_material/ontologize_youtube/README.md](source_material/ontologize_youtube/README.md) | Official Palantir partner — 24 hrs of Foundry/AIP walkthroughs; TM cross-reference index included |

### Palantir Public Documentation

> Source: https://www.palantir.com/docs/foundry/ | Scraped: 2026-03-17
> Full index: [source_material/palantir_community/PALANTIR_DOCS_REFERENCE.md](source_material/palantir_community/PALANTIR_DOCS_REFERENCE.md)

| Resource | Topic Area | TM Relevance |
|----------|-----------|--------------|
| Ontology Overview | Object Types, Link Types, Properties, Interfaces, Structs, Value Types | TM-20, TM-30, TM-40K |
| Actions & Functions | Action Types, TypeScript/Python Functions, Transactions, Webhooks | TM-30, TM-40L |
| Data Integration | Data Connection (200+ connectors), Pipeline Builder, Code Transforms, Streaming | TM-20, TM-30, TM-40L |
| AIP Logic | Block-based AI workflows, Ontology integration, Branching logic, Eval suites | TM-40H, TM-50H |
| AIP Agent Studio | Agent state, Retrieval context, Tools, Agents-as-Functions, Marketplace | TM-40H, TM-50H |
| Document Intelligence | Extraction strategies, Vision-language models, RAG pipeline support | TM-40H, TM-40M |
| Security & Governance | Dual control (mandatory + discretionary), RBAC, Marking-based access, Audit logs | TM-40J, TM-40K |

### Palantir Developer Community

> Source: https://community.palantir.com/ | Scraped: 2026-03-17
> Full index: [source_material/palantir_community/README.md](source_material/palantir_community/README.md)
>
> **VERIFICATION NOTE:** Community content is user-generated and may reference outdated product behavior or deprecated features. Cross-reference against [Palantir Public Docs](source_material/palantir_community/PALANTIR_DOCS_REFERENCE.md) and current MSS environment before incorporating into training. Posts marked with Palantir staff flair ("Inside the Product" category) carry higher authority.

**Official Product Guidance (Palantir Staff — Inside the Product)**

| Resource | URL | TM Relevance |
|----------|-----|--------------|
| Ontology and Pipeline Design Principles | [community.palantir.com/t/5481](https://community.palantir.com/t/ontology-and-pipeline-design-principles/5481) | TM-20, TM-30, TM-40K, TM-40L |
| Why We Built It: Compute Modules | [community.palantir.com/t/3292](https://community.palantir.com/t/why-we-built-it-compute-modules/3292) | TM-40L, TM-50L |
| Why We Built It: Foundry for VS Code | [community.palantir.com/t/3486](https://community.palantir.com/t/why-we-built-it-foundry-for-vs-code/3486) | TM-40L, TM-50L |
| Why We Built It: Solution Designer & AIP Architect | [community.palantir.com/t/2666](https://community.palantir.com/t/why-we-built-it-solution-designer-aip-architect/2666) | TM-40J, TM-40K |
| Leveling Up AIP Agents with the Palantir API | [community.palantir.com/t/2956](https://community.palantir.com/t/leveling-up-your-aip-agents-with-the-palantir-api/2956) | TM-40H, TM-50H |
| Launching 10 Build with AIP Examples | [community.palantir.com/t/5137](https://community.palantir.com/t/launching-10-new-build-with-aip-examples/5137) | TM-40H, TM-50H |
| Introducing Model Selector | [community.palantir.com/t/2972](https://community.palantir.com/t/introducing-model-selector-enhancing-your-model-selection-experience/2972) | TM-40H, TM-40M |
| Sneak Peek: Pipeline Builder Roadmap | [community.palantir.com/t/2970](https://community.palantir.com/t/sneak-peek-into-what-s-next-for-pipeline-builder/2970) | TM-20, TM-30 |
| 150+ New Sources in Data Connection | [community.palantir.com/t/507](https://community.palantir.com/t/over-150-new-sources-are-now-available-in-data-connection/507) | TM-20, TM-30 |
| Databricks Enhanced Connectivity | [community.palantir.com/t/4339](https://community.palantir.com/t/databricks-enhanced-connectivity-compute-pushdown/4339) | TM-40L, TM-50L |
| Workflow Builder Game-Changing Features | [community.palantir.com/t/2959](https://community.palantir.com/t/discover-the-latest-game-changing-features-of-workflow-builder/2959) | TM-30, TM-40J |
| Introducing Object Type Groups | [community.palantir.com/t/343](https://community.palantir.com/t/introducing-object-type-groups-in-the-ontology/343) | TM-30, TM-40K |
| Python Functions for Pipeline Builder (Beta) | [community.palantir.com/t/502](https://community.palantir.com/t/introducing-python-functions-for-pipeline-builder-workshop-and-more-beta/502) | TM-30, TM-40L |
| Pipeline Builder Enforced LLM Output Types | [community.palantir.com/t/350](https://community.palantir.com/t/pipeline-builder-now-supports-enforced-output-types-for-llm-nodes/350) | TM-40H, TM-40M |

**Defense & Military-Relevant**

| Resource | URL | TM Relevance |
|----------|-----|--------------|
| Discover Palantir's Defense OSDK | [community.palantir.com/t/3561](https://community.palantir.com/t/discover-the-power-of-palantirs-defense-osdk/3561) | TM-40L, TM-50L |
| Local Inference for DDIL / Classified | [community.palantir.com/t/6146](https://community.palantir.com/t/local-inference-connector-for-aip-logic-ddil-classified-data-use-cases/6146) | TM-40H, TM-50H |

**Certification & Training Alignment**

| Resource | URL | TM Relevance |
|----------|-----|--------------|
| Foundry & AIP Builder Foundations Badge | [community.palantir.com/t/1043](https://community.palantir.com/t/earn-your-foundry-aip-builder-foundations-badge/1043) | TM-10, TM-20 |
| Data Engineer Certification Prep | [community.palantir.com/t/2789](https://community.palantir.com/t/data-engineer-certification-preperation/2789) | TM-30, TM-40L |
| Application Developer Certification | [community.palantir.com/t/548](https://community.palantir.com/t/what-to-expect-in-foundry-application-developer-certification-exam/548) | TM-30, TM-40L |
| Ontologize Build with Us (LPC Courses) | [community.palantir.com/t/5055](https://community.palantir.com/t/ontologize-build-with-us-series-for-palantir-lpc-courses/5055) | TM-20, TM-30 |

**Community Topic Volume by Tag (for supplemental research)**

| Tag | Topics | Primary TM Tracks |
|-----|--------|-------------------|
| workshop | 979 | TM-10, TM-20, TM-30 |
| code-repositories | 659 | TM-30, TM-40L, TM-50L |
| pipeline-builder | 570 | TM-20, TM-30 |
| ontology-management | 530 | TM-20, TM-30, TM-40K |
| functions | 514 | TM-30, TM-40L |
| data-connection | 384 | TM-20, TM-30 |
| osdk | 213 | TM-40L, TM-50L |
| aip-logic | 144 | TM-40H, TM-50H |
| aip-agent-studio | 71 | TM-40H, TM-50H |
| modeling | 62 | TM-40M, TM-50M |
| streaming | 54 | TM-30, TM-40L |
| compute-modules | 39 | TM-40L, TM-50L |
| time-series | 29 | TM-30, TM-40G |
| solution-design-app | 27 | TM-40J, TM-40K |
| machinery | 10 | TM-40D |

---

## Quick-Reference Training Paths

### New Soldier joining the data team

1. If O-5+: read [Data Literacy for Senior Leaders](doctrine/DATA_LITERACY_senior_leaders.md)
2. Skim [Data Literacy Technical Reference](doctrine/DATA_LITERACY_technical_reference.md) Ch 1–3 and Ch 8
3. Complete [TM-10](tm/TM_10_maven_user/TM_10_MAVEN_USER.md)
4. Request MSS access; practice navigation tasks
5. If building: complete [TM-20](tm/TM_20_builder/TM_20_BUILDER.md)
6. Complete [TM-30](tm/TM_30_advanced_builder/TM_30_ADVANCED_BUILDER.md)
7. WFF functional staff: proceed to TM-40A–F per function (after TM-30)
8. Technical specialists: proceed to TM-40G–O per role (after TM-30)

### S6 shop standing up MSS capability

1. Commander reads Data Literacy for Senior Leaders
2. All staff complete TM-10
3. Designated builders complete TM-20
4. Designated data leads complete TM-30
5. Reference Glossary throughout
6. Technical specialists proceed to TM-40G–O per role
7. WFF functional staff proceed to TM-40A–F per function

### TM-40 Track Selection by MOS/Role

| Role / MOS | TM-40 Track |
|---|---|
| All WFF staff | TM-40A–F per assigned warfighting function |
| 17A/17C — Cyber officer/NCO | TM-40L (SWE) or TM-40H (AI Eng) |
| 25D — IT specialist | TM-40L (SWE) |
| 25U — Signal support | TM-40L (SWE) or TM-40J (PM) |
| FA49 — Operations Research | TM-40G (ORSA) |
| 37F — Psychological Operations | TM-40K (KM) |
| G2/S2 analyst | TM-40G (ORSA) or TM-40K (KM) |
| G6/S6 data officer | TM-40L (SWE) or TM-40H (AI Eng) |
| G8/S8 resource manager | TM-40J (PM) |
| Civil Affairs | TM-40J (PM) or TM-40K (KM) |
| Data scientist (GS/contractor) | TM-40G (ORSA) or TM-40M (MLE) |
| AI/ML engineer (GS/contractor) | TM-40H (AI Eng) or TM-40M (MLE) |
| KMO / Knowledge Officer | TM-40K (KM) |
| PM / Program Manager | TM-40J (PM) |

---

*USAREUR-AF Operational Data Team*
*Version 5.1 | March 2026 | CDA doctrine, EA series, and source material indexed; TM-20 appendices and CONCEPTS_GUIDE files added | Supersedes v5.0*
