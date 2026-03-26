# ENVIRONMENT SETUP — EX_50O Advanced Platform Engineer

**Track:** EX_50O — Advanced Platform Engineer (SL 5O) | **Prerequisite:** SL 4O REQUIRED (Go evaluation on file) | **Base environment:** EX_40O (extended)
**Companion exams:** EXAM_TM50O_PRE (administer before exercise), EXAM_TM50O_POST (administer after exercise)

## Environment Type

Extended EX_40O environment: multi-cluster Kubernetes training environment with fleet management tooling, observability stack, and compliance automation. See [EX_40O ENVIRONMENT_SETUP.md](../EX_40O_platform_engineer/ENVIRONMENT_SETUP.md) for base environment setup.

## Base Environment (EX_40O)

Complete **all** EX_40O environment setup steps before proceeding:

1. Kubernetes cluster with namespace-admin privileges per trainee
2. Container registry with per-trainee push/pull access and Iron Bank base images
3. CI/CD tooling with container scanning and SAST/SCA tools
4. Git server with per-trainee repositories
5. Training application (intentionally flawed Dockerfile and manifests)
6. Monitoring stack (Prometheus, Grafana, AlertManager or equivalents)

## SL 5O-Specific Extensions

The following extend the EX_40O environment for fleet-level, advanced tasks.

### 1. Multi-Cluster Fleet Environment

| Attribute | Value |
|-----------|-------|
| Hub cluster | Primary management cluster with fleet-wide visibility |
| Edge clusters | At least 2 simulated edge clusters (can be namespaces with network restrictions simulating separate clusters) |
| Management plane | Fleet management tooling (Rancher, OpenShift ACM, or equivalent) accessible to trainees |
| Connectivity simulation | Ability to degrade network between hub and edge (network policies or traffic control) to simulate DDIL conditions |

### 2. Fleet Observability Stack

| Component | Purpose |
|-----------|---------|
| Federated metrics | Prometheus federation or Thanos/Cortex for cross-cluster metric aggregation |
| Centralized logging | Log aggregation from all clusters (Loki, EFK, or equivalent) |
| Distributed tracing | Trace collection across clusters (Jaeger, Tempo, or equivalent) |
| SLO tooling | Burn-rate alert configuration capability (Sloth, Pyrra, or native Prometheus recording rules) |

### 3. Compliance Automation Tooling

| Component | Purpose |
|-----------|---------|
| Policy engine | OPA/Gatekeeper, Kyverno, or equivalent for policy-as-code enforcement |
| STIG reference | At least 5 STIG-equivalent controls documented for Kubernetes (container non-root, resource limits, network policy, etc.) |
| Evidence export | Tooling or scripting capability to export compliance status to a structured format (JSON/CSV) |

### 4. Incident Scenario Package

For Task 4 (Post-Incident Review), provide each trainee with:
- A written incident scenario describing a fleet-wide deployment failure affecting 3+ clusters
- Timeline data: deployment start time, first alerts, escalation points, resolution
- Simulated monitoring screenshots or data exports showing the degradation pattern
- Blank post-incident review template

### 5. Golden Path Starter Kit

For Task 6 (Golden Path and Developer Experience):
- A skeleton application template repository
- Pre-configured but incomplete CI/CD pipeline (trainees complete it)
- DORA metrics reference card (deployment frequency, lead time, change failure rate, MTTR)
