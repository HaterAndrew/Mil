<!-- MAVEN TRAINING CORPUS — CDA REFERENCE MATERIAL
     Source: odt_workspace/docs/architecture/cda/reference/lessons-learned.md
     Supports: all TM tracks, especially TM-40J (Program Manager), TM-40K (Knowledge Manager)
     Type: Reference
-->
---
sidebar_position: 2
title: "Lessons Learned"
description: How five tools in the same enclave multiplied work exponentially by failing to share doctrinal primitives
layer: architecture
category: reference
---

# LL-001: AVT25 Assessment Tools -- Exponential Work Multiplication

*ODT Lessons Learned Series -- LL-001*

Five tools in the same enclave, all implementing the same doctrinal concepts independently. Zero shared primitives. Work multiplying exponentially with every tool added.

| Field | Value |
|-------|-------|
| Series | LL-001 |
| Exercise | AVT25 |
| Severity | Critical |
| Category | Architecture -- Shared Primitives |
| Doctrine Ref | ADP 5-0 (The Operations Process) |

## Bottom Line Up Front

Five assessment tools in the **same enclave** each independently implemented the same three doctrinal primitives (Assessment, Finding, Recommendation), resulting in **15 separate implementations** of the same concepts. Analysts spend **3 hours per assessment** re-entering the same data across tools. Bug fixes take **30 hours** instead of 6. Cross-tool queries are impossible without manual Excel aggregation. **This is not a cross-domain problem. This is a failure to build shared primitives from doctrine.**

## 01 -- The Problem in Numbers

**5 tools in the SAME ENCLAVE**, all performing assessment per ADP 5-0:

1. Strategic Assessments App
2. IMO/LOO Tool
3. Product Tracker
4. Problem Intake Form
5. Lessons Learned System

Each tool independently implemented the same three doctrinal primitives:

- Assessment
- Finding
- Recommendation

**5 tools x 3 primitives = 15 separate implementations**

## 02 -- Time Cost Per Assessment

### Before DBO -- AVT25 Pattern

| Step | Task | Time |
|------|------|------|
| 1 | Conduct assessment | 60 min |
| 2 | Enter in Strategic Assessments App | 30 min |
| 3 | Re-enter in IMO/LOO Tool | 30 min |
| 4 | Re-enter in Product Tracker | 20 min |
| 5 | Re-enter in Problem Intake Form | 20 min |
| 6 | Re-enter in Lessons Learned | 20 min |
| **Total** | | **180 min (3 hrs)** |

Data quality degrades with each re-entry: typos introduced, different phrasing causes confusion, fields omitted due to fatigue, inconsistent severity assessments.

### After DBO -- Target

| Step | Task | Time |
|------|------|------|
| 1 | Conduct assessment | 60 min |
| 2 | Enter once using DBO primitives | 5 min |
| **Total** | | **65 min** |

**64% reduction -- 115 min saved per assessment.** Single entry, zero transcription errors. Consistent across all tools. All fields captured once.

## 03 -- The Scaling Problem

### What happens when we add a 6th tool?

**Before DBO -- Exponential O(n^2):**

- New tool implements Assessment, Finding, Recommendation
- Now 6 x 3 = **18 implementations**
- Analyst workflow: 6 tools x 30 min = **210 min (3.5 hrs)**
- Maintenance burden: fix bugs 6 times
- Each new tool adds burden to ALL existing tools. Each new primitive must be replicated n times. Cross-tool queries become UNION across n tables.

**After DBO -- Linear O(n):**

- New tool consumes existing Assessment primitives
- Still **3 implementations** (shared backend)
- Analyst workflow: still **65 min**
- Maintenance burden: fix once
- New tools are additive, not multiplicative. Primitives remain constant. Cross-tool queries are one SELECT.

### Scaling Projections

