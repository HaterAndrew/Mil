# POST-TEST — TM-50G: ADVANCED ORSA
## Maven Smart System (MSS) — USAREUR-AF

| Field | Detail |
|---|---|
| **Course** | TM-50G: Advanced ORSA |
| **Form** | Post-Test |
| **Level** | TM-50G (Advanced Specialist) |
| **Audience** | FA49 / senior ORSA analysts; prerequisite: TM-40G + 18 months ORSA experience + graduate quantitative methods |
| **Time Allowed** | 45 minutes |
| **Passing Score** | 70% (42/60) |

---

## INSTRUCTIONS

This assessment evaluates mastery of course learning objectives. A passing score of 70% is required to receive credit. Complete independently without reference to training materials.

---

## SECTION 1 — MULTIPLE CHOICE

*Circle the letter of the best answer. (2 points each)*

**1. A multi-objective optimization problem with two conflicting objectives (maximize readiness, minimize cost) does NOT have a single "optimal solution" because:**

A. The problem is infeasible — conflicting objectives cannot be simultaneously optimized
B. The trade-off structure means any improvement in one objective worsens the other — the Pareto frontier represents all non-dominated solutions
C. The objective functions cannot both be linear if they conflict
D. Multi-objective problems require integer programming, which does not have a closed-form solution

**2. A stochastic optimization approach is preferred over a deterministic LP when:**

A. The problem has more than 100 decision variables
B. The feasible region is bounded by more than 10 constraints
C. Key parameters (demand, availability, failure rates) are uncertain and their probability distributions are known, enabling the optimizer to account for this uncertainty in the solution
D. The commander requires an answer within one hour

**3. A metaheuristic algorithm (e.g., simulated annealing, genetic algorithm) is used for optimization when:**

A. The problem has a known analytical solution that is computationally expensive
B. The problem is too complex for exact methods (non-convex, combinatorial) and a high-quality approximate solution is acceptable
C. The problem requires guaranteed global optimality
D. Sensitivity analysis must be performed on the solution

**4. In agent-based modeling calibration, the process of "fitting agent rules to historical data" risks which analytical failure?**

A. Overfitting individual agent rules to historical patterns at the expense of predictive validity under novel conditions
B. Under-specifying the number of agents, causing the model to fail to reproduce emergent behavior
C. Selecting an incorrect simulation timestep that causes numerical instability
D. Including too many agent types, increasing computational cost beyond available resources

**5. "D-separation" in a Bayesian network determines:**

A. Whether two variables have a direct causal relationship
B. Whether two variables are conditionally independent given a set of observed variables, based on the network structure
C. The direction of information flow between parent and child nodes
D. The strength of a causal relationship between two nodes

**6. A Bayesian network analysis of equipment failure uses conditional probability tables (CPTs). The CPT for a failure node given its parent nodes represents:**

A. The unconditional probability of failure regardless of parent node values
B. The marginal distribution of the failure node after integrating over all parent states
C. The sensitivity of the failure probability to changes in the prior distributions
D. The probability of failure for every combination of parent node states, enabling inference when some parent values are observed

**7. In a campaign analysis product for a corps commander, the ORSA's primary role is:**

A. Recommending a single preferred COA based on the analytical findings
B. Running the campaign simulation and validating results against classified intelligence estimates
C. Quantifying the expected outcomes and risk distributions for each COA, characterizing campaign-level uncertainty, and presenting decision-relevant findings in operational terms
D. Coordinating with the G3 to translate MDMP products into analytical inputs

**8. A DAUX robustness analysis shows that COA A performs acceptably in 18 of 20 scenarios while COA B performs acceptably in 12 of 20 scenarios. How should this be presented to the commander?**

A. "COA A is more robust across the scenario space (18/20 scenarios within acceptable performance bounds vs. 12/20 for COA B). The 2 scenarios where COA A fails are [scenarios]. This analysis does not account for probability weights across scenarios — the commander should consider which scenarios are operationally most likely."
B. "Recommend COA A — it is analytically superior."
C. "Both COAs are acceptable — there is no clear winner."
D. "The analysis is inconclusive — additional scenarios should be modeled before a recommendation is made."

**9. A hierarchical demand forecasting model produces forecasts at division, brigade, and battalion levels. When the battalion-level forecasts aggregate to a different total than the division-level forecast, the resolution method is:**

