# USAREUR-AF Operational Data Team

```
HEADQUARTERS
UNITED STATES ARMY EUROPE AND AFRICA
Wiesbaden, Germany
```

**Distribution:** Approved for public release; distribution is unlimited.

---

## Repository Overview

This repository contains the Maven Smart System (MSS) training curriculum, data science reference library, and supporting tools for the USAREUR-AF Operational Data Team.

---

## Contents

### [Maven Training Curriculum](maven_training/)

Doctrine-aligned training for all USAREUR-AF personnel who access, build on, or lead with the Maven Smart System. Organized by audience and role.

Full curriculum index: [maven_training/README.md](maven_training/README.md)

#### TM-40 Track Selection (Quick Reference)

| Your Role | Track |
|---|---|
| All personnel | TM-10 → TM-20 |
| WFF functional staff (INT/FIRES/M2/SUST/PROT/MC) | TM-40A–F (after TM-30) |
| Data-adjacent specialists (17/25-series, S6/G6, G2) | TM-30 → TM-40G–M |
| Technical specialists (engineers, analysts, data pros) | TM-30 → TM-40G–M → TM-50G–M |
| Senior leaders (O-5+, CSM+, senior civilians) | Data Literacy for Senior Leaders |

#### Complete Publication Hierarchy

```
maven_training/
│
├── QUICK_START.md                            ← 30-min onboarding for new MSS users
│
├── doctrine/                                 ← Doctrine publications (platform-agnostic)
│   ├── DATA_LITERACY_technical_reference.md  ← Comprehensive data literacy ref (all personnel)
│   ├── DATA_LITERACY_senior_leaders.md       ← Command-level decision framework (O-5+/CSM+)
│   └── GLOSSARY_data_foundry.md             ← Data ↔ Foundry term equivalency glossary
│
├── tm/                                       ← Technical Manuals (platform-specific)
│   │
│   ├── TM_10_maven_user/                     ← TM-10: All personnel — access & consume data
│   │   └── TM_10_MAVEN_USER.md
│   ├── TM_20_builder/                        ← TM-20: All staff — no-code building
│   │   └── TM_20_BUILDER.md
│   ├── TM_30_advanced_builder/               ← TM-30: Data-adjacent specialists
│   │   └── TM_30_ADVANCED_BUILDER.md
│   │
│   │   ── TM-40A through TM-40F: Warfighting Function Tracks (prereq: TM-30) ──
│   ├── TM_40A_intelligence/                  ← TM-40A: Intelligence (INT) WFF
│   │   ├── TM_40A_INTELLIGENCE.md
│   │   └── CONCEPTS_GUIDE_TM40A_INTELLIGENCE.md
│   ├── TM_40B_fires/                         ← TM-40B: Fires WFF
│   │   ├── TM_40B_FIRES.md
│   │   └── CONCEPTS_GUIDE_TM40B_FIRES.md
│   ├── TM_40C_movement_maneuver/             ← TM-40C: Movement & Maneuver (M2) WFF
│   │   ├── TM_40C_MOVEMENT_MANEUVER.md
│   │   └── CONCEPTS_GUIDE_TM40C_MOVEMENT_MANEUVER.md
│   ├── TM_40D_sustainment/                   ← TM-40D: Sustainment WFF
│   │   ├── TM_40D_SUSTAINMENT.md
│   │   └── CONCEPTS_GUIDE_TM40D_SUSTAINMENT.md
│   ├── TM_40E_protection/                    ← TM-40E: Protection WFF
│   │   ├── TM_40E_PROTECTION.md
│   │   └── CONCEPTS_GUIDE_TM40E_PROTECTION.md
│   ├── TM_40F_mission_command/               ← TM-40F: Mission Command (MC) WFF
│   │   ├── TM_40F_MISSION_COMMAND.md
│   │   └── CONCEPTS_GUIDE_TM40F_MISSION_COMMAND.md
│   │
│   │   ── TM-40G through TM-40L: Technical Specialist Tracks (prereq: TM-30) ──
│   ├── TM_40G_orsa/                          ← TM-40G: ORSA (FA49, quantitative analysts)
│   │   ├── TM_40G_ORSA.md
│   │   └── CONCEPTS_GUIDE_TM40G_ORSA.md
│   ├── TM_40H_ai_engineer/                   ← TM-40H: AI Engineer (AIP Logic, agents)
│   │   ├── TM_40H_AI_ENGINEER.md
│   │   └── CONCEPTS_GUIDE_TM40H_AI_ENGINEER.md
│   ├── TM_40M_ml_engineer/                   ← TM-40M: Machine Learning Engineer
│   │   ├── TM_40M_ML_ENGINEER.md
│   │   └── CONCEPTS_GUIDE_TM40M_ML_ENGINEER.md
│   ├── TM_40J_program_manager/               ← TM-40J: Program Manager (G8/S8, tech PMs)
│   │   ├── TM_40J_PROGRAM_MANAGER.md
│   │   └── CONCEPTS_GUIDE_TM40J_PROGRAM_MANAGER.md
│   ├── TM_40K_knowledge_manager/             ← TM-40K: Knowledge Manager (KMO, 37F)
│   │   ├── TM_40K_KNOWLEDGE_MANAGER.md
│   │   └── CONCEPTS_GUIDE_TM40K_KNOWLEDGE_MANAGER.md
│   ├── TM_40L_software_engineer/             ← TM-40L: Software Engineer (OSDK, TypeScript)
│   │   ├── TM_40L_SOFTWARE_ENGINEER.md
│   │   └── CONCEPTS_GUIDE_TM40L_SOFTWARE_ENGINEER.md
│   │
│   │   ── TM-50G through TM-50L: Advanced Specialist Tracks (prereq: corresponding TM-40G–M) ──
│   ├── TM_50G_orsa_advanced/                 ← TM-50G: Advanced ORSA (prereq: TM-40G)
│   │   ├── TM_50G_ORSA_ADVANCED.md
│   │   └── CONCEPTS_GUIDE_TM50G_ORSA_ADVANCED.md
│   ├── TM_50H_ai_engineer_advanced/          ← TM-50H: Advanced AI Engineer (prereq: TM-40H)
│   │   ├── TM_50H_AI_ENGINEER_ADVANCED.md
│   │   └── CONCEPTS_GUIDE_TM50H_AI_ENGINEER_ADVANCED.md
│   ├── TM_50M_ml_engineer_advanced/          ← TM-50M: Advanced MLE (prereq: TM-40M)
│   │   ├── TM_50M_ML_ENGINEER_ADVANCED.md
│   │   └── CONCEPTS_GUIDE_TM50M_ML_ENGINEER_ADVANCED.md
│   ├── TM_50J_program_manager_advanced/      ← TM-50J: Advanced PM (prereq: TM-40J)
│   │   ├── TM_50J_PROGRAM_MANAGER_ADVANCED.md
│   │   └── CONCEPTS_GUIDE_TM50J_PROGRAM_MANAGER_ADVANCED.md
│   ├── TM_50K_knowledge_manager_advanced/    ← TM-50K: Advanced KM (prereq: TM-40K)
│   │   ├── TM_50K_KNOWLEDGE_MANAGER_ADVANCED.md
│   │   └── CONCEPTS_GUIDE_TM50K_KNOWLEDGE_MANAGER_ADVANCED.md
│   └── TM_50L_software_engineer_advanced/    ← TM-50L: Advanced SWE (prereq: TM-40L)
│       ├── TM_50L_SOFTWARE_ENGINEER_ADVANCED.md
│       └── CONCEPTS_GUIDE_TM50L_SOFTWARE_ENGINEER_ADVANCED.md
│
├── syllabi/                                  ← Student/instructor-facing course syllabi
│   ├── SYLLABUS_TM10.md
│   ├── SYLLABUS_TM20.md
│   ├── SYLLABUS_TM30.md
│   ├── SYLLABUS_TM40A.md                     ← WFF track: Intelligence
│   ├── SYLLABUS_TM40B.md                     ← WFF track: Fires
│   ├── SYLLABUS_TM40C.md                     ← WFF track: Movement & Maneuver
│   ├── SYLLABUS_TM40D.md                     ← WFF track: Sustainment
│   ├── SYLLABUS_TM40E.md                     ← WFF track: Protection
│   ├── SYLLABUS_TM40F.md                     ← WFF track: Mission Command
│   ├── SYLLABUS_TM40G.md                     ← Technical: ORSA
│   ├── SYLLABUS_TM40H.md                     ← Technical: AI Engineer
│   ├── SYLLABUS_TM40M.md                     ← Technical: ML Engineer
│   ├── SYLLABUS_TM40J.md                     ← Technical: Program Manager
│   ├── SYLLABUS_TM40K.md                     ← Technical: Knowledge Manager
│   ├── SYLLABUS_TM40L.md                     ← Technical: Software Engineer
│   ├── SYLLABUS_TM50G.md                     ← Advanced: ORSA
│   ├── SYLLABUS_TM50H.md                     ← Advanced: AI Engineer
│   ├── SYLLABUS_TM50M.md                     ← Advanced: ML Engineer
│   ├── SYLLABUS_TM50J.md                     ← Advanced: Program Manager
│   ├── SYLLABUS_TM50K.md                     ← Advanced: Knowledge Manager
│   └── SYLLABUS_TM50L.md                     ← Advanced: Software Engineer
│
├── exercises/
│   ├── README.md
│   ├── exams/                                ← Pre- and post-tests (diagnostic + summative)
│   │   ├── EXAM_TM10_PRE.md / POST.md
│   │   ├── EXAM_TM20_PRE.md / POST.md
│   │   ├── EXAM_TM30_PRE.md / POST.md
│   │   ├── EXAM_TM40A_PRE.md / POST.md       ← WFF: Intelligence
│   │   ├── EXAM_TM40B_PRE.md / POST.md       ← WFF: Fires
│   │   ├── EXAM_TM40C_PRE.md / POST.md       ← WFF: Movement & Maneuver
│   │   ├── EXAM_TM40D_PRE.md / POST.md       ← WFF: Sustainment
│   │   ├── EXAM_TM40E_PRE.md / POST.md       ← WFF: Protection
│   │   ├── EXAM_TM40F_PRE.md / POST.md       ← WFF: Mission Command
│   │   ├── EXAM_TM40G_PRE.md / POST.md       ← Technical: ORSA
│   │   ├── EXAM_TM40H_PRE.md / POST.md       ← Technical: AI Engineer
│   │   ├── EXAM_TM40M_PRE.md / POST.md       ← Technical: ML Engineer
│   │   ├── EXAM_TM40J_PRE.md / POST.md       ← Technical: Program Manager
│   │   ├── EXAM_TM40K_PRE.md / POST.md       ← Technical: Knowledge Manager
│   │   ├── EXAM_TM40L_PRE.md / POST.md       ← Technical: Software Engineer
│   │   ├── EXAM_TM50G_PRE.md / POST.md       ← Advanced: ORSA
│   │   ├── EXAM_TM50H_PRE.md / POST.md       ← Advanced: AI Engineer
│   │   ├── EXAM_TM50M_PRE.md / POST.md       ← Advanced: ML Engineer
│   │   ├── EXAM_TM50J_PRE.md / POST.md       ← Advanced: Program Manager
│   │   ├── EXAM_TM50K_PRE.md / POST.md       ← Advanced: Knowledge Manager
│   │   └── EXAM_TM50L_PRE.md / POST.md       ← Advanced: Software Engineer
│   │
│   ├── EX_10_operator_basics/                ← Practical exercise: TM-10
│   │   ├── ENVIRONMENT_SETUP.md
│   │   └── EXERCISE.md
│   ├── EX_20_no_code_builder/                ← Practical exercise: TM-20
│   ├── EX_30_advanced_builder/               ← Practical exercise: TM-30
│   ├── EX_40A_intelligence/                  ← Practical exercise: TM-40A (WFF)
│   ├── EX_40B_fires/                         ← Practical exercise: TM-40B (WFF)
│   ├── EX_40C_movement_maneuver/             ← Practical exercise: TM-40C (WFF)
│   ├── EX_40D_sustainment/                   ← Practical exercise: TM-40D (WFF)
│   ├── EX_40E_protection/                    ← Practical exercise: TM-40E (WFF)
│   ├── EX_40F_mission_command/               ← Practical exercise: TM-40F (WFF)
│   ├── EX_40G_orsa/                          ← Practical exercise: TM-40G (Technical)
│   ├── EX_40H_ai_engineer/                   ← Practical exercise: TM-40H (Technical)
│   ├── EX_40M_ml_engineer/                   ← Practical exercise: TM-40M (Technical)
│   ├── EX_40J_program_manager/               ← Practical exercise: TM-40J (Technical)
│   ├── EX_40K_knowledge_manager/             ← Practical exercise: TM-40K (Technical)
│   └── EX_40L_software_engineer/             ← Practical exercise: TM-40L (Technical)
│
├── training_management/                      ← Administrative and instructor publications
│   ├── MTP_MSS.md                            ← Mission Training Plan (TLOs/ELOs, Go/No-Go criteria)
│   ├── POI_MSS.md                            ← Program of Instruction
│   ├── CAD_MSS.md                            ← Course Administrative Data
│   ├── TEO_MSS.md                            ← Training and Evaluation Outline
│   ├── ANNUAL_TRAINING_SCHEDULE.md
│   ├── ENROLLMENT_SOP.md
│   ├── COMPLETION_CERTIFICATE.md
│   ├── FACULTY_DEVELOPMENT_PLAN.md
│   ├── POLICY_LETTER.md
│   ├── CURRICULUM_MAINTENANCE_SOP.md
│   ├── AAR_TEMPLATE.md
│   └── lesson_plans/
│       ├── LP_TEMPLATE.md                    ← Blank lesson plan template
│       ├── TM20_LESSON_PLAN_OUTLINES.md
│       ├── TM30_LESSON_PLAN_OUTLINES.md
│       ├── TM40_SPECIALIST_LESSON_PLAN_OUTLINES.md
│       └── TM10/
│           └── TM10_LESSON_PLANS.md
│
├── standards/
│   └── NAMING_AND_GOVERNANCE_STANDARDS.md    ← USAREUR-AF MSS naming conventions & governance
│
├── quick_reference/
│   └── cheatsheet.md                         ← Quick-reference card (all levels)
│
├── mss_info_app/                             ← Standalone HTML training hub (Workshop-embeddable)
│   ├── index.html
│   └── training_schedule.html
│
├── pdf/                                      ← Generated PDFs for distribution (one per source doc)
│
└── _archive/                                 ← Retired source documents (deprecated, do not use)
    ├── palantir_foundry_field_manual.md
    └── MAVEN_FIELD_MANUAL.md
```

