# Self-Study Addendum — TM-40A: Intelligence Warfighting Function
## Palantir Developers Reference Library

> **NOT REQUIRED FOR QUALIFICATION.** This addendum provides curated references from the Palantir Developers YouTube channel ([@PalantirDevelopers](https://www.youtube.com/@PalantirDevelopers)) for personnel who want to deepen their MSS technical skills beyond the core curriculum. All content is publicly available.

**Companion Resource — Ontologize Channel:** [@Ontologize](https://www.youtube.com/@Ontologize) — Official Palantir training partner. 68 indexed video walkthroughs covering Foundry and AIP features. Full catalog with TM cross-references: [source_material/ontologize_youtube/README.md](../../source_material/ontologize_youtube/README.md)

---

## How to Use This Addendum

Videos are grouped by topic and ordered from foundational to advanced. Start with the group most relevant to your current work. These are not assigned — use what helps.

---

## New Doctrine References (March 2026)

The following doctrine sections were added to TM-40A this session. Review after the corresponding TM chapter:

- **Intelligence Cycle Data Mapping** — FM 2-0 intelligence cycle phases mapped to MSS data capabilities and pipeline stages. See TM-40A concepts guide.
- **IPB as a Continuous Data Process** — Intelligence Preparation of the Battlefield reframed as a living MSS data workflow rather than a one-time product. See TM-40A concepts guide.
- **Classification Inheritance in Integrated Environments** — Rules for handling derivative classification when multi-INT data converges in shared MSS workspaces. See TM-40A concepts guide.

---

## Group 1 — Ontology and Data Foundations for Intelligence

| Video | What it Covers | Relevant TM Chapter |
|---|---|---|
| *Palantir Ontology Overview* | High-level introduction to the Foundry Ontology: object types, links, and the operational data model that intelligence workspaces consume. Essential context for understanding how threat ORBATs and collection data are structured. | Ch 1 |
| *Foundry Reference Project \| Ontology* | Reference implementation of a Foundry Ontology — object types, property definitions, link rules. Relevant to understanding how intelligence object types (targets, SIGACTs, NAIs) are modeled. | Ch 1, Ch 2 |
| *How Palantir Integrates with Your Current Data Systems* | Overview of how Foundry/MSS connects to existing data systems — relevant context for understanding how DCGS-A, SIGINT, and GEOINT feeds flow into the intelligence data layer. | Ch 1 |
| *Foundry Reference Project \| Data Pipeline* | Walkthrough of a reference data pipeline — covers dataset structure and transform conventions that feed intelligence analytical workspaces. | Ch 1 |
| *Deep Dive: Advanced Ontology \| DevCon 5* | Advanced Ontology patterns including object type hierarchies — relevant for intelligence analysts coordinating with TM-30 practitioners on multi-INT data models. | Ch 1, Ch 4 |

---

## Group 2 — Quiver: Intelligence Analysis and Visualization

| Video | What it Covers | Relevant TM Chapter |
|---|---|---|
| *Quiver \| How to Build an Analysis in Palantir Foundry* | End-to-end walkthrough of creating a Quiver workbook — connecting data, building charts, publishing. Directly applicable to building SIGACT trend analysis and threat pattern products. | Ch 4, Ch 7 |
| *Quiver \| How to Perform Ad-Hoc Aggregations* | On-the-fly group-by aggregations without modifying datasets. Useful for exploratory analysis of SIGACT data by type, location, or time period. | Ch 4 |
| *Quiver \| How to Navigate the Dependency Graph and Expand your Analysis* | Using Quiver's dependency graph to trace upstream data lineage — useful for verifying source data provenance in multi-INT analytical products. | Ch 4 |
| *Quiver \| How to Use Parameters in Your Analysis* | Creating parameter widgets for dynamic filtering across charts. Applicable to building filtered intelligence products by area, time window, or threat category. | Ch 4, Ch 7 |
| *Quiver \| Calculating KPIs for Time Series Data in Palantir Foundry* | Computing KPI metrics from time-series data including rolling aggregations. Directly applicable to SIGACT trend analysis and threat activity rate tracking. | Ch 4, Ch 8 |

---

## Group 3 — Geospatial and Mapping

| Video | What it Covers | Relevant TM Chapter |
|---|---|---|
| *Contour \| Building a Year Over Year Sales Dashboard* | Structuring a Contour workbook for period-over-period comparison. The YoY pattern applies to threat activity trend comparison across reporting periods — directly relevant to intelligence assessment products. | Ch 7 |
| *Anduril: Ontology: Launchpad for Operations* | Defense-sector case study on operationalizing the Ontology for complex operational environments — illustrates how integrated data models enable rapid intelligence product development. | Ch 1, Ch 4 |

---

## Group 4 — AI-Assisted Intelligence and RAG

| Video | What it Covers | Relevant TM Chapter |
|---|---|---|
| *AIP with Jeg: Adding RAG to a Simple Notes Application* | Step-by-step RAG pipeline build — relevant to intelligence document ingestion and automated report summarization. | Ch 7 |
| *Build with AIP: Semantic Search* | Semantic search capabilities within AIP — applicable to searching across intelligence reports, INTSUMs, and threat assessments by meaning rather than keyword. | Ch 4, Ch 7 |
| *Applied AI: Scaling AI Workflows and Task Execution with AIP* | AIP multi-step analytical workflows — relevant as intelligence products increasingly incorporate AI-assisted pattern detection and summarization layers. | Ch 4 |
| *Build with AIP: AIP Assist* | AIP Assist agent capabilities — applicable to configuring interactive Q&A against intelligence databases and reporting archives. | Ch 4, Ch 7 |

---

## Group 5 — Platform Security and Access Control

| Video | What it Covers | Relevant TM Chapter |
|---|---|---|
| *Security \| How to use Projects to Help Enable your Business to Scale* | Foundry Projects for access control governance — directly relevant to compartmented intelligence workspace design and multi-echelon access management. | Ch 1, Ch 6 |
| *Chad & Arnav \| Privacy & Security with Palantir AIP* | Privacy and security controls for AIP — relevant to intelligence practitioners handling classified data in AI-integrated workflows. | Ch 6 |
| *Security \| How to Debug a User's Access to a File* | Diagnostic procedure for access control issues — essential when troubleshooting intelligence workspace access for newly-credentialed analysts. | Ch 1 |

---

*USAREUR-AF Operational Data Team — UNCLASSIFIED*
