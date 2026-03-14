<!-- MAVEN TRAINING CORPUS — PROJECT REFERENCE MATERIAL
     Source: odt_workspace/docs/enterprise-v10-plan.md
     Supports: TM-40H (AI Engineer), TM-40I (ML Engineer), TM-40L (Software Engineer), TM-50H/I/L (Advanced)
     Type: Project Reference — ODT Enterprise v10 Release Plan
-->

# ODT Enterprise v10 — Unified Release Plan

**Generated:** 2026-03-12
**Loop:** Ralph-001
**Goal:** Releasable, doctrine-aligned, enterprise-grade products across all bounded contexts.

---

## North Star

> Doctrine as Executable Architecture — a universal semantic model of how military institutions intend to behave.

Every piece of this repo must serve that north star: a machine-readable, cross-national, bi-temporal doctrinal knowledge graph surfaced through releasable products.

---

## Bounded Contexts & Release Targets

### 1. ARCHITECTURE — Doctrine Modeling

#### 1a. GDAP — Global Doctrine Alignment Platform
**Target:** Full 10-domain capability implementation (all phases from vision.md)

Phases to complete:
- Phase 1: Doctrine Ingestion & Atomization (Steps 1–5) — 6,092 elements extracted; ensure pipeline is idempotent & tested
- Phase 2: Cross-National Alignment Engine (Steps 6–9) — embedding + similarity + divergence scoring releasable
- Phase 3: Doctrine-to-Data Mapping (Steps 10–12) — element → schema linkage complete
- Phase 4: Temporal Tracking (Steps 13–14) — bi-temporal store working in DuckDB
- Phase 5: DVEE — Doctrine Vulnerability & Exploitability Engine (Steps 15–20) — authority graph + exploitability index

**Release criteria:**
- All GDAP CLI commands work on mss_nipr data
- REST API returns doctrine elements with OSDK-compatible IDs
- UI shows alignment, drift, divergence dashboards
- All 7 content types classified
- Tests: >80% coverage

#### 1b. MIM — Military Information Model
**Target:** MIM 5.3 → production Foundry ontology TypeScript + SQL DDL

Tasks:
- Generate complete Foundry Object Type TypeScript from all MIM 5.3 concepts
- Publish generated output to `schemas/ontology/` as declarative JSON-LD
- MIM admin app: complete schema store, diff view, vector search
- MIM viewer: working D3/Three.js visualization of entity graph

**Release criteria:**
- `make mim-generate` produces valid Foundry TypeScript
- Generated ontology committed to `schemas/ontology/`
- MIM admin server passes all 36 test files

#### 1c. CDA — Cross-Domain Architecture
**Target:** NAF Architecture Builder + alignment apps production-ready

Tasks:
- NAF Architecture Builder: drag-and-drop canvas exports valid NAF 4.0 JSON
- All CDA skeleton apps — either complete or removed
- Doctrine atomization tools: idempotent, tested, producing clean DoctrineElements

#### 1d. Declarative Doctrine Ontology (CRITICAL PATH)
**Target:** A single, usable, deployable doctrine-aligned ontology

Output: `schemas/ontology/doctrine-ontology.json` (JSON-LD + OWL annotations)

Structure:
```
DoctrineDocument
  DoctrineSection
    DoctrineElement (7 content types)
      Concept | Task | Authority | Process | InfoRequirement | Constraint | Definition
  Warfighting Function → Element links
  Cross-Nation Alignment → Element links
  Capability → Element links (via CapabilityElementLink)
  System → Capability links
  Gap tracking
```

Must be:
- Machine-readable (JSON-LD with @context)
- Foundry-deployable (Object Types + Links in TypeScript)
- OSDK-consumable (exported types)
- Usable in products (platform, chase, one-more-brief)

---

### 2. PIPELINES — Data Ingestion

**Target:** All 33 catalog pipelines green, orchestrated, producing clean DuckDB/Parquet

Priority pipelines:
1. `gdap` — doctrine element ingestion — CRITICAL
2. `foundry-platform-catalog` — Foundry metadata — CRITICAL
3. `mil-pubs` — military publications indexer — HIGH
4. `acled`, `sipri`, `ucdp`, `cow` — conflict data for CHASE — HIGH
5. `nations`, `countries`, `world-factbook` — reference data — MEDIUM

