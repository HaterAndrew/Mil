# MAVEN TRAINING CORPUS — DEPENDENCY MAP
## USAREUR-AF Operational Data Team | C2DAO Training Branch

**Generated:** 13 March 2026
**Last updated:** 16 March 2026 (final editing pass: EXAM_TM10_POST → EXAM_TM10_SUPPLEMENTAL; ANNUAL_TRAINING_CALENDAR_FY27.html added; INSTRUCTOR_OVERVIEW.md integrated; stale refs cleaned across dep map, exercises README, generate_dep_map.py, audit.py, PILOT_AGENT_PROMPT)
**Audit method:** Full manual read of all source files across 6 parallel agent passes (13 March); ralf branch content migration (14 March); Palantir Developers video mapping (14 March); full ralf file inventory and PDF build (14 March); full content read of all 30 CDA slide decks (14 March) — level assignments corrected corpus-wide; pre-v2.0 content accuracy and consistency audit across all curriculum, app, widget, and PPTX files (14 March)
**Status at generation:** Corpus at v2.0-ready state. All naming and content issues resolved. TM-40D/E/F prereq discrepancy resolved 2026-03-14 — all WFF tracks (TM-40A–F) now require TM-30 as terminal prerequisite. Pre-v2.0 audit complete: 8 content fixes applied (README.md, POLICY_LETTER.md, cheatsheet.md, Home.tsx, TM40.tsx, mss_info_app/index.html, .gitignore, MSS_Project_Overview.pptx); MSS_Training_Progression.pptx specialist column fully rebuilt with clean WFF (A–F) / Specialist (G–L) grouping. PDFs regenerated (3 source-changed files rebuilt). See changelog entry #95–103.

---

## READING THIS MAP

**Relationship symbols:**
- **→** requires / directly depends on
- **↔** companion / integration reference (not a prereq)
- **⇢** recommended reading for

**Publication type tags:**

| Tag | Type | Description |
|-----|------|-------------|
| **[COURSE]** | Course & Assessment | TM (Technical Manual), Syllabus, Exercise, Exam, Concepts Guide — anything a student completes or is evaluated against |
| **[PPT]** | Slide Deck | CDA slide deck (conceptual prereq; `maven_training/source_material/course_portal/`) |
| **[REF]** | Reference | Quick-reference tools, cheatsheets, job aids — consulted during work, not studied (`maven_training/quick_reference/`) |
| **[SUPP]** | Supplemental | Supporting doctrine, guidance, or architecture docs that enrich understanding but are not part of the course sequence (`maven_training/doctrine/`, `source_material/cda_docs/`) |
| **[EA]** | Enterprise Architecture | EA series docs (`maven_training/doctrine/enterprise_architecture/`) |
| **[CANON]** | CDA Canon | CDA canon and doctrine docs (`maven_training/doctrine/cda_doctrine/`) |

---

## PREREQUISITE CHAIN (AUTHORITATIVE)

```
TM-10 (all personnel)
  └── TM-20 (builders)
        │
        ├── [BSP] Builder Sprint ← parallel track; outside TM chain; no TM credit granted
        │         Prereq: TM-20 Go + command-validated project. See builder_sprint/BSP_GUIDE.md
        │
        └── TM-30 (advanced builders / data-adjacent)
              ├── TM-40A (Intelligence WFF)
              ├── TM-40B (Fires WFF)
              ├── TM-40C (Movement & Maneuver WFF)
              ├── TM-40D (Sustainment WFF)
              ├── TM-40E (Protection WFF)
              ├── TM-40F (Mission Command WFF)
              ├── TM-40G (ORSA) ──────────────→ TM-50G (Advanced ORSA)
              ├── TM-40H (AI Engineer) ────────→ TM-50H (Advanced AI Eng)
              ├── TM-40I (ML Engineer) ────────→ TM-50I (Advanced ML Eng)
              ├── TM-40J (Program Manager) ────→ TM-50J (Advanced PM)
              ├── TM-40K (Knowledge Manager) ──→ TM-50K (Advanced KM)
              └── TM-40L (Software Engineer) ──→ TM-50L (Advanced SWE)
```

> **NOTE:** TM-50A through TM-50F do NOT exist. Only TM-50G–L (advanced specialist) are valid.
> WFF tracks (TM-40A–F) require TM-30 (same prereq chain as Specialist tracks) — design decision 2026-03-13.
> Specialist tracks (TM-40G–L) all require TM-30 (required, not recommended).
> **Builder Sprint (BSP)** is a separate quarterly event outside the TM chain. Prereq: TM-20. Does NOT grant TM-30 credit. Does NOT unlock TM-40 enrollment. See training_management/BUILDER_SPRINT_SOP.md.

---

## CDA SLIDE LIBRARY OVERLAY (CONCEPTUAL PREREQS)

The CDA slide decks provide conceptual grounding that the TM series assumes but does not teach.
They are recommended reading, not required prerequisites. They feed into the TM chain as follows.

**Last alignment audit:** 14 March 2026 — full content read of all 30 decks; level assignments
corrected based on actual slide content vs. TM audience (user / no-code builder / advanced builder / code-level).

```
CDA "TM-10" (2 decks) ──────────────⇢ TM-10 / all personnel
  army_data_orientation_v1             ⇢ TM-10 — WHY MSS exists; Army data landscape; all personnel
                                           v2 (army_data_orientation_v2.pptx) patches slides 12–14
                                           for end-user (consumer) audience; v1 had builder framing
  mss_platform_overview                ⇢ TM-10 — NEW (2026-03-14): HOW to use MSS as an end user
                                           Covers: platform navigation, reading dashboards, AIP
                                           queries, submitting forms, classification handling,
                                           problem reporting, user vs. builder boundary
                                           File: source_material/course_portal/downloads/mss_platform_overview.pptx

CDA "Intro To Data" (10 decks) ─────⇢ TM-20 (conceptual prereqs for no-code builders)
  architecture_primer                  ⇢ before TM-20 (stability stack, activities vs enablers)
                                           [was tagged TM-10 — wrong; no end-user content]
  2026_Data_Stack_Deep_Dive            ⇢ before TM-20 (five-layer L1–L5 stack overview)
  AI_ML_Beyond_The_Hype               ⇢ TM-20 (what AI actually is; why clean ontology enables AIP)
                                           [was tagged TM-40H — wrong; no code content; TM-20 builders
                                           need this to understand why good data enables AIP]
  The_Semantic_Layer_Instructions      ⇢ TM-20 (slides 1–6) / TM-30 (slides 7–11 governance content)
  What_Is_An_Ontology                  ⇢ TM-20 (three building blocks, definition clarity test)
  L5_Activation_Interface_Deep_Dive    ⇢ TM-20 (Workshop/activation decision framework slides 1–5)
                                           NOTE: slides 6–9 (Custom React Widgets, Streamlit, Plotly)
                                           are TM-40L content — not TM-20
  Dont_Filter_This_Isnt_Excel          ⇢ TM-20 (platform mindset shift; essential for all builders)
  L2_Ingestion_Integration_Deep_Dive   ⇢ TM-30 (CDC, DAGs, orchestration, schema evolution)
                                           [was tagged TM-20 — wrong; no-code builders don't design CDC]
  Data_Modeling_Foundations            ⇢ TM-30 (Kimball, Inmon, DataVault, Enterprise Compass)
                                           [was tagged TM-20 — wrong; too academic for no-code builders]
  Data_Platforms_Cloud_Deep_Dive       ⇢ TM-30 (JWCC, cross-domain, edge, OCONUS design concerns)
                                           [was tagged TM-20 — slides 1–4 fine at TM-20 but 5–10 are TM-30]
  decision_advantage_deep_dive         ⇢ TM-30 / all WFF tracks TM-40A–F (ADP 3-13 doctrine framework;
                                           decision-as-node-graph; maps to Foundry object types)
                                           [was tagged TM-40A — wrong; not Intel-WFF-specific; no code]

CDA "Data 101" (6 decks) ────────────⇢ TM-20 / TM-30
  The_Four_Layers                      ⇢ TM-20 (ontology vs dataset vs pipeline vs app; essential)
  Data_Modeling_Fundamentals_Level1    ⇢ TM-20 (tables, keys, cardinality, schemas, data types)
  ObjectType_WhatToWatchFor            ⇢ TM-20 (filter-as-type anti-pattern; downstream avalanche)
  Links_and_Relationships              ⇢ TM-20 (cardinality, direction, optionality)
  Controlled_Vocabularies              ⇢ TM-20 / TM-30 (needed before building first object type)
                                           [was tagged TM-30 only — should start at TM-20]
  Identity_Who_Owns_The_Key            ⇢ TM-20 / TM-30 (primary key authority, six rules, entity resolution)
                                           [was tagged TM-30 only — fundamentals needed at TM-20]

CDA "Data 201" (10 decks) ───────────⇢ TM-30 / TM-40G–L
  Semantic_Modelling_Course_Intro      ⇢ TM-30 / TM-40L (entry to 12-deck series; prereq: DM L2)
  Deck_01_Architecture_First_Principles ⇢ TM-30 / TM-40L (separation of concerns, stability stack)
  Deck_02_Scope_Engineering            ⇢ TM-30 (schema fit vs scope fit, fit scorecard)
  Deck_03_RDF_OWL_Foundations          ⇢ TM-30 (part of 12-deck series; RDF/OWL/SKOS/SHACL)
                                           [was tagged TM-40K — wrong; this is Deck 3 of the same
                                           series as Decks 1, 2, 4, 5, 6 which are all TM-30]
  Deck_04_Object_Type_Varieties        ⇢ TM-30 / TM-40L (nine canonical varieties, decision tree)
  Deck_05_Identity_Governance          ⇢ TM-30 / TM-40K (identity authority matrix, entity resolution arch)
  Deck_06_Relationship_Modeling        ⇢ TM-30 / TM-40L (reification, role patterns, SHACL constraints)
  Deck_07_Temporal_Bitemporal          ⇢ TM-30 (part of 12-deck series; event/state, bitemporal patterns)
                                           [was tagged TM-40G — wrong; temporal modeling is general TM-30;
                                           applies across all specializations not just ORSA]
  Data_Modeling_Fundamentals_Level2    ⇢ TM-40 general / TM-40G / TM-40I / TM-40L
                                           (Kimball/Inmon/DataVault comparison, Enterprise Compass)
  Deck_12_Capstone_Foundry             ⇢ TM-40 general (end-to-end ontology engineering capstone;
                                           prereq: Decks 1–11; bridges TM-30 theory → TM-40 practice)
                                           [was tagged TM-40G only — not ORSA-specific]
```

---

## SECTION 0B — CDA DOCTRINE AND REFERENCE MATERIALS

### Enterprise Architecture (TM-30 / TM-40K / TM-40L)
| File | Type | Supports |
|---|---|---|
| doctrine/enterprise_architecture/EA_00_REFERENCE_CARD.md | [EA] | → TM-30, TM-40K, TM-40L |
| doctrine/enterprise_architecture/EA_01_FOUNDATION.md | [EA] | → TM-30 (architecture thinking) |
| doctrine/enterprise_architecture/EA_02_SCHOOLS_OF_THOUGHT.md | [EA] | → TM-30, TM-40K |
| doctrine/enterprise_architecture/EA_03_ARTIFACTS_AND_VIEWS.md | [EA] | → TM-40K, TM-40L |
| doctrine/enterprise_architecture/EA_04_GOVERNANCE.md | [EA] | → TM-40K |
| doctrine/enterprise_architecture/EA_05_MILITARY_APPLICATION.md | [EA] | → TM-30, TM-40G–L |

### Senior Leader Guidance
| File | Type | Supports |
|---|---|---|
| doctrine/CG_GUIDANCE.md | [REF] | → TM-10, TM-20 (CG public doctrine; AUSA 2025, Green Notebook 2026) |

