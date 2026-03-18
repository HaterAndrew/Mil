# Self-Study Addendum — TM-50G: Advanced Operations Research and Systems Analysis
## Palantir Developers Reference Library

> **NOT REQUIRED FOR QUALIFICATION.** This addendum provides curated references from the Palantir Developers YouTube channel ([@PalantirDevelopers](https://www.youtube.com/@PalantirDevelopers)) for personnel who want to deepen their MSS technical skills beyond the core curriculum. All content is publicly available.

**Companion Resource — Ontologize Channel:** [@Ontologize](https://www.youtube.com/@Ontologize) — Official Palantir training partner. 68 indexed video walkthroughs covering Foundry and AIP features. Full catalog with TM cross-references: [source_material/ontologize_youtube/README.md](../../source_material/ontologize_youtube/README.md)

---

## How to Use This Addendum

Videos are grouped by topic and ordered from foundational to advanced. TM-40G self-study references are included here for completeness — analysts who completed TM-40G recently may skip Group 1 and Group 2. Start with Groups 3 and 4 for content specific to TM-50G advanced topics.

---

## New Doctrine References (March 2026)

The following doctrine sections were added to TM-50G this session. Review after the corresponding TM chapter:

- **MOE/MOP Assessment at Theater Level** — Theater-level measures of effectiveness and performance for GO/SES analytical products. See TM-50G concepts guide.
- **CARVER Scoring (Multi-Echelon)** — CARVER methodology applied to multi-echelon risk prioritization and Pareto optimization inputs. See TM-50G concepts guide.
- **Force Ratio Computation (Advanced)** — Force ratio integration with Bayesian readiness models and network vulnerability analysis. See TM-50G concepts guide.

---

## Group 1 — Quiver: Building and Navigating Analyses (from TM-40G)

| Video | What it Covers | Relevant TM Chapter |
|---|---|---|
| *Quiver \| How to Build an Analysis in Palantir Foundry* | End-to-end walkthrough of creating a Quiver workbook from scratch. | TM-40G Ch 8 |
| *Quiver \| How to Perform Ad-Hoc Aggregations* | On-the-fly group-by aggregations without modifying underlying pipelines. | TM-40G Ch 8 |
| *Quiver \| How to Navigate the Dependency Graph and Expand your Analysis* | Tracing upstream data lineage and extending analyses in Quiver. | TM-40G Ch 8 |
| *Quiver \| How to Use Parameters in Your Analysis* | Parameter widgets for dynamic filtering across Quiver charts. | TM-40G Ch 8 |
| *Quiver \| Calculating KPIs for Time Series Data in Palantir Foundry* | KPI metrics from time-series data including rolling aggregations. | TM-40G Ch 4, Ch 8 |

---

## Group 2 — Contour and Dashboard Construction (from TM-40G)

| Video | What it Covers | Relevant TM Chapter |
|---|---|---|
| *Contour \| Building a Year Over Year Sales Dashboard* | Period-over-period comparison patterns in Contour for executive audiences. | TM-40G Ch 8 |

---

## Group 3 — Platform Architecture and Data Foundations

| Video | What it Covers | Relevant TM Chapter |
|---|---|---|
| *How Palantir Integrates with Your Current Data Systems* | How Foundry/MSS connects to existing Army data systems — context for ORSA data layer design. | TM-40G Ch 2, Ch 8 |
| *Why do I need Palantir if I already have a cloud data platform?* | What Foundry provides beyond standard cloud analytics — useful framing for senior practitioners explaining MSS value to leadership. | TM-40G Ch 1 |
| *Palantir Ontology Overview* | High-level Ontology introduction: object types, links, and operational data model. | TM-40G Ch 2 |
| *Foundry Reference Project \| Data Pipeline* | Reference data pipeline implementation in Foundry — Pipeline Builder patterns and transform conventions. | TM-40G Ch 2 |
| *Foundry Reference Project \| Ontology* | Reference Ontology implementation with object types, property definitions, and link rules. | TM-40G Ch 2 |
| *Platform APIs x SLB for Digital Sustainability* | Using Foundry Platform APIs to integrate external data and automate workflows. | Ch 8 |
| *Deep Dive: Optimizing Data Pipelines with Iceberg Tables and Lightweight Compute \| DevCon 4* | Foundry Iceberg table format and lightweight compute for high-volume pipeline optimization — relevant to persistent ORSA analytical environments with recurring ETL pipelines. | Ch 8 |
| *Deep Dive: Advanced Ontology \| DevCon 5* | Advanced Ontology patterns including object type hierarchies, action types, and cross-domain entity linking — foundational to Bayesian and causal models that require a structured operational data model. | Ch 4, Ch 8 |
| *Anduril: Ontology: Launchpad for Operations* | Case study on operationalizing the Palantir Ontology as a semantic layer for complex operational environments. | TM-40G Ch 1, Ch 2 |

---

## Group 4 — AI, Advanced Workflows, and Strategic Platform

| Video | What it Covers | Relevant TM Chapter |
|---|---|---|
| *Applied AI: Scaling AI Workflows and Task Execution with AIP* | How AIP orchestrates multi-step analytical workflows and automates task routing — directly relevant to designing persistent OR capability where recurring analytical cycles are automated rather than rebuilt manually. | Ch 8 |
| *Deep Dive: Interoperability at Scale with the Multimodal Data Plane \| DevCon 5* | How Foundry handles interoperability across heterogeneous data sources and modalities at scale — relevant for senior ORSA practitioners designing theater-level analytical environments that span multiple classification domains and data systems. | Ch 8 |
| *Building Enterprise Autonomy with Shyam Sankar, CTO* | Palantir CTO perspective on the trajectory toward enterprise autonomy — strategic context for ORSA practitioners advising leadership on where AI-enabled decision support is heading. | Ch 7 |
| *Product Launch: Hivemind \| DevCon 5* | Palantir's Hivemind product for multi-domain decision support and autonomous task execution — relevant to ORSA analysts integrating AI decision-support products with commander workflows. | Ch 7 |
| *Akshay Krishnaswamy Opening Remarks \| DevCon 5* | Strategic overview of Palantir's operational AI direction — useful context for senior ORSA practitioners briefing leadership on the MSS roadmap and capability trajectory. | Ch 7 |

---

*USAREUR-AF Operational Data Team — UNCLASSIFIED*
