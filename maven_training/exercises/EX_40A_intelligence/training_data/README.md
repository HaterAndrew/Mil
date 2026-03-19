# EX_40A Intelligence — Training Data

## Overview

This directory contains synthetic training data for the EX_40A Intelligence practical exercise. All data supports the S2 BCT HQ scenario described in EXERCISE.md.

## Required Datasets

### 1. Threat Activity Events (`sigact_reports.csv`)

SIGACT/threat activity feed providing 30 synthetic events across the AOR for COP layer configuration (Task 1).

| Column | Type | Description |
|--------|------|-------------|
| date | DATE (YYYY-MM-DD) | Report date |
| unit | TEXT | Reporting unit |
| report_type | TEXT | SIGACT, SALUTE, SPOT, INTREP, TIPPER |
| priority | TEXT | FLASH, IMMEDIATE, PRIORITY, ROUTINE |
| grid_ref | TEXT | MGRS grid reference |
| classification | TEXT | UNCLASSIFIED or CUI |
| analyst | TEXT | Analyst identifier |
| processing_hours | FLOAT | Hours to process report |

**Row count:** ~90 rows (covering 90-day window). Minimum 30 events required for Task 1 AOR display.

### 2. NAI/TAI Overlay (`nai_tai_overlay.csv`)

Named Areas of Interest and Target Areas of Interest for collection management (Tasks 1, 4).

| Column | Type | Description |
|--------|------|-------------|
| nai_tai_id | TEXT | Unique identifier (NAI-01, TAI-01, etc.) |
| type | TEXT | NAI or TAI |
| name | TEXT | Descriptive name |
| grid_center | TEXT | MGRS center point |
| radius_km | FLOAT | Observation radius in km |
| assigned_asset | TEXT | Collection asset assigned (or UNASSIGNED) |
| pir_linkage | TEXT | PIR number this NAI/TAI supports |
| last_report_dtg | DATETIME | Last report DTG from this NAI/TAI |
| status | TEXT | ACTIVE, INACTIVE, GAP |

**Row count:** 8 rows (4 NAIs, 4 TAIs per exercise scenario).

### 3. Target List (`intel_target_list.csv`)

Active target list for the targeting data product (Task 3).

| Column | Type | Description |
|--------|------|-------------|
| target_id | TEXT | Target designator (e.g., HPT-001) |
| target_type | TEXT | ADA, ARMOR, IDF, C2 |
| confirmation_status | TEXT | CONFIRMED or SUSPECTED |
| reporting_source | TEXT | SIGINT or HUMINT |
| grid_ref | TEXT | MGRS grid reference |
| first_observed_dtg | DATETIME | First observation DTG |
| last_observed_dtg | DATETIME | Most recent observation DTG |
| data_as_of | DATETIME | Timestamp of source feed |
| remarks | TEXT | Analyst notes |

**Row count:** 10-15 rows. Mix of CONFIRMED/SUSPECTED and SIGINT/HUMINT sources required for Task 3 attribution.

### 4. PIR Test Data (`pir_test_values.csv`)

Test event records that should trigger the three PIRs configured in Task 2. Evaluator uses these to verify PIR alert configuration.

| Column | Type | Description |
|--------|------|-------------|
| test_event_id | TEXT | Test identifier |
| pir_number | INT | PIR this event should trigger (1, 2, or 3) |
| event_type | TEXT | Event type matching PIR trigger |
| grid_ref | TEXT | MGRS grid within PIR geographic boundary |
| expected_result | TEXT | FIRES or NO_FIRE |

**Row count:** 6 rows (2 per PIR — one should fire, one should not).

## Format

All files are CSV (UTF-8, comma-delimited, header row). Timestamps use ISO 8601 format.

## Data Currency

The synthetic data period is June-August 2025. All timestamps within this window are valid for exercise purposes. The SIGINT feed staleness inject (Task 5) is handled via ENVIRONMENT_SETUP.md procedures, not by modifying this data.

## Classification


All grid references, unit designators, and event data are fictitious.

---

Instructor: generate or provide this data before class. See ENVIRONMENT_SETUP.md for detailed provisioning instructions.
