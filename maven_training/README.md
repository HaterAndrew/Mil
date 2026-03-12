# Maven Smart System (MSS) — Training Curriculum
## USAREUR-AF Operational Data Team

```
HEADQUARTERS, UNITED STATES ARMY EUROPE AND AFRICA
Wiesbaden, Germany
```

**Distribution:** DRAFT — Not yet approved for distribution.

---

> **New to MSS?** Read **[QUICK_START.md](QUICK_START.md)** first — operational in 30 minutes.

---

## How to Use This Curriculum

### Step 1 — Know Your Level

| Level | Who You Are | Start Here |
|-------|-------------|------------|
| All personnel | Soldier, officer, or civilian accessing MSS for data consumption | TM-10 |
| All staff (light builders) | Building dashboards, forms, or basic pipelines | TM-20 (prereq: TM-10) |
| Data-adjacent specialists | 17/25-series, S6/G6, G2/G9, operational data analysts | TM-30 (prereq: TM-20) |
| WFF functional staff | Assigned to INT, FIRES, M2, SUST, PROTECTION, or MC | TM-40A–F (prereq: TM-20) |
| Technical specialists | Writing code, building external apps, ML models | TM-40G–L (prereq: TM-30) |
| Senior leaders (O-5+, CSM+) | Commanding or directing a data-capable formation | Data Literacy for Senior Leaders |
| All — background reading | Pre-MSS data concepts foundation | Data Literacy Technical Reference |

> **TM-40 Disambiguation:** Two distinct sub-series share the TM-40 designation.
> - **TM-40A–F** — Warfighting Function tracks. Prereq: TM-20. No coding required. Audience: functional WFF staff.
> - **TM-40G–L** — Technical Specialist tracks. Prereq: TM-30. Audience: engineers, analysts, and data professionals.
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
                                           │            │
                              ┌────────────┘            └────────────┐
                              ▼                                      ▼
                   WFF Staff (TM-40A–F)                  Data-Adjacent Specialists
                   TM-40A  Intelligence                  TM-30 (Advanced Builder)
                   TM-40B  Fires                               │
                   TM-40C  Movement/Maneuver         ┌─────────┴─────────┐
                   TM-40D  Sustainment               ▼                   ▼
                   TM-40E  Protection         TM-40G–40L           TM-50G–50L
                   TM-40F  Mission Command  (Tech Specialists)      (Advanced)
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

### Technical Manuals — Foundational

| Publication | File | Audience | Prereq |
|-------------|------|----------|--------|
| TM-10 — Maven User | [tm/TM_10_maven_user/TM_10_MAVEN_USER.md](tm/TM_10_maven_user/TM_10_MAVEN_USER.md) | All staff | None |
| TM-20 — Builder | [tm/TM_20_builder/TM_20_BUILDER.md](tm/TM_20_builder/TM_20_BUILDER.md) | All staff | TM-10 |
| TM-30 — Advanced Builder | [tm/TM_30_advanced_builder/TM_30_ADVANCED_BUILDER.md](tm/TM_30_advanced_builder/TM_30_ADVANCED_BUILDER.md) | Data-adjacent specialists | TM-10, TM-20 |

### TM-40A–F — Warfighting Function Tracks (Prereq: TM-20)

