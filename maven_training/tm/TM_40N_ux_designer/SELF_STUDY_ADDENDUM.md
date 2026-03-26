# Self-Study Addendum — SL 4N: UI/UX Designer
## Palantir Developers Reference Library

> **NOT REQUIRED FOR QUALIFICATION.** This addendum provides curated references from the Palantir Developers YouTube channel ([@PalantirDevelopers](https://www.youtube.com/@PalantirDevelopers)) for personnel who want to deepen their MSS technical skills beyond the core curriculum. All content is publicly available.

---

## How to Use This Addendum

Videos are grouped by topic and ordered from foundational to advanced. Start with the group most relevant to your current work or the chapter you just completed. UI/UX Designers should prioritize Groups 1 and 2 (application surfaces and Workshop patterns) before proceeding to platform context in Groups 3 and 4.

---

## Group 1 — Workshop and Application Surfaces

| Video | What it Covers | Relevant TM Chapter |
|---|---|---|
| *Foundry Reference Project \| Apps* | The application layer of the Foundry Reference Project — current recommended patterns for Workshop-based and OSDK-backed apps. Essential context for understanding the platform surfaces Designers specify against. | Ch 3 (Workshop Layout Patterns) |
| *Foundry Reference Project \| Ontology* | The Ontology layer — object types, computed properties, and how the data model drives widget data binding in Workshop applications. Designers must understand the Ontology to specify data-driven layouts. | Ch 3 (Information Architecture) |
| *Foundry Reference Project \| Structure* | Canonical Foundry project structure — helps Designers understand how application artifacts are organized, which informs handoff specifications to SWEs (SL 4L). | Ch 8 (Cross-Track Coordination) |
| *Product Launch: Build Operational Apps with Your Developer Toolkit of Choice* | Overview of Palantir's developer toolkit for building operational applications — provides Designers with vocabulary and context for the implementation platforms their designs target. | Ch 3 (Workshop Layout Patterns) |

---

## Group 2 — Ontology and Data Model Context

| Video | What it Covers | Relevant TM Chapter |
|---|---|---|
| *Palantir Ontology Overview* | High-level introduction to the Foundry Ontology: object types, links, and the operational data model. Designers bind widgets to Ontology properties — understanding the model is a prerequisite for effective information architecture. | Ch 3 (Information Architecture) |
| *Deep Dive: Advanced Ontology \| DevCon 5* | Advanced Ontology patterns including object type hierarchies and action types — relevant when designing drill-down navigation, cross-entity views, and action-triggered workflows. | Ch 3, Ch 5 (Prototyping) |
| *Functions \| Getting Started* | Introductory walkthrough of Foundry Functions — Designers should understand Functions on Objects (FOO) because they power computed values and actions that appear in Workshop widgets. | Ch 3, Ch 5 |

---

## Group 3 — User-Facing Platform Capabilities

| Video | What it Covers | Relevant TM Chapter |
|---|---|---|
| *Product Launch: Rapid Software Development with OSDK 2.0* | OSDK 2.0 release — developer experience improvements that affect the implementation feasibility of Designer specifications. Understanding OSDK capabilities helps Designers scope designs realistically. | Ch 8 (Designer-Engineer Handoff) |
| *Building with Palantir AIP: the Ontology Software Development Kit* | OSDK in action for AIP-integrated applications — practical walkthrough relevant when designing interfaces that surface AI-generated content or AIP Logic outputs. | Ch 8 |
| *Product Launch: Media, Real-Time Updates, and Expressive Compute in OSDK \| DevCon 2* | WebSocket-based real-time object updates — relevant for Designers specifying live-updating dashboards, streaming status indicators, and real-time operational displays. | Ch 3, Ch 4 (Visual Design) |
| *Anduril: Ontology: Launchpad for Operations* | Defense-sector case study of the Ontology as an operational data platform — highly relevant to understanding how USAREUR-AF WFF users consume the interfaces Designers create. | Ch 1, Ch 2 (SCD Methodology) |

---

## Group 4 — Accessibility, Security, and Field Context

| Video | What it Covers | Relevant TM Chapter |
|---|---|---|
| *Security \| How to use Projects to Help Enable your Business to Scale* | How Foundry Projects structure access governance — relevant for Designers who must understand how classification-based access control affects what different users see in the same application. | Ch 4 (Classification Marking), Ch 6 (Accessibility) |
| *Security \| How to Debug a User's Access to a File* | Diagnostic procedure for access control issues — useful context when Designer-specified views produce "access denied" for certain user groups due to CBAC boundaries. | Ch 4, Ch 6 |
| *Product Launch: Edge Embedded Ontology \| DevCon 2* | Edge-embedded Ontology for disconnected operations — context for Designers specifying field-condition interfaces that must function without continuous network connectivity (DDIL). | Ch 4 (Field Conditions) |
| *Chad & Arnav \| Privacy & Security with Palantir AIP* | Privacy and security considerations for AIP-integrated applications — relevant when designing interfaces that surface AI-generated content alongside classified operational data. | Ch 4, Ch 6 |

---

## Group 5 — Case Studies and Design Context

| Video | What it Covers | Relevant TM Chapter |
|---|---|---|
| *Ontology SDK x Lennar for Quality Inspection* | Production case study of OSDK for quality inspection workflows — real-world example of form-based data entry and status tracking designs that parallel MSS data entry patterns. | Ch 3 (Workshop Layout Patterns), Ch 5 (Prototyping) |
| *7Bridges: AIP for Automated Invoice Auditing* | Production case study of AIP-integrated automation — illustrates how AI outputs are presented to users in operational decision workflows, a pattern Designers must support. | Ch 2 (SCD Methodology), Ch 5 |
| *Code in Production: Process Orchestration x Eaton \| DevCon 4* | Production case study on workflow automation and orchestration — provides examples of multi-step operational workflows that require careful interaction design. | Ch 5 (Prototyping) |
| *Build with Palantir Developers* | Overview of the developer ecosystem and production deployment patterns — general context for understanding the implementation environment. | General |

---

*USAREUR-AF Operational Data Team*