| Metric | Before (n=5) | Before (n=10) | After DBO | Savings |
|--------|-------------|---------------|-----------|---------|
| Primitive implementations | 15 | 30 | 3 | 80-90% |
| Time per assessment | 180 min | 330 min | 65 min | 64-80% |
| Time per bug fix | 30 hrs | 60 hrs | 6 hrs | 80-90% |
| Time per feature addition | 52 hrs | 102 hrs | 11 hrs | 79-89% |
| Cross-tool query | 2-4 hrs manual | 4-8 hrs manual | 30 sec | >99% |

**Pattern:** Savings increase as n increases. The DBO approach gets *better* with scale while the AVT25 pattern gets exponentially worse.

## 04 -- Query Capability

**Task:** "Show me all critical findings from the last 30 days."

### Before DBO (AVT25)

```
-- IMPOSSIBLE without manual aggregation
-- 1. Query Strategic Assessments App database
-- 2. Export to Excel
-- 3. Query IMO/LOO Tool database
-- 4. Export to Excel
-- 5. Query Product Tracker database
-- 6. Export to Excel
-- 7. Query Problem Intake database
-- 8. Export to Excel
-- 9. Query Lessons Learned database
-- 10. Export to Excel
-- 11. Manually combine 5 Excel files
-- 12. Deduplicate (same finding entered 5 times)
-- 13. Format for leadership brief
```

Time: 2-4 hours of manual work. Result: Inconsistent, error-prone.

### After DBO

```sql
SELECT
    a.title,
    af.finding_text,
    af.severity,
    tac.tool_id AS source_tool,
    a.assessed_by,
    a.assessment_date
FROM assessments a
JOIN assessment_findings af
    ON a.assessment_id = af.assessment_id
LEFT JOIN tool_assessment_contexts tac
    ON a.assessment_id = tac.assessment_id
WHERE af.severity = 'critical'
    AND a.assessment_date >= CURRENT_DATE - INTERVAL '30 days'
ORDER BY a.assessment_date DESC;
```

Time: 30 seconds. Result: Comprehensive, accurate, real-time.

## 05 -- Maintenance Cost

### Bug Fix: "Assessment date validation is wrong"

**Before DBO:**

| Step | Task | Time |
|------|------|------|
| 1 | Fix in Strategic Assessments App | 6 hrs |
| 2 | Fix in IMO/LOO Tool | 6 hrs |
| 3 | Fix in Product Tracker | 6 hrs |
| 4 | Fix in Problem Intake | 6 hrs |
| 5 | Fix in Lessons Learned | 6 hrs |
| **Total** | | **30 hours** |

**After DBO:**

| Step | Task | Time |
|------|------|------|
| 1 | Fix in Assessment primitive | 6 hrs |
| | All 5 tools inherit the fix automatically | |
| **Total** | | **6 hours** |

**80% reduction -- 24 hours saved.**

### Feature Addition: "Add confidence level to assessments"

**Before DBO:**

| Step | Task | Time |
|------|------|------|
| 1 | Update 5 schemas + UIs | 40 hrs |
| 2 | Migrate data in 5 databases | 12 hrs |
| **Total** | | **52 hours** |

**After DBO:**

| Step | Task | Time |
|------|------|------|
| 1 | Add to Assessment primitive + backend | 4 hrs |
| 2 | Migrate data once | 2 hrs |
| 3 | Update 5 tool UIs to display field | 5 hrs |
| **Total** | | **11 hours** |

**79% reduction -- 41 hours saved.**

## 06 -- The Math of Exponential Work

```
n = number of tools
p = number of primitives (Assessment, Finding, Recommendation)
t = time per entry
m = maintenance time per change

Before DBO (AVT25 Pattern):
  Implementations  = n x p      (grows with both dimensions)
  Entry time       = n x t      (analyst enters n times)
  Maintenance      = n x m      (fix in n places)
  Queries          = O(n)       (UNION across n tables)

After DBO:
  Implementations  = p          (constant, regardless of n)
  Entry time       = t          (analyst enters once)
  Maintenance      = m          (fix once)
  Queries          = O(1)       (single SELECT)
```

## 07 -- Leadership Statements