| Publication | File | Concepts Guide | WFF |
|-------------|------|----------------|-----|
| TM-40A — Intelligence | [tm/TM_40A_intelligence/TM_40A_INTELLIGENCE.md](tm/TM_40A_intelligence/TM_40A_INTELLIGENCE.md) | [CONCEPTS_GUIDE_TM40A](tm/TM_40A_intelligence/CONCEPTS_GUIDE_TM40A_INTELLIGENCE.md) | INT |
| TM-40B — Fires | [tm/TM_40B_fires/TM_40B_FIRES.md](tm/TM_40B_fires/TM_40B_FIRES.md) | [CONCEPTS_GUIDE_TM40B](tm/TM_40B_fires/CONCEPTS_GUIDE_TM40B_FIRES.md) | Fires |
| TM-40C — Movement & Maneuver | [tm/TM_40C_movement_maneuver/TM_40C_MOVEMENT_MANEUVER.md](tm/TM_40C_movement_maneuver/TM_40C_MOVEMENT_MANEUVER.md) | [CONCEPTS_GUIDE_TM40C](tm/TM_40C_movement_maneuver/CONCEPTS_GUIDE_TM40C_MOVEMENT_MANEUVER.md) | M2 |
| TM-40D — Sustainment | [tm/TM_40D_sustainment/TM_40D_SUSTAINMENT.md](tm/TM_40D_sustainment/TM_40D_SUSTAINMENT.md) | [CONCEPTS_GUIDE_TM40D](tm/TM_40D_sustainment/CONCEPTS_GUIDE_TM40D_SUSTAINMENT.md) | Sustainment |
| TM-40E — Protection | [tm/TM_40E_protection/TM_40E_PROTECTION.md](tm/TM_40E_protection/TM_40E_PROTECTION.md) | [CONCEPTS_GUIDE_TM40E](tm/TM_40E_protection/CONCEPTS_GUIDE_TM40E_PROTECTION.md) | Protection |
| TM-40F — Mission Command | [tm/TM_40F_mission_command/TM_40F_MISSION_COMMAND.md](tm/TM_40F_mission_command/TM_40F_MISSION_COMMAND.md) | [CONCEPTS_GUIDE_TM40F](tm/TM_40F_mission_command/CONCEPTS_GUIDE_TM40F_MISSION_COMMAND.md) | MC |

### TM-40G–L — Technical Specialist Tracks (Prereq: TM-30)

| Publication | File | Concepts Guide | Audience |
|-------------|------|----------------|----------|
| TM-40G — ORSA | [tm/TM_40G_orsa/TM_40G_ORSA.md](tm/TM_40G_orsa/TM_40G_ORSA.md) | [CONCEPTS_GUIDE_TM40G](tm/TM_40G_orsa/CONCEPTS_GUIDE_TM40G_ORSA.md) | ORSA analysts |
| TM-40H — AI Engineer | [tm/TM_40H_ai_engineer/TM_40H_AI_ENGINEER.md](tm/TM_40H_ai_engineer/TM_40H_AI_ENGINEER.md) | [CONCEPTS_GUIDE_TM40H](tm/TM_40H_ai_engineer/CONCEPTS_GUIDE_TM40H_AI_ENGINEER.md) | AI/ML specialists |
| TM-40I — ML Engineer | [tm/TM_40I_ml_engineer/TM_40I_ML_ENGINEER.md](tm/TM_40I_ml_engineer/TM_40I_ML_ENGINEER.md) | [CONCEPTS_GUIDE_TM40I](tm/TM_40I_ml_engineer/CONCEPTS_GUIDE_TM40I_ML_ENGINEER.md) | MLEs |
| TM-40J — Program Manager | [tm/TM_40J_program_manager/TM_40J_PROGRAM_MANAGER.md](tm/TM_40J_program_manager/TM_40J_PROGRAM_MANAGER.md) | [CONCEPTS_GUIDE_TM40J](tm/TM_40J_program_manager/CONCEPTS_GUIDE_TM40J_PROGRAM_MANAGER.md) | PMs, G8/S8 |
| TM-40K — Knowledge Manager | [tm/TM_40K_knowledge_manager/TM_40K_KNOWLEDGE_MANAGER.md](tm/TM_40K_knowledge_manager/TM_40K_KNOWLEDGE_MANAGER.md) | [CONCEPTS_GUIDE_TM40K](tm/TM_40K_knowledge_manager/CONCEPTS_GUIDE_TM40K_KNOWLEDGE_MANAGER.md) | KMOs, 37F |
| TM-40L — Software Engineer | [tm/TM_40L_software_engineer/TM_40L_SOFTWARE_ENGINEER.md](tm/TM_40L_software_engineer/TM_40L_SOFTWARE_ENGINEER.md) | [CONCEPTS_GUIDE_TM40L](tm/TM_40L_software_engineer/CONCEPTS_GUIDE_TM40L_SOFTWARE_ENGINEER.md) | SWEs |

