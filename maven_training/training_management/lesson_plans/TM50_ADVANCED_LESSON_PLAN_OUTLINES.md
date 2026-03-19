# LESSON PLAN OUTLINES — TM-50 ADVANCED SPECIALIST TRACKS
## USAREUR-AF Operational Data Team — C2DAO
**Covers:** TM-50G (Advanced ORSA) | TM-50H (Advanced AI Engineer) | TM-50M (Advanced ML Engineer) | TM-50J (Advanced PM) | TM-50K (Advanced KM) | TM-50L (Advanced SWE) | TM-50N (Advanced UX Designer) | TM-50O (Advanced Platform Engineer)
**Version:** 1.0 — March 2026

> Abbreviated LP outlines for TM-50 advanced courses.
> TM-50 instructors must hold the corresponding TM-40 certification and active domain SME status at the advanced level. These outlines supplement deep domain expertise — they do not replace it.
> Expand individual blocks using `LP_TEMPLATE.md` as needed. For full lesson plan format reference, see `TM10/TM10_LESSON_PLANS.md`.

**Duration summary:**
- TM-50G, H, M, L: 5 days (40 hours)
- TM-50J, K, N, O: 3 days (24 hours)

**Prerequisite note:** TM-50 courses are NOT required for the majority of specialist billets. Before confirming enrollment, verify the trainee is in an active role that requires TM-50-level work. Refer to each syllabus for the prerequisite warning.

---

# PART G — TM-50G: ADVANCED ORSA

**Duration:** 5 days (40 hours) | **T:I ratio:** 4:1 | **Instructor req:** FA49 O-4+ or equivalent, TM-50G certified or C2DAO Advanced ORSA SME; active analytical practice at theater level

---

### Block 1 — TM-50G Standards and Product Requirements
**Hours:** 1.0 | **Method:** Seminar | **Day:** 1 | **Time:** 0800–0900

**Purpose:** The product standard at TM-50G is not just technical correctness — it is interpretability, peer reviewability, and honest uncertainty characterization for GO/SES audiences. This block establishes that standard before any method is taught.

**TLO:** The trainee will state the four non-negotiable TM-50G product standards: uncertainty quantification on all estimates, documented assumption register, peer review complete and on file, and full model reproducibility.

**Key Delivery Notes:**
- The difference between TM-40G products and TM-50G products: TM-40G products answer "what is the readiness?" TM-50G products answer "what is the readiness, how confident are we, under what assumptions, and what would change the answer?"
- Peer review is not optional at TM-50G. Every product submitted for GO/SES use must have a peer review signature block.
- Reproducibility: set random seeds. Document package versions. A result that cannot be reproduced is not a result — it is a point estimate with no analytical foundation.

**Assessment:** Standards are evaluated during the Day 5 practical exercise debrief. Evaluator will ask the trainee to point to each of the four non-negotiables in their submitted product.

**New doctrine content (March 2026):** MOE/MOP assessment framework at theater level, CARVER scoring for multi-echelon risk prioritization, and force ratio computation integrated with Bayesian models. Reference in Blocks 1, 10–11, and 21–22.

---

### Block 2 — Bayesian Inference: Prior Selection and Posterior Estimation
**Hours:** 2.0 | **Method:** Lab | **Day:** 1 | **Time:** 0900–1100

**Purpose:** Bayesian inference is the appropriate framework for operational analysis under uncertainty — it forces explicit prior assumption documentation and produces interpretable probability estimates rather than binary confidence intervals.

**TLO:** The trainee will implement a Bayesian model in Python (PyMC or equivalent) for an operational readiness problem — selecting a justified prior, estimating the posterior, and documenting the prior assumption in the assumption register.

**Key Delivery Notes:**
- Prior selection is an analytical decision, not a default. "Uniform prior" is a decision. Document it with a justification.
- Use operational examples: binomial/beta model for readiness probability, Poisson/gamma for event arrival rates (maintenance requests, failure events).
- Posterior interpretation: the posterior is a probability distribution, not a point estimate. Present the full distribution. Then communicate the mode or mean and the credible interval.
- Common error: selecting an informative prior without documenting where the prior came from. If the prior came from historical readiness data, cite the data. If it is expert judgment, cite the expert and date.

**Student Activity:** Implement a beta-binomial readiness model on the provided operational dataset. Document the prior selection in the assumption register template. Plot the posterior distribution. State the 90% credible interval.

**Assessment:** Evaluated as component of Day 5 Practical Exercise Part 1.

---

### Block 3 — Conjugate Priors and Binomial/Beta Models
**Hours:** 0.75 | **Method:** Lab | **Day:** 1 | **Time:** 1115–1200

**Key Delivery Notes:**
- Conjugate priors simplify computation and provide interpretable closed-form solutions — appropriate when the operational context fits the conjugate family.
- Binomial/beta: readiness proportion estimation (X of N systems are mission-capable). Beta parameters have an intuitive interpretation as "pseudo-observations."
- Hands-on: parameterize the beta prior from historical readiness records. Show how adding each new observation updates the posterior sequentially.

---

### Block 4 — Hierarchical Bayesian Models
**Hours:** 2.0 | **Method:** Lab | **Day:** 1 | **Time:** 1300–1500

**Purpose:** Multi-echelon operational data (battalion, brigade, division) has natural hierarchical structure. Hierarchical Bayesian models share statistical strength across echelons — a battalion with few observations borrows strength from the brigade-level posterior.

**TLO:** The trainee will implement a hierarchical Bayesian model pooling readiness data across three echelons — comparing complete pooling, no pooling, and partial pooling — and state when each approach is appropriate.

**Key Delivery Notes:**
- Complete pooling: one estimate for all echelons. Ignores echelon differences. Fast, but inappropriate when echelons have structurally different readiness profiles.
- No pooling: separate estimate per echelon. Appropriate when echelon differences are structural. Insufficient data per echelon is the failure mode.
- Partial pooling (hierarchical): echelon estimates shrink toward the group mean. Appropriate for most operational multi-echelon problems.
- Communication: translate partial pooling into plain language for the GO/SES brief. "We used shared evidence across battalions to inform each battalion's estimate, which improves precision where data is sparse."

**Assessment:** Evaluated in Day 5 Practical Exercise Part 1.

---

### Block 5 — Bayesian Updating
**Hours:** 1.75 | **Method:** Lab | **Day:** 1 | **Time:** 1515–1700

**Purpose:** Operational analysis is not a one-time product. Bayesian updating formalizes the process of incorporating new evidence without discarding prior analysis.

**TLO:** The trainee will implement a Bayesian update cycle — incorporating a new LOGSTAT submission into an existing readiness posterior — and produce a product showing the pre-update and post-update estimates with the delta quantified.

**Key Delivery Notes:**
- The prior for the update is the previous posterior. This is the mathematical mechanism — make it explicit in the code and in the product.
- Sequential analysis patterns: if LOGSTAT arrives daily, the model updates daily. Configure the pipeline to accept new data without full retraining.
- Document the update in the assumption register: "Posterior updated [DTG] incorporating LOGSTAT from [unit list]. Previous estimate [X% ± Y%]. Updated estimate [A% ± B%]."

---

### Block 6 — Agent-Based Simulation
**Hours:** 2.0 | **Method:** Lab | **Day:** 2 | **Time:** 0830–1030

**Purpose:** Agent-based models capture emergent behavior in complex operational systems — logistics convoys, attrition dynamics, route network congestion — that equation-based models cannot represent.

**TLO:** The trainee will build a logistics convoy agent-based simulation using Mesa or equivalent, define agent behaviors and environment interaction rules, and produce a results distribution over at least 100 simulation runs.

**Key Delivery Notes:**
- Agent definition: each agent has state variables (load, current location, remaining fuel, status) and behavior rules (move toward destination, stop if fuel below threshold, re-route if blocked).
- Environment: define the grid or network the agents operate in. For a logistics convoy simulation: a route network with node capacities and arc transit times.
- Run multiple simulations (Monte Carlo): ABS results are stochastic. A single run is not a result. Run 100+ simulations and report the distribution of outcomes.
- Seed: set and document the random seed for every production run. Results must be reproducible.

**Assessment:** Evaluated as component of Day 5 Practical Exercise.

---

### Block 7 — Calibration and Validation
**Hours:** 1.25 | **Method:** Lab | **Day:** 2 | **Time:** 1045–1200

**Purpose:** An uncalibrated model is worse than no model — it produces precise wrong answers. Calibration and validation are non-negotiable before any ABS result enters a commander decision product.

**TLO:** The trainee will conduct a parameter sensitivity sweep, identify the parameters with the highest influence on simulation output, and compare simulation output against a historical analogue — documenting calibration decisions in the assumption register.

**Key Delivery Notes:**
- Parameter sweep: vary one parameter at a time across a plausible range. Identify which parameters move the output distribution by more than 10% — these are the "key parameters" requiring the most careful calibration.
- Historical comparison: find a historical scenario (exercise, real operation) with known outcomes. Run the model against the historical inputs and compare the output to the known outcome. Document the difference.
- If calibration fails significantly: do not present the model as validated. Present it as a tool for exploring "what-if" scenarios, not for estimating expected outcomes.

---

### Block 8 — Network Analysis: Centrality and Flow
**Hours:** 2.0 | **Method:** Lab | **Day:** 2 | **Time:** 1300–1500

**Purpose:** Operational networks (supply chains, communications, route networks, task organization hierarchies) are amenable to graph-theoretic analysis. Centrality and flow measures translate directly into operational language.

**TLO:** The trainee will construct a supply chain network graph, compute centrality measures (degree, betweenness, eigenvector), and identify critical nodes — translating graph centrality into an operational risk recommendation.

**Key Delivery Notes:**
- Graph construction: nodes = logistics nodes (BSA, FSB, POD, POE), arcs = routes with capacity and transit time as edge attributes. Build from the logistics dataset.
- Betweenness centrality: which nodes carry the most "flow"? These are the supply chain choke points. High betweenness + single path = fragile node.
- Operational translation: "Node X has the highest betweenness centrality in the supply network. Degrading Node X reduces network flow by 40% in our simulation. Risk: HIGH."
- Shortest path and max-flow: use for route planning (fastest/most capacity path from POD to supported element).

**Assessment:** Evaluated in Day 5 Practical Exercise.

---

### Block 9 — Network Vulnerability Analysis
**Hours:** 1.75 | **Method:** Lab | **Day:** 2 | **Time:** 1515–1700

**Purpose:** Extends Block 8 from descriptive to prescriptive — what happens when critical nodes are removed, and what does that imply for network hardening or alternate route planning?

**TLO:** The trainee will systematically remove high-centrality nodes from the supply network graph, measure the impact on network connectivity and maximum flow, and produce a node priority list for network hardening.

**Key Delivery Notes:**
- Sequential node removal: remove the highest-betweenness node, recompute flow, record the degradation. Repeat for the next-highest. This produces an ordered vulnerability list.
- Connectivity: after each removal, check whether the network remains connected (all nodes reachable from the source). Disconnection is a catastrophic failure mode.
- Network hardening recommendation: nodes where removal drops flow by >25% or disconnects the network are "critical" and warrant redundant route development or alternative sourcing.

---

### Block 10 — Multi-Objective Optimization
**Hours:** 2.0 | **Method:** Lab | **Day:** 3 | **Time:** 0830–1030

**Purpose:** Theater-level planning problems routinely involve competing objectives (cost vs. risk, speed vs. sustainability). Multi-objective optimization maps the tradeoff space and enables commanders to make explicit tradeoff decisions rather than implicit ones.

**TLO:** The trainee will formulate a two-objective optimization problem (e.g., minimize supply cost vs. minimize supply chain risk), compute the Pareto frontier using scipy.optimize or equivalent, and produce a Pareto frontier visualization with at least 3 named COA points.

**Key Delivery Notes:**
- Objective function design: each objective must be quantifiable from operational data. "Minimize risk" must become "minimize expected supply disruption probability" with a defined formula.
- Pareto frontier: a set of solutions where you cannot improve one objective without degrading another. Every point on the frontier is a legitimate COA — the commander chooses based on priorities.
- COA naming: select 3–5 points on the frontier and name them operationally. "COA A: Minimum Cost (high risk)," "COA B: Balanced," "COA C: Minimum Risk (high cost)." The commander selects; the analyst does not.

**Assessment:** Evaluated in Day 5 Practical Exercise.

---

### Block 11 — Communicating Pareto Tradeoffs to Commanders
**Hours:** 1.25 | **Method:** Lab | **Day:** 3 | **Time:** 1045–1200

**Purpose:** A Pareto frontier that a general cannot interpret is an analytical product that will not influence decisions. Translating the frontier into operational language is as important as computing it.

**TLO:** The trainee will present a Pareto tradeoff brief to the evaluator (playing a GO role) — communicating the tradeoff space, the three named COAs, and a recommendation with explicit assumption caveats — without using technical optimization vocabulary.

**Key Delivery Notes:**
- BLUF first: "G4, we have two objectives in tension: minimize cost and minimize risk. We computed the range of feasible solutions. Here are three COAs at different points on that range."
- Do not say "Pareto frontier" to a GO/SES audience. Say "the range of feasible options where improving one objective requires accepting more of the other."
- Recommendation structure: state your recommended COA, the operational rationale, the key assumption, and the condition that would change the recommendation.

---

### Block 12 — Ensemble Methods and Out-of-Sample Validation
**Hours:** 2.0 | **Method:** Lab | **Day:** 3 | **Time:** 1300–1500

**Purpose:** Ensemble models are more reliable than individual models for operational prediction tasks. But reliability must be demonstrated with rigorous out-of-sample validation — not just in-sample fit.

**TLO:** The trainee will implement a stacking ensemble (at least 3 base learners) with a holdout validation set, report the bias-variance decomposition, and document the model complexity justification.

**Key Delivery Notes:**
- Base learners: select diverse learners (e.g., gradient boosting + ridge regression + random forest). Diversity in base learner error patterns is what makes stacking valuable.
- Out-of-sample validation: strict temporal split (train on data before T, validate on data after T) for operational time-series data. Never random split for time-ordered operational data.
- Bias-variance documentation: report training error vs. validation error. High training / low validation = overfit. Document the complexity choice and its justification.

