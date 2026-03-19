# Self-Study Addendum — TM-40E: Protection Warfighting Function
## Palantir Developers Reference Library

> **NOT REQUIRED FOR QUALIFICATION.** This addendum provides curated references from the Palantir Developers YouTube channel ([@PalantirDevelopers](https://www.youtube.com/@PalantirDevelopers)) for personnel who want to deepen their MSS technical skills beyond the core curriculum. All content is publicly available.

**Companion Resource — Ontologize Channel:** [@Ontologize](https://www.youtube.com/@Ontologize) — Official Palantir training partner. 68 indexed video walkthroughs covering Foundry and AIP features. Full catalog with TM cross-references: [source_material/ontologize_youtube/README.md](../../source_material/ontologize_youtube/README.md)

---

## How to Use This Addendum

Videos are grouped by topic and ordered from foundational to advanced. Start with the group most relevant to your current work. These are not assigned — use what helps.

---

## New Doctrine References (March 2026)

The following doctrine sections were added to TM-40E this session. Review after the corresponding TM chapter:

- **Integrated Protection Picture** — Five questions the protection picture must answer at all times, derived from ADP 3-37 doctrinal logic. See TM-40E concepts guide.
- **CRM as a Data Quality Problem** — FM 5-19 Composite Risk Management process reframed as a data completeness and data quality discipline. See TM-40E concepts guide.
- **C-UAS as an Emerging Data Domain** — Counter-UAS data maturation framework including legal, tracking, and classification challenges. See TM-40E concepts guide.

---

## Group 1 — Ontology and Data Foundations for Protection

| Video | What it Covers | Relevant TM Chapter |
|---|---|---|
| *Palantir Ontology Overview* | High-level introduction to the Foundry Ontology: object types, links, and the operational data model. Essential context for understanding how CBRN events, AT assessments, and physical security data are structured in MSS. | Ch 1 |
| *How Palantir Integrates with Your Current Data Systems* | Overview of how Foundry/MSS connects to existing data systems — relevant context for understanding how AMD warning feeds, CBRN sensor data, and AT reporting flow into the protection data layer. | Ch 1 |
| *Foundry Reference Project \| Ontology* | Reference Ontology implementation — applicable to understanding how protection object types (threats, hazards, incidents, assessments) are modeled and linked across protection functional cells. | Ch 1, Ch 2 |
| *Foundry Reference Project \| Data Pipeline* | Reference data pipeline — covers dataset structure and transform conventions relevant to protection data source feeds. | Ch 1 |

---

## Group 2 — Quiver: Protection Analysis and Risk Products

| Video | What it Covers | Relevant TM Chapter |
|---|---|---|
| *Quiver \| How to Build an Analysis in Palantir Foundry* | End-to-end Quiver workbook creation. Directly applicable to building CBRN event tracking, AT assessment trending, and integrated protection picture products. | Ch 2, Ch 3 |
| *Quiver \| How to Perform Ad-Hoc Aggregations* | On-the-fly aggregations without modifying datasets. Useful for roll-up analysis of incidents by type, risk categories by severity, or FPCON history by installation. | Ch 2, Ch 4 |
| *Quiver \| How to Use Parameters in Your Analysis* | Parameter widgets for dynamic filtering. Applicable to building filtered protection products by threat type, hazard category, location, or time window. | Ch 4, Ch 9 |
| *Quiver \| Calculating KPIs for Time Series Data in Palantir Foundry* | KPI metrics from time-series data — applicable to tracking incident rates, CBRN detection event frequency, and AT vulnerability assessment trends over time. | Ch 3, Ch 4 |

---

## Group 3 — Contour: Protection Assessment Dashboards

| Video | What it Covers | Relevant TM Chapter |
|---|---|---|
| *Contour \| Building a Year Over Year Sales Dashboard* | Period-over-period comparison dashboard. The pattern applies to comparing incident rates, FPCON history, and protection posture metrics across reporting periods. | Ch 9 |

---

## Group 4 — Platform Architecture and Security

| Video | What it Covers | Relevant TM Chapter |
|---|---|---|
| *Security \| How to use Projects to Help Enable your Business to Scale* | Foundry Projects for access control governance — directly relevant to protection data compartmentation where AT, CBRN, and PMO data may have different access requirements. | Ch 1, Ch 4 |
| *Chad & Arnav \| Privacy & Security with Palantir AIP* | Privacy and security controls for AIP — relevant to protection practitioners handling sensitive threat data and AT assessment information. | Ch 4, Ch 7 |
| *Why do I need Palantir if I already have a cloud data platform?* | What Foundry provides beyond standard data capabilities — useful framing for protection officers evaluating MSS alongside legacy force protection tools. | Ch 1 |
| *Anduril: Ontology: Launchpad for Operations* | Defense-sector case study on operationalizing the Ontology — illustrates how integrated data models enable rapid protection product development across multiple functional cells. | Ch 1 |

---

## Group 5 — AI-Assisted Protection Operations

| Video | What it Covers | Relevant TM Chapter |
|---|---|---|
| *Applied AI: Scaling AI Workflows and Task Execution with AIP* | AIP multi-step analytical workflows — relevant as protection products increasingly incorporate automated threat correlation and risk pattern detection. | Ch 4, Ch 6 |
| *AIP for Medical Record Management \| Tackling VHA Healthcare Provider Burnout* | AIP applied to high-stakes document analysis with human review requirements — pattern applicable to AT assessment review workflows and CRM documentation. | Ch 2 |

---

*USAREUR-AF Operational Data Team*
