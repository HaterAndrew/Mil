# EX-30 — Advanced Builder
## Practical Exercise — TM-30 Proficiency

**Version 1.0 | March 2026**
**Prerequisite:** TM-30, Advanced No-Code Builder Technical Manual (and TM-10, TM-20)
**Duration:** 2–3 hours
**Environment:** MSS training instance with Pipeline Builder and Contour/Quiver access (see ENVIRONMENT_SETUP.md)

---

## SCENARIO

G2 has a raw intelligence summary dataset (synthetic) covering 60 days of SIGACT-type events across a training AOR. You are tasked to build an analytical pipeline that cleans and enriches the data, produces a Contour geospatial view, and builds a Quiver pivot for pattern-of-life analysis. No code required — Pipeline Builder and no-code tools only.

**Training dataset:** Synthetic SIGACT-analog events with date, grid, event type, and unit fields.

---

## TASK LIST

### Task 1 — Data Profiling (20 min)
- [ ] Load the raw dataset into a Pipeline Builder branch
- [ ] Identify: null rate per column, duplicate records, date range coverage
- [ ] Produce a written data quality summary (3–5 bullet points) for your evaluator
- **Go:** Summary accurately reflects null rates and duplicates; date range is correct
- **No-Go:** Summary contains factual errors about the dataset

### Task 2 — Clean and Enrich (40 min)
- [ ] Deduplicate records on event ID
- [ ] Fill null unit fields with "UNKNOWN"
- [ ] Add a derived column: `week_number` from the date field
- [ ] Output to a clean dataset following naming standards
- **Go:** Output has no duplicates; no null unit fields; week_number column present and correct
- **No-Go:** Duplicates remain or derived column is wrong

### Task 3 — Contour Geospatial View (30 min)
- [ ] Connect the clean dataset to Contour
- [ ] Plot events as points using the grid coordinate field
- [ ] Color-code by event type
- [ ] Add a time filter for the past 30 days
- **Go:** Points render on map; color coding is correct; time filter functions
- **No-Go:** Map does not render or color coding is absent

### Task 4 — Quiver Pattern-of-Life (30 min)
- [ ] Create a Quiver pivot: rows = week_number, columns = event type, values = count
- [ ] Add a heat-map color scale
- [ ] Identify the week with the highest activity (annotate for evaluator)
- **Go:** Pivot is correct; heat map renders; high-activity week identified accurately
- **No-Go:** Pivot counts are incorrect or high-activity week is wrong

### Task 5 — AIP Logic Filter (no-code) (20 min)
- [ ] Build a simple AIP Logic rule in the UI (no code): flag any event with a null grid as "INCOMPLETE"
- [ ] Verify flagged records appear in a filtered view
- **Go:** Rule fires correctly on null grid records
- **No-Go:** Rule does not fire or fires on wrong records

---

## EVALUATOR NOTES

> **TODO:** Complete after dry run. Task 3 is highly environment-dependent — confirm Contour has correct grid projection for training data. Adjust timing based on cohort experience level.

Scoring: 5 tasks. Go on 4 of 5 = overall Go. No-Go on Task 2 = automatic No-Go.

---

## ENVIRONMENT SETUP

> **TODO:** Pre-load synthetic SIGACT-analog dataset. Confirm Contour access and correct grid projection. Document in `ENVIRONMENT_SETUP.md`.