### CDA Doctrine (TM-40G–L)
| File | Type | Supports |
|---|---|---|
| doctrine/CDA_CONSTRAINTS_AND_DIRECTIVES.md | [CNCPT] | → TM-40G–L (12 operational constraints and directives governing CDA work) |
| doctrine/cda_doctrine/CDA_OVERVIEW.md | [CNCPT] | → TM-30 (bridge: CDA user taxonomy, enterprise index) |
| doctrine/cda_doctrine/CDA_DOCTRINE_OVERVIEW.md | [CNCPT] | → TM-40G–L (doctrine-driven development) |
| doctrine/cda_doctrine/CDA_DOCTRINE_AGENT.md | [CNCPT] | → TM-40H, TM-40L |
| doctrine/cda_doctrine/CDA_AVT25_ASSESSMENT.md | [CNCPT] | → TM-40G, TM-40H |
| doctrine/cda_doctrine/CDA_IDENTITY_VS_CLASSIFICATION.md | [CNCPT] | → TM-30, TM-40K, TM-40L |
| doctrine/ONTOLOGY_DESIGN_PRINCIPLES.md | [CNCPT] | → TM-40H, TM-40K, TM-40L, TM-50H/K/L (DDD, DRY, Open/Closed, PECS, Composition; Foundry-specific) |

### CDA Architecture Doctrine — Agents Series (TM-40H/I/K/L, TM-50H/I/K/L)
Bedrock → specialization hierarchy. Core Principles govern; specialized docs extend.
| File | Type | Supports |
|---|---|---|
| doctrine/cda_doctrine/agents/CDA_AGENTS_OVERVIEW.md | [CNCPT] | → index for agents subdirectory; hierarchy diagram |
| doctrine/cda_doctrine/agents/CDA_AGENTS_CORE_PRINCIPLES.md | [CNCPT] | → TM-40H, TM-40I, TM-40K, TM-40L, TM-50H/I/K/L (12 bedrock principles: Stability Stack, Four-Layer Architecture, Scope Engineering, Nine Object Types, Identity Governance, VAULTIS-A, 14 anti-patterns) |
| doctrine/cda_doctrine/agents/CDA_AGENTS_ONTOLOGY_ENGINEER.md | [CNCPT] | → TM-40H, TM-40K, TM-40L, TM-50H/K/L (specializes Core Principles 3/7/8/9/10/11; RDF, OWL2, SHACL, SPARQL, PROV-O; SHACL shapes, competency questions) |
| doctrine/cda_doctrine/agents/CDA_AGENTS_ENTITY_RESOLUTION.md | [CNCPT] | → TM-40H, TM-40I, TM-40L, TM-50H/I/L (9-stage ER pipeline; blocking, scoring, decisioning, cluster building, survivorship; threshold bands; 10 anti-patterns) |
| doctrine/cda_doctrine/agents/CDA_AGENTS_INGESTION_INTEGRATION.md | [CNCPT] | → TM-40H, TM-40I, TM-40L, TM-50H/I/L (Five-Stage Ingestion Pattern; ELT over ETL; Dagster DAG; VAULTIS-A per pipeline; 9 anti-patterns; 10-item output checklist) |

### GDAP — Global Doctrine Alignment Platform (TM-40H/I/K/L, TM-50H/I/K/L)
| File | Type | Supports |
|---|---|---|
| doctrine/gdap/GDAP_OVERVIEW.md | [CNCPT] | → TM-40H, TM-40I, TM-40K, TM-40L (platform quickstart, LlamaIndex retrieval stack, API endpoints) |
| doctrine/gdap/GDAP_VISION.md | [CNCPT] | → TM-40H, TM-40I, TM-40K, TM-40L, TM-50H/I/K/L (full vision: 10 use-case domains, 20 pipeline steps, DVEE, coalition seam detection) |
| doctrine/gdap/GDAP_PERSISTENCE_STRATEGY.md | [CNCPT] | → TM-40H, TM-40I, TM-40L, TM-50H/I/L (DuckDB = canonical truth; LlamaIndex = derived serving artifacts; versioning/rebuild/rollback policy) |
| doctrine/gdap/GDAP_ACCEPTANCE_TESTS.md | [CNCPT] | → TM-40H, TM-40I, TM-40L, TM-50H/I/L (P0/P1/P2 release gates across 9 sections: A=Foundation, B=Ingestion, C=Retrieval, D=Routing, E=Response Quality, F=Agents, G=Evaluation, H=Ops, I=Consumer Delight) |
| doctrine/gdap/GDAP_ADR_0001_LLAMAINDEX.md | [CNCPT] | → TM-40H, TM-40I, TM-40L, TM-50H/I/L (ADR-0001 accepted: DuckDB owns canonical truth; LlamaIndex owns serving artifacts; boundary rules) |

### MIM — MIP Information Model (TM-40H/I/K/L, TM-50H/I/K/L)
| File | Type | Supports |
|---|---|---|
| doctrine/mim/MIM_OVERVIEW.md | [CNCPT] | → TM-40H, TM-40I, TM-40K, TM-40L (toolchain: HTML/XSD parsers, Foundry backend, repo structure, package quick ref) |
| doctrine/mim/MIM_STANDARD.md | [CNCPT] | → TM-40H, TM-40I, TM-40K, TM-40L, TM-50H/I/K/L (MIM semantic model: namespaces, type/instance/status, roles, discriminators, code types, design principles, Semantic IDs) |
| doctrine/mim/MIM_STATE.md | [CNCPT] | → TM-40H, TM-40I, TM-40L, TM-50H/I/L (project snapshot 2026-02-28: maturity by area, passing/failing tests, key gaps, 30/60/90 priorities) |
| doctrine/mim/MIM_ACADEMICS.md | [CNCPT] | → TM-40H, TM-40I, TM-40K, TM-40L, TM-50H/I/K/L (Dr. Gerz / NATO interoperability; MIM↔Foundry structural alignment analysis; UML↔OT mapping; MIP governance) |
| doctrine/mim/MIM_DECISION_RECORDS.md | [CNCPT] | → TM-40H, TM-40L (ADR structure decision: repo-level and per-package ADRs) |
| doctrine/mim/MIM_FUTURE_CLASSES.md | [CNCPT] | → TM-40H, TM-40I, TM-40L, TM-50H/I/L (planned: mim-studio, mim-ui, adapters, backends, mim-sdk, mim-provenance) |
| doctrine/mim/MIM_ONTOLOGY_DOCS.md | [CNCPT] | → TM-40H, TM-40L, TM-50H/L (OSDK Maker Package full TypeScript API: SPTs, Value Types, Interfaces, Objects, Links, Interface Link Constraints, Actions, Derived Properties) |

### Canon Reference (TM-40G–L)
| File | Type | Supports |
|---|---|---|
| doctrine/cda_doctrine/canon/CANON_ADP_CROSSWALK.md | [CANON] | → all specialist tracks TM-40G–L |
| doctrine/cda_doctrine/canon/CANON_CONDITIONS_INDICATORS_THRESHOLDS.md | [CANON] | → TM-40G, TM-40H |
| doctrine/cda_doctrine/canon/CANON_ENGAGEMENT.md | [CANON] | → TM-40G, TM-40H |
| doctrine/cda_doctrine/canon/CANON_INFORMATION.md | [CANON] | → TM-40H, TM-40K |

### Quick Reference
| File | Type | Supports |
|---|---|---|
| quick_reference/cda_reference/EA_VS_DA.md | [REF] | → TM-30, TM-40K |
| quick_reference/cda_reference/ENTERPRISE_DATA_COMPASS.md | [REF] | → TM-40J, TM-40K |
| quick_reference/cda_reference/LESSONS_LEARNED.md | [REF] | → all tracks |
| quick_reference/cda_reference/PLAN_FOR_SUCCESS.md | [REF] | → TM-40J, TM-30 |
| quick_reference/cda_reference/DOCTRINE_ELEMENT_FOUNDRY_MAPPING.md | [REF] | → TM-40H, TM-40I, TM-40L, TM-50H/I/L (DoctrineElement property map, bi-temporal fields, TypeScript interface, OSDK query patterns, link types, enums) |
| exercises/exams/EXAM_CDA_FINAL.md | [EXAM] | → assesses Intro To Data + Data 101 + Data 201 |

### Interactive Apps
| App | Type | Supports |
|---|---|---|
| source_material/cda_apps/ea-vs-da-reference/ | [REF] | → TM-30, TM-40K, TM-40L |
| source_material/cda_apps/enterprise-data-compass/ | [REF] | → TM-40J, TM-40K |
| source_material/cda_apps/lessons-learned/ | [REF] | → all tracks |
| source_material/cda_apps/plan-for-success/ | [REF] | → TM-40J, TM-30 |
| source_material/course_portal/ | [PPT] | → see CDA Slide Library above |

---

## SECTION 1 — BASE TRACKS

### TM-10: Maven User
| File | Type | Outbound Dependencies |
|---|---|---|
| TM_10_MAVEN_USER.md | [TM] | → TM-20 (next step), ⇢ DATA_LITERACY_technical_reference |
| (no Concepts Guide) | — | — |
| SYLLABUS_TM10.md | [SYL] | → TM-10 [TM] |
| EX-10_operator_basics/EXERCISE.md | [EX] | → TM-10 [TM] |
| EXAM_TM10_PRE.md | [EXAM] | assesses TM-10 readiness |
| EXAM_TM10_SUPPLEMENTAL.md | [EXAM] | optional supplemental knowledge check for TM-10 |

**Inbound references from:** TM-20, TM-30, TM-40A–F (all list TM-10 as prereq), SYLLABUS_TM20, SYLLABUS_TM30, all TM-40/50 syllabi, MTP, POI, CAD, TEO, ENROLLMENT_SOP, ANNUAL_TRAINING_SCHEDULE, CHEATSHEET, README, QUICK_START

**Recommended CDA decks [PPT]:** ⇢ army_data_orientation_v1 · architecture_primer · 2026_Data_Stack_Deep_Dive

---

### TM-20: Builder
| File | Type | Outbound Dependencies |
|---|---|---|
| TM_20_BUILDER.md | [TM] | → TM-10 (prereq), → TM-30 (escalation), ↔ TM-10 Ch 4/5/8 task refs, ⇢ TM-40I, ⇢ TM-40L |
| CONCEPTS_GUIDE_TM20_BUILDER.md | [CNCPT] | ↔ TM_20_BUILDER [TM] (companion), ⇢ TM-30 escalation guide |
| SYLLABUS_TM20.md | [SYL] | → TM-10 (prereq) |
| EX-20_no_code_builder/EXERCISE.md | [EX] | → TM-20 [TM], → NAMING_AND_GOVERNANCE_STANDARDS |
| EXAM_TM20_PRE.md | [EXAM] | assesses TM-20 readiness |
| EXAM_TM20_POST.md | [EXAM] | assesses TM-20 completion |

**Inbound references from:** TM-30, TM-40A–L (prereq chain via TM-30), all training mgmt docs, CHEATSHEET, README

**Recommended CDA decks [PPT]:** ⇢ What_Is_An_Ontology · Data_Modeling_Foundations · The_Semantic_Layer_Instructions · L2_Ingestion_Integration_Deep_Dive · L5_Activation_Interface_Deep_Dive · Dont_Filter_This_Isnt_Excel · The_Four_Layers · Data_Modeling_Fundamentals_Level1 · ObjectType_WhatToWatchFor · Links_and_Relationships

---

### TM-30: Advanced Builder
| File | Type | Outbound Dependencies |
|---|---|---|
| TM_30_ADVANCED_BUILDER.md | [TM] | → TM-10 (prereq), → TM-20 (prereq), ⇢ DATA_LITERACY_technical_reference |
| CONCEPTS_GUIDE_TM30_ADVANCED_BUILDER.md | [CNCPT] | ↔ TM_30_ADVANCED_BUILDER [TM] (companion), ⇢ TM-40G–L escalation guide, ⇢ EA Series, ⇢ CDA doctrine |
| SYLLABUS_TM30.md | [SYL] | → TM-10, → TM-20 (prereqs) |
| EX-30_advanced_builder/EXERCISE.md | [EX] | → TM-30 [TM], → NAMING_AND_GOVERNANCE_STANDARDS |
| EXAM_TM30_PRE.md | [EXAM] | assesses TM-30 readiness |
| EXAM_TM30_POST.md | [EXAM] | assesses TM-30 completion |

