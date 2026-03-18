# COURSE SYLLABUS — TM-40G: OPERATIONS RESEARCH/SYSTEMS ANALYSIS (ORSA)
## Maven Smart System (MSS) — USAREUR-AF

| Field | Detail |
|---|---|
| **Level** | TM-40G (ORSA Specialist Track) |
| **Duration** | 5 days (40 hours) |
| **Prerequisites** | TM-10, TM-20, TM-30 (all Go evaluations on file — **REQUIRED**, not recommended); Data Literacy Technical Reference (recommended); graduate-level quantitative background (statistics, linear algebra, optimization); working proficiency in Python or R |
| **Audience** | FA49 Operations Research officers, quantitative analysts, ORSA-assigned civilians |
| **Format** | Instructor-led lab + guided practice + commander brief practical |
| **Location** | MSS Training Environment (Code Workspace provisioned) |

---

**BLUF:** TM-40G teaches ORSA analysts to translate operational questions into models inside Foundry — connecting to operational data, building quantitative models, and delivering products commanders can use to allocate resources and compare COAs. Course does not teach statistics from scratch; it applies existing quantitative skills to MSS data and USAREUR-AF ORSA product standards.

---

## Learning Objectives

| # | Objective |
|---|---|
| 1 | Configure a Python/R Code Workspace with required packages; verify Foundry dataset connectivity; write outputs back to Foundry curated datasets via transaction |
| 2 | Build and validate a regression model for a provided readiness or logistics dataset; document validation statistics and assumptions |
| 3 | Construct a time series forecast with documented model selection rationale, assumptions, and confidence bounds |
| 4 | Run a Monte Carlo simulation for a COA comparison scenario; quantify risk at defined probability thresholds |
| 5 | Formulate and solve a linear programming resource allocation problem with documented constraints and sensitivity analysis |
| 6 | Build analytical Quiver/Contour visualizations displaying model outputs with uncertainty bounds |
| 7 | Produce a commander brief presenting findings in operational language — every point estimate with a confidence range; explicitly stated assumptions and limitations |
| 8 | Apply USAREUR-AF ORSA product standards: documentation, validation, reproducibility (set seed), and uncertainty communication |

---

## Pre-Course Checklist

Complete **7–10+ duty days before Day 1:**

- [ ] Request **Code Workspace access** from C2DAO — standard unit MSS Administrator access is insufficient; allow 7–10 duty days
- [ ] Confirm the workspace runs a provided test script before Day 1 — if the test script fails, contact C2DAO before arriving
- [ ] Read TM-40G, Chapter 1 (Introduction, role, prerequisites self-check) — 30 min
- [ ] Read TM-40G, Chapter 2, Sections 2-1 and 2-2 (Code Workspace overview) — 20 min

---

## Daily Schedule

### Day 1 — Environment Setup and Foundry Data Access

| Time | Block | Method | Content |
|---|---|---|---|
| 0800–0900 | 1 | Brief | ORSA role on MSS; analytical product standards; the Foundry data model and how ORSA connects to it |
| 0900–1100 | 2 | Lab | Code Workspace setup: Python/R environment, package installation, GPU/CPU allocation, environment reproducibility |
| 1100–1115 | — | Break | |
| 1115–1200 | 3 | Lab | Foundry dataset connectivity: accessing Ontology datasets from Code Workspace, reading via Spark/pandas, inspecting schema |
| 1200–1300 | — | Lunch | |
| 1300–1500 | 4 | Lab | Writing outputs to Foundry: transaction pattern for writing results back to curated datasets — test this on Day 1, not Day 4 |
| 1500–1515 | — | Break | |
| 1515–1700 | 5 | Lab | Data profiling in Code Workspace: null distributions, outlier detection, feature distributions — building QC habits before modeling |

**Evening reading:** TM-40G, Chapter 3 (Statistical Modeling) — review regression and validation procedures.

---

### Day 2 — Statistical Modeling

