#!/usr/bin/env python3
"""
build_atis_packet.py — Extract MSS training program data into ATIS-compatible format.

Produces two outputs:
  1. JSON structured data (maven_training/atis/atis_courses.json)
     - Machine-readable, suitable for ATIS import or future T2COM submission tooling
  2. TR 350-70 formatted markdown (maven_training/atis/ATIS_COURSE_PACKET.md)
     - Human-readable, suitable for G3/7 submission (USAREUR-AF) and later T2COM

Design: Structured for TR 350-70 compliance from day one so the same packet
works for USAREUR-AF G3/7 command training registration NOW and ports to
T2COM institutional registration LATER without rework.

References:
  - TR 350-70: Army Learning Policy and Systems
  - TP 350-70-14: Training Development in Institutional Domain
  - AR 350-1: Army Training and Leader Development

Run from repo root:
  python3 scripts/build_atis_packet.py
"""

import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
OUT_DIR = REPO_ROOT / "maven_training" / "atis"
TM_DIR = REPO_ROOT / "maven_training" / "tm"
SYLLABI_DIR = REPO_ROOT / "maven_training" / "syllabi"
LP_DIR = REPO_ROOT / "maven_training" / "training_management" / "lesson_plans"

# ── Program-level metadata ────────────────────────────────────────────────────

PROGRAM_META = {
    "program_title": "Maven Smart System (MSS) Training Program",
    "program_designation": "MSS-POI-001",
    "proponent": "USAREUR-AF C2DAO",
    "proponent_organization": "USAREUR-AF C2DAO Training Branch",
    "proponent_dsn": "[To be assigned]",
    "proponent_email": "usarmy.wiesbaden.usareur-af.list.c2dao-training@army.mil",
    "effective_date": "March 2026",
    "classification": "",
    "review_cycle": "Annual or upon major platform update",
    "authority": "C2DAO Data Governance Directive",
    "training_environment": "MSS Training Environment (dedicated Foundry instance, synthetic data)",
    "registration_phase": {
        "phase_1": "USAREUR-AF G3/7 command training registration",
        "phase_2": "T2COM institutional registration (future)",
    },
    "authoritative_references": [
        {"pub": "AR 350-1", "title": "Army Training and Leader Development",
         "relevance": "Master regulation for Army training policy"},
        {"pub": "AR 350-10", "title": "Management of Army Individual Training Requirements and Resources",
         "relevance": "Governs individual training seat management and enrollment"},
        {"pub": "TR 350-70", "title": "Army Learning Policy and Systems",
         "relevance": "TRADOC master regulation governing POI standards and course administration"},
        {"pub": "TP 350-70-14", "title": "Training Development in Institutional Domain",
         "relevance": "TRADOC pamphlet governing POI construction and instructional system development"},
        {"pub": "TP 350-70-7", "title": "Army Educational Processes",
         "relevance": "Curriculum development, assessment design, and evaluation methodology"},
        {"pub": "ADP 7-0", "title": "Training",
         "relevance": "Army training doctrine; principles for training management"},
        {"pub": "FM 7-0", "title": "Training",
         "relevance": "Unit training management procedures; GO/NO-GO evaluation guidance"},
    ],
}


# ── Course definitions ────────────────────────────────────────────────────────
# Master course registry — single source of truth for all 24 courses + FBC.
# Fields map directly to TR 350-70 / ATIS required data elements.