**Inbound references from:** TM-40A–F (all WFF tracks, hard prereq), TM-40G–L (all specialist tracks, hard prereq), TM-40K (pipeline builder), TM-40L (peer note), all training mgmt docs, CHEATSHEET, README

**Recommended CDA decks [PPT]:** ⇢ Data_Architecture_Deep_Dive · Data_Platforms_Cloud_Deep_Dive · Semantic_Modelling_Course_Intro · Deck_01_Architecture_First_Principles · Deck_02_Scope_Engineering · Deck_04_Object_Type_Varieties · Deck_05_Identity_Governance · Deck_06_Relationship_Modeling · Controlled_Vocabularies · Identity_Who_Owns_The_Key

---

## SECTION 1B — BUILDER SPRINT (BSP)
### Prereq: TM-20 Go on file + command-approved project
### NOT part of the TM-10 → TM-50 sequence; does NOT grant TM credit

| File | Type | Outbound Dependencies |
|---|---|---|
| builder_sprint/BSP_GUIDE.md | [BSP] | → TM-20 (prereq); does NOT → TM-30 (explicitly not a substitute) |
| builder_sprint/ENVIRONMENT_SETUP.md | [BSP] | → BSP_GUIDE (coordinator checklist for sprint setup) |
| builder_sprint/SPRINT_PACKAGE.md | [BSP] | → BSP_GUIDE Ch 5 (evaluator/coordinator standards); → ENROLLMENT_SOP (enrollment workflow) |
| training_management/BUILDER_SPRINT_SOP.md | [SOP] | → TM-20 (prereq); → BSP_GUIDE, → SPRINT_PACKAGE, → ENVIRONMENT_SETUP (references all BSP docs); → ANNUAL_TRAINING_SCHEDULE (quarterly calendar) |

**Inbound references from:** DEPENDENCY_MAP prereq chain, DEMO_BRIEF_CG, WHITE_PAPER_MSS_TRAINING, mss_info_app/index.html (if applicable)

**Key governance note:** BSP is a quarterly 5-day supervised build event. Prereq: TM-20 Go + command-validated project. Does NOT grant TM-30 credit. Does NOT unlock TM-40 enrollment.

---

## SECTION 2 — WFF FUNCTIONAL TRACKS (TM-40A–F)
### Prereq for all: TM-10 + TM-20 + TM-30 + track Concepts Guide

### TM-40A: Intelligence
| File | Type | Outbound Dependencies |
|---|---|---|
| TM_40A_INTELLIGENCE.md | [TM] | → TM-10, → TM-20, → TM-30, → CONCEPTS_GUIDE_TM40A (prereq read), ↔ TM-40F (CCIR coordination) |
| CONCEPTS_GUIDE_TM40A_INTELLIGENCE.md | [CNCPT] | → TM-10 (prereq baseline), ↔ TM -40A [TM] (Appendix D), ⇢ FM 2-0, ATP 2-01.3, ATP 2-01 |
| SYLLABUS_TM40A.md | [SYL] | → TM-10, → TM-20, → TM-30, ⇢ FM 2-0, ATP 2-01 |
| EX-40A_intelligence/EXERCISE.md | [EX] | → TM-40A [TM] |
| EXAM_TM40A_PRE.md | [EXAM] | assesses TM-40A readiness |
| EXAM_TM40A_POST.md | [EXAM] | assesses TM-40A completion |

**Inbound references from:** TM-40D (companion cross-ref), TM-40E (AT intel integration), DATA_LITERACY_technical_reference, CHEATSHEET, mss_info_app/index.html, README

**Recommended CDA decks [PPT]:** ⇢ decision_advantage_deep_dive

---

### TM-40B: Fires
| File | Type | Outbound Dependencies |
|---|---|---|
| TM_40B_FIRES.md | [TM] | → TM-10, → TM-20, → TM-30, → CONCEPTS_GUIDE_TM40B (prereq read), ⇢ TM-40L (system admin) |
| CONCEPTS_GUIDE_TM40B_FIRES.md | [CNCPT] | ↔ TM -40B [TM] (read before TM-40B), ⇢ ADP 3-19, FM 3-09, FM 3-60, ATP 3-01.8, ATP 3-52.2, ATP 3-09.42, ATP 3-09.50 |
| SYLLABUS_TM40B.md | [SYL] | → TM-10, → TM-20, → TM-30, ⇢ FM 3-09, ATP 3-09.42, FM 3-60 |
| EX-40B_fires/EXERCISE.md | [EX] | → TM-40B [TM] |
| EXAM_TM40B_PRE.md | [EXAM] | assesses TM-40B readiness |
| EXAM_TM40B_POST.md | [EXAM] | assesses TM-40B completion |

**Inbound references from:** TM-40D (ammo mgmt companion), TM-40E (AMD coordination), DATA_LITERACY_technical_reference, CHEATSHEET, mss_info_app/index.html, README

**Recommended CDA decks [PPT]:** ⇢ decision_advantage_deep_dive

---

### TM-40C: Movement & Maneuver
| File | Type | Outbound Dependencies |
|---|---|---|
| TM_40C_MOVEMENT_MANEUVER.md | [TM] | → TM-10, → TM-20, → TM-30, → CONCEPTS_GUIDE_TM40C (prereq read), ↔ TM-40E (NBC/protection layer) |
| CONCEPTS_GUIDE_TM40C_MOVEMENT_MANEUVER.md | [CNCPT] | ↔ TM -40C [TM] (doctrinal framework), ⇢ ADP 3-0, FM 3-96 |
| SYLLABUS_TM40C.md | [SYL] | → TM-10, → TM-20, → TM-30, ⇢ ADP 3-0, FM 3-0, ATP 3-90.90 |
| EX-40C_movement_maneuver/EXERCISE.md | [EX] | → TM-40C [TM] |
| EXAM_TM40C_PRE.md | [EXAM] | assesses TM-40C readiness |
| EXAM_TM40C_POST.md | [EXAM] | assesses TM-40C completion |

**Inbound references from:** TM-40D (maneuver unit readiness companion), TM-40E (physical security/base camp siting), DATA_LITERACY_technical_reference, CHEATSHEET, mss_info_app/index.html, README

**Recommended CDA decks [PPT]:** ⇢ decision_advantage_deep_dive

---

### TM-40D: Sustainment
| File | Type | Outbound Dependencies |
|---|---|---|
| TM_40D_SUSTAINMENT.md | [TM] | → TM-10, → TM-20, → TM-30, → CONCEPTS_GUIDE_TM40D (prereq read), ↔ TM-40A (intel/threat feed), ↔ TM-40B (ammo coordination), ↔ TM-40C (maneuver readiness), ↔ TM-40E (CBRN/convoy protection), ↔ TM-40F (COP/LOGSTAT), ⇢ TM-40I (ML models) |
| CONCEPTS_GUIDE_TM40D_SUSTAINMENT.md | [CNCPT] | ↔ TM -40D [TM] (para 4-7), ↔ TM-40F (COP framework/S4 producer) |
| SYLLABUS_TM40D.md | [SYL] | → TM-10, → TM-20, → TM-30, ⇢ ADP 4-0, FM 4-0, ATP 4-0.1 |
| EX-40D_sustainment/EXERCISE.md | [EX] | → TM-40D [TM] |
| EXAM_TM40D_PRE.md | [EXAM] | assesses TM-40D readiness |
| EXAM_TM40D_POST.md | [EXAM] | assesses TM-40D completion |

**Inbound references from:** TM-40E (CBRN resupply), CHEATSHEET, mss_info_app/index.html, README

**Recommended CDA decks [PPT]:** ⇢ decision_advantage_deep_dive

---

### TM-40E: Protection
| File | Type | Outbound Dependencies |
|---|---|---|
| TM_40E_PROTECTION.md | [TM] | → TM-10, → TM-20, → TM-30, → CONCEPTS_GUIDE_TM40E (prereq read), ↔ TM-40A (AT intel), ↔ TM-40B (AMD coordination), ↔ TM-40C (base camp siting), ↔ TM-40D (CBRN resupply/medical), ↔ TM-40F (COP/CCIR protection data), ⇢ TM-40L (pipeline construction) |
| CONCEPTS_GUIDE_TM40E_PROTECTION.md | [CNCPT] | ↔ TM -40E [TM] (Appendix A naming, Appendix H data quality) |
| SYLLABUS_TM40E.md | [SYL] | → TM-10, → TM-20, → TM-30, ⇢ ADP 3-37, ATP 3-37.2 |
| EX-40E_protection/EXERCISE.md | [EX] | → TM-40E [TM] |
| EXAM_TM40E_PRE.md | [EXAM] | assesses TM-40E readiness |
| EXAM_TM40E_POST.md | [EXAM] | assesses TM-40E completion |

**Inbound references from:** TM-40C (NBC data integration), DATA_LITERACY_technical_reference, CHEATSHEET, mss_info_app/index.html, README

**Recommended CDA decks [PPT]:** ⇢ decision_advantage_deep_dive

---

### TM-40F: Mission Command
| File | Type | Outbound Dependencies |
|---|---|---|
| TM_40F_MISSION_COMMAND.md | [TM] | → TM-10, → TM-20, → TM-30, → CONCEPTS_GUIDE_TM40F (prereq read), ↔ TM-40G (ORSA products for G35), ↔ TM-40H (AI-enabled CCIR alerts), ↔ TM-40I (predictive products), ↔ TM-40J (PM readiness/portfolio), ↔ TM-40K (KM info products/lessons learned) |
| CONCEPTS_GUIDE_TM40F_MISSION_COMMAND.md | [CNCPT] | ↔ TM -40F [TM] (proceed to TM-40F for task instruction), → TM-10 (baseline proficiency) |
| SYLLABUS_TM40F.md | [SYL] | → TM-10, → TM-20, → TM-30, ⇢ ADP 6-0, FM 6-0 |
| EX-40F_mission_command/EXERCISE.md | [EX] | → TM-40F [TM] |
| EXAM_TM40F_PRE.md | [EXAM] | assesses TM-40F readiness |
| EXAM_TM40F_POST.md | [EXAM] | assesses TM-40F completion |

**Inbound references from:** TM-40A (CCIR coordination), TM-40C (S3 coordination), TM-40D (COP/LOGSTAT), TM-40E (COP/CCIR protection), CONCEPTS_GUIDE_TM40D (COP framework), DATA_LITERACY_technical_reference, CHEATSHEET, mss_info_app/index.html, README

**Recommended CDA decks [PPT]:** ⇢ decision_advantage_deep_dive

---

## SECTION 3 — SPECIALIST TRACKS (TM-40G–L)
### Prereq for all: TM-10 + TM-20 + TM-30 (all required)

### TM-40G: ORSA
| File | Type | Outbound Dependencies |
|---|---|---|
| TM_40G_ORSA.md | [TM] | → TM-10, → TM-20, → TM-30, → CONCEPTS_GUIDE_TM40G, ⇢ TM-40H (AI library install), ⇢ TM-40I (ML integration) |
| CONCEPTS_GUIDE_TM40G_ORSA.md | [CNCPT] | ↔ TM -40G [TM] (companion), ⇢ TM-40G Appendix D checklist |
| SYLLABUS_TM40G.md | [SYL] | → TM-10, → TM-20, → TM-30 |
| EX-40G_orsa/EXERCISE.md | [EX] | → TM-40G [TM] |
| EXAM_TM40G_PRE.md | [EXAM] | assesses TM-40G readiness |
| EXAM_TM40G_POST.md | [EXAM] | assesses TM-40G completion |

**Advanced track:** → TM-50G
**Inbound references from:** TM-40J (portfolio analytics), TM-50G (prereq), DATA_LITERACY_technical_reference, CHEATSHEET, task_index.html (17 tasks), mss_info_app/index.html, README

**Recommended CDA decks [PPT]:** ⇢ Data_Modeling_Fundamentals_Level2 · Deck_07_Temporal_Bitemporal · Deck_12_Capstone_Foundry

---

