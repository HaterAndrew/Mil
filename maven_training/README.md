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

## How to Use This Curriculum

### Step 1 — Know Your Level

| Level | You Are... | Start Here |
|-------|-----------|------------|
| All personnel | A Soldier, officer, or civilian who uses MSS to access operational data | TM-10 |
| All staff, light builders | Building dashboards, forms, or basic pipelines on MSS | TM-20 (after TM-10) |
| Data-adjacent specialists | Assigned to a data/analytical role (17/25-series, S6/G6, G2/G9) | TM-30 (after TM-20) |
| Developers / technical specialists | Writing code, building external apps, ML models | TM-40 (track) after TM-30 |
| Senior leaders (O-5+, CSM+) | Commanding or directing a data-capable formation | ADP 1 |
| All — background reading | Anyone who wants to understand data concepts before touching MSS | ADRP 1 |

### Step 2 — Read the Right Publications

```
Senior Leaders ──────────────────────────► ADP 1 (Data Literacy for Senior Leaders)
                                                │
                                                ▼
All Personnel ───────────────────────────► ADRP 1 (Data Literacy Reference) [recommended]
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
                         Developer tracks           Non-developer tracks
                         (prereq: TM-30)            (prereq: TM-20)
                         TM-40A (ORSA)              TM-40D (PM)
                         TM-40B (AI Eng)            TM-40E (KM)
                         TM-40C (MLE)
                         TM-40F (SWE)
                                    │
                                    ▼
                         [FUTURE] TM-50 series (advanced, per track)
```

### Step 3 — Reference the Glossary

At any point, consult the [Data & Foundry Glossary](doctrine/GLOSSARY_data_foundry.md) to translate between general data concepts and MSS/Foundry terminology.

---

## Publications Index

### Doctrine Publications

| Publication | File | Audience | Purpose |
|-------------|------|----------|---------|
| **ADP 1** — Data Literacy for Senior Leaders | [doctrine/ADP_1_data_literacy_senior.md](doctrine/ADP_1_data_literacy_senior.md) | O-5+, CSM+, Senior Civilians | Principles, command responsibilities, evaluating data products |
| **ADRP 1** — Data Literacy | [doctrine/ADRP_1_data_literacy.md](doctrine/ADRP_1_data_literacy.md) | All personnel | Comprehensive data literacy reference — platform-agnostic |
| **Glossary** — Data & Foundry Terms | [doctrine/GLOSSARY_data_foundry.md](doctrine/GLOSSARY_data_foundry.md) | All personnel | Equates general data concepts to MSS/Foundry terminology |

### Technical Manuals (Platform-Specific)

| Publication | File | Audience | Prerequisite |
|-------------|------|----------|--------------|
| **TM-10** — Maven User | [tm/TM_10_maven_user/TM_10_MAVEN_USER.md](tm/TM_10_maven_user/TM_10_MAVEN_USER.md) | All staff | None |
| **TM-20** — Builder | [tm/TM_20_builder/TM_20_BUILDER.md](tm/TM_20_builder/TM_20_BUILDER.md) | All staff | TM-10 |
| **TM-30** — Advanced Builder | [tm/TM_30_advanced_builder/TM_30_ADVANCED_BUILDER.md](tm/TM_30_advanced_builder/TM_30_ADVANCED_BUILDER.md) | Data-adjacent specialists | TM-10, TM-20 |

### TM-40 Series — Technical Specialist Tracks (Prerequisite: TM-30)

| Publication | File | Audience | Prerequisite |
|-------------|------|----------|--------------|
| **TM-40A** — ORSA | [tm/TM_40A_orsa/TM_40A_ORSA.md](tm/TM_40A_orsa/TM_40A_ORSA.md) | Operations Research analysts | TM-30 |
| **TM-40B** — AI Engineer | [tm/TM_40B_ai_engineer/TM_40B_AI_ENGINEER.md](tm/TM_40B_ai_engineer/TM_40B_AI_ENGINEER.md) | AI/ML specialists | TM-30 |
| **TM-40C** — Machine Learning Engineer | [tm/TM_40C_ml_engineer/TM_40C_ML_ENGINEER.md](tm/TM_40C_ml_engineer/TM_40C_ML_ENGINEER.md) | MLEs | TM-30 |
| **TM-40D** — Program Manager | [tm/TM_40D_program_manager/TM_40D_PROGRAM_MANAGER.md](tm/TM_40D_program_manager/TM_40D_PROGRAM_MANAGER.md) | PMs, resource managers, G8/S8 | TM-20 |
| **TM-40E** — Knowledge Manager | [tm/TM_40E_knowledge_manager/TM_40E_KNOWLEDGE_MANAGER.md](tm/TM_40E_knowledge_manager/TM_40E_KNOWLEDGE_MANAGER.md) | KMOs, 37F, S2/S3/S6 KM roles | TM-20 |
| **TM-40F** — Software Engineer | [tm/TM_40F_software_engineer/TM_40F_SOFTWARE_ENGINEER.md](tm/TM_40F_software_engineer/TM_40F_SOFTWARE_ENGINEER.md) | SWEs | TM-30 |

### Planned Publications (Not Yet Produced)

| Publication | Audience | Notes |
|-------------|----------|-------|
| **TM-50A–F** — Advanced Developer Tracks | Senior developers (all tracks) | Advanced versions of each TM-40 track |

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

---

## Supporting Reference Material

| Resource | Location | Notes |
|----------|----------|-------|
| Foundry Python Patterns (runnable code) | [data_skills/13_foundry_patterns/](../data_skills/13_foundry_patterns/) | Local shim for offline development and testing |
| Full data science reference library | [data_skills/](../data_skills/) | 15 modules: Python → ML → ETL → deployment |
| SITREP Tracker (applied project) | [sitrep_tracker/](../sitrep_tracker/) | Click + Rich + SQLite — reference implementation |

---

## Quick-Reference Training Path

### For a New Soldier joining the data team:
1. Read [ADP 1](doctrine/ADP_1_data_literacy_senior.md) if O-5+; skip if not
2. Skim [ADRP 1](doctrine/ADRP_1_data_literacy.md) Ch 1-3 and Ch 8
3. Complete [TM-10](tm/TM_10_maven_user/TM_10_MAVEN_USER.md) cover to cover
4. Request MSS access; practice navigation tasks
5. If building: complete [TM-20](tm/TM_20_builder/TM_20_BUILDER.md)
6. If data specialist: complete [TM-30](tm/TM_30_advanced_builder/TM_30_ADVANCED_BUILDER.md) after TM-20

### For an S6 shop standing up MSS capability:
1. Commander reads ADP 1
2. All staff complete TM-10
3. Designate builders: complete TM-20
4. Designate data leads: complete TM-30
5. Reference Glossary throughout

---

*USAREUR-AF Operational Data Team — UNCLASSIFIED*
*Version 2.0 | Compiled [Current Year] | Supersedes previous MAVEN_FIELD_MANUAL.md*
