# Source Material — USAREUR-AF MSS Training Corpus

## Overview

This directory contains all source content used to develop and support the Maven Smart System (MSS) training curriculum. Content is organized by type. 

Do not modify files in this directory without coordinating with the Operational Data Team (ODT). These are authoritative source materials — edits to training content belong in `maven_training/tm/`, `maven_training/syllabi/`, and related curriculum directories.

---

## Directory Index

### `course_portal/` — CDA Slide Library (Training Portal)

Interactive browser-based slide viewer serving the CDA training deck library. Contains 29 downloadable PDF decks across three series:

**Intro To Data series** — Foundational concepts. Prereq for TM-10 (Maven User).
- `army_data_orientation_v1.pdf` — Army data context and MSS orientation
- `What_Is_An_Ontology.pdf` — Ontology fundamentals
- `The_Four_Layers.pdf` — 4-layer architecture overview
- `Dont_Filter_This_Isnt_Excel.pdf` — Foundry vs spreadsheet mental model
- `The Semantic Layer Instructions.pdf` — Doctrine-first semantic layer governance
- `decision_advantage_deep_dive.pdf` — Decision advantage framework

**Data 101 series** — Builder-level skills. Prereq for TM-20 (Builder).
- `Data_Modeling_Foundations.pdf` — Conceptual, logical, physical modeling
- `Data_Modeling_Fundamentals_Level1.pdf` — Kimball, Inmon, Data Vault
- `Data_Modeling_Fundamentals_Level2.pdf` — Advanced modeling patterns
- `Data_Architecture_Deep_Dive.pdf` — Data architecture design patterns
- `Data_Platforms_Cloud_Deep_Dive.pdf` — Cloud platforms and Foundry
- `L2_Ingestion_Integration_Deep_Dive.pdf` — Integration patterns and pipelines
- `Controlled_Vocabularies.pdf` — CV design and governance
- `Links_and_Relationships.pdf` — Ontology link modeling
- `Identity_Who_Owns_The_Key.pdf` — Identity resolution
- `ObjectType_WhatToWatchFor.pdf` — Object type anti-patterns
- `2026_Data_Stack_Deep_Dive.pdf` — 5-Layer Data Stack with Foundry mapping

**Data 201 series** — Advanced builder / specialist prereq for TM-30 and TM-40G–O.
- `Deck_01_Architecture_First_Principles.pdf` — EA/DA first principles
- `Deck_02_Scope_Engineering.pdf` — Scope and requirements engineering
- `Deck_03_RDF_OWL_Foundations.pdf` — Semantic web and ontology foundations
- `Deck_04_Object_Type_Varieties.pdf` — The nine object type varieties
- `Deck_05_Identity_Governance.pdf` — Identity governance at scale
- `Deck_06_Relationship_Modeling.pdf` — Advanced relationship patterns
- `Deck_07_Temporal_Bitemporal.pdf` — Bitemporal modeling
- `Deck_12_Capstone_Foundry.pdf` — End-to-end Foundry implementation
- `Semantic_Modelling_Course_Intro.pdf` — Semantic modeling course overview
- `architecture_primer.pdf` — Architecture primer for practitioners
- `AI_ML_Beyond_The_Hype.pdf` — AI/ML grounded in data architecture
- `L5_Activation_Interface_Deep_Dive.pdf` — L5 activation and OSDK patterns

**Portal files:** `index.html`, `deck.html`, `pathways.html`, `app.js`, `styles.css`, `manifest.json`, `nav-manifest.json`, `portal-module.tsx`

**TM Track support:** TM-10 through TM-40G–O (all tracks, as prereq reading)

---

### `cda_apps/` — Interactive Training Tools

Standalone browser-based applications reinforcing MSS curriculum concepts. See `cda_apps/README.md` for full detail.

| App | Key Content | Supports |
|-----|-------------|----------|
| `ea-vs-da-reference/` | EA vs DA definitions, comparison table, hierarchy model | TM-30, TM-40K, TM-40L |
| `enterprise-data-compass/` | 5-Layer Stack, ontology standards, VAULTIS-A, governance, CDS rules | TM-40J, TM-40K |
| `lessons-learned/` | AAR format, LL-001 AVT25 assessment tools case study | All tracks |
| `plan-for-success/` | Technology Radar + 5-phase program roadmap with approval chains | TM-40J, TM-30 |
| `shared/` | `nato-theme.css`, `hermes-theme.css` design tokens | (shared assets) |

---

### `cda_docs/` — Source PDFs and Reference Documents

Authoritative reference documents used to develop curriculum content. Organized by type.

