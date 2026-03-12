# COURSE SYLLABUS
## TM-40G — OPERATIONS RESEARCH/SYSTEMS ANALYSIS (ORSA)
### Maven Smart System (MSS) — USAREUR-AF

| | |
|---|---|
| **Level** | TM-40G (ORSA Specialist Track) |
| **Duration** | 5 days (40 hours) |
| **Prerequisites** | TM-10, TM-20, TM-30 (all Go evaluations on file); Data Literacy Technical Reference (recommended); graduate-level quantitative background (statistics, linear algebra, optimization); working proficiency in Python or R |
| **Audience** | FA49 Operations Research officers, quantitative analysts, ORSA-assigned civilians |
| **Format** | Instructor-led lab + guided practice + commander brief practical |
| **Location** | MSS Training Environment (Code Workspace provisioned) |

---

## What This Course Does for You

ORSA analysts on MSS translate operational questions into models and translate model outputs into commander decisions. This course teaches you to do that work inside Foundry — connecting directly to operational data, building quantitative models, and delivering products that commanders can actually use to allocate resources and compare COAs.

TM-40G does not teach statistics from scratch. It teaches you to apply your existing quantitative skills on MSS data, using Foundry Code Workspaces, and to deliver outputs that meet USAREUR-AF ORSA product standards.

Five days provides time for Code Workspace configuration without displacing instruction, sufficient repetition on each modeling technique, and a complete practice build before the evaluated practical exercise.

---

## Learning Objectives

By the end of training, you will be able to:

1. Configure a Python/R Code Workspace with required packages, verify Foundry dataset connectivity, and write outputs back to Foundry curated datasets via transaction
2. Build and validate a regression model for a provided readiness or logistics dataset; document validation statistics and assumptions
3. Construct a time series forecast with documented model selection rationale, assumptions, and confidence bounds
4. Run a Monte Carlo simulation for a COA comparison scenario and quantify risk at defined probability thresholds
5. Formulate and solve a linear programming resource allocation problem with documented constraints and sensitivity analysis
6. Build analytical Quiver/Contour visualizations displaying model outputs with uncertainty bounds
7. Produce a commander brief presenting findings in operational language — every point estimate with a confidence range; explicitly stated assumptions and limitations
8. Apply USAREUR-AF ORSA product standards: documentation, validation, reproducibility (set seed), and uncertainty communication

---

## Before You Attend: Pre-Course Checklist

Complete **7–10+ duty days before Day 1:**
- [ ] Request **Code Workspace access** from C2DAO — standard unit MSS Administrator access is not sufficient. Allow 7–10 duty days. Contact C2DAO directly.
- [ ] Confirm the workspace runs a provided test script before Day 1. If the test script fails, contact C2DAO before arriving — do not wait until Day 1.
- [ ] Read TM-40G, Chapter 1 (Introduction, role, prerequisites self-check) — 30 min
- [ ] Read TM-40G, Chapter 2, Sections 2-1 and 2-2 (Code Workspace overview) — 20 min

---

## Daily Schedule

**Day 1 — Environment Setup and Foundry Data Access**

| Time | Block | Method | Content |
|---|---|---|---|
| 0800–0900 | 1  | Brief    | ORSA role on MSS; analytical product standards; the Foundry data model and how ORSA connects to it |
| 0900–1100 | 2  | Lab      | Code Workspace setup: Python/R environment, package installation, confirming GPU/CPU allocation, environment reproducibility |
| 1100–1115 | —  | Break    | |
| 1115–1200 | 3  | Lab      | Foundry dataset connectivity: accessing Ontology datasets from Code Workspace, reading via Spark/pandas, inspecting schema |
| 1200–1300 | —  | Lunch    | |
| 1300–1500 | 4  | Lab      | Writing outputs to Foundry: transaction pattern for writing results back to curated datasets; test this on Day 1, not Day 4 |
| 1500–1515 | —  | Break    | |
| 1515–1700 | 5  | Lab      | Data profiling in Code Workspace: null distributions, outlier detection, feature distributions — building QC habits before modeling |

