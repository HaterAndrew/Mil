# Self-Study Addendum — TM-40L Software Engineer
## Palantir Developers Reference Library

> **NOT REQUIRED FOR QUALIFICATION.** This addendum provides curated references from the Palantir Developers YouTube channel ([@PalantirDevelopers](https://www.youtube.com/@PalantirDevelopers)) for personnel who want to deepen their MSS technical skills beyond the core curriculum. All content is publicly available.

**Companion Resource — Ontologize Channel:** [@Ontologize](https://www.youtube.com/@Ontologize) — Official Palantir training partner. 68 indexed video walkthroughs covering Foundry and AIP features. Full catalog with TM cross-references: [source_material/ontologize_youtube/README.md](../../source_material/ontologize_youtube/README.md)

---

## How to Use This Addendum

Videos are grouped by topic and ordered from foundational to advanced within each group. Start with the group most relevant to your current work or the chapter you just completed. Selected videos are also cited inline within TM-40L where content most directly reinforces a specific section.

---

## Code Repository Fundamentals

| Video | What it Covers | Relevant TM Chapter |
|---|---|---|
| *Code Repositories \| How to Write Data Transformations in Palantir Foundry* | Core procedure for writing data transforms in Foundry Code Repositories — the foundation of all pipeline work on MSS | Ch 4 (Platform SDK) |
| *Code Repositories \| How to Write Incremental Data Transforms in Palantir Foundry* | Incremental transform pattern using watermarks to process only new or changed data — reduces compute cost vs. full-dataset rewrites | Ch 4 (Platform SDK) |
| *Code Repositories \| How to Create a Python Library in Palantir Foundry* | How to package shared transform logic as a reusable Python library within Foundry | Ch 4 (Platform SDK) |
| *Code Repositories \| How to Consume a Library in Palantir Foundry* | Importing and using a Foundry Python library in a transform or pipeline | Ch 4 (Platform SDK) |
| *Code Repositories \| How to Parse Excel Files into a Usable Dataset in Palantir Foundry* | Ingesting and parsing Excel files into Foundry datasets — common for feeding data from external Army reporting tools | Ch 4 (Platform SDK) |
| *Code Repositories \| How to Use Data Expectations in Palantir Foundry* | Foundry's built-in Data Expectations feature for data quality assertions within a pipeline | Ch 8 (CI/CD) |
| *Code Repositories \| How to Unit Test PySpark in Palantir Foundry* | PySpark unit testing patterns applicable to both transform pipelines and Python-based FOO | Ch 5 / Ch 8 |
| *Code Repositories \| Reviewing Code and Best Practices* | Code review standards within Foundry repositories | Ch 8 (CI/CD) |
| *Code Repositories \| Development Process and Pipeline Craftsmanship in Palantir Foundry* | Full development lifecycle for Foundry code resources — branching strategy, PR discipline, promotion | Ch 8 (CI/CD) |
| *Code Repositories \| Best Practices for Creating Pull Requests in Palantir Foundry* | PR best practices in Foundry code repositories, reinforcing the C2DAO code review workflow | Ch 8 (CI/CD) |

---

## Functions on Objects (FOO)

| Video | What it Covers | Relevant TM Chapter |
|---|---|---|
| *Functions \| Getting Started* | Introductory walkthrough of Foundry Functions — repository structure, basic function authoring, Ontology integration | Ch 5 (FOO) |
| *Functions \| Unit Testing Functions on Objects in Palantir Foundry* | Unit testing patterns for FOO, including mock object construction and Jest test setup | Ch 5 (FOO) |
| *Functions \| How to Locate and Edit Objects from your Ontology in Foundry* | How to programmatically locate and interact with Ontology Objects in a code context | Ch 5 / Ch 2 |

---

## OSDK and Platform SDK

| Video | What it Covers | Relevant TM Chapter |
|---|---|---|
| *Product Launch: Rapid Software Development with OSDK 2.0* | OSDK 2.0 release — developer experience improvements, simplified client setup, improved TypeScript type generation | Ch 2 (OSDK Fundamentals) |
| *Product Launch: Build Operational Apps with Your Developer Toolkit of Choice* | Overview of Palantir's developer toolkit for building operational applications | Ch 2 (OSDK Fundamentals) |
| *Building with Palantir AIP: the Ontology Software Development Kit* | OSDK in action for AIP-integrated applications — practical walkthrough of authentication and object query patterns | Ch 2 (OSDK Fundamentals) |
| *Ontology SDK x Lennar for Quality Inspection* | Production case study of OSDK for quality inspection workflows — real-world OSDK architecture decisions | Ch 2 / Ch 3 |
| *Palantir Ontology Overview* | Foundational overview of the Palantir Ontology model — useful context for all OSDK chapters | Ch 2 (OSDK Fundamentals) |
| *Platform APIs x SLB for Digital Sustainability* | Production case study using Foundry Platform APIs at enterprise scale | Ch 4 (Platform SDK) |
| *Product Launch: Media, Real-Time Updates, and Expressive Compute in OSDK \| DevCon 2* | WebSocket-based real-time object updates and expressive compute patterns introduced in OSDK | Ch 3 (Subscriptions) |
| *Product Launch: Edge Embedded Ontology \| DevCon 2* | Edge-embedded Ontology for Ontology queries without central infrastructure — specialized deployment pattern | Ch 3 (OSDK Advanced) |

---

## Foundry Reference Project

| Video | What it Covers | Relevant TM Chapter |
|---|---|---|
| *Foundry Reference Project \| Structure* | Walks through the canonical Foundry Reference Project structure — OSDK, Ontology, and pipeline organization | Ch 1 / Ch 2 |
| *Foundry Reference Project \| Data Pipeline* | The data pipeline layer of the Foundry Reference Project | Ch 4 (Platform SDK) |
| *Foundry Reference Project \| Ontology* | The Ontology layer — Functions, Object Types, and computed properties in a production Ontology | Ch 2 / Ch 5 |
| *Foundry Reference Project \| Apps* | The application layer — current recommended patterns for Workshop-based and OSDK-backed apps | Ch 7 (Slate/App migration) |

---

## Security and Compliance

| Video | What it Covers | Relevant TM Chapter |
|---|---|---|
| *Cipher \| How to Encrypt Data in Foundry with Cipher* | Foundry's Cipher tool for field-level encryption of sensitive data | Ch 9 (Security) |
| *Security \| How to Debug a User's Access to a File* | Diagnostic procedure for investigating access control issues in Foundry | Ch 9 (Security) |
| *Security \| How to use Projects to Help Enable your Business to Scale* | How Foundry Projects structure access governance at scale — relevant to CBAC architecture | Ch 9 (Security) |
| *Platform Administration \| Setting up SSO in Palantir Foundry* | SSO configuration for the Foundry platform | Ch 9 (Security) |
| *Chad & Arnav \| Privacy & Security with Palantir AIP* | Privacy and security considerations for AIP-integrated applications | Ch 9 (Security) |

---

## Pipeline and Schedules

| Video | What it Covers | Relevant TM Chapter |
|---|---|---|
| *Schedules \| Creation, Configuration, and Execution in Palantir Foundry* | Setting up automated pipeline schedules in Foundry | Ch 4 / Ch 8 |
| *Schedules \| Management, Metrics, and Triggers in Foundry* | Managing schedule health, metrics, and trigger conditions | Ch 8 (CI/CD) |
| *Schedules \| Separating Data Ownership within a Pipeline in Foundry* | Data stewardship and ownership patterns for pipeline scheduling | Ch 4 / Ch 8 |
| *Pipeline Monitoring \| How to Start Monitoring Data Health in Palantir Foundry* | Foundational pipeline monitoring and data health tracking | Ch 8 (CI/CD) |
| *Pipeline Monitoring \| How to Monitor Health Across a Pipeline in Palantir Foundry* | End-to-end pipeline health monitoring across multi-step data flows | Ch 8 (CI/CD) |

---

## Advanced Patterns (MCP, Edge, Streaming)

| Video | What it Covers | Relevant TM Chapter |
|---|---|---|
| *Code in Production: Lennar x MCP \| DevCon 3* | Model Context Protocol (MCP) integration with Foundry in a production deployment — emerging pattern for LLM tool use against the Ontology | Ch 3 (OSDK Advanced) |
| *Product Launch: AIP Agents and Ontology-MCP \| DevCon 4* | AIP Agents using MCP to interact with the Ontology — extends the MCP pattern above | Ch 3 (OSDK Advanced) |
| *Deep Dive: Code-Based AI Development with Ontology* | Code-based development patterns extending traditional OSDK usage into AI-integrated workflows | Ch 2 / Ch 3 |
| *Developer Deskside \| Building Apps on Kafka Streaming Data in Palantir Foundry* | Building Foundry applications that consume Kafka streaming data | Ch 4 (Platform SDK) |
| *Deep Dive: Interoperability at Scale with the Multimodal Data Plane \| DevCon 5* | Cross-platform data interoperability at enterprise scale — senior-level architecture content | Ch 3 / Ch 8 |

---

## Case Studies in Production

| Video | What it Covers | Relevant TM Chapter |
|---|---|---|
| *Build with Palantir Developers* | Overview of the developer ecosystem and production deployment patterns | General |
| *7Bridges: AIP for Automated Invoice Auditing* | Production case study: AIP-integrated automation in a complex operational workflow | Ch 3 / Ch 5 |
| *Anduril: Ontology: Launchpad for Operations* | Defense-sector case study of the Ontology as an operational data platform — highly relevant to USAREUR-AF context | Ch 2 / Ch 3 |
| *Code in Production: Process Orchestration x Eaton \| DevCon 4* | Production case study on workflow automation and orchestration | Ch 6 / Ch 8 |
| *Code in Production: AI FDE x Lear & Trinity Industries \| DevCon 4* | Production case study on AI-integrated developer workflows | Ch 3 / Ch 5 |
| *Code in Production: Gallatin x Observability \| DevCon 3* | Production observability and monitoring for Foundry applications | Ch 8 (CI/CD) |

---

## Analytics Tools (SWE Context)

| Video | What it Covers | Relevant TM Chapter |
|---|---|---|
| *Quiver \| How to Build an Analysis in Palantir Foundry* | Building analytical workflows in Quiver — useful context when SWE output feeds analytical consumers | Ch 4 / General |
| *Quiver \| How to Use Parameters in Your Analysis* | Parameterized analysis in Quiver — relevant to building flexible analytical products | Ch 4 / General |

---

*USAREUR-AF Operational Data Team*