COURSES = [
    # ── Tier 1: Foundation ──
    {
        "course_id": "TM-10",
        "atis_number": "[TBD — assigned by ATIS upon registration]",
        "title": "Maven User",
        "tier": "Foundation",
        "tier_number": 1,
        "duration_days": 1,
        "duration_hours": 8,
        "prerequisites": [],
        "prerequisite_description": "None. All USAREUR-AF personnel eligible.",
        "audience": "All USAREUR-AF personnel",
        "audience_mos": "All MOS",
        "max_class_size": 20,
        "min_class_size": 4,
        "cadence": "Monthly or as-needed",
        "instructor_ratio": "10:1",
        "instructor_qualification": "TM-20 certified; 90 days active MSS use",
        "access_level": "Viewer (standard)",
        "provisioning_lead_days": 5,
        "evaluation_type": "Practical exercise (6 tasks, GO/NO-GO)",
        "evaluation_hours": 1.0,
        "hard_nogo": "Incorrect classification marking or export procedure",
        "remediation_hours": 2,
        "remediation_method": "Self-study with TM + supervised lab with instructor",
        "equipment": {
            "workstation": "Government workstation with CAC reader",
            "network": "MSS production environment",
            "facilities": "Classroom, projector",
            "special": "None",
        },
        "security_clearance": "None required",
        "hours_by_method": {
            "lecture_brief": 1.5,
            "lab": 5.5,
            "discussion_review": 0.0,
            "workshop_seminar": 0.0,
            "evaluation": 1.0,
        },
        "blocks": [
            {"block": 1, "title": "MSS Overview and Data Literacy Fundamentals", "hours": 1.0, "method": "LEC", "ref": "TM-10 Ch 1; Data Literacy Technical Reference Ch 1"},
            {"block": 2, "title": "Login and Navigation: CAC Authentication, Project Access", "hours": 1.0, "method": "LAB", "ref": "TM-10 Ch 2"},
            {"block": 3, "title": "Workshop Applications: Tables, Filters, Dashboards", "hours": 1.0, "method": "LAB", "ref": "TM-10 Ch 3"},
            {"block": 4, "title": "Actions: Executing Status Updates and Form Submissions", "hours": 1.0, "method": "LAB", "ref": "TM-10 Ch 4"},
            {"block": 5, "title": "Contour: Building a Basic Chart and Applying a Filter", "hours": 1.0, "method": "LAB", "ref": "TM-10 Ch 5"},
            {"block": 6, "title": "Quiver: Exploring Object Types, Filters, and Exporting Views", "hours": 1.0, "method": "LAB", "ref": "TM-10 Ch 6"},
            {"block": 7, "title": "AIP Interface: Submitting a Query; Understanding AI Output Limitations", "hours": 0.5, "method": "LAB", "ref": "TM-10 Ch 7"},
            {"block": 8, "title": "Classification Markings and Authorized Export Procedures", "hours": 0.5, "method": "LEC", "ref": "TM-10 Ch 8"},
            {"block": 9, "title": "Practical Exercise (Evaluated)", "hours": 1.0, "method": "EVAL", "ref": "TM-10 Practical Exercise Guide"},
        ],
        "teo_tasks": [
            "TM10-01: Log In and Navigate to Designated Application",
            "TM10-02: Filter Table to Identify Missing Submissions",
            "TM10-03: Execute an Authorized Action",
            "TM10-04: Export Filtered Table to CSV",
            "TM10-05: Build a Basic Contour Chart",
            "TM10-06: Explore Object Types in Quiver",
        ],
    },
    # ── Tier 2: Builder ──
    {
        "course_id": "TM-20",
        "atis_number": "[TBD — assigned by ATIS upon registration]",
        "title": "Builder",
        "tier": "Builder",
        "tier_number": 2,
        "duration_days": 5,
        "duration_hours": 40,
        "prerequisites": ["TM-10"],
        "prerequisite_description": "TM-10 Go on file",
        "audience": "All staff assigned to build or maintain MSS data products",
        "audience_mos": "All MOS with data product responsibilities",
        "max_class_size": 12,
        "min_class_size": 4,
        "cadence": "Quarterly",
        "instructor_ratio": "8:1",
        "instructor_qualification": "TM-30 certified; 6+ months Foundry build experience; able to troubleshoot all TM-20 labs",
        "access_level": "Builder",
        "provisioning_lead_days": 5,
        "evaluation_type": "Practical exercise (11 tasks, GO/NO-GO)",
        "evaluation_hours": 4.0,
        "hard_nogo": "Viewer-role test account can trigger Action or modify data",
        "remediation_hours": 4,
        "remediation_method": "Supervised lab on failed tasks; build from scratch on a different dataset",
        "equipment": {
            "workstation": "Government workstation with CAC reader",
            "network": "MSS production + training sandbox",
            "facilities": "Classroom, projector",
            "special": "None",
        },
        "security_clearance": "None required",
        "hours_by_method": {
            "lecture_brief": 0.0,
            "lab": 31.25,
            "discussion_review": 2.75,
            "workshop_seminar": 0.0,
            "evaluation": 4.0,
        },
        "blocks": [
            {"block": 1, "title": "Project Creation: Naming Conventions, Markings, Folder Structure", "hours": 1.5, "method": "LAB", "ref": "TM-20 Ch 2"},
            {"block": 2, "title": "File Ingestion: Upload CSV, Inspect Schema, Types, Row Count", "hours": 0.75, "method": "LAB", "ref": "TM-20 Ch 3 Sec 3-1"},
            {"block": 3, "title": "Dataset Explorer: Column Profiling, Null Detection, Type Mismatches", "hours": 1.0, "method": "LAB", "ref": "TM-20 Ch 3 Sec 3-2"},
            {"block": 4, "title": "Pipeline Builder Orientation: Canvas, Step Library, I/O Config", "hours": 2.0, "method": "LAB", "ref": "TM-20 Ch 3 Sec 3-3"},
            {"block": 5, "title": "C2DAO Naming Conventions: Datasets, Pipelines, Object Types", "hours": 0.5, "method": "DIS", "ref": "Standards Ch 1-2"},
            {"block": 6, "title": "Individual Practice: Second Project, Ingest Provided Dataset", "hours": 1.5, "method": "LAB", "ref": "TM-20 Ch 2-3"},
            {"block": 7, "title": "Pipeline: Filter Step, Rename Step, CAST for Type Correction", "hours": 2.0, "method": "LAB", "ref": "TM-20 Ch 3 Sec 3-4"},
            {"block": 8, "title": "Pipeline: Calculated Columns — String Functions, Conditional Logic, COALESCE", "hours": 1.25, "method": "LAB", "ref": "TM-20 Ch 3 Sec 3-5"},
            {"block": 9, "title": "Pipeline: Date and Time Functions — DATEDIFF, DATE_TRUNC, CURRENT_DATE", "hours": 2.0, "method": "LAB", "ref": "TM-20 Ch 3 Sec 3-6"},
            {"block": 10, "title": "End-to-End Pipeline Practice: Raw Input to Typed Filtered Output", "hours": 1.75, "method": "LAB", "ref": "TM-20 Ch 3"},
            {"block": 11, "title": "Pipeline: Join Step — Inner/Left Join, Key Selection, Deduplication", "hours": 2.0, "method": "LAB", "ref": "TM-20 Ch 3 Sec 3-7"},
            {"block": 12, "title": "Pipeline: Group-By Aggregation, Union Step, Output Mode Configuration", "hours": 1.25, "method": "LAB", "ref": "TM-20 Ch 3 Sec 3-8"},
            {"block": 13, "title": "Ontology Manager: Create Object Type — Properties, PK, Display Name", "hours": 2.0, "method": "LAB", "ref": "TM-20 Ch 4 Sec 4-1"},
            {"block": 14, "title": "Ontology Manager: Create Link Type — Cardinality, Directionality", "hours": 0.75, "method": "LAB", "ref": "TM-20 Ch 4 Sec 4-2"},
            {"block": 15, "title": "Pipeline: Ontology Write Step — Property Mapping, Run and Verify", "hours": 1.0, "method": "LAB", "ref": "TM-20 Ch 4 Sec 4-3"},
            {"block": 16, "title": "Actions: Create Basic Action — Parameter, Write Rule, Access Restriction", "hours": 1.5, "method": "LAB", "ref": "TM-20 Ch 4 Sec 4-4"},
            {"block": 17, "title": "Workshop Orientation: Canvas, Widget Library, Object Type Binding, Table Widget", "hours": 1.75, "method": "LAB", "ref": "TM-20 Ch 5 Sec 5-1"},
            {"block": 18, "title": "Workshop: Filter Widget, Metric Widget, Bar Chart Widget", "hours": 2.0, "method": "LAB", "ref": "TM-20 Ch 5 Sec 5-2"},
            {"block": 19, "title": "Workshop: Connecting Action Button — Trigger, Confirmation, Post-Action Refresh", "hours": 1.25, "method": "LAB", "ref": "TM-20 Ch 5 Sec 5-3"},
            {"block": 20, "title": "Access Control Model: Viewer vs. Editor Roles", "hours": 0.5, "method": "DIS", "ref": "TM-20 Ch 6 Sec 6-1"},
            {"block": 21, "title": "Workshop Publishing: Visibility, Viewer Access, Confirm Viewer Cannot Edit", "hours": 1.0, "method": "LAB", "ref": "TM-20 Ch 6 Sec 6-2"},
            {"block": 22, "title": "Branching: Create Branch, Make Change on Branch, Verify Branch-Only", "hours": 1.0, "method": "LAB", "ref": "TM-20 Ch 7 Sec 7-1"},
            {"block": 23, "title": "Promotion Workflow: Write Description, Submit to Steward, Respond to Rejection", "hours": 0.75, "method": "LAB", "ref": "TM-20 Ch 7 Sec 7-2"},
            {"block": 24, "title": "Full-Stack Review: Trace Product from Raw File to Access Control", "hours": 1.0, "method": "REV", "ref": "TM-20 All Chapters"},
            {"block": 25, "title": "Practical Exercise (Evaluated)", "hours": 4.0, "method": "EVAL", "ref": "TM-20 Practical Exercise Guide"},
        ],
        "teo_tasks": [
            "TM20-01: Create a Foundry Project with Correct Naming and Structure",
            "TM20-02: Ingest a File and Verify Data Quality",
            "TM20-03: Build a Clean/Transform Pipeline",
            "TM20-04: Build a Join Pipeline with Derived Columns",
            "TM20-05: Create an Object Type with Properties and PK",
            "TM20-06: Create a Link Type Between Object Types",
            "TM20-07: Configure a Pipeline Ontology Write Step",
            "TM20-08: Configure an Action with Parameter and Access Control",
            "TM20-09: Build a Workshop Application with Table, Filter, Metric, Chart",
            "TM20-10: Connect an Action Button to a Workshop Widget",
            "TM20-11: Manage Access Control (Viewer/Editor) and Verify Role Behavior",
        ],
    },
    # ── Tier 3: Advanced Builder ──
    {
        "course_id": "TM-30",
        "atis_number": "[TBD — assigned by ATIS upon registration]",
        "title": "Advanced Builder",
        "tier": "Advanced",
        "tier_number": 3,
        "duration_days": 5,
        "duration_hours": 40,
        "prerequisites": ["TM-10", "TM-20"],
        "prerequisite_description": "TM-10 and TM-20 Go on file",
        "audience": "Data-adjacent specialists, unit data leads",
        "audience_mos": "17-series, 25-series, S6/G6, G2, unit data leads",
        "max_class_size": 8,
        "min_class_size": 3,
        "cadence": "Quarterly",
        "instructor_ratio": "6:1",
        "instructor_qualification": "TM-40 (any track) or C2DAO SME designation; able to conduct design critiques",
        "access_level": "Editor + AIP Logic configuration",
        "provisioning_lead_days": 7,
        "evaluation_type": "Practical exercise (6 tasks, including reviewed design document; GO/NO-GO)",
        "evaluation_hours": 4.0,
        "hard_nogo": "Fatally-flawed Ontology design not corrected before build; promotion submitted without description",
        "remediation_hours": 8,
        "remediation_method": "Full-day supervised lab; rebuilding failed components",
        "equipment": {
            "workstation": "Government workstation with CAC reader",
            "network": "MSS production + training sandbox",
            "facilities": "Classroom, projector, whiteboard",
            "special": "None",
        },
        "security_clearance": "None required",
        "hours_by_method": {
            "lecture_brief": 1.0,
            "lab": 26.0,
            "discussion_review": 1.0,
            "workshop_seminar": 4.75,
            "evaluation": 4.0,
        },
        "blocks": [
            {"block": 1, "title": "Multi-Page Workshop: Navigation, Page Parameters, URL Deep Links", "hours": 2.0, "method": "LAB", "ref": "TM-30 Ch 2 Sec 2-1"},
            {"block": 2, "title": "Conditional Logic: Show/Hide Panels, Conditional Formatting, Dynamic Visibility", "hours": 1.25, "method": "LAB", "ref": "TM-30 Ch 2 Sec 2-2"},
            {"block": 3, "title": "Variable Passing: Object Selections Between Pages, Filtered Detail Views", "hours": 2.0, "method": "LAB", "ref": "TM-30 Ch 2 Sec 2-3"},
            {"block": 4, "title": "Design Exercise: 3-Page Operations Dashboard; Instructor Critique", "hours": 1.75, "method": "WKS", "ref": "TM-30 Ch 2"},
            {"block": 5, "title": "Multi-Source Joins: Inner/Left/Outer, Fan-Out Handling, Post-Join Deduplication", "hours": 2.0, "method": "LAB", "ref": "TM-30 Ch 3 Sec 3-1"},
            {"block": 6, "title": "Union Transforms: Compatible Schemas, Handling Mismatches", "hours": 1.25, "method": "LAB", "ref": "TM-30 Ch 3 Sec 3-2"},
            {"block": 7, "title": "Group-By Aggregations: Count/Sum/Min/Max, Aggregate-Then-Join Patterns", "hours": 2.0, "method": "LAB", "ref": "TM-30 Ch 3 Sec 3-3"},
            {"block": 8, "title": "Output Mode: Overwrite vs. Append; Append for Snapshot Pipelines", "hours": 1.25, "method": "LAB", "ref": "TM-30 Ch 3 Sec 3-4"},
            {"block": 9, "title": "Scheduled Pipeline: Schedule Expression, Build Failure Email Alert", "hours": 0.5, "method": "LAB", "ref": "TM-30 Ch 3 Sec 3-5"},
            {"block": 10, "title": "Ontology Design Methodology: Domain Analysis, Entity ID, Relationship Mapping, Action Design", "hours": 1.0, "method": "LEC", "ref": "TM-30 Ch 4 Sec 4-1"},
            {"block": 11, "title": "Individual Design Exercise: Mission Requirement to Documented Ontology Schema", "hours": 1.75, "method": "LAB", "ref": "TM-30 Ch 4 Sec 4-2"},
            {"block": 12, "title": "Design Critique: Peer Presentations, Class Review Against 6-Item Rubric", "hours": 2.0, "method": "WKS", "ref": "TM-30 Design Rubric"},
            {"block": 13, "title": "Build the Approved Design: Create Ontology, Connect Pipeline via Write Step", "hours": 2.25, "method": "LAB", "ref": "TM-30 Ch 4 Sec 4-3"},
            {"block": 14, "title": "Contour: Pivot Tables, Calculated Columns, Parameter Controls, Saved Views", "hours": 2.0, "method": "LAB", "ref": "TM-30 Ch 5"},
            {"block": 15, "title": "Quiver: Multi-Object Analysis, Linked Views, Cross-Filter Propagation, Drilling", "hours": 1.25, "method": "LAB", "ref": "TM-30 Ch 6"},
            {"block": 16, "title": "AIP Logic Configuration: Triggers, Inputs, Outputs; Human Review Queue Design", "hours": 1.5, "method": "LAB", "ref": "TM-30 Ch 7 Sec 7-1"},
            {"block": 17, "title": "Data Lineage: Reading Lineage Graphs, Identifying Sources and Consumers", "hours": 1.25, "method": "LAB", "ref": "TM-30 Ch 8"},
            {"block": 18, "title": "C2DAO Production Standards: Quality Gates for Production-Ready Data Products", "hours": 1.0, "method": "DIS", "ref": "Standards Ch 3"},
            {"block": 19, "title": "Full C2DAO Promotion Workflow: Branch, Change, Submit, Respond, Approval", "hours": 1.0, "method": "LAB", "ref": "TM-30 Ch 9"},
            {"block": 20, "title": "Full-Stack Review: Raw Source to Pipeline to Ontology to Workshop to Governance", "hours": 1.0, "method": "REV", "ref": "TM-30 All Chapters"},
            {"block": 21, "title": "Practical Exercise Scenario Brief and Design Planning Time", "hours": 1.25, "method": "BRF", "ref": "—"},
            {"block": 22, "title": "Practical Exercise (Evaluated)", "hours": 4.0, "method": "EVAL", "ref": "TM-30 Practical Exercise Guide"},
        ],
        "teo_tasks": [
            "TM30-01: Build a Multi-Page Workshop with Variable Passing",
            "TM30-02: Build an Advanced Pipeline (Multi-Source Join, Aggregation)",
            "TM30-03: Design and Document an Ontology Schema",
            "TM30-04: Build an Ontology from Approved Design",
            "TM30-05: Configure AIP Logic with Human Review Queue",
            "TM30-06: Execute Full Promotion Workflow",
        ],
    },
    # ── Tier 4a: WFF Functional Tracks ──
    {
        "course_id": "TM-40A",
        "atis_number": "[TBD — assigned by ATIS upon registration]",
        "title": "Intelligence Warfighting Function",
        "tier": "WFF Functional",
        "tier_number": 4,
        "duration_days": 3,
        "duration_hours": 24,
        "prerequisites": ["TM-10", "TM-20", "TM-30"],
        "prerequisite_description": "TM-10, TM-20, and TM-30 Go on file (all required)",
        "audience": "G2/S2 staff, targeting officers, all-source analysts",
        "audience_mos": "35-series, FA30",
        "max_class_size": 12,
        "min_class_size": 4,
        "cadence": "Quarterly or as-needed (high demand)",
        "instructor_ratio": "8:1",
        "instructor_qualification": "TM-40A certified; G2/S2 Intel functional background; TM-30 proficiency",
        "access_level": "Builder",
        "provisioning_lead_days": 5,
        "evaluation_type": "Practical exercise (GO/NO-GO)",
        "evaluation_hours": 3.0,
        "hard_nogo": "Intelligence product without data-as-of timestamp or source attribution",
        "remediation_hours": 4,
        "remediation_method": "Supervised lab on failed tasks; build from scratch on a different dataset",
        "equipment": {
            "workstation": "Government workstation with CAC reader",
            "network": "MSS production + WFF-specific datasets",
            "facilities": "Classroom, projector",
            "special": "None",
        },
        "security_clearance": "None required",
        "hours_by_method": {
            "lecture_brief": 1.0,
            "lab": 15.0,
            "discussion_review": 1.0,
            "workshop_seminar": 0.0,
            "evaluation": 3.0,
        },
        "doctrinal_references": ["FM 2-0", "ATP 2-01", "FM 3-60"],
        "blocks": [
            {"block": 1, "title": "Doctrinal Context: MSS in Intelligence Operations", "hours": 1.0, "method": "BRF", "ref": "TM-40A Ch 1; FM 2-0"},
            {"block": 2, "title": "Intelligence COP Configuration: Threat, NAI/TAI, IPB Products", "hours": 2.0, "method": "LAB", "ref": "TM-40A Ch 2"},
            {"block": 3, "title": "Data Currency Verification: Timestamps, Source Tracing, Stale Feed Escalation", "hours": 0.75, "method": "LAB", "ref": "TM-40A Ch 2"},
            {"block": 4, "title": "PIR Alert Configuration: Triggers, Geographic/Threshold Conditions, Routing", "hours": 2.0, "method": "LAB", "ref": "TM-40A Ch 3"},
            {"block": 5, "title": "PIR Scenario Exercise (Day 1)", "hours": 1.75, "method": "LAB", "ref": "TM-40A Ch 3"},
            {"block": 6, "title": "Collection Status Dashboard: NAI/TAI Coverage, Asset Task Status, Gap Analysis", "hours": 2.0, "method": "LAB", "ref": "TM-40A Ch 4"},
            {"block": 7, "title": "All-Source Intelligence Summary Product with Sourcing and Currency Caveats", "hours": 2.0, "method": "LAB", "ref": "TM-40A Ch 5"},
            {"block": 8, "title": "Targeting Support: Confirmed vs Unconfirmed Targets, BDA Status, TWG Product", "hours": 2.0, "method": "LAB", "ref": "TM-40A Ch 6"},
            {"block": 9, "title": "OPSEC for Intelligence Products: Marking, Distribution, Export, Need-to-Know", "hours": 1.0, "method": "DIS", "ref": "TM-40A Ch 7"},
            {"block": 10, "title": "Tabletop: Intelligence Data Failure Scenario and Response", "hours": 1.5, "method": "SEM", "ref": "TM-40A Ch 7"},
            {"block": 11, "title": "Practical Exercise (Evaluated)", "hours": 3.0, "method": "EVAL", "ref": "TM-40A Practical Exercise Guide"},
        ],
        "teo_tasks": [
            "TM40A-01: Configure Intelligence COP with Source Attribution",
            "TM40A-02: Configure PIR Alerts with Correct Triggers",
            "TM40A-03: Build Collection Status Dashboard",
            "TM40A-04: Produce All-Source Intelligence Summary",
            "TM40A-05: Build Targeting Support Product for TWG",
            "TM40A-06: Apply OPSEC Procedures to Intelligence Products",
        ],
    },
    {
        "course_id": "TM-40B",
        "atis_number": "[TBD — assigned by ATIS upon registration]",
        "title": "Fires Warfighting Function",
        "tier": "WFF Functional",
        "tier_number": 4,
        "duration_days": 3,
        "duration_hours": 24,
        "prerequisites": ["TM-10", "TM-20", "TM-30"],
        "prerequisite_description": "TM-10, TM-20, and TM-30 Go on file (all required)",
        "audience": "Fires/FSCOORD staff, fire support officers, targeting personnel",
        "audience_mos": "13-series, FA30",
        "max_class_size": 12,
        "min_class_size": 4,
        "cadence": "Quarterly or as-needed",
        "instructor_ratio": "8:1",
        "instructor_qualification": "TM-40B certified; Fires/FSCOORD functional background; TM-30 proficiency",
        "access_level": "Builder",
        "provisioning_lead_days": 5,
        "evaluation_type": "Practical exercise (GO/NO-GO)",
        "evaluation_hours": 3.0,
        "hard_nogo": "Fire support product without FSCM visualization or clearance-of-fires integration",
        "remediation_hours": 4,
        "remediation_method": "Supervised lab on failed tasks; build from scratch on a different dataset",
        "equipment": {
            "workstation": "Government workstation with CAC reader",
            "network": "MSS production + WFF-specific datasets",
            "facilities": "Classroom, projector",
            "special": "None",
        },
        "security_clearance": "None required",
        "hours_by_method": {"lecture_brief": 1.0, "lab": 15.0, "discussion_review": 1.0, "workshop_seminar": 0.0, "evaluation": 3.0},
        "doctrinal_references": ["FM 3-09", "ATP 3-09.42", "FM 3-60"],
        "blocks": [],  # Detailed blocks in WFF Lesson Plan Outlines
        "teo_tasks": [],
    },
    {
        "course_id": "TM-40C",
        "atis_number": "[TBD — assigned by ATIS upon registration]",
        "title": "Movement and Maneuver Warfighting Function",
        "tier": "WFF Functional",
        "tier_number": 4,
        "duration_days": 3,
        "duration_hours": 24,
        "prerequisites": ["TM-10", "TM-20", "TM-30"],
        "prerequisite_description": "TM-10, TM-20, and TM-30 Go on file (all required)",
        "audience": "G3/S3 movement and maneuver staff",
        "audience_mos": "Operations staff, maneuver planners",
        "max_class_size": 12,
        "min_class_size": 4,
        "cadence": "Quarterly or as-needed",
        "instructor_ratio": "8:1",
        "instructor_qualification": "TM-40C certified; G3/S3 movement and maneuver background; TM-30 proficiency",
        "access_level": "Builder",
        "provisioning_lead_days": 5,
        "evaluation_type": "Practical exercise (GO/NO-GO)",
        "evaluation_hours": 3.0,
        "hard_nogo": "Movement tracker without unit position currency or route status attribution",
        "remediation_hours": 4,
        "remediation_method": "Supervised lab on failed tasks; build from scratch on a different dataset",
        "equipment": {
            "workstation": "Government workstation with CAC reader",
            "network": "MSS production + WFF-specific datasets",
            "facilities": "Classroom, projector",
            "special": "None",
        },
        "security_clearance": "None required",
        "hours_by_method": {"lecture_brief": 1.0, "lab": 15.0, "discussion_review": 1.0, "workshop_seminar": 0.0, "evaluation": 3.0},
        "doctrinal_references": ["FM 3-90-1", "ATP 3-90.1", "ADP 3-90"],
        "blocks": [],
        "teo_tasks": [],
    },
    {
        "course_id": "TM-40D",
        "atis_number": "[TBD — assigned by ATIS upon registration]",
        "title": "Sustainment Warfighting Function",
        "tier": "WFF Functional",
        "tier_number": 4,
        "duration_days": 3,
        "duration_hours": 24,
        "prerequisites": ["TM-10", "TM-20", "TM-30"],
        "prerequisite_description": "TM-10, TM-20, and TM-30 Go on file (all required)",
        "audience": "G4/S4 sustainment staff",
        "audience_mos": "92-series, sustainment planners",
        "max_class_size": 12,
        "min_class_size": 4,
        "cadence": "Quarterly or as-needed",
        "instructor_ratio": "8:1",
        "instructor_qualification": "TM-40D certified; G4/S4 sustainment background; TM-30 proficiency",
        "access_level": "Builder",
        "provisioning_lead_days": 5,
        "evaluation_type": "Practical exercise (GO/NO-GO)",
        "evaluation_hours": 3.0,
        "hard_nogo": "Logistics dashboard without data-as-of timestamp or supply status attribution",
        "remediation_hours": 4,
        "remediation_method": "Supervised lab on failed tasks; build from scratch on a different dataset",
        "equipment": {
            "workstation": "Government workstation with CAC reader",
            "network": "MSS production + WFF-specific datasets",
            "facilities": "Classroom, projector",
            "special": "None",
        },
        "security_clearance": "None required",
        "hours_by_method": {"lecture_brief": 1.0, "lab": 15.0, "discussion_review": 1.0, "workshop_seminar": 0.0, "evaluation": 3.0},
        "doctrinal_references": ["FM 4-0", "ATP 4-93", "ATP 4-42"],
        "blocks": [],
        "teo_tasks": [],
    },
    {
        "course_id": "TM-40E",
        "atis_number": "[TBD — assigned by ATIS upon registration]",
        "title": "Protection Warfighting Function",
        "tier": "WFF Functional",
        "tier_number": 4,
        "duration_days": 3,
        "duration_hours": 24,
        "prerequisites": ["TM-10", "TM-20", "TM-30"],
        "prerequisite_description": "TM-10, TM-20, and TM-30 Go on file (all required)",
        "audience": "Protection staff",
        "audience_mos": "Protection cell, AT/FP, physical security",
        "max_class_size": 12,
        "min_class_size": 4,
        "cadence": "Quarterly or as-needed",
        "instructor_ratio": "8:1",
        "instructor_qualification": "TM-40E certified; Protection functional background; TM-30 proficiency",
        "access_level": "Builder",
        "provisioning_lead_days": 5,
        "evaluation_type": "Practical exercise (GO/NO-GO)",
        "evaluation_hours": 3.0,
        "hard_nogo": "Protection product without threat condition linkage or incident tracking attribution",
        "remediation_hours": 4,
        "remediation_method": "Supervised lab on failed tasks; build from scratch on a different dataset",
        "equipment": {
            "workstation": "Government workstation with CAC reader",
            "network": "MSS production + WFF-specific datasets",
            "facilities": "Classroom, projector",
            "special": "None",
        },
        "security_clearance": "None required",
        "hours_by_method": {"lecture_brief": 1.0, "lab": 15.0, "discussion_review": 1.0, "workshop_seminar": 0.0, "evaluation": 3.0},
        "doctrinal_references": ["ADP 3-37", "ATP 3-37.34", "ATP 3-37.2"],
        "blocks": [],
        "teo_tasks": [],
    },
    {
        "course_id": "TM-40F",
        "atis_number": "[TBD — assigned by ATIS upon registration]",
        "title": "Mission Command Warfighting Function",
        "tier": "WFF Functional",
        "tier_number": 4,
        "duration_days": 3,
        "duration_hours": 24,
        "prerequisites": ["TM-10", "TM-20", "TM-30"],
        "prerequisite_description": "TM-10, TM-20, and TM-30 Go on file (all required)",
        "audience": "MC/G6/S6 staff",
        "audience_mos": "25-series, signal officers, mission command planners",
        "max_class_size": 12,
        "min_class_size": 4,
        "cadence": "Quarterly or as-needed",
        "instructor_ratio": "8:1",
        "instructor_qualification": "TM-40F certified; Mission Command/G6 background; TM-30 proficiency",
        "access_level": "Builder",
        "provisioning_lead_days": 5,
        "evaluation_type": "Practical exercise (GO/NO-GO)",
        "evaluation_hours": 3.0,
        "hard_nogo": "COP configuration without network status integration or data feed health monitoring",
        "remediation_hours": 4,
        "remediation_method": "Supervised lab on failed tasks; build from scratch on a different dataset",
        "equipment": {
            "workstation": "Government workstation with CAC reader",
            "network": "MSS production + WFF-specific datasets",
            "facilities": "Classroom, projector",
            "special": "None",
        },
        "security_clearance": "None required",
        "hours_by_method": {"lecture_brief": 1.0, "lab": 15.0, "discussion_review": 1.0, "workshop_seminar": 0.0, "evaluation": 3.0},
        "doctrinal_references": ["ADP 6-0", "FM 6-0", "ATP 6-0.5"],
        "blocks": [],
        "teo_tasks": [],
    },
    # ── Tier 4b: Specialist Tracks ──
    {
        "course_id": "TM-40G",
        "atis_number": "[TBD — assigned by ATIS upon registration]",
        "title": "ORSA Specialist",
        "tier": "Specialist",
        "tier_number": 4,
        "duration_days": 5,
        "duration_hours": 40,
        "prerequisites": ["TM-10", "TM-20", "TM-30"],
        "prerequisite_description": "TM-10, TM-20, TM-30 Go on file (all required); quantitative background (statistics, linear algebra); Python or R proficiency",
        "audience": "ORSA analysts",
        "audience_mos": "FA49, operations research analysts",
        "max_class_size": 6,
        "min_class_size": 2,
        "cadence": "Semi-annual or on demand",
        "instructor_ratio": "4:1",
        "instructor_qualification": "FA49 or equivalent ORSA background; TM-40G certified or C2DAO SME designation",
        "access_level": "Code Workspace (CPU or GPU) + standard Editor",
        "provisioning_lead_days": 10,
        "evaluation_type": "Practical exercise (6 tasks); evaluated commander brief; GO/NO-GO",
        "evaluation_hours": 4.0,
        "hard_nogo": "Point estimate without confidence/credible interval; undocumented assumptions",
        "remediation_hours": 8,
        "remediation_method": "Full-day supervised lab; rebuilding failed components",
        "equipment": {
            "workstation": "Government workstation with CAC reader",
            "network": "MSS training sandbox + development environment",
            "facilities": "Lab with individual workstations",
            "special": "Code Workspace (CPU); IDE access",
        },
        "security_clearance": "None required",
        "hours_by_method": {
            "lecture_brief": 2.0,
            "lab": 30.0,
            "discussion_review": 1.0,
            "workshop_seminar": 0.0,
            "evaluation": 4.0,
        },
        "blocks": [
            {"block": 1, "title": "ORSA Role on MSS; Analytical Product Standards; Foundry Data Model", "hours": 1.0, "method": "BRF", "ref": "TM-40G Ch 1-2"},
            {"block": 2, "title": "Code Workspace Setup: Package Install, GPU/CPU Allocation, Reproducibility", "hours": 2.0, "method": "LAB", "ref": "TM-40G Ch 2 Sec 2-3"},
            {"block": 3, "title": "Foundry Dataset Connectivity: Reading via Spark/Pandas, Schema Inspection", "hours": 0.75, "method": "LAB", "ref": "TM-40G Ch 2 Sec 2-4"},
            {"block": 4, "title": "Writing Outputs to Foundry: Transaction Pattern for Results to Curated Datasets", "hours": 2.0, "method": "LAB", "ref": "TM-40G Ch 2 Sec 2-5"},
            {"block": 5, "title": "Data Profiling: Null Distributions, Outlier Detection, Feature Distributions", "hours": 1.75, "method": "LAB", "ref": "TM-40G Ch 3 Sec 3-1"},
            {"block": 6, "title": "Regression: Linear Regression for Readiness Forecasting, Validation Statistics", "hours": 2.0, "method": "LAB", "ref": "TM-40G Ch 3 Sec 3-2"},
            {"block": 7, "title": "Classification Models: Logistic Regression, Decision Trees, Cross-Validation", "hours": 1.25, "method": "LAB", "ref": "TM-40G Ch 3 Sec 3-3"},
            {"block": 8, "title": "Model Validation Standards: Residual Analysis, Documenting Assumptions", "hours": 2.0, "method": "LAB", "ref": "TM-40G Ch 3 Sec 3-4"},
            {"block": 9, "title": "Practice Build: Regression to Foundry Output to Quiver Visualization", "hours": 1.75, "method": "LAB", "ref": "TM-40G Ch 3"},
            {"block": 10, "title": "Time Series: Stationarity, ACF/PACF, ARIMA Model Identification", "hours": 2.0, "method": "LAB", "ref": "TM-40G Ch 4 Sec 4-1"},
            {"block": 11, "title": "ARIMA/SARIMA Build: Readiness Trend with 90% Confidence Bounds", "hours": 1.25, "method": "LAB", "ref": "TM-40G Ch 4 Sec 4-2"},
            {"block": 12, "title": "Monte Carlo: COA Comparison, Distribution Selection, 1000-Trial Simulation", "hours": 2.0, "method": "LAB", "ref": "TM-40G Ch 5"},
            {"block": 13, "title": "Sensitivity Analysis; Logistics Stockage Risk Modeling", "hours": 1.75, "method": "LAB", "ref": "TM-40G Ch 5 Sec 5-3"},
            {"block": 14, "title": "Linear Programming: Resource Allocation Formulation, scipy/lpSolve", "hours": 2.0, "method": "LAB", "ref": "TM-40G Ch 6"},
            {"block": 15, "title": "Scheduling Optimization: Maintenance vs. Operational Commitments", "hours": 1.25, "method": "LAB", "ref": "TM-40G Ch 6 Sec 6-3"},
            {"block": 16, "title": "Wargame/Exercise Data Architecture: Collection Templates, Analysis Pipeline", "hours": 2.0, "method": "LAB", "ref": "TM-40G Ch 7"},
            {"block": 17, "title": "Quiver/Contour for ORSA: Forecast Dashboard, COA Comparison, Uncertainty Bounds", "hours": 1.75, "method": "LAB", "ref": "TM-40G Ch 8"},
            {"block": 18, "title": "Communicating Uncertainty: Confidence Intervals, Briefing Posture, Translation", "hours": 1.0, "method": "LEC", "ref": "TM-40G Ch 9"},
            {"block": 19, "title": "Common ORSA Brief Failures: Point Estimates Without Bounds, Methods-Paper Language", "hours": 1.0, "method": "DIS", "ref": "TM-40G Ch 9"},
            {"block": 20, "title": "Practical Exercise Scenario Brief and ORSA Product Standards Review", "hours": 1.5, "method": "BRF", "ref": "—"},
            {"block": 21, "title": "Practical Exercise (Evaluated): Regression + Time Series + Commander Brief", "hours": 4.0, "method": "EVAL", "ref": "TM-40G Practical Exercise Guide"},
        ],
        "teo_tasks": [
            "TM40G-01: Configure Code Workspace and Verify Foundry Connectivity",
            "TM40G-02: Build Regression Model for Readiness Forecasting",
            "TM40G-03: Build Time Series Model with Confidence Bounds",
            "TM40G-04: Run Monte Carlo Simulation for COA Comparison",
            "TM40G-05: Build ORSA Forecast Dashboard",
            "TM40G-06: Deliver Commander Brief with Documented Uncertainty",
        ],
    },
    {
        "course_id": "TM-40H",
        "atis_number": "[TBD — assigned by ATIS upon registration]",
        "title": "AI Engineer",
        "tier": "Specialist",
        "tier_number": 4,
        "duration_days": 5,
        "duration_hours": 40,
        "prerequisites": ["TM-10", "TM-20", "TM-30"],
        "prerequisite_description": "TM-10, TM-20, TM-30 Go on file (all required); Python proficiency; Data Literacy Technical Reference read",
        "audience": "AI/ML specialists building AIP workflows",
        "audience_mos": "AI engineers, data scientists with AIP focus",
        "max_class_size": 6,
        "min_class_size": 2,
        "cadence": "Semi-annual or on demand",
        "instructor_ratio": "4:1",
        "instructor_qualification": "AIP Logic authoring experience; C2DAO AI SME designation; TM-40H certified",
        "access_level": "AIP Logic authoring + Agent Studio",
        "provisioning_lead_days": 10,
        "evaluation_type": "Practical exercise (7 tasks); AIP Authorization Checklist review; GO/NO-GO",
        "evaluation_hours": 4.0,
        "hard_nogo": "Any AIP workflow writes to production Objects without human checkpoint",
        "remediation_hours": 8,
        "remediation_method": "Full-day supervised lab; rebuilding failed components",
        "equipment": {
            "workstation": "Government workstation with CAC reader",
            "network": "MSS training sandbox + development environment",
            "facilities": "Lab with individual workstations",
            "special": "AIP Logic authoring access; Agent Studio access; IDE",
        },
        "security_clearance": "None required",
        "hours_by_method": {"lecture_brief": 3.75, "lab": 28.25, "discussion_review": 0.0, "workshop_seminar": 2.0, "evaluation": 4.0},
        "mandatory_attendance_note": "Day 1 Block 1 (AI Safety Seminar) is mandatory — no exceptions, no rescheduling",
        "blocks": [],  # Full blocks in POI Ch 3-5
        "teo_tasks": [],
    },
    {
        "course_id": "TM-40M",
        "atis_number": "[TBD — assigned by ATIS upon registration]",
        "title": "ML Engineer",
        "tier": "Specialist",
        "tier_number": 4,
        "duration_days": 5,
        "duration_hours": 40,
        "prerequisites": ["TM-10", "TM-20", "TM-30"],
        "prerequisite_description": "TM-10, TM-20, TM-30 Go on file (all required); Python proficiency (pandas, scikit-learn, PyTorch or equivalent)",
        "audience": "ML engineers building/deploying models on Foundry",
        "audience_mos": "MLEs, data scientists with model deployment focus",
        "max_class_size": 6,
        "min_class_size": 2,
        "cadence": "Semi-annual or on demand",
        "instructor_ratio": "4:1",
        "instructor_qualification": "ML production experience; TM-40M certified; C2DAO MLE SME designation",
        "access_level": "GPU-enabled Code Workspace",
        "provisioning_lead_days": 10,
        "evaluation_type": "Practical exercise (7 tasks); model card review; GO/NO-GO",
        "evaluation_hours": 4.0,
        "hard_nogo": "Model calibration not performed; governance document missing required sections",
        "remediation_hours": 8,
        "remediation_method": "Full-day supervised lab; rebuilding failed components",
        "equipment": {
            "workstation": "Government workstation with CAC reader",
            "network": "MSS training sandbox + development environment",
            "facilities": "Lab with individual workstations",
            "special": "GPU-enabled Code Workspace; IDE",
        },
        "security_clearance": "None required",
        "hours_by_method": {"lecture_brief": 1.0, "lab": 31.0, "discussion_review": 0.0, "workshop_seminar": 0.0, "evaluation": 4.0},
        "blocks": [],
        "teo_tasks": [],
    },
    {
        "course_id": "TM-40J",
        "atis_number": "[TBD — assigned by ATIS upon registration]",
        "title": "Program Manager",
        "tier": "Specialist",
        "tier_number": 4,
        "duration_days": 4,
        "duration_hours": 32,
        "prerequisites": ["TM-10", "TM-20", "TM-30"],
        "prerequisite_description": "TM-10, TM-20, TM-30 Go on file (all required)",
        "audience": "Program managers, G8/S8 resource managers",
        "audience_mos": "FA51, program/resource managers",
        "max_class_size": 8,
        "min_class_size": 3,
        "cadence": "Quarterly",
        "instructor_ratio": "6:1",
        "instructor_qualification": "Program management background; TM-30 certified; GFEBS/IMS proficiency",
        "access_level": "Builder",
        "provisioning_lead_days": 5,
        "evaluation_type": "Practical exercise (7 tasks); PM Dashboard Standards Checklist review; GO/NO-GO",
        "evaluation_hours": 4.0,
        "hard_nogo": "Dashboard has no data-as-of timestamp",
        "remediation_hours": 4,
        "remediation_method": "Supervised lab on failed tasks; build from scratch on a different dataset",
        "equipment": {
            "workstation": "Government workstation with CAC reader",
            "network": "MSS training sandbox + development environment",
            "facilities": "Lab with individual workstations",
            "special": "None",
        },
        "security_clearance": "None required",
        "hours_by_method": {"lecture_brief": 0.5, "lab": 17.75, "discussion_review": 0.5, "workshop_seminar": 0.0, "evaluation": 4.0},
        "blocks": [],
        "teo_tasks": [],
    },
    {
        "course_id": "TM-40K",
        "atis_number": "[TBD — assigned by ATIS upon registration]",
        "title": "Knowledge Manager",
        "tier": "Specialist",
        "tier_number": 4,
        "duration_days": 4,
        "duration_hours": 32,
        "prerequisites": ["TM-10", "TM-20", "TM-30"],
        "prerequisite_description": "TM-10, TM-20, TM-30 Go on file (all required)",
        "audience": "Knowledge managers, KMOs (37F)",
        "audience_mos": "37F, knowledge management officers",
        "max_class_size": 8,
        "min_class_size": 3,
        "cadence": "Quarterly",
        "instructor_ratio": "6:1",
        "instructor_qualification": "Knowledge management background; TM-30 certified; AIP Logic configuration proficiency",
        "access_level": "Builder + AIP Logic configuration",
        "provisioning_lead_days": 7,
        "evaluation_type": "Practical exercise (6 tasks); PCS package instructor review; GO/NO-GO",
        "evaluation_hours": 4.0,
        "hard_nogo": "AIP workflow auto-publishes without human review gate",
        "remediation_hours": 4,
        "remediation_method": "Supervised lab on failed tasks; build from scratch on a different dataset",
        "equipment": {
            "workstation": "Government workstation with CAC reader",
            "network": "MSS training sandbox + development environment",
            "facilities": "Lab with individual workstations",
            "special": "AIP Logic configuration access",
        },
        "security_clearance": "None required",
        "hours_by_method": {"lecture_brief": 1.0, "lab": 14.25, "discussion_review": 0.0, "workshop_seminar": 2.25, "evaluation": 4.0},
        "blocks": [],
        "teo_tasks": [],
    },
    {
        "course_id": "TM-40L",
        "atis_number": "[TBD — assigned by ATIS upon registration]",
        "title": "Software Engineer",
        "tier": "Specialist",
        "tier_number": 4,
        "duration_days": 5,
        "duration_hours": 40,
        "prerequisites": ["TM-10", "TM-20", "TM-30"],
        "prerequisite_description": "TM-10, TM-20, TM-30 Go on file (all required); TypeScript or Python proficiency; REST API familiarity",
        "audience": "Software engineers building Foundry integrations",
        "audience_mos": "SWEs, developers, 17-series with coding background",
        "max_class_size": 6,
        "min_class_size": 2,
        "cadence": "Semi-annual or on demand",
        "instructor_ratio": "4:1",
        "instructor_qualification": "Software engineering background; OSDK/Platform SDK proficiency; TM-40L certified",
        "access_level": "OSDK developer access + developer token",
        "provisioning_lead_days": 10,
        "evaluation_type": "Practical exercise (6 tasks); validator test suite (8 test cases); deployment checklist review; GO/NO-GO",
        "evaluation_hours": 4.0,
        "hard_nogo": "Hardcoded credential in application code; validator test suite not fully passing",
        "remediation_hours": 8,
        "remediation_method": "Full-day supervised lab; rebuilding failed components",
        "equipment": {
            "workstation": "Government workstation with CAC reader",
            "network": "MSS training sandbox + development environment",
            "facilities": "Lab with individual workstations",
            "special": "OSDK developer access; developer token; IDE",
        },
        "security_clearance": "None required",
        "hours_by_method": {"lecture_brief": 2.0, "lab": 30.0, "discussion_review": 0.0, "workshop_seminar": 0.0, "evaluation": 4.0},
        "blocks": [],
        "teo_tasks": [],
    },
    # ── Tier 5: Advanced Specialist ──
    {
        "course_id": "TM-50G",
        "atis_number": "[TBD — assigned by ATIS upon registration]",
        "title": "Advanced ORSA",
        "tier": "Advanced Specialist",
        "tier_number": 5,
        "duration_days": 5,
        "duration_hours": 40,
        "prerequisites": ["TM-10", "TM-20", "TM-30", "TM-40G"],
        "prerequisite_description": "TM-40G Go on file (required); active ORSA role at theater level",
        "audience": "Senior ORSA analysts",
        "audience_mos": "FA49, senior operations research analysts",
        "max_class_size": 6,
        "min_class_size": 2,
        "cadence": "Annual or on demand",
        "instructor_ratio": "4:1",
        "instructor_qualification": "FA49 O-4+ or equivalent; TM-50G certified or C2DAO Advanced ORSA SME; active analytical practice at theater level",
        "access_level": "Code Workspace (CPU/GPU) + Editor",
        "provisioning_lead_days": 10,
        "evaluation_type": "Practical exercise; peer-reviewed analytical product; GO/NO-GO",
        "evaluation_hours": 4.0,
        "hard_nogo": "Product without uncertainty quantification, documented assumptions, peer review, or reproducibility",
        "remediation_hours": 8,
        "remediation_method": "Full-day supervised lab; rebuilding failed components",
        "equipment": {
            "workstation": "Government workstation with CAC reader",
            "network": "MSS training sandbox + development environment",
            "facilities": "Lab with individual workstations",
            "special": "Code Workspace (CPU/GPU); IDE",
        },
        "security_clearance": "None required",
        "hours_by_method": {"lecture_brief": 2.0, "lab": 30.0, "discussion_review": 1.0, "workshop_seminar": 1.0, "evaluation": 4.0},
        "blocks": [],
        "teo_tasks": [],
    },
    {
        "course_id": "TM-50H",
        "atis_number": "[TBD — assigned by ATIS upon registration]",
        "title": "Advanced AI Engineer",
        "tier": "Advanced Specialist",
        "tier_number": 5,
        "duration_days": 5,
        "duration_hours": 40,
        "prerequisites": ["TM-10", "TM-20", "TM-30", "TM-40H"],
        "prerequisite_description": "TM-40H Go on file (required)",
        "audience": "Senior AI engineers",
        "audience_mos": "AI engineers with production AIP experience",
        "max_class_size": 6,
        "min_class_size": 2,
        "cadence": "Annual or on demand",
        "instructor_ratio": "4:1",
        "instructor_qualification": "TM-50H certified or C2DAO Advanced AI SME; production AIP/Agent Studio experience",
        "access_level": "AIP Logic authoring + Agent Studio + Code Workspace",
        "provisioning_lead_days": 10,
        "evaluation_type": "Practical exercise; GO/NO-GO",
        "evaluation_hours": 4.0,
        "hard_nogo": "Agent deployed without authorization controls or human oversight",
        "remediation_hours": 8,
        "remediation_method": "Full-day supervised lab; rebuilding failed components",
        "equipment": {
            "workstation": "Government workstation with CAC reader",
            "network": "MSS training sandbox + development environment",
            "facilities": "Lab with individual workstations",
            "special": "AIP authoring; Agent Studio; Code Workspace; IDE",
        },
        "security_clearance": "None required",
        "hours_by_method": {"lecture_brief": 2.0, "lab": 30.0, "discussion_review": 0.0, "workshop_seminar": 2.0, "evaluation": 4.0},
        "blocks": [],
        "teo_tasks": [],
    },
    {
        "course_id": "TM-50M",
        "atis_number": "[TBD — assigned by ATIS upon registration]",
        "title": "Advanced ML Engineer",
        "tier": "Advanced Specialist",
        "tier_number": 5,
        "duration_days": 5,
        "duration_hours": 40,
        "prerequisites": ["TM-10", "TM-20", "TM-30", "TM-40M"],
        "prerequisite_description": "TM-40M Go on file (required)",
        "audience": "Senior ML engineers",
        "audience_mos": "MLEs with production model deployment experience",
        "max_class_size": 6,
        "min_class_size": 2,
        "cadence": "Annual or on demand",
        "instructor_ratio": "4:1",
        "instructor_qualification": "TM-50M certified or C2DAO Advanced MLE SME; production ML pipeline experience",
        "access_level": "GPU-enabled Code Workspace + Editor",
        "provisioning_lead_days": 10,
        "evaluation_type": "Practical exercise; model governance review; GO/NO-GO",
        "evaluation_hours": 4.0,
        "hard_nogo": "Model deployed without drift monitoring or governance documentation",
        "remediation_hours": 8,
        "remediation_method": "Full-day supervised lab; rebuilding failed components",
        "equipment": {
            "workstation": "Government workstation with CAC reader",
            "network": "MSS training sandbox + development environment",
            "facilities": "Lab with individual workstations",
            "special": "GPU-enabled Code Workspace; IDE",
        },
        "security_clearance": "None required",
        "hours_by_method": {"lecture_brief": 1.0, "lab": 31.0, "discussion_review": 0.0, "workshop_seminar": 0.0, "evaluation": 4.0},
        "blocks": [],
        "teo_tasks": [],
    },
    {
        "course_id": "TM-50J",
        "atis_number": "[TBD — assigned by ATIS upon registration]",
        "title": "Advanced Program Manager",
        "tier": "Advanced Specialist",
        "tier_number": 5,
        "duration_days": 3,
        "duration_hours": 24,
        "prerequisites": ["TM-10", "TM-20", "TM-30", "TM-40J"],
        "prerequisite_description": "TM-40J Go on file (required)",
        "audience": "Senior program managers",
        "audience_mos": "FA51, senior resource/program managers",
        "max_class_size": 8,
        "min_class_size": 3,
        "cadence": "Annual or on demand",
        "instructor_ratio": "6:1",
        "instructor_qualification": "TM-50J certified or C2DAO Advanced PM SME; enterprise portfolio management experience",
        "access_level": "Builder + Editor",
        "provisioning_lead_days": 7,
        "evaluation_type": "Practical exercise; GO/NO-GO",
        "evaluation_hours": 4.0,
        "hard_nogo": "Portfolio dashboard without cross-program roll-up or data currency indicator",
        "remediation_hours": 4,
        "remediation_method": "Supervised lab on failed tasks",
        "equipment": {
            "workstation": "Government workstation with CAC reader",
            "network": "MSS training sandbox + development environment",
            "facilities": "Lab with individual workstations",
            "special": "None",
        },
        "security_clearance": "None required",
        "hours_by_method": {"lecture_brief": 1.0, "lab": 15.0, "discussion_review": 1.0, "workshop_seminar": 0.0, "evaluation": 4.0},
        "blocks": [],
        "teo_tasks": [],
    },
    {
        "course_id": "TM-50K",
        "atis_number": "[TBD — assigned by ATIS upon registration]",
        "title": "Advanced Knowledge Manager",
        "tier": "Advanced Specialist",
        "tier_number": 5,
        "duration_days": 3,
        "duration_hours": 24,
        "prerequisites": ["TM-10", "TM-20", "TM-30", "TM-40K"],
        "prerequisite_description": "TM-40K Go on file (required)",
        "audience": "Senior knowledge managers",
        "audience_mos": "37F, senior KMOs",
        "max_class_size": 8,
        "min_class_size": 3,
        "cadence": "Annual or on demand",
        "instructor_ratio": "6:1",
        "instructor_qualification": "TM-50K certified or C2DAO Advanced KM SME; enterprise KM architecture experience",
        "access_level": "Builder + AIP Logic configuration + Editor",
        "provisioning_lead_days": 7,
        "evaluation_type": "Practical exercise; GO/NO-GO",
        "evaluation_hours": 4.0,
        "hard_nogo": "Knowledge architecture without lifecycle governance or audit trail",
        "remediation_hours": 4,
        "remediation_method": "Supervised lab on failed tasks",
        "equipment": {
            "workstation": "Government workstation with CAC reader",
            "network": "MSS training sandbox + development environment",
            "facilities": "Lab with individual workstations",
            "special": "AIP Logic configuration access",
        },
        "security_clearance": "None required",
        "hours_by_method": {"lecture_brief": 1.0, "lab": 15.0, "discussion_review": 0.0, "workshop_seminar": 2.0, "evaluation": 4.0},
        "blocks": [],
        "teo_tasks": [],
    },
    {
        "course_id": "TM-50L",
        "atis_number": "[TBD — assigned by ATIS upon registration]",
        "title": "Advanced Software Engineer",
        "tier": "Advanced Specialist",
        "tier_number": 5,
        "duration_days": 5,
        "duration_hours": 40,
        "prerequisites": ["TM-10", "TM-20", "TM-30", "TM-40L"],
        "prerequisite_description": "TM-40L Go on file (required)",
        "audience": "Senior software engineers",
        "audience_mos": "SWEs, senior developers, 17-series with advanced coding",
        "max_class_size": 6,
        "min_class_size": 2,
        "cadence": "Annual or on demand",
        "instructor_ratio": "4:1",
        "instructor_qualification": "TM-50L certified or C2DAO Advanced SWE SME; production Foundry integration experience",
        "access_level": "OSDK developer + Platform SDK + Code Workspace",
        "provisioning_lead_days": 10,
        "evaluation_type": "Practical exercise; CI/CD pipeline review; GO/NO-GO",
        "evaluation_hours": 4.0,
        "hard_nogo": "Hardcoded credential; no automated test coverage; deployment without review",
        "remediation_hours": 8,
        "remediation_method": "Full-day supervised lab; rebuilding failed components",
        "equipment": {
            "workstation": "Government workstation with CAC reader",
            "network": "MSS training sandbox + development environment",
            "facilities": "Lab with individual workstations",
            "special": "OSDK developer access; Platform SDK; Code Workspace; IDE",
        },
        "security_clearance": "None required",
        "hours_by_method": {"lecture_brief": 2.0, "lab": 30.0, "discussion_review": 0.0, "workshop_seminar": 0.0, "evaluation": 4.0},
        "blocks": [],
        "teo_tasks": [],
    },
]

