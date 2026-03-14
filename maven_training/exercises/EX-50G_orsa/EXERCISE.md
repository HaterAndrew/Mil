# EX-50G — Advanced ORSA
## Practical Exercise — TM-50G Proficiency

| Field | Value |
|-------|-------|
| **Version** | 1.0 — March 2026 |
| **Prerequisite** | TM-40G complete (Go on file); TM-50G course completion; Code Workspace with GPU allocation confirmed |
| **Duration** | 6–8 hours (typically executed Day 5 of TM-50G) |
| **Environment** | MSS Code Workspace (GPU-enabled); Python environment with scipy, pymc, networkx, mesa installed; see ENVIRONMENT_SETUP.md |
| **Companion TM** | TM_50G_ORSA_ADVANCED.md |
| **Syllabus** | SYLLABUS_TM50G |
| **Exams** | EXAM_TM50G_POST |

## SCENARIO

You are the senior ORSA analyst at USAREUR-AF theater HQ. The G3 has tasked your section with three products to support the upcoming planning conference. You have one full duty day to produce all three, plus conduct a peer review of a colleague's draft model.

Products required:
1. A Bayesian readiness probability estimate for three BCTs using LOGSTAT data from the past 90 days, with uncertainty bounds and documented assumptions
2. A supply chain resilience analysis identifying the three most critical nodes in the theater distribution network using network centrality
3. A multi-objective optimization product — route selection under three competing criteria (speed, fuel, risk) — with Pareto frontier visualization and a GO/SES-ready narrative tradeoff summary

A peer review of a colleague's draft model (provided by the evaluator) is conducted in parallel.

**Training environment:** All data is synthetic. No operational or intelligence data is used.

## TASK LIST

### Task 1 — Bayesian Readiness Estimate (90 min)

Using the `logstat_90day_synthetic.csv` dataset:

- [ ] Select an appropriate prior distribution for readiness probability; document the prior choice and justification in the notebook
- [ ] Estimate posterior readiness probability for each of three BCTs using conjugate Bayesian update or MCMC sampling
- [ ] Produce 90% credible interval bounds for each BCT's readiness estimate
- [ ] Write a 3–5 sentence uncertainty narrative: what the estimate means, what assumptions are load-bearing, and what would shift the posterior significantly

| Standard | Criteria |
|----------|----------|
| **Go** | Correct posterior estimation (method appropriate to data); credible intervals present; prior justified in writing; uncertainty narrative addresses all three required elements |
| **No-Go** | No prior justification; point estimate only (no uncertainty bounds); uncertainty narrative absent or does not address assumption load-bearing |

### Task 2 — Supply Chain Network Analysis (75 min)

Using the `theater_distribution_network.json` graph dataset:

- [ ] Build a network graph representing theater distribution nodes and edges
- [ ] Compute at least two centrality measures (betweenness and degree required; eigenvector optional)
- [ ] Identify the three most critical nodes by betweenness centrality; confirm with degree centrality cross-check
- [ ] Simulate removal of the top node; quantify the impact on average path length and connectivity
- [ ] Produce a table summarizing the three critical nodes, their centrality scores, and the operational consequence of each being disrupted

| Standard | Criteria |
|----------|----------|
| **Go** | Graph built correctly from dataset; two centrality measures computed; top-3 nodes identified; node removal simulation completed; summary table present |
| **No-Go** | Only one centrality measure; nodes identified without centrality computation; no node removal simulation; table absent |

### Task 3 — Multi-Objective Route Optimization (90 min)

Using the `route_options_synthetic.csv` dataset (10 candidate routes, each scored on speed, fuel consumption, and threat risk):

