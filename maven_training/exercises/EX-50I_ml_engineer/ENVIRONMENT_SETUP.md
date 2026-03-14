# ENVIRONMENT SETUP — EX-50I Advanced ML Engineer (TM-50I)

**Companion resources:** TM_50I_ML_ENGINEER_ADVANCED.md | SYLLABUS_TM50I | EXAM_TM50I_POST

## Environment Type

MSS Code Workspace (Python, GPU) and Pipeline Builder (write access). Standard viewer or Workshop-only access is insufficient. Both Code Workspace and Pipeline Builder write access must be confirmed operational before exercise day.

## Required Access

| Account | Role |
|---------|------|
| Participant | Code Workspace (Python, GPU), Pipeline Builder (create and configure triggers), Ontology read, training project read/write, Workshop publish |
| Evaluator | Training project read (to receive Task 5 submission), Pipeline Builder read (to verify trigger configuration) |

**Lead time:** Code Workspace with GPU must be requested from C2DAO no fewer than **10 duty days** before exercise. Pipeline Builder write access is a separate permission — confirm both independently. Do not assume one implies the other.

## Pre-Load Instructions

### 1. Production Model Artifacts

Load `EX-50I_ML_Training_Data/production_model_v2_artifacts/` into training project:

| File | Description |
|------|-------------|
| `model_v2.pkl` | Serialized production model (sklearn Pipeline or equivalent) |
| `training_data_window.csv` | 180-day training window used for v2 (reference distribution) |
| `training_distribution_stats.json` | Pre-computed feature statistics for drift baseline (mean, std, percentiles) |
| `production_config.yaml` | Hyperparameter config: learning_rate, max_depth, n_estimators, etc. |
| `validation_auc_baseline.json` | Recorded production AUC for promotion gate comparison (Task 2) |

### 2. Current Serving Data

Load `EX-50I_ML_Training_Data/current_serving_data_synthetic.csv`:

| Field | Description |
|-------|-------------|
| `unit_id` | Unit identifier |
| `report_date` | LOGSTAT submission date |
| `equip_age_months` | Primary feature — has moderate-to-severe drift (PSI ~0.22) |
| `maint_cycle_days` | Primary feature — no drift (PSI ~0.07) |
| `usage_hours_week` | Primary feature — moderate drift (PSI ~0.18) |
| `readiness_pct` | Target variable |
| `unit_type` | BCT / sustainment / aviation (for Task 3 bias stratification) |

**CRITICAL:** Verify drift is intact after load. Run a quick PSI check before exercise day:
- Feature A (equip_age_months): PSI should be ~0.22
- Feature B (maint_cycle_days): PSI should be ~0.07
- Feature C (usage_hours_week): PSI should be ~0.18

If values deviate significantly, regenerate the dataset using the seed script in `EX-50I_ML_Training_Data/generate_synthetic_data.py`.

### 3. Candidate Model Architectures

Load `EX-50I_ML_Training_Data/candidate_model_architectures/`:

| File | Description | Designed characteristics |
|------|-------------|--------------------------|
| `candidate_model_A.pkl` | Gradient boosted ensemble | Higher AUC (~0.89) but poorly calibrated (Brier ~0.18) |
| `candidate_model_B.pkl` | Calibrated random forest | Lower AUC (~0.84) but well calibrated (Brier ~0.09) |
| `test_set_held_out.csv` | Held-out test set | Shared across all three models for fair comparison |

The design intent: Model A is tempting on AUC alone but poor for probability-based planning. Model B is better for operational decisions that depend on calibrated probability estimates. The exercise forces participants to reason about operational consequences, not just metric maximization.

### 4. Python Environment Verification

Verify before exercise day (run in participant's Code Workspace):

```python
import sklearn
import scipy.stats        # for Kolmogorov-Smirnov
import numpy
import pandas
import matplotlib
import joblib             # for model artifact loading
from sklearn.calibration import calibration_curve, CalibrationDisplay
print("All imports OK")
# Quick check: load production model artifact
import joblib
model = joblib.load("production_model_v2_artifacts/model_v2.pkl")
print(f"Model loaded: {type(model)}")
```

### 5. Pipeline Builder Configuration

Confirm participant has Pipeline Builder access by verifying they can:
1. Open Pipeline Builder in the training project
2. Create a new dataset transform (blank)
3. Configure a schedule trigger (does not need to save — just confirm the UI is accessible)

If Pipeline Builder is read-only for the participant, escalate to C2DAO before exercise day — this is a blocking requirement for Task 2.

### 6. Blank Responsible AI Assessment

Place `usareur_responsible_ai_assessment_blank.md` in participant's project folder:

Sections:
1. Intended Use Statement
2. Fairness Analysis Summary
3. Failure Mode Documentation (table: failure mode, likelihood, impact, mitigation)
4. Human Oversight Declaration
5. Signature block

## Environment URL

```
[Insert training MSS tenant URL here]
```

## Scoring Sheet Reference

Evaluators record task Go/No-Go on standard EX-50I Evaluation Form (available from training NCO). For Task 2, photograph or screenshot the configured pipeline trigger for training records. For Task 3, the model comparison table should be attached to the evaluation form. Overall Go/No-Go, participant name, evaluator name, and date required for training record submission.

## Notes

- GPU is required for ensemble model training components; CPU-only execution may time out on the candidate model evaluation step with large test sets
- If Pipeline Builder write access cannot be provisioned on exercise day, Task 2 may be completed as a documented design (flowchart + configuration specification), but this is a graded deviation — note on evaluation form
- All models are serialized synthetic artifacts; they contain no real readiness data or unit-identifiable information
- The drift values are seeded deterministically — if the dataset is regenerated, use the same random seed (seed=42 in the generate script) to preserve the designed PSI values