# ── Instructional method code lookup (TR 350-70) ─────────────────────────────

METHOD_CODES = {
    "LEC": "Lecture",
    "LAB": "Laboratory (hands-on)",
    "DIS": "Discussion",
    "SEM": "Seminar",
    "BRF": "Brief",
    "REV": "Review",
    "EVAL": "Evaluation (practical exercise, graded)",
    "WKS": "Workshop (design workshop, peer review)",
    "SPRINT": "Foundry Bootcamp (self-directed applied build)",
}


# ── Output: JSON ──────────────────────────────────────────────────────────────

def build_json(out_path: Path):
    """Write the full ATIS-compatible course data to JSON."""
    packet = {
        "_meta": {
            "generated": datetime.now(timezone.utc).isoformat() + "Z",
            "generator": "build_atis_packet.py",
            "format": "TR 350-70 ATIS Course Registration Packet",
            "phase_1_target": "USAREUR-AF G3/7 command training registration",
            "phase_2_target": "T2COM institutional registration",
            "total_courses": len(COURSES),
            "total_program_hours": sum(c["duration_hours"] for c in COURSES),
        },
        "program": PROGRAM_META,
        "method_codes": METHOD_CODES,
        "courses": COURSES,
        "prerequisite_chain": {
            "description": "TM-10 → TM-20 → TM-30 → ALL TM-40 (A-M) → TM-50 (G-M only)",
            "tree": {
                "TM-10": {
                    "TM-20": {
                        "TM-30": {
                            "TM-40A": {}, "TM-40B": {}, "TM-40C": {},
                            "TM-40D": {}, "TM-40E": {}, "TM-40F": {},
                            "TM-40G": {"TM-50G": {}},
                            "TM-40H": {"TM-50H": {}},
                            "TM-40M": {"TM-50M": {}},
                            "TM-40J": {"TM-50J": {}},
                            "TM-40K": {"TM-50K": {}},
                            "TM-40L": {"TM-50L": {}},
                        }
                    }
                }
            },
        },
    }
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w") as f:
        json.dump(packet, f, indent=2, ensure_ascii=False)
    print(f"  JSON → {out_path}")


