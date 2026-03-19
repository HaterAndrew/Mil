# EX_40C Movement & Maneuver — Training Data

## Overview

This directory contains synthetic training data for the EX_40C Movement & Maneuver practical exercise. All data supports the S3 BCT HQ attack-order scenario described in EXERCISE.md.

## Required Datasets

### 1. Maneuver Tracking (`maneuver_tracking.csv`)

Daily unit position and status records for three maneuver battalions (Tasks 1, 5).

| Column | Type | Description |
|--------|------|-------------|
| date | DATE (YYYY-MM-DD) | Report date |
| unit | TEXT | Reporting unit |
| operation_type | TEXT | ATTACK, DEFEND, RETROGRADE, SCREEN, MOVEMENT_TO_CONTACT |
| vehicles_available | INT | Total vehicles on hand |
| vehicles_mission_capable | INT | Mission-capable vehicles |
| personnel_strength_pct | FLOAT | Personnel strength percentage |
| phase_line_reached | TEXT | Current PL (PL_ALPHA, PL_BRAVO, PL_CHARLIE) |
| supply_status | TEXT | GREEN, AMBER, RED |

**Row count:** ~60 rows. All five BCT subordinate units represented across a 60-day window.

### 2. Unit Position Feed (`unit_positions.csv`)

Simulated position reports for 1st, 2nd, and 3rd Maneuver Battalions with timestamps for COP display (Task 1) and CCIR verification (Task 3).

| Column | Type | Description |
|--------|------|-------------|
| position_id | TEXT | Position report identifier |
| unit | TEXT | 1-1 IN BN, 2-1 IN BN, or 3-1 FA BN |
| report_dtg | DATETIME | Position report DTG |
| grid_ref | TEXT | MGRS grid reference |
| heading_deg | INT | Movement heading (degrees) |
| speed_kph | FLOAT | Speed in km/h (0 = stationary) |
| data_as_of | DATETIME | Feed timestamp |

**Row count:** 10 rows (sample). Full dataset should contain hourly reports per battalion for the 24-hour exercise window.

### 3. Graphic Control Measures (`graphic_control_measures.csv`)

Phase lines and objectives for operational graphics (Task 2). Evaluator provides this as a handout.

| Column | Type | Description |
|--------|------|-------------|
| graphic_id | TEXT | Graphic identifier |
| graphic_type | TEXT | LD, PHASE_LINE, OBJECTIVE |
| label | TEXT | LD, PL AMBER, PL BLACK, OBJ IRON |
| grid_start | TEXT | MGRS start point |
| grid_end | TEXT | MGRS end point (lines) or center (objectives) |
| symbology | TEXT | FM 1-02.1 reference |

**Row count:** 4 rows (LD, PL AMBER, PL BLACK, OBJ IRON).

### 4. Task Organization Annex (`task_org_annex.csv`)

OPORD task organization for the task org display (Task 4).

| Column | Type | Description |
|--------|------|-------------|
| unit | TEXT | Subordinate unit |
| parent_hq | TEXT | Assigned/attached HQ |
| relationship | TEXT | ORGANIC, ATTACHED, OPCON, TACON |
| effective_dtg | DATETIME | DTG task org takes effect |
| remarks | TEXT | Notes (e.g., attached for movement) |

**Row count:** 8-10 rows covering all maneuver and support elements.

### 5. CCIR Test Data (`maneuver_ccir_test_values.csv`)

Test record for verifying CCIR — battalion crossing PL AMBER (Task 3).

| Column | Type | Description |
|--------|------|-------------|
| test_event_id | TEXT | Test identifier |
| unit | TEXT | Battalion |
| grid_ref | TEXT | MGRS position (north of PL AMBER) |
| expected_result | TEXT | FIRES or NO_FIRE |

**Row count:** 2 rows (one should fire, one should not).

## Format

All files are CSV (UTF-8, comma-delimited, header row). Timestamps use ISO 8601 format.

## Data Currency

The synthetic data period is June-July 2025. The 2nd Battalion position feed staleness inject (Task 5) is handled via ENVIRONMENT_SETUP.md procedures, not by modifying this data.

## Classification


All grid references, unit designators, and position data are fictitious.

---

Instructor: generate or provide this data before class. See ENVIRONMENT_SETUP.md for detailed provisioning instructions.
