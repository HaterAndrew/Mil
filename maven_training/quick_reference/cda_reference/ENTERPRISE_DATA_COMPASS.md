<!-- MAVEN TRAINING CORPUS — CDA REFERENCE MATERIAL
     Source: odt_workspace/docs/architecture/cda/reference/enterprise-data-compass.md
     Supports: all TM tracks, especially TM-40J (Program Manager), TM-40K (Knowledge Manager)
     Type: Reference
-->
---
sidebar_position: 1
title: "Enterprise Data Compass"
description: The authoritative standard for data architecture, ontology design, and semantic governance across all USAREUR-AF operational data systems
layer: architecture
category: reference
---

# Enterprise Data Compass

*USAREUR-AF Authoritative Reference -- Version 1.0 -- February 2026*

The authoritative standard for data architecture, ontology design, and semantic governance across all USAREUR-AF operational data systems.

### Authorizing Directive

This document establishes the **authoritative standard** for all data architecture, ontology modeling, and semantic layer governance within USAREUR-AF. Compliance is **mandatory** for any team creating, extending, or consuming object types in the operational data platform.

| Role | Signature |
|------|-----------|
| Chief Technology Officer, USAREUR-AF | (pending) |
| Chief Data Architect, ODT | (pending) |

> **Bottom Line:** **Definition before data. Doctrine before design. One canonical type per concept.** Every object type traces to published doctrine, passes peer review, and meets VAULTIS-A quality standards before it touches production.

## Section 1: Governing Principles

### Principle 1 -- Definition Before Data

Every object type begins with a human-readable definition grounded in published doctrine (FM, ADP, ATP, STANAG, MIM). The definition is the contract. If the definition is wrong, the data model is wrong regardless of technical correctness.

### Principle 2 -- One Canonical Type Per Doctrine Concept

The Ontology maintains exactly one canonical object type per doctrine concept. When data scope is insufficient, expand the existing type. Type proliferation (multiple types representing the same concept with different data populations) is the primary anti-pattern.

### Principle 3 -- The Semantic Layer Is the Critical Layer

In the 5-Layer Data Stack, Layer 3 (Semantic) is where meaning is assigned. Everything above it (analytics, activation) inherits that meaning. Investment in L2 + L3 takes priority over L5. A weak semantic layer produces fast garbage.

### Principle 4 -- Governance By Design, Not By Memo

Every object type change goes through peer review. Every data product follows DDOF phase gates. Every quality metric is measured by VAULTIS-A. Governance is enforced in the platform, not in email threads.

### Principle 5 -- Cross-Domain From Day One

Architecture must account for NIPR, SIPR, and JWICS classification boundaries as a first-class design constraint. CDS topology is an input to data architecture, not an afterthought.

## Section 2: The 5-Layer Data Stack

Every operational data capability maps to exactly one layer. Teams invest from the bottom up. Skipping layers produces fragile systems.

| Layer | Name | Description |
|-------|------|-------------|
| L1 | Infrastructure | Compute, network, storage |
| L2 | Integration | Pipelines, ingestion, sync |
| **L3** | **Semantic** | **Ontology, meaning, truth** *(Critical)* |
| L4 | Analytics | BI, models, dashboards |
| L5 | Activation | Apps, workflows, AI |

### Foundry Implementation by Layer

| Layer | Foundry Implementation | Owns |
|-------|----------------------|------|
| L1 Infrastructure | Cloud hosting, Foundry platform deployment | Platform team / DISA |
| L2 Integration | Pipeline Builder, Code Workbook, data connections | Data engineers |
| L3 Semantic | Ontology object types, properties, links, definitions | CDA / ODT |
| L4 Analytics | Contour, Workshop analytics, Quiver | Analysts / ORSA |
| L5 Activation | Workshop apps, Slate dashboards, operational workflows | Product teams |

> **Investment Rule:** L2 + L3 investment must exceed L5 investment. A strong semantic layer makes every application built on top of it faster, cheaper, and more trustworthy. A weak semantic layer makes every application a liability.

## Section 3: Ontology Standards

The **Object Type Cookbook v2.0** is the implementing document for all ontology design. The nine object type varieties below are the only authorized modeling patterns.

| Variety | Description |
|---------|-------------|
| Entity | People, units, equipment |
| Event | SIGACTs, movements |
| Capability | What the force can do |
| Controlled Vocab | Enumerations, codes |
| Reference Object | Lookups (4 tiers) |
| Relationship | Links between objects |
| Assessment | Scores, readiness |
| Document | OPORDs, products |
| Metric | KPIs, measures |

> **Mandatory Decision Framework:** Before creating any new object type, teams must complete the **Doctrine-to-Ontology Alignment Worksheet** (Cookbook Addendum A). The assessment produces one of three outcomes: **REUSE** existing type, **EXTEND** existing type, or **CREATE NEW** canonical type. CREATE NEW requires written justification that extension is insufficient.

### Doctrine Alignment Requirements

- Every object type definition must cite its authoritative doctrine source (FM, ADP, ATP, STANAG, MIM)
- Definitions are verbatim from doctrine or explicitly annotated as derived
- Variety selection (Entity, Capability, CV, etc.) must match the doctrine concept classification
- Schema fit assessment scored across 7 weighted dimensions (see Cookbook Addendum A, Section B)
- Data scope assessment is mandatory alongside schema fit (Addendum A, Section A)