---

### Block 13 — Limitation Documentation Standards
**Hours:** 1.75 | **Method:** Lab | **Day:** 3 | **Time:** 1515–1700

**Purpose:** An ORSA product without a documented limitations section is incomplete. Limitations tell the commander when NOT to use the model — which is as important as telling them when to use it.

**TLO:** The trainee will produce a complete limitations register for their ensemble model — covering data limitations, modeling assumptions, out-of-sample validity boundaries, and conditions that would invalidate the model.

**Key Delivery Notes:**
- Data limitations: what data was missing, imputed, or excluded? What is the time window of training data? Is there a survivorship bias in the data?
- Modeling assumptions: what assumptions are embedded in the model structure? (e.g., "assumes stationarity of the readiness process over the training window")
- Validity boundary: the model is valid under [DESCRIBED CONDITIONS]. If conditions change (theater OPORD changes, new equipment type introduced), the model must be retrained.
- Invalidation conditions: explicit statements of the form "If [X happens], this model's predictions should not be trusted." Every analyst should be able to state at least three invalidation conditions.

---

### Block 14 — GO/SES ORSA Product Standards
**Hours:** 1.0 | **Method:** Seminar | **Day:** 4 | **Time:** 0800–0900

**Purpose:** TM-50G products are briefed to GO/SES audiences. The product format is not optional — it is the standard that makes the analysis actionable at that level.

**Key Delivery Notes:**
- Required sections: BLUF, methodology (1 paragraph, accessible), results with uncertainty quantification, assumption register, limitations, recommendation, and peer review signature block.
- BLUF format: "Bottom line: [result]. Confidence: [HIGH/MEDIUM/LOW with quantified basis]. Key assumption: [most load-bearing assumption]. If you change [assumption], the answer changes to [X]."
- Peer review signature block: reviewer name, date, and a one-sentence summary of what was reviewed. Without this block, the product cannot be forwarded to GO/SES.

---

### Block 15 — Draft Analytical Product Workshop
**Hours:** 2.0 | **Method:** Workshop | **Day:** 4 | **Time:** 0900–1100

**Purpose:** Trainees apply the TM-50G product standard to an operational problem from their own experience. The product from this block is the basis for the Day 4 peer review.

**TLO:** The trainee will produce a draft TM-50G-standard analytical product from their prepared operational problem — covering all required sections — for peer review.

**Key Delivery Notes:**
- Each trainee works on their own prepared problem (from pre-course checklist). Instructor circulates for individual guidance.
- Block focus: getting the BLUF and uncertainty section right. These are the most commonly incomplete sections.
- Product does not need to be polished — it needs to be reviewable. Peer reviewers will use the structured checklist.

---

### Block 16 — Individual Instructor Feedback
**Hours:** 0.75 | **Method:** Workshop | **Day:** 4 | **Time:** 1115–1200

**Key Delivery Notes:**
- Instructor meets 1:1 with each trainee for 8–10 minutes. Primary feedback targets: (1) BLUF clarity, (2) uncertainty quantification completeness, (3) assumption register coverage.
- Note gaps for each trainee before the peer review — what the peer reviewers should look for.

---

### Block 17 — Structured Peer Review
**Hours:** 2.0 | **Method:** Peer Review | **Day:** 4 | **Time:** 1300–1500

**Purpose:** Peer review at TM-50G is a professional practice, not a social courtesy. The reviewer's job is to find the methodological weaknesses before the product reaches a commander.

**TLO:** The trainee will review a peer's product using the TM-50G peer review checklist — identifying at least one methodological weakness and one limitation gap — and deliver the review in writing using the prescribed review format.

**Key Delivery Notes:**
- Checklist items: (1) BLUF present and complete, (2) uncertainty quantified with bounds and basis, (3) assumption register complete (every assumption listed), (4) limitations register present and realistic, (5) reproducibility confirmed (code runs without modification), (6) recommendation does not exceed the analytical foundation.
- Written review: reviewer completes the checklist and adds a narrative summary (2–5 sentences). The narrative should be direct: "The model does not document the prior selection justification for the Brigade-level prior. This needs to be addressed before this product can be forwarded."
- Professional standard: critique the product, not the analyst. Every comment must be actionable.

---

### Block 18 — Peer Review Debrief and Product Revision
**Hours:** 1.75 | **Method:** Debrief | **Day:** 4 | **Time:** 1515–1700

**Key Delivery Notes:**
- Class-level debrief: instructor highlights the 3–4 most common peer review findings across all products. These become the Day 5 evaluation focus areas.
- Individual revision time: trainees incorporate peer review feedback into their products before Day 5 evaluation.
- Evening work: trainees finalize products. The evaluator expects that Day 4 peer review feedback has been addressed in the Day 5 submission.

---

### Block 19 — Product Revision and Evaluation Brief
**Hours:** 1.0 | **Method:** Review | **Day:** 5 | **Time:** 0800–0900

**Key Delivery Notes:**
- Final revision questions (30 min). Confirm all four non-negotiables are present in every trainee's product before the evaluation begins.
- Evaluation brief (30 min): state the Day 5 scenario and the two evaluation parts. Trainees know the evaluation structure before it begins — there should be no surprises.

---

### Block 20 — Practical Exercise Scenario Brief
**Hours:** 1.0 | **Method:** Brief | **Day:** 5 | **Time:** 0900–1000

**Key Delivery Notes:**
- Issue scenario brief. Trainees have the break period to review requirements before Part 1 begins.
- Scenario: theater-level logistics analysis. G4 requires: Bayesian readiness probability estimate for two maneuver brigades, supply chain resilience analysis (network), and multi-objective optimization of two sustainment COAs.

---

### Block 21 — Practical Exercise Part 1: Advanced Method Application
**Hours:** 2.25 | **Method:** Evaluation | **Day:** 5 | **Time:** 1015–1200

**Tasks:** (1) Implement Bayesian readiness probability model for both brigades — posterior estimates with 90% credible intervals and documented priors. (2) Construct supply chain network and compute betweenness centrality — identify top 3 critical nodes with operational risk rating. (3) Run Pareto optimization of the two sustainment COAs — plot frontier and name 3 COA points.

**Go standard:** All three method components complete. Bayesian credible intervals present. Network analysis identifies critical nodes with operational translation. Pareto frontier computable and plotted.

---

### Block 22 — Practical Exercise Part 2: GO/SES Product
**Hours:** 3.0 | **Method:** Evaluation | **Day:** 5 | **Time:** 1300–1600

**Tasks:** Produce a GO/SES-ready analytical product from Part 1 results. Required sections: BLUF, methodology, results with uncertainty, assumption register, limitations register, recommendation, peer review signature block. Submit in writing.

**Go standard:** Pass 4 of 5 product elements. Required: uncertainty quantification on all estimates, assumption register present, peer review complete, models reproducible. Hard No-Go: no credible intervals on readiness estimates; peer review block missing.

---

### Block 23 — Evaluator Feedback and Graduation
**Hours:** 1.0 | **Method:** Review | **Day:** 5 | **Time:** 1600–1700

**Key Delivery Notes:**
- Individual feedback: evaluator meets with each trainee for 8–10 minutes. Communicate Go/No-Go, specific strengths, and the one highest-priority improvement area.
- Class debrief: common gaps across the cohort. This feedback informs the next course iteration.

---

## TM-50G COURSE COMPLETION

TM-50G graduates are eligible to take TM-50H, TM-50M, or TM-50J as peer tracks. No additional prerequisites beyond domain experience.

---

---

# PART H — TM-50H: ADVANCED AI ENGINEERING

**Duration:** 5 days (40 hours) | **T:I ratio:** 4:1 | **Instructor req:** Senior AI engineer with enterprise production AI system experience; TM-50H certified or C2DAO AI Architecture SME
**Advanced access required:** AIP Logic (multi-agent features), Python Transforms, embedding model access

---

### Block 1 — Enterprise AI Standards and the Demo-to-Production Gap
**Hours:** 1.0 | **Method:** Seminar | **Day:** 1 | **Time:** 0800–0900

**TLO:** The trainee will distinguish enterprise AI system requirements from prototype AI requirements, and describe the four domains where production AI systems fail: retrieval quality, prompt brittleness, orchestration failure, and governance gaps.

**Key Delivery Notes:**
- The demo-to-production gap: a prototype that impresses in a demo can fail in production due to edge-case queries, corpus updates, model API changes, or load at scale. This course addresses all four failure domains.
- Enterprise requirements: reproducibility, auditability, human review gates, rollback procedures, version control on prompts and data — none of these exist in a prototype.
- Instructor opens with a real failure pattern: an AI system that passed all demo scenarios but failed on 30% of production queries because the retrieval system returned empty results on short queries. This is the course motivation.

**New doctrine content (March 2026):** ADP 3-13 AI/ML framing at enterprise scale, PED-to-pipeline mapping for multi-source intelligence-AI integration, and UDRA governance framework for enterprise AI data access controls. Reference in Blocks 2–5 (RAG architecture), 14 (AI governance), and 19–20 (practical exercise).

---

### Block 2 — Enterprise RAG Pipeline Architecture
**Hours:** 2.0 | **Method:** Lab | **Day:** 1 | **Time:** 0900–1100

**TLO:** The trainee will design a RAG pipeline architecture — chunking strategy, metadata schema, and ingestion flow — for a provided document corpus, justifying each design decision against the retrieval quality tradeoffs.

**Key Delivery Notes:**
- Chunking strategy tradeoffs: fixed-size (fast, loses semantic coherence at boundaries), semantic (slow, better retrieval relevance), sentence-level (granular, higher storage). No universal answer — choose based on query pattern.
- Metadata schema: every chunk must have metadata (source document, date, section, classification level). Metadata enables filtered retrieval and supports OPSEC classification handling.
- Ingestion flow: document source → preprocessing (clean, deduplicate) → chunking → embedding → vector store. Each step needs error handling; a bad document at ingestion should not crash the pipeline.

**Assessment:** Architecture review component of Day 5 evaluation.

---

### Block 3 — Embedding Model Selection and OPSEC Implications
**Hours:** 0.75 | **Method:** Lab | **Day:** 1 | **Time:** 1115–1200

**Key Delivery Notes:**
- Embedding model criteria: retrieval quality (benchmark on your actual query set, not on standard benchmarks), inference latency, and OPSEC posture (external API vs. on-premises model).
- OPSEC critical point: documents sent to an external embedding API are transmitted off-premises. For operationally sensitive content, on-premises embedding is required. Confirm classification of the corpus before selecting an embedding provider.
- Evaluate retrieval quality by testing the embedding model on 20–30 representative queries. Check whether the correct documents are in the top-3 results.

---

### Block 4 — Hybrid Retrieval and Re-ranking
**Hours:** 2.0 | **Method:** Lab | **Day:** 1 | **Time:** 1300–1500

**TLO:** The trainee will implement a hybrid retrieval pipeline combining dense (vector) and sparse (BM25) retrieval, apply a re-ranking step, and evaluate retrieval quality using Mean Reciprocal Rank (MRR) on a held-out query set.

**Key Delivery Notes:**
- Why hybrid: dense retrieval is strong on semantic similarity but weak on exact-match queries (abbreviations, unit designators, specific dates). BM25 is strong on keyword match. Combining both improves robustness.
- Fusion: reciprocal rank fusion (RRF) is the standard method for combining rankings from multiple retrieval systems. Simple and effective.
- Re-ranking: a cross-encoder re-ranker scores each candidate document against the query and reorders. Compute-intensive but significantly improves top-3 precision.
- MRR evaluation: for each test query, what rank is the first relevant document? Average MRR across the test set. Target: MRR > 0.7 before calling retrieval "good."

---

### Block 5 — Retrieval Evaluation Harness
**Hours:** 1.75 | **Method:** Lab | **Day:** 1 | **Time:** 1515–1700

**TLO:** The trainee will build an automated retrieval quality evaluation harness — ground truth query set, MRR computation, and a regression test that flags retrieval degradation when the corpus or embedding model changes.

**Key Delivery Notes:**
- Ground truth query set: 30–50 representative queries with known-good answer documents. This must be built manually — synthetic query generation is a shortcut that produces low-quality test sets for operational corpora.
- Regression test: run the harness on every corpus update or model version change. If MRR drops >5% from baseline, flag for human review before promoting the update.
- Version the ground truth set with the corpus. As the corpus grows, add new test queries to maintain coverage.

---

### Block 6 — Prompt Engineering for Production Systems
**Hours:** 2.0 | **Method:** Lab | **Day:** 2 | **Time:** 0830–1030

**TLO:** The trainee will design a production-quality system prompt with a structured few-shot template, output format enforcement via JSON schema, and a versioned prompt registry entry.

**Key Delivery Notes:**
- System prompt architecture: role definition, behavioral constraints, output format, few-shot examples. All four must be present in a production system prompt.
- Output format enforcement: instruct the model to produce JSON matching a specified schema. Validate every output against the schema before processing. Reject non-conforming outputs — do not parse them.
- Prompt versioning: every change to a production prompt is a version. Track versions in the prompt registry. Rollback must be possible within 15 minutes.
- OPSEC: system prompts in operational AI systems may contain classification-sensitive instructions. Apply classification handling to the prompt registry itself.

---

### Block 7 — Chain-of-Thought and Reliability Patterns
**Hours:** 1.25 | **Method:** Lab | **Day:** 2 | **Time:** 1045–1200

**Key Delivery Notes:**
- Chain-of-thought: instructs the model to reason step by step before answering. Reliably improves accuracy on multi-step reasoning tasks. Does NOT help on factual recall tasks.
- Step-back prompting: ask the model to identify the general principle before addressing the specific question. Useful for operational analysis tasks where classification of the problem matters.
- Self-consistency: run the prompt N times, take the majority-vote answer. Increases reliability at the cost of latency and token usage. Use only when the output is binary or categorical.
- When NOT to use CoT: simple classification, factual lookup, format transformation. Adding CoT adds tokens and latency for no reliability gain.

---

### Block 8 — Adversarial Robustness for Operational AI
**Hours:** 2.0 | **Method:** Lab | **Day:** 2 | **Time:** 1300–1500