A. Always use the division-level forecast and recalculate battalion allocations proportionally
B. Present both levels' forecasts to the commander and let the G4 decide which to use
C. Apply reconciliation (top-down, bottom-up, or optimal combination) to ensure coherent forecasts at all levels
D. Use the higher of the two estimates to ensure no shortfall

**10. The TM-50G standard for uncertainty communication to a GO audience requires that every analytical finding include:**

A. A p-value demonstrating statistical significance
B. A plain-language characterization of uncertainty (e.g., scenario range, robustness score, or confidence bounds) alongside the point estimate or key finding
C. The full posterior distribution plot for each parameter
D. A note that all analyses are inherently uncertain and should not drive decisions

**11. An ensemble forecast that combines ARIMA, ETS, and TBATS model outputs for a supply consumption time series is MOST valuable when:**

A. The individual models disagree — ensemble reduces variance and avoids reliance on any single model assumption
B. The individual models agree — ensemble confirms accuracy
C. Only one of the three models is statistically significant at p < 0.05
D. The forecast horizon is less than four weeks

**12. For a wargame analysis product, the ORSA's documentation package must include at minimum:**

A. The wargame game cards and adjudication rules used by the controller
B. Commander's written approval of the analytical method before the wargame
C. The classified intelligence estimate used as the initial scenario conditions
D. Methodology, key assumptions, data sources, scenario parameters, analytical limitations, and a statement that results represent a specific scenario set — not a prediction

**13. A "state space model" for time series forecasting is preferred over a classical ARIMA model when:**

A. The underlying system has explicit structural components (trend, seasonality, irregular shocks) that change over time and can be modeled using a state evolution equation
B. The time series has fewer than 30 data points
C. The analyst needs a simpler model for GO-level briefing
D. The time series has been differenced to achieve stationarity

**14. TM-50G analytical product governance requires peer review by:**

A. The MSS program office before delivery
B. The G3 for operational relevance validation
C. The unit's Staff Judge Advocate for legal and ethical review
D. At least one other TM-50G qualified ORSA analyst before the product is delivered to the commander

**15. "Building persistent OR capability" at the command level means:**

A. Ensuring that ORSA models are stored in the SIPR network for long-term access
B. Purchasing commercial OR software licenses that persist beyond the current ORSA's assignment
C. Documenting methodology, training junior ORSAs, maintaining model reproducibility, and institutionalizing analytical standards so capability does not degrade with personnel turnover
D. Maintaining a 24/7 ORSA duty roster to provide continuous analytical support

---

## SECTION 2 — SHORT ANSWER

*Answer in 2–5 sentences. (6 points each)*

**SA-1. A theater-level resource allocation problem involves 15 units, 8 resource categories, competing operational priorities, and uncertainty in adversary actions. Explain why a simple LP is insufficient and describe the advanced OR methodology you would apply, including how you would handle the uncertainty dimension.**

&nbsp;

&nbsp;

&nbsp;

&nbsp;

**SA-2. You are asked to model how information spreads through a logistics network during a disruption event. Describe why an agent-based modeling approach is more appropriate than a system-dynamics model for this problem, and outline the key design decisions you would make in building the ABM.**

&nbsp;

&nbsp;

&nbsp;

&nbsp;

**SA-3. A corps G3 asks for a causal analysis of what factors drive unit readiness, not just correlation. Describe how you would build a causal model (DAG), what confounders you would need to control for, and how you would interpret the results operationally.**

&nbsp;

&nbsp;

&nbsp;

&nbsp;

**SA-4. You have been tasked to deliver a 5-minute analytical brief to a LTG on adversary sustainment capability. Your analysis has significant uncertainty. Apply the TM-50G GO/SES briefing standard: describe the structure of the brief, what you will state in the BLUF, how you will communicate uncertainty, and what backup slides you will have prepared.**

&nbsp;

&nbsp;

&nbsp;

&nbsp;

**SA-5. Describe the TM-50G approach to building persistent OR capability in a command. What are the four key components of a persistent capability program, and what is the most significant risk if this program is not maintained?**

&nbsp;

&nbsp;

&nbsp;

&nbsp;

---

## SCORING SUMMARY

| Section | Questions | Points Each | Total Points |
|---|---|---|---|
| Multiple Choice | 15 | 2 | 30 |
| Short Answer | 5 | 6 | 30 |
| **Total** | — | — | **60** |