**Orchestrator (Dagster):**
- All assets defined with proper metadata
- Schedules set for nightly runs
- dbt transforms complete for `mil_pubs_dbt_assets`
- Sensors for new doctrine document detection

**Release criteria:**
- `make pipelines-run` completes without errors
- GDAP pipeline produces DoctrineElements consumable by GDAP API
- All catalog outputs have smoke tests

---

### 3. PRODUCTS — User-Facing Applications

#### 3a. Platform — Operational Decision Engine (ODE)
**Target:** Production-ready v1.0 decision support platform

#### 3b. CHASE — Conflict History Analysis & Scenario Engine
**Target:** Releasable conflict prediction product

Tasks:
- All 6 ML models loaded and serving predictions via API
- Frontend: complete all views
- Data pipeline: ACLED+SIPRI+UCDP+COW → CHASE data objects → API

#### 3c. One-More-Brief — MDMP Planning
**Target:** Desktop app builds, installs, produces brief

#### 3d. ODT Appstore — App Discovery
**Target:** App catalog functional with all ODT apps listed

---

### 4. FOUNDRY — Developer Tools

#### 4a. VS Code Extension (vs-ffs)
**Target:** v0.5.0 published to marketplace or .vsix ready for distribution

#### 4b. foundry-platform-utils (odt)
**Target:** v0.2.0 with complete API coverage + tests

#### 4c. foundry-widget-factory
**Target:** Widget build system working, hermes + llm-prep widgets complete

#### 4d. foundry-local-builder
**Target:** Build ontology locally from MIM IR output — roundtrip MIM → local DuckDB → Foundry TypeScript

---

## Milestone Gates

### Gate M1 — Ontology Complete
- `schemas/ontology/doctrine-ontology.json` committed
- MIM → Foundry TypeScript generated
- DoctrineElement → Foundry Object Type mapping documented

### Gate M2 — Pipelines Green
- GDAP pipeline produces ≥5,000 elements
- All catalog smoke tests pass
- Dagster UI launches without errors

### Gate M3 — Products Bootable
- `docker-compose up --profile products` starts all product services
- Chase API returns predictions
- Platform UI loads

### Gate M4 — Foundry Tools Ship
- VS Code extension installs and connects
- `odt` library passes full test suite

### Gate M5 — RELEASE GATE (quality-guardian + ddd-reviewer + contract-steward)
- DDD compliance review passed
- All contracts consistent
- No P0 issues open
- Coverage targets met
- Docker Compose full stack starts clean

---

## Agent Assignments — Loop 1

| Agent | Primary Task | Output |
|-------|-------------|--------|
| `doctrine-modeler` | Extend GDAP to full 10-domain capability; capability models; DVEE schema | `src/architecture/gdap/gdap/` |
| `ontology-builder` | Build declarative doctrine ontology; MIM→Foundry OT generation | `schemas/ontology/` |
| `pipeline-engineer` | Fix all P0 pipeline issues; Dagster assets complete; smoke tests | `src/pipelines/` |
| `product-builder` | CHASE P0 fixes; Platform API completion; ODT Appstore | `src/products/` |
| `foundry-developer` | vs-ffs polish; odt v0.2; widget factory | `src/foundry/` |
| `contract-steward` | Audit all cross-context contracts; enforce naming | cross-cutting |
| `workspace-operator` | Makefile targets; Docker Compose; CI; docs | root + compose/ |
| `quality-guardian` | Milestone gate reviews; test coverage reports | docs/architecture/loop/ |
| `ddd-reviewer` | DDD compliance on all bounded contexts | docs/architecture/loop/ |

---

## Enterprise v10 Feature Checklist

- [ ] Doctrine ontology declarative JSON-LD
- [ ] GDAP 10-domain capability
- [ ] DVEE (exploitability engine)
- [ ] Cross-national alignment (US/UK/NATO/CA/AU)
- [ ] Bi-temporal tracking in DuckDB
- [ ] All 33 catalog pipelines green
- [ ] Dagster orchestrator scheduling
- [ ] CHASE predictions serving
- [ ] Platform ODE API complete
- [ ] One-More-Brief desktop builds
- [ ] ODT Appstore catalog complete
- [ ] VS Code extension v0.5.0 release-ready
- [ ] odt library v0.2.0 tested
- [ ] Docker Compose full stack boots
- [ ] Nginx routing all products
- [ ] CI/CD pipeline green
- [ ] Gate M5 quality score ≥ 85/100
