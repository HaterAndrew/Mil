# COURSE SYLLABUS — SL 5O: ADVANCED PLATFORM ENGINEER
## Maven Smart System (MSS) — USAREUR-AF

| Field | Detail |
|---|---|
| **Level** | SL 5O — Advanced Platform Engineer Specialist Track |
| **Duration** | 3 days (24 hours) |
| **Prerequisites** | SL 4O (Go evaluation on file — **REQUIRED**); demonstrated operational experience managing MSS infrastructure |
| **Audience** | Experienced platform engineers leading infrastructure at fleet scale on MSS |
| **Format** | Instructor-led seminar + lab + practical exercise |
| **Location** | MSS Training Environment (Multi-cluster access required; fleet management tooling) |

---

**BLUF:** SL 5O extends SL 4O from single-cluster operations to fleet management — multi-cluster lifecycle management, platform reliability engineering (SLOs/SLIs/error budgets), RMF/ATO compliance automation, and developer experience engineering. SL 5O is for platform engineers who design the systems that manage systems, not just operate individual clusters.

---

## Learning Objectives

| # | Objective |
|---|---|
| 1 | Design a fleet topology for MSS spanning hub and edge clusters across multiple regions and classification levels |
| 2 | Implement a fleet-wide upgrade strategy with wave-based rollout, canary validation, and automated rollback |
| 3 | Define SLOs and SLIs for MSS platform services with error budgets and budget-based decision policies |
| 4 | Execute a blameless post-incident review following the detect-triage-mitigate-resolve-review-improve framework |
| 5 | Build an automated compliance pipeline that generates RMF evidence from live system data — scan results, configuration baselines, access logs |
| 6 | Implement STIG automation using policy-as-code with pass/fail/exception reporting |
| 7 | Design a golden path for MSS application onboarding that takes a new project from template to deployed application in <90 minutes |
| 8 | Configure federated observability across multiple clusters with cross-cluster correlation and SLO-based alerting |

---

## Pre-Course Checklist

Complete **5+ duty days before Day 1:**

- [ ] Read TM-50O, Chapter 2 (Multi-Cluster Fleet Management) — fleet topology and upgrade strategy
- [ ] Read TM-50O, Chapter 3 (Platform Reliability Engineering) — SLO framework and error budgets
- [ ] Review your SL 4O operational experience: identify incidents, scaling challenges, or compliance gaps that fleet-level tooling would have addressed

---

## Daily Schedule

### Day 1 — Fleet Management and Reliability Engineering

| Time | Block | Method | Content |
|---|---|---|---|
| 0800–0900 | 1 | Seminar | From cluster ops to fleet management: the scale shift; fleet topology models; Cluster API |
| 0900–1100 | 2 | Lab | Fleet provisioning: define cluster templates; provision a multi-cluster fleet declaratively |
| 1100–1115 | — | Break | |
| 1115–1200 | 3 | Lab | Fleet-wide upgrades: implement wave-based rollout with canary validation |
| 1200–1300 | — | Lunch | |
| 1300–1500 | 4 | Seminar + Lab | SRE fundamentals: SLOs, SLIs, error budgets; define SLOs for MSS platform services |
| 1500–1515 | — | Break | |
| 1515–1700 | 5 | Lab | Incident management: tabletop exercise — walk through a platform incident using the detect-through-improve framework |

---

### Day 2 — Compliance Automation and Developer Experience

| Time | Block | Method | Content |
|---|---|---|---|
| 0800–0830 | — | Review | Day 1 questions; SLO checkpoint — confirm all trainees have defined SLOs with error budgets |
| 0830–1030 | 6 | Seminar + Lab | RMF/ATO automation: continuous compliance monitoring; automated evidence generation; evidence API |
| 1030–1045 | — | Break | |
| 1045–1200 | 7 | Lab | STIG automation: implement policy-as-code STIG checks; build compliance dashboard with pass/fail/exception |
| 1200–1300 | — | Lunch | |
| 1300–1500 | 8 | Seminar + Lab | Developer experience engineering: golden paths, self-service portals, DORA metrics |
| 1500–1515 | — | Break | |
| 1515–1700 | 9 | Lab | Build a golden path: create an application onboarding template with pre-configured CI/CD, monitoring, and security |

---

### Day 3 — Observability, Cross-Domain, and Capstone

| Time | Block | Method | Content |
|---|---|---|---|
| 0800–0900 | 10 | Seminar | Fleet-scale observability: federated metrics, centralized logging, distributed tracing, alert philosophy at scale |
| 0900–1100 | 11 | Lab | Federated monitoring: configure cross-cluster metric federation and SLO-based alerting |
| 1100–1115 | — | Break | |
| 1115–1200 | 12 | Seminar | Cross-domain infrastructure: multi-classification cluster management, data diode integration, cross-domain replication |
| 1200–1300 | — | Lunch | |
| 1300–1500 | 13 | Exercise | **EX_50O Capstone:** Design and implement a fleet management solution: topology, upgrade strategy, SLOs, compliance pipeline, and observability |
| 1500–1515 | — | Break | |
| 1515–1630 | 14 | Presentation | Capstone presentations and peer review |
| 1630–1700 | 15 | Evaluation | Post-test (EXAM_TM50O_POST); course evaluation |