### TM-40H: AI Engineer
| File | Type | Outbound Dependencies |
|---|---|---|
| TM_40H_AI_ENGINEER.md | [TM] | → TM-10, → TM-20, → TM-30, → CONCEPTS_GUIDE_TM40H, ⇢ TM-40I (fine-tuning/model topics) |
| CONCEPTS_GUIDE_TM40H_AI_ENGINEER.md | [CNCPT] | role distinction table with TM-40I, TM-40L; ↔ TM -40H [TM] |
| SYLLABUS_TM40H.md | [SYL] | → TM-10, → TM-20, → TM-30 |
| EX-40H_ai_engineer/EXERCISE.md | [EX] | → TM-40H [TM] |
| EXAM_TM40H_PRE.md | [EXAM] | assesses TM-40H readiness |
| EXAM_TM40H_POST.md | [EXAM] | assesses TM-40H completion |

**Advanced track:** → TM-50H
**Inbound references from:** TM-40F (AI-enabled CCIR), TM-40G (library install), TM-40K (AIP Agent Studio), TM-50G (pipeline architecture), TM-50H (prereq), TM-50L (recommended), DATA_LITERACY_technical_reference, CHEATSHEET, task_index.html (1 task), mss_info_app/index.html, README

**Recommended CDA decks [PPT]:** ⇢ AI_ML_Beyond_The_Hype · Deck_12_Capstone_Foundry

---

### TM-40I: ML Engineer
| File | Type | Outbound Dependencies |
|---|---|---|
| TM_40I_ML_ENGINEER.md | [TM] | → TM-10, → TM-20, → TM-30, → CONCEPTS_GUIDE_TM40I, ⇢ TM-40G (RStudio/ORSA workflows), ⇢ TM-40L (VS Code) |
| CONCEPTS_GUIDE_TM40I_ML_ENGINEER.md | [CNCPT] | role matrix consistent with TM-40G/H/L; ↔ TM -40I [TM] |
| SYLLABUS_TM40I.md | [SYL] | → TM-10, → TM-20, → TM-30 |
| EX-40I_ml_engineer/EXERCISE.md | [EX] | → TM-40I [TM] |
| EXAM_TM40I_PRE.md | [EXAM] | assesses TM-40I readiness |
| EXAM_TM40I_POST.md | [EXAM] | assesses TM-40I completion |

**Advanced track:** → TM-50I
**Inbound references from:** TM-40F (predictive products), TM-40G (ML integration), TM-50G (ML integration), TM-50H (fine-tuning infrastructure), TM-50I (prereq), DATA_LITERACY_technical_reference, CHEATSHEET, task_index.html (21 tasks), mss_info_app/index.html, README

**Recommended CDA decks [PPT]:** ⇢ AI_ML_Beyond_The_Hype · Data_Modeling_Fundamentals_Level2 · Deck_07_Temporal_Bitemporal

---

### TM-40J: Program Manager
| File | Type | Outbound Dependencies |
|---|---|---|
| TM_40J_PROGRAM_MANAGER.md | [TM] | → TM-10, → TM-20, → TM-30 (all required), ⇢ TM-40H, ⇢ TM-40I |
| CONCEPTS_GUIDE_TM40J_PROGRAM_MANAGER.md | [CNCPT] | ↔ TM -40J [TM] |
| SYLLABUS_TM40J.md | [SYL] | → TM-10, → TM-20, → TM-30 (required) |
| EX-40J_program_manager/EXERCISE.md | [EX] | → TM-40J [TM] |
| EXAM_TM40J_PRE.md | [EXAM] | assesses TM-40J readiness |
| EXAM_TM40J_POST.md | [EXAM] | assesses TM-40J completion |

**Advanced track:** → TM-50J
**Inbound references from:** TM-40F (PM readiness/portfolio), TM-50J (prereq, recommends TM-40G/H/I/K/L), DATA_LITERACY_technical_reference, CHEATSHEET, task_index.html (18 tasks), mss_info_app/index.html, README

**Recommended CDA decks [PPT]:** ⇢ Deck_02_Scope_Engineering

---

### TM-40K: Knowledge Manager
| File | Type | Outbound Dependencies |
|---|---|---|
| TM_40K_KNOWLEDGE_MANAGER.md | [TM] | → TM-10, → TM-20, → TM-30 (all required), ⇢ TM-40H (AIP Agent Studio), ⇢ TM-40L (TypeScript/OSDK, custom logic) |
| CONCEPTS_GUIDE_TM40K_KNOWLEDGE_MANAGER.md | [CNCPT] | ↔ TM -40K [TM] |
| SYLLABUS_TM40K.md | [SYL] | → TM-10, → TM-20, → TM-30 (required) |
| EX-40K_knowledge_manager/EXERCISE.md | [EX] | → TM-40K [TM] |
| EXAM_TM40K_PRE.md | [EXAM] | assesses TM-40K readiness |
| EXAM_TM40K_POST.md | [EXAM] | assesses TM-40K completion |

**Advanced track:** → TM-50K
**Inbound references from:** TM-40F (KM info products), TM-50K (prereq), DATA_LITERACY_technical_reference, CHEATSHEET, task_index.html (6 tasks), mss_info_app/index.html, README

**Recommended CDA decks [PPT]:** ⇢ Controlled_Vocabularies · Identity_Who_Owns_The_Key · Deck_03_RDF_OWL_Foundations · Deck_05_Identity_Governance

---

### TM-40L: Software Engineer
| File | Type | Outbound Dependencies |
|---|---|---|
| TM_40L_SOFTWARE_ENGINEER.md | [TM] | → TM-10, → TM-20, → TM-30, → CONCEPTS_GUIDE_TM40L; noted peer to TM-40G/H/I |
| CONCEPTS_GUIDE_TM40L_SOFTWARE_ENGINEER.md | [CNCPT] | role matrix shows TM-40L as SWE; ↔ TM -40L [TM] |
| SYLLABUS_TM40L.md | [SYL] | → TM-10, → TM-20, → TM-30 |
| EX-40L_software_engineer/EXERCISE.md | [EX] | → TM-40L [TM] |
| EXAM_TM40L_PRE.md | [EXAM] | assesses TM-40L readiness |
| EXAM_TM40L_POST.md | [EXAM] | assesses TM-40L completion |

**Advanced track:** → TM-50L
**Inbound references from:** TM-40B (system admin/platform), TM-40E (pipeline construction), TM-40K (custom logic), TM-50L (prereq, TM-40H/I recommended), DATA_LITERACY_technical_reference, CHEATSHEET, task_index.html (30 tasks), mss_info_app/index.html, README

**Recommended CDA decks [PPT]:** ⇢ Deck_03_RDF_OWL_Foundations · Deck_04_Object_Type_Varieties · Deck_06_Relationship_Modeling · Deck_07_Temporal_Bitemporal · Data_Modeling_Fundamentals_Level2 · Deck_12_Capstone_Foundry

---

## SECTION 4 — ADVANCED SPECIALIST TRACKS (TM-50G–L)
### Prereq for each: corresponding TM-40G–L (required)

| Track | Prereq | Key Cross-Refs | Advanced Track File |
|---|---|---|---|
| TM-50G (Adv ORSA) | TM-40G | ↔ TM-40H, TM-40I, TM-40J | TM_50G_ORSA_ADVANCED.md + CG |
| TM-50H (Adv AI Eng) | TM-40H | ↔ TM-50G, TM-50I, TM-50J, TM-50K, TM-50L; ⇢ TM-40I | TM_50H_AI_ENGINEER_ADVANCED.md + CG |
| TM-50I (Adv ML Eng) | TM-40I | ↔ TM-50H (fine-tuning infra) | TM_50I_ML_ENGINEER_ADVANCED.md + CG |
| TM-50J (Adv PM) | TM-40J | ⇢ TM-40G, TM-40H, TM-40I, TM-40K, TM-40L | TM_50J_PROGRAM_MANAGER_ADVANCED.md + CG |
| TM-50K (Adv KM) | TM-40K | ↔ TM-50H (corpus design) | TM_50K_KNOWLEDGE_MANAGER_ADVANCED.md + CG |
| TM-50L (Adv SWE) | TM-40L | ⇢ TM-40H, TM-40I; ↔ TM-50H (OSDK integration) | TM_50L_SOFTWARE_ENGINEER_ADVANCED.md + CG |

**Syllabi:** SYLLABUS_TM50G–L present and published
**Exams:** EXAM_TM50G–L PRE + POST present
**Exercises:** EX-50G–L directories present (EX-50G_orsa/, EX-50H_ai_engineer/, EX-50I_ml_engineer/, EX-50J_program_manager/, EX-50K_knowledge_manager/, EX-50L_software_engineer/ — each with EXERCISE.md + ENVIRONMENT_SETUP.md)

---

## SECTION 5 — DOCTRINE & STANDARDS

| File | Type | Referenced By |
|---|---|---|
| DATA_LITERACY_technical_reference.md | Doctrine/ADP-analog | TM-10, TM-20, TM-30, TM-40G–L, TM-50G–L (all recommended prereq read) |
| DATA_LITERACY_senior_leaders.md | Doctrine/senior leader brief | Standalone; referenced in README, QUICK_START |
| GLOSSARY_data_foundry.md | Reference | Standalone; referenced in README, cheatsheet |
| NAMING_AND_GOVERNANCE_STANDARDS.md | Standards | EX-20, EX-30 (required read); TM-40I Appendix A, TM-40L Appendix B |
| cheatsheet.md | Quick Reference | Standalone; links to all TMs A–L, 50G–L, base tracks |

---

## SECTION 6 — TRAINING MANAGEMENT

| File | Covers | Key Cross-Refs |
|---|---|---|
| MTP_MSS.md | Master training plan; course overview table + TM-10 throughput risk item (Sec 7-4, G-3 action required) | All TMs; corrected durations: TM-20=5d, TM-30=5d, TM-40A–F=3d, TM-40G/H/I/L=5d, TM-40J/K=4d |
| POI_MSS.md | Program of instruction; tier/prereq structure | All TMs; prereq tree A–L; TM-40J/K now correctly in TM-30 branch |
| CAD_MSS.md | Course admin; access reqs by track | All TMs; TM-40J/K prereq = TM-30 required |
| TEO_MSS.md | T&EO evaluation standards; TM20-03 Row 5 now [CRITICAL] (date arithmetic) | TM-10 through TM-40L critical performance measures |
| ANNUAL_TRAINING_SCHEDULE.md | Schedule by track (2026) | All TMs; TM-40J/K prereq = TM-30 |
| ANNUAL_TRAINING_CALENDAR_FY27.html | Interactive FY27 training calendar (HTML) | Visual companion to ANNUAL_TRAINING_SCHEDULE |
| FACULTY_DEVELOPMENT_PLAN.md | Instructor quals by track | All TMs; WFF (A–F) vs. Specialist (G–L) instructor profiles |
| COMPLETION_CERTIFICATE.md | Certificate templates | Generic; course title filled at completion |
| CURRICULUM_MAINTENANCE_SOP.md | Maintenance SOP + Platform Monitoring procedure (Sec 2A) + Semi-Annual Deep Review (Sec 5A) | Scope: TM-10 through TM-40L |
| ENROLLMENT_SOP.md | Enrollment process + prereq verification + Training Records Requirements section (minimum data standard, retention, query process) | All TMs; TM-40J/K prereq = TM-30 required |
| COMMANDERS_GUIDE_MSS_TRAINING.md | Commander/XO reference: who trains on what, timelines, CDR responsibilities, throughput risk | → ENROLLMENT_SOP; → MTP; all TM levels |
| TM10_LESSON_PLANS.md | Lesson plan: TM-10 | TM-10 Ch 1–8, DATA_LITERACY_technical_reference Ch 1 |
| TM20_LESSON_PLAN_OUTLINES.md | Lesson plan: TM-20 | TM-20 Ch 2–5, NAMING_AND_GOVERNANCE_STANDARDS |
| TM30_LESSON_PLAN_OUTLINES.md | Lesson plan: TM-30 | TM-30 Ch 2–9, Standards Ch 3–4 |
| TM40_SPECIALIST_LESSON_PLAN_OUTLINES.md | Lesson plans: TM-40G–L | All specialist tracks G–L; WFF A–F managed separately with WFF proponents |
| POLICY_LETTER.md | Training policy letter | All tracks; command direction and training requirements by echelon |
| AAR_TEMPLATE.md | After Action Review template | All training events; standard format for post-course review |
| lesson_plans/LP_TEMPLATE.md | Standard lesson plan template | Blank template; TLO, Key Delivery Notes, Student Activity, Assessment blocks |
| ENTERPRISE_V10_PLAN.md | ODT Enterprise v10 release plan (2026-03-12) | 5 bounded contexts (Architecture/Pipelines/Products/Foundry/QA); M1–M5 milestone gates; agent assignments; feature checklist |
| ENTERPRISE_IMPLEMENTATION_PLAN.md | Enterprise implementation plan — CUI // FOUO | 6-phase/20-week hardening plan; 46 acceptance functions; 12 CG architectural constraints; current-state assessment |
| BUILDER_SPRINT_SOP.md | Builder Sprint SOP: quarterly event enrollment, execution, evaluation | → BSP_GUIDE, → ENROLLMENT_SOP, → ANNUAL_TRAINING_SCHEDULE |
| INSTRUCTOR_OVERVIEW.md | Instructor onboarding guide: program structure, materials, execution | All TMs; → MTP, → POI, → CAD, → TEO, → ENROLLMENT_SOP, → lesson plans |
| DEMO_BRIEF_CG.md | CG decision brief: request TASKORD authorization for MSS MTT | → TASKORD, → WHITE_PAPER; ↔ all training management docs |
| TASKORD_MSS_TRAINING_CELL.md | Draft TASKORD: MSS MTT activation (theater-wide) | → MTP, → POI, → ENROLLMENT_SOP, → ANNUAL_TRAINING_SCHEDULE |
| WHITE_PAPER_MSS_TRAINING.md | Strategic white paper: case for MSS training across USAREUR-AF | → all TMs (program overview); ↔ DEMO_BRIEF_CG |
| MSS_TRAINING_BRIEF.pptx | CG briefing slide deck (PowerPoint) | ↔ DEMO_BRIEF_CG (companion visual) |
| lesson_plans/TM40_WFF_LESSON_PLAN_OUTLINES.md | Lesson plans: TM-40A–F WFF tracks | All WFF tracks A–F |
| lesson_plans/TM50_ADVANCED_LESSON_PLAN_OUTLINES.md | Lesson plans: TM-50G–L advanced tracks | All advanced tracks G–L |

