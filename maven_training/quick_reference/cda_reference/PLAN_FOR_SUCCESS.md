<!-- MAVEN TRAINING CORPUS — CDA REFERENCE MATERIAL
     Source: odt_workspace/docs/architecture/cda/reference/plan-for-success.md
     Supports: all TM tracks, especially TM-40J (Program Manager), TM-40K (Knowledge Manager)
     Type: Reference
-->
---
sidebar_position: 3
title: "Plan for Success"
description: USAREUR-AF Data Architecture Radar with 5-phase implementation roadmap, approval tracking, and technology standards
layer: architecture
category: reference
---

# Data Architecture Radar -- Plan for Success

*USAREUR-AF Enterprise Data Compass and Plan for Success -- Version 1.0 -- February 2026*
*CUI // FOUO*

### Authorizing Document

This radar is the **authoritative record** of data architecture standards, tool selections, and approval status for **USAREUR-AF**.

| Role | Signature |
|------|-----------|
| Chief Technology Officer, USAREUR-AF | (pending) |
| Chief Data Architect, ODT | (pending) |

> **BLUF -- Bottom Line Up Front:** **Definition before data. Doctrine before design. One canonical type per concept.** Every object type traces to published doctrine, passes peer review, and meets VAULTIS-A quality standards before it touches production. This plan sequences 5 phases from institutional authority through multi-echelon expansion. **Phase 1 must complete within 30 days** -- without signed authority, everything downstream is advisory. MVP delivery per Secretary of the Army priorities: **speed over perfection, warfighter first.**

## Architecture Radar

### Ring Definitions

| Ring | Description |
|------|-------------|
| **Adopt** | Approved standard. Use it. |
| **Trial** | Validated in pilot. |
| **Assess** | Under evaluation. |
| **Hold** | Proceed with caution. |

### 5-Layer Data Stack

| Layer | Name | Description | Owner |
|-------|------|-------------|-------|
| L1 | Infrastructure | Compute, network, storage | Platform / DISA |
| L2 | Integration | Pipelines, ingestion, sync | Data Engineers |
| **L3** | **Semantic** | **Ontology, meaning, truth** *(Critical)* | **CDA / ODT** |
| L4 | Analytics | BI, models, dashboards | Analysts / ORSA |
| L5 | Activation | Apps, workflows, AI | Product Teams |

**Investment Rule: L2 + L3 > L5** -- Foundation before features.

### Quadrants

| Quadrant | Focus |
|----------|-------|
| Standards and Governance | Principles, documents, processes |
| Platform and Tools | Foundry capabilities, tooling |
| Ontology and Modeling | Object types, patterns, design |
| Interoperability and Security | CDS, NATO, classification |

### Key Radar Items by Layer

#### L1 -- Infrastructure

| Item | Ring | Notes |
|------|------|-------|
| DISA Cloud Hosting | Adopt | FedRAMP-compliant compute, storage, network |
| Foundry/Vantage Platform Designation | Trial | Formal command guidance pending CTO signature |
| MSS/Vantage NIPR Instance | Adopt | Primary unclassified operational data environment |
| Vantage SIPR Instance | Trial | Required for cross-domain architecture |
| Vantage JWICS Instance | Assess | Under evaluation for USAREUR-AF deployment |
| Platform Team Ownership Model | Adopt | Clear RACI for compute, network, storage provisioning |

#### L2 -- Integration

| Item | Ring | Notes |
|------|------|-------|
| Pipeline Builder | Adopt | Primary L2 integration tool |
| Code Workbook | Adopt | Custom data transformations |
| Data Connections | Adopt | Source system integration |
| Cross-Domain From Day One | Adopt | CDS topology as first-class design constraint |
| CDS Export/Import Pattern | Trial | Source -> export filter -> CDS guard -> target -> ontology merge |
| Foundry Cross-Enclave Sync | Assess | NCDSMO baseline patterns; hardest technical risk |
| NCDSMO Baseline Compliance | Trial | Cross-domain data flow standards |
| CDS Latency Documentation | Trial | Per Compass Section 6 |

#### L3 -- Semantic (Critical Layer)

