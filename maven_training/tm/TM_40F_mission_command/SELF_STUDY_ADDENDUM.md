# Self-Study Addendum — TM-40F: Mission Command Warfighting Function
## Palantir Developers Reference Library

> **NOT REQUIRED FOR QUALIFICATION.** This addendum provides curated references from the Palantir Developers YouTube channel ([@PalantirDevelopers](https://www.youtube.com/@PalantirDevelopers)) for personnel who want to deepen their MSS technical skills beyond the core curriculum. All content is publicly available.

**Companion Resource — Ontologize Channel:** [@Ontologize](https://www.youtube.com/@Ontologize) — Official Palantir training partner. 68 indexed video walkthroughs covering Foundry and AIP features. Full catalog with TM cross-references: [source_material/ontologize_youtube/README.md](../../source_material/ontologize_youtube/README.md)

---

## How to Use This Addendum

Videos are grouped by topic and ordered from foundational to advanced. Start with the group most relevant to your current work. These are not assigned — use what helps.

---

## New Doctrine References (March 2026)

The following doctrine sections were added to TM-40F this session. Review after the corresponding TM chapter:

- **MOE vs. MOP Assessment Design** — Distinguishing measures of effectiveness from measures of performance for assessment product design on MSS. See TM-40F concepts guide.
- **CCIR Threshold Translation** — Procedure for converting commander's CCIRs into MSS-monitorable data thresholds for continuous monitoring. See TM-40F concepts guide.
- **Staff Data Ownership Model** — Data stewardship responsibilities by staff section (S1–S6) and the cross-staff data dependency framework. See TM-40F concepts guide.

---

## Group 1 — Ontology and Data Foundations for Mission Command

| Video | What it Covers | Relevant TM Chapter |
|---|---|---|
| *Palantir Ontology Overview* | High-level introduction to the Foundry Ontology: object types, links, and the operational data model. Essential context for understanding how the COP, readiness data, and staff products are structured in MSS. | Ch 1, Ch 7 |
| *How Palantir Integrates with Your Current Data Systems* | Overview of how Foundry/MSS connects to existing data systems — relevant context for understanding how DTMS, GCSS-Army, IPPS-A, and other source feeds populate the staff operational picture. | Ch 1 |
| *Foundry Reference Project \| Ontology* | Reference Ontology implementation — applicable to understanding the data model that backs cross-staff dashboards and COP products. | Ch 1, Ch 7 |
| *Foundry Reference Project \| Apps* | Reference implementation of Workshop applications connected to an Ontology — directly relevant to the pre-built Workshop products mission command practitioners operate daily. | Ch 7 |

---

## Group 2 — Quiver: Staff Analysis and Assessment Products

| Video | What it Covers | Relevant TM Chapter |
|---|---|---|
| *Quiver \| How to Build an Analysis in Palantir Foundry* | End-to-end Quiver workbook creation. Applicable to building readiness tracking, training completion, and operational assessment products for the BUA cycle. | Ch 7, Ch 8 |
| *Quiver \| How to Perform Ad-Hoc Aggregations* | On-the-fly aggregations without modifying datasets. Useful for exploratory analysis of readiness data by unit, personnel fill by MOS, or training completion rates. | Ch 7, Ch 8 |
| *Quiver \| How to Use Parameters in Your Analysis* | Parameter widgets for dynamic filtering. Applicable to building commander-facing products filterable by unit, time period, or readiness threshold. | Ch 6, Ch 8 |
| *Quiver \| Calculating KPIs for Time Series Data in Palantir Foundry* | KPI metrics from time-series data — directly applicable to readiness trend dashboards, personnel strength tracking, and MOE/MOP assessment products. | Ch 8 |

---

## Group 3 — Contour: Command Assessment Dashboards

| Video | What it Covers | Relevant TM Chapter |
|---|---|---|
| *Contour \| Building a Year Over Year Sales Dashboard* | Period-over-period comparison dashboard. The pattern applies directly to readiness trend comparison, training progression tracking, and phase-over-phase operational assessment products. | Ch 8 |

---

## Group 4 — Platform Architecture and COP Design

| Video | What it Covers | Relevant TM Chapter |
|---|---|---|
| *Why do I need Palantir if I already have a cloud data platform?* | What Foundry provides beyond standard data capabilities — useful framing for S3/XO officers understanding why MSS replaces slide-driven staff products. | Ch 1 |
| *Anduril: Ontology: Launchpad for Operations* | Defense-sector case study on operationalizing the Ontology — illustrates how integrated data models enable the shared understanding that ADP 6-0 requires for Mission Command. | Ch 1, Ch 7 |
| *Building Enterprise Autonomy with Shyam Sankar, CTO* | Strategic framing on enterprise AI autonomy — relevant context for Mission Command practitioners preparing for AI-augmented planning environments like Thunderforge. | Ch 1 |
| *Deep Dive: Advanced Ontology \| DevCon 5* | Advanced Ontology patterns — useful for Mission Command practitioners coordinating with TM-30 builders on cross-staff COP data models. | Ch 7 |

---

## Group 5 — AI and Decision Support

| Video | What it Covers | Relevant TM Chapter |
|---|---|---|
| *Applied AI: Scaling AI Workflows and Task Execution with AIP* | AIP multi-step analytical workflows — relevant as MDMP and assessment products increasingly incorporate AI-assisted data synthesis and decision support layers. | Ch 3, Ch 8 |
| *Build with AIP: AIP Assist* | AIP Assist interactive capabilities — applicable to configuring AI-assisted staff Q&A against readiness data, CCIR status, and operational reporting archives. | Ch 6, Ch 7 |
| *AIP Now: Dynamic Scheduling* | AIP-driven dynamic scheduling — applicable to battle rhythm optimization and staff task management. | Ch 4 |

---

*USAREUR-AF Operational Data Team*