> **TM-40 Series Note:** The TM-40 series has two distinct sub-series. Do not assume a track based on letter alone.
> - **TM-40A through TM-40F** — Warfighting Function (WFF) tracks. Audience: functional staff in the six WFFs. Prerequisite: TM-30.
> - **TM-40G through TM-40L** — Technical Specialist tracks. Prerequisite: TM-30.

#### TM-40 WFF Tracks — What Each Track Covers

These tracks are for functional staff who work *within* a WFF and need MSS skills tailored to their operational domain. All six require TM-30 as a hard prerequisite (TM-10 → TM-20 → TM-30 complete, all Go evaluations on file).

| Track | WFF | Primary Audience | MSS Focus |
|---|---|---|---|
| **TM-40A** | Intelligence (INT) | G2/S2, MI Officers, 35-series | PIR/CCIR management, INTSUM pipelines, threat pattern analysis, Named Area of Interest monitoring |
| **TM-40B** | Fires | FA Officers, 13-series, FSO/FSCOORD | Target acquisition data, FSCM tracking, D3A confidence scoring, MOE/MOP for fires effects |
| **TM-40C** | Movement & Maneuver | Maneuver Officers, 11/19-series, ALO | Route analysis, traffic/mobility data, unit position tracking, obstacle and gap assessment |
| **TM-40D** | Sustainment | G4/S4, 88/92/25-series, BSB | Supply readiness dashboards, Class IX/fuel consumption, maintenance pipeline, distribution analysis |
| **TM-40E** | Protection | G3/S3 protection cell, CBRN, 31-series | Force protection metrics, CCIR monitoring, threat/incident tracking, access control data |
| **TM-40F** | Mission Command (MC) | G3/S3, XO/S3-shop, Battle Captains | Operations dashboard design, SITREP/SPOTREP pipelines, battle rhythm data, cross-WFF integration |

