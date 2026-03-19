# Self-Study Addendum — TM-50O: Advanced Platform Engineer
## Palantir Developers Reference Library

> **NOT REQUIRED FOR QUALIFICATION.** This addendum provides curated references from the Palantir Developers YouTube channel ([@PalantirDevelopers](https://www.youtube.com/@PalantirDevelopers)) for personnel who want to deepen their MSS technical skills beyond the core curriculum. All content is publicly available.

---

## How to Use This Addendum

TM-50O builds directly on TM-40O. The full TM-40O addendum (located at `../self_study/SELF_STUDY_TM40O_PLATFORM_ENGINEER.md`) remains relevant — all videos in that addendum apply at TM-50O level. This addendum adds videos specifically relevant to TM-50O's advanced and enterprise-level content: multi-cluster fleet management, platform reliability engineering, RMF/ATO automation, developer experience engineering, and platform observability at scale.

Videos are grouped by topic. Within each group, content is ordered from foundational to advanced.

---

## Group 1 — Fleet Management and Advanced Infrastructure

| Video | What it Covers | Relevant TM Chapter |
|---|---|---|
| *Product Launch: Edge Embedded Ontology \| DevCon 2* | Edge-embedded Ontology for Ontology queries without central infrastructure — directly relevant to Advanced Platform Engineers managing edge cluster fleets and DDIL-resilient deployments across the USAREUR-AF AOR. | Ch 2 (Multi-Cluster Fleet Management) |
| *Deep Dive: Interoperability at Scale with the Multimodal Data Plane \| DevCon 5* | Cross-platform data interoperability at enterprise scale — senior-level architecture content for Advanced Platform Engineers managing fleet-wide data plane infrastructure across classification boundaries. | Ch 2 (Fleet Topology) |
| *Deep Dive: Optimizing Data Pipelines with Iceberg Tables and Lightweight Compute \| DevCon 4* | Foundry Iceberg table format and lightweight compute — relevant to fleet-wide storage optimization and compute resource management across hub and edge clusters. | Ch 2, Ch 3 (Capacity Planning) |
| *Developer Deskside \| Building Apps on Kafka Streaming Data in Palantir Foundry* | Building applications on Kafka streaming data — context for Advanced Platform Engineers provisioning and managing streaming infrastructure at fleet scale. | Ch 2 (Multi-Cluster Fleet Management) |

---

## Group 2 — Observability, Monitoring, and Reliability

| Video | What it Covers | Relevant TM Chapter |
|---|---|---|
| *Code in Production: Gallatin x Observability \| DevCon 3* | Production observability and monitoring case study — directly applicable to building the federated observability stack described in Chapter 6 (distributed tracing, log aggregation, metric federation). | Ch 6 (Platform Observability at Scale) |
| *Pipeline Monitoring \| How to Start Monitoring Data Health in Palantir Foundry* | Foundational pipeline monitoring — applies to Advanced Platform Engineers establishing baseline health monitoring across the fleet before building advanced SLO-based alerting. | Ch 3 (SLOs and SLIs), Ch 6 |
| *Pipeline Monitoring \| How to Monitor Health Across a Pipeline in Palantir Foundry* | End-to-end pipeline health monitoring across multi-step data flows — relevant to cross-cluster pipeline observability and federated alerting strategies. | Ch 3 (Platform Reliability Engineering), Ch 6 |
| *Schedules \| Management, Metrics, and Triggers in Foundry* | Managing schedule health and metrics at scale — relevant to fleet-wide workload scheduling governance and error budget tracking. | Ch 3 (Error Budgets and Decision Making) |

---

## Group 3 — Security, Compliance, and RMF Automation

| Video | What it Covers | Relevant TM Chapter |
|---|---|---|
| *Cipher \| How to Encrypt Data in Foundry with Cipher* | Field-level encryption for sensitive data — relevant to Advanced Platform Engineers implementing fleet-wide encryption policies and cross-domain data protection controls for continuous compliance. | Ch 4 (RMF/ATO Automation) |
| *Security \| How to use Projects to Help Enable your Business to Scale* | Foundry Projects for access governance at scale — applicable to fleet-wide access control architecture and automated policy distribution across clusters. | Ch 4 (STIG Automation) |
| *Security \| How to Debug a User's Access to a File* | Diagnostic procedure for access control issues — useful for Advanced Platform Engineers building self-service access troubleshooting into the developer experience portal. | Ch 5 (Self-Service Portal Design) |
| *Platform Administration \| Setting up SSO in Palantir Foundry* | SSO configuration — relevant to fleet-wide identity and authentication infrastructure that must function consistently across hub and edge clusters. | Ch 4 (Continuous Compliance) |
| *Chad & Arnav \| Privacy & Security with Palantir AIP* | Privacy and security architecture for AIP systems — context for Advanced Platform Engineers securing AI workload infrastructure across classification domains. | Ch 4 (RMF/ATO Automation) |

---

## Group 4 — Developer Experience and Platform Product

| Video | What it Covers | Relevant TM Chapter |
|---|---|---|
| *Product Launch: Developer Experience \| DevCon 5* | Developer experience improvements from DevCon 5 — directly relevant to Advanced Platform Engineers engineering golden paths and self-service portals described in Chapter 5. | Ch 5 (Developer Experience Engineering) |
| *Product Launch: Rapid Software Development with OSDK 2.0* | OSDK 2.0 developer experience — context for Advanced Platform Engineers understanding the application development workflow their platform must support and accelerate. | Ch 5 (Golden Paths) |
| *Code Repositories \| Development Process and Pipeline Craftsmanship in Palantir Foundry* | Full development lifecycle and pipeline craftsmanship — foundational reference for designing the golden path CI/CD workflows that application teams consume. | Ch 5 (Golden Paths) |
| *Code Repositories \| Best Practices for Creating Pull Requests in Palantir Foundry* | PR best practices — context for enforcing code review standards in fleet-wide CI/CD pipeline templates. | Ch 5 (Developer Experience Engineering) |

---

## Group 5 — Strategic Platform Leadership

| Video | What it Covers | Relevant TM Chapter |
|---|---|---|
| *Akshay Krishnaswamy Opening Remarks \| DevCon 5* | Strategic overview of Palantir's operational AI direction — context for Advanced Platform Engineers planning fleet evolution and infrastructure roadmaps that support emerging platform capabilities. | Ch 5 (Developer Productivity Measurement) |
| *Building Enterprise Autonomy with Shyam Sankar, CTO* | CTO perspective on enterprise autonomy — strategic context for senior Platform Engineers advising leadership on infrastructure investment and platform strategy. | General |
| *Product Launch: Hivemind \| DevCon 5* | Palantir Hivemind for multi-domain decision support and autonomous task execution — relevant for Advanced Platform Engineers planning infrastructure to support next-generation AI workloads. | Ch 2 (Fleet Topology) |
| *Anduril: Ontology: Launchpad for Operations* | Defense-sector Ontology as operational data platform — closely analogous to USAREUR-AF MSS. Illustrates fleet-scale infrastructure decisions in a military operational context. | General |
| *Code in Production: Process Orchestration x Eaton \| DevCon 4* | Production workflow orchestration at scale — case study relevant to fleet-wide pipeline orchestration and deployment automation patterns. | Ch 2, Ch 5 |

---

## Full TM-40O Addendum Reference

All video groups from the TM-40O Self-Study Addendum remain applicable at TM-50O:

- **CI/CD Pipeline and Code Repository Operations** — foundational for Chapter 5 (Golden Paths) and fleet-wide pipeline templates
- **Security, Compliance, and Access Control** — directly supports Chapter 4 (RMF/ATO Automation) and Chapter 6 (Observability)
- **Pipeline Monitoring and Scheduling** — supports Chapter 3 (Platform Reliability Engineering) and Chapter 6 (Alerting Strategy)
- **Platform Architecture and Advanced Patterns** — supports Chapter 2 (Fleet Management) and cross-domain infrastructure
- **Case Studies and Platform Context** — general fleet-scale platform leadership context

See `../self_study/SELF_STUDY_TM40O_PLATFORM_ENGINEER.md` for the full list.

---

*USAREUR-AF Operational Data Team — UNCLASSIFIED*