---

## SECTION 7 — HTML APPLICATIONS

| File | Contents | TM Dependencies |
|---|---|---|
| mss_info_app/index.html | Training hub — 6 WFF cards (A–F, TM-30 chip) + 6 specialist cards (G–L, TM-30 chip) + 6 TM-50 cards | All TM-40A–L PDFs, all CGs, all exams, all syllabi |
| mss_info_app/training_schedule.html | Schedule view | Training schedule data |
| task_index.html | Task index by specialist track | TM-40G(17 tasks), TM-40H(1), TM-40I(21), TM-40J(18), TM-40K(6), TM-40L(30) = 93 total |
| mss_info_app/index_sharepoint.html | SharePoint-hosted variant of MSS Training Hub | Same as index.html; adapted for SharePoint embedding |
| mss_info_app/PILOT_AGENT_PROMPT.md | System prompt for MSS pilot AI agent | ↔ mss_info_app/index.html (serves the training hub) |
| mss_info_app/DEPLOYMENT.md | Deployment guide: Cloudflare Pages + SharePoint + Foundry | → index.html, → index_sharepoint.html |
| mss_info_app/Maven_Rollout_Plan.pptx | Rollout plan slide deck (PPTX) | ↔ DEMO_BRIEF_CG (CG rollout strategy) |
| source_material/course_portal/ | CDA slide library — 29 decks, 3 tracks, 397 PNG slides | ⇢ all TM levels (see Section 8); source of all [PPT] refs |

---

---

## SECTION 8 — CDA SLIDE LIBRARY (repos/)

**Source:** `maven_training/source_material/course_portal/`
**Format:** Slide decks (PNG images + PDF/PPTX downloads); manifest-driven
**Status:** Not yet integrated into mss_info_app; planned as panel-slide-library
**Role in curriculum:** Conceptual prereq layer — fills the "why and what" gap the TM series does not cover

All 29 decks listed below. Track assignment and TM alignment are authoritative for merge planning.

### Track: Intro To Data (12 decks)

| Deck ID | Title | Slides | TM Alignment | Notes |
|---|---|---|---|---|
| army_data_orientation_v1 | Army Data Orientation | 14 | ⇢ Data Literacy (SL) / all personnel | Direct parallel to doctrine panel content; Army-specific framing |
| architecture_primer | Architecture Primer | 12 | ⇢ before TM-10 | Orientation to the data stack before first MSS login |
| 2026_Data_Stack_Deep_Dive | 2026 Data Stack — Five Layers | 10 | ⇢ TM-20 | Explains the five-layer stack TM-20 teaches users to build in |
| L2_Ingestion_Integration_Deep_Dive | L2 Ingestion & Integration | 10 | ⇢ TM-20 | Pipeline concepts behind Pipeline Builder tasks |
| The_Semantic_Layer_Instructions | The Semantic Layer | 11 | ⇢ TM-20 / TM-30 | Why the Ontology layer exists; frames TM-20 Ontology Manager tasks |
| What_Is_An_Ontology | What Is an Ontology? | 12 | ⇢ TM-20 | Conceptual base for Object Types; gap in TM-20 |
| Data_Modeling_Foundations | Data Modeling Foundations | 11 | ⇢ TM-20 / TM-30 | Normalization → strategy; underpins TM-30 architecture decisions |
| Data_Platforms_Cloud_Deep_Dive | Data Platforms & Cloud | 10 | ⇢ TM-20 / TM-30 | Where Foundry/MSS sits in the broader platform landscape |
| L5_Activation_Interface_Deep_Dive | L5 Activation & Interface | 10 | ⇢ TM-20 | Workshop conceptual grounding; explains why Workshop widgets exist |
| Dont_Filter_This_Isnt_Excel | Don't Filter — This Isn't Excel | 11 | ⇢ TM-20 | Critical mindset shift; Foundry vs spreadsheet mental model |
| decision_advantage_deep_dive | Decision Advantage | 10 | ⇢ TM-40A–F (all WFF) | The "why" behind WFF data integration; all six WFF tracks |
| AI_ML_Beyond_The_Hype | AI/ML — Beyond the Hype | 11 | ⇢ TM-40H / TM-40I | Conceptual framing required before AIP Logic and model training |

### Track: Data 101 (7 decks)

| Deck ID | Title | Slides | TM Alignment | Notes |
|---|---|---|---|---|
| The_Four_Layers | The Four Layers | 13 | ⇢ TM-20 / TM-30 | Data layer model; directly maps to stack diagram in TM-20 |
| Data_Modeling_Fundamentals_Level1 | Data Modeling Fundamentals — Level 1 | 15 | ⇢ TM-20 | Object type design patterns; prereq conceptual content for TM-20 tasks |
| ObjectType_WhatToWatchFor | Object Types — What to Watch For | 13 | ⇢ TM-20 / TM-30 | Anti-patterns; fills gap neither TM-20 nor TM-30 covers |
| Links_and_Relationships | Links & Relationships | 11 | ⇢ TM-20 | Link type conceptual base; maps to "Create Link Types" in TM-20 |
| Controlled_Vocabularies | Controlled Vocabularies | 11 | ⇢ TM-30 / TM-40K | Vocab standardization; TM-40K owns this operationally |
| Identity_Who_Owns_The_Key | Identity — Who Owns the Key? | 11 | ⇢ TM-30 / TM-40K / TM-40L | Primary keys, master data, identity governance |
| Dont_Filter_This_Isnt_Excel | (see Intro To Data above) | — | ⇢ TM-20 | Listed in both tracks in source manifest |

### Track: Data 201 (10 decks)

| Deck ID | Title | Slides | TM Alignment | Notes |
|---|---|---|---|---|
| Semantic_Modelling_Course_Intro | Semantic Modelling — Course Intro | 10 | ⇢ TM-30 / TM-40L | Entry to formal semantic modeling; TM-30 architects and SWEs |
| Deck_01_Architecture_First_Principles | 01 — Architecture First Principles | 10 | ⇢ TM-30 / TM-40L | Core architecture decision principles; above TM-30 procedure level |
| Deck_02_Scope_Engineering | 02 — Scope Engineering | 10 | ⇢ TM-30 / TM-40J | How to scope a data problem; TM-30 governance + PM track |
| Deck_03_RDF_OWL_Foundations | 03 — RDF & OWL Foundations | 10 | ⇢ TM-40K / TM-40L | RDF triples, OWL classes; knowledge graph and semantic layer work |
| Deck_04_Object_Type_Varieties | 04 — Object Type Varieties | 10 | ⇢ TM-30 / TM-40L | Advanced object type design patterns |
| Deck_05_Identity_Governance | 05 — Identity & Governance | 10 | ⇢ TM-30 / TM-40K | Formal governance patterns for shared ontology |
| Deck_06_Relationship_Modeling | 06 — Relationship Modeling | 10 | ⇢ TM-30 / TM-40L | Advanced link type and relationship design |
| Deck_07_Temporal_Bitemporal | 07 — Temporal & Bitemporal | 10 | ⇢ TM-40G / TM-40I / TM-40L | Time-aware data modeling; ORSA time series + SWE pipeline patterns |
| Data_Modeling_Fundamentals_Level2 | Data Modeling Fundamentals — Level 2 | 13 | ⇢ TM-40G / TM-40I / TM-40L | Advanced modeling; senior technical specialist level |
| Deck_12_Capstone_Foundry | 12 — Capstone: Foundry | 10 | ⇢ TM-40G / TM-40H / TM-40L | Bridges CDA theory to Foundry/MSS practice; single highest-value deck for specialists |

---

## SECTION 7 — EXTERNAL REFERENCE LIBRARY: PALANTIR DEVELOPERS

**Source:** Palantir Developers YouTube channel (@PalantirDevelopers) — official Palantir product deep-dive video library.
**Integration method:** (1) Inline NOTE callouts embedded in TM files at the relevant chapter/task locations. (2) SELF_STUDY_ADDENDUM.md files in each TM directory for organized self-study guidance. No class time added — all content is reference or optional self-study only.
**[SS]** = Self-Study Addendum file type (used in this section only)

### Self-Study Addenda — File Registry

| File | Type | Supports | Groups / Videos |
|---|---|---|---|
| tm/TM_30_advanced_builder/SELF_STUDY_ADDENDUM.md | [SS] | TM-30 | 5 groups: Workshop Scenarios, Pipeline Monitoring, Quiver Advanced, Contour Advanced, Platform Security |
| tm/TM_40G_orsa/SELF_STUDY_ADDENDUM.md | [SS] | TM-40G | 4 groups: Quiver analytics, Contour analytics, Platform Architecture, AI/Advanced |
| tm/TM_40H_ai_engineer/SELF_STUDY_ADDENDUM.md | [SS] | TM-40H | 9 groups: RAG, Evals, MCP, Observability, Safety, Agent Studio, AIP Logic, Ontology, Platform |
| tm/TM_40I_ml_engineer/SELF_STUDY_ADDENDUM.md | [SS] | TM-40I | 7 groups: Spark, PySpark testing, Iceberg, Compute Modules, Pipeline Monitoring, Model Registry, Feature Engineering |
| tm/TM_40J_program_manager/SELF_STUDY_ADDENDUM.md | [SS] | TM-40J | 4 groups: Delivery & Scaling, Project Tracking, Case Studies, Leadership |
| tm/TM_40K_knowledge_manager/SELF_STUDY_ADDENDUM.md | [SS] | TM-40K | 5 groups: RAG & Retrieval, Knowledge Architecture, Semantic Search, AIP-Assisted KM, Platform Admin |
| tm/TM_40L_software_engineer/SELF_STUDY_ADDENDUM.md | [SS] | TM-40L | 8 groups: OSDK 2.0, Functions, Code Repos, Cipher, MCP, Edge Ontology, Spark, Platform SDK (~45 videos) |
| tm/TM_50G_orsa_advanced/SELF_STUDY_ADDENDUM.md | [SS] | TM-50G | TM-40G groups + 7 TM-50G-specific additions (Bayesian, persistent ORSA, data layer) |
| tm/TM_50H_ai_engineer_advanced/SELF_STUDY_ADDENDUM.md | [SS] | TM-50H | TM-40H groups + 8 TM-50H-specific additions (multi-agent, observability, enterprise) |
| tm/TM_50I_ml_engineer_advanced/SELF_STUDY_ADDENDUM.md | [SS] | TM-50I | 8 groups, 29 videos (Iceberg advanced, xAI model tuning, Lightweight Transforms, Scaling AI) |
| tm/TM_50J_program_manager_advanced/SELF_STUDY_ADDENDUM.md | [SS] | TM-50J | TM-40J groups + enterprise autonomy, process orchestration, enterprise automation |
| tm/TM_50K_knowledge_manager_advanced/SELF_STUDY_ADDENDUM.md | [SS] | TM-50K | TM-40K groups + Advanced Ontology, Enterprise KM, multimodal data plane |
| tm/TM_50L_software_engineer_advanced/SELF_STUDY_ADDENDUM.md | [SS] | TM-50L | TM-40L reference + 5 TM-50L additions (Code-based AI, interoperability, Gallatin observability, Edge Embedded, Developer Experience) |