Each WFF track pairs a Technical Manual (TM) with a Concepts Guide that explains the domain-specific data logic behind the MSS tasks. See [maven_training/README.md](maven_training/README.md) for full syllabi, exercises, and exam files per track.

---

### [Data Skills Reference Library](skills/data_skills/)

15-module Python curriculum covering the full data engineering and analytics stack. Used as a reference for TM-30/40-level technical work.

| Module | Topic |
|---|---|
| 01–05 | Python, Pandas, SQL, Visualization, Statistics |
| 06–10 | ML, Time Series, ETL Pipelines, Data Quality, End-to-End |
| 11–12 | FastAPI, Testing (pytest) |
| 13 | Foundry Patterns (runnable shim — transforms, ontology, checks) |
| 14–15 | Streamlit Dashboards, Deployment (Docker) |

Activate venv: `source data_skills/.venv/bin/activate`

---

### [SITREP Tracker](sitrep_tracker/)

Applied CLI project demonstrating SQLite, Click, Rich, and DTG utilities. Reference implementation for TM-20/30 pipeline and reporting patterns.

**Install and run:**

```bash
# Option A — install as a package (recommended, works from any directory)
pip install -e .
sitrep --help

# Option B — run directly from the sitrep_tracker/ directory
cd sitrep_tracker/
python3 cli.py --help
```

