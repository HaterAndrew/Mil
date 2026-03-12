# EX-40J TRAINING — Open Tickets
## LOGSTAT Aggregation Pipeline
**Classification:** UNCLASSIFIED // TRAINING USE ONLY

## Ticket Summary

| Ticket | Title | Priority | Status |
|--------|-------|----------|--------|
| #EX40J-004 | BSB API returns inconsistent equipment class codes | Medium | In Progress |
| #EX40J-007 | FSB and CSSB APIs rate-limited — cannot complete integration | **HIGH — SCHEDULE BLOCKER** | Open — No resolution |
| #EX40J-011 | MSS dataset schema validation — null handling | Low | Open |
| #EX40J-015 | Dashboard date filter default shows last 7 days — G4 wants last 30 | Low | Open |

---

## Ticket #EX40J-004

**Title:** BSB API returns inconsistent equipment class codes
**Priority:** Medium | **Status:** In Progress | **Opened:** Week 3

**Description:** BSB API returns equipment class as free text (e.g., "Wheeled Veh", "wheeled vehicle", "WHEELED") — normalization transform handles ~90% of cases but edge cases remain.

**Action Required:** Add additional normalization rules; run against full 90-day backfill to validate.

---

## Ticket #EX40J-007 — CRITICAL BLOCKER

**Title:** FSB and CSSB APIs rate-limited — cannot complete integration
**Priority:** HIGH — SCHEDULE BLOCKER | **Status:** Open — No resolution | **Opened:** Week 4

**Description:** FSB and CSSB logistics APIs are rate-limited to 100 requests/hour. The pipeline as designed requires approximately 2,000 requests/hour to ingest all equipment records within the 2-hour latency window. Integration is halted. Week 4 milestone missed as a result.

**Downstream Impact:** Week 5 transform incomplete, Week 7 UAT delayed, Week 8 deadline at risk.

**Action Required:** Identify workaround or escalate to source system owners for rate limit increase.

> NOTE: A batched overnight run approach has not yet been evaluated.

---

## Ticket #EX40J-011

**Title:** MSS dataset schema validation — null handling
**Priority:** Low | **Status:** Open | **Opened:** Week 6

**Description:** When source record has null `equipment_available` field, the load step fails silently (writes null instead of defaulting to 0). Affects dashboard readiness % calculation for records with incomplete data.

**Action Required:** Add null coalesce in transform; rerun BSB backfill after fix.

---

## Ticket #EX40J-015

**Title:** Dashboard date filter default shows last 7 days — G4 wants last 30
**Priority:** Low | **Status:** Open | **Opened:** Week 6

**Description:** Minor UX issue. G4 POC prefers 30-day default view.

**Action Required:** Update Workshop dashboard default filter after UAT.