### TM-50G–L — Advanced Technical Specialist Tracks

Each TM-50 track builds on its TM-40G–L counterpart. Prereq: corresponding TM-40G–L.

| Publication | File | Concepts Guide | Audience | Prereq |
|-------------|------|----------------|----------|--------|
| TM-50G — Advanced ORSA | [tm/TM_50G_orsa_advanced/TM_50G_ORSA_ADVANCED.md](tm/TM_50G_orsa_advanced/TM_50G_ORSA_ADVANCED.md) | [CONCEPTS_GUIDE_TM50G](tm/TM_50G_orsa_advanced/CONCEPTS_GUIDE_TM50G_ORSA_ADVANCED.md) | Senior ORSA | TM-40G |
| TM-50H — Advanced AI Engineer | [tm/TM_50H_ai_engineer_advanced/TM_50H_AI_ENGINEER_ADVANCED.md](tm/TM_50H_ai_engineer_advanced/TM_50H_AI_ENGINEER_ADVANCED.md) | [CONCEPTS_GUIDE_TM50H](tm/TM_50H_ai_engineer_advanced/CONCEPTS_GUIDE_TM50H_AI_ENGINEER_ADVANCED.md) | Senior AI engineers | TM-40H |
| TM-50I — Advanced MLE | [tm/TM_50I_ml_engineer_advanced/TM_50I_ML_ENGINEER_ADVANCED.md](tm/TM_50I_ml_engineer_advanced/TM_50I_ML_ENGINEER_ADVANCED.md) | [CONCEPTS_GUIDE_TM50I](tm/TM_50I_ml_engineer_advanced/CONCEPTS_GUIDE_TM50I_ML_ENGINEER_ADVANCED.md) | Senior ML engineers | TM-40I |
| TM-50J — Advanced PM | [tm/TM_50J_program_manager_advanced/TM_50J_PROGRAM_MANAGER_ADVANCED.md](tm/TM_50J_program_manager_advanced/TM_50J_PROGRAM_MANAGER_ADVANCED.md) | [CONCEPTS_GUIDE_TM50J](tm/TM_50J_program_manager_advanced/CONCEPTS_GUIDE_TM50J_PROGRAM_MANAGER_ADVANCED.md) | Senior tech PMs | TM-40J |
| TM-50K — Advanced KM | [tm/TM_50K_knowledge_manager_advanced/TM_50K_KNOWLEDGE_MANAGER_ADVANCED.md](tm/TM_50K_knowledge_manager_advanced/TM_50K_KNOWLEDGE_MANAGER_ADVANCED.md) | [CONCEPTS_GUIDE_TM50K](tm/TM_50K_knowledge_manager_advanced/CONCEPTS_GUIDE_TM50K_KNOWLEDGE_MANAGER_ADVANCED.md) | Senior KMOs | TM-40K |
| TM-50L — Advanced SWE | [tm/TM_50L_software_engineer_advanced/TM_50L_SOFTWARE_ENGINEER_ADVANCED.md](tm/TM_50L_software_engineer_advanced/TM_50L_SOFTWARE_ENGINEER_ADVANCED.md) | [CONCEPTS_GUIDE_TM50L](tm/TM_50L_software_engineer_advanced/CONCEPTS_GUIDE_TM50L_SOFTWARE_ENGINEER_ADVANCED.md) | Senior SWEs | TM-40L |

---

## Training Level Descriptions

### TM-10 — Maven User
**Audience:** All personnel. **Prereq:** None.

Competencies: CAC-based login; platform navigation; Workshop application use; authorized Action execution; Contour/Quiver no-code analysis; AIP/Agent interfaces; classification handling; access troubleshooting.

### TM-20 — Builder
**Audience:** All staff. **Prereq:** TM-10.

