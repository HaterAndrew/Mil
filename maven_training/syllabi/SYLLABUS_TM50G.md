# COURSE SYLLABUS — SL 5G: ADVANCED OPERATIONS RESEARCH/SYSTEMS ANALYSIS
## Maven Smart System (MSS) — USAREUR-AF

| Field | Detail |
|---|---|
| **Level** | SL 5G — Advanced ORSA Specialist Track |
| **Duration** | 5 days (40 hours) |
| **Prerequisites** | SL 4G complete (Go evaluation on file); 18+ months active ORSA experience or graduate-level OR/MS program (concurrent enrollment accepted); demonstrated proficiency with Python or R and validated quantitative models in an operational context |
| **Audience** | Senior FA49 officers and analysts, theater-level ORSA practitioners, data scientists in advanced analytical roles |
| **Format** | Seminar + advanced lab + peer-reviewed analytical product |
| **Location** | MSS Training Environment (Code Workspace provisioned, GPU allocation confirmed) |

> **PREREQUISITE WARNING:** SL 5G is not required for the majority of ORSA billets. It is intended for personnel actively assigned to advanced modeling, campaign analysis, or platform architecture roles at theater level. If uncertain whether this track applies to your billet, consult your supervisor or C2DAO before enrolling.

---

**BLUF:** SL 5G moves beyond SL 4G's operational modeling toolkit to the methods and standards required for theater-strategic analytical products — campaign analysis, multi-echelon optimization, Bayesian inference under deep uncertainty, and agent-based simulation. Products from SL 5G analysts inform GO/SES decisions and alliance planning. The standard at this level is not just technical correctness — it is interpretability, peer reviewability, and honest uncertainty characterization.

---

## Learning Objectives

| # | Objective |
|---|---|
| 1 | Apply Bayesian inference for operational decision analysis: posterior estimation, conjugate priors, hierarchical models for multi-echelon data |
| 2 | Build agent-based simulation models for complex adaptive scenarios (logistics, attrition, route analysis) with documented calibration and validation |
| 3 | Design and execute multi-objective optimization models; navigate Pareto tradeoffs; communicate tradeoff implications at the operational and strategic level |
| 4 | Apply network analysis (graph theory, centrality, flow) to operational problems: supply chain resilience, communications network vulnerability, task organization analysis |
| 5 | Build ensemble and stacked model architectures; conduct rigorous out-of-sample validation; document bias-variance tradeoffs |
| 6 | Produce a theater-level ORSA analytical report meeting USAREUR-AF GO/SES product standards: uncertainty quantification, assumption documentation, peer review, reproducibility |
| 7 | Conduct and document a peer review of another analyst's model and product; identify methodological weaknesses and limitation gaps |

---

## Pre-Course Checklist

Complete **10+ duty days before Day 1:**

- [ ] Confirm Code Workspace access with GPU allocation (contact C2DAO — standard access is insufficient)
- [ ] Install and test: scipy, statsmodels, pymc3 (or equivalent Bayesian library), networkx
- [ ] Read TM-50G, Chapter 1 (Advanced ORSA Standards) in full — the peer review and uncertainty documentation requirements are assessed on Day 5
- [ ] Prepare a 1-page description of a current or recent operational analytical problem from your unit — you will use this for the Day 5 product exercise

---

## Daily Schedule

### Day 1 — Bayesian Methods for Operational Analysis

| Time | Block | Method | Content |
|---|---|---|---|
| 0800–0900 | 1 | Seminar | SL 5G standards: peer review requirements, uncertainty documentation, GO/SES product expectations |
| 0900–1100 | 2 | Lab | Bayesian inference: prior selection, likelihood functions, posterior estimation — operational examples (casualty estimation, readiness probability) |
| 1100–1115 | — | Break | |
| 1115–1200 | 3 | Lab | Conjugate priors; binomial/beta model for readiness probability; documenting prior assumptions |
| 1200–1300 | — | Lunch | |
| 1300–1500 | 4 | Lab | Hierarchical Bayesian models: multi-echelon readiness pooling; partial pooling vs. no pooling tradeoffs |
| 1500–1515 | — | Break | |
| 1515–1700 | 5 | Lab | Bayesian updating: incorporating new LOGSTAT data into existing posteriors; sequential analysis patterns |

**Evening reading:** TM-50G, Chapter 2 (Agent-Based Simulation) — sections on calibration and operational scenario design.

---

### Day 2 — Agent-Based Simulation and Network Analysis

