# MSS TRAINING ANALYTICS SUITE — DEPENDENCY MAP
## USAREUR-AF Operational Data Team | C2DAO Training Branch

**Generated:** 18 March 2026
**Status:** 15 apps + portal + shared theme — all SQLite-backed, FastAPI + Streamlit

---

## READING THIS MAP

**Relationship symbols:**
- **→** requires / hard runtime dependency
- **↔** reads data from (try/except wrapped — graceful degradation)
- **⇢** seed-time or documentation reference only

**App tier tags:**

| Tag | Tier | Description |
|-----|------|-------------|
| **[CORE]** | Foundation | Authoritative data source; other apps depend on it |
| **[STANDALONE]** | Independent | Own database, no cross-app runtime imports |
| **[DEPENDENT]** | Dependent | Requires another app's DB/exports at runtime |
| **[AGGREGATOR]** | Read-Only Roll-Up | Collects metrics from multiple sibling apps |
| **[HUB]** | Portal | Central navigation and KPI dashboard |

---

## ARCHITECTURE OVERVIEW

```
                            ┌─────────────────────┐
                            │   portal.py [HUB]    │
                            │      Port 8500       │
                            └──────────┬──────────┘
                                       │ ↔ reads from all
          ┌────────────────────────────┼────────────────────────────┐
          │                            │                            │
  ┌───────┴───────┐          ┌─────────┴─────────┐       ┌─────────┴──────────┐
  │ CORE TIER     │          │ STANDALONE TIER    │       │ AGGREGATION TIER   │
  │               │          │                    │       │                    │
  │ readiness_    │ ←───────── progress_tracker   │       │ training_metrics   │
  │ tracker       │          │ enrollment_manager │       │ (↔ reads ALL apps) │
  │ [CORE]        │          │                    │       │ [AGGREGATOR]       │
  └───────────────┘          │ aar_aggregator     │       └────────────────────┘
                             │ exam_analytics     │
                             │ instructor_manager │
                             │ mtt_scheduler      │
                             │ curriculum_tracker │
                             │ lessons_learned    │
                             │ data_quality       │
                             │ glossary_search    │
                             │ xref_validator     │
                             │ offline_packager   │
                             │ sharepoint_sync    │
                             │ [STANDALONE]       │
                             └────────────────────┘
```

---

## APP CATALOG

### Core Tier

| App | Purpose | Ports | Dependencies |
|-----|---------|-------|--------------|
| [Readiness Tracker](readiness_tracker/README.md) | Authoritative trainee roster, course completion history, prerequisite enforcement, readiness funnel | API 8001 / UI 8501 | None — foundational. Exports `PREREQ_CHAIN`, `COURSE_CATALOG`, `check_eligibility()` to dependent apps |

### Dependent Tier

| App | Purpose | Ports | Dependencies |
|-----|---------|-------|--------------|
| [Progress Tracker](progress_tracker/README.md) | Individual milestone tracking, stalled/overdue detection, training records | API 8004 / UI 8504 | → [Readiness Tracker](readiness_tracker/README.md) (PREREQ_CHAIN, COURSE_CATALOG, trainee roster, check_eligibility) |

### Standalone Tier

