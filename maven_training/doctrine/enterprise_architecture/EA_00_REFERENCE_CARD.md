<!-- MAVEN TRAINING CORPUS — CDA REFERENCE MATERIAL
     Source: odt_workspace/docs/architecture/cda/enterprise-architecture/00-reference-card.md
     Supports: TM-30, TM-40K (Knowledge Manager), TM-40L (Software Engineer)
     Type: Enterprise Architecture
-->
---
sidebar_position: 1
title: "EA Reference Card"
---

# Enterprise Architecture — Reference Card
### Quick-access summaries and navigation

---

## The Series

| File | Topic | Key Question Answered |
|---|---|---|
| [01 — Foundation](EA_01_FOUNDATION.md) | What EA is and why it exists | "What is Enterprise Architecture?" |
| [02 — Schools of Thought](EA_02_SCHOOLS_OF_THOUGHT.md) | The three EA philosophies | "Why do EA efforts talk past each other?" |
| [03 — Artifacts and Views](EA_03_ARTIFACTS_AND_VIEWS.md) | What EA produces | "What does EA actually deliver?" |
| [04 — Governance](EA_04_GOVERNANCE.md) | How EA influences decisions | "How does EA become authoritative?" |
| [05 — Military Application](EA_05_MILITARY_APPLICATION.md) | Defense and theater context | "How does EA work at USAREUR-AF?" |

---

## Core Definitions

**Enterprise Architecture** — The discipline of making enterprise change deliberate, coherent, and governable.

**Capability** — What the enterprise needs to be able to do, independent of how or by whom.

**View** — A representation of the enterprise from a specific stakeholder perspective, addressing specific concerns.

**Governance** — The mechanisms by which EA actually influences decisions before they are made.

**Authoritative Source** — The designated system or organization that is the official source of record for a given data entity.

**Ontology** — A formal, machine-readable semantic model of what entities exist, what properties they have, and how they relate — the physical instantiation of the DIV.

---

## The Three Schools (One-Liners)

| School | Purpose | Pattern |
|---|---|---|
| **IT Design** | Plan and govern technology | App rationalization, tech standards |
| **Enterprise Integrating** | Coherence across all domains | Capability maps, cross-domain views |
| **Ecosystem Adaptation** | Build resilience and learning | Modular design, feedback loops |

Defense/theater CTO = **Integrating** primary + **Adaptation** design principle.

---

## The Minimum EA Artifact Set

1. **Capability Map** — what the enterprise does
2. **Application/System Inventory** — what systems exist
3. **Data/Information Map** — what data exists, who owns it
4. **Capability Heat Map** — where the gaps are
5. **Technology Reference Architecture** — approved platforms and patterns
6. **Roadmap** — sequenced transformation plan

---

## The Four Governance Entry Points

1. **Investment / Portfolio** — EA shapes what gets funded
2. **Solution Intake / ARB** — EA reviews what gets built
3. **Acquisition / Requirements** — EA is written into what gets procured
4. **Data / Metadata** — EA governs what data means and who owns it

---

## DODAF Quick Reference

| View Set | Focus | Most Useful Products |
|---|---|---|
| CV | Capabilities | CV-2 (taxonomy), CV-3 (phasing) |
| OV | Operations | OV-1 (concept), OV-5 (activities) |
| SV | Systems | SV-1 (interfaces), SV-6 (data exchange) |
| DIV | Data | DIV-1 (conceptual), DIV-2 (logical) |
| TV | Standards | TV-1 (profile), TV-2 (forecast) |

---

## Foundry-to-EA Mapping

| EA Concept | Foundry |
|---|---|
| Conceptual/logical data model | Ontology object types and relationships |
| Authoritative source | Dataset provenance and source tracking |
| Data integration | Pipeline Builder / Code Workbook |
| Operational view | Workshop / Slate applications |
| Data governance | Access controls, branch review, ontology review |
| Cross-domain flow | AIP Gateway / multi-instance architecture |

---

## The EA Maturity Sequence

```
0 — Foundation (charter, vocabulary, alignment)
1 — Inventory (what exists: systems, data, capabilities)
2 — Model (structure into governed views)
3 — Govern (ARB + investment/acquisition connection)
4 — Roadmap (sequenced transformation plan)
5 — Maintain (living practice, not static documents)
```

Don't skip to 4. A roadmap without an accurate inventory is fiction.

---

## Key Failure Modes

- Artifact-first (diagrams with no decision connection)
- IT-only scope (ignores process, data, people)
- No governance hook (EA is advisory, not authoritative)
- No deviation process (teams route around rigid standards)
- Unmaintained artifacts (nobody trusts stale models)
- Mixed schools (leadership wants one thing, EA delivers another)
- Roadmap without inventory (sequencing imaginary current state)

---

## One Truth About EA

> EA is only real if it shows up in investment decisions, solution reviews, acquisition requirements, data standards, and operational adoption. Everything else is documentation.