### Inline NOTE Callouts — Summary by Track

| Track | NOTE Count | Primary Chapters |
|---|---|---|
| TM-30 | 4 | Ch 2 (Workshop Scenarios), Ch 3 (Pipeline Monitoring), Ch 5 (Quiver), Ch 7 (Security) |
| TM-40G | 6 | Ch 8 (Quiver/Contour analytics) |
| TM-40H | 12 | Ch 2, 5, 6, 7, 8, 9 (RAG, Evals, MCP, Observability, Safety) |
| TM-40I | 10 | Spark, PySpark testing, Iceberg, Compute Modules, Pipeline Monitoring |
| TM-40J | 6 | Phase 5/6 lifecycle, project tracking tools, delivery planning |
| TM-40K | 9 | Knowledge architecture, AIP/RAG, search/discovery |
| TM-40L | 30 | All chapters (OSDK 2.0, Functions, Code Repos, Cipher, MCP, Edge Ontology, Spark, Platform SDK) |
| TM-50G | 3 | Ch 4 Bayesian, Ch 8 persistent ORSA, data layer |
| TM-50H | 5 | Ch 2 multi-agent, Ch 6 observability, Ch 8 enterprise |
| TM-50I | 4 | Iceberg, xAI model tuning, Lightweight Transforms, Scaling AI |
| TM-50J | 3 | Enterprise autonomy, process orchestration, enterprise automation |
| TM-50K | 3 | Advanced Ontology, Enterprise KM, multimodal data plane |
| TM-50L | 5 | Code-based AI dev, interoperability, Gallatin observability, Edge Embedded, Developer Experience |
| **Total** | **~100** | Across TM-30 through TM-50L |

---

## CHANGE LOG — ISSUES FOUND & FIXED (12 March 2026 Audit)

| # | File | Line | Issue | Fix Applied |
|---|---|---|---|---|
| 1 | TM_40G_ORSA.md | 81 | "see TM-30 and TM-40G/40B" — TM-40B is WFF Fires, not pipeline dev | Changed to "see TM-30" |
| 2 | SYLLABUS_TM40J.md | 9 | TM-30 listed as "recommended but not required" — contradicts TM source | Changed to "TM-10/20/30 all required" |
| 3 | SYLLABUS_TM40K.md | 9 | TM-30 listed as "recommended" — contradicts TM source | Changed to "TM-10/20/30 all required" |
| 4 | POI_MSS.md | 38, 51–52 | TM-40J/K listed outside TM-30 branch; labeled TM-30 as exception | Fixed prereq tree; TM-40J/K now under TM-30 branch |
| 5 | CAD_MSS.md | 71–72, 75 | TM-40J/K prereq listed as "TM-30 recommended but not required" | Updated to "TM-30 required"; advisory note updated |
| 6 | ENROLLMENT_SOP.md | 63–64 | TM-40J/K prereq listed as TM-10/20 only | Updated to include TM-30 required |
| 7 | MTP_MSS.md | 58–66 | Multiple duration errors: TM-20=2d (should be 5), TM-30=3d (should be 5), TM-40G/H/I/L=4d (should be 5), TM-40J/K prereq=TM-20 (should be TM-30) | All durations and prereqs corrected |
| 8 | ANNUAL_TRAINING_SCHEDULE.md | 120, 133, 188 | TM-40J/K prereq listed as TM-20; prereq chain table omitted TM-30 | Updated all three locations |
| 9 | (PDF) 42 stale PDFs | — | Old specialist naming scheme (TM-40A=ORSA etc., TM-50A–F) | Deleted all 42 stale PDFs |
| 10 | build_pdfs.py | — | Missing WFF syllabi A–F, exams A–F, exercises A–F | Added all to MD_TARGETS and PUB_TYPES |

---

## AUDIT VERIFICATION COMMANDS

```bash
# Run full corpus audit (from repo root)
python3 scripts/audit.py

# Rebuild PDFs for changed source files
python3 scripts/build_pdfs.py

# Verify PDF count and check for stale files
ls maven_training/pdf/*.pdf | wc -l
```

*Expected audit result: PASS — 0 issues (pending TM-40D/E/F prereq resolution)*

---

## CHANGE LOG — ISSUES FOUND & FIXED (13 March 2026 Second Full Audit)

**Scope:** 925 files, 6 parallel agent passes. Full read of every file in corpus.

| # | File(s) | Issue | Fix Applied |
|---|---|---|---|
| 11 | source_material/course_portal/assets/The Semantic Layer Instructions/ | Space in directory name (naming violation) | Renamed → The_Semantic_Layer_Instructions/ |
| 12 | source_material/cda_docs/training/Data 201/ | Space in directory name | Renamed → removed (was empty after dedup) |
| 13 | source_material/cda_docs/training/Intro To Data/ | Spaces in directory name | Renamed → removed (was empty after dedup) |
| 14 | source_material/course_portal/downloads/The Semantic Layer Instructions.pdf | Space in filename | Renamed → The_Semantic_Layer_Instructions.pdf |
| 15 | source_material/cda_docs/training/The Semantic Layer Instructions.pdf | Space in filename | Renamed → The_Semantic_Layer_Instructions.pdf |
| 16 | source_material/cda_docs/reference/Cross-Domain Solutions_ Complete Technical Reference for Ontology Modeling.pdf | Spaces in filename | Renamed → cross-domain-solutions-technical-reference-ontology-modeling.pdf |
| 17 | source_material/cda_docs/training/Intro To Data/The Semantic Layer Instructions.pdf | Identical duplicate of training/ root copy | Deleted |
| 18 | source_material/cda_docs/training/Data 201/Data_Modeling_Fundamentals_Level2.pdf | Identical duplicate of training/ root copy | Deleted |
| 19 | source_material/cda_docs/reference/DDOF_Playbook_v2_0.pdf | Identical duplicate of cda_docs/ root copy | Deleted |
| 20 | course_portal/manifest.json + downloads/index.html | Stale paths referencing renamed files | Updated to match new filenames |
| 21 | DEPENDENCY_MAP.md | Missing entries: CDA_CONSTRAINTS_AND_DIRECTIVES, POLICY_LETTER, AAR_TEMPLATE, LP_TEMPLATE | Added to Sections 0B and 6 |

**OPEN ITEM — RESOLVED:**

| # | Files Affected | Issue | Resolution |
|---|---|---|---|
| OPEN-1 | TM_40A–F [TM], CONCEPTS_GUIDE_TM40A–F [CG], SYLLABUS_TM40A–F [SYL], mss_info_app, mss_widget, DEPENDENCY_MAP | WFF tracks prereq inconsistency — some files stated TM-20 only, others TM-30. | **RESOLVED 2026-03-13:** Design decision — all WFF tracks (TM-40A–F) now require TM-30 (same prereq chain as Specialist tracks, TM-10 + TM-20 + TM-30). All governance docs and app files updated. TM/CG content files require separate update pass to align. |

---

## CHANGE LOG — RALF BRANCH MIGRATION (14 March 2026)

**Scope:** 25 files migrated from `orsuh/repos` `ralf` branch (12 commits ahead of main, unmerged). Content classified as TM-40/50 specialist level (architecture doctrine, engineering reference).

| # | Files Added | Destination | Level |
|---|---|---|---|
| 22 | doctrine/CG_GUIDANCE.md | Senior leader doctrine | TM-10/20 |
| 23 | doctrine/cda_doctrine/CDA_OVERVIEW.md | CDA user taxonomy + enterprise index | TM-30 bridge |
| 24 | doctrine/cda_doctrine/agents/CDA_AGENTS_OVERVIEW.md | Agents index doc | TM-40H/I/K/L |
| 25 | doctrine/cda_doctrine/agents/CDA_AGENTS_CORE_PRINCIPLES.md | 12 bedrock principles, 14 anti-patterns, decision framework | TM-40H/I/K/L |
| 26 | doctrine/cda_doctrine/agents/CDA_AGENTS_ONTOLOGY_ENGINEER.md | Specializes Principles 3/7/8/9/10/11; RDF/OWL2/SHACL/SPARQL | TM-40H/K/L |
| 27 | doctrine/cda_doctrine/agents/CDA_AGENTS_ENTITY_RESOLUTION.md | 9-stage ER pipeline; threshold bands; data product architecture | TM-40H/I/L |
| 28 | doctrine/cda_doctrine/agents/CDA_AGENTS_INGESTION_INTEGRATION.md | Five-Stage Ingestion Pattern; Dagster DAG; VAULTIS-A | TM-40H/I/L |
| 29 | doctrine/ONTOLOGY_DESIGN_PRINCIPLES.md | DDD, DRY, Open/Closed, PECS, Composition; Foundry-specific rules | TM-40H/K/L |
| 30 | doctrine/gdap/GDAP_OVERVIEW.md | LlamaIndex retrieval stack, API endpoints | TM-40H/I/K/L |
| 31 | doctrine/gdap/GDAP_VISION.md | Full 10-domain vision, 20 pipeline steps, DVEE | TM-40H/I/K/L |
| 32 | doctrine/gdap/GDAP_PERSISTENCE_STRATEGY.md | DuckDB vs LlamaIndex boundary; versioning/rebuild policy | TM-40H/I/L |
| 33 | doctrine/gdap/GDAP_ACCEPTANCE_TESTS.md | P0/P1/P2 release gates across 9 sections | TM-40H/I/L |
| 34 | doctrine/gdap/GDAP_ADR_0001_LLAMAINDEX.md | ADR-0001: DuckDB = truth, LlamaIndex = serving | TM-40H/I/L |
| 35 | doctrine/mim/MIM_OVERVIEW.md | Toolchain: parsers, Foundry backend, package structure | TM-40H/I/K/L |
| 36 | doctrine/mim/MIM_STANDARD.md | MIM semantic model, namespaces, roles, code types, Semantic IDs | TM-40H/I/K/L |
| 37 | doctrine/mim/MIM_STATE.md | Project snapshot 2026-02-28; maturity by area; gaps/priorities | TM-40H/I/L |
| 38 | doctrine/mim/MIM_ACADEMICS.md | Dr. Gerz / NATO; MIM↔Foundry structural alignment analysis | TM-40H/I/K/L |
| 39 | doctrine/mim/MIM_DECISION_RECORDS.md | ADR: repo-level and per-package ADR structure | TM-40H/L |
| 40 | doctrine/mim/MIM_FUTURE_CLASSES.md | Planned adapters, backends, mim-studio, mim-sdk | TM-40H/I/L |
| 41 | doctrine/mim/MIM_ONTOLOGY_DOCS.md | OSDK Maker Package full TypeScript API reference | TM-40H/L |
| 42 | quick_reference/cda_reference/DOCTRINE_ELEMENT_FOUNDRY_MAPPING.md | Property mapping, bi-temporal fields, TS interface, OSDK queries, enums | TM-40H/I/L |
| 43 | training_management/ENTERPRISE_V10_PLAN.md | ODT v10 release plan; 5 bounded contexts; M1–M5 gates | TM-40H/I/L |
| 44 | training_management/ENTERPRISE_IMPLEMENTATION_PLAN.md | 6-phase/20-wk hardening plan — **CUI // FOUO** | TM-40H/I/L |