**Evening reading:** TM-40G, Chapter 3 (Statistical Modeling) — review regression and validation procedures.

---

**Day 2 — Statistical Modeling**

| Time | Block | Method | Content |
|---|---|---|---|
| 0800–0830 | —  | Review   | Day 1 questions; Foundry write transaction troubleshooting |
| 0830–1030 | 6  | Lab      | Regression: linear regression for readiness forecasting — feature selection, assumption checking, training, validation statistics |
| 1030–1045 | —  | Break    | |
| 1045–1200 | 7  | Lab      | Classification models: logistic regression, decision trees — feature selection, cross-validation, calibration check |
| 1200–1300 | —  | Lunch    | |
| 1300–1500 | 8  | Lab      | Model validation standards: residual analysis, cross-validation, documenting assumptions; writing validated output to Foundry |
| 1500–1515 | —  | Break    | |
| 1515–1700 | 9  | Lab      | Practice build: apply regression to a second provided dataset; document model, write output to Foundry, build a Quiver visualization |

**Evening reading:** TM-40G, Chapter 4 (Time Series) — review ARIMA procedures and confidence bound requirements; TM-40G, Chapter 5 (Monte Carlo) — review simulation framework.

---

**Day 3 — Time Series and Monte Carlo**

| Time | Block | Method | Content |
|---|---|---|---|
| 0800–0830 | —  | Review   | Day 2 questions; model documentation standards check |
| 0830–1030 | 10 | Lab      | Time series: stationarity testing, ACF/PACF plot interpretation, ARIMA model identification — document why you chose (p,d,q), not just what you chose |
| 1030–1045 | —  | Break    | |
| 1045–1200 | 11 | Lab      | ARIMA/SARIMA build: readiness trend forecast and logistics demand signal with 90% confidence bounds |
| 1200–1300 | —  | Lunch    | |
| 1300–1500 | 12 | Lab      | Monte Carlo: COA comparison framework, distribution selection rationale, 1,000-trial simulation (minimum), seed for reproducibility |
| 1500–1515 | —  | Break    | |
| 1515–1700 | 13 | Lab      | Sensitivity analysis; logistics stockage level risk modeling; quantifying probability at operationally meaningful thresholds |

**Evening reading:** TM-40G, Chapter 6 (Linear Programming) — review formulation and constraint documentation; TM-40G, Chapter 9 (Communicating Uncertainty) — read before the commander brief exercise on Day 5.

---

**Day 4 — Optimization and Decision Support**

| Time | Block | Method | Content |
|---|---|---|---|
| 0800–0830 | —  | Review   | Day 3 questions; Monte Carlo output review — confirm 1,000 trials, seed set, probability at threshold documented |
| 0830–1030 | 14 | Lab      | Linear programming: resource allocation formulation, constraint definition, scipy/lpSolve implementation |
| 1030–1045 | —  | Break    | |
| 1045–1200 | 15 | Lab      | Scheduling optimization: maintenance scheduling against operational commitments; sensitivity analysis on constraints |
| 1200–1300 | —  | Lunch    | |
| 1300–1500 | 16 | Lab      | Wargame/exercise data architecture: collection templates, aggregation pipelines, outcome measurement; post-exercise analysis pipeline build |
| 1500–1515 | —  | Break    | |
| 1515–1700 | 17 | Lab      | Quiver/Contour for ORSA: readiness forecast dashboard, COA comparison visualization, uncertainty bound display |

**Evening reading:** TM-40G, Chapter 9 (Communicating Uncertainty) — the briefing posture and what NOT to say sections. Review your full model output from this week — what would you brief to the G4?

---

**Day 5 — Commander Brief Standards and Practical Exercise**