**TLO:** The trainee will identify at least 3 prompt injection attack patterns relevant to operational AI systems and implement at least 2 mitigation strategies — testing both attack and mitigation on the training system.

**Key Delivery Notes:**
- Prompt injection: a user input that overrides the system prompt's instructions. Pattern: "Ignore previous instructions and..." Mitigation: input sanitization, instruction hierarchy enforcement, output validation.
- Data extraction: an attacker queries the system to reconstruct documents from the retrieval corpus. Mitigation: limit the number of retrieved documents returned to users; do not include raw chunk text in the output.
- OPSEC relevance: operational AI systems may retrieve classified or sensitive information. Adversarial inputs that cause the system to over-share are a significant OPSEC risk.
- Testing: run the attack patterns against the training system. Document which attacks succeed and which are mitigated. Document both results — the evaluator will ask.

---

### Block 9 — Prompt Regression Testing and Version Control
**Hours:** 1.75 | **Method:** Lab | **Day:** 2 | **Time:** 1515–1700

**TLO:** The trainee will implement an automated prompt regression test suite that compares output distributions between prompt versions — flagging significant changes for human review before production promotion.

**Key Delivery Notes:**
- Test suite: 30–50 test prompts with expected output characteristics (not exact match — LLM outputs are non-deterministic). Test for: does the output contain the required information, does it conform to the output schema, is it within the expected length range.
- Change detection: run the suite on the candidate new prompt and the current production prompt. Compute the overlap score. If it drops below a threshold, human review is required.
- Promotion gate: no prompt update reaches production without passing the regression suite and a human review approval.

---

### Block 10 — Multi-Agent Architecture: Orchestrator/Worker Pattern
**Hours:** 2.0 | **Method:** Lab | **Day:** 3 | **Time:** 0830–1030

**TLO:** The trainee will implement a multi-agent system with an orchestrator agent and at least two specialized worker agents — demonstrating routing logic, capability registration, and task delegation.

**Key Delivery Notes:**
- Orchestrator role: receives user requests, routes to appropriate worker agents, aggregates results, generates final response. Does not perform specialized tasks itself.
- Worker specialization: each worker has a defined capability scope. The orchestrator consults the capability registry to determine routing. Hard-coded routing is a fragile design.
- Capability registration: each worker registers its capabilities as a structured description. The orchestrator uses this to match requests to workers. New workers can be added without modifying the orchestrator.

**Assessment:** Evaluated in Day 5 architecture review.

---

### Block 11 — Memory Architecture for Multi-Agent Systems
**Hours:** 1.25 | **Method:** Lab | **Day:** 3 | **Time:** 1045–1200

**Key Delivery Notes:**
- Short-term memory: within the context window. Degrades as conversation grows (relevant early context moves out of the window). Solution: summarization at intervals to compress context.
- Long-term memory: vector store or structured database. Agents write and retrieve from it across sessions. Access control required — not all agents should read/write all memory.
- Shared memory across agents: design shared memory schemas carefully. Unstructured shared memory leads to agents reading stale or conflicting state from each other.

---

### Block 12 — Failure Recovery and Tool Hand-Off
**Hours:** 2.0 | **Method:** Lab | **Day:** 3 | **Time:** 1300–1500

**TLO:** The trainee will implement failure recovery logic for a multi-agent system — timeout handling, fallback chains, and a dead-letter queue for failed agent tasks — and test the recovery path with an injected failure.

**Key Delivery Notes:**
- Timeout handling: every agent call must have a timeout. A hung agent that never returns blocks the orchestrator indefinitely. Set and enforce timeouts.
- Fallback chains: if the primary worker fails, the orchestrator attempts the next-best worker or falls back to a degraded-capability response. The fallback must be defined before the system goes to production.
- Dead-letter queue: failed tasks that exhaust all fallback options go to a human review queue. Never silently drop a failed task.
- Tool hand-off: structured tool output schemas prevent hand-off failures. Output schema validation is the worker's responsibility before returning to the orchestrator.

---

### Block 13 — Tool Output Schema and Circular Dependency Detection
**Hours:** 1.75 | **Method:** Lab | **Day:** 3 | **Time:** 1515–1700

**Key Delivery Notes:**
- Tool output schema: every tool produces structured output in a defined schema. The orchestrator validates the schema before passing the output to the next step.
- Circular dependency: Agent A calls Agent B, which calls Agent A. Detection: track the call stack and fail if a cycle is detected. Do not let circular dependencies cause infinite loops.

---

### Block 14 — AI Governance Framework Design
**Hours:** 2.0 | **Method:** Lab | **Day:** 4 | **Time:** 0800–1000

**TLO:** The trainee will design a human-in-the-loop governance framework for a production AI system — specifying human review gate placements, approval workflow, output audit logging, and rollback procedures.

**Key Delivery Notes:**
- Human review gate placement: place gates at outputs that (1) write to Ontology Objects, (2) are presented to commanders, or (3) involve PII or classified information. Every consequential action should have a gate.
- Gate design: output goes to draft status → human reviewer approves or rejects → approved outputs promote to production status. Rejection sends to revision queue.
- Audit logging: every AI output that enters a review workflow is logged with the query, the output, the reviewer identity, the review decision, and the timestamp.
- Rollback: if a production AI system produces a systematic error, rollback must be possible within 15 minutes. Document the rollback procedure before the system goes live.

---

### Block 15 — AI Evaluation Harness and Ground Truth Design
**Hours:** 1.25 | **Method:** Lab | **Day:** 4 | **Time:** 1015–1200

**TLO:** The trainee will build an automated AI evaluation harness with a human-annotated ground truth set — computing precision, recall, and inter-rater reliability across at least two annotators.

**Key Delivery Notes:**
- Ground truth design: for operational AI systems, ground truth must be human-annotated by domain experts. The annotation guide must be specific enough that two annotators produce >80% agreement (inter-rater reliability).
- Inter-rater reliability (IRR): measure with Cohen's kappa. Below 0.6 = annotation guide is too ambiguous. Fix the guide before the ground truth set is used for evaluation.
- Evaluation cadence: run the evaluation harness weekly for production systems. Any metric that drops >5% below baseline triggers a human review.

---

### Block 16 — OPSEC for Operational AI Systems
**Hours:** 0.75 | **Method:** Seminar | **Day:** 4 | **Time:** 1300–1400

**Key Delivery Notes:**
- Classification handling: AI systems that ingest classified content must be deployed on infrastructure cleared to that level. The engineer is responsible for ensuring the deployment environment matches the data classification.
- Output classification: an AI output derived from classified sources carries the source classification, even if the output itself appears unclassified. Label outputs accordingly.
- Access control: the AI system must enforce access control on retrieved content. Users should only retrieve documents they have need-to-know for.

---

### Block 17 — Architecture Review: Participant Systems
**Hours:** 2.25 | **Method:** Workshop | **Day:** 4 | **Time:** 1415–1700

**Purpose:** Each trainee presents the AI system they currently maintain (from the pre-course checklist) for structured architecture review against TM-50H standards.

**TLO:** The trainee will present their AI system architecture and receive a structured critique identifying governance gaps, retrieval quality risks, and failure recovery weaknesses.

**Key Delivery Notes:**
- Presentation: 5 minutes, architecture diagram required. Cover: data flow, retrieval mechanism, human review gates, failure recovery, and OPSEC handling.
- Review criteria: retrieval quality (measured or untested?), prompt version control (tracked or ad hoc?), human review gates (present or absent?), OPSEC compliance (deployment environment cleared?).
- Every system will have gaps. The goal is identification, not condemnation.

---

### Block 18 — Practical Exercise Scenario Brief
**Hours:** 1.0 | **Method:** Brief | **Day:** 5 | **Time:** 0800–0900

**Scenario brief issued.** Trainees design an enterprise AI system architecture for a provided operational context. Requirements include: RAG pipeline for a classified document corpus, multi-agent routing for three query types, human review gates for all consequential outputs, and an evaluation harness.

---

### Block 19 — Practical Exercise: System Design
**Hours:** 3.0 | **Method:** Evaluation | **Day:** 5 | **Time:** 0900–1200

**Tasks:** (1) Design RAG pipeline architecture: chunking strategy, metadata schema, retrieval method, evaluation harness. Justify each decision in writing. (2) Design multi-agent system: orchestrator routing logic, worker capabilities, failure recovery path, tool output schemas. (3) Design governance framework: human review gate placement, audit log schema, rollback procedure.

**Go standard:** All three design components complete and internally consistent. Hard No-Go: no human review gates on consequential outputs; OPSEC classification handling not addressed.

---

### Block 20 — Practical Exercise: Implementation and Review
**Hours:** 3.25 | **Method:** Evaluation | **Day:** 5 | **Time:** 1300–1700

**Tasks:** Implement the retrieval evaluation harness on the provided corpus. Run the harness and report MRR. Implement one agent with failure recovery. Present the architecture document to the evaluator in a 15-minute technical review.

**Go standard:** Evaluation harness runs and produces MRR score. Agent implements at least one failure recovery path. Architecture document covers all required sections.

---

---

# PART M — TM-50M: ADVANCED ML ENGINEERING

**Duration:** 5 days (40 hours) | **T:I ratio:** 4:1 | **Instructor req:** Senior ML engineer with production MLOps experience; TM-50M certified or C2DAO ML Platform SME
**Advanced access required:** Python Transforms, Model Integration (registry), Code Workspace GPU

---

### Block 1 — The Production ML Lifecycle and Silent Failures
**Hours:** 1.0 | **Method:** Seminar | **Day:** 1 | **Time:** 0800–0900

**TLO:** The trainee will describe the production ML lifecycle from initial deployment to deprecation, and identify the three most common silent failure modes: data drift, concept drift, and scope creep.

**Key Delivery Notes:**
- Silent failures: a model that degrades gradually without triggering alerts is the most dangerous failure mode. The model still produces outputs — they are just increasingly wrong.
- Data drift: the distribution of model inputs changes after deployment (new data sources, seasonal patterns, operational OPTEMPO changes). The model was not trained on the current distribution.
- Concept drift: the relationship between inputs and outputs changes. The world changed; the model did not.
- Scope creep: the model is applied to questions it was not designed to answer because it produces outputs that look plausible. ORSA and data science teams must establish explicit scope boundaries.

---

### Block 2 — Data Drift Detection
**Hours:** 2.0 | **Method:** Lab | **Day:** 1 | **Time:** 0900–1100

**TLO:** The trainee will implement data drift detection using PSI (Population Stability Index) and KL-divergence for numerical and categorical features — establishing baseline distributions and configuring alert thresholds.

**Key Delivery Notes:**
- PSI: < 0.1 = no significant drift; 0.1–0.2 = moderate drift (investigate); > 0.2 = significant drift (model review required). These are standard thresholds — document the rationale if you deviate.
- KL-divergence: directional (not symmetric). Compute both directions to characterize the shift fully.
- Baseline distribution: establish at the time of model deployment, not at training time. The deployment-time distribution is the reference — not the training distribution.
- Binning for continuous features: PSI requires binned distributions. Use training-time bin edges (not current-data-driven bins) to ensure the baseline is comparable.

**Assessment:** Drift monitoring pipeline evaluated in Day 5.

---

### Block 3 — Concept Drift Detection
**Hours:** 0.75 | **Method:** Lab | **Day:** 1 | **Time:** 1115–1200

**Key Delivery Notes:**
- Concept drift indicators: prediction confidence trend (declining average confidence suggests the model is increasingly uncertain about new data), label distribution shift (if ground truth labels are available), error rate trend on labeled holdout.
- Sliding window detection: compute drift metrics on a rolling 30-day window. If the metric exceeds the threshold for 3 consecutive windows, trigger a drift event.
- Distinguishing data drift from concept drift: data drift changes the input distribution; concept drift changes the input-output relationship. Run both monitors. The combination of findings determines the response.

---

### Block 4 — Drift Monitoring Pipeline
**Hours:** 2.0 | **Method:** Lab | **Day:** 1 | **Time:** 1300–1500

**TLO:** The trainee will build a Foundry Transform pipeline that computes PSI and concept drift metrics on a weekly cadence — outputting drift scores to a monitoring dataset and triggering an alert when thresholds are exceeded.

**Key Delivery Notes:**
- Pipeline schedule: weekly cadence minimum. Daily cadence for high-frequency operational data.
- Output schema: drift score per feature, alert flag (NONE/MODERATE/SIGNIFICANT), computation timestamp, model version the baseline was established on.
- Alert routing: drift alert → model owner → C2DAO ML SME. Do not route to commanders directly — drift requires technical triage before it becomes an operational concern.

---

### Block 5 — Drift Response Playbook
**Hours:** 1.75 | **Method:** Lab | **Day:** 1 | **Time:** 1515–1700

**TLO:** The trainee will produce a drift response playbook for a provided model — specifying the severity tiers, decision criteria for retraining vs. rollback vs. deprecation, and the escalation path for each tier.

**Key Delivery Notes:**
- Severity tiers: (1) MONITOR — drift detected but below retraining threshold; continue monitoring. (2) INVESTIGATE — drift exceeds threshold; pull recent predictions and compare to ground truth. (3) RETRAIN — drift confirmed to degrade performance; initiate retraining pipeline. (4) DEPRECATE — model cannot be retrained to acceptable performance with available data; remove from production.
- Rollback: available when retraining fails validation. Requires a previous production model version to roll back to. Always maintain at least one prior version in the model registry.

---

### Block 6 — Automated Retraining Pipeline
**Hours:** 2.0 | **Method:** Lab | **Day:** 2 | **Time:** 0830–1030

**TLO:** The trainee will design and implement an automated retraining pipeline — triggered by the drift monitoring alert — that trains a new model version on the refreshed dataset and writes it to the model registry as a candidate.

**Key Delivery Notes:**
- Trigger: drift monitoring pipeline writes SIGNIFICANT alert → retraining pipeline starts automatically.
- Data version pinning: the retraining pipeline must capture the exact data version used for training. If the pipeline runs again tomorrow on updated data, the model versions must be distinguishable.
- Training environment reproducibility: all random seeds set, package versions pinned in requirements file. The trained model must be reproducible from the archived data version and the pinned code.
- Output: new model version in the registry with status = CANDIDATE. Not promoted to PRODUCTION until validation passes.