# ── Output: TR 350-70 Formatted Markdown ──────────────────────────────────────

def _hours_table(c: dict) -> str:
    """Render the academic hours breakdown table for a course."""
    h = c["hours_by_method"]
    total = sum(h.values())
    # Remainder hours = scheduled hours minus method-attributed hours
    remainder = c["duration_hours"] - total
    lines = [
        "| Method | Hours |",
        "|---|---|",
        f"| Lecture / Brief | {h['lecture_brief']:.1f} |",
        f"| Laboratory (hands-on) | {h['lab']:.1f} |",
        f"| Discussion / Review | {h['discussion_review']:.1f} |",
        f"| Workshop / Seminar | {h['workshop_seminar']:.1f} |",
        f"| Evaluation | {h['evaluation']:.1f} |",
    ]
    if remainder > 0.1:
        lines.append(f"| Review / Scenario Brief (unattributed) | {remainder:.1f} |")
    lines.append(f"| **Total** | **{c['duration_hours']:.1f}** |")
    return "\n".join(lines)


def _blocks_table(c: dict) -> str:
    """Render the blocks of instruction table."""
    if not c["blocks"]:
        return "> *Detailed block-of-instruction tables are maintained in the applicable Lesson Plan Outlines and Syllabus. See WFF Lesson Plan Outlines (TM-40A–F) or TM-50 Advanced Lesson Plan Outlines.*\n"
    lines = [
        "| Block | Title | Hours | Method | Reference |",
        "|---|---|---|---|---|",
    ]
    for b in c["blocks"]:
        lines.append(f"| {b['block']} | {b['title']} | {b['hours']:.2g} | {b['method']} | {b['ref']} |")
    return "\n".join(lines)


