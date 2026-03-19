# AR 350-1 ALIGNMENT MAP

## Maven Smart System (MSS) Training Ecosystem — USAREUR-AF

---

## 1. PURPOSE

This document maps the Maven Smart System (MSS) training ecosystem to the requirements of AR 350-1 (Army Training and Leader Development). It serves as the authoritative compliance reference for the MSS training program, identifying regulatory alignment, supporting artifacts, and known gaps with planned mitigations.

## 2. COMPLIANCE SUMMARY

| Metric | Value |
|--------|-------|
| AR 350-1 Areas Assessed | 11 |
| Fully Addressed | 10 |
| Partially Addressed | 1 |
| SAT Artifacts | 7 |
| Analytics Applications | 15 |
| Course Tracks | 20+ |
| Identified Gaps | 3 (mitigations in progress) |

**BLUF:** MSS provides comprehensive AR 350-1 coverage for institutional training across USAREUR-AF. Full SAT artifact set, programmatic prerequisite enforcement, instructor certification pipeline, and closed-loop evaluation are in place. Remaining gaps are integration-level items with planned mitigations — none block training delivery.

---

## 3. REQUIREMENT ALIGNMENT TABLE

| AR 350-1 Reference | Requirement | MSS Components | Status |
|---------------------|-------------|----------------|--------|
| Ch 1 | Training Responsibilities | Training Metrics dashboard (BLUF exec view), command approval gates, Policy Letter | **FULL** |
| Ch 3-3 | Training Management Cycle (Plan/Prepare/Execute/Assess) | MTT Scheduler (plan), Curriculum Tracker (prepare), Enrollment Manager & Readiness Tracker (execute), Exam Analytics & AAR Aggregator (assess) | **FULL** |
| Ch 3-5 | Resource Allocation | MTT Scheduler (5 venues, instructor availability), Enrollment Manager (seat capacity, waitlist), capacity projections | **FULL** |
| Ch 3-12 | Training Schedules | Annual Training Schedule, LRTC integration, MTT Calendar (Gantt view, 5 venues) | **FULL** |
| Ch 3-14 | Training Evaluation | Pre/post exams via Exam Analytics (gain scores), AAR Aggregator (WFF categorization), Lessons Learned Pipeline (5-stage lifecycle) | **FULL** |
| Ch 3-18 | Instructor Certification | T3-I instructor track, Instructor Manager (certification tracking, expiry alerts, workload), Faculty Development Plan (4 tiers) | **FULL** |
| Ch 3-21 | Systems Approach to Training (SAT/ADDIE) | MTP (TLOs/ELOs), POI (blocks/hours), CAD (admin), TEO (performance measures), Curriculum Maintenance SOP (governance) | **FULL** |
| Ch 3-23 | Training Aids, Devices, and Simulators | MSS Training Hub (standalone HTML, Foundry-embeddable), Offline Packager (DDIL), cheatsheets, 254 PDFs | **FULL** |
| Ch 3-27 | Training Records | Readiness Tracker (DODID roster, completion history), Progress Tracker (milestones), completion certificates | **PARTIAL** |
| Ch 3-30 | After Action Reviews | AAR Aggregator (structured intake, recurring-issue detection), AAR Template, Lessons Learned Pipeline | **FULL** |
| Ch 5 | Institutional Training | Formal POI, certified instructors (T3-I), standardized materials, Enrollment SOP (5-phase process) | **FULL** |

> **NOTE:** Ch 3-27 (Training Records) is marked PARTIAL because the Readiness Tracker does not yet feed DTMS/ATRRS automatically. Manual upload serves as an interim measure. See Section 5 for gap details.

---

## 4. SAT ARTIFACT COVERAGE

The following SAT artifacts are maintained in `training_management/` and satisfy the regulatory references listed.

| Artifact | AR 350-1 / TR 350-70 Coverage |
|----------|-------------------------------|
| MTP (Mission Training Plan) | Ch 3-3, 3-12, 3-27 — TLOs, ELOs, task conditions and standards, Go/No-Go criteria, sustainment training requirements |
| POI (Program of Instruction) | Ch 5, 3-21 — Blocks of instruction, duration, prerequisites, evaluation standards, hard No-Go items |
| CAD (Course Administrative Data) | Ch 5 — Enrollment, attendance, academic policy, conduct, training records, No-Go remediation |
| TEO (Training and Evaluation Outline) | Ch 3-14 — Performance measures, critical items, scoring sheets, Go/No-Go steps |
| Faculty Development Plan | Ch 3-18 — 4 instructor tiers (Instructor, Senior, Master, Unit Data Trainer), certification process, sustainment, observation criteria |
| Enrollment SOP | Ch 5 — 5-phase enrollment process, prerequisite verification, access provisioning, training records minimum data standard |
| Curriculum Maintenance SOP | Ch 3-21, TR 350-70 — Platform monitoring cadence, trigger events, change classification, quarterly and semi-annual review cycles |

