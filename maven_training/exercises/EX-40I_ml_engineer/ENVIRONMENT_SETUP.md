# ENVIRONMENT SETUP — EX-40I ML Engineer

## Environment Type

MSS with Python Transforms, Model Integration (Foundry model registry), and Ontology edit access.

## Required Access

| Account | Permissions Required |
|---------|---------------------|
| Training accounts | Python Transform create/edit, model registration, Ontology property write |

## Pre-Load Instructions

### 1. Dataset

Load synthetic PMCS records with NMC labels:

| Attribute | Value |
|-----------|-------|
| File | `EX-40I_PMCS_NMC_Training_Data.csv` (from training data package) |
| Row count | ~5,000 equipment events |
| Class balance | ~10% positive rate (`nmc_within_7d = True`) — intentionally imbalanced to drive Task 3 discussion |
| Null injection | ~5% nulls in `days_since_last_service` to require imputation |
| Destination | `[Training Project]/EX-40I/source/` |

**Schema:** `equipment_id`, `date`, `days_since_last_service` (int), `maintenance_count_30d`, `maintenance_count_60d`, `maintenance_count_90d`, `equipment_class` (categorical), `unit`, `nmc_within_7d` (boolean, target label)

### 2. Ontology Setup

Pre-create the following in the training Ontology:

| Element | Configuration |
|---------|--------------|
| Object Type | `Equipment` |
| Properties | `equipment_id` (primary key, string), `unit` (string), `equipment_class` (string), `nmc_risk_score` (float, model-backed — leave empty for participant to populate) |
| Permission | Training accounts must have permission to register model-backed properties |

### 3. Model Integration

- [ ] Confirm the Foundry model registry is accessible to training accounts
- [ ] Confirm training accounts can register a Python model artifact
- [ ] Confirm the `nmc_risk_score` property slot accepts a float output from a registered model

## Environment URL

```
[Insert training MSS tenant URL here]
```

## Notes

- The ~10% class imbalance is intentional — do not rebalance the dataset
- Participants who use accuracy as their primary metric without addressing imbalance should be prompted to explain their choice (teaching moment for Task 3)
- If Model Integration is unavailable, Task 4 cannot be completed — escalate to training management