def _teo_list(c: dict) -> str:
    """Render the T&EO task crosswalk."""
    if not c["teo_tasks"]:
        return "> *T&EO task crosswalk maintained in TEO_MSS.md. See applicable course section.*\n"
    lines = []
    for t in c["teo_tasks"]:
        lines.append(f"- {t}")
    return "\n".join(lines)


def build_markdown(out_path: Path):
    """Write the TR 350-70 formatted ATIS course packet."""
    sections = []

    # ── Header ──
    sections.append(f"""# ATIS COURSE REGISTRATION PACKET
## Maven Smart System (MSS) Training Program
### USAREUR-AF Operational Data Team — C2DAO

| | |
|---|---|
| **Program Designation** | {PROGRAM_META['program_designation']} |
| **Proponent** | {PROGRAM_META['proponent']} |
| **Proponent Organization** | {PROGRAM_META['proponent_organization']} |
| **Proponent DSN** | {PROGRAM_META['proponent_dsn']} |
| **Proponent Email** | {PROGRAM_META['proponent_email']} |
| **Effective Date** | {PROGRAM_META['effective_date']} |
| **Classification** | {PROGRAM_META['classification']} |
| **Review Cycle** | {PROGRAM_META['review_cycle']} |
| **Total Courses** | {len(COURSES)} |
| **Total Program Hours** | {sum(c['duration_hours'] for c in COURSES)} |
| **Format** | TR 350-70 compliant; structured for ATIS registration |
| **Phase 1** | USAREUR-AF G3/7 command training registration |
| **Phase 2** | T2COM institutional registration (future) |

---

## REGISTRATION STATUS

> **ATIS Course Numbers:** To be assigned upon registration. Internal designators (TM-10 through TM-50L) are used throughout this packet. Upon ATIS registration, each course will receive a formal ATIS course number which will be annotated in the ATIS Number field of each course record.

> **T2COM Note:** This packet is structured to TR 350-70 specification. When transitioning to T2COM institutional registration, the following additional elements will be required:
> - Formal TRADOC school partnership (proponent alignment)
> - ASI/SQI/Skill Identifier request (DA-level action via DAPE-MPE) if applicable
> - ATRRS registration for Army-wide course catalog visibility
> - Ammunition and training aid requirements (N/A for this program but fields required)

---

## AUTHORITATIVE REFERENCES

| Publication | Title | Relevance |
|---|---|---|""")

    for ref in PROGRAM_META["authoritative_references"]:
        sections.append(f"| {ref['pub']} | {ref['title']} | {ref['relevance']} |")

    sections.append("""
---

## PREREQUISITE CHAIN

```
TM-10 (all personnel)
  +-- TM-20 (builders)
        +-- TM-30 (advanced builders / data-adjacent / WFF functional staff)
              |-- TM-40A (Intelligence WFF)
              |-- TM-40B (Fires WFF)
              |-- TM-40C (Movement & Maneuver WFF)
              |-- TM-40D (Sustainment WFF)
              |-- TM-40E (Protection WFF)
              |-- TM-40F (Mission Command WFF)
              |-- TM-40G (ORSA) ----------> TM-50G (Advanced ORSA)
              |-- TM-40H (AI Engineer) ---> TM-50H (Advanced AI Engineer)
              |-- TM-40M (ML Engineer) ---> TM-50M (Advanced ML Engineer)
              |-- TM-40J (Program Mgr) ---> TM-50J (Advanced PM)
              |-- TM-40K (Knowledge Mgr) -> TM-50K (Advanced KM)
              +-- TM-40L (Software Eng) --> TM-50L (Advanced SWE)
```

> **NOTE:** TM-30 is a HARD prerequisite for ALL TM-40 tracks (WFF A-F and specialist G-M). There are NO TM-50A-F tracks.

---

## PROGRAM HOURS SUMMARY

| Course | Title | Tier | Days | Hours | Prereq | ATIS # |
|---|---|---|---|---|---|---|""")

    for c in COURSES:
        prereq_str = ", ".join(c["prerequisites"]) if c["prerequisites"] else "None"
        sections.append(f"| {c['course_id']} | {c['title']} | {c['tier']} | {c['duration_days']} | {c['duration_hours']} | {prereq_str} | {c['atis_number']} |")

    sections.append("""
---

## COURSE RECORDS

Each course record below contains all TR 350-70 required data elements for ATIS registration.

---
""")

    # ── Individual course records ──
    for c in COURSES:
        prereq_str = ", ".join(c["prerequisites"]) if c["prerequisites"] else "None"
        mandatory_note = ""
        if c.get("mandatory_attendance_note"):
            mandatory_note = f"\n> **MANDATORY ATTENDANCE:** {c['mandatory_attendance_note']}\n"

        doctrinal_refs = ""
        if c.get("doctrinal_references"):
            doctrinal_refs = f"\n| **Doctrinal References** | {', '.join(c['doctrinal_references'])} |"

        sections.append(f"""### {c['course_id']}: {c['title']}

| Field | Value |
|---|---|
| **ATIS Course Number** | {c['atis_number']} |
| **Internal Designator** | {c['course_id']} |
| **Course Title** | {c['title']} |
| **Tier** | {c['tier']} (Tier {c['tier_number']}) |
| **Duration** | {c['duration_days']} days ({c['duration_hours']} hours) |
| **Prerequisites** | {c['prerequisite_description']} |
| **Prerequisite Codes** | {prereq_str} |
| **Audience** | {c['audience']} |
| **Target MOS/Branch** | {c['audience_mos']} |
| **Max Class Size** | {c['max_class_size']} |
| **Min Class Size** | {c['min_class_size']} |
| **Scheduling Cadence** | {c['cadence']} |
| **Instructor Ratio** | {c['instructor_ratio']} |
| **Instructor Qualification** | {c['instructor_qualification']} |
| **Access Level Required** | {c['access_level']} |
| **Provisioning Lead Time** | {c['provisioning_lead_days']} duty days |
| **Evaluation** | {c['evaluation_type']} |
| **Hard NO-GO** | {c['hard_nogo']} |
| **Remediation Hours** | {c['remediation_hours']} hours |
| **Remediation Method** | {c['remediation_method']} |
| **Security Clearance** | {c['security_clearance']} |{doctrinal_refs}
{mandatory_note}
#### Equipment and Facility Requirements

| Requirement | Detail |
|---|---|
| Workstation | {c['equipment']['workstation']} |
| Network Access | {c['equipment']['network']} |
| Facilities | {c['equipment']['facilities']} |
| Special Equipment | {c['equipment']['special']} |

#### Academic Hours by Instructional Method

{_hours_table(c)}

#### Blocks of Instruction

{_blocks_table(c)}

#### T&EO Task Crosswalk

{_teo_list(c)}

---
""")

    # ── Footer ──
    sections.append(f"""## AMENDMENT RECORD

| Amendment | Date | Description | Approved By |
|---|---|---|---|
| Initial Publication | {PROGRAM_META['effective_date']} | Initial ATIS course registration packet | C2DAO |
| | | | |

---

*USAREUR-AF Operational Data Team — {PROGRAM_META['classification']}*
*ATIS Course Registration Packet | {PROGRAM_META['program_designation']} | {PROGRAM_META['effective_date']}*
*Generated: {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')} by build_atis_packet.py*
""")

    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w") as f:
        f.write("\n".join(sections))
    print(f"  MD  → {out_path}")


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    print("build_atis_packet.py — ATIS Course Registration Packet Generator")
    print(f"  Program: {PROGRAM_META['program_title']}")
    print(f"  Courses: {len(COURSES)}")
    print(f"  Total hours: {sum(c['duration_hours'] for c in COURSES)}")
    print()

    json_path = OUT_DIR / "atis_courses.json"
    md_path = OUT_DIR / "ATIS_COURSE_PACKET.md"

    build_json(json_path)
    build_markdown(md_path)

    print()
    print("Done. Outputs:")
    print(f"  {json_path.relative_to(REPO_ROOT)}")
    print(f"  {md_path.relative_to(REPO_ROOT)}")
    print()
    print("Next steps:")
    print("  Phase 1: Submit ATIS_COURSE_PACKET.md to USAREUR-AF G3/7 for command training registration")
    print("  Phase 2: Use atis_courses.json as structured input for T2COM institutional registration tooling")


if __name__ == "__main__":
    main()