Competencies: Foundry project creation via Compass UI; Pipeline Builder visual ETL; Ontology Manager Object Types and Link Types via UI; Action Editor; Workshop application build and publish; project permissions management; Foundry branching via UI; USAREUR-AF naming conventions.

### TM-30 — Advanced Builder
**Audience:** Data-adjacent specialists (17/25-series, S6/G6, G2/G9). **Prereq:** TM-10, TM-20.

Competencies: Multi-page Workshop with conditional logic and variable passing; advanced Pipeline Builder multi-source joins and aggregations; Ontology design (Object Types, Link Types, Actions) via UI; advanced Contour/Quiver; AIP Logic workflow configuration (not authoring); data lineage review; governance workflows; branching and production promotion; C2DAO governance standards.

### TM-40A–F — Warfighting Function Tracks
**Prereq:** TM-20. No coding required.

| Track | WFF | Audience | Focus |
|-------|-----|----------|-------|
| TM-40A | Intelligence | G2/S2 staff, targeting officers, all-source analysts | Collection management, targeting, all-source analysis workflows |
| TM-40B | Fires | FSE, fire support officers, targeting teams | Targeting data, effects assessment, fire support coordination |
| TM-40C | Movement & Maneuver | G3/S3 maneuver staff | Maneuver tracking, route analysis, operational visualization |
| TM-40D | Sustainment | G4/S4, logistics staff | Logistics visibility, supply chain analytics, readiness tracking |
| TM-40E | Protection | Force protection, CBRN staff | Threat tracking, vulnerability assessment, protection COA support |
| TM-40F | Mission Command | C2/MC staff, battle captains | Operational dashboards, CCIR management, battle rhythm products |

### TM-40G–L — Technical Specialist Tracks
**Prereq:** TM-30.

| Track | Audience | Key Competencies |
|-------|----------|------------------|
| TM-40G ORSA | FA49, quantitative analysts | Code Workspaces (Python/R); regression, classification, time series, Monte Carlo, linear programming; wargame data architecture; analytical decision support products |
| TM-40H AI Engineer | AI/ML specialists | AIP Logic authoring; Agent Studio; LLM integration (RAG, ontology grounding); AI safety gates; Python transforms for AI consumption; production deployment and monitoring |
| TM-40I ML Engineer | MLEs, data scientists | Code Workspace model dev; model versioning and experiment tracking; production deployment and Ontology integration; MLOps patterns; responsible AI documentation |
| TM-40J Program Manager | PMs, G8/S8 | Agile PM (Scrum/Kanban) for data/AI; user stories for data products; ML/AI lifecycle management; sprint tracking dashboards; change management and user adoption |
| TM-40K Knowledge Manager | KMOs, 37F | AAR capture systems; lessons-learned ingestion pipelines; AIP Logic for knowledge summarization; semantic search systems; doctrine/SOP version control; expertise registries |
| TM-40L Software Engineer | SWEs | OSDK (TypeScript/Python); Foundry Platform SDK; TypeScript Functions on Objects; Action validators; Slate applications; USAREUR-AF code review and deployment standards |

> **NOTE — TM-40J/TM-40K Prereq Variance:** The MTP lists TM-20 as the minimum prereq for TM-40J and TM-40K. The respective syllabi list TM-30. Route technical PMs and KMOs who will oversee code-writing teams through TM-30 first. PMs/KMOs overseeing no-code or builder-level teams may proceed from TM-20.

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

### Lesson Plans

