# Self-Study Addendum — TM-40B: Fires Warfighting Function
## Palantir Developers Reference Library

> **NOT REQUIRED FOR QUALIFICATION.** This addendum provides curated references from the Palantir Developers YouTube channel ([@PalantirDevelopers](https://www.youtube.com/@PalantirDevelopers)) for personnel who want to deepen their MSS technical skills beyond the core curriculum. All content is publicly available.

**Companion Resource — Ontologize Channel:** [@Ontologize](https://www.youtube.com/@Ontologize) — Official Palantir training partner. 68 indexed video walkthroughs covering Foundry and AIP features. Full catalog with TM cross-references: [source_material/ontologize_youtube/README.md](../../source_material/ontologize_youtube/README.md)

---

## How to Use This Addendum

Videos are grouped by topic and ordered from foundational to advanced. Start with the group most relevant to your current work. These are not assigned — use what helps.

---

## New Doctrine References (March 2026)

The following doctrine sections were added to TM-40B this session. Review after the corresponding TM chapter:

- **FSCM Data Stewardship** — Fire support coordination measure data currency, accuracy, and command authority requirements mapped to MSS workspace discipline. See TM-40B concepts guide.
- **MOE vs. MOP for Fires Assessment** — Distinguishing measures of effectiveness from measures of performance in fires assessment products. See TM-40B concepts guide.
- **D3A Data Circuit** — Decide-Detect-Deliver-Assess targeting cycle mapped to MSS data flows and pipeline stages. See TM-40B concepts guide.

---

## Group 1 — Ontology and Data Foundations for Fires

| Video | What it Covers | Relevant TM Chapter |
|---|---|---|
| *Palantir Ontology Overview* | High-level introduction to the Foundry Ontology: object types, links, and the operational data model. Essential context for understanding how targets, FSCMs, and fires assets are modeled in MSS. | Ch 1 |
| *How Palantir Integrates with Your Current Data Systems* | Overview of how Foundry/MSS connects to existing data systems — relevant context for understanding how AFATDS, IBCS, and AMD system feeds flow into the MSS fires data layer. | Ch 1 |
| *Foundry Reference Project \| Ontology* | Reference Ontology implementation — object types, properties, link rules. Applicable to understanding the fires data model and target-to-asset linkages. | Ch 1, Ch 2 |
| *Foundry Reference Project \| Data Pipeline* | Reference data pipeline walkthrough — covers dataset structure and transform conventions that feed fires analytical products. | Ch 1 |

---

## Group 2 — Quiver: Fires Analysis and Targeting Products

| Video | What it Covers | Relevant TM Chapter |
|---|---|---|
| *Quiver \| How to Build an Analysis in Palantir Foundry* | End-to-end Quiver workbook creation. Directly applicable to building target tracking, BDA tracking, and ammunition consumption analysis products. | Ch 2, Ch 8 |
| *Quiver \| How to Perform Ad-Hoc Aggregations* | On-the-fly aggregations without modifying datasets. Useful for roll-up analysis of BDA data, fires missions by type, or Class V consumption by unit. | Ch 8 |
| *Quiver \| How to Use Parameters in Your Analysis* | Parameter widgets for dynamic filtering. Applicable to building filtered fires products by target category, time window, or engagement authority. | Ch 2, Ch 8 |
| *Quiver \| Calculating KPIs for Time Series Data in Palantir Foundry* | KPI metrics from time-series data — applicable to fires rate analysis, ammunition consumption trending, and engagement timeline tracking. | Ch 5, Ch 8 |

---

## Group 3 — Contour: Fires Assessment Dashboards

| Video | What it Covers | Relevant TM Chapter |
|---|---|---|
| *Contour \| Building a Year Over Year Sales Dashboard* | Period-over-period comparison dashboard. The pattern applies directly to fires assessment products comparing BDA rates, target attrition, and fires effectiveness across operational phases. | Ch 8 |

---

## Group 4 — Platform Architecture

| Video | What it Covers | Relevant TM Chapter |
|---|---|---|
| *Why do I need Palantir if I already have a cloud data platform?* | What Foundry provides beyond standard data capabilities — useful framing for fires officers comparing MSS to legacy fires management tools. | Ch 1 |
| *Deep Dive: Optimizing Data Pipelines with Iceberg Tables and Lightweight Compute \| DevCon 4* | Pipeline optimization for high-volume data — applicable when fires data pipelines grow to include high-frequency sensor feeds and C-RAM tracking data. | Ch 6 |
| *Platform APIs x SLB for Digital Sustainability* | Foundry Platform API integration — applicable to fires officers coordinating with TM-40L/40H on automating fires data pipeline feeds from AFATDS and IBCS. | Ch 1 |

---

## Group 5 — AI and Automation for Fires

| Video | What it Covers | Relevant TM Chapter |
|---|---|---|
| *Applied AI: Scaling AI Workflows and Task Execution with AIP* | AIP multi-step analytical workflows — relevant as fires assessment products increasingly incorporate automated BDA synthesis and target pattern detection. | Ch 8 |
| *Anduril: Ontology: Launchpad for Operations* | Defense-sector case study on operationalizing the Ontology — illustrates how a well-designed data model enables rapid fires product development in a complex operational environment. | Ch 1, Ch 7 |

---

*USAREUR-AF Operational Data Team*