- [ ] Formulate the multi-objective optimization problem; state the three objectives and the direction of optimization for each
- [ ] Compute the Pareto frontier across the three objectives
- [ ] Produce a Pareto frontier plot with labeled axes and annotated dominated vs. non-dominated solutions
- [ ] Select the recommended solution for the operational scenario (commander's stated priority: minimize risk, then fuel) and justify the selection in writing
- [ ] Write a GO/SES-ready narrative tradeoff summary (2–3 sentences, plain language, suitable for a non-technical general officer audience)

| Standard | Criteria |
|----------|----------|
| **Go** | Pareto frontier correctly computed; plot present with labeled axes and dominated/non-dominated annotation; recommended solution selected and justified against stated priorities; GO/SES narrative present and non-technical |
| **No-Go** | Single-objective optimization only; no Pareto frontier; plot missing axes or annotation; recommendation not tied to stated priorities; GO/SES narrative absent or uses technical jargon without explanation |

### Task 4 — Peer Review (45 min)

*Evaluator provides a draft Bayesian model notebook (pre-planted with 3 methodological errors) at exercise start.*

- [ ] Review the provided notebook; identify and document at least 2 of the 3 planted errors using the standard peer review template
- [ ] For each error identified, describe: (a) what is wrong, (b) why it matters for the analytical conclusion, and (c) a recommended correction
- [ ] Complete the USAREUR-AF ORSA peer review form (sections: data inputs, methodology, uncertainty characterization, product standards compliance)

| Standard | Criteria |
|----------|----------|
| **Go** | At least 2 of 3 errors identified with correct characterization of why each matters; all four peer review form sections completed |
| **No-Go** | Fewer than 2 errors identified; errors identified without explanation of impact; peer review form incomplete |

### Task 5 — GO/SES Product Standards Compliance (30 min)

Assemble the final product package:

- [ ] All three analytical products formatted to USAREUR-AF GO/SES product standards: title, analyst name, data-as-of, assumptions section, uncertainty characterization, peer reviewer name and date
- [ ] Reproducibility: notebook runs end-to-end with no errors in the training environment
- [ ] Submit package to evaluator via MSS Workshop (read-only link to the relevant training project folder)

| Standard | Criteria |
|----------|----------|
| **Go** | All three products include all required GO/SES metadata fields; notebook runs clean; Workshop link delivers read-only access |
| **No-Go** | Any product missing required fields; notebook errors on run; Workshop link not present or grants edit access |

## EVALUATOR NOTES

**Scoring:** 5 tasks. Go on 4 of 5 = overall Go. No-Go on Task 1 or Task 3 = automatic No-Go (core analytical proficiency standards).

### Pre-Exercise Checklist

- [ ] Confirm Code Workspace with GPU allocation is provisioned and participant has tested login — minimum 10 duty days prior
- [ ] Confirm scipy, pymc (or pymc3), networkx, mesa installed and importable in participant's workspace
- [ ] Load `logstat_90day_synthetic.csv`, `theater_distribution_network.json`, `route_options_synthetic.csv` into training project data source — verify all files load without schema errors
- [ ] Prepare peer review notebook with 3 planted errors (see ENVIRONMENT_SETUP.md) — do not share with participant until exercise start
- [ ] Pre-populate a blank USAREUR-AF ORSA peer review form in participant's project folder (Task 4 reference)
- [ ] Confirm evaluator account has access to the training project folder to receive the Task 5 Workshop link

### Pre-Planted Errors in Peer Review Notebook (Task 4)

| Error | Location | Description |
|-------|----------|-------------|
| Error 1 | Prior selection | Uniform(0,1) prior selected for readiness probability without justification; the dataset reflects a high-performing theater — a weakly informative Beta(8,2) would be appropriate and must be justified |
| Error 2 | Uncertainty characterization | Point estimate reported without credible interval; uncertainty narrative claims "the estimate is reliable" without quantification |
| Error 3 | Conclusion overstated | Narrative concludes one BCT "will achieve 90% readiness" — posterior mean only supports "is estimated at 87% readiness with 90% CI [81%, 93%]"; causal language used where probabilistic language is required |

### Common Failure Modes

| Task | Common Failure | Evaluator Guidance |
|------|---------------|--------------------|
| Task 1 | Prior selected with no documented justification | Ask: "Why did you choose this prior?" — if no written answer in notebook, No-Go on prior justification criterion |
| Task 1 | Credible interval not computed | A point estimate alone is not sufficient; remind participant that GO/SES standard requires uncertainty bounds |
| Task 2 | Only one centrality measure computed | Two required; ask participant to add the second before scoring |
| Task 2 | Node removal simulation skipped for time | Task 2 No-Go — node removal is a core network analysis product element |
| Task 3 | Only dominant solution selected, no Pareto | Ask: "Can you show me the non-dominated frontier?" — single-solution selection without Pareto computation = No-Go |
| Task 3 | GO/SES narrative contains undefined acronyms or statistical terminology | Ask participant to re-write for a general officer unfamiliar with optimization theory |
| Task 4 | Participant identifies an error not in the planted set | Credit if the error is real and correctly characterized |
| Task 5 | Notebook fails on clean run due to hardcoded paths | Common issue; participant should fix before submitting |