Passing: 42/60 (70%) — Post-test only. Pre-test is diagnostic.

---

## ANSWER KEY — INSTRUCTOR USE ONLY

*Do not distribute to students.*

**Multiple Choice:**
1. B — Pareto frontier = all non-dominated solutions; no single solution improves all objectives.
2. C — Stochastic optimization is preferred when parameter uncertainty has known distributions.
3. B — Metaheuristics handle non-convex, combinatorial problems where exact methods are infeasible.
4. A — Overfitting historical patterns reduces predictive validity under novel (out-of-distribution) conditions.
5. B — D-separation determines conditional independence based on network structure.
6. D — CPT specifies probability of child node state for every combination of parent node states.
7. C — ORSA quantifies outcomes, characterizes risk distributions, and presents decision-relevant findings.
8. A — Present robustness scores with scenario context, note probability weights not included, defer decision.
9. C — Reconciliation (top-down, bottom-up, or optimal) ensures coherent forecasts at all levels.
10. B — Plain-language uncertainty characterization alongside findings is the TM-50G GO standard.
11. A — Ensemble is most valuable when individual models disagree, reducing reliance on any single model.
12. D — Documentation must include methodology, assumptions, data sources, scenario parameters, limitations, and scenario-vs-prediction disclaimer.
13. A — State space models handle explicit structural components that evolve over time.
14. D — Peer review by at least one other TM-50G qualified ORSA is required before commander delivery.
15. C — Persistent capability = documented methodology, trained junior ORSAs, reproducible models, institutionalized standards.

**Short Answer Guidance:**

SA-1. Full credit: simple LP assumes deterministic parameters and a single objective — neither holds here (uncertainty in adversary actions, multiple competing priorities); apply multi-objective stochastic programming or robust optimization; for the uncertainty dimension, model adversary action uncertainty via scenario tree or distributional robustness; present Pareto frontier to commander showing trade-off between competing objectives under different adversary scenarios; robustness analysis identifies allocations that remain feasible across the most scenarios. Must address both multi-objective AND uncertainty dimensions.

SA-2. Full credit: ABM is preferred because: (1) individual agents (units, supply officers, logistics nodes) make heterogeneous decisions; (2) information spread is a network phenomenon emerging from local interactions, not a top-down aggregate flow; (3) ABM captures bottlenecks and cascade failures that aggregate models miss; key design decisions: agent types and decision rules (unit logistics officers, supply nodes, transporters); network topology (who communicates with whom); disruption injection mechanism; output metrics (time to detection, spread rate, coverage); calibration dataset. Partial credit (3 pts) for correct reasoning without design decisions.

SA-3. Full credit: (1) draw a DAG of candidate causal factors (training hours, maintenance quality, leadership tenure, equipment age, operational tempo); (2) identify confounders: unit experience level (affects both training and readiness), deployment history (affects both maintenance and readiness); (3) apply backdoor criterion to identify which confounders to adjust for; (4) use causal estimator (IPW, regression adjustment, or IV) to estimate effect of each factor; (5) interpret operationally: "increasing scheduled maintenance by 10% causes readiness to increase by X percentage points, holding other factors constant." Must include DAG design, confounder identification, and operational interpretation.

SA-4. Full credit: BLUF (15 seconds): "Adversary sustainment capability is assessed as degraded. Key finding: [range]. Primary uncertainty: [variable]. Decision required: [specific action]"; uncertainty communication: present range estimate with explicit scenario assumptions (not a single point); note that the finding depends critically on [key assumption] — brief backup scenarios; structure: BLUF → key finding with range → top 2 supporting data points → what we don't know → decision required; backup slides: methodology, full scenario analysis, data sources, assumptions, sensitivity chart. 5-minute constraint means no technical detail in the main brief.

SA-5. Full credit: four components — (1) documented methodology and reproducible models (code + data + random seeds archived); (2) junior ORSA training and mentorship program with progressive complexity; (3) institutional analytical standards (TM-50G product standards, peer review requirement); (4) model maintenance schedule (retraining, re-calibration as operational data changes); most significant risk of non-maintenance: analytical capability becomes resident in one or two senior ORSAs who PCS — command loses the capability entirely at a personnel transition, forcing rebuilding from scratch at the next critical decision point.

---

*USAREUR-AF Operational Data Team — UNCLASSIFIED*
*TM-50G Post-Test | Version 1.0 | March 2026*