---

### Block 7 — Validation Gates and Shadow Mode Deployment
**Hours:** 1.25 | **Method:** Lab | **Day:** 2 | **Time:** 1045–1200

**TLO:** The trainee will configure a validation gate for the retraining pipeline — running the candidate model in shadow mode alongside the production model and comparing output distributions before promoting to production.

**Key Delivery Notes:**
- Shadow mode: the candidate model runs on every production query but its outputs are not returned to users. Outputs are logged for comparison against the production model.
- Validation criteria: candidate model achieves equal or better performance on the held-out validation set AND shadow mode outputs do not diverge significantly from production outputs on current data.
- Human approval gate: after shadow mode validation passes, a human reviewer must approve the promotion to production. Automated validation alone is insufficient for production promotion.

---

### Block 8 — Feature Stores and Time-Aware Feature Construction
**Hours:** 2.0 | **Method:** Lab | **Day:** 2 | **Time:** 1300–1500

**TLO:** The trainee will design a feature store schema for an operational readiness prediction problem — implementing point-in-time correct feature construction and demonstrating feature leakage detection on a provided dataset.

**Key Delivery Notes:**
- Point-in-time correctness: when computing features for a training example at time T, use only data available at time T. Using data from after T is feature leakage — it produces unrealistically high training performance that will not hold in production.
- Leakage detection: for each feature, verify the feature generation timestamp is earlier than the label timestamp in the training dataset. Automate this check in the training pipeline.
- Feature store design: each feature has a name, data type, update cadence, source pipeline, and point-in-time retrieval semantics. These must be documented before the feature store is used for training.

---

### Block 9 — Feature Store Integration with Foundry Ontology
**Hours:** 1.75 | **Method:** Lab | **Day:** 2 | **Time:** 1515–1700

**Key Delivery Notes:**
- Feature store features are pre-computed properties that are useful for multiple models. Store them as Object properties in the Foundry Ontology — they become reusable across models and accessible to Workshop applications.
- Connecting the feature pipeline to the Ontology: the feature store pipeline runs on schedule and writes computed features to the Object property via an Ontology write step.
- Access control: features derived from classified data carry the source classification. Apply the same access controls to feature store properties as to the underlying data.

---

### Block 10 — Ensemble Architectures
**Hours:** 2.0 | **Method:** Lab | **Day:** 3 | **Time:** 0830–1030

**TLO:** The trainee will implement a stacking ensemble with at least 3 diverse base learners and a meta-learner — with a strict temporal out-of-sample validation and documented bias-variance tradeoff.

**Key Delivery Notes:**
- Base learner diversity: select learners with different inductive biases (gradient boosting, regularized regression, neural network). Diverse error patterns are what make stacking effective.
- Temporal split: for operational time-series data, always split by time — never randomly. Train on data before T, validate on data after T.
- Meta-learner: typically a simple model (logistic regression, ridge) trained on base learner predictions. A complex meta-learner overfits — keep it simple.
- Bias-variance tradeoff: report training error vs. validation error. Justify the chosen model complexity against the operational context.

---

### Block 11 — Failure Mode Analysis
**Hours:** 1.25 | **Method:** Lab | **Day:** 3 | **Time:** 1045–1200

**TLO:** The trainee will conduct a systematic failure mode analysis for a provided operational ML model — identifying at least 5 failure modes, their operational consequences, and mitigation strategies.

**Key Delivery Notes:**
- Failure mode taxonomy: (1) systematic bias against a subgroup, (2) high error on tail-distribution inputs, (3) overconfident predictions in novel conditions, (4) feature corruption (unexpected nulls), (5) label noise in the training data.
- Operational consequence mapping: for each failure mode, describe the operational consequence if the failure occurs in production. "Model predicts C1 readiness for a C4-rated unit" is an operational consequence — not just a model error.
- Mitigation strategy: for each failure mode, specify a mitigation. Not all failure modes can be mitigated — some require limiting the scope of the model's use.

---

### Block 12 — Responsible AI for Operational ML
**Hours:** 2.0 | **Method:** Lab | **Day:** 3 | **Time:** 1300–1500

**TLO:** The trainee will conduct a fairness evaluation of a provided ML model — computing disparate impact across at least 2 subgroups — and design a human review gate placement for the model's operational use.

**Key Delivery Notes:**
- Disparate impact: compute model performance (accuracy, false positive rate) separately for each relevant subgroup (e.g., unit type, echelon, operational theater). Subgroups with significantly different performance require investigation before operational use.
- USAREUR-AF context: common subgroups for readiness models include unit type (maneuver vs. support), echelon (company vs. brigade), and geographic location (CONUS vs. OCONUS).
- Human review gate: place gates where model output drives consequential decisions. Require a human reviewer to affirm the model output before it is acted upon for high-stakes decisions.

---

### Block 13 — Human Review Gate Design
**Hours:** 1.75 | **Method:** Lab | **Day:** 3 | **Time:** 1515–1700

**Key Delivery Notes:**
- Gate placement criteria: any output that (1) writes to production Objects, (2) is presented as a briefing to commanders, or (3) triggers automated downstream actions — must pass through a human review gate.
- Gate bypass audit trail: any bypassed gate must be logged with the bypassing user's identity and a documented reason. No silent bypasses.
- Gate efficiency: design gates so reviewers can process them efficiently. A gate that takes 30 minutes to review will be bypassed in practice. Streamline the review interface.

---

### Block 14 — Model Governance Package
**Hours:** 2.0 | **Method:** Lab | **Day:** 4 | **Time:** 0800–1000

**TLO:** The trainee will produce a complete model governance package for their Day 3 ensemble model — including model card, training data documentation, known limitations register, and deprecation criteria.

**Key Delivery Notes:**
- Model card: model description, intended use, out-of-scope uses, training data summary, performance metrics on evaluation set, known limitations, contact information.
- Training data documentation: source datasets, date range, preprocessing applied, known data quality issues.
- Deprecation criteria: explicit conditions under which the model must be retired: "Model will be deprecated if validation performance drops below [X] on the standard evaluation set" or "if the operational context described in the intended use section changes materially."

---

### Block 15 — Production Model Audit
**Hours:** 2.0 | **Method:** Workshop | **Day:** 4 | **Time:** 1015–1200

**TLO:** The trainee will conduct a production model audit — evaluating a provided deployed model against its original model card — identifying drift, scope creep, and limitation gaps, and recommending a disposition (continue / retrain / deprecate).

**Key Delivery Notes:**
- Audit checklist: (1) is the model being used within its documented intended use scope? (2) is performance within the model card's stated bounds? (3) has drift occurred since the model card was written? (4) is the documentation current (training data, known limitations, contact)?
- Scope creep identification: compare the questions the model is actually being asked (from audit logs) to the intended use section of the model card.

---

### Block 16 — Peer Audit and Feedback
**Hours:** 1.75 | **Method:** Workshop | **Day:** 4 | **Time:** 1300–1445

**TLO:** The trainee will present their Day 15 audit findings to a peer and receive structured critique — identifying gaps in the audit methodology and alternative recommendations.

---

### Block 17 — Governance Documentation Revision
**Hours:** 1.25 | **Method:** Lab | **Day:** 4 | **Time:** 1500–1700

**Key Delivery Notes:**
- Incorporate peer feedback into the model governance package. Evaluator will assess the final package on Day 5.

---

### Block 18 — Practical Exercise Scenario Brief
**Hours:** 1.0 | **Method:** Brief | **Day:** 5 | **Time:** 0800–0900

**Scenario brief issued.** Trainees will build a drift monitoring pipeline, implement an automated retraining trigger, conduct a fairness evaluation, and produce a model governance package for a provided operational readiness model.

---

### Block 19 — Practical Exercise Part 1: Drift and Retraining
**Hours:** 2.25 | **Method:** Evaluation | **Day:** 5 | **Time:** 0900–1200

**Tasks:** (1) Build drift monitoring pipeline computing PSI on provided dataset. Identify which features have exceeded the SIGNIFICANT threshold. (2) Implement automated retraining trigger from the drift alert. (3) Configure shadow mode comparison between candidate and production model versions.

**Go standard:** Drift pipeline runs and produces PSI scores. Retraining trigger is configured and demonstrably linked to the drift alert. Shadow mode comparison produces output.

---

### Block 20 — Practical Exercise Part 2: Governance
**Hours:** 2.5 | **Method:** Evaluation | **Day:** 5 | **Time:** 1300–1545

**Tasks:** (1) Conduct fairness evaluation on the provided model — compute performance by subgroup. (2) Design human review gate placement for the model's operational use. (3) Produce complete model governance package (model card, training data docs, limitations register, deprecation criteria).

**Go standard:** Fairness evaluation covers at least 2 subgroups. At least one human review gate is placed on a consequential output. Model card addresses all required sections. Hard No-Go: no deprecation criteria; fairness evaluation not conducted.

---

### Block 21 — Evaluator Feedback and Graduation
**Hours:** 0.5 | **Method:** Review | **Day:** 5 | **Time:** 1545–1700

---

---

# PART J — TM-50J: ADVANCED PROGRAM MANAGEMENT (TECHNICAL)

**Duration:** 3 days (24 hours) | **T:I ratio:** 6:1 | **Instructor req:** Senior PM with portfolio-level leadership experience; TM-50J certified or C2DAO PM SME at GO/SES interface
**Note:** TM-50J is 3 days (24 hours), not 5 days.

---

### Block 1 — Portfolio Architecture and the Program-Project Distinction
**Hours:** 1.0 | **Method:** Seminar | **Day:** 1 | **Time:** 0800–0900

**TLO:** The trainee will distinguish program portfolio management from project management, describe the three structural differences in planning, governance, and risk management — and map their current portfolio against the TM-50J framework.

**Key Delivery Notes:**
- Project = defined scope, schedule, cost. Program = a collection of interdependent projects sharing strategic objectives. Portfolio = a collection of programs managed for strategic value optimization.
- The failure mode of applying project management to a portfolio: optimizing each project in isolation while the portfolio fails due to unmanaged interdependencies.
- Each trainee maps their current portfolio at the start of this block. The map is used throughout the course. If a trainee manages a single project, they develop a notional portfolio for the exercises.

**New doctrine content (March 2026):** DDOF friction matrix for portfolio-level integration friction analysis, roles and PM oversight mapping at enterprise scale, and portfolio health metrics tied to DDOF governance standards. Reference in Blocks 2–4 (dependency mapping and portfolio dashboard) and 10–12 (risk and practical exercise).

---

### Block 2 — Portfolio Dependency Mapping
**Hours:** 2.0 | **Method:** Workshop | **Day:** 1 | **Time:** 0900–1100

**TLO:** The trainee will produce a dependency map for their portfolio — identifying critical path dependencies, shared resource constraints, and dependency risks — and present it for instructor critique.

**Key Delivery Notes:**
- Dependency types: (1) hard dependency (B cannot start until A delivers), (2) resource dependency (B and A compete for the same team), (3) information dependency (B's decisions depend on A's findings).
- Critical path: the sequence of hard dependencies that determines the minimum portfolio completion time. Resource dependencies can convert into hard dependencies under resource constraints.
- Dependency risk: for each hard dependency, ask "what happens to the portfolio if this dependency slips 30 days?" Identify the three highest-impact dependency risks.

---

### Block 3 — Enterprise Delivery Governance
**Hours:** 0.75 | **Method:** Seminar | **Day:** 1 | **Time:** 1115–1200

**Key Delivery Notes:**
- Stage-gate review: a decision point where the portfolio sponsor reviews progress and makes a go/no-go decision on continued investment. Distinct from a status update — the output is a decision, not information.
- Portfolio health dashboard: milestone adherence, dependency health, risk register status, team velocity trend, and budget burn rate. All five dimensions must be present.
- Cross-program dependency management: a dependency between two programs requires a shared risk register entry and a named owner on each side.

---

### Block 4 — Portfolio Health Dashboard Build
**Hours:** 2.0 | **Method:** Workshop | **Day:** 1 | **Time:** 1300–1500

**TLO:** The trainee will build a portfolio health dashboard in MSS covering all five required dimensions — with milestone status, dependency health indicators, risk register summary, team velocity, and budget burn rate.

**Key Delivery Notes:**
- Build from the trainee's own portfolio data (or the notional portfolio established in Block 1).
- Dashboard format: one screen readable by a GO/SES audience in 60 seconds. Remove anything that requires explanation.
- Milestone status: GREEN (on track), AMBER (at risk, recovery plan in place), RED (missed/unrecoverable without intervention). Every milestone has one of these three statuses.

**Assessment:** Dashboard used in Day 2 GO/SES brief exercise.

---

### Block 5 — Enterprise Delivery Metrics
**Hours:** 1.75 | **Method:** Seminar | **Day:** 1 | **Time:** 1515–1700

**Key Delivery Notes:**
- Velocity: story points or features delivered per sprint/iteration. Useful for team-level planning. Does not aggregate meaningfully across teams without normalization.
- Predictability: ratio of planned vs. actual delivery over trailing 3 months. More useful than velocity for portfolio planning.
- Portfolio flow: how long does work take from intake to delivery? Long flow times indicate process bottlenecks, not team performance.
- Technical debt accumulation: track as a metric, not as an afterthought. Unmanaged technical debt is a portfolio risk.
- Metrics theater: reporting metrics that look good but do not drive decisions. If a metric does not change a decision, it should not be in the portfolio dashboard.

---

### Block 6 — Technical Investment Brief for GO/SES
**Hours:** 2.0 | **Method:** Workshop | **Day:** 2 | **Time:** 0830–1030

**TLO:** The trainee will structure a technical investment brief for a GO/SES audience — covering BLUF, capability gap, proposed solution, cost/schedule/performance tradeoffs, risks, and recommendation — using their prepared case study.

**Key Delivery Notes:**
- BLUF first, every time. "Bottom line: we need X to achieve Y. The cost is Z. The risk of not investing is [CONSEQUENCE]."
- Tradeoff table: every investment brief must include a table of options with cost, schedule, performance, and risk ratings. The recommended option is highlighted with the rationale for the recommendation.
- Language: translate technical content for a GO/SES audience. "We are using a transformer-based semantic search" becomes "we are using AI to find relevant documents based on meaning, not just keywords." If you cannot say it in plain language, you do not understand it well enough.

