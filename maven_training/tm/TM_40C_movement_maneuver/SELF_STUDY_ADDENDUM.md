# Self-Study Addendum — SL 4C: Movement and Maneuver Warfighting Function
## Palantir Developers Reference Library

> **NOT REQUIRED FOR QUALIFICATION.** This addendum provides curated references from the Palantir Developers YouTube channel ([@PalantirDevelopers](https://www.youtube.com/@PalantirDevelopers)) for personnel who want to deepen their MSS technical skills beyond the core curriculum. All content is publicly available.

**Companion Resource — Ontologize Channel:** [@Ontologize](https://www.youtube.com/@Ontologize) — Official Palantir training partner. 68 indexed video walkthroughs covering Foundry and AIP features. Full catalog with TM cross-references: [source_material/ontologize_youtube/README.md](../../source_material/ontologize_youtube/README.md)

---

## How to Use This Addendum

Videos are grouped by topic and ordered from foundational to advanced. Start with the group most relevant to your current work. These are not assigned — use what helps.

---

## New Doctrine References (March 2026)

The following doctrine sections were added to TM-40C this session. Review after the corresponding TM chapter:

- **Tempo and Information Speed** — ADP 3-0 tempo principles mapped to MSS information latency and combined arms workspace currency requirements. See TM-40C concepts guide.
- **OAKOC as a Data Framework** — Observation and fields of fire, Avenues of approach, Key terrain, Obstacles, Cover and concealment translated to MSS data layer requirements. See TM-40C concepts guide.
- **Combined Arms Synchronization Failure Modes** — Where M&M synchronization breaks down due to data latency, stale graphics, and BFT misinterpretation. See TM-40C concepts guide.

---

## Group 1 — Ontology and Data Foundations for M&M

| Video | What it Covers | Relevant TM Chapter |
|---|---|---|
| *Palantir Ontology Overview* | High-level introduction to the Foundry Ontology: object types, links, and the operational data model. Essential context for understanding how operational graphics, route data, and force tracking are modeled in MSS. | Ch 1 |
| *How Palantir Integrates with Your Current Data Systems* | Overview of how Foundry/MSS connects to existing data systems — relevant context for understanding how JBC-P, CPCE, and engineer reporting feeds flow into the M&M data layer. | Ch 1 |
| *Foundry Reference Project \| Ontology* | Reference Ontology implementation — applicable to understanding how maneuver object types (units, routes, obstacles, graphics) are structured and linked. | Ch 1, Ch 2 |
| *Foundry Reference Project \| Data Pipeline* | Reference data pipeline — covers dataset structure relevant to understanding the combined arms data feeds that populate M&M workspaces. | Ch 1 |

---

## Group 2 — Quiver: Maneuver Analysis and Operational Products

| Video | What it Covers | Relevant TM Chapter |
|---|---|---|
| *Quiver \| How to Build an Analysis in Palantir Foundry* | End-to-end Quiver workbook creation. Applicable to building route status tracking, obstacle clearance monitoring, and force disposition analysis products. | Ch 3, Ch 11 |
| *Quiver \| How to Perform Ad-Hoc Aggregations* | On-the-fly aggregations without modifying datasets. Useful for roll-up analysis of phase line crossing times, route usage by unit, or obstacle status by sector. | Ch 8, Ch 11 |
| *Quiver \| How to Use Parameters in Your Analysis* | Parameter widgets for dynamic filtering. Applicable to building filtered M&M products by phase, sector, unit, or time window. | Ch 2, Ch 11 |
| *Quiver \| Calculating KPIs for Time Series Data in Palantir Foundry* | KPI metrics from time-series data — applicable to tracking force movement rates, BFT update intervals, and route capacity utilization over time. | Ch 8, Ch 11 |

---

## Group 3 — Contour: Operational Assessment Dashboards

| Video | What it Covers | Relevant TM Chapter |
|---|---|---|
| *Contour \| Building a Year Over Year Sales Dashboard* | Period-over-period comparison dashboard. The pattern applies to comparing operational tempo, movement rates, and task completion across phases or exercises. | Ch 11 |

---

## Group 4 — Platform Architecture and Real-Time Data

| Video | What it Covers | Relevant TM Chapter |
|---|---|---|
| *Why do I need Palantir if I already have a cloud data platform?* | What Foundry provides beyond standard data capabilities — useful framing for S3/G3 officers evaluating MSS alongside legacy C2 systems. | Ch 1 |
| *Deep Dive: Optimizing Data Pipelines with Iceberg Tables and Lightweight Compute \| DevCon 4* | Pipeline optimization for high-volume data — applicable when M&M data pipelines process high-frequency BFT position updates and sensor feeds during operations. | Ch 8 |
| *Anduril: Ontology: Launchpad for Operations* | Defense-sector case study on operationalizing the Ontology — illustrates how integrated data models enable combined arms decision-making in complex operational environments. | Ch 1, Ch 5 |

---

## Group 5 — AI and Automation

| Video | What it Covers | Relevant TM Chapter |
|---|---|---|
| *Applied AI: Scaling AI Workflows and Task Execution with AIP* | AIP multi-step analytical workflows — relevant as M&M products increasingly incorporate automated route analysis and force disposition pattern detection. | Ch 3, Ch 8 |
| *AIP Now: Dynamic Scheduling* | AIP-driven dynamic scheduling and optimization — applicable to movement planning and convoy scheduling use cases. | Ch 3, Ch 4 |

---

*USAREUR-AF Operational Data Team*