Propagating these tools without a shared backend does not scale linearly — it multiplies the work exponentially. Every new assessment tool added under the AVT25 pattern increases burden across all existing tools. This is mathematically unsustainable.

**Lesson:** Every new assessment tool adds burden to ALL existing tools. The work does not scale linearly — it scales exponentially.

The distinction between what end users request and what doctrine requires must be maintained. Doctrine is the authoritative starting point. Do not derive Assessment object definitions from individual tool team preferences.

**Lesson:** Do not ask each tool team "what Assessment object do you want?" (results in 5 different answers). Ask ADP 5-0 "what is Assessment?" (one answer). Build it once. All tools consume it.

## 08 -- The Solution -- DBO Convergence

### Phase 1 -- 30 Days: Build Assessment Primitives from ADP 5-0 (Foundation)

- Assessment (identity)
- AssessmentFinding (identity)
- AssessmentRecommendation (identity)
- ToolAssessmentContext (classification)

### Phase 2 -- 90 Days: Migrate Strategic App + IMO/LOO Tool (Proof of concept)

- Demonstrates shared backend working
- Proves 64% time savings
- Validates cross-tool queries

### Phase 3 -- 90 Days: Migrate Remaining 3 Tools (Full convergence)

- Product Tracker
- Problem Intake Form
- Lessons Learned System

### Result

| Dimension | Before | After |
|-----------|--------|-------|
| Backends | 5 tools -> 5 backends | 5 tools -> 1 backend |
| Analyst time | 180 min / assessment | 65 min / assessment |
| Scaling behavior | Exponential | Linear |
| Cross-tool queries | Manual Excel aggregation | Single SQL query |
| Sustainability | Unsustainable | Sustainable |

## Bottom Line

**AVT25 Assessment Tools are the smoking gun.**

Same enclave. Same doctrinal function. Zero shared foundation. Work multiplying exponentially.

This is not a cross-enclave problem (CDS). This is not a cross-workshop problem (doctrine drift). **This is a fundamental failure to build shared primitives from doctrine.**

If we cannot get assessment tools in the same enclave to share a backend, we have already lost.

**Doctrine is gospel. Start there.**

---

---

# LL-002: Data Literacy Baseline Required Before ODT Employment

*ODT Lessons Learned Series -- LL-002*

Deploying specialized ODTs to units without a data literacy baseline wastes ODT capacity and produces minimal operational value. Units must possess foundational skills before ODT integration.

| Field | Value |
|-------|-------|
| Series | LL-002 |
| Exercise | Mojave Falcon (Army Reserve, Jun 2025) |
| Severity | Significant |
| Category | Training -- Prerequisite Enforcement |
| Doctrine Ref | MCCoE Decision Optimization CONOPS; ADP 7-0 (Training) |

## Bottom Line Up Front

The Army Reserve's first ODT deployment at Exercise Mojave Falcon (Fort Hunter Liggett, June 2025) demonstrated that **ODTs are not a substitute for baseline training**. Staff who had not trained on data tools before the exercise refused to learn them during operations. Leaders who lacked data literacy could not articulate analytical requirements, resulting in ODT capacity wasted on ad-hoc requests rather than structured problem-solving.

## 01 -- The Problem

The OCAR Chief Data and Analytics Office deployed an ODT supporting the 79th TSC and 311th ESC. The team brought Palantir, Tableau, and Power BI capabilities. Key friction points:

- **Cultural resistance:** Some staff preferred "map boards and acetate overlays." One intelligence officer stated they were "just calling all routes red because we don't really see a pattern" — demonstrating a fundamental analytical gap no ODT can fix on the fly.
- **Training gaps:** Personnel had not trained on tools beforehand. One officer said: "This is great, but I don't have time to figure out a new tool while we're trying to execute."
- **Data governance confusion:** Personnel unclear on responsibilities for managing digital artifacts. Export from classified to unclassified required approvals nobody had pre-coordinated.
- **Simulation data quality:** Exercise data poorly mimicked real-world conditions — ammunition lacked TAMIS-level granularity; food and fuel information was oversimplified.

