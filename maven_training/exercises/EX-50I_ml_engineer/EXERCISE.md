# EX-50I — Advanced ML Engineering
## Practical Exercise — TM-50I Proficiency

| Field | Value |
|-------|-------|
| **Version** | 1.0 — March 2026 |
| **Prerequisite** | TM-40I complete (Go on file); TM-50I course completion; Code Workspace with GPU and pipeline write access confirmed |
| **Duration** | 6–8 hours (typically executed Day 5 of TM-50I) |
| **Environment** | MSS Code Workspace (Python, GPU), Pipeline Builder (write access), Ontology read; see ENVIRONMENT_SETUP.md |
| **Companion TM** | TM_50I_ML_ENGINEER_ADVANCED.md |
| **Syllabus** | SYLLABUS_TM50I |
| **Exams** | EXAM_TM50I_POST |

## SCENARIO

You are the senior ML Engineer for USAREUR-AF. Your team runs a predictive equipment readiness model in production. You have been tasked with a one-day audit and hardening of the production model pipeline:

1. Detect whether the production model has drifted since its last training run
2. Design and configure an automated retraining trigger based on drift detection results
3. Evaluate two candidate ensemble architectures against the current production baseline
4. Complete a Responsible AI assessment for the model and document the results

**Training environment:** All data, models, and pipeline configurations use synthetic datasets. No operational equipment data is used.

## TASK LIST

### Task 1 — Drift Detection Audit (75 min)

Using the `production_model_v2_artifacts/` package and `current_serving_data_synthetic.csv`:

- [ ] Compute feature drift for the three primary input features using Population Stability Index (PSI) or Kolmogorov-Smirnov test; document which test was selected and why
- [ ] Compute prediction distribution drift: compare current model output distribution against the training distribution baseline
- [ ] Classify drift severity for each feature: none (PSI < 0.1 or KS p > 0.1), moderate (PSI 0.1–0.25), severe (PSI > 0.25)
- [ ] Write a 3–5 sentence drift summary: which features have drifted, severity classification, and recommendation (retrain now / monitor / no action)

| Standard | Criteria |
|----------|----------|
| **Go** | Both feature drift and prediction distribution drift computed; drift test selection documented with rationale; severity classified per feature; drift summary with recommendation present |
| **No-Go** | Only one drift metric computed; no severity classification; recommendation absent; test selection not documented |

### Task 2 — Automated Retraining Trigger (60 min)

- [ ] Configure a pipeline trigger in Pipeline Builder: fires when PSI for any primary feature exceeds 0.15 on a weekly drift check run
- [ ] Define the retraining pipeline inputs: new training data window (rolling 180 days), hyperparameter config (inherit from current production config), and validation dataset
- [ ] Configure a promotion gate: new model only promotes to production if validation AUC ≥ current production AUC − 0.02 (within 2% tolerance)
- [ ] Document the full trigger-to-promotion workflow in a 1-page architecture diagram or flowchart

| Standard | Criteria |
|----------|----------|
| **Go** | Trigger configured with correct PSI threshold (0.15) and weekly cadence; promotion gate configured with AUC tolerance; 1-page workflow documented |
| **No-Go** | Trigger not configured in Pipeline Builder (documented only); promotion gate absent; workflow documentation absent |

### Task 3 — Ensemble Evaluation (90 min)

Using the `candidate_model_architectures/` package (two pre-trained candidate models + production baseline):

- [ ] Evaluate all three models on the held-out test set: AUC, F1, precision, recall; record results in a comparison table
- [ ] Evaluate calibration for each model: plot calibration curves; compute Brier score; identify which model is best calibrated
- [ ] Select the recommended model for production; justify the selection with reference to evaluation metrics AND the operational use case (consequences of false positive vs. false negative readiness prediction)
- [ ] Document bias check: evaluate model performance stratified by unit type (BCT vs. sustainment vs. aviation); flag any performance gap ≥10% across strata

| Standard | Criteria |
|----------|----------|
| **Go** | Comparison table complete (AUC, F1, precision, recall for all three); calibration curves plotted with Brier scores; recommendation justified with both metrics and operational consequence reasoning; bias check by unit type completed |
| **No-Go** | Comparison table incomplete; no calibration evaluation; recommendation not tied to operational consequences; bias check absent |

### Task 4 — Responsible AI Assessment (45 min)

