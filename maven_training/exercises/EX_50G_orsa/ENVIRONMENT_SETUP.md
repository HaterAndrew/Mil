# ENVIRONMENT SETUP — EX_50G Advanced ORSA (SL 5G)

**Companion resources:** TM_50G_ORSA_ADVANCED.md | SYLLABUS_TM50G | EXAM_TM50G_POST

## Environment Type

MSS Code Workspace with GPU allocation. Participants require Python environment access — this is not a standard viewer or Workshop exercise. Standard MSS training instance access is insufficient.

## Required Access

| Account | Role |
|---------|------|
| Participant | Code Workspace (Python), GPU allocation, training project read/write, Workshop publish (for Task 5 submission) |
| Evaluator | Training project read (to receive Task 5 Workshop link and review submitted notebooks), peer review notebook write (to plant errors before exercise) |

**Lead time:** Code Workspace with GPU must be requested from C2DAO no fewer than **10 duty days** before the exercise. Standard access requests take 3–5 duty days; GPU allocation requires additional approval. Do not defer this request.

## Pre-Load Instructions

### 1. Synthetic LOGSTAT Dataset

Load `EX_50G_ORSA_Training_Data/logstat_90day_synthetic.csv` into training project data source:

| Field | Type | Description |
|-------|------|-------------|
| `report_date` | date | LOGSTAT submission date (90 days of daily reports) |
| `unit_id` | string | BCT identifier (BCT-1, BCT-2, BCT-3) |
| `equipment_total` | int | Total reportable equipment items |
| `equipment_fmc` | int | Fully mission capable count |
| `equipment_pmcs` | int | Scheduled maintenance count |
| `readiness_pct` | float | Computed readiness rate (fmc / total) |

**Dataset design requirements:**
- BCT-1: Mean readiness ~0.84, moderate variance (stable unit)
- BCT-2: Mean readiness ~0.71, high variance (recovering unit; has a 2-week dip mid-period)
- BCT-3: Mean readiness ~0.91, low variance (high-performing unit)
- At least 85 of 90 days have reports for all three units; 5 days have at least one missing submission

Place in: `[Training Project]/EX_50G/source/`

### 2. Theater Distribution Network Graph

Load `EX_50G_ORSA_Training_Data/theater_distribution_network.json` (NetworkX node-link format):

| Element | Description |
|---------|-------------|
| Nodes | 18 distribution nodes (supply points, forward support areas, ports of entry) |
| Edges | Weighted edges representing route capacity (tons/day) and transit time (hours) |
| Node attributes | `node_id`, `type` (port/FSA/DSA/supply_point), `location` (lat/lon), `daily_throughput_tons` |
| Edge attributes | `from`, `to`, `capacity_tons_day`, `transit_hours`, `reliability` (0–1 scale) |

**Dataset design requirements:**
- Graph is connected with two primary hubs (high betweenness centrality) and one secondary hub
- Removing the top betweenness node should increase average path length by ≥30%
- At least one node has high degree but low betweenness (common distractor)

### 3. Route Options Dataset

Load `EX_50G_ORSA_Training_Data/route_options_synthetic.csv`:

| Field | Type | Description |
|-------|------|-------------|
| `route_id` | string | Route identifier (R01–R10) |
| `speed_score` | float (0–1) | Normalized speed (1 = fastest) |
| `fuel_score` | float (0–1) | Normalized fuel efficiency (1 = most efficient) |
| `risk_score` | float (0–1) | Normalized threat risk (1 = lowest risk) |
| `dominated` | bool | Pre-computed label for evaluator reference only |

**Dataset design requirements:**
- 3–4 routes on the Pareto frontier (non-dominated)
- 6–7 routes dominated by at least one other option
- No route optimal on all three objectives (forces Pareto tradeoff analysis)
- Under priority (minimize risk, then fuel): one clear Pareto-optimal selection at R05 or R07

### 4. Peer Review Notebook

Prepare `EX_50G_peer_review_notebook.ipynb` with 3 planted errors (see EXERCISE.md Evaluator Notes for error descriptions). Distribute to participant via the training project folder at exercise start — do not pre-share.

Blank USAREUR-AF ORSA peer review form (`peer_review_form_blank.md`) must be placed in participant's project folder before exercise start. Form sections: (1) Data Inputs, (2) Methodology, (3) Uncertainty Characterization, (4) Product Standards Compliance.

### 5. Python Environment Verification

Verify before exercise day (run in participant's Code Workspace):

```python
import scipy
import pymc       # or pymc3 — either accepted
import networkx
import mesa
import matplotlib
import numpy
import pandas
print("All imports OK")
```

If any import fails, escalate to C2DAO immediately — do not proceed with the exercise until resolved.

## Environment URL

```
[Insert training MSS tenant URL here]
```

## Scoring Sheet Reference

Evaluators record task Go/No-Go on standard EX_50G Evaluation Form (available from training NCO). Record specific peer review errors identified (Task 4) for AAR analysis. Overall Go/No-Go, participant name, evaluator name, and date required for training record submission.

## Notes

- GPU allocation is required for MCMC sampling (Task 1 with pymc); CPU-only sampling may time out on the 90-day dataset at full MCMC
- The peer review notebook errors are calibrated at the level a SL 5G-qualified analyst should catch; do not hint at error locations during the exercise
- If the training environment does not support Code Workspace with Python on exercise day, postpone — there is no viable substitution for this exercise
- All datasets are entirely synthetic; field names mirror operational schemas for training realism but contain no actual LOGSTAT or operational data