---

## 5. IDENTIFIED GAPS

### Gap 1: DTMS/ATRRS Integration

**AR 350-1 Reference:** Ch 3-27 (Training Records)

**Description:** The Readiness Tracker is the MSS system of record for training completion but does not yet export to DTMS or ATRRS automatically.

**Mitigation:** Manual upload to Army systems of record serves as an interim measure. Automated DTMS-compatible export format planned for FY27 Q3.

### Gap 2: METL Linkage

**AR 350-1 Reference:** Ch 3-1 (Mission Essential Task List)

**Description:** MSS course learning outcomes are not yet explicitly mapped to unit Mission Essential Task Lists. The WFF tracks (TM-40A through TM-40F) provide a natural mapping framework but the formal linkage has not been documented.

**Mitigation:** Pending G3 METL review. WFF track outcomes will be mapped to corresponding collective and individual tasks upon completion.

### Gap 3: Demographic Analysis

**AR 350-1 Reference:** Ch 6 (Equal Opportunity in Training)

**Description:** Training analytics do not currently include race, gender, or grade breakdowns for EO compliance reporting.

**Mitigation:** Privacy and legal review required before implementation. The underlying data fields exist in the Readiness Tracker roster — the gap is in analytics reporting, not data collection.

---

## 6. ANALYTICS APPLICATIONS SUPPORTING AR 350-1

The MSS ecosystem includes 15 interconnected Streamlit applications that programmatically enforce and support AR 350-1 requirements:

| Application | AR 350-1 Alignment | Function |
|-------------|---------------------|----------|
| Training Metrics | Ch 1 | Commander's executive dashboard; BLUF briefing format; aggregates all 14 app metrics |
| Readiness Tracker | Ch 3-27, Ch 5 | Single source of truth for trainee roster, completion history; programmatic prerequisite enforcement |
| Enrollment Manager | Ch 5 | Class enrollment, seat allocation, auto-waitlist, priority-based promotion |
| MTT Scheduler | Ch 3-5, Ch 3-12 | Mobile Training Team scheduling across 5 AOR venues; instructor availability; Gantt calendar |
| Exam Analytics | Ch 3-14 | Pre/post exam analysis, gain score calculations, pass/fail rates, cross-cohort comparison |
| AAR Aggregator | Ch 3-30 | Structured AAR intake, recurring-issue detection, WFF categorization |
| Lessons Learned Pipeline | Ch 3-14, Ch 3-30 | 5-stage lifecycle (NEW → VALIDATED → ACTIONABLE → IMPLEMENTED → ARCHIVED); tag taxonomy |
| Instructor Manager | Ch 3-18 | Instructor certifications, expiration alerts (30/60/90 day), workload tracking |
| Curriculum Tracker | Ch 3-21 | Document versioning, SHA-256 change detection, review cycle tracking, stale-document alerts |
| Progress Tracker | Ch 3-27 | Individual milestone tracking, stalled/overdue detection |
| XRef Validator | Ch 3-21 | Corpus validation: broken links, stale references, naming violations, prerequisite consistency |
| Data Quality Monitor | Ch 3-3 | Pipeline health: completeness, timeliness, freshness, volume, accuracy; RAG status |
| Glossary Search | Ch 3-23 | Full-text search across glossary, doctrine, and training definitions |
| Offline Packager | Ch 3-23 | Bundle training materials for DDIL/disconnected environments; prerequisite-aware dependency resolution |
| SharePoint Sync | Ch 3-23 | Tracks sync state between local corpus, Cloudflare Pages, and SharePoint |

---

## 7. REFERENCES

- AR 350-1, Army Training and Leader Development
- TR 350-70, Army's Institutional Training Quality Assurance System
- TP 350-70-14, Training and Education Development in Support of the Institutional Domain
- ADP 7-0, Training
- FM 7-0, Training
- USAREUR-AF Command Training Guidance (FY26–27)

---

## 8. DOCUMENT HISTORY

| Date | Change |
|------|--------|
| 19 MAR 2026 | Initial publication — 11 AR 350-1 areas mapped, 3 gaps identified |