| Time | Block | Method | Content |
|---|---|---|---|
| 0800–0900 | 18 | Lecture  | Communicating uncertainty: confidence intervals, prediction intervals, briefing posture, translating quantitative output to operational language |
| 0900–1000 | 19 | Discuss  | Common ORSA brief failures: point estimates without bounds, unqualified predictions, methods-paper language at a commanders' brief |
| 1000–1015 | —  | Break    | |
| 1015–1100 | 20 | Brief    | Practical exercise scenario brief; planning time; ORSA product standards checklist review |
| 1100–1200 | —  | Buffer   | Questions / environment check |
| 1200–1300 | —  | Lunch    | |
| 1300–1700 | 21 | **Eval** | **Practical exercise:** build regression + time series forecast + commander brief from provided dataset |

---

## Required Reading Summary

| When | Reading |
|---|---|
| Before Day 1 | TM-40G, Ch 1 (Introduction/prereq self-check) |
| Before Day 1 | TM-40G, Ch 2 Sec 2-1/2-2 (Code Workspace overview) |
| Day 1 evening | TM-40G, Ch 3 (Statistical Modeling — regression/validation) |
| Day 2 evening | TM-40G, Ch 4 (Time Series — ARIMA/confidence bounds) |
| Day 2 evening | TM-40G, Ch 5 (Monte Carlo — simulation framework) |
| Day 3 evening | TM-40G, Ch 6 (Linear Programming — formulation) |
| Day 3 evening | TM-40G, Ch 9 (Communicating Uncertainty) |
| Day 4 evening | TM-40G, Ch 9 (re-read briefing posture sections) |

---

## Practical Exercise

**Scenario:** The G4 requires a readiness forecast and risk analysis to support a theater sustainment planning session. Using a provided 12-month readiness dataset:

**Tasks:**
1. Configure Code Workspace and connect to the provided dataset; verify write transaction works before building models
2. Build a linear regression to identify readiness predictors; document validation statistics and model assumptions
3. Build an ARIMA time series forecast for the next 6 months with 90% confidence intervals; document model selection rationale (ACF/PACF analysis)
4. Run a Monte Carlo simulation comparing two sustainment COAs at D+30; produce probability distributions; set seed for reproducibility
5. Build a Quiver dashboard displaying the forecast with uncertainty bounds
6. Produce a commander brief (slide or written product) presenting findings — every point estimate must show its confidence range; explicitly state model assumptions and limitations; present in operational language the G4 can use

**Go standard:** Pass 5 of 6 tasks. Commander brief reviewed by ORSA evaluator (FA49 or equivalent) and meets ORSA product standards checklist. A brief that presents numbers without uncertainty characterization fails that element — this is a hard standard.

---

## What "Go" Looks Like

The practical brief is graded by a qualified ORSA evaluator. A brief that presents numbers without uncertainty characterization does not pass. If you brief "C2 probability of 78%" without confidence bounds, the evaluator will fail that element.

The model code must be readable and documented. Variable names must be interpretable; non-obvious logic requires inline comments. An ORSA product you cannot explain to another analyst does not meet the standard.

Monte Carlo: 1,000 trials minimum, seed set for reproducibility. The evaluator will ask to re-run the simulation — it must produce the same output.

---

## Tips From Previous Graduates

- The hardest shift is from "analysis in Excel" to "analysis in Foundry." The data is already there — you do not export it. Connect the Code Workspace to the Foundry dataset directly and write results back. Test the write transaction on Day 1 (Block 4), not Day 4. Trainees who skip this lose time they cannot recover.
- ARIMA model selection requires checking ACF/PACF plots. Do not skip this and guess at (p,d,q). The evaluator will ask why you chose your parameters — "I tried a few things" is not an answer.
- Monte Carlo: 100-trial simulations produce unstable distributions that will not pass. Set your seed for reproducibility before the evaluation.
- The commander brief is not a methods paper. The audience is a G4 or CG — they want "what is the probability we run out of Class IX by D+30 under each COA" not "we used ARIMA(1,1,0) with AIC model selection." Translate methods into operational language.
- Sensitivity analysis is consistently skipped in training due to time pressure. Read TM-40G, Chapter 5 before Day 3. The evaluator's questions on brief assumptions draw directly from it.

---

*USAREUR-AF Operational Data Team — UNCLASSIFIED*
*Syllabus TM-40G | Version 2.0 | March 2026*