| Time | Block | Method | Content |
|---|---|---|---|
| 0800–0830 | — | Review | Day 1 questions; Foundry write transaction troubleshooting |
| 0830–1030 | 6 | Lab | Regression: linear regression for readiness forecasting — feature selection, assumption checking, training, validation statistics |
| 1030–1045 | — | Break | |
| 1045–1200 | 7 | Lab | Classification models: logistic regression, decision trees — feature selection, cross-validation, calibration check |
| 1200–1300 | — | Lunch | |
| 1300–1500 | 8 | Lab | Model validation standards: residual analysis, cross-validation, documenting assumptions; writing validated output to Foundry |
| 1500–1515 | — | Break | |
| 1515–1700 | 9 | Lab | Practice build: apply regression to a second provided dataset; document model, write output to Foundry, build a Quiver visualization |

**Evening reading:** TM-40G, Chapter 4 (Time Series — ARIMA procedures and confidence bound requirements); Chapter 5 (Monte Carlo — simulation framework).

---

### Day 3 — Time Series and Monte Carlo

| Time | Block | Method | Content |
|---|---|---|---|
| 0800–0830 | — | Review | Day 2 questions; model documentation standards check |
| 0830–1030 | 10 | Lab | Time series: stationarity testing, ACF/PACF plot interpretation, ARIMA model identification — document why you chose (p,d,q) |
| 1030–1045 | — | Break | |
| 1045–1200 | 11 | Lab | ARIMA/SARIMA build: readiness trend forecast and logistics demand signal with 90% confidence bounds |
| 1200–1300 | — | Lunch | |
| 1300–1500 | 12 | Lab | Monte Carlo: COA comparison framework, distribution selection rationale, 1,000-trial simulation (minimum), seed for reproducibility |
| 1500–1515 | — | Break | |
| 1515–1700 | 13 | Lab | Sensitivity analysis; logistics stockage level risk modeling; quantifying probability at operationally meaningful thresholds |

**Evening reading:** TM-40G, Chapter 6 (Optimization — Resource Allocation and Scheduling: formulation and constraint documentation); Chapter 9 (Communicating Uncertainty).

---

### Day 4 — Optimization and Decision Support

| Time | Block | Method | Content |
|---|---|---|---|
| 0800–0830 | — | Review | Day 3 questions; Monte Carlo output review — confirm 1,000 trials, seed set, probability at threshold documented |
| 0830–1030 | 14 | Lab | Linear programming: resource allocation formulation, constraint definition, scipy/lpSolve implementation |
| 1030–1045 | — | Break | |
| 1045–1200 | 15 | Lab | Scheduling optimization: maintenance scheduling against operational commitments; sensitivity analysis on constraints |
| 1200–1300 | — | Lunch | |
| 1300–1500 | 16 | Lab | Wargame/exercise data architecture: collection templates, aggregation pipelines, outcome measurement; post-exercise analysis pipeline build |
| 1500–1515 | — | Break | |
| 1515–1700 | 17 | Lab | Quiver/Contour for ORSA: readiness forecast dashboard, COA comparison visualization, uncertainty bound display |

**Evening reading:** TM-40G, Chapter 9 (Communicating Uncertainty — briefing posture and what NOT to say). Review your full model output from this week — what would you brief to the G4?

---

### Day 5 — Commander Brief Standards and Practical Exercise

| Time | Block | Method | Content |
|---|---|---|---|
| 0800–0900 | 18 | Lecture | Communicating uncertainty: confidence intervals, prediction intervals, briefing posture, translating quantitative output to operational language |
| 0900–1000 | 19 | Discuss | Common ORSA brief failures: point estimates without bounds, unqualified predictions, methods-paper language at a commanders' brief |
| 1000–1015 | — | Break | |
| 1015–1100 | 20 | Brief | Practical exercise scenario brief; planning time; ORSA product standards checklist review |
| 1100–1200 | — | Buffer | Questions / environment check |
| 1200–1300 | — | Lunch | |
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
| Day 3 evening | TM-40G, Ch 6 (Optimization — Resource Allocation and Scheduling) |
| Day 3 evening | TM-40G, Ch 9 (Communicating Uncertainty) |
| Day 4 evening | TM-40G, Ch 9 (re-read briefing posture sections) |