## 02 -- What Worked

Early adopters — future battalion and brigade commanders, CW5s, and SGMs — embraced the ODT, requested data analysis, and leaned into predictive capabilities. These leaders represent the formation's data-literate nucleus. The ODT found that elevating the quality of questions staff asked produced more value than delivering finished products.

## 03 -- Lesson

**ODTs should deploy to units that already possess a data literacy baseline.** Deploying a specialized analytics team to a unit with no digital muscle memory is not a great use of resources. This is an institutional culture challenge, not a technology limitation.

**Application to MSS Training:**
- TM-10 (Maven User) and TM-20 (Builder) establish the minimum baseline. Units must complete TM-10 theater-wide before ODT integration produces full value.
- The Unit Data Trainer (T3-F) model builds local capacity between MTT visits — exactly the mechanism needed to create the baseline that ODTs require.
- TM-30 is the hard prerequisite before specialist employment. Mojave Falcon validates this: personnel without TM-30-level skills cannot effectively consume or direct ODT products.

*Source: Perkins, Jim. "Lessons from the Army Reserve's First Operational Data Team." War on the Rocks, July 2025.*

---

# LL-003: Complementary Army Data Literacy Programs

*ODT Lessons Learned Series -- LL-003*

Multiple Army organizations are simultaneously developing data literacy training. Awareness of complementary programs prevents duplication and enables cross-referencing.

| Field | Value |
|-------|-------|
| Series | LL-003 |
| Severity | Informational |
| Category | Training -- Institutional Awareness |
| Doctrine Ref | ADP 7-0 (Training); TR 350-70 |

## Programs Identified

| Program | Proponent | Format | Audience | Relevance to MSS |
|---|---|---|---|---|
| **Signal School Data for Leaders Course** | U.S. Army Signal School (Fort Eisenhower) | 4-day MTT, Power BI focused | Senior military leaders | Establishes commander data literacy baseline. Complementary to TM-SL. Created by CPT Derek Koslowski, CDO at Signal School. First MTT delivered at Fort Cavazos, Nov 2024. Topics: data literacy, data governance, cloud fundamentals, storytelling with data, zero trust. |
| **AKMP Data Immersion Course** | MCCoE/C2ID (AKMP) | 32-hour online | KMs at DIV+ level | Covers data governance, Army Data Catalog, data workforce roles, GenAI, Vantage. Aligns with TM-40K. |
| **Data Literacy 101 (DL101-TTC)** | West Point CDAS | 5-day TTC, 10 hrs instruction | Train-the-Trainer | Foundational data literacy + teaching methodology. 140 attendees at Jun 2024 iteration. |
| **TRADOC OCKO Data Literacy Portal** | TRADOC C2DAO | Online courses | TRADOC workforce | Central hub for data literacy training. Decision Optimization Branch targeting FOC Dec 2025. |
| **CALL 25-10** | Center for Army Lessons Learned | Handbook (PDF) | Commanders and staff | Data literacy fundamentals tailored for military leaders. Published Apr 2025. |
| **CAC Maven Integration** | MCCoE/CGSC/CAC C2DAO | 8-hr operator course + PME integration | CGSC students, operators | Maven being integrated into KM Qual Course, SAMS, SCP, and Data Academy Builders Course. Train-the-trainer held Feb 2026. |

## Bottom Line

The MSS Training Program is ahead of the institutional curve — our curriculum is published, delivering, and evaluated to Go/No-Go standard while many of these programs are still in pilot. Awareness of these programs enables cross-referencing in supplementary reading sections and validates the MSS training design against institutional Army direction.

---

*Distribution: Authorized personnel -- USAREUR-AF and supporting commands*
*Proponent: Operational Data Team, USAREUR-AF*
*Authority: Chief Data and Analytics Officer, USAREUR-AF*
*Classification Guide: Per DoDI 5200.48 and DoDM 5200.01, Vol 2*
*CUI*