## Section 4: Governance Model

### Architecture Review Board

- **Reviews:** New object types, schema changes, link additions
- **Criteria:** Cookbook compliance, doctrine alignment, VAULTIS-A readiness
- **Authority:** Approve, request revision, or reject
- **Cadence:** Biweekly minimum

### Peer Review (Mandatory)

- Every new or modified object type requires peer review before production
- Checklist-driven (Cookbook Section 9)
- Covers: definition, variety, properties, links, quality metrics, data scope
- Reviewer cannot be the author

### DDOF Lifecycle Phases

| Phase | Name | Duration | Gate Output |
|-------|------|----------|-------------|
| 1 | Problem Framing | 3-5 days | Approved requirement + SMART statement |
| 2 | Data Provisioning | 5-10 days | Secured access to authoritative sources |
| 3 | Data Wrangling | 7-12 days | Clean data passing VAULTIS-A at 85%+ |
| 4 | Development | 15-25 days | Functional product with governance controls |
| 5 | Test and Evaluation | 7-12 days | Validated product approved by decision maker |
| 6 | Operations | Ongoing | Live product with monitoring and refresh |

**MVP Mandate:** Per Secretary of the Army priorities: MVP delivery within 30 days. Extensions require C2DAO approval with documented justification. Speed over perfection. Warfighter first.

## Section 5: VAULTIS-A Quality Framework

Every data product must be scored against these eight dimensions before advancing past DDOF Phase 3. No exceptions.

| Dimension | Target |
|-----------|--------|
| **V** -- Visible | 100% |
| **A** -- Accessible | 99% |
| **U** -- Understandable | 100% |
| **L** -- Linked | 100% |
| **T** -- Trusted | 95% |
| **I** -- Interoperable | 90% |
| **S** -- Secure | 100% |
| **A** -- Auditable | 100% |

> **Minimum Gate Score:** 85% weighted average across all eight dimensions to pass DDOF Phase 3. Products below threshold are returned for remediation with documented deficiencies.

## Section 6: Cross-Domain Architecture

> **Classification Boundary Is a First-Class Design Constraint.** Designing a data architecture and then discovering the critical data lives in a domain the consuming system cannot reach is the single most expensive failure mode in OCONUS operations. **CDS topology is an input to architecture design, not an afterthought.**

### Mandatory CDS Design Rules

- Every object type must declare its **classification ceiling** as a first-class property
- Data flow diagrams must explicitly show domain boundaries (NIPR / SIPR / JWICS)
- CDS latency and bandwidth constraints documented for each cross-domain data flow
- Authoritative source of record location (which domain) documented per object type
- Foundry cross-enclave synchronization patterns follow NCDSMO baseline product standards

```
Classification Domains
 ├── NIPR   // Unclassified operational data
 ├── SIPR   // Secret operational data
 └── JWICS  // TS/SCI intelligence data

CDS Sync Pattern (Foundry)
 ├── Source enclave → export filter → CDS guard
 ├── CDS guard → classification validation → transfer
 └── Target enclave → import pipeline → ontology merge
```

## Section 7: NATO Interoperability

USAREUR-AF is a NATO-committed theater command. Ontology design must be **NAFv4-compatible** to support coalition interoperability.

### Framework Alignment

- **NAFv4:** Architecture viewpoints and ArchiMate mapping
- **DODAF:** DIV-1/2/3 as ontology design artifacts
- **STANAGs:** 4559 (Intel), 5500 (TDL), APP-6 (Symbology)

### The Semantic Bridge

The DIV (Data and Information View) in DODAF and the corresponding NAFv4 viewpoints are the **physical instantiation of the ontology**. Good ontology design directly produces compliant architecture products. Bad ontology produces products that have to be rebuilt.

## Section 8: Implementing Documents

| Document | Purpose | Authority |
|----------|---------|-----------|
| Object Type Cookbook v2.0 | Ontology design standards, decision trees, quality metrics, peer review | CDA / ODT |
| Cookbook Addendum A | Data scope assessment, doctrine-to-ontology alignment, bitemporal modeling | CDA / ODT |
| DDOF Playbook v2.2 | 6-phase data product lifecycle with VAULTIS-A quality gates | T2COM C2DAO / HQDA CIO/G-6 / SAIS-ADD |
| Semantic Layer Instructions | Doctrine-first governance philosophy and stewardship model | CDA / ODT |
| CDS Technical Reference | Cross-domain ontology patterns and NCDSMO compliance | CDA / ODT |
| Tool Convergence Assessment | Platform consolidation onto Foundry/Vantage | CTO / ODT |
| EA Curriculum (6-part) | Enterprise architecture foundations through military application | CDA / ODT |

> **The Standard:** Ontology design is **doctrine-driven** (grounded in authoritative publications) and **EA-governed** (aligned to the theater capability map). Ontologies designed bottom-up from available data sources instead of top-down from operational requirements produce technically correct but **operationally useless** models.

---

*Operational Data Team -- HERMES Program -- USAREUR-AF*
*CUI*
*Enterprise Data Compass v1.0 -- February 2026*
