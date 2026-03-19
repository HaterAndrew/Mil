# Self-Study Addendum — TM-40G: Operations Research and Systems Analysis
## Palantir Developers Reference Library

> **NOT REQUIRED FOR QUALIFICATION.** This addendum provides curated references from the Palantir Developers YouTube channel ([@PalantirDevelopers](https://www.youtube.com/@PalantirDevelopers)) for personnel who want to deepen their MSS technical skills beyond the core curriculum. All content is publicly available.

**Companion Resource — Ontologize Channel:** [@Ontologize](https://www.youtube.com/@Ontologize) — Official Palantir training partner. 68 indexed video walkthroughs covering Foundry and AIP features. Full catalog with TM cross-references: [source_material/ontologize_youtube/README.md](../../source_material/ontologize_youtube/README.md)

---

## How to Use This Addendum

Videos are grouped by topic and ordered from foundational to advanced. Start with the group most relevant to your current work. These are not assigned — use what helps.

---

## New Doctrine References (March 2026)

The following doctrine sections were added to TM-40G this session. Review after the corresponding TM chapter:

- **MOE/MOP Assessment Framework** — Measures of effectiveness and measures of performance for ORSA analytical products. See TM-40G concepts guide.
- **CARVER Scoring** — Target/risk prioritization methodology applied to analytical product design. See TM-40G concepts guide.
- **Force Ratio Computation** — Standardized force ratio calculations from MSS data for COA comparison. See TM-40G concepts guide.

---

## Group 1 — Quiver: Building and Navigating Analyses

| Video | What it Covers | Relevant TM Chapter |
|---|---|---|
| *Quiver \| How to Build an Analysis in Palantir Foundry* | End-to-end walkthrough of creating a Quiver workbook from scratch: connecting data, building charts, publishing. Start here before your first Quiver build. | Ch 8 |
| *Quiver \| How to Perform Ad-Hoc Aggregations* | Performing on-the-fly group-by aggregations (sum, count, percentile) without modifying underlying datasets or pipelines. Useful for exploratory rollup of simulation outputs. | Ch 8 |
| *Quiver \| How to Navigate the Dependency Graph and Expand your Analysis* | Using Quiver's dependency graph to trace upstream data lineage, diagnose broken chart connections, and extend an analysis by branching from existing nodes. | Ch 8 |
| *Quiver \| How to Use Parameters in Your Analysis* | Creating and wiring parameter widgets (dropdowns, date pickers) to drive dynamic filtering across charts in a Quiver workbook. | Ch 8 |
| *Quiver \| Calculating KPIs for Time Series Data in Palantir Foundry* | Computing and displaying KPI metrics from time-series data including rolling aggregations and threshold-based indicators. Directly applicable to readiness forecast dashboards. | Ch 4, Ch 8 |

---

## Group 2 — Contour: Dashboard Construction

| Video | What it Covers | Relevant TM Chapter |
|---|---|---|
| *Contour \| Building a Year Over Year Sales Dashboard* | Structuring a Contour workbook for period-over-period comparison with calculated delta fields, reference lines, and executive-ready layout. The YoY pattern applies directly to readiness trend and COA comparison products. | Ch 8 |

---

## Group 3 — Platform Architecture and Data Foundations

| Video | What it Covers | Relevant TM Chapter |
|---|---|---|
| *How Palantir Integrates with Your Current Data Systems* | Overview of how Foundry/MSS connects to existing Army data systems — relevant context for understanding how operational feeds (DRRS, logistics, training) flow into the ORSA data layer. | Ch 2 |
| *Why do I need Palantir if I already have a cloud data platform?* | Addresses the question of what Foundry provides beyond standard data warehouse/cloud analytics capabilities — useful framing for ORSA analysts new to MSS. | Ch 1, Ch 2 |
| *Palantir Ontology Overview* | High-level introduction to the Foundry Ontology: object types, links, and the operational data model that ORSA analytical products consume. | Ch 2 |
| *Foundry Reference Project \| Data Pipeline* | Walkthrough of a reference data pipeline implementation in Foundry — covers Pipeline Builder patterns, dataset structure, and transform conventions that feed Code Workspace analysis. | Ch 2 |
| *Foundry Reference Project \| Ontology* | Reference implementation of a Foundry Ontology — object types, property definitions, link rules, and how the Ontology connects to downstream Workshop and analytical products. | Ch 2 |
| *Platform APIs x SLB for Digital Sustainability* | Demonstrates using Foundry Platform APIs to integrate external data systems and automate workflows — applicable to ORSA analysts coordinating with TM-40L/40H for productionizing analytical pipelines. | Ch 2 |

---

## Group 4 — AI and Advanced Workflows

| Video | What it Covers | Relevant TM Chapter |
|---|---|---|
| *Applied AI: Scaling AI Workflows and Task Execution with AIP* | How Palantir AIP orchestrates multi-step analytical workflows and integrates AI-generated outputs into operational decision products — relevant as ORSA products increasingly incorporate automated synthesis layers. | Ch 8 |
| *Deep Dive: Optimizing Data Pipelines with Iceberg Tables and Lightweight Compute \| DevCon 4* | Foundry Iceberg table format and lightweight compute for high-volume pipeline optimization — applicable when the ORSA data layer grows to include high-frequency readiness or logistics feeds. | Ch 2 |
| *Deep Dive: Advanced Ontology \| DevCon 5* | Advanced Ontology patterns including object type hierarchies and action types — relevant for ORSA analysts coordinating with TM-40H / TM-30 practitioners on the data model supporting cross-domain analysis. | Ch 2 |
| *Anduril: Ontology: Launchpad for Operations* | Case study on operationalizing the Palantir Ontology as the semantic layer for a complex operational environment — illustrates how a well-designed Ontology enables rapid analytical product development. | Ch 1, Ch 2 |

---

*USAREUR-AF Operational Data Team — UNCLASSIFIED*
