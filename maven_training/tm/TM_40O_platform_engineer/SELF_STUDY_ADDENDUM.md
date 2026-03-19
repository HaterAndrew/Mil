# Self-Study Addendum — TM-40O: Platform Engineer
## Palantir Developers Reference Library

> **NOT REQUIRED FOR QUALIFICATION.** This addendum provides curated references from the Palantir Developers YouTube channel ([@PalantirDevelopers](https://www.youtube.com/@PalantirDevelopers)) for personnel who want to deepen their MSS technical skills beyond the core curriculum. All content is publicly available.

---

## How to Use This Addendum

Videos are grouped by topic and ordered from foundational to advanced. Start with the group most relevant to your current work or the chapter you just completed. Platform Engineers should prioritize Groups 1 and 2 (CI/CD, pipeline architecture, and security) before proceeding to advanced integration and architecture topics in Groups 3 and 4.

---

## Group 1 — CI/CD Pipeline and Code Repository Operations

| Video | What it Covers | Relevant TM Chapter |
|---|---|---|
| *Code Repositories \| Development Process and Pipeline Craftsmanship in Palantir Foundry* | Full development lifecycle for Foundry code resources — branching strategy, PR discipline, and promotion. Directly relevant to CI/CD pipeline design and developer workflow governance. | Ch 6 (CI/CD Pipeline Design) |
| *Code Repositories \| Best Practices for Creating Pull Requests in Palantir Foundry* | PR best practices in Foundry code repositories — reinforces the code review and merge controls that Platform Engineers enforce in pipeline gates. | Ch 6 (Pipeline Security Gates) |
| *Code Repositories \| Reviewing Code and Best Practices* | Code review standards within Foundry repositories — context for Platform Engineers configuring review enforcement in CI/CD pipelines. | Ch 6 (Pipeline Security Gates) |
| *Code Repositories \| How to Use Data Expectations in Palantir Foundry* | Foundry's built-in Data Expectations for data quality assertions — relevant to pipeline quality gates that Platform Engineers configure and monitor. | Ch 6 (CI/CD Pipeline Design) |
| *Code Repositories \| How to Unit Test PySpark in Palantir Foundry* | PySpark unit testing patterns — context for Platform Engineers configuring test stages in CI/CD pipelines for data transform code. | Ch 6 (CI/CD Pipeline Design) |

---

## Group 2 — Security, Compliance, and Access Control

| Video | What it Covers | Relevant TM Chapter |
|---|---|---|
| *Cipher \| How to Encrypt Data in Foundry with Cipher* | Foundry's Cipher tool for field-level encryption of sensitive data — directly relevant to Platform Engineers implementing data-at-rest encryption controls for RMF/ATO compliance. | Ch 8 (Platform Security and Compliance) |
| *Security \| How to Debug a User's Access to a File* | Diagnostic procedure for investigating access control issues in Foundry — essential for Platform Engineers troubleshooting CBAC boundary and permission issues. | Ch 8 (Access Control and Audit) |
| *Security \| How to use Projects to Help Enable your Business to Scale* | How Foundry Projects structure access governance at scale — relevant to Platform Engineers designing namespace isolation and multi-tenant access patterns. | Ch 8 (Access Control and Audit) |
| *Platform Administration \| Setting up SSO in Palantir Foundry* | SSO configuration for the Foundry platform — directly relevant to Platform Engineers managing authentication infrastructure. | Ch 8 (Platform Security and Compliance) |
| *Chad & Arnav \| Privacy & Security with Palantir AIP* | Privacy and security architecture for AIP-integrated applications — context for Platform Engineers securing AI workload infrastructure. | Ch 8 (Platform Security and Compliance) |

---

## Group 3 — Pipeline Monitoring and Scheduling

| Video | What it Covers | Relevant TM Chapter |
|---|---|---|
| *Pipeline Monitoring \| How to Start Monitoring Data Health in Palantir Foundry* | Foundational pipeline monitoring and data health tracking — directly applicable to Platform Engineers building observability for CI/CD pipelines and data flows. | Ch 6 (CI/CD Pipeline Design) |
| *Pipeline Monitoring \| How to Monitor Health Across a Pipeline in Palantir Foundry* | End-to-end pipeline health monitoring across multi-step data flows — relevant to cross-pipeline observability and alerting configuration. | Ch 6, Ch 8 |
| *Schedules \| Creation, Configuration, and Execution in Palantir Foundry* | Setting up automated pipeline schedules in Foundry — context for Platform Engineers managing scheduled workload orchestration. | Ch 6 (CI/CD Pipeline Design) |
| *Schedules \| Management, Metrics, and Triggers in Foundry* | Managing schedule health, metrics, and trigger conditions — relevant to platform-level scheduling governance and resource management. | Ch 3 (Resource Management and Quotas) |
| *Schedules \| Separating Data Ownership within a Pipeline in Foundry* | Data stewardship and ownership patterns for pipeline scheduling — applicable to multi-tenant pipeline isolation in Kubernetes namespaces. | Ch 3 (Kubernetes), Ch 4 (IaC) |

---

## Group 4 — Platform Architecture and Advanced Patterns

| Video | What it Covers | Relevant TM Chapter |
|---|---|---|
| *How Palantir Integrates with Your Current Data Systems* | How Foundry/MSS connects to existing Army data systems — context for Platform Engineers managing integration infrastructure and data ingestion pipelines. | Ch 1, Ch 2 (Platform-as-Product) |
| *Deep Dive: Interoperability at Scale with the Multimodal Data Plane \| DevCon 5* | Cross-platform data interoperability at enterprise scale — senior-level architecture content for Platform Engineers managing multi-system integration infrastructure. | Ch 7 (Air-Gapped and DDIL Operations) |
| *Developer Deskside \| Building Apps on Kafka Streaming Data in Palantir Foundry* | Building Foundry applications consuming Kafka streaming data — relevant for Platform Engineers provisioning and managing streaming infrastructure. | Ch 2 (Platform-as-Product), Ch 3 (Kubernetes) |
| *Product Launch: Edge Embedded Ontology \| DevCon 2* | Edge-embedded Ontology for disconnected operations — directly relevant to Platform Engineers managing edge cluster deployments and DDIL-resilient infrastructure. | Ch 7 (Edge Cluster Management) |
| *Deep Dive: Optimizing Data Pipelines with Iceberg Tables and Lightweight Compute \| DevCon 4* | Foundry Iceberg table format and lightweight compute for high-volume pipeline optimization — relevant to storage class configuration and compute resource management. | Ch 3 (Resource Management) |

---

## Group 5 — Case Studies and Platform Context

| Video | What it Covers | Relevant TM Chapter |
|---|---|---|
| *Code in Production: Gallatin x Observability \| DevCon 3* | Production observability and monitoring for Foundry applications — directly applicable to Platform Engineers building the observability stack described in Chapter 8. | Ch 8 (Platform Security and Compliance) |
| *Anduril: Ontology: Launchpad for Operations* | Defense-sector case study of the Ontology as an operational data platform — context for understanding the application workloads that run on the platform infrastructure. | Ch 1, Ch 2 |
| *Code in Production: Process Orchestration x Eaton \| DevCon 4* | Production case study on workflow automation and orchestration — illustrates the application patterns that CI/CD pipelines must support. | Ch 6 (CI/CD Pipeline Design) |
| *Platform APIs x SLB for Digital Sustainability* | Production case study using Foundry Platform APIs at enterprise scale — relevant context for Platform Engineers managing API gateway infrastructure. | Ch 2 (Platform-as-Product) |

---

*USAREUR-AF Operational Data Team*