| App | Purpose | Ports | Dependencies |
|-----|---------|-------|--------------|
| [Exam Analytics](exam_analytics/README.md) | Exam session tracking, pass/fail rates, question-level analysis, cross-cohort comparison | API 8002 / UI 8502 | None |
| [AAR Aggregator](aar_aggregator/README.md) | After-Action Review collection, recurring issue detection, improvement tracking | API 8003 / UI 8503 | None |
| [MTT Scheduler](mtt_scheduler/README.md) | Mobile Training Team event scheduling, instructor/venue assignment across USAREUR-AF AOR (Grafenwoehr, Vilseck, Wiesbaden, Vicenza, Poznan) | API 8005 / UI 8505 | None |
| [XRef Validator](xref_validator/README.md) | Cross-reference validation — scans maven_training/ corpus for broken links, stale refs, naming violations | API 8006 / UI 8506 | None (embeds local PREREQ_CHAIN copy) |
| [Glossary Search](glossary_search/README.md) | Searchable Army/MSS terminology glossary with fuzzy matching | API 8007 / UI 8507 | None |
| [Offline Packager](offline_packager/README.md) | Build offline training packages from maven_training/ corpus with prereq-aware dependency resolution | UI 8508 | None (embeds local PREREQ_CHAIN copy) |
| [SharePoint Sync](sharepoint_sync/README.md) | Track sync state of maven_training/ corpus against SharePoint document library | UI 8509 | None |
| [Data Quality](data_quality/README.md) | Data pipeline monitoring, metric thresholds, alert management, health scoring | API 8010 / UI 8510 | None |
| [Instructor Manager](instructor_manager/README.md) | Instructor certifications, course coverage matrix (RAG heatmap), expiration alerts, teaching workload | API 8011 / UI 8511 | None |
| [Enrollment Manager](enrollment_manager/README.md) | Class enrollment, seat allocation, waitlist management, roster CSV export | API 8012 / UI 8512 | ⇢ [Readiness Tracker](readiness_tracker/README.md) (seed-time roster names only) |
| [Curriculum Tracker](curriculum_tracker/README.md) | Document versioning, review cycles, content freshness, SHA-256 change detection across maven_training/ corpus | API 8013 / UI 8513 | None |
| [Lessons Learned](lessons_learned/README.md) | Structured lessons-learned pipeline (NEW → VALIDATED → ACTIONABLE → IMPLEMENTED → ARCHIVED) with tagging taxonomy aligned to TM-40K | API 8014 / UI 8514 | None |

### Aggregation Tier

| App | Purpose | Ports | Dependencies |
|-----|---------|-------|--------------|
| [Training Metrics](training_metrics/README.md) | Senior-leader / CG briefing dashboard. Aggregates data from ALL sibling apps into executive view. BLUF format per Army writing standards | API 8015 / UI 8515 | ↔ All apps (try/except wrapped — degrades gracefully) |

### Hub

| App | Purpose | Ports | Dependencies |
|-----|---------|-------|--------------|
| [Portal](portal.py) | Central navigation + cross-app KPI dashboard | UI 8500 | ↔ [Readiness Tracker](readiness_tracker/README.md), [Exam Analytics](exam_analytics/README.md), [AAR Aggregator](aar_aggregator/README.md) (mandatory) + all others (optional) |

### Shared

| Module | Purpose |
|--------|---------|
| [theme.py](theme.py) | Navy/Gold branding palette, USAREUR-AF insignia SVG, Plotly theme — imported by all dashboards |

---

## CROSS-APP DEPENDENCY GRAPH

```
readiness_tracker ──→ progress_tracker
                  ──→ training_metrics (via collect_all_metrics)
                  ⇢── enrollment_manager (seed-time names only)

exam_analytics ─────→ training_metrics
aar_aggregator ─────→ training_metrics
mtt_scheduler ──────→ training_metrics
data_quality ───────→ training_metrics
instructor_manager ─→ training_metrics
enrollment_manager ─→ training_metrics
curriculum_tracker ─→ training_metrics
lessons_learned ────→ training_metrics
progress_tracker ───→ training_metrics

theme.py ───────────→ ALL dashboards

portal.py ──────────↔ ALL apps (optional except RT, EA, AAR)
```

---

## SHARED CONSTANTS (AUTHORITATIVE)

| Constant | Source | Consumers |
|----------|--------|-----------|
| `PREREQ_CHAIN` | [Readiness Tracker](readiness_tracker/README.md) | Progress Tracker, XRef Validator, Offline Packager |
| `COURSE_CATALOG` | [Readiness Tracker](readiness_tracker/README.md) | Progress Tracker, Enrollment Manager |
| `ALL_COURSES` | [Readiness Tracker](readiness_tracker/README.md) | Readiness Tracker API |
| Theme colors/branding | [theme.py](theme.py) | All dashboards |

---

## MANDATORY STARTUP SEQUENCE

```
1. python -m apps.readiness_tracker.seed     ← MUST be first (foundational)
2. python -m apps.progress_tracker.seed      ← depends on readiness_tracker
3. python -m apps.{all other apps}.seed      ← independent, any order
4. python -m apps.training_metrics.seed      ← SHOULD be last (aggregates all)
5. streamlit run apps/portal.py --server.port 8500
```
