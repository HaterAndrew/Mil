# Self-Study Addendum — TM-40H AI Engineer
## Palantir Developers Reference Library

> **NOT REQUIRED FOR QUALIFICATION.** This addendum provides curated references from the Palantir Developers YouTube channel ([@PalantirDevelopers](https://www.youtube.com/@PalantirDevelopers)) for personnel who want to deepen their MSS technical skills beyond the core curriculum. All content is publicly available.

**Companion Resource — Ontologize Channel:** [@Ontologize](https://www.youtube.com/@Ontologize) — Official Palantir training partner. 68 indexed video walkthroughs covering Foundry and AIP features. Full catalog with TM cross-references: [source_material/ontologize_youtube/README.md](../../source_material/ontologize_youtube/README.md)

---

## How to Use This Addendum

Videos are grouped by topic and ordered from foundational to advanced within each group. Start with the group most relevant to your current work. Videos marked in the TM with inline NOTE callouts are flagged here as well for easy cross-reference.

---

## New Doctrine References (March 2026)

The following doctrine sections were added to TM-40H this session. Review after the corresponding TM chapter:

- **ADP 3-13 AI/ML Framing** — Doctrinal context for AI/ML in operational information environments. See TM-40H concepts guide.
- **PED-to-Pipeline Mapping** — Processing, Exploitation, and Dissemination mapped to AIP Logic pipeline stages. See TM-40H concepts guide.
- **UDRA Governance** — Unified Data Reference Architecture governance framework for AI data access and controls. See TM-40H concepts guide.

---

## Group 1 — AIP Platform and Architecture Overview

| Video | What it Covers | Relevant TM Chapter |
|---|---|---|
| *Launching Build with AIP* | Introduction to the Build with AIP initiative and overall AIP platform direction | Ch 2 |
| *Product Launch: AI FDE \| DevCon 3* *(inline NOTE in TM)* | AI-driven Feature Development Environment — platform toolchain for code-assisted AI product development | Ch 2 |
| *Product Launch: AI FDE \| DevCon 5* | Updated AI FDE capabilities and developer experience enhancements | Ch 2 |
| *You Suck at AIP* | Common AIP engineering mistakes and how to avoid them — blunt, practical | Ch 2, Ch 3 |
| *Building Enterprise Autonomy with Shyam Sankar, CTO* | Strategic framing on enterprise AI autonomy from Palantir's CTO | Ch 2, Ch 9 |

---

## Group 2 — RAG Architecture and Retrieval

| Video | What it Covers | Relevant TM Chapter |
|---|---|---|
| *AIP with Jeg: Adding RAG to a Simple Notes Application* *(inline NOTE in TM)* | Step-by-step RAG pipeline build — ingestion, retrieval, grounding | Ch 5-2 |
| *Building with Palantir AIP: Logic Tools for RAG/OAG* *(inline NOTE in TM)* | AIP Logic tools for RAG and Ontology-Augmented Generation | Ch 5-2 |
| *Building with Palantir AIP: Data Tools for RAG/OAG* *(inline NOTE in TM)* | Data preparation and transform tools for RAG/OAG pipelines | Ch 5-2 |
| *Build with AIP: Semantic Search* | Semantic search capabilities within the AIP platform | Ch 5-3 |
| *Building with Palantir AIP: Semantic Search* *(inline NOTE in TM)* | AIP semantic search implementation walkthrough | Ch 5-3 |
| *Building with Palantir AIP: Advanced Search* | Advanced retrieval patterns beyond basic semantic search | Ch 5-3 |
| *Building with Palantir AIP: Ontology Software Development Kit* | OSDK integration patterns for Ontology-grounded AI pipelines | Ch 5-4 |

---

## Group 3 — AIP Evals, Testing, and Automation

| Video | What it Covers | Relevant TM Chapter |
|---|---|---|
| *Palantir AIP Evals \| Feedback to Fix* *(inline NOTE in TM)* | AIP Evals framework — structured feedback loops for AI output quality improvement | Ch 8 |
| *Chad & Colton \| Operationalizing AI with Palantir AIP Evals* *(inline NOTE in TM)* | Operationalizing eval-driven automation — moving from manual review to systematic gating | Ch 8, Ch 9 |
| *Product Launch: Eval-Driven Automation in AIP \| DevCon 2* *(inline NOTE in TM)* | Product-level introduction to eval-driven automation as a platform capability | Ch 6-2, Ch 8 |

---

## Group 4 — Agent Studio and Agent Architecture

| Video | What it Covers | Relevant TM Chapter |
|---|---|---|
| *Build with AIP: AIP Assist* | AIP Assist agent capabilities and configuration | Ch 4 |
| *Product Launch: AIP Agents and Ontology-MCP \| DevCon 4* *(inline NOTE in TM)* | AIP Agent integration with Ontology-MCP for Ontology-aware agent tool use | Ch 4-4 |
| *AIP Agents x HelmGuard AI: Function-Backed Agent Context \| DevCon 2* | Using function-backed context in AIP agents — practical agent tool design | Ch 4-2 |
| *ElevenLabs: Ontology-Driven Voice Agents \| DevCon 2* | Ontology-driven agent design demonstrated through a voice agent use case | Ch 4 |
| *AIP Logic x AT&T for Automating Operational Support \| DevCon 2* | Real-world AIP Logic automation at scale for operational support workflows | Ch 3, Ch 4 |

---

## Group 5 — Production Deployment, Observability, and Security

| Video | What it Covers | Relevant TM Chapter |
|---|---|---|
| *Chad & Bennett \| Observability with Palantir AIP* *(inline NOTE in TM)* | Monitoring and observability tooling for AIP workflows in production | Ch 9-3 |
| *Chad & Arnav \| Privacy & Security with Palantir AIP* *(inline NOTE in TM)* | Privacy controls, data handling boundaries, and security configuration for AIP | Ch 6-4 |
| *Product Launch: AIP Deployment at Scale \| DevCon 3* | Platform-level AIP deployment capabilities for enterprise-scale production systems | Ch 9 |
| *Product Launch: DevOps for AI Products \| DevCon 2* | DevOps practices adapted for AI product delivery — CI/CD, monitoring, governance gates | Ch 9 |
| *Deep Dive: Code-Based AI Development with Ontology* *(inline NOTE in TM)* | Python-based AI development using the Ontology as the data layer | Ch 7 |

---

## Group 6 — Compute Modules and Streaming Pipelines

| Video | What it Covers | Relevant TM Chapter |
|---|---|---|
| *AIP with Jeg: Building a Streaming Ingestor with Compute Modules* | Building a real-time streaming ingestor using Compute Modules | Ch 7-2 |
| *Build with AIP: Compute Modules* | Compute Modules capabilities and use cases for AI data pipelines | Ch 7 |

---

## Group 7 — Automation and Process Mining

| Video | What it Covers | Relevant TM Chapter |
|---|---|---|
| *Product Launch: Autopilot \| DevCon 3* | Autopilot — automated AI-driven workflow execution | Ch 3, Ch 9 |
| *Product Launch: Enterprise Automation \| DevCon 5* | Enterprise automation platform capabilities across organizational boundaries | Ch 9 |
| *Building with Palantir AIP: AI-Powered Process Mining* | Using AI to analyze and optimize operational processes — relevant to workflow design | Ch 3 |
| *Chad & Craig \| Data Migrations with AI FDE* | Using AI FDE to accelerate data migration and transformation work | Ch 7 |
| *Build with AIP: ERP HyperAuto* | AIP-powered automation applied to ERP systems — enterprise automation pattern | Ch 3 |

---

## Group 8 — Domain and Vertical Use Cases

| Video | What it Covers | Relevant TM Chapter |
|---|---|---|
| *Building with Palantir AIP: Customer Service Engine* | End-to-end AI customer service engine — agent design, tool use, and human escalation | Ch 4 |
| *Build with AIP \| Customer Service Engine* | Alternative walkthrough of the customer service engine use case | Ch 4 |
| *Building with Palantir AIP: Procurement* | AI-powered procurement automation — relevant to logistics and sustainment AI use cases | Ch 3 |
| *Chad & Agathe \| How Palantir Powers AI Automation Across Procurement* | Procurement AI automation at scale — operational workflow design | Ch 3 |
| *Chad & Chris \| Tariff Savings and Compliance through Palantir AIP* | AIP-driven compliance and cost analysis — structured workflow pattern | Ch 3 |
| *AIP for Piping and Instrumentation Diagram (P&ID) Analysis* | Vision-capable AI applied to technical diagram analysis | Ch 5 |
| *AIP for Medical Record Management \| Tackling VHA Healthcare Provider Burnout* | AIP applied to high-stakes document analysis with human review requirements | Ch 6 |

---

## Group 9 — AIP Now (Live Demonstrations)

| Video | What it Covers | Relevant TM Chapter |
|---|---|---|
| *AIP Now: AIP Response with Vision* | Live demo of vision-capable AIP response — multi-modal AI inference | Ch 5 |
| *AIP Now: Connected Construction* | AIP applied to real-time construction operations monitoring | Ch 3 |
| *AIP Now: Dynamic Scheduling* | AIP-driven dynamic scheduling — optimization with AI in the loop | Ch 3 |
| *AIP Now: Material Harmonization* | AIP applied to supply chain material harmonization — logistics pattern | Ch 3 |

---

*USAREUR-AF Operational Data Team — UNCLASSIFIED*
