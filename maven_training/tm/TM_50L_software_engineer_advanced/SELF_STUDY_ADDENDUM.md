# Self-Study Addendum — TM-50L Advanced Software Engineer
## Palantir Developers Reference Library

> **NOT REQUIRED FOR QUALIFICATION.** This addendum provides curated references from the Palantir Developers YouTube channel ([@PalantirDevelopers](https://www.youtube.com/@PalantirDevelopers)) for personnel who want to deepen their MSS technical skills beyond the core curriculum. All content is publicly available.

**Companion Resource — Ontologize Channel:** [@Ontologize](https://www.youtube.com/@Ontologize) — Official Palantir training partner. 68 indexed video walkthroughs covering Foundry and AIP features. Full catalog with TM cross-references: [source_material/ontologize_youtube/README.md](../../source_material/ontologize_youtube/README.md)

---

## How to Use This Addendum

TM-50L builds directly on TM-40L. The full TM-40L addendum (located at `../TM_40L_software_engineer/SELF_STUDY_ADDENDUM.md`) remains relevant — all videos in that addendum apply at TM-50L level. This addendum adds videos specifically relevant to TM-50L's advanced and leadership-level content: platform architecture, enterprise interoperability, advanced DevSecOps, observability, and senior technical leadership.

Videos are grouped by topic. Within each group, content is ordered from foundational to advanced.

---

## Advanced Platform Architecture

| Video | What it Covers | Relevant TM Chapter |
|---|---|---|
| *Deep Dive: Code-Based AI Development with Ontology* | Code-based development patterns extending traditional OSDK and Platform SDK usage into AI-integrated workflows — senior architecture content for SWEs designing AI-supporting infrastructure | Ch 2 (Platform SDK Infrastructure) |
| *Deep Dive: Advanced Ontology \| DevCon 5* | Advanced Ontology patterns announced at DevCon 5, covering schema design, object relationship modeling, and Ontology performance at scale | Ch 2 / Ch 3 |
| *Product Launch: Edge Embedded Ontology \| DevCon 2* | Edge-embedded Ontology allowing Ontology queries to run at the edge without central infrastructure — specialized architecture for forward-deployed or disconnected operations | Ch 4 (Multi-Tenant Architecture) |
| *Deep Dive: Interoperability at Scale with the Multimodal Data Plane \| DevCon 5* | Cross-platform data interoperability at enterprise scale — senior-level architecture for multi-system MSS integration patterns | Ch 3 (Performance) |
| *Product Launch: Hivemind \| DevCon 5* | Palantir Hivemind platform capabilities announced at DevCon 5 — context for near-term platform evolution relevant to TM-50L platform roadmap responsibilities | Ch 8 (Platform Leadership) |

---

## Developer Experience and DevSecOps

| Video | What it Covers | Relevant TM Chapter |
|---|---|---|
| *Product Launch: Developer Experience \| DevCon 5* | Developer experience improvements from DevCon 5, including toolchain enhancements relevant to CI/CD pipeline setup and DevSecOps workflow | Ch 6 (DevSecOps) |
| *Code Repositories \| Development Process and Pipeline Craftsmanship in Palantir Foundry* | Full development lifecycle for Foundry code resources — foundational reference for the DevSecOps pipeline in Chapter 6 | Ch 6 (DevSecOps) |
| *Code Repositories \| Best Practices for Creating Pull Requests in Palantir Foundry* | PR best practices reinforcing the code review standards in Chapter 8 | Ch 8 (Platform Leadership) |
| *Code Repositories \| Reviewing Code and Best Practices* | Code review standards — directly supports the TM-50L code review responsibilities described in Section 8-3 | Ch 8 (Platform Leadership) |

---

## Observability and Production Operations

| Video | What it Covers | Relevant TM Chapter |
|---|---|---|
| *Code in Production: Gallatin x Observability \| DevCon 3* | Production observability case study — how a real engineering team instruments and monitors their Foundry deployment | Ch 3 (Performance) / Ch 6 (DevSecOps) |
| *Pipeline Monitoring \| How to Start Monitoring Data Health in Palantir Foundry* | Foundational pipeline monitoring and data health tracking — applies to TM-50L's platform health governance responsibilities | Ch 6 (DevSecOps) |
| *Pipeline Monitoring \| How to Monitor Health Across a Pipeline in Palantir Foundry* | End-to-end pipeline health monitoring across multi-step data flows | Ch 6 (DevSecOps) |
| *Schedules \| Management, Metrics, and Triggers in Foundry* | Managing schedule health and metrics at scale — relevant to TM-50L's compute cost management and pipeline governance | Ch 3 (Performance) |

---

## Advanced Integration Patterns

| Video | What it Covers | Relevant TM Chapter |
|---|---|---|
| *Developer Deskside \| Building Apps on Kafka Streaming Data in Palantir Foundry* | Building Foundry applications consuming Kafka streaming data — foundational reference for the Kafka integration patterns in Chapter 5 | Ch 5 (External Integration) |
| *Code in Production: Lennar x MCP \| DevCon 3* | Model Context Protocol (MCP) integration with Foundry in production — MCP as an emerging standard for LLM tool use against the Ontology | Ch 5 / Ch 2 |
| *Product Launch: AIP Agents and Ontology-MCP \| DevCon 4* | AIP Agents using MCP to interact with the Ontology — next-generation integration architecture | Ch 5 / Ch 4 |
| *Code in Production: Process Orchestration x Eaton \| DevCon 4* | Production case study on workflow automation and orchestration at scale | Ch 5 (External Integration) |

---

## Security and Compliance (Advanced)

| Video | What it Covers | Relevant TM Chapter |
|---|---|---|
| *Cipher \| How to Encrypt Data in Foundry with Cipher* | Field-level encryption for sensitive data in Foundry — relevant to classification-aware design in Chapter 4 | Ch 4 (Multi-Tenant) / Ch 7 (Security) |
| *Security \| How to Debug a User's Access to a File* | Diagnostic procedure for access control issues — useful in authorized security testing and CBAC boundary debugging | Ch 7 (Security Assessment) |
| *Chad & Arnav \| Privacy & Security with Palantir AIP* | Privacy and security architecture for AIP-integrated systems — senior-level context for TM-50L security assessment responsibilities | Ch 7 (Security Assessment) |
| *Platform Administration \| Setting up SSO in Palantir Foundry* | SSO configuration — relevant to TM-50L engineers managing authentication architecture for multi-tenant deployments | Ch 4 / Ch 7 |

---

## Platform Leadership and Community

| Video | What it Covers | Relevant TM Chapter |
|---|---|---|
| *Akshay Krishnaswamy Opening Remarks \| DevCon 5* | DevCon 5 opening remarks from Palantir's CEO — strategic context for platform direction, relevant to TM-50L platform roadmap review responsibilities | Ch 8 (Platform Leadership) |
| *Building Enterprise Autonomy with Shyam Sankar, CTO* | CTO-level perspective on enterprise autonomy and platform direction — context for senior SWEs advising on platform strategy and ATO planning | Ch 8 (Platform Leadership) |
| *Anduril: Ontology: Launchpad for Operations* | Defense-sector case study of the Ontology as an operational data platform — closely analogous to the USAREUR-AF MSS architecture | General / Ch 4 |

---

## Full TM-40L Addendum Reference

All video groups from the TM-40L Self-Study Addendum remain applicable at TM-50L:

- **Code Repository Fundamentals** — directly supports Chapter 6 (DevSecOps)
- **Functions on Objects (FOO)** — supports Chapter 6 (Ontology CI) and Chapter 8 (code review)
- **OSDK and Platform SDK** — foundational for Chapters 2, 3, and 5
- **Foundry Reference Project** — architecture reference for Chapter 8 leadership responsibilities
- **Security and Compliance** — supplements Chapter 7 (Security Assessment)
- **Pipeline and Schedules** — supports Chapter 3 (Performance) and Chapter 6 (DevSecOps)
- **Advanced Patterns** — supplements Chapters 4 and 5
- **Case Studies in Production** — general leadership context

See `/home/dale/Desktop/claude/maven_training/tm/TM_40L_software_engineer/SELF_STUDY_ADDENDUM.md` for the full list.

---

*USAREUR-AF Operational Data Team — UNCLASSIFIED*
