# Self-Study Addendum — SL 4D: Sustainment Warfighting Function
## Palantir Developers Reference Library

> **NOT REQUIRED FOR QUALIFICATION.** This addendum provides curated references from the Palantir Developers YouTube channel ([@PalantirDevelopers](https://www.youtube.com/@PalantirDevelopers)) for personnel who want to deepen their MSS technical skills beyond the core curriculum. All content is publicly available.

**Companion Resource — Ontologize Channel:** [@Ontologize](https://www.youtube.com/@Ontologize) — Official Palantir training partner. 68 indexed video walkthroughs covering Foundry and AIP features. Full catalog with TM cross-references: [source_material/ontologize_youtube/README.md](../../source_material/ontologize_youtube/README.md)

---

## How to Use This Addendum

Videos are grouped by topic and ordered from foundational to advanced. Start with the group most relevant to your current work. These are not assigned — use what helps.

---

## New Doctrine References (March 2026)

The following doctrine sections were added to TM-40D this session. Review after the corresponding TM chapter:

- **Supply Chain Velocity and Throughput** — ADP 4-0 sustainment principles translated to measurable supply chain data metrics in MSS. See TM-40D concepts guide.
- **Readiness Trend Analysis** — Predictive sustainment using C-rating trend data and maintenance backlog rates for combat power forecasting. See TM-40D concepts guide.
- **Distribution Feedback Loop** — Push vs. pull logistics data requirements and the MSS distribution management data cycle. See TM-40D concepts guide.

---

## Group 1 — Ontology and Data Foundations for Sustainment

| Video | What it Covers | Relevant TM Chapter |
|---|---|---|
| *Palantir Ontology Overview* | High-level introduction to the Foundry Ontology: object types, links, and the operational data model. Essential context for understanding how supply, maintenance, and personnel data are structured in MSS. | Ch 1 |
| *How Palantir Integrates with Your Current Data Systems* | Overview of how Foundry/MSS connects to existing data systems — relevant context for understanding how GCSS-Army, SAMS-E, and IPPS-A feeds flow into the sustainment data layer. | Ch 1 |
| *Foundry Reference Project \| Ontology* | Reference Ontology implementation — applicable to understanding how sustainment object types (supply items, work orders, requisitions, personnel) are modeled and linked. | Ch 1, Ch 2 |
| *Foundry Reference Project \| Data Pipeline* | Reference data pipeline — covers dataset structure and transform conventions relevant to sustainment source system feeds. | Ch 1 |

---

## Group 2 — Quiver: Sustainment Analysis and LOGSTAT Products

| Video | What it Covers | Relevant TM Chapter |
|---|---|---|
| *Quiver \| How to Build an Analysis in Palantir Foundry* | End-to-end Quiver workbook creation. Directly applicable to building supply status dashboards, maintenance readiness trackers, and LOGSTAT compilation products. | Ch 2, Ch 3 |
| *Quiver \| How to Perform Ad-Hoc Aggregations* | On-the-fly aggregations without modifying datasets. Useful for roll-up analysis of supply status by class, readiness rates by unit, or maintenance backlog by equipment type. | Ch 2, Ch 3 |
| *Quiver \| How to Use Parameters in Your Analysis* | Parameter widgets for dynamic filtering. Applicable to building filtered sustainment products by supply class, unit, time window, or readiness threshold. | Ch 2, Ch 9 |
| *Quiver \| Calculating KPIs for Time Series Data in Palantir Foundry* | KPI metrics from time-series data — directly applicable to readiness trend dashboards, Days of Supply forecasting, and maintenance backlog rate tracking. | Ch 3, Ch 9 |

---

## Group 3 — Contour: Sustainment Assessment Dashboards

| Video | What it Covers | Relevant TM Chapter |
|---|---|---|
| *Contour \| Building a Year Over Year Sales Dashboard* | Period-over-period comparison dashboard. The pattern applies directly to comparing readiness rates, supply consumption, and equipment availability across reporting periods or exercises. | Ch 9 |

---

## Group 4 — Supply Chain and Distribution Patterns

| Video | What it Covers | Relevant TM Chapter |
|---|---|---|
| *AIP Now: Material Harmonization* | AIP applied to supply chain material harmonization — directly relevant to Class IX parts standardization and supply catalog deconfliction in the sustainment data layer. | Ch 2 |
| *Building with Palantir AIP: Procurement* | AI-powered procurement automation — applicable to sustainment logistics and requisition workflow optimization. | Ch 2, Ch 4 |
| *Chad & Agathe \| How Palantir Powers AI Automation Across Procurement* | Procurement AI automation at scale — operational workflow pattern applicable to USAREUR-AF sustainment operations. | Ch 2, Ch 4 |

---

## Group 5 — Platform Architecture

| Video | What it Covers | Relevant TM Chapter |
|---|---|---|
| *Why do I need Palantir if I already have a cloud data platform?* | What Foundry provides beyond standard data capabilities — useful framing for sustainment officers comparing MSS to legacy logistics management tools. | Ch 1 |
| *Deep Dive: Optimizing Data Pipelines with Iceberg Tables and Lightweight Compute \| DevCon 4* | Pipeline optimization for high-volume data — applicable when sustainment data pipelines grow to include high-frequency GCSS-Army transaction feeds. | Ch 1 |
| *Anduril: Ontology: Launchpad for Operations* | Defense-sector case study on operationalizing the Ontology — illustrates how integrated data models enable rapid sustainment product development across the formation. | Ch 1 |

---

*USAREUR-AF Operational Data Team*