**Note on ENTERPRISE_IMPLEMENTATION_PLAN.md:** Source document bears `CUI // FOUO` classification. Handle per local policy before committing to shared repository.

---

## CHANGE LOG — PALANTIR DEVELOPERS ENRICHMENT (14 March 2026)

**Scope:** Full Palantir Developers YouTube channel (@PalantirDevelopers) enumerated via yt-dlp (~130 videos). All videos mapped to TM tracks (TM-30 through TM-50L). TM-30 scope limited to UI-only tools (no code). TM-40/50 specialist tracks received code-level content appropriate to their domains.

**Method:** (1) Inline NOTE callouts embedded at relevant chapter/task anchor points. (2) SELF_STUDY_ADDENDUM.md overflow files for content that did not fit inline. No class time or schedule changes made.

| # | Files Added / Modified | Change | Level |
|---|---|---|---|
| 45 | TM_30_ADVANCED_BUILDER.md | 4 inline NOTEs added (Workshop Scenarios, Pipeline Monitoring, Quiver advanced, Security) | TM-30 |
| 46 | SYLLABUS_TM30.md | Supplemental self-study note added after Day 1 evening reading block | TM-30 |
| 47 | tm/TM_30_advanced_builder/SELF_STUDY_ADDENDUM.md | NEW — 5 groups covering TM-30-scoped UI tool depth content (~15 videos) | TM-30 |
| 48 | TM_40G_ORSA.md | 6 inline NOTEs added (Quiver/Contour analytics) | TM-40G |
| 49 | tm/TM_40G_orsa/SELF_STUDY_ADDENDUM.md | NEW — 4 groups, 16 videos | TM-40G |
| 50 | TM_40H_AI_ENGINEER.md | 12 inline NOTEs added (RAG, Evals, MCP, Observability, Safety) | TM-40H |
| 51 | tm/TM_40H_ai_engineer/SELF_STUDY_ADDENDUM.md | NEW — 9 groups, 43 videos | TM-40H |
| 52 | TM_40I_ML_ENGINEER.md | 10 inline NOTEs added (Spark, PySpark, Iceberg, Compute Modules) | TM-40I |
| 53 | tm/TM_40I_ml_engineer/SELF_STUDY_ADDENDUM.md | NEW — 7 groups, 25 videos | TM-40I |
| 54 | TM_40J_PROGRAM_MANAGER.md | 6 inline NOTEs added (lifecycle phases, project tracking, delivery) | TM-40J |
| 55 | tm/TM_40J_program_manager/SELF_STUDY_ADDENDUM.md | NEW — 4 groups | TM-40J |
| 56 | TM_40K_KNOWLEDGE_MANAGER.md | 9 inline NOTEs added (knowledge architecture, AIP/RAG, search) | TM-40K |
| 57 | tm/TM_40K_knowledge_manager/SELF_STUDY_ADDENDUM.md | NEW — 5 groups | TM-40K |
| 58 | TM_40L_SOFTWARE_ENGINEER.md | 30 inline NOTEs added across all chapters (OSDK, Functions, Cipher, MCP, Edge, Spark) | TM-40L |
| 59 | tm/TM_40L_software_engineer/SELF_STUDY_ADDENDUM.md | NEW — 8 groups, ~45 videos | TM-40L |
| 60 | TM_50G_ORSA_ADVANCED.md | 3 inline NOTEs added | TM-50G |
| 61 | tm/TM_50G_orsa_advanced/SELF_STUDY_ADDENDUM.md | NEW — extends TM-40G + 7 TM-50G additions | TM-50G |
| 62 | TM_50H_AI_ENGINEER_ADVANCED.md | 5 inline NOTEs added | TM-50H |
| 63 | tm/TM_50H_ai_engineer_advanced/SELF_STUDY_ADDENDUM.md | NEW — extends TM-40H + 8 TM-50H additions | TM-50H |
| 64 | TM_50I_ML_ENGINEER_ADVANCED.md | 4 inline NOTEs added | TM-50I |
| 65 | tm/TM_50I_ml_engineer_advanced/SELF_STUDY_ADDENDUM.md | NEW — 8 groups, 29 videos | TM-50I |
| 66 | TM_50J_PROGRAM_MANAGER_ADVANCED.md | 3 inline NOTEs added | TM-50J |
| 67 | tm/TM_50J_program_manager_advanced/SELF_STUDY_ADDENDUM.md | NEW — extends TM-40J + enterprise content | TM-50J |
| 68 | TM_50K_KNOWLEDGE_MANAGER_ADVANCED.md | 3 inline NOTEs added | TM-50K |
| 69 | tm/TM_50K_knowledge_manager_advanced/SELF_STUDY_ADDENDUM.md | NEW — extends TM-40K + advanced | TM-50K |
| 70 | TM_50L_SOFTWARE_ENGINEER_ADVANCED.md | 5 inline NOTEs added | TM-50L |
| 71 | tm/TM_50L_software_engineer_advanced/SELF_STUDY_ADDENDUM.md | NEW — TM-50L additions + reference to TM-40L addendum | TM-50L |
| 72 | scripts/build_pdfs.py | Added PUB_TYPES + MD_TARGETS for: TM-50 syllabi (6), EX-50 exercises (6), SELF_STUDY_ADDENDUM files (13) | Build |
| 73 | DEPENDENCY_MAP.md | Section 7 added for Palantir Developers external reference library | All |

---

## CHANGE LOG — RALF BRANCH FULL INVENTORY (14 March 2026)

**Scope:** Full file inventory of ralf-branch-migrated content revealed additional files beyond the initial 25 tracked in entries #22–44. These files were already present in Section 0B but not captured in the changelog.

| # | Files Added | Destination | Level |
|---|---|---|---|
| 74 | doctrine/CDA_CONSTRAINTS_AND_DIRECTIVES.md | 12 CDA operational constraints; governs all specialist CDA work | TM-40G–L |
| 75 | doctrine/cda_doctrine/CDA_DOCTRINE_OVERVIEW.md | Doctrine-driven development framework; DDD applied to CDA | TM-40G–L |
| 76 | doctrine/cda_doctrine/CDA_DOCTRINE_AGENT.md | Doctrine Agent reference — AI-assisted doctrine authoring patterns | TM-40H, TM-40L |
| 77 | doctrine/cda_doctrine/CDA_AVT25_ASSESSMENT.md | AVT-25 assessment framework for CDA capability evaluation | TM-40G, TM-40H |
| 78 | doctrine/cda_doctrine/CDA_IDENTITY_VS_CLASSIFICATION.md | Identity vs. classification disambiguation; semantic precision | TM-30, TM-40K, TM-40L |
| 79 | doctrine/enterprise_architecture/EA_00_REFERENCE_CARD.md | EA one-pager; frameworks overview (TOGAF, NAF, DODAF, Zachman) | TM-30, TM-40K, TM-40L |
| 80 | doctrine/enterprise_architecture/EA_01_FOUNDATION.md | EA foundational concepts; what EA is and is not | TM-30 |
| 81 | doctrine/enterprise_architecture/EA_02_SCHOOLS_OF_THOUGHT.md | TOGAF, Zachman, FEA, NAF, DODAF compared | TM-30, TM-40K |
| 82 | doctrine/enterprise_architecture/EA_03_ARTIFACTS_AND_VIEWS.md | NAF/DODAF views; architecture artifacts; diagram types | TM-40K, TM-40L |
| 83 | doctrine/enterprise_architecture/EA_04_GOVERNANCE.md | Architecture governance; review boards; decision authority | TM-40K |
| 84 | doctrine/enterprise_architecture/EA_05_MILITARY_APPLICATION.md | EA applied to military C2 / joint operations context | TM-30, TM-40G–L |
| 85 | doctrine/cda_doctrine/canon/CANON_ADP_CROSSWALK.md | ADP 3-0 / 6-0 crosswalk to Foundry data model | TM-40G–L |
| 86 | doctrine/cda_doctrine/canon/CANON_CONDITIONS_INDICATORS_THRESHOLDS.md | Conditions, indicators, and threshold patterns for data products | TM-40G, TM-40H |
| 87 | doctrine/cda_doctrine/canon/CANON_ENGAGEMENT.md | Engagement authority and engagement event data model | TM-40G, TM-40H |
| 88 | doctrine/cda_doctrine/canon/CANON_INFORMATION.md | Information taxonomy and schema for common operational data | TM-40H, TM-40K |
| 89 | quick_reference/cda_reference/EA_VS_DA.md | Enterprise Architecture vs. Data Architecture decision tool | TM-30, TM-40K |
| 90 | quick_reference/cda_reference/ENTERPRISE_DATA_COMPASS.md | Data strategy decision compass; orientation for PM/KM roles | TM-40J, TM-40K |
| 91 | quick_reference/cda_reference/LESSONS_LEARNED.md | CDA implementation lessons learned registry | All tracks |
| 92 | quick_reference/cda_reference/PLAN_FOR_SUCCESS.md | CDA project planning checklist and success criteria | TM-40J, TM-30 |

---

## CHANGE LOG — PDF BUILD: ARCH / MGMT / REF SERIES (14 March 2026)

**Scope:** 42 new PDFs generated for all ralf-branch architecture, management, and reference docs. Distinct naming convention (`ARCH_`, `MGMT_`, `REF_`) to clearly separate from TM/CG/SYL/EX/EXAM corpus.

**PDF naming scheme:**

| Prefix | Category | PUB_TYPE label | Example stems |
|---|---|---|---|
| `ARCH_CDA_` | CDA Doctrine & Agents | ARCHITECTURE REFERENCE / ODT-CDA | ARCH_CDA_AGENTS_CORE_PRINCIPLES, ARCH_CDA_CANON_ADP_CROSSWALK |
| `ARCH_GDAP_` | GDAP Platform | ARCHITECTURE REFERENCE / ODT-GDAP | ARCH_GDAP_OVERVIEW, ARCH_GDAP_ADR_0001_LLAMAINDEX |
| `ARCH_MIM_` | MIM Reference | ARCHITECTURE REFERENCE / ODT-MIM | ARCH_MIM_STANDARD, ARCH_MIM_ACADEMICS |
| `ARCH_EA_` | Enterprise Architecture | ARCHITECTURE REFERENCE / ODT-EA | ARCH_EA_01_FOUNDATION, ARCH_EA_05_MILITARY_APPLICATION |
| `ARCH_ONTOLOGY_` | Ontology Design | ARCHITECTURE REFERENCE / ODT-ONT | ARCH_ONTOLOGY_DESIGN_PRINCIPLES |
| `MGMT_` | Management / Planning | SENIOR LEADER GUIDANCE or ENTERPRISE PLAN | MGMT_CG_GUIDANCE, MGMT_ENTERPRISE_V10_PLAN |
| `REF_` | Quick Reference | QUICK REFERENCE / ODT-REF | REF_DOCTRINE_ELEMENT_FOUNDRY_MAPPING, REF_EA_VS_DA |

| # | Action | Files | Output |
|---|---|---|---|
| 93 | scripts/build_pdfs.py — PUB_TYPES + MD_TARGETS expanded | Added ARCH_CDA/GDAP/MIM/EA/ONT, MGMT_, REF_ key prefixes and 42 source paths | 42 new PDFs in maven_training/pdf/ |
| 94 | DEPENDENCY_MAP.md | Updated header metadata; added changelog entries #74–94 | This file |

---

## CHANGE LOG — PRE-v2.0 FULL-CORPUS AUDIT (14 March 2026)

**Scope:** Team-of-teams content accuracy and consistency audit across all curriculum files, React widget, HTML app, Python scripts, and PPTX presentation files. Primary goal: verify prereq chain enforcement (TM-30 hard prereq for ALL TM-40 tracks A–F and G–L) and content alignment between all delivery surfaces.

**Audit findings and resolutions:**