| Item | Ring | Notes |
|------|------|-------|
| Definition Before Data | Adopt | Principle: definition grounded in published doctrine |
| One Canonical Type Per Concept | Adopt | Type proliferation is the primary anti-pattern |
| Semantic Layer Is Critical Layer | Adopt | L2 + L3 investment takes priority over L5 |
| Governance By Design | Adopt | Peer review, DDOF gates, VAULTIS-A |
| Object Type Cookbook v2.0 | Adopt | 9 varieties, decision trees, quality metrics |
| Cookbook Addendum A | Adopt | Data scope assessment, doctrine alignment |
| Peer Review (Mandatory) | Adopt | Checklist-driven, reviewer cannot be author |
| Architecture Review Board | Trial | Biweekly cadence, approve/revise/reject authority |
| Entity Object Type | Adopt | People, units, equipment |
| Event Object Type | Adopt | SIGACTs, movements |
| Capability Object Type | Adopt | Warfighting functions, operational capabilities |
| Controlled Vocabulary | Adopt | Enumerations and codes |
| Reference Object (4-Tier) | Adopt | Standardized lookups |
| Relationship Link | Adopt | Object-to-object connections |
| Assessment Object Type | Trial | Scores and readiness assessments |
| Document Object Type | Trial | OPORDs, publications |
| Metric Object Type | Assess | KPIs and measures |
| Doctrine-to-Ontology Alignment Worksheet | Adopt | REUSE/EXTEND/CREATE decision framework |
| Core Ontology Starter Set | Assess | Minimum shared starting point |
| Bitemporal Modeling | Assess | Valid-time and transaction-time tracking |
| Classification Ceiling Property | Adopt | Mandatory per Compass Section 6 |
| NAFv4 Compatibility | Assess | Coalition interoperability requirement |
| DODAF DIV-1/2/3 Alignment | Trial | Architecture viewpoints as ontology artifacts |
| STANAG Alignment (4559/5500/APP-6) | Assess | NATO interoperability |

#### L4 -- Analytics

| Item | Ring | Notes |
|------|------|-------|
| Contour | Adopt | Interactive data analysis and BI |
| Workshop Analytics | Trial | Ontology-backed analytics applications |
| Quiver | Assess | Advanced analytical notebooks |
| VAULTIS-A Quality Framework | Adopt | 8 quality dimensions, 85% minimum gate score |
| Ontology Health Dashboard | Assess | Object type counts, quality scores, freshness |

#### L5 -- Activation

| Item | Ring | Notes |
|------|------|-------|
| Workshop Apps | Trial | Ontology-backed operational applications |
| Slate Dashboards | Hold | Legacy; being superseded by Workshop/OSDK |
| OSDK Front-End | Trial | Custom web apps against Foundry ontology |
| DDOF Playbook v2.0 | Adopt | 6-phase data product lifecycle |
| NAF Architecture Builder | Assess | React graph editor, prototype stage |
| Course Portal | Adopt | Training slide-viewer with 4 decks |
| Investment Rule: L2+L3 > L5 | Adopt | Foundation before features |
| Semantic Layer Instructions | Adopt | Doctrine-first governance philosophy |

## Assessment of Current State

### Strengths

| Asset | Status | Assessment |
|-------|--------|------------|
| Object Type Cookbook v2 + Addendum A | Complete | Production-grade. 9 object type varieties, decision trees, quality metrics, peer review checklists. |
| Semantic Layer Instructions | Complete | Doctrinally sound. Definition-first, PR-based governance, full-time stewardship mandate. |
| Data Modeling Foundations (L1 + L2) | Complete | Strong training curriculum. Covers Kimball, Inmon, Data Vault with Foundry mapping. |
| 2026 Data Stack Deep Dive | Complete | 5-layer architecture with Foundry mapping. L3 correctly identified as critical layer. |
| EA Curriculum (6-part series) | Complete | Comprehensive. Covers foundations through military application. |
| Tool Convergence Assessment | Complete | Ready for CTO signature. 7 testable hypotheses. |
| DDOF Playbook v2.0 | Complete | 6-phase lifecycle with VAULTIS-A quality framework. |
| Cross-Domain Solutions Reference | Complete | CDS taxonomy, NCDSMO baseline, Foundry cross-enclave sync patterns. |
| HERMES Program Identity | Complete | Landing page, OPORD 0015-26 context, team roster, timeline. |
| NAF Architecture Builder | Prototype | React graph editor with xyflow. IR extraction pipeline works. |
| Course Portal | Complete | Static site serving 4 training decks with slide preview and downloads. |
| EA vs DA Reference Page | Complete | Clean interactive reference establishing DA as first-class child of EA. |