| Time | Block | Method | Content |
|---|---|---|---|
| 0800–0830 | — | Review | Bayesian questions; common prior misspecification errors |
| 0830–1030 | 6 | Lab | Agent-based simulation: Mesa/NetLogo patterns; defining agents, environment, and interaction rules; logistics convoy simulation |
| 1030–1045 | — | Break | |
| 1045–1200 | 7 | Lab | Calibration and validation: parameter sweeps, sensitivity to initial conditions; comparing to historical analogues |
| 1200–1300 | — | Lunch | |
| 1300–1500 | 8 | Lab | Network analysis: graph construction, centrality measures, shortest path; supply chain resilience analysis |
| 1500–1515 | — | Break | |
| 1515–1700 | 9 | Lab | Network vulnerability: removing critical nodes; communications network fragility; task organization restructuring analysis |

**Evening reading:** TM-50G, Chapter 3 (Multi-Objective Optimization) — Pareto frontier and tradeoff communication sections.

---

### Day 3 — Multi-Objective Optimization and Ensemble Methods

| Time | Block | Method | Content |
|---|---|---|---|
| 0800–0830 | — | Review | Simulation calibration check; network analysis output review |
| 0830–1030 | 10 | Lab | Multi-objective optimization: objective function design, constraint formulation, Pareto frontier computation |
| 1030–1045 | — | Break | |
| 1045–1200 | 11 | Lab | Communicating Pareto tradeoffs to commanders: translating the frontier into operational COA options |
| 1200–1300 | — | Lunch | |
| 1300–1500 | 12 | Lab | Ensemble methods: bagging, boosting, stacking; cross-validation architecture; out-of-sample validation |
| 1500–1515 | — | Break | |
| 1515–1700 | 13 | Lab | Bias-variance tradeoff documentation; model complexity justification; limitation documentation standards |

**Evening reading:** TM-50G, Chapter 7 (Senior-Level OR Products and Briefings) — complete read before Day 4 product work.

---

### Day 4 — Product Standards and Peer Review

| Time | Block | Method | Content |
|---|---|---|---|
| 0800–0900 | 14 | Seminar | GO/SES ORSA product standards: structure, uncertainty section, assumption register, peer review signature block |
| 0900–1100 | 15 | Workshop | Draft analytical product from participant's prepared operational problem (see pre-course checklist) |
| 1100–1115 | — | Break | |
| 1115–1200 | 16 | Workshop | Continue product development; instructor circulates for individual feedback |
| 1200–1300 | — | Lunch | |
| 1300–1500 | 17 | Peer Review | Structured peer review exercise: exchange draft products; apply the SL 5G peer review checklist |
| 1500–1515 | — | Break | |
| 1515–1700 | 18 | Debrief | Peer review findings; common gaps; revise products based on feedback |

**Evening reading:** Revise analytical product incorporating peer review feedback; prepare for Day 5 evaluation.

---

### Day 5 — Advanced Integration and Practical Evaluation

| Time | Block | Method | Content |
|---|---|---|---|
| 0800–0900 | 19 | Review | Product revision questions; evaluation briefing |
| 0900–1000 | 20 | Brief | Practical evaluation scenario brief and planning time |
| 1000–1015 | — | Break | |
| 1015–1200 | 21 | **Eval** | **Evaluation Part 1:** Advanced method application (Bayesian model or optimization on provided dataset) |
| 1200–1300 | — | Lunch | |
| 1300–1600 | 22 | **Eval** | **Evaluation Part 2:** Produce GO/SES-ready analytical product; submit for peer review |
| 1600–1700 | 23 | Review | Evaluator feedback; graduation requirements review |

---

## Practical Exercise

**Scenario:** Theater-level logistics analysis for campaign planning. The G4 requires: a Bayesian readiness probability estimate for two maneuver brigades, a supply chain resilience analysis (network), and a multi-objective optimization of two sustainment COAs trading cost against risk.

**Go standard:** Pass 4 of 5 product elements. Product must include: uncertainty quantification on all estimates, assumption register, peer review complete, all models reproducible with set seed or documented parameters.

---

## Peer Advanced Tracks

| Track | Relevance to SL 5G |
|---|---|
| SL 5H (Advanced AI Eng) | AI-augmented analytical pipelines; LLM-assisted pattern recognition in ORSA products |
| SL 5M (Advanced ML Eng) | Advanced model architectures (ensemble, Bayesian) used in ORSA modeling; drift detection for deployed ORSA models |
| SL 5J (Advanced PM) | Communicating ORSA findings at portfolio level to GO/SES audiences; resource allocation analysis feeding PM dashboards |

---

*USAREUR-AF Operational Data Team*
*Syllabus SL 5G | Version 1.0 | March 2026*