| # | File | Issue | Resolution |
|---|---|---|---|
| 95 | README.md (root) | WFF prereq stated TM-20 in 4 places (table, tree, footnote lines) | Fixed → TM-30 in all 4 locations |
| 96 | maven_training/training_management/POLICY_LETTER.md | Official governance table: WFF tracks listed TM-20 as prereq | Fixed → TM-30 |
| 97 | maven_training/mss_widget/src/panels/Home.tsx | WFF specialist row "Start Here" cell showed TM-10 → TM-20 only; TM-30 missing | Fixed → TM-10 → TM-20 → TM-30 chain |
| 98 | maven_training/quick_reference/cheatsheet.md | WFF track description said "after TM-20"; prereq chain diagram wrong | Fixed → TM-30 throughout; diagram rebuilt with WFF + Specialist both branching from TM-30 |
| 99 | maven_training/mss_widget/src/panels/TM40.tsx | TM-40J card: builder-focused language ("PM Dashboards, Reporting Pipelines") mismatched actual TM content (Agile PM theory, ML lifecycle, stakeholder mgmt); BLUF embedded full WFF track list creating confusion | Fixed: TM-40J card rewritten to PM theory; BLUF simplified with cross-reference to HOME tab |
| 100 | maven_training/mss_info_app/index.html | TM-40J card matched stale builder-focused TM40.tsx (dual-maintenance surface) | Fixed: TM-40J card updated to match TM40.tsx (PM theory content) |
| 101 | .gitignore | node_modules/ missing; 65MB React deps at risk of commit | Added node_modules/ |
| 102 | maven_training/pdf/MSS_Project_Overview.pptx | Slide 1: old "6 Specialist Tracks: 40A ORSA · 40B AI · 40C MLE..." scheme | Rebuilt via python-pptx: "12 Tracks (WFF + Specialist) / WFF (A–F): Intel · Fires · M&M / Specialist (G–L): ORSA · AI Eng · MLE · PM · KM · SWE" |
| 103 | maven_training/pdf/MSS_Training_Progression.pptx | Specialist column: original 6-slot design insufficient; partial fix left WFF A–D mixed with specialist H–I, sub-headers misplaced | Full column rebuild via python-pptx: deleted all 19 old content shapes; clean layout with "▸ WFF TRACKS (A–F)" (A–F) / "▸ SPECIALIST (G–L)" (G–L) sub-headers; TM-50 G–L note added at bottom |
| 104 | scripts/build_pdfs.py (PDF rebuild) | 3 source files changed: POLICY_LETTER.md, cheatsheet.md, task_index.html | Hash-based rebuild: 3 PDFs regenerated (POLICY_LETTER.pdf, CHEATSHEET.pdf + task_index.html-derived); 199 unchanged |
| 105 | DEPENDENCY_MAP.md | Audit findings not logged | This entry |
| 106 | SYLLABUS_TM40B.md, TM40_WFF_LESSON_PLAN_OUTLINES.md, DEPENDENCY_MAP.md | ATP 3-60 (inactive, May 2015) referenced instead of superseding FM 3-60 (Aug 2023) | replace_all ATP 3-60 → FM 3-60 in all 3 files (2 + 4 + 1 = 7 instances) |
| 107 | DEPENDENCY_MAP.md | No external doctrinal reference index | Added "External Doctrinal References" section with 32-pub table |
| 108 | TM_40E, SYLLABUS_TM40E, DEPENDENCY_MAP, index.html, index_sharepoint.html, TM40_WFF_LESSON_PLAN_OUTLINES | Phantom FM 3-37 cited (pub does not exist); protection capstone is ADP 3-37 | Removed/replaced FM 3-37 → ADP 3-37 across 6 files (10 edits); zero instances remain |
| 109 | TM_50K_KNOWLEDGE_MANAGER_ADVANCED | FM 6-01.1 cited (pub type wrong); correct is ATP 6-01.1 | Changed FM 6-01.1 → ATP 6-01.1 (Techniques for Effective Knowledge Management) |
| 110 | TM_40C, CONCEPTS_GUIDE_TM40C, index.html, index_sharepoint.html | FM 3-90-1 and FM 3-90-2 cited; both merged into FM 3-90 (May 2023) | Consolidated 19 refs across 4 files → FM 3-90, Offense and Defense (May 2023) |
| 111 | TM_40C_MOVEMENT_MANEUVER | Stale edition dates: FM 3-0 (2022), FM 3-09 (2020), FM 5-0 (2022), FM 6-0 (2014) | Updated to current: FM 3-0 (Mar 2025), FM 3-09 (Aug 2024), FM 5-0 (Nov 2024), FM 6-0 (May 2022) |
| 112 | TM_40K, TM_50K | FM 7-0 subtitle "Train to Win in a Complex World" (2016 ed.) | Updated to current: FM 7-0, Training (Jun 2021) |
| 113 | TM_50H_AI_ENGINEER_ADVANCED | AR 25-55 cited (rescinded; incorporated into AR 25-30) | Changed AR 25-55 → AR 25-30 (FOIA) |
| 114 | 25 TM/doctrine/training_management files | Strategic guidance docs mixed into Governing/Doctrinal References tables | Separated into distinct "Strategic Guidance" sections; 21 files modified |
| 115 | 13 TM files (TM-10, TM-40A–L) | No professional reading lists | Added Professional Reading List appendices with 65+ curated journal articles |
| 116 | 7 files (CG docs, TM-40F/G/H/I, CDA) | No EUCOM theater context | Added Theater and Strategic Context sections (BRAVO Hackathon, Thunderforge, Posture Statement, 49B career path) |
| 117 | TM-40A, TM-40C, TM-40K, TM-40L, TM-50K, TM-50L, GLOSSARY | NATO MIM standards gap — no STANAG 5643/5527, ADatP-36/5644, or CWIX references | Added 4 NATO standards to doctrine refs, CWIX context notes, glossary MIM disambiguation |

---

## External Doctrinal References

> Publications prefixed TR/TP are published by TRADOC at adminpubs.tradoc.army.mil, not DA APD (armypubs.army.mil).

| Publication | Title | Referenced By |
|---|---|---|
| AR 350-1 | Army Training and Leader Development | All training management docs |
| TR 350-70 | Army Learning Policy and Systems (TRADOC) | POI, CAD, CURRICULUM_MAINTENANCE_SOP, INSTRUCTOR_OVERVIEW |
| TP 350-70-14 | Training Development in Institutional Domain (TRADOC) | POI, CAD, CURRICULUM_MAINTENANCE_SOP |
| TP 350-70-7 | Army Educational Processes (TRADOC) | POI, INSTRUCTOR_OVERVIEW |
| TP 350-70-3 | Faculty and Staff Development Program (TRADOC) | INSTRUCTOR_OVERVIEW |
| DA PAM 25-40 | Army Publishing: Action Officers' Guide | Publication standards (all docs) |
| AR 25-50 | Preparing and Managing Correspondence | Army writing style (all docs) |
| AR 25-1 | Army Information Technology | TM-40K, TM-40L, POLICY_LETTER, data governance |
| DA PAM 25-1-1 | Army IT Implementation Instructions | TM-40K, TM-40L |
| AR 25-400-2 | Army Records Management Program | TM-40K |
| DA PAM 25-403 | Army Guide to Recordkeeping | TM-40K |
| ATP 6-01.1 | Techniques for Effective Knowledge Management | TM-40K, TM-50K |
| DA PAM 600-3 | Officer Professional Development | TM-40G (FA 49 ORSA) |
| AR 5-11 | Management of Army M&S | TM-40G, TM-50G |
| DA PAM 5-11 | VV&A of Army Models and Simulations | TM-40G, TM-50G |
| ATP 5-0.3 | Multi-Service TTP for Operation Assessment | TM-40G, TM-50G |
| AR 71-9 | Warfighting Capabilities Determination | TM-40G |
| Army DIR 2024-03 | Digital Engineering Policy | TM-40H, TM-40I, TM-40L, TM-50H, TM-50I, TM-50L |
| FM 3-12 | Cyberspace Operations and EW | TM-40E, TM-40H, TM-40I, TM-40L |
| DA PAM 25-2-5 | Software Assurance | TM-40H, TM-40I, TM-40L |
| FM 3-27 | Army Global Integrated Fires | TM-40B |
| ATP 3-01.81 | Counter-UAS Techniques | TM-40B |
| FM 3-81 | Maneuver Enhancement Brigade | TM-40C |
| ATP 4-33 | Maintenance Operations | TM-40D |
| FM 1-0 | Human Resources Support | TM-40D |
| AR 525-2 | The Army Protection Program | TM-40E |
| AR 530-1 | Operations Security | TM-40E |
| ATP 5-0.1 | Army Design Methodology | TM-40F |
| TC 6-0.2 | Training the C2 WFF for BN/BDE/BCT | TM-40F |
| ATP 2-33.4 | Intelligence Analysis | TM-40A |
| ATP 2-22.9-1 | PAI Research and OSINT | TM-40A |
| FM 3-60 | Army Targeting | TM-40A, TM-40B |
| | | |
| **DoD/Joint Strategic Guidance** | | |
| DoD Data Strategy (2020) | Data as Strategic Asset / VAUTI Framework | TM-10, TM-20, TM-30, doctrine/ |
| DoD Data, Analytics & AI Adoption Strategy (Nov 2023) | AI Hierarchy of Needs; adopt-buy-create | COMMANDERS_GUIDE, POLICY_LETTER, doctrine/ |
| DoD Responsible AI Strategy (Jun 2024) | Five AI Ethical Principles (RETRG) | TM-40H, TM-40I, TM-50H, TM-50I |
| DoD Zero Trust Reference Architecture v2.0 (Jul 2022) | 152 ZT activities across 7 pillars | TM-30 |
| DoD AI Cybersecurity Risk Mgmt Guide | Secure AI/ML development | TM-40H, TM-40I, TM-50H, TM-50I |
| DoDI 5000.87 | Software Acquisition Pathway | TM-40L, TM-50L, TM-40J, TM-50J |
| DoDD 3000.09 | Autonomy in Weapon Systems (Jan 2023) | TM-40A–F |
| DoD Software Modernization Strategy (Feb 2022) | DevSecOps frameworks | TM-40L, TM-50L |
| JADC2 Strategy Summary (Mar 2022) | Cross-domain data integration | TM-40A–F, TM-40G, TM-50G |
| JCOIE | Operating in the Information Environment | TM-40F |
| | | |
| **Army Strategic Guidance** | | |
| Army Data Plan (2022) | 11 strategic objectives for data transformation | TM-10, TM-20, TM-30, COMMANDERS_GUIDE, POLICY_LETTER |
| Army Cloud Plan (2022) | ZT, secure dev, data-driven decisions | TM-10, TM-20, TM-30 |
| UDRA v1.1 (Feb 2025) | Data mesh, decentralized governance | TM-30, TM-40G–L, TM-50G–L |
| Army CIO Data Stewardship Memo (Apr 2024) | Chain of responsibility for data governance | TM-10, TM-20, TM-30, TM-40K |
| Army Directive 2024-02 | Agile Software Dev & Acquisition (Dec 2024) | TM-40L, TM-50L, TM-40J, TM-50J |
| | | |
| **NATO** | | |
| NATO Data Strategy for the Alliance (Feb 2025) | Alliance-wide data governance mandate | TM-30, TM-40K, TM-50K, CDA_CONSTRAINTS |
| NATO Data Centric Reference Architecture v2 (2025) | Digital transformation reference arch | TM-30, CDA_CONSTRAINTS |
| NATO Data Quality Framework (Aug 2025) | Quality governance and metrics | TM-30 |
| NATO Digital Transformation Implementation Strategy (Oct 2024) | MDO interoperability | TM-40A–F |
| NATO Warfighting Capstone Concept (2021) | 6 Critical Enablers incl. Data | TM-40F |
| ADatP-34/NISP (NATO) | C3 Interoperability Standards | TM-40K, TM-50K, TM-40L, TM-50L |
| STANAG 5636/NCMS (NATO) | Core Metadata Specification | TM-40K, TM-50K |
| STANAG 5643 (proposed) | MIM Governance Standard | TM-40K, TM-50K, TM-40L, TM-50L |
| ADatP-5644 | Web Service Messaging Profile (WSMP) | TM-40L, TM-50L |
| ADatP-36 | Friendly Force Information (FFI) | TM-40A, TM-40C |
| STANAG 5527 | Friendly Force Tracking Systems Interoperability | TM-40A |
