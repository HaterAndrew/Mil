# EX_40E Protection — Training Data

## Overview

This directory contains synthetic training data for the EX_40E Protection practical exercise. All data supports the Force Protection Officer BCT HQ scenario described in EXERCISE.md.

## Required Datasets

### 1. Force Protection Log (`force_protection.csv`)

Installation-level threat incident and access control data for threat layer configuration (Task 1).

| Column | Type | Description |
|--------|------|-------------|
| date | DATE (YYYY-MM-DD) | Report date |
| location | TEXT | Installation name |
| fpcon_level | TEXT | NORMAL, ALPHA, BRAVO, CHARLIE, DELTA |
| threat_type | TEXT | SAF, IDF, VBIED, CYBER, INSIDER |
| incidents_reported | INT | Number of incidents that day |
| access_control_checks | INT | Number of access control checks |
| anomalies_detected | INT | Anomalies flagged during checks |

**Row count:** ~60 rows across multiple installations and a 60-day window.

### 2. Threat Incident Feed (`threat_incidents.csv`)

Geo-located threat incidents by sector (NORTH, CENTRAL, SOUTH) for threat display and heat map (Tasks 1, 4, 5).

| Column | Type | Description |
|--------|------|-------------|
| incident_id | TEXT | Incident identifier |
| sector | TEXT | NORTH, CENTRAL, or SOUTH |
| incident_type | TEXT | IED, SAF, IDF, VBIED, COMPLEX |
| grid_ref | TEXT | MGRS grid reference |
| incident_dtg | DATETIME | Incident DTG |
| casualties_wia | INT | WIA count |
| casualties_kia | INT | KIA count |
| reporting_unit | TEXT | Unit that reported the incident |
| data_as_of | DATETIME | Feed timestamp |

**Row count:** 10 rows (sample). Full dataset: 30-50 incidents across all three sectors for the 30-day IED filter window.

### 3. PERSTAT Feed (`perstat_feed.csv`)

Personnel accountability by battalion for PERSTAT display (Task 3).

| Column | Type | Description |
|--------|------|-------------|
| report_date | DATE | PERSTAT report date |
| unit | TEXT | Organic battalion |
| assigned | INT | Total assigned personnel |
| present_for_duty | INT | Present for duty |
| pfd_pct | FLOAT | Present-for-duty percentage |
| last_submission_dtg | DATETIME | DTG PERSTAT was submitted |
| data_as_of | DATETIME | Feed timestamp |

**Row count:** 10 rows (sample). Full dataset: daily for all organic battalions.

### 4. Route and Installation Overlay (`route_installation_overlay.csv`)

MSR segments and installation perimeters for vulnerability assessment (Task 4).

| Column | Type | Description |
|--------|------|-------------|
| feature_id | TEXT | Feature identifier |
| feature_type | TEXT | MSR_SEGMENT, ASR_SEGMENT, INSTALLATION_PERIMETER |
| name | TEXT | Route or installation name |
| grid_start | TEXT | MGRS start/center point |
| grid_end | TEXT | MGRS end point (routes) or blank (perimeters) |
| radius_km | FLOAT | Perimeter radius (installations only) |

**Row count:** 8 rows.

### 5. CCIR Test Data (`protection_ccir_test_values.csv`)

Test records for verifying the two force protection CCIRs (Task 2).

| Column | Type | Description |
|--------|------|-------------|
| test_event_id | TEXT | Test identifier |
| ccir_number | INT | CCIR this event should trigger (1 or 2) |
| event_type | TEXT | THREAT_IN_RESTRICTED_AREA or CASUALTY_THRESHOLD |
| grid_ref | TEXT | MGRS grid (for CCIR 1 boundary check) |
| casualty_count | INT | Cumulative 72hr casualty count (for CCIR 2) |
| casualty_type | TEXT | WIA or KIA |
| expected_result | TEXT | FIRES or NO_FIRE |

**Row count:** 4 rows (2 per CCIR).

## Format

All files are CSV (UTF-8, comma-delimited, header row). Timestamps use ISO 8601 format.

## Data Currency

The synthetic data period is June-July 2025. The Sector SOUTH threat reporting staleness inject (Task 5) is handled via ENVIRONMENT_SETUP.md procedures, not by modifying this data.

## Classification


All grid references, installation names, incident data, and personnel figures are fictitious.

---

Instructor: generate or provide this data before class. See ENVIRONMENT_SETUP.md for detailed provisioning instructions.