| Resource | File |
|----------|------|
| Lesson Plan Template | [training_management/lesson_plans/LP_TEMPLATE.md](training_management/lesson_plans/LP_TEMPLATE.md) |
| TM-20 Lesson Plan Outlines | [training_management/lesson_plans/TM20_LESSON_PLAN_OUTLINES.md](training_management/lesson_plans/TM20_LESSON_PLAN_OUTLINES.md) |
| TM-30 Lesson Plan Outlines | [training_management/lesson_plans/TM30_LESSON_PLAN_OUTLINES.md](training_management/lesson_plans/TM30_LESSON_PLAN_OUTLINES.md) |
| TM-40 Specialist Lesson Plan Outlines | [training_management/lesson_plans/TM40_SPECIALIST_LESSON_PLAN_OUTLINES.md](training_management/lesson_plans/TM40_SPECIALIST_LESSON_PLAN_OUTLINES.md) |

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
| TM-40I | [syllabi/SYLLABUS_TM40I.md](syllabi/SYLLABUS_TM40I.md) | MLEs |
| TM-40J | [syllabi/SYLLABUS_TM40J.md](syllabi/SYLLABUS_TM40J.md) | PMs, G8/S8 |
| TM-40K | [syllabi/SYLLABUS_TM40K.md](syllabi/SYLLABUS_TM40K.md) | KMOs, 37F |
| TM-40L | [syllabi/SYLLABUS_TM40L.md](syllabi/SYLLABUS_TM40L.md) | SWEs |

> **Note:** TM-50 series syllabi not yet published. TM-50 instruction is managed through the MTP. Contact training management for scheduling.

---

## Supporting Reference Material

| Resource | File | Notes |
|----------|------|-------|
| MSS Quick Start | [QUICK_START.md](QUICK_START.md) | 30-minute onboarding |
| Naming & Governance Standards | [standards/NAMING_AND_GOVERNANCE_STANDARDS.md](standards/NAMING_AND_GOVERNANCE_STANDARDS.md) | USAREUR-AF MSS naming conventions and governance checklists |
| MSS Training Hub (web) | [mss_info_app/index.html](mss_info_app/index.html) | Standalone HTML training hub — open in browser |
| Practical Exercises | [exercises/](exercises/) | Hands-on packages for TM-10 through TM-40L |
| Foundry Python Patterns | [data_skills/13_foundry_patterns/](../data_skills/13_foundry_patterns/) | Local shim for offline development and testing |
| Full data science reference library | [data_skills/](../data_skills/) | 15 modules: Python → ML → ETL → deployment |
| SITREP Tracker (applied project) | [sitrep_tracker/](../sitrep_tracker/) | Click + Rich + SQLite reference implementation |

---

## Quick-Reference Training Paths

### New Soldier joining the data team

1. If O-5+: read [Data Literacy for Senior Leaders](doctrine/DATA_LITERACY_senior_leaders.md)
2. Skim [Data Literacy Technical Reference](doctrine/DATA_LITERACY_technical_reference.md) Ch 1–3 and Ch 8
3. Complete [TM-10](tm/TM_10_maven_user/TM_10_MAVEN_USER.md)
4. Request MSS access; practice navigation tasks
5. If building: complete [TM-20](tm/TM_20_builder/TM_20_BUILDER.md)
6. WFF functional staff: proceed to TM-40A–F per function (after TM-20)
7. Data specialists: complete [TM-30](tm/TM_30_advanced_builder/TM_30_ADVANCED_BUILDER.md) after TM-20
8. Technical specialists: proceed to TM-40G–L per role (after TM-30)

### S6 shop standing up MSS capability

1. Commander reads Data Literacy for Senior Leaders
2. All staff complete TM-10
3. Designated builders complete TM-20
4. Designated data leads complete TM-30
5. Reference Glossary throughout
6. Technical specialists proceed to TM-40G–L per role
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
| G9/Civil Affairs | TM-40J (PM) or TM-40K (KM) |
| Data scientist (GS/contractor) | TM-40G (ORSA) or TM-40I (MLE) |
| AI/ML engineer (GS/contractor) | TM-40H (AI Eng) or TM-40I (MLE) |
| KMO / Knowledge Officer | TM-40K (KM) |
| PM / Program Manager | TM-40J (PM) |

---

*USAREUR-AF Operational Data Team — UNCLASSIFIED*
*Version 5.0 | March 2026 | TM-40 WFF and Technical Specialist tracks complete; TM-50 series complete | Supersedes v4.0*