---

## Practical Exercise

**Scenario:** The G4 requires a readiness forecast and risk analysis to support a theater sustainment planning session. Provided: a 12-month readiness dataset.

| # | Task |
|---|---|
| 1 | Configure Code Workspace; connect to the provided dataset; verify write transaction works before building models |
| 2 | Build a linear regression to identify readiness predictors; document validation statistics and model assumptions |
| 3 | Build an ARIMA time series forecast for the next 6 months with 90% confidence intervals; document model selection rationale (ACF/PACF analysis) |
| 4 | Run a Monte Carlo simulation comparing two sustainment COAs at D+30; produce probability distributions; set seed for reproducibility |
| 5 | Build a Quiver dashboard displaying the forecast with uncertainty bounds |
| 6 | Produce a commander brief presenting findings — every point estimate with confidence range; explicitly state model assumptions and limitations; present in operational language the G4 can use |

**Go standard:** Pass 5 of 6 tasks. Commander brief reviewed by ORSA evaluator (FA49 or equivalent) against the ORSA product standards checklist. A brief that presents numbers without uncertainty characterization fails that element.

---

## Go Criteria

| Task | Hard Standard |
|---|---|
| Commander brief | Numbers without uncertainty characterization do not pass — "C2 probability of 78%" without confidence bounds fails that element |
| Model code | Must be readable and documented — variable names interpretable; non-obvious logic requires inline comments |
| Monte Carlo | 1,000 trials minimum; seed set for reproducibility; evaluator will ask to re-run the simulation and it must produce the same output |

---

## Key Tips

| Risk | Guidance |
|---|---|
| Foundry write transaction | Test the write transaction on Day 1 (Block 4), not Day 4. Trainees who skip this lose time during the evaluation when the write fails |
| ARIMA model selection | Check ACF/PACF plots — do not guess at (p,d,q). The evaluator will ask why you chose your parameters |
| Monte Carlo trial count | 100-trial simulations produce unstable distributions that will not pass. Set seed for reproducibility before evaluation |
| Commander brief language | The audience is a G4 or CG — they want "probability we run out of Class IX by D+30 under each COA," not ARIMA model specification. Translate methods into operational language |
| Sensitivity analysis | Consistently skipped due to time pressure — read TM-40G, Chapter 5 before Day 3; evaluator questions on brief assumptions draw directly from it |

---

## Continuation

Graduates who remain in active ORSA roles and require theater-level analytical capability may pursue **TM-50G (Advanced ORSA)**. TM-50G covers Bayesian inference, agent-based simulation, multi-objective optimization, network analysis, and GO/SES-standard analytical products. Prerequisites: TM-40G Go evaluation on file; 18+ months active ORSA experience or concurrent graduate enrollment.

---

## Associated Exercises and Assessments

| Item | Reference |
|---|---|
| Pre-course exam | EXAM_TM40G_PRE |
| Post-course exam | EXAM_TM40G_POST |
| Practical exercise | EX_40G (EXERCISE.md + ENVIRONMENT_SETUP.md) |

---

## Relationship to WFF Tracks

WFF track analysts (TM-40A through TM-40F) are the operational consumers of ORSA products built in this course. ORSA practitioners should understand the analytical questions each WFF community brings to MSS: sustainment analysts (TM-40D) drive demand for logistics forecasts and resource allocation; intelligence analysts (TM-40A) consume risk and COA comparison products; movement and maneuver analysts (TM-40C) use optimization outputs for route and task organization analysis.

---

*USAREUR-AF Operational Data Team — UNCLASSIFIED*
*Syllabus TM-40G | Version 2.0 | March 2026*