---

### Block 7 — GO/SES Briefing Delivery
**Hours:** 1.25 | **Method:** Workshop | **Day:** 2 | **Time:** 1045–1200

**TLO:** The trainee will present their investment brief to the evaluator (playing GO role) — demonstrating BLUF framing, handling a challenging question, and adjusting the recommendation in response to a new constraint injected during the brief.

**Key Delivery Notes:**
- Challenging question: evaluator injects "Why can't we just use the existing system?" Trainee must respond with the gap analysis, not defensiveness.
- New constraint inject: evaluator injects a budget constraint mid-brief. Trainee must adjust the recommendation in real time. Prepare a "budget-constrained" option before the session.
- Debrief: evaluator feedback on BLUF clarity, tradeoff communication, and how the constraint inject was handled.

---

### Block 8 — Organizational Change Leadership for MSS Adoption
**Hours:** 2.0 | **Method:** Seminar | **Day:** 2 | **Time:** 1300–1500

**TLO:** The trainee will apply a stakeholder analysis framework to an MSS capability adoption scenario — mapping resistance types, change communication approaches, and training pipeline integration requirements.

**Key Delivery Notes:**
- Stakeholder map: for each stakeholder group: current state (support/neutral/resist), reason for stance, and the specific change communication required to move them toward support.
- Resistance types: (1) capability resistance (they do not believe MSS can do what is claimed), (2) workload resistance (they believe adoption will add burden without removing any), (3) identity resistance (the new capability threatens their sense of professional value).
- Different resistance types require different responses. Capability resistance → demonstration. Workload resistance → evidence of time savings. Identity resistance → repositioning the new capability as amplifying their expertise, not replacing it.

---

### Block 9 — 90-Day Adoption Plan
**Hours:** 1.75 | **Method:** Workshop | **Day:** 2 | **Time:** 1515–1700

**TLO:** The trainee will produce a 90-day MSS capability adoption plan for a notional BCT — covering stakeholder communication, training pipeline integration, success metrics, and risk mitigation.

**Key Delivery Notes:**
- Day 1–30: stakeholder mapping, CDR engagement, training enrollment kick-off, quick-win identification (one high-visibility product on MSS within 30 days).
- Day 31–60: first cohort trained (TM-10), first MSS products in the battle rhythm, CCIR configuration reviewed by CDR.
- Day 61–90: second cohort trained (TM-20 builders), first builder product promoted to production, adoption metrics reviewed with CDR.
- Success metrics: number of trained personnel, number of MSS products in the battle rhythm, CCIR alert response time (did the alerts drive decisions?).

---

### Block 10 — Portfolio Risk at Scale
**Hours:** 1.5 | **Method:** Seminar | **Day:** 3 | **Time:** 0800–0930

**TLO:** The trainee will design a portfolio-level risk management framework — covering aggregate risk exposure, cross-program dependency risk, and strategic risk escalation criteria.

**Key Delivery Notes:**
- Risk aggregation: individual project risks may be managed at the project level. Risks that affect multiple programs or the portfolio's strategic objective must be escalated to the portfolio level.
- Strategic risk escalation criteria: define explicitly what conditions require GO/SES notification. "Any risk with probability > 30% and impact > [X threshold] that affects delivery by more than 60 days."
- Dependency risk: a risk in Program A that affects Program B's critical path is a portfolio risk, not a Program A risk.

---

### Block 11 — Practical Exercise Scenario Brief
**Hours:** 0.5 | **Method:** Brief | **Day:** 3 | **Time:** 0930–1000

**Scenario brief issued.** Trainees will conduct a portfolio health review, present a technical investment brief, and develop a risk mitigation plan for an injected portfolio risk.

---

### Block 12 — Practical Exercise (Evaluated)
**Hours:** 4.0 | **Method:** Evaluation | **Day:** 3 | **Time:** 1300–1700

**Tasks:**

| Task | Standard |
|------|----------|
| 1 | Update portfolio health dashboard with provided data; identify top 3 risks and dependency health status |
| 2 | Present technical investment brief for the provided scenario (10 min); answer challenging question |
| 3 | Respond to evaluator-injected portfolio risk: update risk register, state escalation decision, and brief the evaluator on the recommended response |

**Go standard:** Pass all 3 tasks. Hard No-Go: investment brief with no BLUF; risk escalation decision not made in response to the inject.

---

---

# PART K — TM-50K: ADVANCED KNOWLEDGE MANAGEMENT

**Duration:** 3 days (24 hours) | **T:I ratio:** 6:1 | **Instructor req:** Senior KMO or organizational knowledge architect; TM-50K certified or C2DAO KM SME
**Note:** TM-50K is 3 days (24 hours), not 5 days.

---

### Block 1 — Enterprise KM Architecture Principles
**Hours:** 1.0 | **Method:** Seminar | **Day:** 1 | **Time:** 0800–0900

**TLO:** The trainee will distinguish enterprise KM architecture from unit-level KM practice, and describe the three design principles that determine whether a knowledge system survives personnel turnover: governance clarity, quality automation, and retrieval reliability.

**Key Delivery Notes:**
- Enterprise KM failure mode: systems designed by and for one KMO that collapse when that person rotates. Architecture must not depend on any individual's tacit knowledge.
- Governance clarity: every knowledge artifact has a designated owner, freshness policy, and review cadence. Without these, knowledge degrades silently.
- Quality automation: manual quality processes fail under personnel pressure. Any quality check that can be automated should be.
- Retrieval reliability: a knowledge system that does not return results for 30% of queries will be abandoned. Zero-recall failure is the leading cause of knowledge system non-use.

**New doctrine content (March 2026):** FM 6-0 KM 5-step process at enterprise scale, developmental domains framework for theater-level KM capability maturity, and Critical Knowledge Items (CKI) identification methodology for cross-domain knowledge architectures. Reference in Blocks 2–5 (taxonomy and quality governance) and 6–8 (AI-augmented tagging and continuity systems).

---

### Block 2 — Multi-Domain Taxonomy Design
**Hours:** 2.0 | **Method:** Workshop | **Day:** 1 | **Time:** 0900–1100

**TLO:** The trainee will design a multi-domain controlled vocabulary for a theater formation's knowledge architecture — with cross-functional linkage between domains and a governance process for vocabulary updates.

**Key Delivery Notes:**
- Domain separation: each functional domain (operations, intelligence, sustainment, personnel) has its own vocabulary set. Cross-domain terms require explicit mapping.
- Cross-functional linkage: a SIGACT event (operations domain) may link to a lessons learned entry (training domain) and a doctrine reference (doctrine domain). Design these links explicitly.
- Vocabulary governance: who can add a term to the controlled vocabulary? Who can modify or deprecate a term? Document this before the taxonomy goes live.
- Common failure: domain vocabulary created independently by each staff section without coordination. Result: the same concept appears under 3 different terms across domains, and cross-domain queries fail.

---

### Block 3 — Knowledge Quality Governance
**Hours:** 0.75 | **Method:** Seminar | **Day:** 1 | **Time:** 1115–1200

**Key Delivery Notes:**
- Accuracy auditing: sample-based review of knowledge artifacts against authoritative sources. Cadence: quarterly at minimum. KM lead reviews a random 10% sample each quarter.
- Freshness policy: every knowledge artifact has a maximum age before it is flagged for review. Training content: 12 months. Doctrine references: when the source doctrine is updated. TTPs: 6 months (TTPs change faster than doctrine).
- Contradiction management: when two artifacts in the knowledge system contradict each other, one must be designated authoritative. The other is either updated or retired. Document the contradiction event in the system.

---

### Block 4 — Semantic Search Architecture for Knowledge Repositories
**Hours:** 2.0 | **Method:** Lab | **Day:** 1 | **Time:** 1300–1500

**TLO:** The trainee will design a semantic search architecture for a theater knowledge repository — covering embedding strategy, query expansion, and zero-recall failure handling.

**Key Delivery Notes:**
- Embedding strategy: embed knowledge artifacts at document or paragraph level, depending on artifact length. Short TTPs: document-level. Longer doctrine references: paragraph-level.
- Query expansion: if the user query returns no results, the system should automatically try related terms from the controlled vocabulary. Document the expansion rules.
- Zero-recall failure: the most critical failure mode. When a query returns no results, the system should: (1) log the query, (2) suggest related terms to the user, (3) route the query to a human KM reviewer for content gap identification.
- Zero-recall rate target: < 5% of queries. Monitor this metric weekly.

---

### Block 5 — Knowledge System Health Metrics
**Hours:** 1.75 | **Method:** Lab | **Day:** 1 | **Time:** 1515–1700

**TLO:** The trainee will design a health metrics dashboard for a knowledge system — covering zero-recall rate, content age distribution, query volume by domain, and coverage gap identification.