**Dev setup — restore data_skills symlink** (required after a fresh clone, since `data_skills/` is gitignored):

```bash
ln -sf "$(pwd)/sitrep_tracker" data_skills/projects/sitrep_tracker
```

---

### [Skills Library](skills/)

Third-party Claude Code skill collections organized for operational data work. Includes Anthropic official skills (pdf, xlsx, docx, pptx), engineering skills, scientific/geospatial skills, and PM toolkits.

See [skills/INDEX.md](skills/INDEX.md) for the full catalog and activation instructions.

---

## Deploying the Training Hub to Foundry Workshop

The [MSS Training Hub](maven_training/mss_info_app/index.html) is a self-contained HTML application suitable for hosting in Palantir Foundry Workshop as an embedded module.

### Option A — Embed via Code Repository (recommended)

1. **Push this repository to a Foundry Code Repository** (or sync an existing one).
2. In Foundry, navigate to the code repo and confirm `maven_training/mss_info_app/index.html` is present.
3. Open or create your **Workshop** application in the MSS Foundry environment.
4. Add a new layout panel and insert an **Embed** widget.
5. Set the embed source to the static file URL for `index.html` served from the code repository. The URL follows the pattern:
   ```
   /static/<repo-rid>/maven_training/mss_info_app/index.html
   ```
   Replace `<repo-rid>` with your code repository's resource identifier (visible in the repo's URL bar).