### Gaps

| Gap | Risk If Not Addressed |
|-----|----------------------|
| Enterprise Data Compass (signed) | Without the signed Compass, every standard in the Cookbook is advisory, not authoritative. |
| Starter Ontology (core object types) | Every team builds from scratch. No shared starting point. |
| Doctrine-to-Ontology Mappings | No traceable thread from DoD Data Strategy to Foundry object type. |
| Ontology Health Metrics Dashboard | Cannot answer: is the architecture being used? |
| 90-Day Tool Audit Results | The 7 hypotheses remain untested. Leadership cannot act on assertions. |
| Training Certification Mechanism | Training becomes optional in practice. |
| Cross-Domain Implementation Guide | Each team figures out CDS independently. Inconsistent patterns. |
| Sequenced Program Roadmap | No visible critical path. Leadership cannot track progress. |

## 5-Phase Implementation Roadmap

### Phase 1: Establish Authority (30 days)

**Objective:** Convert the existing body of work into signed, enforceable institutional authority. Without this, everything downstream is optional.

**Deliverables:**

1. **Enterprise Data Compass v1.0** -- Compile the Cookbook, Semantic Layer Instructions, and 5-Layer Stack into a single signed reference. CTO and CDAO signature blocks. Version-controlled.
2. **Tool Convergence Directive** -- Get the existing convergence memo signed by the CTO. Issue moratorium on new non-strategic tool adoption.
3. **Foundry/Vantage Platform Designation** -- Formal command guidance designating Foundry/Vantage as the authoritative operational data platform.
4. **HERMES Program Charter** -- Formalize HERMES with scope, authority, resourcing, and reporting chain.

**Exit Criteria:**

- Enterprise Data Compass signed by CTO/CDAO
- Tool convergence memo signed and moratorium in effect
- Platform designation guidance issued
- HERMES charter approved

### Phase 2: Build the Foundation (60 days)

**Objective:** Deploy the first production ontology objects and complete the first doctrine-to-ontology mapping. Prove the methodology works end-to-end.

**Deliverables:**

1. **Core Ontology Starter Set** -- Deploy foundational object types: Unit, Person, Equipment (entities) + WarfightingFunction, OperationalDomain, Echelon, ClassificationLevel (CVs) + Capability + SIGACT (event). Each passes Cookbook peer review.
2. **First Doctrine-to-Ontology Mapping** -- Complete Addendum A worksheet for one priority domain (Readiness or Force Structure). Document REUSE/EXTEND/CREATE decisions with full traceability.
3. **CDS Architecture Pattern Validation** -- Implement and validate Foundry cross-enclave sync for at least one object type across NIPR/SIPR.
4. **DDOF Pilot Product (Phase 1-3)** -- Run DDOF playbook end-to-end on one data product. Validate VAULTIS-A quality gates. Document lessons learned.

**Exit Criteria:**

- Core starter ontology deployed in production Foundry
- At least one doctrine mapping completed with peer review
- CDS sync validated for at least one object type
- One DDOF product through Gate 3 with VAULTIS-A scores documented

### Phase 3: Scale Through Training (45 days)

**Objective:** Ensure every person building on the ontology has completed training and can pass a competency check.

**Deliverables:**

1. **Training Certification Program** -- Build assessments for each level (Foundations, Level 2, Semantic Layer). Minimum passing score. Certificates tracked in HERMES.
2. **Level 3 Training: Advanced Patterns** -- New deck covering CDS ontology patterns, bitemporal modeling, entity resolution, and DDOF integration.
3. **Leadership Briefing Package** -- Condensed training for G3/G8/CTO audiences. Why it matters, how to consume it, how to govern it.
4. **Train-the-Trainer Cadre** -- Certify 3-5 instructors who can deliver training at echelon without ODT presence.

