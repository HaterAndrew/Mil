# MAVEN TRAINING CORPUS — DEPENDENCY MAP
## USAREUR-AF Operational Data Team | C2DAO Training Branch

> **PUBLISHED OUTPUT:** The authoritative HTML dependency map is `maven_training/DEPENDENCY_MAP.html` (7,400+ lines). **Do NOT overwrite it with the short ~900-line file produced by `scripts/generate_dep_map.py`.** That script generates a disposable summary — it must NEVER write to `DEPENDENCY_MAP.html`. If you need to update the dep map, edit `DEPENDENCY_MAP.html` directly. Never open, reference, or show the short generated version.

**Generated:** 13 March 2026
**Last structural change:** 18 March 2026 — Added T3 Train-the-Trainer tracks: T3-I (Instructor Certification, 5 days, prereq SL 3) and T3-F (MSC Force Multiplier / Unit Data Trainer, half day, prereq SL 2); added SL 4N (UI/UX Designer) and SL 4O (Platform Engineer) specialist tracks with SL 5N/SL 5O advanced tracks; ASF role alignment (PM, Designer, SWE, Platform Engineer); prereq chain extended G–O
**Last updated:** 18 March 2026 (integrated USAREUR-AF Data and Analytics Strategy (CG-signed May 2025) and Unified Data Transition Strategy (CUI quarterly product cycle) into corpus — Sec 0B, Sec 5, External Refs, doctrine panel, publications index; changelog #118–119)
**Audit method:** Full manual read of all source files across 6 parallel agent passes (13 March); ralf branch content migration (14 March); Palantir Developers video mapping (14 March); full ralf file inventory and PDF build (14 March); full content read of all 30 CDA slide decks (14 March) — level assignments corrected corpus-wide; pre-v2.0 content accuracy and consistency audit across all curriculum, app, widget, and PPTX files (14 March)
**Status at generation:** Corpus at v2.0-ready state. All naming and content issues resolved. SL 4D/E/F prereq discrepancy resolved 2026-03-14 — all WFF tracks (SL 4A–F) now require SL 3 as terminal prerequisite. SL 4N (UI/UX Designer), SL 4O (Platform Engineer), and corresponding SL 5N/SL 5O advanced tracks added 2026-03-18 with ASF role alignment. Pre-v2.0 audit complete: 8 content fixes applied (README.md, POLICY_LETTER.md, cheatsheet.md, Home.tsx, TM40.tsx, mss_info_app/index.html, .gitignore, MSS_Project_Overview.pptx); MSS_Training_Progression.pptx specialist column fully rebuilt with clean WFF (A–F) / Specialist (G–O) grouping. PDFs regenerated (3 source-changed files rebuilt). See changelog entry #95–103.

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
[EXEC] Senior Leader ← O-5 / E-9+; replaces SL 1 for SL; terminal (no further progression)
         │                 No prereqs. No TM credit granted. Does not feed into TM pipeline.
         │
SL 1 (all other personnel)
  └── SL 2 (builders)
        │
        ├── [FBC] Foundry Bootcamp ← parallel track; outside TM chain; no TM credit granted
        │         Prereq: SL 2 Go + command-validated project. See foundry_bootcamp/FBC_GUIDE.md
        │
        ├── [T3-F] MSC Force Multiplier ← Unit Data Trainer certification (half day)
        │         Prereq: SL 2 Go + commander nomination. Authorizes: SL 1 delivery,
        │         SL 1 exam proctoring, training status reporting to C2DAO.
        │         Does NOT grant SL 3 credit. Does NOT unlock SL 4 enrollment.
        │
        └── SL 3 (advanced builders / data-adjacent)
              │
              ├── [T3-I] Instructor Certification ← C2DAO instructor pipeline
              │         Prereq: SL 3 Go + C2DAO Training OIC selection.
              │         Phase 1: 5-day classroom. Phase 2: supervised practicum (separate).
              │         Graduates authorized to teach SL 1 through SL 3 (+ domain tracks per FDP).
              │
              ├── SL 4A (Intelligence WFF)
              ├── SL 4B (Fires WFF)
              ├── SL 4C (Movement & Maneuver WFF)
              ├── SL 4D (Sustainment WFF)
              ├── SL 4E (Protection WFF)
              ├── SL 4F (Mission Command WFF)
              ├── SL 4G (ORSA) ──────────────→ SL 5G (Advanced ORSA)
              ├── SL 4H (AI Engineer) ────────→ SL 5H (Advanced AI Eng)
              ├── SL 4M (ML Engineer) ────────→ SL 5M (Advanced ML Eng)
              ├── SL 4J (Program Manager) ────→ SL 5J (Advanced PM)
              ├── SL 4K (Knowledge Manager) ──→ SL 5K (Advanced KM)
              ├── SL 4L (Software Engineer) ──→ SL 5L (Advanced SWE)
              ├── SL 4N (UI/UX Designer) ────→ SL 5N (Advanced UI/UX)
              └── SL 4O (Platform Engineer) ──→ SL 5O (Advanced Platform Eng)
```

> **NOTE:** SL 5A through SL 5F do NOT exist. Only SL 5G–O (advanced specialist) are valid.
> WFF tracks (SL 4A–F) require SL 3 (same prereq chain as Specialist tracks) — design decision 2026-03-13.
> Specialist tracks (SL 4G–O) all require SL 3 (required, not recommended).
> SL 4N (UI/UX Designer) and SL 4O (Platform Engineer) align with Army Software Factory (ASF) role tracks. Together with SL 4J (PM) and SL 4L (SWE), these four tracks cover all ASF career paths.
> **Cross-track companions:** SL 4N ↔ SL 4J ↔ SL 4L form the ASF "balanced team" triad (Designer + PM + Engineer). SL 4O ↔ SL 4L (platform ↔ application boundary). SL 4O ↔ SL 4H (infrastructure for AI workloads).
> **Foundry Bootcamp (FBC)** is a separate quarterly event outside the TM chain. Prereq: SL 2. Does NOT grant SL 3 credit. Does NOT unlock SL 4 enrollment. See training_management/FOUNDRY_BOOTCAMP_SOP.md.
> **Senior Leader (EXEC)** is a separate 1-day executive course outside the TM chain. Audience: O-5 / E-9+. Replaces SL 1 for senior leaders. Terminal — does not unlock SL 2 or any further progression. Does NOT grant SL 1 credit.
> **T3-F (MSC Force Multiplier)** certifies Unit Data Trainers (UDTs) at the MSC level. Prereq: SL 2. Half day. Authorizes SL 1 delivery, SL 1 exam proctoring, and training status reporting. UDTs are the forward training presence between MTT rotations. Does NOT authorize SL 2 or any SL 3+ delivery.
> **T3-I (Instructor Certification)** is the formal C2DAO instructor pipeline. Prereq: SL 3 + OIC selection. Phase 1 is a 5-day classroom course (adult learning, lab facilitation, evaluation calibration, microteaching). Phase 2 is a supervised practicum scheduled around actual course iterations. Graduates are authorized to teach independently per domain qualification (FDP §2-1). See UNIT_DATA_TRAINER_SOP.md for T3-F governance and FACULTY_DEVELOPMENT_PLAN.md for T3-I certification standards.

---

## CDA SLIDE LIBRARY OVERLAY (CONCEPTUAL PREREQS)

The CDA slide decks provide conceptual grounding that the TM series assumes but does not teach.
They are recommended reading, not required prerequisites. They feed into the TM chain as follows.

**Last alignment audit:** 14 March 2026 — full content read of all 30 decks; level assignments
corrected based on actual slide content vs. TM audience (user / no-code builder / advanced builder / code-level).

```
CDA "SL 1" (2 decks) ──────────────⇢ SL 1 / all personnel
  army_data_orientation_v1             ⇢ SL 1 — WHY MSS exists; Army data landscape; all personnel
                                           v2 (army_data_orientation_v2.pptx) patches slides 12–14
                                           for end-user (consumer) audience; v1 had builder framing
  mss_platform_overview                ⇢ SL 1 — NEW (2026-03-14): HOW to use MSS as an end user
                                           Covers: platform navigation, reading dashboards, AIP
                                           queries, submitting forms, classification handling,
                                           problem reporting, user vs. builder boundary
                                           File: source_material/course_portal/downloads/mss_platform_overview.pptx

CDA "Intro To Data" (10 decks) ─────⇢ SL 2 (conceptual prereqs for no-code builders)
  architecture_primer                  ⇢ before SL 2 (stability stack, activities vs enablers)
                                           [was tagged SL 1 — wrong; no end-user content]
  2026_Data_Stack_Deep_Dive            ⇢ before SL 2 (five-layer L1–L5 stack overview)
  AI_ML_Beyond_The_Hype               ⇢ SL 2 (what AI actually is; why clean ontology enables AIP)
                                           [was tagged SL 4H — wrong; no code content; SL 2 builders
                                           need this to understand why good data enables AIP]
  The_Semantic_Layer_Instructions      ⇢ SL 2 (slides 1–6) / SL 3 (slides 7–11 governance content)
  What_Is_An_Ontology                  ⇢ SL 2 (three building blocks, definition clarity test)
  L5_Activation_Interface_Deep_Dive    ⇢ SL 2 (Workshop/activation decision framework slides 1–5)
                                           NOTE: slides 6–9 (Custom React Widgets, Streamlit, Plotly)
                                           are SL 4L content — not SL 2
  Dont_Filter_This_Isnt_Excel          ⇢ SL 2 (platform mindset shift; essential for all builders)
  L2_Ingestion_Integration_Deep_Dive   ⇢ SL 3 (CDC, DAGs, orchestration, schema evolution)
                                           [was tagged SL 2 — wrong; no-code builders don't design CDC]
  Data_Modeling_Foundations            ⇢ SL 3 (Kimball, Inmon, DataVault, Enterprise Compass)
                                           [was tagged SL 2 — wrong; too academic for no-code builders]
  Data_Platforms_Cloud_Deep_Dive       ⇢ SL 3 (JWCC, cross-domain, edge, OCONUS design concerns)
                                           [was tagged SL 2 — slides 1–4 fine at SL 2 but 5–10 are SL 3]
  decision_advantage_deep_dive         ⇢ SL 3 / all WFF tracks SL 4A–F (ADP 3-13 doctrine framework;
                                           decision-as-node-graph; maps to Foundry object types)
                                           [was tagged SL 4A — wrong; not Intel-WFF-specific; no code]

CDA "Data 101" (6 decks) ────────────⇢ SL 2 / SL 3
  The_Four_Layers                      ⇢ SL 2 (ontology vs dataset vs pipeline vs app; essential)
  Data_Modeling_Fundamentals_Level1    ⇢ SL 2 (tables, keys, cardinality, schemas, data types)
  ObjectType_WhatToWatchFor            ⇢ SL 2 (filter-as-type anti-pattern; downstream avalanche)
  Links_and_Relationships              ⇢ SL 2 (cardinality, direction, optionality)
  Controlled_Vocabularies              ⇢ SL 2 / SL 3 (needed before building first object type)
                                           [was tagged SL 3 only — should start at SL 2]
  Identity_Who_Owns_The_Key            ⇢ SL 2 / SL 3 (primary key authority, six rules, entity resolution)
                                           [was tagged SL 3 only — fundamentals needed at SL 2]

CDA "Data 201" (10 decks) ───────────⇢ SL 3 / SL 4G–O
  Semantic_Modelling_Course_Intro      ⇢ SL 3 / SL 4L (entry to 12-deck series; prereq: DM L2)
  Deck_01_Architecture_First_Principles ⇢ SL 3 / SL 4L (separation of concerns, stability stack)
  Deck_02_Scope_Engineering            ⇢ SL 3 (schema fit vs scope fit, fit scorecard)
  Deck_03_RDF_OWL_Foundations          ⇢ SL 3 (part of 12-deck series; RDF/OWL/SKOS/SHACL)
                                           [was tagged SL 4K — wrong; this is Deck 3 of the same
                                           series as Decks 1, 2, 4, 5, 6 which are all SL 3]
  Deck_04_Object_Type_Varieties        ⇢ SL 3 / SL 4L (nine canonical varieties, decision tree)
  Deck_05_Identity_Governance          ⇢ SL 3 / SL 4K (identity authority matrix, entity resolution arch)
  Deck_06_Relationship_Modeling        ⇢ SL 3 / SL 4L (reification, role patterns, SHACL constraints)
  Deck_07_Temporal_Bitemporal          ⇢ SL 3 (part of 12-deck series; event/state, bitemporal patterns)
                                           [was tagged SL 4G — wrong; temporal modeling is general SL 3;
                                           applies across all specializations not just ORSA]
  Data_Modeling_Fundamentals_Level2    ⇢ SL 4 general / SL 4G / SL 4M / SL 4L
                                           (Kimball/Inmon/DataVault comparison, Enterprise Compass)
  Deck_12_Capstone_Foundry             ⇢ SL 4 general (end-to-end ontology engineering capstone;
                                           prereq: Decks 1–11; bridges SL 3 theory → SL 4 practice)
                                           [was tagged SL 4G only — not ORSA-specific]
```

---

## SECTION 0B — CDA DOCTRINE AND REFERENCE MATERIALS

### Enterprise Architecture (SL 3 / SL 4K / SL 4L)
| File | Type | Supports |
|---|---|---|
| doctrine/enterprise_architecture/EA_00_REFERENCE_CARD.md | [EA] | → SL 3, SL 4K, SL 4L |
| doctrine/enterprise_architecture/EA_01_FOUNDATION.md | [EA] | → SL 3 (architecture thinking) |
| doctrine/enterprise_architecture/EA_02_SCHOOLS_OF_THOUGHT.md | [EA] | → SL 3, SL 4K |
| doctrine/enterprise_architecture/EA_03_ARTIFACTS_AND_VIEWS.md | [EA] | → SL 4K, SL 4L |
| doctrine/enterprise_architecture/EA_04_GOVERNANCE.md | [EA] | → SL 4K |
| doctrine/enterprise_architecture/EA_05_MILITARY_APPLICATION.md | [EA] | → SL 3, SL 4G–O |

### Command Strategy
| File | Type | Supports |
|---|---|---|
| doctrine/USAREUR_AF_DATA_ANALYTICS_STRATEGY.md | [SUPP] | → All TMs, COMMANDERS_GUIDE, POLICY_LETTER (USAREUR-AF Data and Analytics Strategy; CG-signed May 2025; 4 strategic outcomes, VAULTIS framework, Cognitive Hierarchy) |
| doctrine/UNIFIED_DATA_TRANSITION_STRATEGY.md | [SUPP] | → SL 3, SL 4G–O, SL 5G–O (Unified Data Transition Strategy quarterly product cycle; CUI; Discovery & Framing → PSB → Iteration & Implementation) |

### Senior Leader Guidance
| File | Type | Supports |
|---|---|---|
| doctrine/CG_GUIDANCE.md | [REF] | → SL 1, SL 2 (CG public doctrine; AUSA 2025, Green Notebook 2026) |

### CDA Doctrine (SL 4G–O)
| File | Type | Supports |
|---|---|---|
| doctrine/CDA_CONSTRAINTS_AND_DIRECTIVES.md | [CNCPT] | → SL 4G–O (12 operational constraints and directives governing CDA work) |
| doctrine/cda_doctrine/CDA_OVERVIEW.md | [CNCPT] | → SL 3 (bridge: CDA user taxonomy, enterprise index) |
| doctrine/cda_doctrine/CDA_DOCTRINE_OVERVIEW.md | [CNCPT] | → SL 4G–O (doctrine-driven development) |
| doctrine/cda_doctrine/CDA_DOCTRINE_AGENT.md | [CNCPT] | → SL 4H, SL 4L |
| doctrine/cda_doctrine/CDA_AVT25_ASSESSMENT.md | [CNCPT] | → SL 4G, SL 4H |
| doctrine/cda_doctrine/CDA_IDENTITY_VS_CLASSIFICATION.md | [CNCPT] | → SL 3, SL 4K, SL 4L |
| doctrine/ONTOLOGY_DESIGN_PRINCIPLES.md | [CNCPT] | → SL 4H, SL 4K, SL 4L, SL 5H/K/L (DDD, DRY, Open/Closed, PECS, Composition; Foundry-specific) |

### CDA Architecture Doctrine — Agents Series (SL 4H/M/K/L, SL 5H/M/K/L)
Bedrock → specialization hierarchy. Core Principles govern; specialized docs extend.
| File | Type | Supports |
|---|---|---|
| doctrine/cda_doctrine/agents/CDA_AGENTS_OVERVIEW.md | [CNCPT] | → index for agents subdirectory; hierarchy diagram |
| doctrine/cda_doctrine/agents/CDA_AGENTS_CORE_PRINCIPLES.md | [CNCPT] | → SL 4H, SL 4M, SL 4K, SL 4L, SL 5H/M/K/L (12 bedrock principles: Stability Stack, Four-Layer Architecture, Scope Engineering, Nine Object Types, Identity Governance, VAULTIS-A, 14 anti-patterns) |
| doctrine/cda_doctrine/agents/CDA_AGENTS_ONTOLOGY_ENGINEER.md | [CNCPT] | → SL 4H, SL 4K, SL 4L, SL 5H/K/L (specializes Core Principles 3/7/8/9/10/11; RDF, OWL2, SHACL, SPARQL, PROV-O; SHACL shapes, competency questions) |
| doctrine/cda_doctrine/agents/CDA_AGENTS_ENTITY_RESOLUTION.md | [CNCPT] | → SL 4H, SL 4M, SL 4L, SL 5H/M/L (9-stage ER pipeline; blocking, scoring, decisioning, cluster building, survivorship; threshold bands; 10 anti-patterns) |
| doctrine/cda_doctrine/agents/CDA_AGENTS_INGESTION_INTEGRATION.md | [CNCPT] | → SL 4H, SL 4M, SL 4L, SL 5H/M/L (Five-Stage Ingestion Pattern; ELT over ETL; Dagster DAG; VAULTIS-A per pipeline; 9 anti-patterns; 10-item output checklist) |

### GDAP — Global Doctrine Alignment Platform (SL 4H/M/K/L, SL 5H/M/K/L)
| File | Type | Supports |
|---|---|---|
| doctrine/gdap/GDAP_OVERVIEW.md | [CNCPT] | → SL 4H, SL 4M, SL 4K, SL 4L (platform quickstart, LlamaIndex retrieval stack, API endpoints) |
| doctrine/gdap/GDAP_VISION.md | [CNCPT] | → SL 4H, SL 4M, SL 4K, SL 4L, SL 5H/M/K/L (full vision: 10 use-case domains, 20 pipeline steps, DVEE, coalition seam detection) |
| doctrine/gdap/GDAP_PERSISTENCE_STRATEGY.md | [CNCPT] | → SL 4H, SL 4M, SL 4L, SL 5H/M/L (DuckDB = canonical truth; LlamaIndex = derived serving artifacts; versioning/rebuild/rollback policy) |
| doctrine/gdap/GDAP_ACCEPTANCE_TESTS.md | [CNCPT] | → SL 4H, SL 4M, SL 4L, SL 5H/M/L (P0/P1/P2 release gates across 9 sections: A=Foundation, B=Ingestion, C=Retrieval, D=Routing, E=Response Quality, F=Agents, G=Evaluation, H=Ops, I=Consumer Delight) |
| doctrine/gdap/GDAP_ADR_0001_LLAMAINDEX.md | [CNCPT] | → SL 4H, SL 4M, SL 4L, SL 5H/M/L (ADR-0001 accepted: DuckDB owns canonical truth; LlamaIndex owns serving artifacts; boundary rules) |

### MIM — MIP Information Model (SL 4H/M/K/L, SL 5H/M/K/L)
| File | Type | Supports |
|---|---|---|
| doctrine/mim/MIM_OVERVIEW.md | [CNCPT] | → SL 4H, SL 4M, SL 4K, SL 4L (toolchain: HTML/XSD parsers, Foundry backend, repo structure, package quick ref) |
| doctrine/mim/MIM_STANDARD.md | [CNCPT] | → SL 4H, SL 4M, SL 4K, SL 4L, SL 5H/M/K/L (MIM semantic model: namespaces, type/instance/status, roles, discriminators, code types, design principles, Semantic IDs) |
| doctrine/mim/MIM_STATE.md | [CNCPT] | → SL 4H, SL 4M, SL 4L, SL 5H/M/L (project snapshot 2026-02-28: maturity by area, passing/failing tests, key gaps, 30/60/90 priorities) |
| doctrine/mim/MIM_ACADEMICS.md | [CNCPT] | → SL 4H, SL 4M, SL 4K, SL 4L, SL 5H/M/K/L (Dr. Gerz / NATO interoperability; MIM↔Foundry structural alignment analysis; UML↔OT mapping; MIP governance) |
| doctrine/mim/MIM_DECISION_RECORDS.md | [CNCPT] | → SL 4H, SL 4L (ADR structure decision: repo-level and per-package ADRs) |
| doctrine/mim/MIM_FUTURE_CLASSES.md | [CNCPT] | → SL 4H, SL 4M, SL 4L, SL 5H/M/L (planned: mim-studio, mim-ui, adapters, backends, mim-sdk, mim-provenance) |
| doctrine/mim/MIM_ONTOLOGY_DOCS.md | [CNCPT] | → SL 4H, SL 4L, SL 5H/L (OSDK Maker Package full TypeScript API: SPTs, Value Types, Interfaces, Objects, Links, Interface Link Constraints, Actions, Derived Properties) |

### Canon Reference (SL 4G–O)
| File | Type | Supports |
|---|---|---|
| doctrine/cda_doctrine/canon/CANON_ADP_CROSSWALK.md | [CANON] | → all specialist tracks SL 4G–O |
| doctrine/cda_doctrine/canon/CANON_CONDITIONS_INDICATORS_THRESHOLDS.md | [CANON] | → SL 4G, SL 4H |
| doctrine/cda_doctrine/canon/CANON_ENGAGEMENT.md | [CANON] | → SL 4G, SL 4H |
| doctrine/cda_doctrine/canon/CANON_INFORMATION.md | [CANON] | → SL 4H, SL 4K |

### Quick Reference
| File | Type | Supports |
|---|---|---|
| quick_reference/cda_reference/EA_VS_DA.md | [REF] | → SL 3, SL 4K |
| quick_reference/cda_reference/ENTERPRISE_DATA_COMPASS.md | [REF] | → SL 4J, SL 4K |
| quick_reference/cda_reference/LESSONS_LEARNED.md | [REF] | → all tracks |
| quick_reference/cda_reference/PLAN_FOR_SUCCESS.md | [REF] | → SL 4J, SL 3 |
| quick_reference/cda_reference/DOCTRINE_ELEMENT_FOUNDRY_MAPPING.md | [REF] | → SL 4H, SL 4M, SL 4L, SL 5H/M/L (DoctrineElement property map, bi-temporal fields, TypeScript interface, OSDK query patterns, link types, enums) |
| exercises/exams/EXAM_CDA_FINAL.md | [EXAM] | → assesses Intro To Data + Data 101 + Data 201 |

### Interactive Apps
| App | Type | Supports |
|---|---|---|
| source_material/cda_apps/ea-vs-da-reference/ | [REF] | → SL 3, SL 4K, SL 4L |
| source_material/cda_apps/enterprise-data-compass/ | [REF] | → SL 4J, SL 4K |
| source_material/cda_apps/lessons-learned/ | [REF] | → all tracks |
| source_material/cda_apps/plan-for-success/ | [REF] | → SL 4J, SL 3 |
| source_material/course_portal/ | [PPT] | → see CDA Slide Library above |

---

## SECTION 0C — SENIOR LEADER EXECUTIVE COURSE (EXEC)
### Audience: O-5 / E-9+. No prereqs. Terminal qualification — does not feed into TM pipeline.
### Replaces SL 1 for senior leaders. Does NOT grant SL 1 credit.

| File | Type | Outbound Dependencies |
|---|---|---|
| TM_EXEC_SENIOR_LEADER.md | [TM] | ⇢ CG_GUIDANCE (strategic context), ⇢ DATA_LITERACY_technical_reference, ⇢ SL 1 (if SL wants hands-on) |
| CONCEPTS_GUIDE_TM_EXEC_SENIOR_LEADER.md | [CNCPT] | ↔ TM_EXEC_SENIOR_LEADER [TM] (read-ahead companion) |
| SYLLABUS_TM_EXEC.md | [SYL] | → EXEC [TM] |
| (no Exercise) | — | Assessment is organizational, not individual |
| (no Exam) | — | Qualification recorded as "Complete" upon attendance |

**Inbound references from:** DEPENDENCY_MAP prereq chain, ENROLLMENT_SOP, ANNUAL_TRAINING_SCHEDULE, MTP, mss_info_app/index.html (if applicable)

**Recommended pre-reading:** ⇢ CG_GUIDANCE.md · DATA_LITERACY_technical_reference Ch 1

**Key governance note:** EXEC is a 1-day instructor-led course for O-5 / E-9+ personnel. It replaces SL 1 for this population. It covers formation-level data product impact, agile project management, working with data professionals, governance, and the training pipeline. It is terminal — senior leaders who want hands-on qualification enroll in SL 1 separately.

---

## SECTION 1 — BASE TRACKS

### SL 1: Maven User
| File | Type | Outbound Dependencies |
|---|---|---|
| TM_10_MAVEN_USER.md | [TM] | → SL 2 (next step), ⇢ DATA_LITERACY_technical_reference |
| (no Concepts Guide) | — | — |
| SYLLABUS_TM10.md | [SYL] | → SL 1 [TM] |
| EX_10_operator_basics/EXERCISE.md | [EX] | → SL 1 [TM] |
| EXAM_TM10_PRE.md | [EXAM] | assesses SL 1 readiness |
| EXAM_TM10_SUPPLEMENTAL.md | [EXAM] | optional supplemental knowledge check for SL 1 |

**Inbound references from:** SL 2, SL 3, SL 4A–F (all list SL 1 as prereq), SYLLABUS_TM20, SYLLABUS_TM30, all SL 4/5 syllabi, MTP, POI, CAD, TEO, ENROLLMENT_SOP, ANNUAL_TRAINING_SCHEDULE, CHEATSHEET, README, QUICK_START

**Recommended CDA decks [PPT]:** ⇢ army_data_orientation_v1 · architecture_primer · 2026_Data_Stack_Deep_Dive

---

### SL 2: Builder
| File | Type | Outbound Dependencies |
|---|---|---|
| TM_20_BUILDER.md | [TM] | → SL 1 (prereq), → SL 3 (escalation), ↔ TM-10 Ch 4/5/8 task refs, ⇢ SL 4M, ⇢ SL 4L |
| CONCEPTS_GUIDE_TM20_BUILDER.md | [CNCPT] | ↔ TM_20_BUILDER [TM] (companion), ⇢ SL 3 escalation guide |
| SYLLABUS_TM20.md | [SYL] | → SL 1 (prereq) |
| EX_20_no_code_builder/EXERCISE.md | [EX] | → SL 2 [TM], → NAMING_AND_GOVERNANCE_STANDARDS |
| EXAM_TM20_PRE.md | [EXAM] | assesses SL 2 readiness |
| EXAM_TM20_POST.md | [EXAM] | assesses SL 2 completion |

**Inbound references from:** SL 3, SL 4A–O (prereq chain via SL 3), all training mgmt docs, CHEATSHEET, README

**Recommended CDA decks [PPT]:** ⇢ What_Is_An_Ontology · Data_Modeling_Foundations · The_Semantic_Layer_Instructions · L2_Ingestion_Integration_Deep_Dive · L5_Activation_Interface_Deep_Dive · Dont_Filter_This_Isnt_Excel · The_Four_Layers · Data_Modeling_Fundamentals_Level1 · ObjectType_WhatToWatchFor · Links_and_Relationships

---

### SL 3: Advanced Builder
| File | Type | Outbound Dependencies |
|---|---|---|
| TM_30_ADVANCED_BUILDER.md | [TM] | → SL 1 (prereq), → SL 2 (prereq), ⇢ DATA_LITERACY_technical_reference |
| CONCEPTS_GUIDE_TM30_ADVANCED_BUILDER.md | [CNCPT] | ↔ TM_30_ADVANCED_BUILDER [TM] (companion), ⇢ SL 4G–O escalation guide, ⇢ EA Series, ⇢ CDA doctrine |
| SYLLABUS_TM30.md | [SYL] | → SL 1, → SL 2 (prereqs) |
| EX_30_advanced_builder/EXERCISE.md | [EX] | → SL 3 [TM], → NAMING_AND_GOVERNANCE_STANDARDS |
| EXAM_TM30_PRE.md | [EXAM] | assesses SL 3 readiness |
| EXAM_TM30_POST.md | [EXAM] | assesses SL 3 completion |

**Inbound references from:** SL 4A–F (all WFF tracks, hard prereq), SL 4G–O (all specialist tracks, hard prereq), SL 4K (pipeline builder), SL 4L (peer note), all training mgmt docs, CHEATSHEET, README

**Recommended CDA decks [PPT]:** ⇢ Data_Architecture_Deep_Dive · Data_Platforms_Cloud_Deep_Dive · Semantic_Modelling_Course_Intro · Deck_01_Architecture_First_Principles · Deck_02_Scope_Engineering · Deck_04_Object_Type_Varieties · Deck_05_Identity_Governance · Deck_06_Relationship_Modeling · Controlled_Vocabularies · Identity_Who_Owns_The_Key

---

## SECTION 1B — FOUNDRY BOOTCAMP (FBC)
### Prereq: SL 2 Go on file + command-approved project
### NOT part of the SL 1 → SL 5 sequence; does NOT grant TM credit
> Quarterly 5-day supervised build event. Does NOT grant SL 3 credit. Does NOT unlock SL 4 enrollment. See training_management/FOUNDRY_BOOTCAMP_SOP.md.

| File | Type | Outbound Dependencies |
|---|---|---|
| foundry_bootcamp/FBC_GUIDE.md | [FBC] | → SL 2 (prereq); does NOT → SL 3 (explicitly not a substitute) |
| foundry_bootcamp/ENVIRONMENT_SETUP.md | [FBC] | → FBC_GUIDE (coordinator checklist for bootcamp setup) |
| foundry_bootcamp/SPRINT_PACKAGE.md | [FBC] | → FBC_GUIDE Ch 5 (evaluator/coordinator standards); → ENROLLMENT_SOP (enrollment workflow) |
| training_management/FOUNDRY_BOOTCAMP_SOP.md | [SOP] | → SL 2 (prereq); → FBC_GUIDE, → SPRINT_PACKAGE, → ENVIRONMENT_SETUP (references all FBC docs); → ANNUAL_TRAINING_SCHEDULE (quarterly calendar) |

**Inbound references from:** DEPENDENCY_MAP prereq chain, DEMO_BRIEF_CG, WHITE_PAPER_MSS_TRAINING, mss_info_app/index.html (if applicable)

---

## SECTION 1C — TRAIN THE TRAINER (T3)

### T3-F: MSC Force Multiplier (Unit Data Trainer Certification)
#### Prereq: SL 2 Go on file + unit commander nomination
#### Half day (4 hours) — Authorizes SL 1 delivery, SL 1 exam proctoring, training status reporting

| File | Type | Outbound Dependencies |
|---|---|---|
| tm/T3_F_msc_force_multiplier/T3_F_MSC_FORCE_MULTIPLIER.md | [COURSE] | → SL 2 (prereq); → SL 1 (delivery authorization); ↔ INSTRUCTOR_OVERVIEW (instructor ecosystem context); → UNIT_DATA_TRAINER_SOP (governance) |
| tm/T3_F_msc_force_multiplier/CONCEPTS_GUIDE_T3F_MSC_FORCE_MULTIPLIER.md | [CNCPT] | → SL 2 (prereq baseline); ⇢ T3-F [COURSE] (pre-course reading) |
| syllabi/SYLLABUS_T3F.md | [SYL] | → SL 2 (prereq); → CONCEPTS_GUIDE_T3F (pre-course reading) |
| exercises/EX_T3F_force_multiplier/EXERCISE.md | [EX] | → T3-F [COURSE]; → SL 1 lesson plans (teach-back source material) |
| exercises/EX_T3F_force_multiplier/ENVIRONMENT_SETUP.md | [EX] | → T3-F [COURSE] (pre-exercise environment checklist) |
| exercises/exams/EXAM_T3F_PRE.md | [EXAM] | → T3-F [COURSE] (diagnostic — Day 1) |
| exercises/exams/EXAM_T3F_POST.md | [EXAM] | → T3-F [COURSE] (knowledge check — Day 3) |
| training_management/lesson_plans/T3F_LESSON_PLAN_OUTLINES.md | [LP] | → T3-F [COURSE]; → SL 1 lesson plans |
| training_management/UNIT_DATA_TRAINER_SOP.md | [SOP] | → T3-F (cert requirement); → C2DAO reporting procedures; → ENROLLMENT_SOP (unit-level enrollment workflow) |

**Inbound references from:** DEPENDENCY_MAP prereq chain, FACULTY_DEVELOPMENT_PLAN (instructor ecosystem), INSTRUCTOR_OVERVIEW (UDT tier), TASKORD_MSS_TRAINING_CELL (MTT delivery of T3-F at MSC sites)

**Key governance note:** T3-F creates a sustainment capability, not a replacement for C2DAO instructors. UDTs deliver SL 1 between MTT rotations. UDTs do NOT deliver SL 2, SL 3, or any SL 4/SL 5 courses. Curriculum authority remains with C2DAO.

### T3-I: Instructor Certification (C2DAO Instructor Pipeline)
#### Prereq: SL 3 Go on file + C2DAO Training OIC selection
#### Phase 1: 5 days (40 hours) classroom — Phase 2: supervised practicum (scheduled separately)

| File | Type | Outbound Dependencies |
|---|---|---|
| tm/T3_I_instructor_certification/T3_I_INSTRUCTOR_CERTIFICATION.md | [COURSE] | → SL 3 (prereq); → SL 1/SL 2/SL 3 lesson plans (platform walkthrough); → TEO_MSS (evaluation calibration); → FACULTY_DEVELOPMENT_PLAN (certification standards) |
| tm/T3_I_instructor_certification/CONCEPTS_GUIDE_T3I_INSTRUCTOR_CERTIFICATION.md | [CNCPT] | → SL 3 (prereq baseline); ⇢ T3-I [COURSE] (pre-course reading); ⇢ TP 350-70-3, TP 350-70-7 |
| syllabi/SYLLABUS_T3I.md | [SYL] | → SL 3 (prereq); → CONCEPTS_GUIDE_T3I (pre-course reading); → FDP §2-1, §6-1 |
| exercises/EX_T3I_instructor_certification/EXERCISE.md | [EX] | → T3-I [COURSE]; → SL 1/SL 2/SL 3 lesson plans (microteaching source); → TEO_MSS (evaluation scoring) |
| exercises/EX_T3I_instructor_certification/ENVIRONMENT_SETUP.md | [EX] | → T3-I [COURSE] (pre-exercise environment checklist) |
| exercises/exams/EXAM_T3I_PRE.md | [EXAM] | → T3-I [COURSE] (diagnostic — Day 1) |
| exercises/exams/EXAM_T3I_POST.md | [EXAM] | → T3-I [COURSE] (knowledge check — Day 5) |
| training_management/lesson_plans/T3I_LESSON_PLAN_OUTLINES.md | [LP] | → T3-I [COURSE]; → all SL 1/SL 2/SL 3 materials |

**Inbound references from:** DEPENDENCY_MAP prereq chain, FACULTY_DEVELOPMENT_PLAN (certification phases), INSTRUCTOR_OVERVIEW (instructor tier structure), POI_MSS (program scope)

**Key governance note:** T3-I replaces the previous ad-hoc 4-phase apprenticeship with a structured, documented certification pathway. Phase 1 (classroom) covers adult learning principles, platform deep-dive from the instructor seat, lab facilitation, Go/No-Go standardization, microteaching, and common trainee error management. Phase 2 (supervised practicum) is scheduled around actual course iterations — the candidate co-teaches, then leads under observation. Domain qualification for SL 4/SL 5 delivery is a separate requirement per FDP §2-1.

**T3 cross-references:**
- T3-F ↔ T3-I: T3-I graduates may deliver T3-F during MTT rotations. T3-F is introduced in T3-I Ch 1 as the unit-level tier.
- T3-F → UNIT_DATA_TRAINER_SOP: Governs UDT authorities, limitations, reporting, and recertification.
- T3-I → FACULTY_DEVELOPMENT_PLAN: Defines instructor tiers (Instructor → Senior Instructor → Master Instructor), certification phases, and recertification requirements.

---

## SECTION 2 — WFF FUNCTIONAL TRACKS (SL 4A–F)
### Prereq for all: SL 1 + SL 2 + SL 3 + track Concepts Guide

### SL 4A: Intelligence
| File | Type | Outbound Dependencies |
|---|---|---|
| TM_40A_INTELLIGENCE.md | [TM] | → SL 1, → SL 2, → SL 3, → CONCEPTS_GUIDE_TM40A (prereq read), ↔ SL 4F (CCIR coordination) |
| CONCEPTS_GUIDE_TM40A_INTELLIGENCE.md | [CNCPT] | → SL 1 (prereq baseline), ↔ SL 4A [TM] (Appendix D), ⇢ FM 2-0, ATP 2-01.3, ATP 2-01 |
| SYLLABUS_TM40A.md | [SYL] | → SL 1, → SL 2, → SL 3, ⇢ FM 2-0, ATP 2-01 |
| EX_40A_intelligence/EXERCISE.md | [EX] | → SL 4A [TM] |
| EXAM_TM40A_PRE.md | [EXAM] | assesses SL 4A readiness |
| EXAM_TM40A_POST.md | [EXAM] | assesses SL 4A completion |

**Inbound references from:** SL 4D (companion cross-ref), SL 4E (AT intel integration), DATA_LITERACY_technical_reference, CHEATSHEET, mss_info_app/index.html, README

**Recommended CDA decks [PPT]:** ⇢ decision_advantage_deep_dive

---

### SL 4B: Fires
| File | Type | Outbound Dependencies |
|---|---|---|
| TM_40B_FIRES.md | [TM] | → SL 1, → SL 2, → SL 3, → CONCEPTS_GUIDE_TM40B (prereq read), ⇢ SL 4L (system admin) |
| CONCEPTS_GUIDE_TM40B_FIRES.md | [CNCPT] | ↔ SL 4B [TM] (read before SL 4B), ⇢ ADP 3-19, FM 3-09, FM 3-60, ATP 3-01.8, ATP 3-52.2, ATP 3-09.42, ATP 3-09.50 |
| SYLLABUS_TM40B.md | [SYL] | → SL 1, → SL 2, → SL 3, ⇢ FM 3-09, ATP 3-09.42, FM 3-60 |
| EX_40B_fires/EXERCISE.md | [EX] | → SL 4B [TM] |
| EXAM_TM40B_PRE.md | [EXAM] | assesses SL 4B readiness |
| EXAM_TM40B_POST.md | [EXAM] | assesses SL 4B completion |

**Inbound references from:** SL 4D (ammo mgmt companion), SL 4E (AMD coordination), DATA_LITERACY_technical_reference, CHEATSHEET, mss_info_app/index.html, README

**Recommended CDA decks [PPT]:** ⇢ decision_advantage_deep_dive

---

### SL 4C: Movement & Maneuver
| File | Type | Outbound Dependencies |
|---|---|---|
| TM_40C_MOVEMENT_MANEUVER.md | [TM] | → SL 1, → SL 2, → SL 3, → CONCEPTS_GUIDE_TM40C (prereq read), ↔ SL 4E (NBC/protection layer) |
| CONCEPTS_GUIDE_TM40C_MOVEMENT_MANEUVER.md | [CNCPT] | ↔ SL 4C [TM] (doctrinal framework), ⇢ ADP 3-0, FM 3-96 |
| SYLLABUS_TM40C.md | [SYL] | → SL 1, → SL 2, → SL 3, ⇢ ADP 3-0, FM 3-0, ATP 3-90.90 |
| EX_40C_movement_maneuver/EXERCISE.md | [EX] | → SL 4C [TM] |
| EXAM_TM40C_PRE.md | [EXAM] | assesses SL 4C readiness |
| EXAM_TM40C_POST.md | [EXAM] | assesses SL 4C completion |

**Inbound references from:** SL 4D (maneuver unit readiness companion), SL 4E (physical security/base camp siting), DATA_LITERACY_technical_reference, CHEATSHEET, mss_info_app/index.html, README

**Recommended CDA decks [PPT]:** ⇢ decision_advantage_deep_dive

---

### SL 4D: Sustainment
| File | Type | Outbound Dependencies |
|---|---|---|
| TM_40D_SUSTAINMENT.md | [TM] | → SL 1, → SL 2, → SL 3, → CONCEPTS_GUIDE_TM40D (prereq read), ↔ SL 4A (intel/threat feed), ↔ SL 4B (ammo coordination), ↔ SL 4C (maneuver readiness), ↔ SL 4E (CBRN/convoy protection), ↔ SL 4F (COP/LOGSTAT), ⇢ SL 4M (ML models) |
| CONCEPTS_GUIDE_TM40D_SUSTAINMENT.md | [CNCPT] | ↔ SL 4D [TM] (para 4-7), ↔ SL 4F (COP framework/S4 producer) |
| SYLLABUS_TM40D.md | [SYL] | → SL 1, → SL 2, → SL 3, ⇢ ADP 4-0, FM 4-0, ATP 4-0.1 |
| EX_40D_sustainment/EXERCISE.md | [EX] | → SL 4D [TM] |
| EXAM_TM40D_PRE.md | [EXAM] | assesses SL 4D readiness |
| EXAM_TM40D_POST.md | [EXAM] | assesses SL 4D completion |

**Inbound references from:** SL 4E (CBRN resupply), CHEATSHEET, mss_info_app/index.html, README

**Recommended CDA decks [PPT]:** ⇢ decision_advantage_deep_dive

---

### SL 4E: Protection
| File | Type | Outbound Dependencies |
|---|---|---|
| TM_40E_PROTECTION.md | [TM] | → SL 1, → SL 2, → SL 3, → CONCEPTS_GUIDE_TM40E (prereq read), ↔ SL 4A (AT intel), ↔ SL 4B (AMD coordination), ↔ SL 4C (base camp siting), ↔ SL 4D (CBRN resupply/medical), ↔ SL 4F (COP/CCIR protection data), ⇢ SL 4L (pipeline construction) |
| CONCEPTS_GUIDE_TM40E_PROTECTION.md | [CNCPT] | ↔ SL 4E [TM] (Appendix A naming, Appendix H data quality) |
| SYLLABUS_TM40E.md | [SYL] | → SL 1, → SL 2, → SL 3, ⇢ ADP 3-37, ATP 3-37.2 |
| EX_40E_protection/EXERCISE.md | [EX] | → SL 4E [TM] |
| EXAM_TM40E_PRE.md | [EXAM] | assesses SL 4E readiness |
| EXAM_TM40E_POST.md | [EXAM] | assesses SL 4E completion |

**Inbound references from:** SL 4C (NBC data integration), DATA_LITERACY_technical_reference, CHEATSHEET, mss_info_app/index.html, README

**Recommended CDA decks [PPT]:** ⇢ decision_advantage_deep_dive

---

### SL 4F: Mission Command
| File | Type | Outbound Dependencies |
|---|---|---|
| TM_40F_MISSION_COMMAND.md | [TM] | → SL 1, → SL 2, → SL 3, → CONCEPTS_GUIDE_TM40F (prereq read), ↔ SL 4G (ORSA products for G35), ↔ SL 4H (AI-enabled CCIR alerts), ↔ SL 4M (predictive products), ↔ SL 4J (PM readiness/portfolio), ↔ SL 4K (KM info products/lessons learned) |
| CONCEPTS_GUIDE_TM40F_MISSION_COMMAND.md | [CNCPT] | ↔ SL 4F [TM] (proceed to SL 4F for task instruction), → SL 1 (baseline proficiency) |
| SYLLABUS_TM40F.md | [SYL] | → SL 1, → SL 2, → SL 3, ⇢ ADP 6-0, FM 6-0 |
| EX_40F_mission_command/EXERCISE.md | [EX] | → SL 4F [TM] |
| EXAM_TM40F_PRE.md | [EXAM] | assesses SL 4F readiness |
| EXAM_TM40F_POST.md | [EXAM] | assesses SL 4F completion |

**Inbound references from:** SL 4A (CCIR coordination), SL 4C (S3 coordination), SL 4D (COP/LOGSTAT), SL 4E (COP/CCIR protection), CONCEPTS_GUIDE_TM40D (COP framework), DATA_LITERACY_technical_reference, CHEATSHEET, mss_info_app/index.html, README

**Recommended CDA decks [PPT]:** ⇢ decision_advantage_deep_dive

---

## SECTION 3 — SPECIALIST TRACKS (SL 4G–O)
### Prereq for all: SL 1 + SL 2 + SL 3 (all required)

### SL 4G: ORSA
| File | Type | Outbound Dependencies |
|---|---|---|
| TM_40G_ORSA.md | [TM] | → SL 1, → SL 2, → SL 3, → CONCEPTS_GUIDE_TM40G, ⇢ SL 4H (AI library install), ⇢ SL 4M (ML integration) |
| CONCEPTS_GUIDE_TM40G_ORSA.md | [CNCPT] | ↔ SL 4G [TM] (companion), ⇢ SL 4G Appendix D checklist |
| SYLLABUS_TM40G.md | [SYL] | → SL 1, → SL 2, → SL 3 |
| EX_40G_orsa/EXERCISE.md | [EX] | → SL 4G [TM] |
| EXAM_TM40G_PRE.md | [EXAM] | assesses SL 4G readiness |
| EXAM_TM40G_POST.md | [EXAM] | assesses SL 4G completion |

**Advanced track:** → SL 5G
**Inbound references from:** SL 4J (portfolio analytics), SL 5G (prereq), DATA_LITERACY_technical_reference, CHEATSHEET, task_index.html (17 tasks), mss_info_app/index.html, README

**Recommended CDA decks [PPT]:** ⇢ Data_Modeling_Fundamentals_Level2 · Deck_07_Temporal_Bitemporal · Deck_12_Capstone_Foundry

---

### SL 4H: AI Engineer
| File | Type | Outbound Dependencies |
|---|---|---|
| TM_40H_AI_ENGINEER.md | [TM] | → SL 1, → SL 2, → SL 3, → CONCEPTS_GUIDE_TM40H, ⇢ SL 4M (fine-tuning/model topics) |
| CONCEPTS_GUIDE_TM40H_AI_ENGINEER.md | [CNCPT] | role distinction table with SL 4M, SL 4L; ↔ SL 4H [TM] |
| SYLLABUS_TM40H.md | [SYL] | → SL 1, → SL 2, → SL 3 |
| EX_40H_ai_engineer/EXERCISE.md | [EX] | → SL 4H [TM] |
| EXAM_TM40H_PRE.md | [EXAM] | assesses SL 4H readiness |
| EXAM_TM40H_POST.md | [EXAM] | assesses SL 4H completion |

**Advanced track:** → SL 5H
**Inbound references from:** SL 4F (AI-enabled CCIR), SL 4G (library install), SL 4K (AIP Agent Studio), SL 5G (pipeline architecture), SL 5H (prereq), SL 5L (recommended), DATA_LITERACY_technical_reference, CHEATSHEET, task_index.html (1 task), mss_info_app/index.html, README

**Recommended CDA decks [PPT]:** ⇢ AI_ML_Beyond_The_Hype · Deck_12_Capstone_Foundry

---

### SL 4M: ML Engineer
| File | Type | Outbound Dependencies |
|---|---|---|
| TM_40M_ML_ENGINEER.md | [TM] | → SL 1, → SL 2, → SL 3, → CONCEPTS_GUIDE_TM40M, ⇢ SL 4G (RStudio/ORSA workflows), ⇢ SL 4L (VS Code) |
| CONCEPTS_GUIDE_TM40M_ML_ENGINEER.md | [CNCPT] | role matrix consistent with SL 4G/H/L; ↔ SL 4M [TM] |
| SYLLABUS_TM40M.md | [SYL] | → SL 1, → SL 2, → SL 3 |
| EX_40M_ml_engineer/EXERCISE.md | [EX] | → SL 4M [TM] |
| EXAM_TM40M_PRE.md | [EXAM] | assesses SL 4M readiness |
| EXAM_TM40M_POST.md | [EXAM] | assesses SL 4M completion |

**Advanced track:** → SL 5M
**Inbound references from:** SL 4F (predictive products), SL 4G (ML integration), SL 5G (ML integration), SL 5H (fine-tuning infrastructure), SL 5M (prereq), DATA_LITERACY_technical_reference, CHEATSHEET, task_index.html (21 tasks), mss_info_app/index.html, README

**Recommended CDA decks [PPT]:** ⇢ AI_ML_Beyond_The_Hype · Data_Modeling_Fundamentals_Level2 · Deck_07_Temporal_Bitemporal

---

### SL 4J: Program Manager
| File | Type | Outbound Dependencies |
|---|---|---|
| TM_40J_PROGRAM_MANAGER.md | [TM] | → SL 1, → SL 2, → SL 3 (all required), ⇢ SL 4H, ⇢ SL 4M |
| CONCEPTS_GUIDE_TM40J_PROGRAM_MANAGER.md | [CNCPT] | ↔ SL 4J [TM] |
| SYLLABUS_TM40J.md | [SYL] | → SL 1, → SL 2, → SL 3 (required) |
| EX_40J_program_manager/EXERCISE.md | [EX] | → SL 4J [TM] |
| EXAM_TM40J_PRE.md | [EXAM] | assesses SL 4J readiness |
| EXAM_TM40J_POST.md | [EXAM] | assesses SL 4J completion |

**Advanced track:** → SL 5J
**Inbound references from:** SL 4F (PM readiness/portfolio), SL 5J (prereq, recommends SL 4G/H/M/K/L), DATA_LITERACY_technical_reference, CHEATSHEET, task_index.html (18 tasks), mss_info_app/index.html, README

**Recommended CDA decks [PPT]:** ⇢ Deck_02_Scope_Engineering

---

### SL 4K: Knowledge Manager
| File | Type | Outbound Dependencies |
|---|---|---|
| TM_40K_KNOWLEDGE_MANAGER.md | [TM] | → SL 1, → SL 2, → SL 3 (all required), ⇢ SL 4H (AIP Agent Studio), ⇢ SL 4L (TypeScript/OSDK, custom logic) |
| CONCEPTS_GUIDE_TM40K_KNOWLEDGE_MANAGER.md | [CNCPT] | ↔ SL 4K [TM] |
| SYLLABUS_TM40K.md | [SYL] | → SL 1, → SL 2, → SL 3 (required) |
| EX_40K_knowledge_manager/EXERCISE.md | [EX] | → SL 4K [TM] |
| EXAM_TM40K_PRE.md | [EXAM] | assesses SL 4K readiness |
| EXAM_TM40K_POST.md | [EXAM] | assesses SL 4K completion |

**Advanced track:** → SL 5K
**Inbound references from:** SL 4F (KM info products), SL 5K (prereq), DATA_LITERACY_technical_reference, CHEATSHEET, task_index.html (6 tasks), mss_info_app/index.html, README

**Recommended CDA decks [PPT]:** ⇢ Controlled_Vocabularies · Identity_Who_Owns_The_Key · Deck_03_RDF_OWL_Foundations · Deck_05_Identity_Governance

---

### SL 4L: Software Engineer
| File | Type | Outbound Dependencies |
|---|---|---|
| TM_40L_SOFTWARE_ENGINEER.md | [TM] | → SL 1, → SL 2, → SL 3, → CONCEPTS_GUIDE_TM40L; noted peer to SL 4G/H/M |
| CONCEPTS_GUIDE_TM40L_SOFTWARE_ENGINEER.md | [CNCPT] | role matrix shows SL 4L as SWE; ↔ SL 4L [TM] |
| SYLLABUS_TM40L.md | [SYL] | → SL 1, → SL 2, → SL 3 |
| EX_40L_software_engineer/EXERCISE.md | [EX] | → SL 4L [TM] |
| EXAM_TM40L_PRE.md | [EXAM] | assesses SL 4L readiness |
| EXAM_TM40L_POST.md | [EXAM] | assesses SL 4L completion |

**Advanced track:** → SL 5L
**Inbound references from:** SL 4B (system admin/platform), SL 4E (pipeline construction), SL 4K (custom logic), SL 5L (prereq, SL 4H/M recommended), DATA_LITERACY_technical_reference, CHEATSHEET, task_index.html (30 tasks), mss_info_app/index.html, README

**Recommended CDA decks [PPT]:** ⇢ Deck_03_RDF_OWL_Foundations · Deck_04_Object_Type_Varieties · Deck_06_Relationship_Modeling · Deck_07_Temporal_Bitemporal · Data_Modeling_Fundamentals_Level2 · Deck_12_Capstone_Foundry

---

### SL 4N: UI/UX Designer
| File | Type | Outbound Dependencies |
|---|---|---|
| TM_40N_UX_DESIGNER.md | [TM] | → SL 1, → SL 2, → SL 3, → CONCEPTS_GUIDE_TM40N; ↔ SL 4J (balanced team), ↔ SL 4L (design-to-dev handoff), ↔ SL 4O (platform constraints) |
| CONCEPTS_GUIDE_TM40N_UX_DESIGNER.md | [CNCPT] | role matrix shows SL 4N as Designer; ↔ SL 4N [TM] |
| SYLLABUS_TM40N.md | [SYL] | → SL 1, → SL 2, → SL 3 |
| EX_40N_ux_designer/EXERCISE.md | [EX] | → SL 4N [TM] |
| EXAM_TM40N_PRE.md | [EXAM] | assesses SL 4N readiness |
| EXAM_TM40N_POST.md | [EXAM] | assesses SL 4N completion |

**Advanced track:** → SL 5N
**Cross-track companions:** ↔ SL 4J (PM — balanced team, backlog handoff), ↔ SL 4L (SWE — design implementation), ↔ SL 4O (Platform — performance constraints)
**ASF alignment:** Maps to ASF UI/UX Designer (Product Designer) role. Covers Soldier Centered Design (SCD), user research, information architecture, visual design, prototyping, usability testing, accessibility (Section 508 / WCAG 2.1 AA), and design governance.

---

### SL 4O: Platform Engineer
| File | Type | Outbound Dependencies |
|---|---|---|
| TM_40O_PLATFORM_ENGINEER.md | [TM] | → SL 1, → SL 2, → SL 3, → CONCEPTS_GUIDE_TM40O; ↔ SL 4L (platform consumers), ↔ SL 4H (AI compute infra), ↔ SL 4N (design constraints) |
| CONCEPTS_GUIDE_TM40O_PLATFORM_ENGINEER.md | [CNCPT] | role matrix shows SL 4O as Platform Eng; ↔ SL 4O [TM] |
| SYLLABUS_TM40O.md | [SYL] | → SL 1, → SL 2, → SL 3 |
| EX_40O_platform_engineer/EXERCISE.md | [EX] | → SL 4O [TM] |
| EXAM_TM40O_PRE.md | [EXAM] | assesses SL 4O readiness |
| EXAM_TM40O_POST.md | [EXAM] | assesses SL 4O completion |

**Advanced track:** → SL 5O
**Cross-track companions:** ↔ SL 4L (SWE — primary platform consumer), ↔ SL 4H (AI Eng — model serving infrastructure), ↔ TM-50L Ch.6 (DevSecOps from application perspective — companion reading)
**ASF alignment:** Maps to ASF Platform Engineer role. Covers platform-as-product, Kubernetes, IaC/GitOps, container security (Iron Bank), CI/CD pipeline design, deployment strategies, air-gapped/DDIL operations, and RMF/ATO from infrastructure perspective. References ASF CReATE platform architecture.

---

## SECTION 4 — ADVANCED SPECIALIST TRACKS (SL 5G–O)
### Prereq for each: corresponding SL 4G–O (required)

| Track | Prereq | Key Cross-Refs | Advanced Track File |
|---|---|---|---|
| SL 5G (Adv ORSA) | SL 4G | ↔ SL 4H, SL 4M, SL 4J | TM_50G_ORSA_ADVANCED.md + CG |
| SL 5H (Adv AI Eng) | SL 4H | ↔ SL 5G, SL 5M, SL 5J, SL 5K, SL 5L; ⇢ SL 4M | TM_50H_AI_ENGINEER_ADVANCED.md + CG |
| SL 5M (Adv ML Eng) | SL 4M | ↔ SL 5H (fine-tuning infra) | TM_50M_ML_ENGINEER_ADVANCED.md + CG |
| SL 5J (Adv PM) | SL 4J | ⇢ SL 4G, SL 4H, SL 4M, SL 4K, SL 4L, SL 4N | TM_50J_PROGRAM_MANAGER_ADVANCED.md + CG |
| SL 5K (Adv KM) | SL 4K | ↔ SL 5H (corpus design) | TM_50K_KNOWLEDGE_MANAGER_ADVANCED.md + CG |
| SL 5L (Adv SWE) | SL 4L | ⇢ SL 4H, SL 4M; ↔ SL 5H (OSDK integration) | TM_50L_SOFTWARE_ENGINEER_ADVANCED.md + CG |
| SL 5N (Adv UI/UX) | SL 4N | ↔ SL 5J (portfolio strategy), ↔ SL 5L (design system impl), ↔ SL 5O (perf budgets) | TM_50N_UX_DESIGNER_ADVANCED.md + CG |
| SL 5O (Adv Platform) | SL 4O | ↔ SL 5L (platform-app boundary), ↔ SL 5J (platform roadmap), ↔ SL 5N (portal design) | TM_50O_PLATFORM_ENGINEER_ADVANCED.md + CG |

**Syllabi:** SYLLABUS_TM50G–O present and published
**Exams:** EXAM_TM50G–O PRE + POST present
**Exercises:** EX_50G–O directories present (EX_50G_orsa/, EX_50H_ai_engineer/, EX_50M_ml_engineer/, EX_50J_program_manager/, EX_50K_knowledge_manager/, EX_50L_software_engineer/, EX_50N_ux_designer/, EX_50O_platform_engineer/ — each with EXERCISE.md + ENVIRONMENT_SETUP.md)

---

## SECTION 4B — ARCHITECTURE PUBLICATIONS (PDF)

Standalone reference material. These are published PDF outputs of the CDA, EA, GDAP, MIM, and Ontology architecture documents. No prerequisites — not part of the TM course sequence. Source markdown lives in `doctrine/` subdirectories (cross-referenced in Section 0B).

### CDA — Cognitive Data Architecture

| PDF | Type | Description |
|---|---|---|
| ARCH_CDA_OVERVIEW.pdf | [SUPP] | CDA enterprise index and user taxonomy |
| ARCH_CDA_DOCTRINE_OVERVIEW.pdf | [SUPP] | Doctrine-driven development overview |
| ARCH_CDA_DOCTRINE_AGENT.pdf | [SUPP] | Doctrine agent architecture |
| ARCH_CDA_AVT25_ASSESSMENT.pdf | [SUPP] | AVT-25 assessment framework |
| ARCH_CDA_IDENTITY_VS_CLASSIFICATION.pdf | [SUPP] | Identity vs classification design patterns |
| ARCH_CDA_CONSTRAINTS_AND_DIRECTIVES.pdf | [SUPP] | 12 operational constraints and directives |
| ARCH_CDA_CANON_ADP_CROSSWALK.pdf | [CANON] | ADP crosswalk for all specialist tracks |
| ARCH_CDA_CANON_CONDITIONS.pdf | [CANON] | Conditions, indicators, and thresholds |
| ARCH_CDA_CANON_ENGAGEMENT.pdf | [CANON] | Engagement canon |
| ARCH_CDA_CANON_INFORMATION.pdf | [CANON] | Information canon |
| ARCH_CDA_AGENTS_OVERVIEW.pdf | [SUPP] | Agents subsystem index and hierarchy diagram |
| ARCH_CDA_AGENTS_CORE_PRINCIPLES.pdf | [SUPP] | 12 bedrock principles: Stability Stack, Four-Layer Architecture, anti-patterns |
| ARCH_CDA_AGENTS_ONTOLOGY_ENGINEER.pdf | [SUPP] | Ontology engineer agent specialization (RDF, OWL2, SHACL, SPARQL) |
| ARCH_CDA_AGENTS_ENTITY_RESOLUTION.pdf | [SUPP] | 9-stage entity resolution pipeline |
| ARCH_CDA_AGENTS_INGESTION_INTEGRATION.pdf | [SUPP] | Five-Stage Ingestion Pattern, ELT, Dagster DAG |

### Enterprise Architecture

| PDF | Type | Description |
|---|---|---|
| ARCH_EA_00_REFERENCE_CARD.pdf | [EA] | EA quick-reference card |
| ARCH_EA_01_FOUNDATION.pdf | [EA] | EA foundational concepts |
| ARCH_EA_02_SCHOOLS_OF_THOUGHT.pdf | [EA] | EA schools of thought |
| ARCH_EA_03_ARTIFACTS_AND_VIEWS.pdf | [EA] | EA artifacts and views |
| ARCH_EA_04_GOVERNANCE.pdf | [EA] | EA governance |
| ARCH_EA_05_MILITARY_APPLICATION.pdf | [EA] | EA military application |

### GDAP — Global Doctrine Alignment Platform

| PDF | Type | Description |
|---|---|---|
| ARCH_GDAP_OVERVIEW.pdf | [SUPP] | Platform quickstart, LlamaIndex retrieval stack, API endpoints |
| ARCH_GDAP_VISION.pdf | [SUPP] | Full vision: 10 use-case domains, 20 pipeline steps, DVEE |
| ARCH_GDAP_PERSISTENCE_STRATEGY.pdf | [SUPP] | DuckDB canonical truth, LlamaIndex serving artifacts, versioning policy |
| ARCH_GDAP_ACCEPTANCE_TESTS.pdf | [SUPP] | P0/P1/P2 release gates across 9 sections |
| ARCH_GDAP_ADR_0001_LLAMAINDEX.pdf | [SUPP] | ADR-0001: DuckDB/LlamaIndex boundary rules |

### MIM — MIP Information Model

| PDF | Type | Description |
|---|---|---|
| ARCH_MIM_OVERVIEW.pdf | [SUPP] | Toolchain: HTML/XSD parsers, Foundry backend, repo structure |
| ARCH_MIM_STANDARD.pdf | [SUPP] | MIM semantic model: namespaces, types, roles, design principles |
| ARCH_MIM_STATE.pdf | [SUPP] | Project snapshot: maturity, passing/failing tests, priorities |
| ARCH_MIM_ACADEMICS.pdf | [SUPP] | NATO interoperability, MIM-Foundry alignment, UML-OT mapping |
| ARCH_MIM_DECISION_RECORDS.pdf | [SUPP] | ADR structure: repo-level and per-package decisions |
| ARCH_MIM_FUTURE_CLASSES.pdf | [SUPP] | Planned packages: mim-studio, mim-ui, adapters, backends, mim-sdk |
| ARCH_MIM_ONTOLOGY_DOCS.pdf | [SUPP] | OSDK Maker Package TypeScript API |

### Ontology

| PDF | Type | Description |
|---|---|---|
| ARCH_ONTOLOGY_DESIGN_PRINCIPLES.pdf | [SUPP] | DDD, DRY, Open/Closed, PECS, Composition; Foundry-specific |

---

## SECTION 5 — DOCTRINE & STANDARDS

| File | Type | Referenced By |
|---|---|---|
| DATA_LITERACY_technical_reference.md | Doctrine/ADP-analog | SL 1, SL 2, SL 3, SL 4G–O, SL 5G–O (all recommended prereq read) |
| DATA_LITERACY_senior_leaders.md | Doctrine/senior leader brief | Standalone; referenced in README, QUICK_START |
| GLOSSARY_data_foundry.md | Reference | Standalone; referenced in README, cheatsheet |
| NAMING_AND_GOVERNANCE_STANDARDS.md | Standards | EX-20, EX-30 (required read); SL 4M Appendix A, SL 4L Appendix B |
| USAREUR_AF_DATA_ANALYTICS_STRATEGY.md | Strategy/CG-signed | All TMs (strategic context); COMMANDERS_GUIDE, POLICY_LETTER, DATA_LITERACY_senior_leaders |
| UNIFIED_DATA_TRANSITION_STRATEGY.md | Strategy/CUI | SL 3, SL 4G–O, SL 5G–O (ODT quarterly product cycle; resource allocation) |
| cheatsheet.md | Quick Reference | Standalone; links to all TMs A–O, 50G–O, base tracks |

---

## SECTION 6 — TRAINING MANAGEMENT

| File | Covers | Key Cross-Refs |
|---|---|---|
| MTP_MSS.md | Master training plan; course overview table + SL 1 throughput risk item (Sec 7-4, G-3 action required) | All TMs + T3-F/T3-I; corrected durations: SL 2=5d, SL 3=5d, SL 4A–F=3d, SL 4G/H/M/L=5d, SL 4J/K=4d, T3-F=0.5d, T3-I=5d |
| POI_MSS.md | Program of instruction; tier/prereq structure | All TMs; prereq tree A–O; SL 4J/K now correctly in SL 3 branch |
| CAD_MSS.md | Course admin; access reqs by track | All TMs; SL 4J/K prereq = SL 3 required |
| TEO_MSS.md | T&EO evaluation standards; TM20-03 Row 5 now [CRITICAL] (date arithmetic) | SL 1 through SL 4M critical performance measures |
| ANNUAL_TRAINING_SCHEDULE.md | Schedule by track (2026) | All TMs; SL 4J/K prereq = SL 3 |
| ANNUAL_TRAINING_CALENDAR_FY27.html | Interactive FY27 training calendar (HTML) | Visual companion to ANNUAL_TRAINING_SCHEDULE |
| FACULTY_DEVELOPMENT_PLAN.md | Instructor quals by track | All TMs; WFF (A–F) vs. Specialist (G–O) instructor profiles |
| COMPLETION_CERTIFICATE.md | Certificate templates | Generic; course title filled at completion |
| CURRICULUM_MAINTENANCE_SOP.md | Maintenance SOP + Platform Monitoring procedure (Sec 2A) + Semi-Annual Deep Review (Sec 5A) | Scope: SL 1 through SL 4O |
| ENROLLMENT_SOP.md | Enrollment process + prereq verification + Training Records Requirements section (minimum data standard, retention, query process) | All TMs; SL 4J/K prereq = SL 3 required |
| COMMANDERS_GUIDE_MSS_TRAINING.md | Commander/XO reference: who trains on what, timelines, CDR responsibilities, throughput risk | → ENROLLMENT_SOP; → MTP; all TM levels |
| lesson_plans/TM10/TM10_LESSON_PLANS.md | Lesson plan: SL 1 | TM-10 Ch 1–8, DATA_LITERACY_technical_reference Ch 1 |
| lesson_plans/TM20_LESSON_PLAN_OUTLINES.md | Lesson plan: SL 2 | TM-20 Ch 2–5, NAMING_AND_GOVERNANCE_STANDARDS |
| lesson_plans/TM30_LESSON_PLAN_OUTLINES.md | Lesson plan: SL 3 | TM-30 Ch 2–9, Standards Ch 3–4 |
| lesson_plans/TM40_SPECIALIST_LESSON_PLAN_OUTLINES.md | Lesson plans: SL 4G–O | All specialist tracks G–O; WFF A–F managed separately with WFF proponents |
| POLICY_LETTER.md | Training policy letter | All tracks; command direction and training requirements by echelon |
| AAR_TEMPLATE.md | After Action Review template | All training events; standard format for post-course review |
| lesson_plans/LP_TEMPLATE.md | Standard lesson plan template | Blank template; TLO, Key Delivery Notes, Student Activity, Assessment blocks |
| ENTERPRISE_V10_PLAN.md | ODT Enterprise v10 release plan (2026-03-12) | 5 bounded contexts (Architecture/Pipelines/Products/Foundry/QA); M1–M5 milestone gates; agent assignments; feature checklist |
| ENTERPRISE_IMPLEMENTATION_PLAN.md | Enterprise implementation plan — CUI | 6-phase/20-week hardening plan; 46 acceptance functions; 12 CG architectural constraints; current-state assessment |
| FOUNDRY_BOOTCAMP_SOP.md | Foundry Bootcamp SOP: quarterly event enrollment, execution, evaluation | → FBC_GUIDE, → ENROLLMENT_SOP, → ANNUAL_TRAINING_SCHEDULE |
| INSTRUCTOR_OVERVIEW.md | Instructor onboarding guide: program structure, materials, execution | All TMs + T3-F/T3-I; → MTP, → POI, → CAD, → TEO, → ENROLLMENT_SOP, → lesson plans |
| DEMO_BRIEF_CG.md | CG decision brief: request TASKORD authorization for MSS MTT | → TASKORD, → WHITE_PAPER; ↔ all training management docs |
| TASKORD_MSS_TRAINING_CELL.md | Draft TASKORD: MSS MTT activation (theater-wide) | → MTP, → POI, → ENROLLMENT_SOP, → ANNUAL_TRAINING_SCHEDULE |
| WHITE_PAPER_MSS_TRAINING.md | Strategic white paper: case for MSS training across USAREUR-AF | → all TMs (program overview); ↔ DEMO_BRIEF_CG |
| AR_350_1_ALIGNMENT_MAP.md | AR 350-1 alignment map: full MSS ecosystem mapped to 11 regulatory areas; SAT artifact coverage; gap analysis with mitigations | → MTP, → POI, → CAD, → TEO, → FACULTY_DEVELOPMENT_PLAN, → ENROLLMENT_SOP, → CURRICULUM_MAINTENANCE_SOP; ↔ all 15 analytics apps |
| MSS_TRAINING_BRIEF.pptx | CG briefing slide deck (PowerPoint) | ↔ DEMO_BRIEF_CG (companion visual) |
| lesson_plans/TM40_WFF_LESSON_PLAN_OUTLINES.md | Lesson plans: SL 4A–F WFF tracks | All WFF tracks A–F |
| lesson_plans/TM50_ADVANCED_LESSON_PLAN_OUTLINES.md | Lesson plans: SL 5G–O advanced tracks | All advanced tracks G–O |
| lesson_plans/T3F_LESSON_PLAN_OUTLINES.md | Lesson plans: T3-F MSC Force Multiplier | T3-F course; SL 1 lesson plans (teach-back source) |
| lesson_plans/T3I_LESSON_PLAN_OUTLINES.md | Lesson plans: T3-I Instructor Certification | T3-I course; all SL 1/SL 2/SL 3 materials (microteaching source) |
| UNIT_DATA_TRAINER_SOP.md | UDT governance: authorities, limitations, reporting, recertification, commander nomination template | → T3-F (certification requirement); → C2DAO (reporting chain); → ENROLLMENT_SOP |

---

## SECTION 7 — HTML APPLICATIONS

| File | Contents | TM Dependencies |
|---|---|---|
| mss_info_app/index.html | Training hub — 6 WFF cards (A–F, SL 3 chip) + 8 specialist cards (G–O, SL 3 chip) + 8 SL 5 cards | All SL 4A–O PDFs, all CGs, all exams, all syllabi |
| mss_info_app/training_schedule.html | Schedule view | Training schedule data |
| task_index.html | Task index by specialist track | SL 4G(17), SL 4H(1), SL 4M(21), SL 4J(18), SL 4K(6), SL 4L(30) = 93 total; SL 4N/O pending integration |
| mss_info_app/index_sharepoint.html | SharePoint-hosted variant of MSS Training Hub | Same as index.html; adapted for SharePoint embedding |
| mss_info_app/PILOT_AGENT_PROMPT.md | System prompt for MSS pilot AI agent | ↔ mss_info_app/index.html (serves the training hub) |
| mss_info_app/DEPLOYMENT.md | Deployment guide: Cloudflare Pages + SharePoint + Foundry | → index.html, → index_sharepoint.html |
| mss_info_app/Maven_Rollout_Plan.pptx | Rollout plan slide deck (PPTX) | ↔ DEMO_BRIEF_CG (CG rollout strategy) |
| source_material/course_portal/ | CDA slide library — 29 decks, 3 tracks, 397 PNG slides | ⇢ all TM levels (see Section 8); source of all [PPT] refs |

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
| architecture_primer | Architecture Primer | 12 | ⇢ before SL 1 | Orientation to the data stack before first MSS login |
| 2026_Data_Stack_Deep_Dive | 2026 Data Stack — Five Layers | 10 | ⇢ SL 2 | Explains the five-layer stack SL 2 teaches users to build in |
| L2_Ingestion_Integration_Deep_Dive | L2 Ingestion & Integration | 10 | ⇢ SL 2 | Pipeline concepts behind Pipeline Builder tasks |
| The_Semantic_Layer_Instructions | The Semantic Layer | 11 | ⇢ SL 2 / SL 3 | Why the Ontology layer exists; frames SL 2 Ontology Manager tasks |
| What_Is_An_Ontology | What Is an Ontology? | 12 | ⇢ SL 2 | Conceptual base for Object Types; gap in SL 2 |
| Data_Modeling_Foundations | Data Modeling Foundations | 11 | ⇢ SL 2 / SL 3 | Normalization → strategy; underpins SL 3 architecture decisions |
| Data_Platforms_Cloud_Deep_Dive | Data Platforms & Cloud | 10 | ⇢ SL 2 / SL 3 | Where Foundry/MSS sits in the broader platform landscape |
| L5_Activation_Interface_Deep_Dive | L5 Activation & Interface | 10 | ⇢ SL 2 | Workshop conceptual grounding; explains why Workshop widgets exist |
| Dont_Filter_This_Isnt_Excel | Don't Filter — This Isn't Excel | 11 | ⇢ SL 2 | Critical mindset shift; Foundry vs spreadsheet mental model |
| decision_advantage_deep_dive | Decision Advantage | 10 | ⇢ SL 4A–F (all WFF) | The "why" behind WFF data integration; all six WFF tracks |
| AI_ML_Beyond_The_Hype | AI/ML — Beyond the Hype | 11 | ⇢ SL 4H / SL 4M | Conceptual framing required before AIP Logic and model training |

### Track: Data 101 (7 decks)

| Deck ID | Title | Slides | TM Alignment | Notes |
|---|---|---|---|---|
| The_Four_Layers | The Four Layers | 13 | ⇢ SL 2 / SL 3 | Data layer model; directly maps to stack diagram in SL 2 |
| Data_Modeling_Fundamentals_Level1 | Data Modeling Fundamentals — Level 1 | 15 | ⇢ SL 2 | Object type design patterns; prereq conceptual content for SL 2 tasks |
| ObjectType_WhatToWatchFor | Object Types — What to Watch For | 13 | ⇢ SL 2 / SL 3 | Anti-patterns; fills gap neither SL 2 nor SL 3 covers |
| Links_and_Relationships | Links & Relationships | 11 | ⇢ SL 2 | Link type conceptual base; maps to "Create Link Types" in SL 2 |
| Controlled_Vocabularies | Controlled Vocabularies | 11 | ⇢ SL 3 / SL 4K | Vocab standardization; SL 4K owns this operationally |
| Identity_Who_Owns_The_Key | Identity — Who Owns the Key? | 11 | ⇢ SL 3 / SL 4K / SL 4L | Primary keys, master data, identity governance |
| Dont_Filter_This_Isnt_Excel | (see Intro To Data above) | — | ⇢ SL 2 | Listed in both tracks in source manifest |

### Track: Data 201 (10 decks)

| Deck ID | Title | Slides | TM Alignment | Notes |
|---|---|---|---|---|
| Semantic_Modelling_Course_Intro | Semantic Modelling — Course Intro | 10 | ⇢ SL 3 / SL 4L | Entry to formal semantic modeling; SL 3 architects and SWEs |
| Deck_01_Architecture_First_Principles | 01 — Architecture First Principles | 10 | ⇢ SL 3 / SL 4L | Core architecture decision principles; above SL 3 procedure level |
| Deck_02_Scope_Engineering | 02 — Scope Engineering | 10 | ⇢ SL 3 / SL 4J | How to scope a data problem; SL 3 governance + PM track |
| Deck_03_RDF_OWL_Foundations | 03 — RDF & OWL Foundations | 10 | ⇢ SL 4K / SL 4L | RDF triples, OWL classes; knowledge graph and semantic layer work |
| Deck_04_Object_Type_Varieties | 04 — Object Type Varieties | 10 | ⇢ SL 3 / SL 4L | Advanced object type design patterns |
| Deck_05_Identity_Governance | 05 — Identity & Governance | 10 | ⇢ SL 3 / SL 4K | Formal governance patterns for shared ontology |
| Deck_06_Relationship_Modeling | 06 — Relationship Modeling | 10 | ⇢ SL 3 / SL 4L | Advanced link type and relationship design |
| Deck_07_Temporal_Bitemporal | 07 — Temporal & Bitemporal | 10 | ⇢ SL 4G / SL 4M / SL 4L | Time-aware data modeling; ORSA time series + SWE pipeline patterns |
| Data_Modeling_Fundamentals_Level2 | Data Modeling Fundamentals — Level 2 | 13 | ⇢ SL 4G / SL 4M / SL 4L | Advanced modeling; senior technical specialist level |
| Deck_12_Capstone_Foundry | 12 — Capstone: Foundry | 10 | ⇢ SL 4G / SL 4H / SL 4L | Bridges CDA theory to Foundry/MSS practice; single highest-value deck for specialists |

---

## SECTION 9 — EXTERNAL REFERENCE LIBRARY: PALANTIR DEVELOPERS

**Source:** Palantir Developers YouTube channel (@PalantirDevelopers) — official Palantir product deep-dive video library.
**Integration method:** (1) Inline NOTE callouts embedded in TM files at the relevant chapter/task locations. (2) SELF_STUDY_ADDENDUM.md files in each TM directory for organized self-study guidance. No class time added — all content is reference or optional self-study only.
**[SS]** = Self-Study Addendum file type (used in this section only)

### Self-Study Addenda — File Registry

| File | Type | Supports | Groups / Videos |
|---|---|---|---|
| tm/TM_30_advanced_builder/SELF_STUDY_ADDENDUM.md | [SS] | SL 3 | 5 groups: Workshop Scenarios, Pipeline Monitoring, Quiver Advanced, Contour Advanced, Platform Security |
| tm/TM_40A_intelligence/SELF_STUDY_ADDENDUM.md | [SS] | SL 4A | 5 groups: Ontology & Data Foundations, Quiver Analysis, Geospatial/Mapping, AI-Assisted Intelligence & RAG, Platform Security & Access (19 videos) |
| tm/TM_40B_fires/SELF_STUDY_ADDENDUM.md | [SS] | SL 4B | 5 groups: Ontology & Data Foundations, Quiver Analysis & Targeting, Contour Dashboards, Platform Architecture, AI & Automation (14 videos) |
| tm/TM_40C_movement_maneuver/SELF_STUDY_ADDENDUM.md | [SS] | SL 4C | 5 groups: Ontology & Data Foundations, Quiver Analysis, Contour Dashboards, Platform Architecture & Real-Time, AI & Automation (14 videos) |
| tm/TM_40D_sustainment/SELF_STUDY_ADDENDUM.md | [SS] | SL 4D | 5 groups: Ontology & Data Foundations, Quiver Analysis & LOGSTAT, Contour Dashboards, Supply Chain Patterns, Platform Architecture (15 videos) |
| tm/TM_40E_protection/SELF_STUDY_ADDENDUM.md | [SS] | SL 4E | 5 groups: Ontology & Data Foundations, Quiver Analysis & Risk, Contour Dashboards, Platform Architecture & Security, AI-Assisted Operations (15 videos) |
| tm/TM_40F_mission_command/SELF_STUDY_ADDENDUM.md | [SS] | SL 4F | 5 groups: Ontology & Data Foundations, Quiver Staff Analysis, Contour Dashboards, Platform Architecture & COP Design, AI & Decision Support (16 videos) |
| tm/TM_40G_orsa/SELF_STUDY_ADDENDUM.md | [SS] | SL 4G | 4 groups: Quiver analytics, Contour analytics, Platform Architecture, AI/Advanced |
| tm/TM_40H_ai_engineer/SELF_STUDY_ADDENDUM.md | [SS] | SL 4H | 9 groups: RAG, Evals, MCP, Observability, Safety, Agent Studio, AIP Logic, Ontology, Platform |
| tm/TM_40M_ml_engineer/SELF_STUDY_ADDENDUM.md | [SS] | SL 4M | 7 groups: Spark, PySpark testing, Iceberg, Compute Modules, Pipeline Monitoring, Model Registry, Feature Engineering |
| tm/TM_40J_program_manager/SELF_STUDY_ADDENDUM.md | [SS] | SL 4J | 4 groups: Delivery & Scaling, Project Tracking, Case Studies, Leadership |
| tm/TM_40K_knowledge_manager/SELF_STUDY_ADDENDUM.md | [SS] | SL 4K | 5 groups: RAG & Retrieval, Knowledge Architecture, Semantic Search, AIP-Assisted KM, Platform Admin |
| tm/TM_40L_software_engineer/SELF_STUDY_ADDENDUM.md | [SS] | SL 4L | 8 groups: OSDK 2.0, Functions, Code Repos, Cipher, MCP, Edge Ontology, Spark, Platform SDK (~45 videos) |
| tm/TM_40N_ux_designer/SELF_STUDY_ADDENDUM.md | [SS] | SL 4N | 5 groups: Workshop/application surfaces, Ontology/data model, platform capabilities, accessibility/security, case studies |
| tm/TM_40O_platform_engineer/SELF_STUDY_ADDENDUM.md | [SS] | SL 4O | 5 groups: CI/CD pipeline ops, security/compliance, pipeline monitoring, platform architecture, case studies |
| tm/TM_50G_orsa_advanced/SELF_STUDY_ADDENDUM.md | [SS] | SL 5G | SL 4G groups + 7 SL 5G-specific additions (Bayesian, persistent ORSA, data layer) |
| tm/TM_50H_ai_engineer_advanced/SELF_STUDY_ADDENDUM.md | [SS] | SL 5H | SL 4H groups + 8 SL 5H-specific additions (multi-agent, observability, enterprise) |
| tm/TM_50M_ml_engineer_advanced/SELF_STUDY_ADDENDUM.md | [SS] | SL 5M | 8 groups, 29 videos (Iceberg advanced, xAI model tuning, Lightweight Transforms, Scaling AI) |
| tm/TM_50J_program_manager_advanced/SELF_STUDY_ADDENDUM.md | [SS] | SL 5J | SL 4J groups + enterprise autonomy, process orchestration, enterprise automation |
| tm/TM_50K_knowledge_manager_advanced/SELF_STUDY_ADDENDUM.md | [SS] | SL 5K | SL 4K groups + Advanced Ontology, Enterprise KM, multimodal data plane |
| tm/TM_50L_software_engineer_advanced/SELF_STUDY_ADDENDUM.md | [SS] | SL 5L | SL 4L reference + 5 SL 5L additions (Code-based AI, interoperability, Gallatin observability, Edge Embedded, Developer Experience) |
| tm/TM_50N_ux_designer_advanced/SELF_STUDY_ADDENDUM.md | [SS] | SL 5N | SL 4N reference + 5 SL 5N additions (design systems, DDIL/edge, AI interfaces, governance, strategic context) |
| tm/TM_50O_platform_engineer_advanced/SELF_STUDY_ADDENDUM.md | [SS] | SL 5O | SL 4O reference + 5 SL 5O additions (fleet mgmt, observability/reliability, RMF automation, DevEx, strategic leadership) |

### Inline NOTE Callouts — Summary by Track

| Track | NOTE Count | Primary Chapters |
|---|---|---|
| SL 3 | 4 | Ch 2 (Workshop Scenarios), Ch 3 (Pipeline Monitoring), Ch 5 (Quiver), Ch 7 (Security) |
| SL 4G | 6 | Ch 8 (Quiver/Contour analytics) |
| SL 4H | 12 | Ch 2, 5, 6, 7, 8, 9 (RAG, Evals, MCP, Observability, Safety) |
| SL 4M | 10 | Spark, PySpark testing, Iceberg, Compute Modules, Pipeline Monitoring |
| SL 4J | 6 | Phase 5/6 lifecycle, project tracking tools, delivery planning |
| SL 4K | 9 | Knowledge architecture, AIP/RAG, search/discovery |
| SL 4L | 30 | All chapters (OSDK 2.0, Functions, Code Repos, Cipher, MCP, Edge Ontology, Spark, Platform SDK) |
| SL 5G | 3 | Ch 4 Bayesian, Ch 8 persistent ORSA, data layer |
| SL 5H | 5 | Ch 2 multi-agent, Ch 6 observability, Ch 8 enterprise |
| SL 5M | 4 | Iceberg, xAI model tuning, Lightweight Transforms, Scaling AI |
| SL 5J | 3 | Enterprise autonomy, process orchestration, enterprise automation |
| SL 5K | 3 | Advanced Ontology, Enterprise KM, multimodal data plane |
| SL 5L | 5 | Code-based AI dev, interoperability, Gallatin observability, Edge Embedded, Developer Experience |
| **Total** | **~100** | Across SL 3 through SL 5M |

---

## CHANGE LOG — ISSUES FOUND & FIXED (12 March 2026 Audit)

| # | File | Line | Issue | Fix Applied |
|---|---|---|---|---|
| 1 | TM_40G_ORSA.md | 81 | "see SL 3 and SL 4G/40B" — SL 4B is WFF Fires, not pipeline dev | Changed to "see SL 3" |
| 2 | SYLLABUS_TM40J.md | 9 | SL 3 listed as "recommended but not required" — contradicts TM source | Changed to "SL 1/20/30 all required" |
| 3 | SYLLABUS_TM40K.md | 9 | SL 3 listed as "recommended" — contradicts TM source | Changed to "SL 1/20/30 all required" |
| 4 | POI_MSS.md | 38, 51–52 | SL 4J/K listed outside SL 3 branch; labeled SL 3 as exception | Fixed prereq tree; SL 4J/K now under SL 3 branch |
| 5 | CAD_MSS.md | 71–72, 75 | SL 4J/K prereq listed as "SL 3 recommended but not required" | Updated to "SL 3 required"; advisory note updated |
| 6 | ENROLLMENT_SOP.md | 63–64 | SL 4J/K prereq listed as SL 1/20 only | Updated to include SL 3 required |
| 7 | MTP_MSS.md | 58–66 | Multiple duration errors: SL 2=2d (should be 5), SL 3=3d (should be 5), SL 4G/H/M/L=4d (should be 5), SL 4J/K prereq=SL 2 (should be SL 3) | All durations and prereqs corrected |
| 8 | ANNUAL_TRAINING_SCHEDULE.md | 120, 133, 188 | SL 4J/K prereq listed as SL 2; prereq chain table omitted SL 3 | Updated all three locations |
| 9 | (PDF) 42 stale PDFs | — | Old specialist naming scheme (e.g., A=ORSA instead of G=ORSA; stale 50-series A–F existed) | Deleted all 42 stale PDFs |
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

*Expected audit result: PASS — 0 issues*

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
| OPEN-1 | TM_40A–F [TM], CONCEPTS_GUIDE_TM40A–F [CG], SYLLABUS_TM40A–F [SYL], mss_info_app, mss_widget, DEPENDENCY_MAP | WFF tracks prereq inconsistency — some files stated SL 2 only, others SL 3. | **RESOLVED 2026-03-13:** Design decision — all WFF tracks (SL 4A–F) now require SL 3 (same prereq chain as Specialist tracks, SL 1 + SL 2 + SL 3). All governance docs and app files updated. TM/CG content files require separate update pass to align. |

---

## CHANGE LOG — RALF BRANCH MIGRATION (14 March 2026)

**Scope:** 25 files migrated from `orsuh/repos` `ralf` branch (12 commits ahead of main, unmerged). Content classified as SL 4/5 specialist level (architecture doctrine, engineering reference).

| # | Files Added | Destination | Level |
|---|---|---|---|
| 22 | doctrine/CG_GUIDANCE.md | Senior leader doctrine | SL 1/20 |
| 23 | doctrine/cda_doctrine/CDA_OVERVIEW.md | CDA user taxonomy + enterprise index | SL 3 bridge |
| 24 | doctrine/cda_doctrine/agents/CDA_AGENTS_OVERVIEW.md | Agents index doc | SL 4H/M/K/L |
| 25 | doctrine/cda_doctrine/agents/CDA_AGENTS_CORE_PRINCIPLES.md | 12 bedrock principles, 14 anti-patterns, decision framework | SL 4H/M/K/L |
| 26 | doctrine/cda_doctrine/agents/CDA_AGENTS_ONTOLOGY_ENGINEER.md | Specializes Principles 3/7/8/9/10/11; RDF/OWL2/SHACL/SPARQL | SL 4H/K/L |
| 27 | doctrine/cda_doctrine/agents/CDA_AGENTS_ENTITY_RESOLUTION.md | 9-stage ER pipeline; threshold bands; data product architecture | SL 4H/M/L |
| 28 | doctrine/cda_doctrine/agents/CDA_AGENTS_INGESTION_INTEGRATION.md | Five-Stage Ingestion Pattern; Dagster DAG; VAULTIS-A | SL 4H/M/L |
| 29 | doctrine/ONTOLOGY_DESIGN_PRINCIPLES.md | DDD, DRY, Open/Closed, PECS, Composition; Foundry-specific rules | SL 4H/K/L |
| 30 | doctrine/gdap/GDAP_OVERVIEW.md | LlamaIndex retrieval stack, API endpoints | SL 4H/M/K/L |
| 31 | doctrine/gdap/GDAP_VISION.md | Full 10-domain vision, 20 pipeline steps, DVEE | SL 4H/M/K/L |
| 32 | doctrine/gdap/GDAP_PERSISTENCE_STRATEGY.md | DuckDB vs LlamaIndex boundary; versioning/rebuild policy | SL 4H/M/L |
| 33 | doctrine/gdap/GDAP_ACCEPTANCE_TESTS.md | P0/P1/P2 release gates across 9 sections | SL 4H/M/L |
| 34 | doctrine/gdap/GDAP_ADR_0001_LLAMAINDEX.md | ADR-0001: DuckDB = truth, LlamaIndex = serving | SL 4H/M/L |
| 35 | doctrine/mim/MIM_OVERVIEW.md | Toolchain: parsers, Foundry backend, package structure | SL 4H/M/K/L |
| 36 | doctrine/mim/MIM_STANDARD.md | MIM semantic model, namespaces, roles, code types, Semantic IDs | SL 4H/M/K/L |
| 37 | doctrine/mim/MIM_STATE.md | Project snapshot 2026-02-28; maturity by area; gaps/priorities | SL 4H/M/L |
| 38 | doctrine/mim/MIM_ACADEMICS.md | Dr. Gerz / NATO; MIM↔Foundry structural alignment analysis | SL 4H/M/K/L |
| 39 | doctrine/mim/MIM_DECISION_RECORDS.md | ADR: repo-level and per-package ADR structure | SL 4H/L |
| 40 | doctrine/mim/MIM_FUTURE_CLASSES.md | Planned adapters, backends, mim-studio, mim-sdk | SL 4H/M/L |
| 41 | doctrine/mim/MIM_ONTOLOGY_DOCS.md | OSDK Maker Package full TypeScript API reference | SL 4H/L |
| 42 | quick_reference/cda_reference/DOCTRINE_ELEMENT_FOUNDRY_MAPPING.md | Property mapping, bi-temporal fields, TS interface, OSDK queries, enums | SL 4H/M/L |
| 43 | training_management/ENTERPRISE_V10_PLAN.md | ODT v10 release plan; 5 bounded contexts; M1–M5 gates | SL 4H/M/L |
| 44 | training_management/ENTERPRISE_IMPLEMENTATION_PLAN.md | 6-phase/20-wk hardening plan — **CUI** | SL 4H/M/L |

**Note on ENTERPRISE_IMPLEMENTATION_PLAN.md:** Source document bears `CUI` classification. Handle per local policy before committing to shared repository.

---

## CHANGE LOG — PALANTIR DEVELOPERS ENRICHMENT (14 March 2026)

**Scope:** Full Palantir Developers YouTube channel (@PalantirDevelopers) enumerated via yt-dlp (~130 videos). All videos mapped to TM tracks (SL 3 through SL 5M). SL 3 scope limited to UI-only tools (no code). SL 4/5 specialist tracks received code-level content appropriate to their domains.

**Method:** (1) Inline NOTE callouts embedded at relevant chapter/task anchor points. (2) SELF_STUDY_ADDENDUM.md overflow files for content that did not fit inline. No class time or schedule changes made.

| # | Files Added / Modified | Change | Level |
|---|---|---|---|
| 45 | TM_30_ADVANCED_BUILDER.md | 4 inline NOTEs added (Workshop Scenarios, Pipeline Monitoring, Quiver advanced, Security) | SL 3 |
| 46 | SYLLABUS_TM30.md | Supplemental self-study note added after Day 1 evening reading block | SL 3 |
| 47 | tm/TM_30_advanced_builder/SELF_STUDY_ADDENDUM.md | NEW — 5 groups covering SL 3-scoped UI tool depth content (~15 videos) | SL 3 |
| 48 | TM_40G_ORSA.md | 6 inline NOTEs added (Quiver/Contour analytics) | SL 4G |
| 49 | tm/TM_40G_orsa/SELF_STUDY_ADDENDUM.md | NEW — 4 groups, 16 videos | SL 4G |
| 50 | TM_40H_AI_ENGINEER.md | 12 inline NOTEs added (RAG, Evals, MCP, Observability, Safety) | SL 4H |
| 51 | tm/TM_40H_ai_engineer/SELF_STUDY_ADDENDUM.md | NEW — 9 groups, 43 videos | SL 4H |
| 52 | TM_40M_ML_ENGINEER.md | 10 inline NOTEs added (Spark, PySpark, Iceberg, Compute Modules) | SL 4M |
| 53 | tm/TM_40M_ml_engineer/SELF_STUDY_ADDENDUM.md | NEW — 7 groups, 25 videos | SL 4M |
| 54 | TM_40J_PROGRAM_MANAGER.md | 6 inline NOTEs added (lifecycle phases, project tracking, delivery) | SL 4J |
| 55 | tm/TM_40J_program_manager/SELF_STUDY_ADDENDUM.md | NEW — 4 groups | SL 4J |
| 56 | TM_40K_KNOWLEDGE_MANAGER.md | 9 inline NOTEs added (knowledge architecture, AIP/RAG, search) | SL 4K |
| 57 | tm/TM_40K_knowledge_manager/SELF_STUDY_ADDENDUM.md | NEW — 5 groups | SL 4K |
| 58 | TM_40L_SOFTWARE_ENGINEER.md | 30 inline NOTEs added across all chapters (OSDK, Functions, Cipher, MCP, Edge, Spark) | SL 4L |
| 59 | tm/TM_40L_software_engineer/SELF_STUDY_ADDENDUM.md | NEW — 8 groups, ~45 videos | SL 4L |
| 60 | TM_50G_ORSA_ADVANCED.md | 3 inline NOTEs added | SL 5G |
| 61 | tm/TM_50G_orsa_advanced/SELF_STUDY_ADDENDUM.md | NEW — extends SL 4G + 7 SL 5G additions | SL 5G |
| 62 | TM_50H_AI_ENGINEER_ADVANCED.md | 5 inline NOTEs added | SL 5H |
| 63 | tm/TM_50H_ai_engineer_advanced/SELF_STUDY_ADDENDUM.md | NEW — extends SL 4H + 8 SL 5H additions | SL 5H |
| 64 | TM_50M_ML_ENGINEER_ADVANCED.md | 4 inline NOTEs added | SL 5M |
| 65 | tm/TM_50M_ml_engineer_advanced/SELF_STUDY_ADDENDUM.md | NEW — 8 groups, 29 videos | SL 5M |
| 66 | TM_50J_PROGRAM_MANAGER_ADVANCED.md | 3 inline NOTEs added | SL 5J |
| 67 | tm/TM_50J_program_manager_advanced/SELF_STUDY_ADDENDUM.md | NEW — extends SL 4J + enterprise content | SL 5J |
| 68 | TM_50K_KNOWLEDGE_MANAGER_ADVANCED.md | 3 inline NOTEs added | SL 5K |
| 69 | tm/TM_50K_knowledge_manager_advanced/SELF_STUDY_ADDENDUM.md | NEW — extends SL 4K + advanced | SL 5K |
| 70 | TM_50L_SOFTWARE_ENGINEER_ADVANCED.md | 5 inline NOTEs added | SL 5L |
| 71 | tm/TM_50L_software_engineer_advanced/SELF_STUDY_ADDENDUM.md | NEW — SL 5L additions + reference to SL 4L addendum | SL 5L |
| 72 | scripts/build_pdfs.py | Added PUB_TYPES + MD_TARGETS for: SL 5 syllabi (6), EX_50 exercises (6), SELF_STUDY_ADDENDUM files (13) | Build |
| 73 | DEPENDENCY_MAP.md | Section 7 added for Palantir Developers external reference library | All |

---

## CHANGE LOG — RALF BRANCH FULL INVENTORY (14 March 2026)

**Scope:** Full file inventory of ralf-branch-migrated content revealed additional files beyond the initial 25 tracked in entries #22–44. These files were already present in Section 0B but not captured in the changelog.

| # | Files Added | Destination | Level |
|---|---|---|---|
| 74 | doctrine/CDA_CONSTRAINTS_AND_DIRECTIVES.md | 12 CDA operational constraints; governs all specialist CDA work | SL 4G–O |
| 75 | doctrine/cda_doctrine/CDA_DOCTRINE_OVERVIEW.md | Doctrine-driven development framework; DDD applied to CDA | SL 4G–O |
| 76 | doctrine/cda_doctrine/CDA_DOCTRINE_AGENT.md | Doctrine Agent reference — AI-assisted doctrine authoring patterns | SL 4H, SL 4L |
| 77 | doctrine/cda_doctrine/CDA_AVT25_ASSESSMENT.md | AVT-25 assessment framework for CDA capability evaluation | SL 4G, SL 4H |
| 78 | doctrine/cda_doctrine/CDA_IDENTITY_VS_CLASSIFICATION.md | Identity vs. classification disambiguation; semantic precision | SL 3, SL 4K, SL 4L |
| 79 | doctrine/enterprise_architecture/EA_00_REFERENCE_CARD.md | EA one-pager; frameworks overview (TOGAF, NAF, DODAF, Zachman) | SL 3, SL 4K, SL 4L |
| 80 | doctrine/enterprise_architecture/EA_01_FOUNDATION.md | EA foundational concepts; what EA is and is not | SL 3 |
| 81 | doctrine/enterprise_architecture/EA_02_SCHOOLS_OF_THOUGHT.md | TOGAF, Zachman, FEA, NAF, DODAF compared | SL 3, SL 4K |
| 82 | doctrine/enterprise_architecture/EA_03_ARTIFACTS_AND_VIEWS.md | NAF/DODAF views; architecture artifacts; diagram types | SL 4K, SL 4L |
| 83 | doctrine/enterprise_architecture/EA_04_GOVERNANCE.md | Architecture governance; review boards; decision authority | SL 4K |
| 84 | doctrine/enterprise_architecture/EA_05_MILITARY_APPLICATION.md | EA applied to military C2 / joint operations context | SL 3, SL 4G–O |
| 85 | doctrine/cda_doctrine/canon/CANON_ADP_CROSSWALK.md | ADP 3-0 / 6-0 crosswalk to Foundry data model | SL 4G–O |
| 86 | doctrine/cda_doctrine/canon/CANON_CONDITIONS_INDICATORS_THRESHOLDS.md | Conditions, indicators, and threshold patterns for data products | SL 4G, SL 4H |
| 87 | doctrine/cda_doctrine/canon/CANON_ENGAGEMENT.md | Engagement authority and engagement event data model | SL 4G, SL 4H |
| 88 | doctrine/cda_doctrine/canon/CANON_INFORMATION.md | Information taxonomy and schema for common operational data | SL 4H, SL 4K |
| 89 | quick_reference/cda_reference/EA_VS_DA.md | Enterprise Architecture vs. Data Architecture decision tool | SL 3, SL 4K |
| 90 | quick_reference/cda_reference/ENTERPRISE_DATA_COMPASS.md | Data strategy decision compass; orientation for PM/KM roles | SL 4J, SL 4K |
| 91 | quick_reference/cda_reference/LESSONS_LEARNED.md | CDA implementation lessons learned registry | All tracks |
| 92 | quick_reference/cda_reference/PLAN_FOR_SUCCESS.md | CDA project planning checklist and success criteria | SL 4J, SL 3 |

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

**Scope:** Team-of-teams content accuracy and consistency audit across all curriculum files, React widget, HTML app, Python scripts, and PPTX presentation files. Primary goal: verify prereq chain enforcement (SL 3 hard prereq for ALL SL 4 tracks A–F and G–O) and content alignment between all delivery surfaces.

**Audit findings and resolutions:**

| # | File | Issue | Resolution |
|---|---|---|---|
| 95 | README.md (root) | WFF prereq stated SL 2 in 4 places (table, tree, footnote lines) | Fixed → SL 3 in all 4 locations |
| 96 | maven_training/training_management/POLICY_LETTER.md | Official governance table: WFF tracks listed SL 2 as prereq | Fixed → SL 3 |
| 97 | maven_training/mss_widget/src/panels/Home.tsx | WFF specialist row "Start Here" cell showed SL 1 → SL 2 only; SL 3 missing | Fixed → SL 1 → SL 2 → SL 3 chain |
| 98 | maven_training/quick_reference/cheatsheet.md | WFF track description said "after SL 2"; prereq chain diagram wrong | Fixed → SL 3 throughout; diagram rebuilt with WFF + Specialist both branching from SL 3 |
| 99 | maven_training/mss_widget/src/panels/TM40.tsx | SL 4J card: builder-focused language ("PM Dashboards, Reporting Pipelines") mismatched actual TM content (Agile PM theory, ML lifecycle, stakeholder mgmt); BLUF embedded full WFF track list creating confusion | Fixed: SL 4J card rewritten to PM theory; BLUF simplified with cross-reference to HOME tab |
| 100 | maven_training/mss_info_app/index.html | SL 4J card matched stale builder-focused TM40.tsx (dual-maintenance surface) | Fixed: SL 4J card updated to match TM40.tsx (PM theory content) |
| 101 | .gitignore | node_modules/ missing; 65MB React deps at risk of commit | Added node_modules/ |
| 102 | maven_training/pdf/MSS_Project_Overview.pptx | Slide 1: old "6 Specialist Tracks: 40A ORSA · 40B AI · 40C MLE..." scheme | Rebuilt via python-pptx: "12 Tracks (WFF + Specialist) / WFF (A–F): Intel · Fires · M&M / Specialist (G–O): ORSA · AI Eng · MLE · PM · KM · SWE · UX · PE" |
| 103 | maven_training/pdf/MSS_Training_Progression.pptx | Specialist column: original 6-slot design insufficient; partial fix left WFF A–D mixed with specialist H–I, sub-headers misplaced | Full column rebuild via python-pptx: deleted all 19 old content shapes; clean layout with "▸ WFF TRACKS (A–F)" (A–F) / "▸ SPECIALIST (G–O)" (G–O) sub-headers; SL 5 G–O note added at bottom |
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
| 115 | 13 TM files (SL 1, SL 4A–O) | No professional reading lists | Added Professional Reading List appendices with 65+ curated journal articles |
| 116 | 7 files (CG docs, SL 4F/G/H/M, CDA) | No EUCOM theater context | Added Theater and Strategic Context sections (BRAVO Hackathon, Thunderforge, Posture Statement, 49B career path) |
| 117 | SL 4A, SL 4C, SL 4K, SL 4L, SL 5K, SL 5L, GLOSSARY | NATO MIM standards gap — no STANAG 5643/5527, ADatP-36/5644, or CWIX references | Added 4 NATO standards to doctrine refs, CWIX context notes, glossary MIM disambiguation |
| 118 | doctrine/, DEPENDENCY_MAP, index.html, Doctrine.tsx | USAREUR-AF Data and Analytics Strategy (CG-signed, May 2025) not in corpus | Created USAREUR_AF_DATA_ANALYTICS_STRATEGY.md; added to Sec 0B (Command Strategy), Sec 5, External Refs, doctrine panel (HTML + React), publications index |
| 119 | doctrine/, DEPENDENCY_MAP, index.html, Doctrine.tsx | Unified Data Transition Strategy quarterly product cycle (CUI) not in corpus | Created UNIFIED_DATA_TRANSITION_STRATEGY.md; added to Sec 0B, Sec 5, External Refs, doctrine panel (HTML + React), publications index |

---

## CHANGE LOG — STRUCTURAL ADDITIONS (18 March 2026)

**Scope:** New course tracks (T3-I, T3-F, SL 4N/O, SL 5N/O), ASF role alignment, and WFF self-study addenda.

| # | Files Added / Modified | Change | Level |
|---|---|---|---|
| 120 | tm/T3_F_msc_force_multiplier/ (TM, CG), syllabi/SYLLABUS_T3F.md, exercises/EX_T3F_force_multiplier/ (EXERCISE, ENV_SETUP), exams/EXAM_T3F_PRE/POST.md, lesson_plans/T3F_LESSON_PLAN_OUTLINES.md, training_management/UNIT_DATA_TRAINER_SOP.md, PDFs (8) | T3-F MSC Force Multiplier (Unit Data Trainer Certification). Half-day course, prereq SL 2. Authorizes SL 1 delivery, SL 1 exam proctoring. | T3-F |
| 121 | tm/T3_I_instructor_certification/ (TM, CG), syllabi/SYLLABUS_T3I.md, exercises/EX_T3I_instructor_certification/ (EXERCISE, ENV_SETUP), exams/EXAM_T3I_PRE/POST.md, lesson_plans/T3I_LESSON_PLAN_OUTLINES.md, PDFs (8) | NEW — T3-I Instructor Certification (C2DAO Instructor Pipeline). Phase 1: 5-day classroom, prereq SL 3 + OIC selection. Phase 2: supervised practicum. | T3-I |
| 122 | tm/TM_40N_ux_designer/ (TM, CG, SS), syllabi/SYLLABUS_TM40N.md, exercises/EX_40N_ux_designer/ (EXERCISE, ENV_SETUP), exams/EXAM_TM40N_PRE/POST.md, PDFs (~8) | NEW — SL 4N UI/UX Designer specialist track. ASF Designer role alignment. Covers SCD, user research, IA, visual design, prototyping, usability testing, Section 508/WCAG 2.1 AA. | SL 4N |
| 123 | tm/TM_40O_platform_engineer/ (TM, CG, SS), syllabi/SYLLABUS_TM40O.md, exercises/EX_40O_platform_engineer/ (EXERCISE, ENV_SETUP), exams/EXAM_TM40O_PRE/POST.md, PDFs (~8) | NEW — SL 4O Platform Engineer specialist track. ASF Platform Engineer role alignment. Covers K8s, IaC/GitOps, Iron Bank, CI/CD, DDIL ops, RMF/ATO. | SL 4O |
| 124 | tm/TM_50N_ux_designer_advanced/ (TM, CG, SS), tm/TM_50O_platform_engineer_advanced/ (TM, CG, SS), syllabi/SYLLABUS_TM50N.md, SYLLABUS_TM50O.md, exercises/EX_50N_ux_designer/, EX_50O_platform_engineer/, exams/EXAM_TM50N/O_PRE/POST.md, PDFs (~12) | NEW — SL 5N (Advanced UI/UX) and SL 5O (Advanced Platform Eng) tracks. Prereqs: SL 4N, SL 4O respectively. | SL 5N/O |
| 125 | tm/TM_40A–F (6 SELF_STUDY_ADDENDUM.md files) | NEW — WFF self-study addenda for all six WFF tracks (Intelligence, Fires, Movement & Maneuver, Sustainment, Protection, Mission Command). 5 groups each, 14–19 videos per track. Palantir Developers source. | SL 4A–F |

---

## CHANGE LOG — ATIS REGISTRATION PACKET (16 March 2026)

**Scope:** Build TR 350-70 compliant ATIS course registration packet for USAREUR-AF G3/7 submission (Phase 1) with forward compatibility for T2COM institutional registration (Phase 2).

| # | File | Issue / Action | Resolution |
|---|---|---|---|
| 118 | scripts/build_atis_packet.py | New script: extracts all 21 course records from POI/CAD/MTP/TEO data into structured ATIS format | Outputs JSON + TR 350-70 formatted markdown; covers all fields: hours by method, blocks, T&EO crosswalk, equipment, prereqs, GO/NO-GO criteria |
| 119 | maven_training/atis/atis_courses.json | New file: machine-readable structured course data (63KB) | 21 courses, 664 total program hours, full prereq tree |
| 120 | maven_training/atis/ATIS_COURSE_PACKET.md | New file: TR 350-70 formatted ATIS registration packet (1,477 lines) | Per-course records with all required ATIS fields; T2COM readiness notes embedded |
| 121 | maven_training/pdf/ATIS_COURSE_PACKET.pdf | New PDF: Army doctrine-styled ATIS packet | Generated via build_pdfs.py pipeline; cover page, DRAFT header/footer, page numbers |
| 122 | scripts/build_pdfs.py | ATIS packet not in PDF build pipeline | Added PUB_TYPES entry (ATIS_COURSE) + MD_TARGETS entry for atis/ATIS_COURSE_PACKET.md |
| 123 | DEPENDENCY_MAP.md | ATIS files not tracked | Added atis/ entries to Section 6; this changelog |

---

## CHANGE LOG — DDOF PLAYBOOK v2.2 RECONCILIATION (17 March 2026)

**Scope:** Reconcile corpus with authoritative DDOF Playbook v2.2 (December 2025, T2COM C2DAO / HQDA CIO/G-6 / SAIS-ADD, CUI // FEDCON). Key changes: VAULTIS-A dimension names corrected, DDOF acronym expansion corrected, phase timelines updated, version references updated from v2.0 to v2.2.

**VAULTIS-A authoritative definition (v2.2, p.9 glossary p.16):**
Visible, Accessible, Understandable, Linked, Trusted, Interoperable, Secure, Auditable.
Supersession: VAUTI (5, AR 25-1 2019) → VAULTIS (7, DoD Data Strategy 2020) → VAULTIS-A (8, DDOF Playbook v2.2 2025).

**Phase timelines (v2.2 Quick Reference Guide, p.14):**
Phase 1: 3-5 days | Phase 2: 5-10 days | Phase 3: 7-12 days | Phase 4: 15-25 days | Phase 5: 7-12 days | Total IOC: 30-60 days.

**New v2.2 content not yet integrated into TM series (noted for future integration):**
- Genesis Mission Alignment (3 directives: Decision Dominance, Bureaucracy Elimination, Accountability)
- Secretary of the Army Priorities mapping (Warfighter First, Speed Over Perfection, Cut the Fat, Trust the Troops)
- ADC Registration Requirements for Phase 6
- Configuration Management Friction Matrix
- Data Product Retirement criteria (90 days no access → FDM review, 180 days → retirement, quality <70% → remediate/retire)
- Roles table (Decision Maker O-6+, C2DAO O-4/O-5, FDM O-3/O-4, etc.)
- Platform-agnostic note: "works with Vantage, ADVANA, or any approved system"

| # | File | Issue / Action | Resolution |
|---|---|---|---|
| 124 | source_material/cda_docs/ddof/reference/ddof.ts | VAULTIS-A property names wrong (Valid/Accurate/Unique/Timely/Integrated) | Renamed to Visible/Accessible/Understandable/Trusted/Interoperable per v2.2 |
| 125 | doctrine/cda_doctrine/agents/CDA_AGENTS_CORE_PRINCIPLES.md | Principle 12 VAULTIS-A dimensions wrong | Updated 8 dimensions to match v2.2 authoritative definition |
| 126 | doctrine/cda_doctrine/agents/CDA_AGENTS_INGESTION_INTEGRATION.md | VAULTIS-A table dimensions wrong | Updated 8 dimensions to match v2.2 |
| 127 | quick_reference/cda_reference/ENTERPRISE_DATA_COMPASS.md | VAULTIS-A dimensions wrong; phase timelines wrong; DDOF v2.0 ref | Fixed all three; v2.0 → v2.2 with correct authority line |
| 128 | quick_reference/cda_reference/PLAN_FOR_SUCCESS.md | DDOF v2.0 references | Updated to v2.2 (2 occurrences) |
| 129 | source_material/cda_apps/enterprise-data-compass/index.html | VAULTIS-A dimensions wrong; phase timelines wrong; DDOF v2.0 | Fixed all three |
| 130 | source_material/cda_apps/plan-for-success/data/plan.json | DDOF v2.0 reference | Updated to v2.2 |
| 131 | source_material/cda_apps/plan-for-success/data/radar.json | DDOF v2.0 reference | Updated to v2.2 |
| 132 | doctrine/GLOSSARY_data_foundry.md | No VAULTIS-A entry; VAUTI entries did not note supersession | Added VAULTIS-A definition; updated VAUTI/VAUTI Framework entries with supersession chain; added VAULTIS/VAULTIS-A abbreviations |
| 133 | tm/TM_30_advanced_builder/TM_30_ADVANCED_BUILDER.md | DDOF = "Doctrine-Driven Ontology Framework" (wrong) | Corrected to "Defense Data Orchestration Framework" |
| 134 | source_material/README.md | DDOF = "Data-Driven Operational Framework" (wrong); v2.0 refs | Corrected acronym; updated to v2.2 with metadata (Dec 2025, T2COM C2DAO, CUI // FEDCON) |
| 135 | tm/_archive_pre_review/TM_30_ADVANCED_BUILDER.md | DDOF = "Doctrine-Driven Ontology Framework" (wrong) | Corrected to "Defense Data Orchestration Framework" |

## CHANGE LOG — DOCTRINE SOURCE RECONCILIATION (17 March 2026, Session 2)

**Scope:** Comprehensive audit of corpus against authoritative source documents (43 ADPs/FMs/strategic docs downloaded and read). VAUTI→VAULTIS-A corrections across all active TMs, doctrine docs, and training management. DDOF lifecycle content added. Army doctrine (ADP 6-0, ADP 3-13) cognitive hierarchy integrated. WFF doctrine references validated and gaps filled.

| # | File | Issue | Resolution |
|---|------|-------|------------|
| 136 | tm/TM_10_MAVEN_USER.md | VAUTI refs (3); no VAULTIS-A consumer section; no cognitive hierarchy | Updated governance chain to VAULTIS/VAULTIS-A; added Section 5-5 VAULTIS-A consumer literacy; added Section 1-2a cognitive hierarchy (ADP 6-0/3-13) |
| 137 | doctrine/DATA_LITERACY_technical_reference.md | Section 4-8 used VAUTI (5 dims); no VAULTIS-A; no DDOF Playbook ref; no cognitive hierarchy | Rewrote Section 4-8 as VAULTIS-A (8 dims, full targets); added DDOF Playbook to strategic refs; added Section 1-2 cognitive hierarchy; updated glossary entries |
| 138 | doctrine/DATA_LITERACY_senior_leaders.md | Section 1-4 used VAUTI (5 dims); glossary/refs stale | Rewrote Section 1-4 as VAULTIS-A (8 dims); updated glossary and references with supersession chain; added DDOF Playbook ref |
| 139 | tm/TM_20_BUILDER.md | VAUTI refs (2) | Updated AR 25-1 and DoD Data Strategy refs with VAULTIS-A supersession |
| 140 | tm/TM_30_ADVANCED_BUILDER.md | VAUTI refs (2); no DDOF lifecycle section | Updated refs; added Section 1-10 DDOF Lifecycle (6 phases, timelines, Genesis Mission, quality gates, retirement triggers) |
| 141 | tm/TM_40K_KNOWLEDGE_MANAGER.md | VAUTI ref (1) | Updated to VAULTIS-A with DDOF Playbook citation |
| 142 | tm/TM_40L_SOFTWARE_ENGINEER.md | VAUTI refs (2) | Updated governance ref and glossary to VAULTIS-A |
| 143 | tm/TM_40M_ML_ENGINEER.md | VAUTI ref (1) | Updated to VAULTIS-A with DDOF Playbook citation |
| 144 | tm/TM_40A–F (all 6 WFF TMs) | No DDOF/VAULTIS-A references anywhere | Added DDOF Playbook v2.2 row to Strategic Guidance tables in all 6 files |
| 145 | tm/TM_40A_INTELLIGENCE.md | FM 3-84 (IPOE) not cited | Added FM 3-84 to Appendix H doctrine cross-reference |
| 146 | tm/TM_40E_PROTECTION.md | FM 3-37 not cited as standalone | Added FM 3-37 alongside ADP 3-37 in Table 1-4 |
| 147 | tm/TM_50J_PROGRAM_MANAGER_ADVANCED.md | DDOF retirement triggers not cited | Added DDOF Playbook v2.2 automatic retirement trigger table (90/180-day, <70% quality) |
| 148 | training_management/COMMANDERS_GUIDE_MSS_TRAINING.md | Missing DoD Data Strategy, DDOF, UDRA, Army Data Plan details | Added 4 strategic guidance rows: DoD Data Strategy (VAULTIS), DDOF Playbook v2.2, UDRA v1.1, expanded Army Data Plan with SO7/SE05 workforce mandate |
| 149 | DEPENDENCY_MAP.md | DoD Data Strategy row said "VAUTI Framework" | Updated to "VAULTIS Framework (7 dimensions)"; added DDOF Playbook v2.2 row |
| 150 | tm/CONCEPTS_GUIDE_TM20_BUILDER.md | VAUTI ref (1) | Updated to VAULTIS/VAULTIS-A |

---

## SECTION 9 — ANALYTICS & TOOLING APPS (`apps/`)

**Source:** `apps/` (repo root)
**Stack:** Python, SQLAlchemy (SQLite/WAL), FastAPI (API), Streamlit (dashboards)
**Portal:** `apps/portal.py` — unified landing page connecting all 15 apps (port 8500)

> All `.db` files are gitignored. Seed data is generated via `python3 -m apps.<name>.seed`.
> Each app follows a standard structure: `db.py`, `models.py`, `api.py`, `dashboard.py`, `seed.py`.

### Training Analytics (core 3)

| App | API Port | Dashboard Port | Purpose | TM Dependencies |
|-----|----------|---------------|---------|-----------------|
| readiness_tracker | 8001 | 8501 | Unit/Soldier completion across prereq chain; RAG heatmap; bottleneck analysis; training funnel | → All TMs (prereq chain is authoritative); ↔ enrollment_manager, ↔ instructor_manager |
| exam_analytics | 8002 | 8502 | Pre/post exam gain scores; item discrimination; question difficulty | → All exams (SL 1 through SL 5); ↔ readiness_tracker |
| aar_aggregator | 8003 | 8503 | AAR trend analysis by WFF; frequency × severity matrix; recurring issues | → All WFF tracks (SL 4A–F); ↔ lessons_learned |

### Training Operations

| App | API Port | Dashboard Port | Purpose | TM Dependencies |
|-----|----------|---------------|---------|-----------------|
| progress_tracker | 8004 | 8504 | Individual training timelines; stalled Soldier detection; overdue milestones | → readiness_tracker (prereq chain); ↔ enrollment_manager |
| mtt_scheduler | 8005 | 8505 | MTT event scheduling across AOR; instructor/venue allocation; conflict detection | ↔ instructor_manager, ↔ enrollment_manager |
| data_quality | 8010 | 8510 | Pipeline health monitoring; quality metrics (5 types); anomaly alerting | ↔ all pipeline-producing apps |

### Content & Quality Tools

| App | API Port | Dashboard Port | Purpose | TM Dependencies |
|-----|----------|---------------|---------|-----------------|
| xref_validator | 8006 | 8506 | Cross-reference validation; broken link detection; prereq chain audit | → all maven_training/ files |
| glossary_search | 8007 | 8507 | Full-text search across glossary terms and doctrine definitions | → GLOSSARY_data_foundry.md, all doctrine/ |
| offline_packager | — | 8508 | Bundle TMs/exercises/PDFs for DDIL environments | → all maven_training/ content |
| sharepoint_sync | — | 8509 | Sync state tracking between local content and Cloudflare/SharePoint | → all maven_training/ files |

### Faculty & Enrollment

| App | API Port | Dashboard Port | Purpose | TM Dependencies |
|-----|----------|---------------|---------|-----------------|
| instructor_manager | 8011 | 8511 | Instructor certification tracking; course coverage matrix; teaching workload; expiration alerts | → FACULTY_DEVELOPMENT_PLAN, → INSTRUCTOR_OVERVIEW; ↔ mtt_scheduler, ↔ enrollment_manager |
| enrollment_manager | 8012 | 8512 | Class enrollment; seat allocation; waitlists; roster management | → ENROLLMENT_SOP; ↔ readiness_tracker, ↔ mtt_scheduler, ↔ instructor_manager |

### Knowledge Management

| App | API Port | Dashboard Port | Purpose | TM Dependencies |
|-----|----------|---------------|---------|-----------------|
| curriculum_tracker | 8013 | 8513 | Document version tracking; review cycles; content freshness; SHA-256 change detection | → CURRICULUM_MAINTENANCE_SOP; → all maven_training/ .md files |
| lessons_learned | 8014 | 8514 | Structured lessons-learned pipeline; TTP/WFF/echelon tagging taxonomy; action tracking | → SL 4K (taxonomy design); ↔ aar_aggregator |

### Executive

| App | API Port | Dashboard Port | Purpose | TM Dependencies |
|-----|----------|---------------|---------|-----------------|
| training_metrics | 8015 | 8515 | CG/DCG/G6 aggregation dashboard; risk register; BLUF briefing export; snapshot comparison | → all 14 other apps (read-only aggregation); → SL 5J (senior leader reporting) |

### App Dependency Graph

```
training_metrics (CG Dashboard)
  ├── readiness_tracker ←─── enrollment_manager
  ├── exam_analytics           ↑
  ├── aar_aggregator ←──── lessons_learned
  ├── progress_tracker
  ├── mtt_scheduler ←───── instructor_manager
  ├── data_quality
  ├── instructor_manager
  ├── enrollment_manager
  ├── curriculum_tracker
  └── lessons_learned
```

---

## CHANGE LOG — ANALYTICS APPS EXPANSION (17 March 2026)

**Scope:** Added 5 new analytics apps to close operational gaps identified in gap analysis against FACULTY_DEVELOPMENT_PLAN, ENROLLMENT_SOP, CURRICULUM_MAINTENANCE_SOP, SL 4K (taxonomy), and SL 5J (senior leader reporting). Portal updated from v3.0 (10 apps) to v4.0 (15 apps).

| # | File(s) | Issue / Action | Resolution |
|---|---------|----------------|------------|
| 151 | apps/instructor_manager/ (7 files) | No tool to track instructor certifications, course coverage gaps, or teaching workload | New app: 3 tables (Instructor, Certification, TeachingHistory), coverage matrix, expiration tracking, workload analysis |
| 152 | apps/enrollment_manager/ (7 files) | No tool to manage class seats, waitlists, or rosters — MTT Scheduler handles events but not enrollment | New app: 3 tables (TrainingClass, Enrollment, WaitlistEntry), auto-waitlist, priority promotion, fill-rate tracking |
| 153 | apps/curriculum_tracker/ (7 files) | No tool to track document freshness, review cycles, or detect content changes | New app: 3 tables (Document, ReviewCycle, ChangeLog), SHA-256 scanning of maven_training/, stale content detection |
| 154 | apps/lessons_learned/ (7 files) | AAR Aggregator limited to WFF-level rollup; SL 4K taxonomy (TTP/echelon/doctrine ref) not implemented | New app: 4 tables (Lesson, LessonTag, ActionItem, LessonComment), full tagging taxonomy, co-occurrence matrix, action tracking |
| 155 | apps/training_metrics/ (7 files) | No executive dashboard for CG/DCG/G6; no snapshot comparison or risk aggregation | New app: aggregates from all 14 apps, auto-generated risk register, BLUF briefing export, weekly snapshots |
| 156 | apps/portal.py | Portal only covered 10 apps | Updated: 3 new sections (Faculty & Enrollment, Knowledge Management, Executive), second KPI row, v3.0 → v4.0 |
| 157 | DEPENDENCY_MAP.md | No apps/ section | Added Section 9 — Analytics & Tooling Apps (15 apps, port map, dependency graph) |

---

## CHANGE LOG — DOCTRINE INTEGRATION — PHASE 2 (17 March 2026, Session 3)

The following changes integrate extracted doctrine from ADPs, FMs, DDOF Playbook v2.2, Army Data Plan, and UDRA v1.1 into the training corpus. Research agents extracted content from 6 ADPs (3-0, 6-0, 3-13, 2-0, 3-37, 7-0), 14 FMs (2-0, 3-0, 3-09, 3-12, 3-34, 3-57, 3-60, 3-84, 3-96, 5-0, 6-0, 6-22, 1-02.1, 3-94), DDOF Playbook v2.2, Army Data Plan (2022), and UDRA v1.1.

| # | File | Change | Source |
|---|------|--------|--------|
| 151 | TM_20_BUILDER.md | VAUTI → VAULTIS-A supersession (2 locations) | DoD Data Strategy / DDOF Playbook v2.2 |
| 152 | TM_30_ADVANCED_BUILDER.md | VAUTI → VAULTIS-A supersession (2 locations) | DoD Data Strategy / DDOF Playbook v2.2 |
| 153 | TM_40K_KNOWLEDGE_MANAGER.md | VAUTI → VAULTIS-A (8 dims, 85% gate) | DDOF Playbook v2.2 |
| 154 | TM_40L_SOFTWARE_ENGINEER.md | VAUTI → VAULTIS-A (strategic guidance + glossary) | DDOF Playbook v2.2 |
| 155 | TM_40M_ML_ENGINEER.md | VAUTI → VAULTIS-A | DDOF Playbook v2.2 |
| 156 | CONCEPTS_GUIDE_TM20_BUILDER.md | "DoD VAUTI" → "DoD VAULTIS / VAULTIS-A" | DoD Data Strategy |
| 157 | DATA_LITERACY_senior_leaders.md | "Trustworthy" → "Trusted" (line 72) | DDOF Playbook v2.2 |
| 158 | TM_40A–F (6 files) | DDOF Playbook v2.2 / VAULTIS-A added to Ch 1 strategic guidance + end-of-file refs | DDOF Playbook v2.2 |
| 159 | TM_30_ADVANCED_BUILDER.md | Sections 1-10a–d: DDOF roles, SMART criteria, fail-closed, ADC registration | DDOF Playbook v2.2 |
| 160 | DATA_LITERACY_technical_reference.md | Section 4-9: UDRA 7 quality dimensions | UDRA v1.1, Table 8 |
| 161 | DATA_LITERACY_technical_reference.md | Chapter 11: Data mesh concepts (products, domains, computational governance, 6 services) | UDRA v1.1 |
| 162 | DATA_LITERACY_technical_reference.md | Chapter 12: Army Data Plan SO1–SO11, SE01–SE05 | Army Data Plan (2022) |
| 163 | DATA_LITERACY_technical_reference.md | 6 new glossary entries | UDRA v1.1 / Army Data Plan |
| 164 | TM_40A_INTELLIGENCE.md | FM 2-0 data literacy NOTE, intel process→pipeline table, 7 quality standards | FM 2-0 (Oct 2023) |
| 165 | TM_40B_FIRES.md | D3A lifecycle, FIVE-O taxonomy, TTLODAC schema, CARVER scoring | FM 3-60 / FM 3-09 |
| 166 | TM_40C_MOVEMENT_MANEUVER.md | PMESII-PT/METT-TC(I), force ratios, geospatial data, recon as data collection | ADP 3-0 / FM 5-0 / FM 3-98 |
| 167 | TM_40C Appendix K | Restructured from narrative list to doctrine mapping table (16 pubs) | Multiple FMs |
| 168 | TM_40D_SUSTAINMENT.md | 8 sustainment principles, 10 classes of supply framework, running estimate NOTE | ADP 4-0 / FM 4-0 / FM 6-0 |
| 169 | TM_40E_PROTECTION.md | CVP analysis, OPSEC 5-step mapping, GMAD NOTE, doctrine table updated | ADP 3-37 / FM 3-13.3 / FM 3-34 |
| 170 | TM_40F_MISSION_COMMAND.md | FM 6-0 IM 6-task mapping, info relevance→VAULTIS-A crosswalk, App D enhanced | FM 6-0 / FM 5-0 |
| 171 | TM_10_MAVEN_USER.md | GMAD framework, Operations Process, METT-TC(I) NOTE | FM 3-34 / ADP 5-0 / ADP 3-0 |
| 172 | COMMANDERS_GUIDE_MSS_TRAINING.md | ADP 7-0: 9 training principles, T/P/U mapping, 3 training domains | ADP 7-0 (Apr 2024) |
| 173 | scripts/build_pdfs.py | Title page centering (flex spacer after topbar) | N/A |
| 174 | TM_40G_ORSA.md | Assessment framework (MOE/MOP/indicators), CARVER scoring model, force ratio/combat power | FM 5-0 / FM 3-60 |
| 175 | TM_40H_AI_ENGINEER.md | ADP 3-13 AI/ML doctrine NOTE, PED→pipeline mapping, UDRA VAULTIS-A governance NOTE | ADP 3-13 / FM 2-0 / UDRA v1.1 |
| 176 | TM_40J_PROGRAM_MANAGER.md | DDOF friction matrix, roles/PM oversight table, portfolio health metrics, 4 glossary entries | DDOF Playbook v2.2 |
| 177 | TM_40K_KNOWLEDGE_MANAGER.md | FM 6-0 KM 5-step process, 3 tasks, 6 tool categories; FM 6-22 domains; FM 3-57 CKI NOTE | FM 6-0 / FM 6-22 / FM 3-57 |
| 178 | TM_30_ADVANCED_BUILDER.md | Section 1-10e: DDIL operations (Denied/Degraded/Intermittent/Limited) | Army Data Plan SO6/SO10 / UDRA v1.1 / ADP 6-0 |
| 179 | DEPENDENCY_MAP.md | Changelog entries #151–179 for Session 3 doctrine integration | N/A |
| 180 | TM_40M_ML_ENGINEER.md | Sections 1-8/9-2a: DDOF Phases 4–5 ML lifecycle, VAULTIS-A model compliance, ADP 3-13 human-machine teaming WARNING | DDOF Playbook v2.2 / ADP 3-13 / UDRA v1.1 |
| 181 | TM_40L_SOFTWARE_ENGINEER.md | Section 1-5b: Army Data Plan SO 7 DevSecOps→DDOF phase mapping; Section 1-7: UDRA 6-service architecture; metadata fields WARNING | Army Data Plan / UDRA v1.1 |
| 182 | TM_50G_ORSA_ADVANCED.md | Section 5-9: multi-variable sensitivity analysis, Bayesian assessment updating, longitudinal trend analysis, OAWG NOTE | FM 5-0 / FM 3-60 |
| 183 | TM_50H_AI_ENGINEER_ADVANCED.md | Section 5-12: multi-source data fusion, adversarial ML defense, model drift monitoring, DDIL deployment NOTE | ADP 3-37 / FM 2-0 / Army Data Plan |
| 184 | TM_50J_PROGRAM_MANAGER_ADVANCED.md | Section 9-6: multi-product dependency mapping, cascading friction analysis, resource optimization, DDOF retirement NOTE | DDOF Playbook v2.2 |
| 185 | TM_50K_KNOWLEDGE_MANAGER_ADVANCED.md | Enterprise KM at theater scale, FM 6-0 five-step process cross-reference, federated ontology governance | FM 6-0 / UDRA v1.1 |
| 186 | TM_50L_SOFTWARE_ENGINEER_ADVANCED.md | Computational governance as code, DDIL-resilient pipeline design, zero trust architecture | Army Data Plan / UDRA v1.1 / DoD ZT RA |
| 187 | TM_50M_ML_ENGINEER_ADVANCED.md | Model governance at portfolio scale, federated ML for coalition, DDOF Phase 6 model versioning | DDOF Playbook v2.2 / UDRA v1.1 |
| 188 | CONCEPTS_GUIDE_TM50G–M (6 files) | NOTE callouts referencing new SL 4 doctrine content in each parent TM | N/A |
| 189 | CONCEPTS_GUIDE_TM40B_FIRES.md | NOTE referencing D3A, FIVE-O, TTLODAC, CARVER content in SL 4B | N/A |
| 190 | CONCEPTS_GUIDE_TM40C_MOVEMENT_MANEUVER.md | NOTE referencing PMESII-PT/METT-TC(I), force ratios, recon content in SL 4C | N/A |
| 191 | CONCEPTS_GUIDE_TM40D_SUSTAINMENT.md | NOTE referencing 8 principles, 10 supply classes, running estimate in SL 4D | N/A |
| 192 | CONCEPTS_GUIDE_TM40E_PROTECTION.md | NOTE referencing CVP, OPSEC 5-step, GMAD content in SL 4E | N/A |
| 193 | CONCEPTS_GUIDE_TM40F_MISSION_COMMAND.md | NOTE referencing FM 6-0 IM tasks, VAULTIS-A crosswalk, App D in SL 4F | N/A |
| 194 | TM40_SPECIALIST_LESSON_PLAN_OUTLINES.md | Doctrine content NOTEs for new CARVER, DDOF friction matrix material | FM 3-60 / DDOF Playbook v2.2 |
| 195 | TM50_ADVANCED_LESSON_PLAN_OUTLINES.md | Doctrine content NOTEs for Bayesian, adversarial ML, cascading friction material | Multiple sources |
| 196 | EXAM_TM30_POST.md | 6 new DDOF Playbook questions (Q16–Q21): VAULTIS-A dims, retirement triggers, phase order, SMART, fail-closed | DDOF Playbook v2.2 |
| 197 | EXAM_TM40M_POST.md | 5 new DDOF/VAULTIS-A/ML questions (Q16–Q20): MVP mandate, Linked dimension, Phase 4 gate, Auditable, ADP 3-13 | DDOF Playbook v2.2 / UDRA v1.1 / ADP 3-13 |
| 198 | TM40_WFF_LESSON_PLAN_OUTLINES.md | Doctrine content NOTEs for all 6 WFF tracks (A–F) Block 1 | Multiple ADPs/FMs |
| 199 | SELF_STUDY_ADDENDUM (SL 3) | Group 5: DDOF and Operational Design Patterns (Sections 1-10a–e) | DDOF Playbook v2.2 |
| 200 | SELF_STUDY_ADDENDUM (SL 4G/H/J/K) | New Doctrine References sections for 4 specialist self-study addenda | Multiple sources |
| 201 | SELF_STUDY_ADDENDUM (SL 5G/H/J/K) | New Doctrine References sections for 4 advanced self-study addenda | Multiple sources |
| 202 | TM_40H_AI_ENGINEER.md | Section 1-5a: Strategic Guidance subsection (ADP 3-13, DDOF, VAULTIS-A, UDRA, Army Data Plan, DoD Responsible AI) | Multiple strategic sources |
| 203 | CONCEPTS_GUIDE_TM40H_AI_ENGINEER.md | Updated NOTE to reference new Section 1-5a Strategic Guidance | N/A |
| 204 | EXAM_TM40A_POST.md | 2 doctrine MC questions: intel process→pipeline mapping (Q9), 7 quality standards (Q10) | FM 2-0 / SL 4A |
| 205 | EXAM_TM40B_POST.md | 2 doctrine MC questions: D3A lifecycle Deliver phase (Q9), CARVER Accessibility factor (Q10) | FM 3-60 / SL 4B |
| 206 | EXAM_TM40C_POST.md | 2 doctrine MC questions: METT-TC(I) Informational addition (Q9), 3:1 force ratio (Q10) | ADP 3-0 / FM 5-0 / SL 4C |
| 207 | EXAM_TM40D_POST.md | 2 doctrine MC questions: Anticipation principle→data (Q9), Class IX update freq (Q10) | ADP 4-0 / FM 4-0 / SL 4D |
| 208 | EXAM_TM40E_POST.md | 2 doctrine MC questions: CVP 3 factors (Q9), OPSEC 5-step sequence (Q10) | ADP 3-37 / FM 3-13.3 / SL 4E |
| 209 | EXAM_TM40F_POST.md | 2 doctrine MC questions: FM 6-0 IM 6 tasks (Q9), Timely→VAULTIS-A (Q10) | FM 6-0 / SL 4F |
| 210 | EXAM_TM40H_POST.md | 2 doctrine MC questions: ADP 3-13 human-machine teaming (Q16), PED Exploitation→AI/ML (Q17) | ADP 3-13 / FM 2-0 / SL 4H |
| 211 | EXAM_TM40K_POST.md | 2 doctrine MC questions: FM 6-0 KM 5-step Design (Q16), FM 3-57 CKI validation (Q17) | FM 6-0 / FM 3-57 / SL 4K |
| 212 | EXAM_TM40L_POST.md | 2 doctrine MC questions: SO 7 DevSecOps→DDOF 30-day MVP (Q16), UDRA security-critical metadata (Q17) | Army Data Plan / UDRA v1.1 / SL 4L |
| 213 | DEPENDENCY_MAP.md | Changelog entries #202–213 for Session 4 exam + strategic guidance gap closure | N/A |

---

## External Doctrinal References

> Publications prefixed TR/TP are published by TRADOC at adminpubs.tradoc.army.mil, not DA APD (armypubs.army.mil).

| Publication | Title | Referenced By |
|---|---|---|
| AR 350-1 | Army Training and Leader Development | All training management docs |
| AR 350-10 | Management of Army Individual Training Requirements and Resources | ATIS_COURSE_PACKET, ENROLLMENT_SOP |
| TR 350-70 | Army Learning Policy and Systems (TRADOC) | POI, CAD, CURRICULUM_MAINTENANCE_SOP, INSTRUCTOR_OVERVIEW |
| TP 350-70-14 | Training Development in Institutional Domain (TRADOC) | POI, CAD, CURRICULUM_MAINTENANCE_SOP |
| TP 350-70-7 | Army Educational Processes (TRADOC) | POI, INSTRUCTOR_OVERVIEW |
| TP 350-70-3 | Faculty and Staff Development Program (TRADOC) | INSTRUCTOR_OVERVIEW |
| DA PAM 25-40 | Army Publishing: Action Officers' Guide | Publication standards (all docs) |
| AR 25-50 | Preparing and Managing Correspondence | Army writing style (all docs) |
| AR 25-1 | Army Information Technology | SL 4K, SL 4L, POLICY_LETTER, data governance |
| DA PAM 25-1-1 | Army IT Implementation Instructions | SL 4K, SL 4L |
| AR 25-400-2 | Army Records Management Program | SL 4K |
| DA PAM 25-403 | Army Guide to Recordkeeping | SL 4K |
| ATP 6-01.1 | Techniques for Effective Knowledge Management | SL 4K, SL 5K |
| DA PAM 600-3 | Officer Professional Development | SL 4G (FA 49 ORSA) |
| AR 5-11 | Management of Army M&S | SL 4G, SL 5G |
| DA PAM 5-11 | VV&A of Army Models and Simulations | SL 4G, SL 5G |
| ATP 5-0.3 | Multi-Service TTP for Operation Assessment | SL 4G, SL 5G |
| AR 71-9 | Warfighting Capabilities Determination | SL 4G |
| Army DIR 2024-03 | Digital Engineering Policy | SL 4H, SL 4M, SL 4L, SL 5H, SL 5M, SL 5L |
| FM 3-12 | Cyberspace Operations and EW | SL 4E, SL 4H, SL 4M, SL 4L |
| DA PAM 25-2-5 | Software Assurance | SL 4H, SL 4M, SL 4L |
| FM 3-27 | Army Global Integrated Fires | SL 4B |
| ATP 3-01.81 | Counter-UAS Techniques | SL 4B |
| FM 3-81 | Maneuver Enhancement Brigade | SL 4C |
| ATP 4-33 | Maintenance Operations | SL 4D |
| FM 1-0 | Human Resources Support | SL 4D |
| AR 525-2 | The Army Protection Program | SL 4E |
| AR 530-1 | Operations Security | SL 4E |
| ATP 5-0.1 | Army Design Methodology | SL 4F |
| TC 6-0.2 | Training the C2 WFF for BN/BDE/BCT | SL 4F |
| ATP 2-33.4 | Intelligence Analysis | SL 4A |
| ATP 2-22.9-1 | PAI Research and OSINT | SL 4A |
| FM 3-60 | Army Targeting (Aug 2023) | SL 4A, SL 4B |
| FM 2-0 | Intelligence (Jul 2018) | SL 4A, SYLLABUS_TM40A |
| FM 3-0 | Operations (Mar 2025) | SL 4C, SYLLABUS_TM40C |
| FM 3-09 | Field Artillery Operations and Fire Support (Aug 2024) | SL 4B, SYLLABUS_TM40B |
| FM 3-90 | Offense and Defense (May 2023) | SL 4C (consolidates former FM 3-90-1 / FM 3-90-2) |
| FM 3-96 | Brigade Combat Team | SL 4C |
| FM 4-0 | Sustainment | SL 4D, SYLLABUS_TM40D |
| FM 5-0 | Army Planning and Orders Production (Nov 2024) | SL 4C, SL 4F |
| FM 6-0 | Commander and Staff Organization and Operations (May 2022) | SL 4F, SYLLABUS_TM40F |
| FM 7-0 | Training (Jun 2021) | SL 4K, SL 5K |
| ADP 3-0 | Operations | SL 4C, SYLLABUS_TM40C, CANON_ADP_CROSSWALK |
| ADP 3-19 | Fires | SL 4B |
| ADP 3-37 | Protection | SL 4E, SYLLABUS_TM40E |
| ADP 4-0 | Sustainment | SL 4D, SYLLABUS_TM40D |
| ADP 6-0 | Mission Command | SL 4F, SYLLABUS_TM40F, CANON_ADP_CROSSWALK |
| AR 25-30 | The Army Freedom of Information Act Program | SL 5H (consolidates former AR 25-55) |
| ATP 2-01 | Planning Requirements and Assessing Collection | SL 4A, SYLLABUS_TM40A |
| ATP 2-01.3 | Intelligence Preparation of the Battlefield | SL 4A |
| ATP 3-01.8 | Combined Arms for Air Defense | SL 4B |
| ATP 3-09.42 | Fire Support for the Brigade Combat Team | SL 4B, SYLLABUS_TM40B |
| ATP 3-09.50 | Battalion-Level Fire Support | SL 4B |
| ATP 3-37.2 | Antiterrorism | SL 4E, SYLLABUS_TM40E |
| ATP 3-52.2 | Airspace Control | SL 4B |
| ATP 3-90.90 | Army Tactical Standard Operating Procedures | SL 4C, SYLLABUS_TM40C |
| ATP 4-0.1 | Army Theater Distribution | SL 4D, SYLLABUS_TM40D |
| | | |
| **DoD/Joint Strategic Guidance** | | |
| DoD Data Strategy (2020) | Data as Strategic Asset / VAULTIS Framework (7 dimensions) | SL 1, SL 2, SL 3, doctrine/ |
| DDOF Playbook v2.2 (Dec 2025) | VAULTIS-A (8 dimensions), 6-phase lifecycle, 85% quality gate | All TMs, doctrine/, training_management/ |
| DoD Data, Analytics & AI Adoption Strategy (Nov 2023) | AI Hierarchy of Needs; adopt-buy-create | COMMANDERS_GUIDE, POLICY_LETTER, doctrine/ |
| DoD Responsible AI Strategy (Jun 2024) | Five AI Ethical Principles (RETRG) | SL 4H, SL 4M, SL 5H, SL 5M |
| DoD Zero Trust Reference Architecture v2.0 (Jul 2022) | 152 ZT activities across 7 pillars | SL 3 |
| DoD AI Cybersecurity Risk Mgmt Guide | Secure AI/ML development | SL 4H, SL 4M, SL 5H, SL 5M |
| DoDI 5000.87 | Software Acquisition Pathway | SL 4L, SL 5L, SL 4J, SL 5J |
| DoDD 3000.09 | Autonomy in Weapon Systems (Jan 2023) | SL 4A–F |
| DoD Software Modernization Strategy (Feb 2022) | DevSecOps frameworks | SL 4L, SL 5L |
| JADC2 Strategy Summary (Mar 2022) | Cross-domain data integration | SL 4A–F, SL 4G, SL 5G |
| JCOIE | Operating in the Information Environment | SL 4F |
| | | |
| **USAREUR-AF Theater Guidance** | | |
| USAREUR-AF Data and Analytics Strategy (May 2025) | CG-signed; 4 strategic outcomes, VAULTIS, Cognitive Hierarchy, decision dominance | All TMs, COMMANDERS_GUIDE, POLICY_LETTER, doctrine/ |
| Unified Data Transition Strategy (CUI) | Quarterly product cycle: Problem ID → Bootcamp → CADs → PSB → PoC → Exercise | SL 3, SL 4G–O, SL 5G–O, training_management/ |
| | | |
| **Army Strategic Guidance** | | |
| Army Data Plan (2022) | 11 strategic objectives for data transformation | SL 1, SL 2, SL 3, COMMANDERS_GUIDE, POLICY_LETTER |
| Army Cloud Plan (2022) | ZT, secure dev, data-driven decisions | SL 1, SL 2, SL 3 |
| UDRA v1.1 (Feb 2025) | Data mesh, decentralized governance | SL 3, SL 4G–O, SL 5G–O |
| Army CIO Data Stewardship Memo (Apr 2024) | Chain of responsibility for data governance | SL 1, SL 2, SL 3, SL 4K |
| Army Directive 2024-02 | Agile Software Dev & Acquisition (Dec 2024) | SL 4L, SL 5L, SL 4J, SL 5J |
| | | |
| **NATO** | | |
| NATO Data Strategy for the Alliance (Feb 2025) | Alliance-wide data governance mandate | SL 3, SL 4K, SL 5K, CDA_CONSTRAINTS |
| NATO Data Centric Reference Architecture v2 (2025) | Digital transformation reference arch | SL 3, CDA_CONSTRAINTS |
| NATO Data Quality Framework (Aug 2025) | Quality governance and metrics | SL 3 |
| NATO Digital Transformation Implementation Strategy (Oct 2024) | MDO interoperability | SL 4A–F |
| NATO Warfighting Capstone Concept (2021) | 6 Critical Enablers incl. Data | SL 4F |
| ADatP-34/NISP (NATO) | C3 Interoperability Standards | SL 4K, SL 5K, SL 4L, SL 5L |
| STANAG 5636/NCMS (NATO) | Core Metadata Specification | SL 4K, SL 5K |
| STANAG 5643 (proposed) | MIM Governance Standard | SL 4K, SL 5K, SL 4L, SL 5L |
| ADatP-5644 | Web Service Messaging Profile (WSMP) | SL 4L, SL 5L |
| ADatP-36 | Friendly Force Information (FFI) | SL 4A, SL 4C |
| STANAG 5527 | Friendly Force Tracking Systems Interoperability | SL 4A |

---

## MSS TRAINING ANALYTICS SUITE

> **Toggle:** Check the "Analytics Apps" checkbox in the HTML dependency map to overlay the app architecture on the corpus graph.
> **Standalone reference:** See `analytics_apps/DEPENDENCY_MAP.md` for full app catalog, ports, startup sequence, and cross-app dependency graph.

The analytics suite (15 Streamlit micro-apps + portal + shared theme) is integrated into the HTML dependency map as a toggleable layer on the far right. Apps are positioned by tier:

```
[HUB]         portal.py (8500)
[AGGREGATOR]  training_metrics (8015/8515)
[CORE]        readiness_tracker (8001/8501)
[DEPENDENT]   progress_tracker (8004/8504) → readiness_tracker
[STANDALONE]  exam_analytics, aar_aggregator, mtt_scheduler,
              xref_validator, glossary_search, offline_packager,
              sharepoint_sync, data_quality, instructor_manager,
              enrollment_manager, curriculum_tracker, lessons_learned
[SHARED]      theme.py
```

**Key relationships:**
- `readiness_tracker → progress_tracker` (hard runtime dependency)
- All apps `→ training_metrics` (soft aggregation)
- `readiness_tracker + exam_analytics + aar_aggregator → portal` (mandatory)
- `theme.py → ALL dashboards` (branding)

| | | |
| **Palantir External References** | | |
| Palantir Developer Community | community.palantir.com — 4,300+ topics across product Q&A, official updates, community feedback | All TMs; see source_material/palantir_community/README.md |
| Palantir Public Docs | docs.palantir.com/foundry — Ontology, Data Integration, AIP, Security | All TMs; see source_material/palantir_community/PALANTIR_DOCS_REFERENCE.md |
| Ontologize YouTube Channel | @Ontologize — 68 indexed videos, 24 hrs runtime; official Palantir training partner | All TMs; see source_material/ontologize_youtube/README.md |
| Palantir Defense OSDK | palantir.com/defense/sdk — WFF-aligned ontology, CJADC2 compatibility | SL 4L, SL 5L |
| Palantir Certifications | Builder Foundations Badge, Data Engineer Cert, App Developer Cert | SL 2, SL 3, SL 4L |

---

## SECTION 10 — EXTERNAL REFERENCE LIBRARY: ONTOLOGIZE & PALANTIR COMMUNITY

**Source:** Ontologize YouTube channel (@Ontologize) — official Palantir partner training videos.
**Source:** Palantir Developer Community (community.palantir.com) — product guidance, feature announcements, community Q&A.
**Integration method:** (1) README.md § Supporting Reference Material — indexed with TM cross-references. (2) All 13 SELF_STUDY_ADDENDUM.md files — companion resource cross-reference to Ontologize channel. (3) Inline NOTE callouts in TM files for specific Palantir best practices (PK rules, project architecture, object type naming, Defense OSDK, Compute Modules, DDIL inference, AI-FDE). (4) Exercise packages — Build with AIP official tutorial references.
**Verification:** Community content is user-generated and may reference deprecated features. "Inside the Product" posts (Palantir staff) carry higher authority. All community content should be cross-referenced against official docs and current MSS environment before incorporation.

### Ontologize Channel — Coverage Summary

| Topic Area | Videos | Primary TM Tracks |
|---|---|---|
| Getting Started / End-to-End | 5 | SL 1, SL 2 |
| Data Connection | 2 | SL 2 |
| Pipeline Builder | 7 | SL 2, SL 3 |
| Code Repositories | 3 | SL 3, SL 4L, SL 4M |
| Ontology Design | 3 | SL 2, SL 3, SL 4K |
| Analytics (Contour/Quiver) | 6 | SL 1, SL 2, SL 4G |
| Workshop Applications | 7 | SL 1, SL 2, SL 3 |
| Geospatial / Mapping | 3 | SL 1, SL 4A–F |
| AIP Logic | 11 | SL 4H, SL 5H |
| AIP Agents | 7 | SL 4H, SL 5H |
| RAG & Semantic Search | 6 | SL 4H, SL 4K, SL 5H |
| LLM & Document Processing | 4 | SL 4H, SL 4M |
| MLOps | 3 | SL 4M, SL 5M |
| Process Mining | 3 | SL 4D |
| OSDK | 2 | SL 4L, SL 5L |
| Data Protection | 1 | SL 4J, SL 4K |
| MCP | 2 | SL 4H, SL 4L |
| **Total** | **68** | **All tracks** |

### Palantir Community — High-Value Content Incorporated

| Resource | Source | Incorporated Into | Content |
|---|---|---|---|
| Ontology & Pipeline Design Principles | community/t/5481 (Palantir staff) | SL 2, SL 3, SL 4K, Naming Standards | PK rules, project architecture taxonomy, object type naming/maturity |
| Defense OSDK | community/t/3561 (Palantir staff) | SL 4L, SL 5L | WFF-aligned ontology, CJADC2, Defense SDK |
| Why We Built It: Compute Modules | community/t/3292 (Palantir staff) | SL 4L, SL 5L | Containerized compute architecture, decision guide |
| DDIL / Classified Inference | community/t/6146 (community) | SL 4H, SL 5H | Local inference for AIP Logic in DDIL/classified environments |
| AI-FDE Core Architecture | community/t/6199 (community) | SL 5H | Modes/Skills hierarchical agent framework |
| Build with AIP Examples (10) | community/t/5137 (Palantir staff) | EX_40H, EX_40J, EX_40K, EX_40L | Installable tutorial templates |
| Certification Alignment | community/t/1043, /2789, /548 | ENROLLMENT_SOP | TM→cert readiness mapping |

---

## CHANGE LOG — PALANTIR COMMUNITY & ONTOLOGIZE INTEGRATION (18 March 2026)

**Scope:** Palantir Developer Community (community.palantir.com) scraped and indexed. Ontologize YouTube channel (68 videos) cross-referenced. Content gap analysis against all TMs completed. 10 incorporation items executed across ~30 files. All 237 PDFs force-rebuilt.

**Sources:** Palantir Developer Community (4 categories, ~4,300 topics), Palantir Public Docs (docs.palantir.com/foundry), Ontologize YouTube (@Ontologize, 68 videos, 24 hrs).

| # | File(s) | Change | Source |
|---|---------|--------|--------|
| 203 | source_material/palantir_community/README.md | NEW — Full community index: 6 sections (official guidance, certifications, tags, extracted content, Build with AIP, AIP agents, DDIL) | community.palantir.com scrape |
| 204 | source_material/palantir_community/PALANTIR_DOCS_REFERENCE.md | NEW — Public docs index: 4 sections (Ontology, Data Integration, AIP, Security) with TM cross-refs | docs.palantir.com/foundry |
| 205 | source_material/ontologize_youtube/README.md | NEW — 68-video index with 17 topic areas and TM track cross-reference | youtube.com/@Ontologize |
| 206 | README.md | Added Palantir Public Docs subsection, Palantir Developer Community subsection, Ontologize entry to Supporting Reference Material | All three sources |
| 207 | TM_20_BUILDER.md + CONCEPTS_GUIDE_TM20 | PK Design Rules NOTE (strings only, uniqueness, no property inference) | community/t/5481 |
| 208 | TM_30_ADVANCED_BUILDER.md | PK rules + Project Architecture Taxonomy (5 types) + Object Type Naming/Maturity Standards | community/t/5481 |
| 209 | TM_40K_KNOWLEDGE_MANAGER.md + CONCEPTS_GUIDE_TM40K | Foundry Project Architecture Taxonomy NOTE (KM-specific) | community/t/5481 |
| 210 | TM_40L_SOFTWARE_ENGINEER.md | Defense OSDK NOTE + Compute Modules architecture NOTE | community/t/3561, community/t/3292 |
| 211 | TM_50L_SOFTWARE_ENGINEER_ADVANCED.md | Defense OSDK NOTE + Compute Modules architecture NOTE | community/t/3561, community/t/3292 |
| 212 | TM_40H_AI_ENGINEER.md | DDIL/Classified Inference NOTE | community/t/6146 |
| 213 | TM_50H_AI_ENGINEER_ADVANCED.md | DDIL/Classified Inference NOTE + AI-FDE Modes/Skills Architecture NOTE | community/t/6146, community/t/6199 |
| 214 | standards/NAMING_AND_GOVERNANCE_STANDARDS.md | Object Type Naming & Lifecycle Standards subsection (naming rules, maturity status, ownership) | community/t/5481 |
| 215 | training_management/ENROLLMENT_SOP.md | Palantir Certification Alignment section (3 cert mappings to TM completion) | community/t/1043, /2789, /548 |
| 216 | 13 × SELF_STUDY_ADDENDUM.md (SL 3, SL 4G–M, SL 5G–M) | Ontologize companion resource cross-reference added after Palantir Developers channel ref | youtube.com/@Ontologize |
| 217 | exercises/EX_40H, EX_40J, EX_40K, EX_40L | Build with AIP Official Tutorials supplemental sections (5/3/3/4 tutorials respectively) | community/t/5137 + build.palantir.com |
| 218 | DEPENDENCY_MAP.md | Section 10, External Doctrinal References (Palantir), changelog entries #203–218 | All sources |
| 219 | 237 PDFs force-rebuilt | All source hash changes reflected; SHA256 manifest regenerated | N/A |
| 220 | pdf/.manifest.json | 11 source hashes updated | N/A |
| 221 | pdf/pdf_manifest.sha256 | 237 entries regenerated | N/A |
| 222 | DEPENDENCY_MAP.html | Regenerated (144 nodes, 337 edges) | N/A |
| 223 | pdf/AR_350_1_ALIGNMENT_MAP.pdf | AR 350-1 alignment map (PDF): 11 regulatory areas mapped to MSS components, SAT artifact coverage table, 3 identified gaps with mitigations, compliance posture summary | AR 350-1, TR 350-70, TP 350-70-14, ADP 7-0, FM 7-0 |
