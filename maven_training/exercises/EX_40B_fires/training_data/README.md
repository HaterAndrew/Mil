# EX_40B Fires — Training Data

## Overview

This directory contains synthetic training data for the EX_40B Fires practical exercise. All data supports the FSE BCT HQ scenario described in EXERCISE.md.

## Required Datasets

### 1. Target List (`target_list.csv`)

Active target list with 15+ entries for fires COP layer and targeting product (Tasks 1, 2).

| Column | Type | Description |
|--------|------|-------------|
| target_id | TEXT | Target designator (TGT-XXXX) |
| date | DATE | Date of last update |
| unit | TEXT | Reporting/owning unit |
| target_type | TEXT | POINT, AREA, LINEAR |
| status | TEXT | NOMINATED, APPROVED, VALIDATED, EXECUTED, BDA_PENDING |
| grid_ref | TEXT | MGRS grid reference |
| priority | INT | Target priority (1=highest) |
| effects_assessment | TEXT | EFFECTIVE, INEFFECTIVE, PENDING |

**Row count:** ~80 rows. Exercise requires a minimum of 15 active entries for Task 1 layer configuration.

### 2. FSCM Overlay (`fscm_overlay.csv`)

Fire support coordination measures for COP overlay (Task 1) and CCIR 3 boundary (Task 3).

| Column | Type | Description |
|--------|------|-------------|
| fscm_id | TEXT | Measure identifier (e.g., RFA-01, NFA-01) |
| fscm_type | TEXT | RFA, NFA, CFL, FSCL, ACA |
| name | TEXT | Named measure (e.g., RFA STEEL) |
| grid_vertices | TEXT | Semicolon-delimited MGRS vertices |
| effective_dtg | DATETIME | DTG measure takes effect |
| expiration_dtg | DATETIME | DTG measure expires |
| establishing_hq | TEXT | HQ that established the measure |
| data_as_of | DATETIME | Feed timestamp |

**Row count:** 8-10 rows covering the BCT AOR.

### 3. BDA Reporting Feed (`bda_reporting.csv`)

Battle damage assessment reports by fires element for the effects assessment display (Task 4) and staleness inject (Task 5).

| Column | Type | Description |
|--------|------|-------------|
| bda_id | TEXT | BDA report identifier |
| target_id | TEXT | Target engaged (FK to target_list) |
| fires_element | TEXT | Fires unit that engaged (e.g., A/3-1 FA, B/3-1 FA) |
| bda_status | TEXT | CONFIRMED, ESTIMATED, NO_BDA |
| assessment_dtg | DATETIME | DTG of BDA assessment |
| data_as_of | DATETIME | Feed timestamp |
| remarks | TEXT | Assessment notes |

**Row count:** 10-15 rows. At least two distinct fires elements required so one can be paused for the staleness inject.

### 4. CCIR Test Data (`fires_ccir_test_values.csv`)

Test records for verifying the three fires CCIRs configured in Task 3.

| Column | Type | Description |
|--------|------|-------------|
| test_event_id | TEXT | Test identifier |
| ccir_number | INT | CCIR this event should trigger (1, 2, or 3) |
| event_type | TEXT | STATUS_CHANGE, BDA_CONFIRMED, FSCM_VIOLATION |
| target_id | TEXT | Target reference |
| grid_ref | TEXT | MGRS grid (for CCIR 3 boundary check) |
| expected_result | TEXT | FIRES or NO_FIRE |

**Row count:** 6 rows (2 per CCIR — one should fire, one should not).

## Format

All files are CSV (UTF-8, comma-delimited, header row). Timestamps use ISO 8601 format.

## Data Currency

The synthetic data period is June-August 2025. The BDA feed staleness inject (Task 5) is handled via ENVIRONMENT_SETUP.md procedures, not by modifying this data directly.

## Classification


All target identifiers, grid references, and unit designators are fictitious.

---

Instructor: generate or provide this data before class. See ENVIRONMENT_SETUP.md for detailed provisioning instructions.
