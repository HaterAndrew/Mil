# ENVIRONMENT SETUP — EX_40O Platform Engineer

**Track:** EX_40O — Platform Engineer (TM-40O) | **Prerequisite:** TM-30 REQUIRED | **Continuation:** TM-50O — Advanced Platform Engineer
**Companion exams:** EXAM_TM40O_PRE (administer before exercise), EXAM_TM40O_POST (administer after exercise)

## Environment Type

Kubernetes training cluster with namespace-admin privileges, container registry, CI/CD tooling, and Git server.

## Required Access

| Account | Permissions Required |
|---------|---------------------|
| Training accounts | Kubernetes namespace-admin (one namespace per trainee); container registry push/pull; Git repo create/push |
| Air-gap simulation namespace | Second namespace per trainee with external registry access disabled (for Task 6) |
| Evaluator account | Cluster-reader on all training namespaces |

## Pre-Load Instructions

### 1. Kubernetes Cluster

| Attribute | Value |
|-----------|-------|
| Cluster | Shared training cluster with sufficient capacity for all trainees |
| Namespaces | Pre-create namespace prefix per trainee (e.g., `ex40o-trainee01`) |
| RBAC | Namespace-admin RoleBinding per trainee; verify no cluster-admin access |
| Network policy support | Cluster must support NetworkPolicy (Calico, Cilium, or equivalent CNI) |
| GitOps controller | Pre-install a GitOps controller (kapp-controller, Flux, or ArgoCD) accessible to all training namespaces |

### 2. Container Registry

| Attribute | Value |
|-----------|-------|
| Registry | Internal container registry accessible from training cluster |
| Access | Per-trainee credentials with push and pull permissions to a dedicated repository path |
| Iron Bank images | Pre-stage at least one Iron Bank base image (e.g., `ironbank/opensource/nginx`) in the registry |

### 3. CI/CD Tooling

| Attribute | Value |
|-----------|-------|
| Pipeline tool | Pre-configured CI/CD system accessible to trainees (GitLab CI, Tekton, or equivalent) |
| Scanning tools | Container vulnerability scanner available (Trivy, Grype, or equivalent) |
| SAST/SCA tools | At least one static analysis tool configured and available |

### 4. Git Server

| Attribute | Value |
|-----------|-------|
| Server | Git server accessible from training environment (GitLab, Gitea, or equivalent) |
| Repos | Per-trainee repository with push access |
| Hooks | Pre-commit hook for secrets detection (optional but recommended) |

### 5. Training Application

Provide each trainee with:
- A simple web application source code (e.g., Python Flask or Node.js Express "hello world")
- A Dockerfile that intentionally has hardening gaps (runs as root, uses a non-Iron Bank base, references tag instead of digest)
- Kubernetes manifests without resource limits, probes, or network policies
- Trainees will fix these issues as part of the exercise

### 6. Monitoring Stack

| Attribute | Value |
|-----------|-------|
| Metrics | Prometheus (or compatible) with per-namespace metrics available |
| Dashboards | Grafana (or compatible) with trainee access to create dashboards |
| Alerting | AlertManager (or compatible) with trainee access to create alert rules |
