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

*Distribution: Authorized personnel -- USAREUR-AF and supporting commands*
*Proponent: Operational Data Team, USAREUR-AF*
*Authority: Chief Data and Analytics Officer, USAREUR-AF*
*Classification Guide: Per DoDI 5200.48 and DoDM 5200.01, Vol 2*
*CUI // FOUO*
