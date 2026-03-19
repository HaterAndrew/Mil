<!-- MAVEN TRAINING CORPUS — CDA REFERENCE MATERIAL
     Source: odt_workspace/docs/architecture/cda/reference/ea-vs-da.md
     Supports: all TM tracks, especially TM-40J (Program Manager), TM-40K (Knowledge Manager)
     Type: Reference
-->
---
sidebar_position: 4
title: "EA vs Data Architecture"
description: Understanding the relationship between organizational blueprints and data design
layer: architecture
category: reference
---

# Enterprise Architecture vs Data Architecture

Understanding the relationship between organizational blueprints and data design.

> **TL;DR:** Enterprise architecture sets the rules of the game; data architecture designs how data plays within them.

## Enterprise Architecture (EA)

### What It Is

Enterprise Architecture is the **holistic blueprint of the organization** -- how strategy, processes, people, systems, and technology fit together to achieve mission outcomes.

> **Primary Question EA Answers:**
> "How should the enterprise be structured to achieve its mission and evolve safely over time?"

### Scope

- Strategy and goals
- Business capabilities and processes
- Applications and platforms
- Technology infrastructure
- Governance, standards, and roadmaps

### Typical Outputs

- Capability maps
- Value streams
- Target-state architectures
- Standards and guardrails
- Investment roadmaps
- Governance models

### Key Metrics

| Dimension | Value |
|-----------|-------|
| Time Horizon | 3-10 years |
| Primary Audience | CxO |
| Focus Level | Strategic |

**In Military Terms:** EA defines how the force fights, organizes, modernizes, and governs change.

## Data Architecture (DA)

### What It Is

Data Architecture is the **intentional design of how data is structured, governed, moved, secured, and used** across the enterprise.

> **Primary Question DA Answers:**
> "How does data flow from source to decision -- correctly, securely, and at scale?"

### Scope

- Data domains and ownership
- Canonical data models / ontologies
- Schemas, object types, and semantics
- Data pipelines and transformations
- Storage patterns (lake, warehouse, graph)
- Metadata, lineage, and quality
- Access control and classification

### Typical Outputs

- Conceptual / logical / physical data models
- Ontologies and semantic layers
- Data standards and naming conventions
- Reference pipelines
- Quality rules and validation logic

### Key Metrics

| Dimension | Value |
|-----------|-------|
| Time Horizon | Continuous |
| Primary Audience | Engineers |
| Focus Level | Technical |

**In Military Terms:** DA defines how information becomes decision advantage.

## Side-by-Side Comparison

| Dimension | Enterprise Architecture | Data Architecture |
|-----------|------------------------|-------------------|
| Core focus | Entire enterprise | Data specifically |
| Primary concern | Alignment to mission and strategy | Trustworthy, usable data |
| Level | Organizational and system-of-systems | Semantic and technical |
| Outputs | Capability maps, standards, roadmaps | Models, schemas, pipelines |
| Change driver | Strategy, budget, policy | Use cases, analytics, AI |
| Failure mode | Fragmented modernization | Silos, inconsistent meaning |
| Success looks like | Coherent, governable enterprise | One version of truth at scale |

## The Relationship

*This is the part most orgs get wrong.*

> **Critical Insight:**
> **Enterprise Architecture is the parent.**
> **Data Architecture is a first-class child** -- not a subset, not a side project.

- **EA's Role:** Sets constraints and intent
- **DA's Role:** Executes those constraints in data form

| Scenario | Result |
|----------|--------|
| EA without DA | PowerPoint governance |
| DA without EA | High-velocity silos |

### A Clean Mental Model

```
Enterprise Architecture
 ├── Business Architecture
 ├── Application Architecture
 ├── Technology Architecture
 └── Data Architecture  ← semantic backbone
```

## A Blunt But Accurate Takeaway

1. If **enterprise architecture** is not grounded in **data architecture**, it will fail the moment analytics or AI matter.
2. If **data architecture** is not anchored in **enterprise architecture**, it will scale chaos faster.

> **The Winning Pattern:**
> The organizations that win treat **data architecture as the semantic execution layer of enterprise architecture** -- not a downstream ETL concern.

---

*Operational Data Team -- USAREUR-AF*
*UNCLASSIFIED // FOUO*