**Key Delivery Notes:**
- Zero-recall rate: (# queries returning 0 results) / (total queries). Track weekly. Any week above 5% triggers a content gap review.
- Content age distribution: histogram of knowledge artifact ages. Skewing toward older content means the system is not being updated.
- Query volume by domain: identifies which domains are actively used vs. which are under-queried (possible content gap or poor discoverability).
- Coverage gap identification: queries that return results but receive low relevance feedback from users indicate a domain where content exists but does not match user needs.

---

### Block 6 — AI-Augmented Tagging Pipeline
**Hours:** 2.0 | **Method:** Lab | **Day:** 2 | **Time:** 0830–1030

**TLO:** The trainee will build an AIP Logic tagging pipeline that auto-tags ingested documents with controlled vocabulary terms — with a human review gate that catches low-confidence tags before they enter the knowledge system.

**Key Delivery Notes:**
- Pipeline flow: document ingested → AIP Logic workflow extracts candidate tags from controlled vocabulary → confidence score per tag → high-confidence tags (> threshold) auto-applied → low-confidence tags routed to human review queue.
- Confidence threshold: set based on evaluation against a gold-standard tagged sample. Do not apply auto-tags with < 70% precision on the evaluation set.
- Human review queue: reviewer sees the document excerpt and the proposed tag with confidence score. Approve or reject. Approved tags enter the production knowledge system.
- Edge case: document that matches no controlled vocabulary terms. Route to the taxonomy governance process as a candidate for vocabulary expansion.

---

### Block 7 — Theme Extraction and Synthesis
**Hours:** 1.25 | **Method:** Lab | **Day:** 2 | **Time:** 1045–1200

**TLO:** The trainee will configure an AIP Logic workflow that generates thematic summaries across a corpus of lessons learned documents — with a human review gate and an accuracy evaluation against a provided ground truth.

**Key Delivery Notes:**
- Theme extraction: LLM-generated summary of the 3–5 dominant themes across a document set. Useful for identifying cross-domain patterns in lessons learned.
- Accuracy evaluation: compare LLM-extracted themes against human-identified themes on a 10-document sample. Report precision of theme identification.
- Human review requirement: AI-generated thematic summaries should not be presented as authoritative without human review. The summary is a draft — the KMO reviews and publishes.

---

### Block 8 — Unit Continuity System Design
**Hours:** 2.0 | **Method:** Workshop | **Day:** 2 | **Time:** 1300–1500

**TLO:** The trainee will design a unit knowledge continuity system — handoff protocol, knowledge decay monitoring, and reactivation procedure — using a real or notional personnel turnover case study.

**Key Delivery Notes:**
- Handoff protocol: at each personnel rotation, the departing member completes a knowledge transfer artifact covering: current projects, critical contacts, undocumented processes, and known system quirks. This artifact enters the knowledge system with a retention period of 24 months.
- Knowledge decay monitoring: track knowledge artifacts associated with departed personnel. Flag for review after 6 months — the content may still be accurate, but needs a new owner assigned.
- Reactivation: when a knowledge system becomes dormant (no updates, no queries for 90 days), a reactivation procedure is required before it is trusted. Verify currency of all artifacts before re-activating the system for operational use.
- Case study: each trainee uses their prepared turnover case (from pre-course checklist). What knowledge was lost? What should have been captured? Design the handoff protocol that would have prevented the loss.

---

### Block 9 — Cross-Organizational KM Interoperability
**Hours:** 1.75 | **Method:** Seminar | **Day:** 2 | **Time:** 1515–1700

**Key Delivery Notes:**
- Federation patterns: each formation maintains its own knowledge system with its own governance. Cross-organizational queries are resolved through a federated search layer — not by merging knowledge systems.
- Shared taxonomy: federated search requires a common vocabulary layer that maps domain-specific terms across formations. Invest in shared taxonomy governance before attempting federation.
- Common failure: organizations attempt to centralize all knowledge into one system. Governance complexity grows beyond what the KM staff can manage. Federated architecture distributes governance while enabling cross-organizational retrieval.

---

### Block 10 — Knowledge System Evaluation
**Hours:** 1.5 | **Method:** Workshop | **Day:** 3 | **Time:** 0800–0930

**TLO:** The trainee will conduct a health evaluation of a provided knowledge system — applying the health metrics dashboard from Block 5 — identifying staleness, coverage gaps, usage patterns, and recommending a remediation plan.

**Key Delivery Notes:**
- Evaluation output: a written evaluation report covering: zero-recall rate (with calculation), content age analysis, top 3 coverage gaps, and a prioritized remediation plan.
- Remediation prioritization: address zero-recall failure first (directly impacts usability), then content staleness (directly impacts trustworthiness), then coverage gaps (impacts breadth of use).

---

### Block 11 — Practical Exercise Scenario Brief
**Hours:** 0.5 | **Method:** Brief | **Day:** 3 | **Time:** 0930–1000

**Scenario brief issued.** Trainees will design a multi-domain knowledge architecture, configure a tagging pipeline, evaluate a knowledge system's health, and design a unit continuity protocol for a notional formation undergoing a major rotation.

---

### Block 12 — Practical Exercise (Evaluated)
**Hours:** 4.0 | **Method:** Evaluation | **Day:** 3 | **Time:** 1300–1700

**Tasks:**

| Task | Standard |
|------|----------|
| 1 | Produce a multi-domain taxonomy design covering 3 functional domains with cross-domain linkages and a governance process |
| 2 | Design an AI-augmented tagging pipeline with human review gate; identify the confidence threshold and its basis |
| 3 | Evaluate the provided knowledge system using the health metrics framework; identify top 3 gaps; produce a remediation plan |
| 4 | Design a unit continuity protocol for the notional formation in the scenario |

**Go standard:** Pass all 4 tasks. Hard No-Go: taxonomy with no cross-domain linkage; health evaluation with no zero-recall analysis.

---

---

# PART L — TM-50L: ADVANCED SOFTWARE ENGINEERING

**Duration:** 5 days (40 hours) | **T:I ratio:** 4:1 | **Instructor req:** Senior SWE with platform engineering and enterprise CI/CD experience; TM-50L certified or C2DAO SWE Architecture SME
**Advanced access required:** OSDK TypeScript SDK (advanced), CI/CD pipeline access in training environment

---

### Block 1 — OSDK-First Architecture: Designing for Consumption
**Hours:** 1.0 | **Method:** Seminar | **Day:** 1 | **Time:** 0800–0900

**TLO:** The trainee will describe the OSDK-first architecture principle — designing Object Types as API contracts for application consumption, not just as data storage structures — and identify the three most common anti-patterns that OSDK-first design prevents.

**Key Delivery Notes:**
- OSDK-first means: before defining a property on an Object Type, ask "what application query will read this property, and in what format?" If you cannot answer, the property may not need to exist.
- Anti-patterns prevented: (1) properties that exist only in the Ontology but are never queried through OSDK, (2) properties with types that are inconvenient for TypeScript consumption, (3) Object Types designed for data storage that create N+1 query patterns in applications.
- Interface contract: the Object Type's OSDK-accessible properties and Actions are a public API. Changes break downstream consumers. Design with stability in mind.

---

### Block 2 — Object Type Modeling for Application Consumption
**Hours:** 2.0 | **Method:** Lab | **Day:** 1 | **Time:** 0900–1100

**TLO:** The trainee will model an Object Type optimized for application consumption — with primary key design, property typing, link traversal optimization, and documented Object Set query patterns.

**Key Delivery Notes:**
- Primary key: must be stable over the Object's lifecycle and unique within the Object Type. Using a mutable business key as the primary key is a common error — the key changes when the entity is renamed.
- Property typing: choose types for TypeScript consumption convenience, not just data correctness. A DATE property is easier to work with in TypeScript than a formatted TIMESTAMP string.
- Link traversal: every Link Type traversal in OSDK adds a query. Model the Object Type to minimize required traversals for the most common application queries.
- Documented query patterns: write down the top 5 OSDK queries the application will make before building. This drives the Object Type design.

---

### Block 3 — OSDK Query Optimization
**Hours:** 0.75 | **Method:** Lab | **Day:** 1 | **Time:** 1115–1200

**Key Delivery Notes:**
- Filter push-down: apply filters as early as possible in the OSDK query chain. Do not load all Objects and filter in TypeScript — push the filter condition into the OSDK query.
- Pagination: all OSDK queries that might return large Object Sets must use pagination. Loading the full Object Set for a large Ontology is a production performance failure.
- Bulk query patterns: when the application needs to load N Objects by a list of primary keys, use the OSDK bulk load API, not N individual Object fetches.

---

### Block 4 — Type-Safe Action Interface Design
**Hours:** 2.0 | **Method:** Lab | **Day:** 1 | **Time:** 1300–1500

**TLO:** The trainee will design a type-safe Action interface in TypeScript — with input validation, error type design, and idempotency patterns — and implement a unit test that covers the validation and error paths.

**Key Delivery Notes:**
- Input validation: validate every Action input at the TypeScript boundary before passing to the OSDK write. Reject invalid inputs with a typed error, not a generic exception.
- Error type design: use discriminated union types for Action errors. `type ActionError = | {type: 'VALIDATION_ERROR', field: string, message: string} | {type: 'CONCURRENT_EDIT', conflictingUser: string}`. Callers handle each error case explicitly.
- Idempotency: Actions that write to Objects should be idempotent where possible. Multiple calls with the same input should produce the same result without side effects.

---

### Block 5 — OSDK Interface Contract Documentation
**Hours:** 1.75 | **Method:** Lab | **Day:** 1 | **Time:** 1515–1700

**TLO:** The trainee will produce an OSDK interface contract document for their Day 1 Object Type — covering available queries, Action signatures, error types, and versioning policy.

**Key Delivery Notes:**
- Contract format: similar to an OpenAPI specification but for Foundry Actions and queries. Cover: available OSDK queries (with filter options), Action names (with input schema and error types), and the versioning policy.
- Versioning policy: what counts as a breaking change? Adding a required Action input is breaking. Adding an optional property is not. Document the policy before the first consumer connects.

---

### Block 6 — TypeScript Advanced Patterns: Memoization and Bulk Query
**Hours:** 2.0 | **Method:** Lab | **Day:** 2 | **Time:** 0830–1030

**TLO:** The trainee will implement memoization for computed Object properties, bulk query batching using a DataLoader pattern, and Object Set operator composition for complex multi-condition queries.

**Key Delivery Notes:**
- Memoization: cache computed properties that are expensive to compute and infrequently change. Cache invalidation: invalidate when the underlying Object is updated. Never cache stale data longer than the Object's update cadence.
- DataLoader pattern: when an application loads N related Objects (e.g., load Equipment for each Unit in a list), batch all N requests into one OSDK bulk query. This reduces N+1 query patterns to 1+1.
- Object Set operators: OSDK allows composing filters using `and`, `or`, `not` operators on Object Sets. Build complex filters at the OSDK level, not by loading and filtering in TypeScript.

---

### Block 7 — Type Narrowing and Discriminated Unions
**Hours:** 1.25 | **Method:** Lab | **Day:** 2 | **Time:** 1045–1200

**Key Delivery Notes:**
- Type narrowing: when a Function receives an Object that could be one of multiple Object Types, use discriminated unions and type guards to handle each case safely.
- Exhaustive pattern matching: use TypeScript's `never` type in the default case of a switch statement to ensure all cases are handled. The compiler will error if a new Object Type is added and the switch is not updated.
- Practical use: an Action that operates on either Equipment or Personnel Objects — discriminated union ensures the correct properties are accessed for each type.

---

### Block 8 — Function Composition and Shared Libraries
**Hours:** 2.0 | **Method:** Lab | **Day:** 2 | **Time:** 1300–1500

**TLO:** The trainee will build a shared Function library from common OSDK query patterns used across multiple applications — with code generation from the Object Type schema — reducing duplication across the platform.

**Key Delivery Notes:**
- Shared library: common OSDK queries (e.g., "get all Equipment for a given Unit") should be implemented once in a shared library, not re-implemented in each application.
- Code generation: generate TypeScript types from the Foundry Object Type schema. This ensures TypeScript types stay in sync with the Ontology without manual maintenance.
- Library versioning: the shared library is a versioned dependency. Patch version = bug fixes (backward compatible). Minor version = new query added (backward compatible). Major version = breaking API change (consumers must migrate).

---

### Block 9 — Function Testing: Unit and Contract Tests
**Hours:** 1.75 | **Method:** Lab | **Day:** 2 | **Time:** 1515–1700

**TLO:** The trainee will implement unit tests for TypeScript Functions using a mock OSDK and contract tests between Functions and their downstream consumers — with a test suite that catches breaking changes before production promotion.

**Key Delivery Notes:**
- Unit tests with mock OSDK: use a mock OSDK client that returns pre-defined Object data. Test the Function logic without hitting the production Ontology.
- Contract tests: the consuming application defines what it expects from the Function (query structure, return type). The Function provider must satisfy these contracts. If the Function changes in a way that breaks a contract, the contract test fails.
- Breaking change detection: run contract tests on every pull request. A failing contract test blocks promotion.

---

### Block 10 — Enterprise CI/CD Pipeline Design
**Hours:** 2.0 | **Method:** Lab | **Day:** 3 | **Time:** 0830–1030

**TLO:** The trainee will design and configure an enterprise CI/CD pipeline for an MSS application — including automated unit + integration test execution, branch protection rules, and promotion gate configuration.

**Key Delivery Notes:**
- Pipeline stages: (1) unit test, (2) integration test (against the training environment Ontology), (3) contract test, (4) security scan, (5) promotion gate (human approval for production). All stages must pass before promotion.
- Branch protection: main branch is protected. No direct pushes. All changes via pull request. At least one reviewer approval required. All CI stages must pass before merge.
- Promotion gate: automated stages pass → human reviewer approves promotion to production. The gate approval is logged with reviewer identity and timestamp.

---

### Block 11 — Consumer-Driven Contract Testing
**Hours:** 1.25 | **Method:** Lab | **Day:** 3 | **Time:** 1045–1200

**TLO:** The trainee will implement consumer-driven contract tests between two MSS applications — demonstrating that a change to the provider application's OSDK interface breaks the consumer's contract test before reaching production.

**Key Delivery Notes:**
- Consumer-driven: the consuming application writes the contract (what it expects from the provider). The provider must satisfy all consumer contracts. This puts the burden of compatibility on the provider, not the consumer.
- Pact or equivalent: use a contract testing framework. The contract is version-controlled alongside the consuming application's code.
- Breaking change scenario: demonstrate that adding a required field to an Action input breaks the consumer's contract test. The pipeline blocks promotion. The provider team must resolve the breaking change.

---

### Block 12 — Security Review Process for MSS Applications
**Hours:** 2.0 | **Method:** Lab | **Day:** 3 | **Time:** 1300–1500

**TLO:** The trainee will conduct a security review of a provided MSS application codebase — using the TM-50L security review checklist — and produce a prioritized findings report.

**Key Delivery Notes:**
- Security checklist items: (1) input validation at all Action boundaries, (2) no hardcoded credentials or tokens, (3) OSDK credential handling (no credentials in client-side code), (4) output encoding (no unescaped user-controlled content in HTML), (5) access control verification (Actions restricted to appropriate roles).
- OSDK credential handling: OSDK client credentials must be handled server-side or via the Foundry token exchange pattern. Never include raw API tokens in client-side TypeScript.
- Findings report: for each finding, document: severity (CRITICAL/HIGH/MEDIUM/LOW), location (file and line), description, and recommended fix. CRITICAL findings block promotion.

---

### Block 13 — Security Testing: Injection and OPSEC Review
**Hours:** 1.75 | **Method:** Lab | **Day:** 3 | **Time:** 1515–1700

**TLO:** The trainee will test a provided MSS application for Action input injection vulnerabilities and identify data over-exposure risks in OSDK queries — documenting findings and proposed mitigations.

**Key Delivery Notes:**
- Action input injection: test whether Action inputs are sanitized before use in downstream operations. Malformed inputs that cause unexpected behavior are injection vulnerabilities.
- OSDK data over-exposure: identify queries that return more Object properties than the application displays or uses. Over-exposed data is an OPSEC risk if the application is accessed by users without need-to-know for all returned properties.
- Remediation: for each finding, implement the fix and verify in the test environment before documenting as resolved.

---

### Block 14 — Architecture Review: Participant Systems
**Hours:** 2.0 | **Method:** Workshop | **Day:** 4 | **Time:** 0800–1000

**Purpose:** Each trainee presents an MSS application they built or maintain for structured peer architecture review — applying the TM-50L review criteria.

**TLO:** The trainee will present their application architecture and receive a structured critique identifying scalability constraints, security gaps, and technical debt — with a recommended refactoring priority list.

**Key Delivery Notes:**
- Presentation: 8 minutes, system diagram required. Cover: OSDK interface design, query patterns, Action structure, CI/CD pipeline status, security review status.
- Review criteria: (1) OSDK-first design or data-centric design? (2) N+1 query patterns present? (3) Type safety enforced? (4) CI/CD pipeline in place? (5) Security review conducted?

---

### Block 15 — Platform Toolchain Design
**Hours:** 2.0 | **Method:** Lab | **Day:** 4 | **Time:** 1015–1200

**TLO:** The trainee will design a developer platform toolchain for an MSS development team — covering shared Transform libraries, common OSDK query utilities, code generation from Object Type schemas, and a developer onboarding guide.

**Key Delivery Notes:**
- Toolchain components: (1) shared Transform library (common pipeline patterns), (2) OSDK query utility library (common Object queries), (3) schema code generator (TypeScript types from Ontology), (4) CI/CD pipeline template (pre-configured pipeline for new applications).
- Developer onboarding guide: a new developer should be productive in 2 days using the toolchain. If onboarding requires more than 2 days of setup, the toolchain has usability gaps.

---

### Block 16 — API Versioning and Deprecation Policy
**Hours:** 1.75 | **Method:** Seminar | **Day:** 4 | **Time:** 1300–1445

**Key Delivery Notes:**
- API versioning for Foundry Functions: version the Function alongside the Object Type contract. Consumers reference a specific version.
- Breaking change classification: adding required input = breaking. Removing a return property = breaking. Adding an optional input = not breaking. Adding a return property = not breaking (depends on consumer contract).
- Deprecation policy: give consumers a 60-day deprecation notice before removing a Function version. Maintain the deprecated version for the notice period. Log usage of deprecated versions to track when consumers have migrated.

---

### Block 17 — Technical Architecture Document
**Hours:** 1.25 | **Method:** Lab | **Day:** 4 | **Time:** 1500–1700

**TLO:** The trainee will produce a technical architecture document for a platform component — covering system diagram, OSDK interface contracts, CI/CD pipeline design, security review findings, API versioning policy, and deprecation criteria.

---

### Block 18 — Practical Exercise Scenario Brief
**Hours:** 1.0 | **Method:** Brief | **Day:** 5 | **Time:** 0800–0900

**Scenario brief issued.** Trainees will design an OSDK-first Object Type, implement a TypeScript Function with type-safe Actions, configure a CI/CD pipeline with contract testing, and conduct a security review of a provided codebase.

---

### Block 19 — Practical Exercise Part 1: Architecture and Implementation
**Hours:** 2.25 | **Method:** Evaluation | **Day:** 5 | **Time:** 0900–1200

**Tasks:** (1) Design OSDK-first Object Type for the provided scenario with interface contract document. (2) Implement a TypeScript Function with type-safe Action input validation and discriminated union error types. (3) Write unit tests covering validation and error paths. (4) Configure CI/CD pipeline with branch protection and promotion gate.

**Go standard:** Object Type is queryable via OSDK. TypeScript Function compiles with no type errors. Unit tests pass. CI/CD pipeline configuration passes review. Hard No-Go: Action with no input validation; no unit tests.

---

### Block 20 — Practical Exercise Part 2: Security and Architecture Review
**Hours:** 3.0 | **Method:** Evaluation | **Day:** 5 | **Time:** 1300–1600

**Tasks:** (1) Conduct security review of provided codebase using the TM-50L checklist. Produce prioritized findings report. (2) Implement fix for any CRITICAL findings identified. (3) Present technical architecture document to evaluator in a 15-minute review.

**Go standard:** Security review covers all 5 checklist categories. CRITICAL findings are fixed and verified. Architecture document covers all required sections. Hard No-Go: CRITICAL security finding not fixed; OSDK credentials present in client-side code.

---

### Block 21 — Evaluator Feedback and Graduation
**Hours:** 1.0 | **Method:** Review | **Day:** 5 | **Time:** 1600–1700

---

---

# PART N — TM-50N: ADVANCED UI/UX DESIGNER

**Duration:** 3 days (24 hours) | **T:I ratio:** 6:1 | **Instructor req:** Senior Designer with design system and enterprise UX experience; TM-50N certified or C2DAO Advanced UX SME
**Note:** TM-50N is 3 days (24 hours), not 5 days.

---

### Block 1 — From Application Design to Design Systems
**Hours:** 1.0 | **Method:** Seminar | **Day:** 1 | **Time:** 0800–0900

**Purpose:** TM-50N moves from designing applications to designing the system that produces applications. The advanced Designer's output is not a single interface — it is the standards, patterns, and processes that make every interface better. This block establishes the scale shift before any system-level design work begins.

**TLO:** The trainee will distinguish enterprise design system leadership from individual application design, describe the design system as a product with its own backlog and release cycle, and state the three principles that determine design system adoption: documentation quality, governance clarity, and developer integration.

**Key Delivery Notes:**
- Scale shift: "How should this dashboard look?" → "How should all dashboards look?" "Is this form accessible?" → "How do we ensure every form across the portfolio is accessible?"
- Design system product mindset: component requests from application teams are feature requests. Breaking changes require migration guides. Deprecating a component requires a sunset period.
- The design system serves two user populations: designers (who compose interfaces from system components) and developers (who implement components). Both must find the system usable.

**Assessment:** Design system mindset evaluated throughout course; assessed in capstone (Day 3).

---

### Block 2 — Design Token Architecture
**Hours:** 2.0 | **Method:** Studio | **Day:** 1 | **Time:** 0900–1100

**TLO:** The trainee will define a design token architecture covering classification colors, status colors, typography, and spacing — with locked vs. configurable token governance and an inheritance hierarchy for MSS.

**Key Delivery Notes:**
- Token categories: color (classification, status, background, text), typography (scale, weight, line height), spacing (grid, padding, margin), elevation (shadow, z-index). Each category has a defined set of tokens.
- Locked vs. configurable: classification banner colors are locked — no application may override them. Status indicator colors are locked. Background and accent colors are configurable within the approved palette. Document which tokens are locked and which are configurable.
- Inheritance hierarchy: global tokens → category tokens → component tokens. A component inherits from the category level unless explicitly overridden. This ensures consistency while allowing component-specific variation.
- Token naming convention: semantic names (`color-status-ready`, `color-status-warning`), not visual names (`green`, `amber`). Semantic names survive palette changes.

**Assessment:** Token architecture evaluated in capstone design system component (Day 3).

---

### Block 3 — Component Documentation Standard
**Hours:** 0.75 | **Method:** Studio | **Day:** 1 | **Time:** 1115–1200

**Key Delivery Notes:**
- Component documentation includes: description, variants (with visual examples), usage guidelines (do/don't), accessibility notes, data binding patterns, responsive behavior, and code examples.
- Do/don't examples: show correct usage AND common misuse. "Do: use the status badge with redundant text label. Don't: use color alone to indicate status."
- The documentation quality test: can a TM-40N designer or TM-40L developer use this component correctly without asking the design system team a question? If not, the documentation is incomplete.

---

### Block 4 — Design System Case Study
**Hours:** 2.0 | **Method:** Case Study | **Day:** 1 | **Time:** 1300–1500

**TLO:** The trainee will review a portfolio of MSS applications, identify consistency gaps that a design system would prevent, and propose system-level fixes with implementation priority.

**Key Delivery Notes:**
- Review 3–5 existing MSS applications. For each, identify: (1) visual inconsistencies (different color meanings, different button styles), (2) interaction inconsistencies (different filter behaviors, different error patterns), (3) accessibility inconsistencies (different contrast approaches, different keyboard navigation patterns).
- System-level fix: do not fix individual applications — propose the design system component or pattern that would prevent the inconsistency portfolio-wide.
- Implementation priority: fix inconsistencies that affect operational comprehension first (classification marking, status meaning). Fix aesthetic inconsistencies last.

---

### Block 5 — Design Governance
**Hours:** 1.75 | **Method:** Seminar | **Day:** 1 | **Time:** 1515–1700

**TLO:** The trainee will establish a design review governance process with defined gates, reviewers, criteria, and a deviation management procedure.

**Key Delivery Notes:**
- Design review gates: when in the development lifecycle does design review occur? Before implementation begins (design review), during implementation (implementation review), before deployment (final accessibility/standards check).
- Reviewers: who reviews? The design system team reviews system-level patterns. Domain designers review application-level layout. Accessibility specialist reviews compliance.
- Deviation management: what happens when an application needs to deviate from the design system? Document the deviation, the rationale, and the planned resolution (contribute a new component, update an existing component, or accept the deviation as an exception).
- Quality metrics: portfolio consistency score (how many applications comply with the design system?), component coverage (how much of the typical application is covered by system components?), deviation rate.

---

### Block 6 — DDIL-Aware Design
**Hours:** 2.0 | **Method:** Seminar + Studio | **Day:** 2 | **Time:** 0830–1030

**Purpose:** DDIL is not an edge case — it is a primary operating condition in the USAREUR-AF AOR. Design for disconnection first; connectivity is the bonus.

**TLO:** The trainee will design a DDIL-aware application implementing data freshness indicators, offline-first interaction patterns, and graceful degradation across all four DDIL tiers.

**Key Delivery Notes:**
- Four-tier DDIL design model: (1) Connected (full functionality), (2) Degraded (reduced bandwidth — progressive loading, compressed assets), (3) Intermittent (queue actions, sync when connected), (4) Disconnected (cached data only, all writes queued).
- Data freshness indicators: every data element has an age. A readiness report from 10 minutes ago is useful. From 4 hours ago, it requires a caveat. From 24 hours ago, it may be misleading. The Designer must encode these freshness states visually so the user never makes a decision on unknowingly stale data.
- Offline-first interaction patterns: design for "no network" as the default state. Show cached data with freshness indicators. Queue user actions for sync. Never show a blank screen.
- Graceful degradation: at each DDIL tier, define what functionality remains available and what is disabled. Display the current connectivity status and what the user can/cannot do.

**Assessment:** DDIL design pattern evaluated in capstone (Day 3).

---

### Block 7 — DDIL Design Exercise
**Hours:** 1.25 | **Method:** Studio | **Day:** 2 | **Time:** 1045–1200

**Key Delivery Notes:**
- Redesign an existing MSS application for DDIL resilience. Add freshness indicators, offline states, and queue patterns.
- For each DDIL tier, annotate the design with: what data is available, what actions are possible, what visual indicators change, and what the user experience is.
- Peer review: swap designs and evaluate whether the DDIL behavior is clear to a user without explanation.

---

### Block 8 — Cross-Domain UI Design
**Hours:** 2.0 | **Method:** Seminar + Studio | **Day:** 2 | **Time:** 1300–1500

**TLO:** The trainee will produce a cross-domain UI specification that maintains unambiguous classification marking across classification transitions — with documented ISSM review requirements.

**Key Delivery Notes:**
- Cross-domain design principle: the user must always know, without doubt, what classification level they are operating at and what classification the data they are viewing carries. This is not a UX problem to "solve" by making it seamless — it is a security requirement to make explicit.
- Multi-classification display patterns: when a single screen shows data from multiple classification levels, each data element must carry its classification marking. Aggregated displays must carry the highest classification present.
- Classification boundary transitions: when the user navigates from one classification level to another, the transition must be unambiguous — visual break, banner change, confirmation dialog. Accidental classification boundary crossing is a security incident.
- ISSM review: every cross-domain UI design requires ISSM review before implementation. The Designer prepares the design with classification annotations; the ISSM validates the marking scheme.

---

### Block 9 — Coalition UI Design
**Hours:** 1.75 | **Method:** Studio | **Day:** 2 | **Time:** 1515–1700

**Key Delivery Notes:**
- International conventions: date format (DD-MMM-YYYY for NATO), time format (24-hour with timezone), number format (period vs. comma as decimal separator varies by nation). Design for the lowest common denominator.
- Releasability markings: coalition data carries releasability designations (REL TO, NOFORN). The UI must display releasability alongside classification. A datum that is SECRET//REL TO USA, GBR is different from SECRET//NOFORN.
- Multi-language considerations: not full localization, but design for non-native English readers. Use full terms with abbreviations in parentheses on first use. Maintain a glossary accessible from every screen. Avoid idioms and colloquialisms in UI text.
- NATO partner interoperability: design patterns must accommodate NATO standard terminology where it differs from US usage.

---

### Block 10 — DesignOps
**Hours:** 1.0 | **Method:** Seminar | **Day:** 3 | **Time:** 0800–0900

**TLO:** The trainee will describe the operational processes for design at scale — tooling, onboarding, research repositories — and establish a DesignOps framework for an MSS design team.

**Key Delivery Notes:**
- DesignOps is to design what DevOps is to development — the operational practices that let design scale beyond individual heroics.
- DesignOps functions: design system maintenance, research repository management, design review governance, tooling and templates, new designer onboarding.
- Without DesignOps: components drift, each app reinvents patterns, same user groups interviewed repeatedly, insights lost at PCS, months of ramp-up for new designers.

---

### Block 11 — Research Repository
**Hours:** 2.0 | **Method:** Studio | **Day:** 3 | **Time:** 0900–1100

**TLO:** The trainee will build a research repository entry from existing user research data, tagged for reuse by other design teams — with tagging taxonomy and retrieval guidelines.

**Key Delivery Notes:**
- User research is expensive: operational access, security clearance requirements, user availability constraints. Every finding should be documented, tagged, and searchable so future teams build on existing knowledge rather than re-conducting the same studies.
- Research repository entry: study date, research questions, methodology, participants (role/rank, not names), key findings, design implications, linked personas, linked design decisions.
- Tagging taxonomy: tag by domain (WFF, track), user population (rank range, role type), methodology (interview, observation, usability test), and finding type (pain point, workflow gap, design validation).
- Retrieval guidelines: before starting new user research, search the repository first. Duplicate research wastes operational access.

---

### Block 12 — Accessibility at Enterprise Scale
**Hours:** 0.75 | **Method:** Studio | **Day:** 3 | **Time:** 1115–1200

**Key Delivery Notes:**
- Automated testing strategies: integrate accessibility scanning into the CI/CD pipeline. Catch contrast, alt text, and ARIA issues automatically.
- Remediation prioritization: Critical accessibility failures (keyboard navigation broken, screen reader unusable) before Major (contrast below threshold) before Minor (missing ARIA labels on non-interactive elements).
- Compliance reporting: produce a portfolio-wide accessibility compliance report. Track compliance rate per application. Set targets and review quarterly.

---

### Block 13 — Capstone Exercise
**Hours:** 2.0 | **Method:** Evaluation | **Day:** 3 | **Time:** 1300–1500

**Tasks:**

| Task | Standard |
|------|----------|
| 1 | Design a design system component with full documentation: variants, accessibility notes, do/don't examples, data binding, and responsive behavior |
| 2 | Design a DDIL pattern for an MSS application covering all four DDIL tiers with freshness indicators and offline states |
| 3 | Produce a design governance proposal covering review gates, deviation management, and quality metrics |

**Go standard:** Pass all 3 tasks. Component documentation is implementation-ready. DDIL pattern covers all four tiers. Governance proposal includes deviation management.

**Hard No-Go:** Design system component with no accessibility documentation. DDIL design that shows a blank screen at any tier. Governance proposal with no deviation management process.

---

### Block 14 — Capstone Presentations and Peer Review
**Hours:** 1.25 | **Method:** Workshop | **Day:** 3 | **Time:** 1515–1630

**Key Delivery Notes:**
- Each trainee presents their capstone: design system component, DDIL pattern, and governance proposal.
- Peer review: structured critique using TM-50N review criteria. Focus on implementation feasibility, documentation completeness, and operational applicability.
- Evaluator debrief: feedback on design system thinking, DDIL awareness, and governance maturity.

---

### Block 15 — Post-Test and Course Evaluation
**Hours:** 0.5 | **Method:** Evaluation | **Day:** 3 | **Time:** 1630–1700

**Post-test:** EXAM_TM50N_POST administered. Course evaluation.

---

---

# PART O — TM-50O: ADVANCED PLATFORM ENGINEER

**Duration:** 3 days (24 hours) | **T:I ratio:** 6:1 | **Instructor req:** Senior Platform Engineer with multi-cluster fleet management and SRE experience; TM-50O certified or C2DAO Advanced Platform SME
**Note:** TM-50O is 3 days (24 hours), not 5 days.

---

### Block 1 — From Cluster Operations to Fleet Management
**Hours:** 1.0 | **Method:** Seminar | **Day:** 1 | **Time:** 0800–0900

**Purpose:** TM-50O moves from operating a single cluster to operating a fleet — and from building infrastructure to building the systems that build infrastructure. The same principle that made TM-40O treat pods as cattle applies at TM-50O to clusters themselves.

**TLO:** The trainee will distinguish fleet management from single-cluster operations, describe the fleet topology model for MSS (hub and edge clusters across regions and classification levels), and state the Cluster API approach to declarative cluster lifecycle management.

**Key Delivery Notes:**
- Scale shift: "How do I deploy to this cluster?" → "How do I deploy to 20 clusters safely?" "Is this cluster healthy?" → "What is the fleet-wide health posture?" "How do I upgrade Kubernetes?" → "How do I upgrade the fleet without downtime?"
- Fleet management is systems thinking: at TM-40O, you solve problems one cluster at a time. At TM-50O, you solve problems by building systems that solve them automatically across the fleet. Manual procedures that work for one cluster do not scale to twenty.
- Cluster API: clusters are provisioned from templates, configured via GitOps, upgraded in waves, and decommissioned when no longer needed. Clusters are cattle, not pets — the same principle from TM-40O applied one level up.

**Assessment:** Fleet management approach evaluated throughout course; assessed in capstone (Day 3).

---

### Block 2 — Fleet Provisioning
**Hours:** 2.0 | **Method:** Lab | **Day:** 1 | **Time:** 0900–1100

**TLO:** The trainee will define cluster templates and provision a multi-cluster fleet declaratively using Cluster API — with parameterized configuration for region, classification level, and workload profile.

**Key Delivery Notes:**
- Cluster template: defines the cluster's Kubernetes version, node pool configuration, network configuration, and default policies. Templates are versioned in Git.
- Parameterized provisioning: same template, different parameters for each environment (region, classification, workload profile). Do not maintain separate templates for each cluster.
- Fleet topology: hub cluster (management plane, GitOps controllers, monitoring aggregation) and edge clusters (workload execution, regional deployment). Design the topology before provisioning.

---

### Block 3 — Fleet-Wide Upgrades
**Hours:** 0.75 | **Method:** Lab | **Day:** 1 | **Time:** 1115–1200

**Key Delivery Notes:**
- Wave-based rollout: upgrade clusters in waves — canary cluster first (lowest-risk workload), then wave 1 (non-production), then wave 2 (production non-critical), then wave 3 (production critical). Wait for validation between waves.
- Canary validation: after upgrading the canary cluster, run automated health checks. If health checks pass, proceed to wave 1. If they fail, stop and investigate. Never proceed to the next wave with a failing canary.
- Automated rollback: if a wave fails validation, automatically rollback the affected clusters to the previous version. Manual intervention should not be required for rollback.

---

### Block 4 — SRE Fundamentals: SLOs, SLIs, and Error Budgets
**Hours:** 2.0 | **Method:** Seminar + Lab | **Day:** 1 | **Time:** 1300–1500

**Purpose:** Perfect reliability is impossible and undesirable. SRE defines "reliable enough" and manages the gap between perfect and enough. Error budgets convert reliability from a vague aspiration into a concrete decision framework.

**TLO:** The trainee will define SLOs and SLIs for MSS platform services, compute an error budget, and describe the budget-based decision policy (when the budget is exhausted, stop shipping and fix reliability).

**Key Delivery Notes:**
- SLI (Service Level Indicator): the metric that measures the service's behavior. For a platform: API server availability (% of successful API calls), pod scheduling latency (p99 time from pod creation to running), deployment success rate.
- SLO (Service Level Objective): the target for the SLI. "API server availability >= 99.9% over 30 days." The SLO is a decision boundary — above the SLO, ship features; below the SLO, fix reliability.
- Error budget: 100% minus the SLO target. For 99.9% availability, the error budget is 0.1% = ~43 minutes of downtime per month. This budget is available for deployments, experiments, upgrades, and maintenance.
- Budget-based policy: when the error budget is exhausted, the team stops shipping features and focuses on reliability. This aligns platform engineers and application developers on shared trade-offs.

**Assessment:** SLO framework evaluated in capstone (Day 3).

---

### Block 5 — Incident Management
**Hours:** 1.75 | **Method:** Lab | **Day:** 1 | **Time:** 1515–1700

**TLO:** The trainee will execute a blameless post-incident review following the detect-triage-mitigate-resolve-review-improve framework — producing an incident report with timeline, root cause, and preventive actions.

**Key Delivery Notes:**
- Tabletop exercise: walk through a platform incident scenario. The trainee practices the full incident lifecycle: detect (alert fires), triage (severity assessment), mitigate (immediate action to reduce impact), resolve (permanent fix), review (blameless postmortem), improve (preventive actions implemented).
- Blameless: the postmortem identifies system failures, not individual failures. "The deployment process allowed an untested change to reach production" — not "Engineer X deployed without testing." Systems fail; fix the system.
- Incident report: timeline (with DTGs), impact assessment, root cause analysis, contributing factors, immediate actions taken, and preventive actions with owners and deadlines.
- Preventive actions must be trackable: add to the team backlog with priority. A preventive action that is "noted" but never implemented is a future incident waiting to happen.

---

### Block 6 — RMF/ATO Compliance Automation
**Hours:** 2.0 | **Method:** Seminar + Lab | **Day:** 2 | **Time:** 0830–1030

**TLO:** The trainee will build an automated compliance pipeline that generates RMF evidence from live system data — scan results, configuration baselines, access logs — and present the evidence through a compliance dashboard.

**Key Delivery Notes:**
- Continuous compliance: if compliance is a manual process, it is a point-in-time snapshot that is outdated the moment it is completed. Continuous compliance means the system proves its own compliance state — automatically, continuously, with evidence.
- Evidence generation: automated vulnerability scans (evidence of patch compliance), configuration baseline comparisons (evidence of configuration compliance), access log aggregation (evidence of access control compliance). All evidence timestamped and stored.
- Evidence API: the AO can query compliance status at any time. Evidence is always current. No manual checklist required.
- Why this matters: the ATO is the legal authorization to process operational data. If the ATO is revoked because compliance evidence is stale, MSS goes offline — every WFF track loses their platform.

---

### Block 7 — STIG Automation
**Hours:** 1.25 | **Method:** Lab | **Day:** 2 | **Time:** 1045–1200

**TLO:** The trainee will implement policy-as-code STIG checks with pass/fail/exception reporting and a compliance dashboard.

**Key Delivery Notes:**
- Policy-as-code: STIG requirements expressed as code that can be automatically evaluated against live system state. Each STIG finding has a corresponding policy check.
- Pass/fail/exception: each check returns pass (compliant), fail (non-compliant), or exception (non-compliant with documented and approved exception). Exceptions require an exception memo from the AO — the automation tracks the memo and its expiration date.
- Compliance dashboard: aggregate pass/fail/exception across all STIG findings. Filter by severity. Track compliance trend over time. A declining compliance trend triggers a review.

---

### Block 8 — Developer Experience Engineering
**Hours:** 2.0 | **Method:** Seminar + Lab | **Day:** 2 | **Time:** 1300–1500

**TLO:** The trainee will design a golden path for MSS application onboarding that takes a new project from template to deployed application in <90 minutes — with pre-configured CI/CD, monitoring, and security scanning.

**Key Delivery Notes:**
- Golden path: a pre-tested, documented, secured, and supported path from "new project" to "deployed application." Developer runs a template command, gets a repo with CI/CD pipeline, monitoring dashboards, security scanning, and deployment configuration pre-configured.
- Golden paths are not mandatory — developers can deviate. But the golden path is tested, documented, secured, and supported. Deviation paths are "you built it, you own it." This creates a natural incentive to follow the golden path.
- DORA metrics: deployment frequency, lead time for changes, change failure rate, time to restore service. These are the primary signal for developer experience. If DORA metrics are declining, the platform is failing its users — regardless of infrastructure metrics.
- Self-service portal: developers should be able to provision what they need without filing a ticket. Every ticket is a platform gap.

---

### Block 9 — Golden Path Build
**Hours:** 1.75 | **Method:** Lab | **Day:** 2 | **Time:** 1515–1700

**Key Delivery Notes:**
- Build an application onboarding template: pre-configured repository structure, Dockerfile (hardened base, multi-stage, non-root), CI/CD pipeline definition with security gates, Kubernetes manifests with resource limits and health checks, monitoring dashboard template, and a README with onboarding instructions.
- Test the golden path: have a peer trainee follow the golden path from template to deployed application. Measure time to deploy. Target: <90 minutes. If it takes longer, identify the bottleneck and fix it.
- Onboarding documentation: the golden path README is the first document a new developer reads. It must be clear, complete, and tested.

---

### Block 10 — Fleet-Scale Observability
**Hours:** 1.0 | **Method:** Seminar | **Day:** 3 | **Time:** 0800–0900

**TLO:** The trainee will describe federated observability architecture across multiple clusters — covering federated metrics, centralized logging, distributed tracing, and SLO-based alerting at fleet scale.

**Key Delivery Notes:**
- At fleet scale, observability is not "can I see what this pod is doing?" — it is "can I correlate an event across 20 clusters, 200 services, and 3 classification domains to understand what happened and why?"
- Federated metrics: Prometheus federation or remote-write to a central metrics store. Cross-cluster dashboards aggregate metrics from all clusters. SLO-based alerts fire when fleet-wide SLIs breach SLO thresholds.
- Centralized logging: logs from all clusters forwarded to a centralized log store. Cross-cluster search capability. Retention policies per classification level.
- Alert philosophy at scale: alert on SLO violations, not on individual pod restarts. A single pod restart is noise. A fleet-wide increase in pod restart rate is a signal.

---

### Block 11 — Federated Monitoring Lab
**Hours:** 2.0 | **Method:** Lab | **Day:** 3 | **Time:** 0900–1100

**TLO:** The trainee will configure cross-cluster metric federation and SLO-based alerting — demonstrating correlation of metrics across multiple clusters.

**Key Delivery Notes:**
- Configure Prometheus federation between two training clusters. Build a cross-cluster dashboard showing fleet-wide resource utilization, pod health, and deployment status.
- SLO-based alerting: configure an alert that fires when the fleet-wide API server availability drops below the SLO target. Demonstrate that the alert fires and routes to the correct notification channel.
- Cross-cluster correlation: when a platform event (e.g., upgrade) occurs on one cluster, correlate the metric impact across all clusters in the federation.

---

### Block 12 — Cross-Domain Infrastructure
**Hours:** 0.75 | **Method:** Seminar | **Day:** 3 | **Time:** 1115–1200

**Key Delivery Notes:**
- Multi-classification cluster management: separate clusters per classification level. Configuration replication through approved cross-domain solutions (data diodes, CDS). Never direct network connectivity between classification levels.
- Data diode integration: one-way data transfer from lower to higher classification. Monitoring data from UNCLASSIFIED clusters can flow to SECRET monitoring aggregation. Not the reverse.
- Cross-domain replication: application artifacts (container images, configuration) must be replicated to each classification level through approved transfer procedures. Air-gapped deployment procedures from TM-40O apply at fleet scale.

---

### Block 13 — Capstone Exercise
**Hours:** 2.0 | **Method:** Evaluation | **Day:** 3 | **Time:** 1300–1500

**Tasks:**

| Task | Standard |
|------|----------|
| 1 | Design a fleet topology for MSS spanning hub and edge clusters across two regions — with cluster templates, upgrade strategy, and rollback procedures |
| 2 | Define SLOs and SLIs for MSS platform services with error budgets and budget-based decision policies |
| 3 | Build an automated compliance pipeline that generates RMF evidence from live system data with a compliance dashboard |
| 4 | Configure federated observability across multiple clusters with SLO-based alerting |

**Go standard:** Pass all 4 tasks. Fleet topology is declaratively provisioned. SLOs include error budgets with decision policies. Compliance pipeline produces evidence automatically. Federated alerting fires on SLO breach.

**Hard No-Go:** Fleet upgrade strategy with no rollback procedure. SLO definition with no error budget. Compliance pipeline that requires manual evidence collection.

---

### Block 14 — Capstone Presentations and Peer Review
**Hours:** 1.25 | **Method:** Workshop | **Day:** 3 | **Time:** 1515–1630

**Key Delivery Notes:**
- Each trainee presents their capstone: fleet topology, SLO framework, compliance pipeline, and observability architecture.
- Peer review: structured critique using TM-50O review criteria. Focus on scalability, automation completeness, and operational feasibility.
- Evaluator debrief: feedback on fleet management thinking, SRE maturity, and compliance automation depth.

---

### Block 15 — Post-Test and Course Evaluation
**Hours:** 0.5 | **Method:** Evaluation | **Day:** 3 | **Time:** 1630–1700

**Post-test:** EXAM_TM50O_POST administered. Course evaluation.

---

---

## TM-50 INSTRUCTOR NOTES — APPLICABLE TO ALL TRACKS

**Instructor qualification bar is high.** TM-50 instructors must be actively practicing at the level they teach. An instructor who completed TM-50G two years ago and has not done advanced ORSA work since is not qualified to teach TM-50G. Verify currency before assignment.

**Enrollment gatekeeping.** Before confirming any TM-50 enrollment, verify: (1) TM-40 Go evaluation is on file for the corresponding track, (2) the trainee is in a role that requires TM-50-level work, (3) prerequisite access has been confirmed (GPU, advanced AIP Logic, CI/CD, etc. — minimum 10 duty days lead time).

**Access lead times:**
- Code Workspace GPU allocation: 7–10 duty days (C2DAO request)
- AIP Logic multi-agent features: 7+ duty days (C2DAO request)
- CI/CD pipeline access (TM-50L): 7+ duty days (C2DAO request)
- Design tool licenses (TM-50N): 7+ duty days (coordinate with C2DAO)
- Multi-cluster fleet access (TM-50O): 10+ duty days (C2DAO request; requires namespace-admin on training fleet)

**Peer review is a graded component.** For TM-50G and TM-50M, the peer review exercise (Day 4) is evaluated. A trainee who fails to conduct a substantive peer review does not receive credit for that block.

**Evaluation format:** All TM-50 courses end with a multi-part practical evaluation. The evaluator does not answer technique questions during the evaluation. Go/No-Go is communicated at end of the final day.

**Hard No-Go conditions:** Each track has explicit Hard No-Go conditions stated in the practical exercise standard. These cannot be compensated by strong performance on other tasks.

---

*USAREUR-AF Operational Data Team*
*TM-50 Advanced Track Lesson Plan Outlines | Version 1.1 | March 2026*
