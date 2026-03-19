# EX_40D Sustainment — Training Data

## Overview

This directory contains synthetic training data for the EX_40D Sustainment practical exercise. All data supports the S4 BCT HQ sustainment sync scenario described in EXERCISE.md.

## Required Datasets

### 1. Supply Status (`supply_status.csv`)

LOGSTAT-derived supply-on-hand data for Class I, III, V (and IX) by unit (Tasks 1, 4).

| Column | Type | Description |
|--------|------|-------------|
| date | DATE (YYYY-MM-DD) | Report date |
| unit | TEXT | Subordinate unit |
| supply_class | TEXT | CL_I, CL_III, CL_V, CL_IX |
| on_hand_days | FLOAT | Days of supply on hand |
| required_days | FLOAT | Required DOS (typically 7.0) |
| status | TEXT | GREEN, AMBER, RED |
| last_resupply | DATE | Date of last resupply |

**Row count:** ~180 rows across five units, four supply classes, and a 60-day reporting window.

### 2. Unit Readiness Feed (`unit_readiness.csv`)

Readiness percentage by subordinate unit for the readiness dashboard (Tasks 1, 2, 3).

| Column | Type | Description |
|--------|------|-------------|
| date | DATE | Report date |
| unit | TEXT | Subordinate unit |
| readiness_pct | FLOAT | Current readiness percentage |
| threshold_pct | FLOAT | Commander's threshold (75.0) |
| status | TEXT | ABOVE_THRESHOLD or BELOW_THRESHOLD |
| data_as_of | DATETIME | LOGSTAT feed timestamp |
| reporting_fsc | TEXT | FSC submitting the LOGSTAT |

**Row count:** 10 rows (sample). Full dataset: daily for 5 units across the exercise window.

### 3. Transportation Status (`transportation_status.csv`)

Transportation overlay data for logistics layer (Task 1).

| Column | Type | Description |
|--------|------|-------------|
| convoy_id | TEXT | Convoy identifier |
| origin | TEXT | Origin point |
| destination | TEXT | Destination point |
| route | TEXT | MSR/ASR designation |
| status | TEXT | EN_ROUTE, COMPLETE, DELAYED, CANCELLED |
| departure_dtg | DATETIME | Departure DTG |
| eta_dtg | DATETIME | Estimated arrival DTG |
| cargo_class | TEXT | Supply class being transported |
| data_as_of | DATETIME | Feed timestamp |

**Row count:** 8 rows (sample).

### 4. CCIR Test Data (`sustainment_ccir_test_values.csv`)

Test records for verifying the two sustainment CCIRs (Task 3).

| Column | Type | Description |
|--------|------|-------------|
| test_event_id | TEXT | Test identifier |
| ccir_number | INT | CCIR this event should trigger (1 or 2) |
| unit | TEXT | Subordinate unit |
| metric | TEXT | readiness_pct or dos_on_hand |
| value | FLOAT | Test value |
| expected_result | TEXT | FIRES or NO_FIRE |

**Row count:** 4 rows (2 per CCIR).

## Format

All files are CSV (UTF-8, comma-delimited, header row). Timestamps use ISO 8601 format.

## Data Currency

The synthetic data period is June-July 2025. The 1st Bn FSC LOGSTAT staleness inject (Task 5) is handled via ENVIRONMENT_SETUP.md procedures, not by modifying this data.

## Classification


All unit designators, supply figures, and readiness data are fictitious.

---

Instructor: generate or provide this data before class. See ENVIRONMENT_SETUP.md for detailed provisioning instructions.