**Top-level:**
- `DDOF_Playbook_v2_2.pdf` — Defense Data Orchestration Framework lifecycle playbook (canonical copy, v2.2, December 2025, T2COM C2DAO, CUI // FEDCON)

**`reference/`** — ODT-produced reference documents and key Army publications:
- `DDOF_Playbook_v2_2.pdf` — DDOF Playbook v2.2 (Defense Data Orchestration Framework, December 2025, T2COM C2DAO)
- `Cross-Domain Solutions_ Complete Technical Reference for Ontology Modeling.pdf` — CDS technical reference
- `Fighting_with_Live_Data_XVIII_ABC_ODTs_MilReview_Feb2026.pdf` — Forney, Herrmann, and Steele, "Fighting with Live Data: XVIII Airborne Corps' Experience with Its Operational Data Teams," *Military Review* Online Exclusive, February 2026. XVIII ABC's pilot experience with the ODT concept — organizational journey, manning structure, problem-solution development process, Program Increment cycles, TIO governance, BDA visualization case study, and echeloned employment concept. **Required reading for TM-40J, TM-40F. Recommended for all TM-40 tracks.**
- `Adkins_Achieving_Decision_Dominance_MilReview_JanFeb2025.pdf` + `.md` (summary) — Adkins, "Achieving Decision Dominance: The Arduous Pursuit of Operationalized Data," *Military Review* 105, no. 1 (January-February 2025). One officer's thought piece proposing decision optimization at echelon. Introduces useful terminology: operationalized data, Automated Fighting Products (AFP), and Decision Optimization Teams (DOT). Proposes echeloned DOT employment from division through HQDA with FA 26B/49/57 workforce. Names Maven Smart System as the USCENTCOM ASCC-level COP platform. Proposes gunnery-table training model for DOT certification. **Supplementary reading for TM-40F, TM-40G, TM-40J. Recommended for all TM-40 tracks and Data Literacy Senior Leaders.**
- `Rainey_Transformation_in_Contact_MilReview_Aug2024.pdf` — Rainey, "Continuous Transformation: Transformation in Contact," *Military Review* Online Exclusive, 9 August 2024. CSA's concept for continuous Army transformation. Establishes the operational context for ODTs and data-centric capabilities — transformation requires a data foundation, not just new technologies. SEC ARMY directed ODT experimentation under TiC 2.0. **Recommended for all TM-40 tracks and training management staff.**

**`training/`** — Training materials:
- `Intro To Data/The Semantic Layer Instructions.pdf`
- `Data 201/Data_Modeling_Fundamentals_Level2.pdf`

**`official_us/`** — Official U.S. government publications:
- `doctrine/` — ADP 3-13, TC 7-0 series
- `policy/` — Software modernization, open source, MPE policy
- `strategy/` — DoD Data Strategy, AI Strategy, Data Quality Priorities, OCONUS Cloud Strategy, Data Analytics/AI Adoption Strategy
- `acquisition/` — Requirements and acquisition guidance

**`official_nato/`** — Official NATO publications:
- `2504-NAFv4-ArchiMate.pdf` — NAF version 4 / ArchiMate mapping
- `NATO Architecture and Semantic Frameworks for NAFv4 Compliance and Military Operational Modeling.pdf`
- `GRAEBENER.pdf` — NATO architecture reference
- `ajp/` — AJP-01, AJP-3, AJP-3.2, AJP-5, AJP-10.1 (Allied Joint Publications)
- `amsp/` — AMSP-01 through AMSP-05 (Allied Metadata Standardization Publications)

**`ddof/`** — DDOF process artifacts:
- `reference/ddof.ts` — TypeScript DDOF data model
- `reference/process.txt` — DDOF process narrative

---

### `doctrine_pdfs/` — Army Doctrine Publications

Official U.S. Army doctrine publications used as source material across all TM tracks.
- `UK_JDP0-01_2019.pdf` — UK Joint Doctrine Publication
- `US_ADP3-0_2019.pdf` — ADP 3-0 Operations
- `US/` — Additional U.S. Army publications

---

## TM Track Quick Reference

| Track | Primary Source Material |
|-------|------------------------|
| TM-10 (Maven User) | course_portal Intro To Data series |
| TM-20 (Builder) | course_portal Data 101 series |
| TM-30 (Advanced Builder) | course_portal Data 201 series; cda_apps/ea-vs-da-reference; cda_apps/plan-for-success |
| TM-40A–F (WFF tracks) | course_portal Data 101 series; cda_apps/lessons-learned |
| TM-40G (ORSA) | course_portal Data 201 series; cda_docs/reference |
| TM-40H (AI Engineer) | course_portal Data 201 + AI_ML_Beyond_The_Hype; cda_docs/official_us/strategy |
| TM-40M (ML Engineer) | course_portal Data 201; cda_docs/official_us/strategy |
| TM-40J (Program Manager) | cda_apps/enterprise-data-compass; cda_apps/plan-for-success; cda_docs/official_us/acquisition |
| TM-40K (Knowledge Manager) | cda_apps/ea-vs-da-reference; cda_apps/enterprise-data-compass |
| TM-40L (Software Engineer) | course_portal Data 201; cda_apps/ea-vs-da-reference; cda_docs/official_nato |
| TM-50G–O (Advanced series) | All Data 201 + cda_docs/official_nato + cda_docs/official_us |

---

*Operational Data Team — USAREUR-AF*
*Last updated: 2026-03-13*