**Exit Criteria:**

- Assessment mechanism deployed for all training levels
- Level 3 deck complete and peer-reviewed
- At least one leadership briefing delivered to GO/SES audience
- 3+ certified trainers outside ODT core team

### Phase 4: Govern and Measure (60 days)

**Objective:** Prove the architecture is being adopted, deliver audit data, and stand up self-sustaining governance.

**Deliverables:**

1. **90-Day Tool and License Audit** -- Quantify: total license costs by tool, FTEs on platform admin vs. operational output, cross-domain availability, capability overlap with Foundry.
2. **Ontology Health Dashboard** -- Foundry Workshop dashboard: object type count, link coverage, quality scores, consumer count, freshness, VAULTIS-A scores.
3. **Architecture Review Board (ARB)** -- Stand up ARB per EA_04 Governance. Connect to Cookbook peer review and DDOF Phase 1 gate. Charter, criteria, cadence.
4. **Talent Reclamation Report** -- Using audit data, quantify personnel recovered from redundant platform management. Map to Foundry roles.

**Exit Criteria:**

- Audit report delivered to CTO with quantified findings
- Ontology health dashboard live in production Foundry
- ARB chartered and operational with first review completed
- Talent reclamation report with specific transition recommendations

### Phase 5: Expand and Sustain (90+ days)

**Objective:** Scale beyond USAREUR-AF core to multi-echelon, joint, and coalition adoption.

**Deliverables:**

1. **Multi-Echelon Deployment** -- Push ontology access and training to division and brigade level. Measure time-to-first-product at each echelon.
2. **Joint Adoption (NAVEUR / USAFE)** -- Execute onboarding plan for NAVEUR and USAFE. Validate semantic layer supports joint operational concepts without forking.
3. **NATO Interoperability Validation** -- Test ontology objects against NAFv4 viewpoints using Architecture Builder. Validate STANAG alignment. Document gaps.
4. **Program Roadmap (Live Artifact)** -- Deploy AG Grid roadmap with actual program data. Capability gaps mapped to funded initiatives. Monthly update cadence.
5. **Enterprise Data Compass v2.0** -- Incorporate lessons learned from Phases 1-4. Update standards based on production experience. Add joint/coalition patterns. Re-sign.

**Exit Criteria:**

- At least 2 echelons below theater producing data products on shared ontology
- At least 1 joint component onboarded to shared semantic layer
- NAF alignment assessment completed with documented results
- Live roadmap accessible to command leadership

## Critical Dependencies

| Dependency | Blocks | Mitigation |
|------------|--------|------------|
| CTO/CDAO signature on Enterprise Data Compass | All of Phase 2-5 (standards become enforceable) | Pre-brief CTO. Use convergence memo as forcing function. |
| Core ontology starter set deployed | Phase 3 training (need real objects to train against) | Begin design in parallel with Phase 1 signatures. |
| 90-Day audit data | Phase 4 ARB decisions and Phase 5 resource reallocation | Start audit data collection in Phase 1. |
| Certified trainers | Phase 5 multi-echelon deployment | Identify candidates in Phase 2. Begin certification in Phase 3. |
| CDS pattern validation | Phase 5 joint and coalition adoption | Start CDS work in Phase 2 and do not stop. Hardest technical risk. |

## Bottom Line

1. Get the Enterprise Data Compass signed. Without this, the Cookbook is a suggestion. With it, the Cookbook is law.
2. Get the convergence memo signed. The moratorium creates urgency.
3. Deploy the core ontology starter set. Every day without shared objects is a day teams build in isolation.

**The doctrine is written. The tools are built. The training exists. Now make it real.**

---

*Operational Data Team -- HERMES Program -- USAREUR-AF*
*CUI // FOUO*
*Distribution: USAREUR-AF / LANDCOM -- Operational Data Team, HERMES Program. Authorized recipients only per CUI handling procedures.*
*Proponent: Chief Data Architect, Operational Data Team (ODT)*
*Authority: OPORD 0015-26, USAREUR-AF Unified Data Transformation Strategy*