Complete the USAREUR-AF Responsible AI Model Assessment for the production readiness model:

- [ ] Intended use statement: what decisions the model supports, what decisions require human override
- [ ] Fairness analysis summary: document the Task 3 bias check results; describe the remediation plan if a ≥10% performance gap was found
- [ ] Failure mode documentation: at least 3 failure modes with likelihood, impact, and mitigation (e.g., data pipeline failure, sensor dropout, distribution shift)
- [ ] Human oversight declaration: identify at least 2 specific decision types where model output alone is insufficient
- [ ] Sign and submit assessment to evaluator via Workshop

| Standard | Criteria |
|----------|----------|
| **Go** | All four sections completed; fairness analysis references Task 3 bias check results; failure mode register has ≥3 entries; human oversight declaration names ≥2 specific decision types |
| **No-Go** | Any section absent; fairness analysis does not reference actual evaluation results; fewer than 3 failure modes; human oversight declaration is generic |

### Task 5 — Production Handoff Package (30 min)

Assemble the production handoff package:

- [ ] Model card: model name, version, training date, training data window, key metrics (AUC, F1, Brier score), known limitations, recommended use cases
- [ ] Retraining SOP: step-by-step procedure for the retraining pipeline trigger, evaluation, promotion, and rollback
- [ ] Responsible AI assessment (from Task 4): attached and signed
- [ ] Submit package to evaluator via Workshop read-only link

| Standard | Criteria |
|----------|----------|
| **Go** | Model card complete with all required fields; retraining SOP is step-by-step (not narrative); RA assessment attached; Workshop link delivers read-only access |
| **No-Go** | Model card missing key fields; SOP is narrative without numbered steps; RA assessment not attached; edit access granted on Workshop link |

## EVALUATOR NOTES

**Scoring:** 5 tasks. Go on 4 of 5 = overall Go. No-Go on Task 1 or Task 3 = automatic No-Go (core drift detection and model evaluation standards).

### Pre-Exercise Checklist

- [ ] Confirm Code Workspace with GPU provisioned — 10 duty days prior
- [ ] Confirm Pipeline Builder write access (trigger and pipeline configuration) — not standard viewer access
- [ ] Load training data package: `production_model_v2_artifacts/`, `current_serving_data_synthetic.csv`, `candidate_model_architectures/` — verify all load without schema errors
- [ ] Place blank USAREUR-AF Responsible AI Model Assessment in participant's project folder
- [ ] Confirm drift in `current_serving_data_synthetic.csv` as designed: Feature A (PSI 0.22 — moderate-to-severe), Feature B (PSI 0.07 — no drift), Feature C (PSI 0.18 — moderate)
- [ ] Confirm candidate models: Model A has higher AUC but worse calibration; Model B is lower AUC but better calibrated; production baseline is in between — forcing a real tradeoff decision

### Synthetic Dataset Drift Design

| Feature | Training Distribution | Serving Distribution | Expected PSI |
|---------|----------------------|----------------------|--------------|
| Feature A (equip_age_months) | Normal(48, 12) | Normal(58, 15) | ~0.22 (moderate-severe) |
| Feature B (maint_cycle_days) | Normal(30, 5) | Normal(31, 5) | ~0.07 (no drift) |
| Feature C (usage_hours_week) | Normal(40, 8) | Normal(46, 10) | ~0.18 (moderate) |

### Common Failure Modes

| Task | Common Failure | Evaluator Guidance |
|------|---------------|--------------------|
| Task 1 | PSI computed but KS not (or vice versa) — only one test per feature | One test per feature is acceptable if the selection is documented and justified |
| Task 1 | Drift summary recommends no action despite moderate drift | Ask: "At PSI 0.22 for equipment age, what would you recommend?" — moderate-to-severe drift on a primary feature should trigger at least a monitoring escalation |
| Task 2 | Trigger documented in text but not configured in Pipeline Builder | No-Go on that criterion — must be configured, not just described |
| Task 3 | Model recommended on AUC alone without calibration consideration | Ask: "If this model is deployed for readiness planning, which is more dangerous — a false positive or false negative?" — calibration matters for asymmetric consequences |
| Task 3 | Bias check not stratified by unit type | Common time-pressure skip; Task 3 No-Go on that criterion |
| Task 4 | Human oversight declaration is generic ("humans should always review") | Ask: "Name two specific decisions an S4 should not make based solely on this model's output." |