6. Set the panel to **full-height** / **no padding** for the best viewing experience.
7. Save and publish the Workshop application. Assign access via Foundry's permission panel to the appropriate groups (e.g., `usareur-af-mss-users`).

### Option B — Inline HTML widget

Use this if you cannot serve static files from a code repository.

1. Open your Workshop application.
2. Add an **HTML** widget to the canvas.
3. Paste the full contents of `maven_training/mss_info_app/index.html` into the widget's HTML editor.
4. Note: some browsers may restrict inline `<script>` execution depending on the Foundry tenant's Content Security Policy. Test interactivity before publishing.

### Notes

- The HTML file is fully self-contained — no external CDN calls, no server-side dependencies.
- Links within the hub that point to TM markdown files will not resolve inside Workshop. If live document links are needed, host the PDFs as Foundry media objects and update the `href` values in `index.html` before embedding.
- For access control, do not use the Workshop app's sharing URL as a substitute for Foundry group permissions.

---

## Standards

- [Naming and Governance Standards](maven_training/standards/NAMING_AND_GOVERNANCE_STANDARDS.md) — USAREUR-AF MSS naming conventions referenced throughout the TM series

---

## Security

All work in this repository is governed by [CLAUDE.md](CLAUDE.md). Key requirements:
- Do not commit operational data, credentials, or connection strings
- Parameterize all SQL — never f-string queries
- Validate at ingestion boundaries
- Do not push to remote without explicit instruction

---

*USAREUR-AF Operational Data Team*
*Version 3.0 | March 2026*
