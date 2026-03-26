#!/usr/bin/env python3
"""
generate_dep_map.py
-------------------
Generates a self-contained, interactive HTML dendritic dependency map of the
USAREUR-AF Maven Training corpus.

Output: maven_training/DEPENDENCY_MAP.html
"""

import html as html_mod
import os
import json
from pathlib import Path

# ---------------------------------------------------------------------------
# 1. NODE DEFINITIONS
# ---------------------------------------------------------------------------
# Each node: id, label (short display), full_path (relative to maven_training/),
# node_type, column (tier), track (cluster within column)

NODES = []

def add(node_id, label, path, node_type, column, track):
    # Escape all user-visible strings that may end up in innerHTML via JS tooltips
    NODES.append({
        "id": node_id,
        "label": html_mod.escape(label),
        "path": html_mod.escape(path),
        "type": html_mod.escape(node_type),
        "col": column,
        "track": html_mod.escape(track),
    })


# ---- DOCTRINE / STANDARDS (column 0) ----
add("DOC_TECHREF",  "DATA_LITERACY\nTech Ref",    "doctrine/DATA_LITERACY_technical_reference.md",  "DOCTRINE", 0, "Doctrine")
add("DOC_SENIOR",   "DATA_LITERACY\nSr Leaders",  "doctrine/DATA_LITERACY_senior_leaders.md",        "DOCTRINE", 0, "Doctrine")
add("DOC_GLOSSARY", "GLOSSARY\nData Foundry",     "doctrine/GLOSSARY_data_foundry.md",               "DOCTRINE", 0, "Doctrine")
add("DOC_NAMING",   "NAMING &\nGOVERNANCE STD",   "standards/NAMING_AND_GOVERNANCE_STANDARDS.md",    "DOCTRINE", 0, "Standards")
add("DOC_CHEAT",    "cheatsheet.md",              "quick_reference/cheatsheet.md",                   "DOCTRINE", 0, "Standards")

# ---- SL 1 CLUSTER (column 1) ----
add("TM10",         "SL 1\nMAVEN USER",     "tm/TM_10_maven_user/TM_10_MAVEN_USER.md",            "TM",   1, "SL 1")
add("SYL10",        "SYLLABUS\nSL 1",       "syllabi/SYLLABUS_TM10.md",                            "SYL",  1, "SL 1")
add("EX10",         "EX-10\nOperator",      "exercises/EX_10_operator_basics/EXERCISE.md",          "EX",   1, "SL 1")
add("EXAM10PRE",    "EXAM SL 1\nPRE",       "exercises/exams/EXAM_TM10_PRE.md",                    "EXAM", 1, "SL 1")
add("EXAM10SUPP",   "EXAM SL 1\nSUPP",      "exercises/exams/EXAM_TM10_SUPPLEMENTAL.md",           "EXAM", 1, "SL 1")

# ---- SL 2 CLUSTER (column 2) ----
add("TM20",         "SL 2\nBUILDER",        "tm/TM_20_builder/TM_20_BUILDER.md",                  "TM",   2, "SL 2")
add("SYL20",        "SYLLABUS\nSL 2",       "syllabi/SYLLABUS_TM20.md",                            "SYL",  2, "SL 2")
add("EX20",         "EX-20\nNo-Code Builder","exercises/EX_20_no_code_builder/EXERCISE.md",         "EX",   2, "SL 2")
add("EXAM20PRE",    "EXAM SL 2\nPRE",       "exercises/exams/EXAM_TM20_PRE.md",                    "EXAM", 2, "SL 2")
add("EXAM20POST",   "EXAM SL 2\nPOST",      "exercises/exams/EXAM_TM20_POST.md",                   "EXAM", 2, "SL 2")

# ---- SL 3 CLUSTER (column 3) ----
add("TM30",         "SL 3\nADV BUILDER",    "tm/TM_30_advanced_builder/TM_30_ADVANCED_BUILDER.md","TM",   3, "SL 3")
add("SYL30",        "SYLLABUS\nSL 3",       "syllabi/SYLLABUS_TM30.md",                            "SYL",  3, "SL 3")
add("EX30",         "EX-30\nAdv Builder",   "exercises/EX_30_advanced_builder/EXERCISE.md",         "EX",   3, "SL 3")
add("EXAM30PRE",    "EXAM SL 3\nPRE",       "exercises/exams/EXAM_TM30_PRE.md",                    "EXAM", 3, "SL 3")
add("EXAM30POST",   "EXAM SL 3\nPOST",      "exercises/exams/EXAM_TM30_POST.md",                   "EXAM", 3, "SL 3")

# ---- SL 4 WFF TRACKS (column 4) ----
WFF_TRACKS = [
    ("A", "intelligence",     "Intelligence"),
    ("B", "fires",            "Fires"),
    ("C", "movement_maneuver","Mvt & Maneuver"),
    ("D", "sustainment",      "Sustainment"),
    ("E", "protection",       "Protection"),
    ("F", "mission_command",  "Mission Cmd"),
]
for letter, dirname, label in WFF_TRACKS:
    t = f"SL 4{letter}"
    add(f"TM40{letter}",       f"SL 4{letter}\n{label}",           f"tm/TM_40{letter}_{dirname}/TM_40{letter}_{dirname.upper()}.md",                               "TM",  4, t)
    add(f"CG40{letter}",       f"CONCEPTS GUIDE\nSL 4{letter}",    f"tm/TM_40{letter}_{dirname}/CONCEPTS_GUIDE_TM40{letter}_{dirname.upper()}.md",                 "CG",  4, t)
    add(f"SYL40{letter}",      f"SYLLABUS\nSL 4{letter}",          f"syllabi/SYLLABUS_TM40{letter}.md",                                                            "SYL", 4, t)
    add(f"EX40{letter}",       f"EX-4{letter}\n{label}",           f"exercises/EX_40{letter}_{dirname}/EXERCISE.md",                                               "EX",  4, t)
    add(f"EXAM40{letter}PRE",  f"EXAM SL 4{letter}\nPRE",          f"exercises/exams/EXAM_TM40{letter}_PRE.md",                                                    "EXAM",4, t)
    add(f"EXAM40{letter}POST", f"EXAM SL 4{letter}\nPOST",         f"exercises/exams/EXAM_TM40{letter}_POST.md",                                                   "EXAM",4, t)

# Fix TM filenames for WFF (actual file uses uppercase dirname but some are mixed)
# Override the TM and CG paths for WFF tracks to match actual filenames on disk
WFF_TM_FILENAME_MAP = {
    "A": ("TM_40A_INTELLIGENCE.md",      "CONCEPTS_GUIDE_TM40A_INTELLIGENCE.md"),
    "B": ("TM_40B_FIRES.md",             "CONCEPTS_GUIDE_TM40B_FIRES.md"),
    "C": ("TM_40C_MOVEMENT_MANEUVER.md", "CONCEPTS_GUIDE_TM40C_MOVEMENT_MANEUVER.md"),
    "D": ("TM_40D_SUSTAINMENT.md",       "CONCEPTS_GUIDE_TM40D_SUSTAINMENT.md"),
    "E": ("TM_40E_PROTECTION.md",        "CONCEPTS_GUIDE_TM40E_PROTECTION.md"),
    "F": ("TM_40F_MISSION_COMMAND.md",   "CONCEPTS_GUIDE_TM40F_MISSION_COMMAND.md"),
}
for node in NODES:
    for letter, dirname, _ in WFF_TRACKS:
        if node["id"] == f"TM40{letter}":
            node["path"] = f"tm/TM_40{letter}_{dirname}/TM_40{letter}_{dirname.upper()}.md"
        elif node["id"] == f"CG40{letter}":
            node["path"] = f"tm/TM_40{letter}_{dirname}/CONCEPTS_GUIDE_TM40{letter}_{dirname.upper()}.md"

# ---- SL 4 SPECIALIST TRACKS (column 4, lower half) ----
SPEC_TRACKS = [
    ("G", "orsa",             "ORSA"),
    ("H", "ai_engineer",      "AI Engineer"),
    ("M", "ml_engineer",      "ML Engineer"),
    ("J", "program_manager",  "Prog Manager"),
    ("K", "knowledge_manager","Knwl Manager"),
    ("L", "software_engineer","Software Engr"),
]
for letter, dirname, label in SPEC_TRACKS:
    t = f"SL 4{letter}"
    add(f"TM40{letter}",       f"SL 4{letter}\n{label}",           f"tm/TM_40{letter}_{dirname}/TM_40{letter}_{dirname.upper()}.md",                               "TM",  4, t)
    add(f"CG40{letter}",       f"CONCEPTS GUIDE\nSL 4{letter}",    f"tm/TM_40{letter}_{dirname}/CONCEPTS_GUIDE_TM40{letter}_{dirname.upper()}.md",                 "CG",  4, t)
    add(f"SYL40{letter}",      f"SYLLABUS\nSL 4{letter}",          f"syllabi/SYLLABUS_TM40{letter}.md",                                                            "SYL", 4, t)
    add(f"EX40{letter}",       f"EX-4{letter}\n{label}",           f"exercises/EX_40{letter}_{dirname}/EXERCISE.md",                                               "EX",  4, t)
    add(f"EXAM40{letter}PRE",  f"EXAM SL 4{letter}\nPRE",          f"exercises/exams/EXAM_TM40{letter}_PRE.md",                                                    "EXAM",4, t)
    add(f"EXAM40{letter}POST", f"EXAM SL 4{letter}\nPOST",         f"exercises/exams/EXAM_TM40{letter}_POST.md",                                                   "EXAM",4, t)

# ---- SL 5 ADVANCED TRACKS (column 5) ----
ADV_TRACKS = [
    ("G", "orsa_advanced",             "Adv ORSA"),
    ("H", "ai_engineer_advanced",      "Adv AI Engr"),
    ("M", "ml_engineer_advanced",      "Adv ML Engr"),
    ("J", "program_manager_advanced",  "Adv Prog Mgr"),
    ("K", "knowledge_manager_advanced","Adv Knwl Mgr"),
    ("L", "software_engineer_advanced","Adv SWE"),
]
for letter, dirname, label in ADV_TRACKS:
    t = f"SL 5{letter}"
    # TM filename
    base = dirname.upper()
    add(f"TM50{letter}",       f"SL 5{letter}\n{label}",         f"tm/TM_50{letter}_{dirname}/TM_50{letter}_{base}.md",                              "TM",  5, t)
    add(f"CG50{letter}",       f"CONCEPTS GUIDE\nSL 5{letter}",  f"tm/TM_50{letter}_{dirname}/CONCEPTS_GUIDE_TM50{letter}_{base}.md",                "CG",  5, t)
    add(f"SYL50{letter}",      f"SYLLABUS\nSL 5{letter}",        f"syllabi/SYLLABUS_TM50{letter}.md",                                                "SYL", 5, t)
    add(f"EXAM50{letter}PRE",  f"EXAM SL 5{letter}\nPRE",        f"exercises/exams/EXAM_TM50{letter}_PRE.md",                                        "EXAM",5, t)
    add(f"EXAM50{letter}POST", f"EXAM SL 5{letter}\nPOST",       f"exercises/exams/EXAM_TM50{letter}_POST.md",                                       "EXAM",5, t)

# ---- TRAINING MANAGEMENT (column 6) ----
TMGMT_NODES = [
    ("MGMT_MTP",     "MTP_MSS",                   "training_management/MTP_MSS.md"),
    ("MGMT_POI",     "POI_MSS",                   "training_management/POI_MSS.md"),
    ("MGMT_CAD",     "CAD_MSS",                   "training_management/CAD_MSS.md"),
    ("MGMT_TEO",     "TEO_MSS",                   "training_management/TEO_MSS.md"),
    ("MGMT_ENROLL",  "ENROLLMENT_SOP",             "training_management/ENROLLMENT_SOP.md"),
    ("MGMT_SCHED",   "ANNUAL_TRAINING\nSCHEDULE",  "training_management/ANNUAL_TRAINING_SCHEDULE.md"),
    ("MGMT_FACULTY", "FACULTY_DEV\nPLAN",          "training_management/FACULTY_DEVELOPMENT_PLAN.md"),
    ("MGMT_CERT",    "COMPLETION\nCERTIFICATE",    "training_management/COMPLETION_CERTIFICATE.md"),
    ("MGMT_CMS",     "CURRICULUM\nMAINT SOP",      "training_management/CURRICULUM_MAINTENANCE_SOP.md"),
    ("LP_TM10",      "TM10\nLESSON PLANS",         "training_management/lesson_plans/TM10/TM10_LESSON_PLANS.md"),
    ("LP_TM20",      "TM20\nLESSON PLANS",         "training_management/lesson_plans/TM20_LESSON_PLAN_OUTLINES.md"),
    ("LP_TM30",      "TM30\nLESSON PLANS",         "training_management/lesson_plans/TM30_LESSON_PLAN_OUTLINES.md"),
    ("LP_TM40SPEC",  "TM40 SPECIALIST\nLESSON PLANS","training_management/lesson_plans/TM40_SPECIALIST_LESSON_PLAN_OUTLINES.md"),
]
for nid, lbl, path in TMGMT_NODES:
    add(nid, lbl, path, "TMGMT", 6, "Training Mgmt")

# ---- HTML APPS (column 6) ----
add("HTML_MSS",      "mss_info_app\nindex.html",        "mss_info_app/index.html",              "HTML", 6, "HTML Apps")
add("HTML_TASKIDX",  "task_index.html",                 "task_index.html",                      "HTML", 6, "HTML Apps")
add("HTML_SCHED",    "training_schedule.html",          "mss_info_app/training_schedule.html",  "HTML", 6, "HTML Apps")

# ---- READMEs (column 6) ----
add("README_MT",     "maven_training\nREADME.md",       "README.md",                            "README", 6, "READMEs")
add("README_QS",     "QUICK_START.md",                  "QUICK_START.md",                       "README", 6, "READMEs")
add("README_ROOT",   "Root\nREADME.md",                 "../README.md",                         "README", 6, "READMEs")

# ---- CDA SLIDE LIBRARY (column -1, prereq layer) ----
# Three aggregate track nodes representing 29 CDA slide decks from repos/
# Intro To Data: army_data_orientation_v1, architecture_primer, Data_Architecture_Deep_Dive,
#   2026_Data_Stack_Deep_Dive, L2_Ingestion_Integration_Deep_Dive, The_Semantic_Layer_Instructions,
#   What_Is_An_Ontology, Data_Modeling_Foundations, Data_Platforms_Cloud_Deep_Dive,
#   L5_Activation_Interface_Deep_Dive, AI_ML_Beyond_The_Hype, decision_advantage_deep_dive
add("CDA_INTRO", "CDA — Intro\nTo Data (12)", "repos/src/architecture/cda/apps/course-portal/", "CDA", -1, "CDA Library")
# Data 101: The_Four_Layers, Data_Modeling_Fundamentals_Level1, ObjectType_WhatToWatchFor,
#   Controlled_Vocabularies, Identity_Who_Owns_The_Key, Links_and_Relationships, Dont_Filter_This_Isnt_Excel
add("CDA_101",   "CDA — Data 101\n(7 decks)",  "repos/src/architecture/cda/apps/course-portal/", "CDA", -1, "CDA Library")
# Data 201: Semantic_Modelling_Course_Intro, Deck_01–07, Data_Modeling_Fundamentals_Level2, Deck_12_Capstone_Foundry
add("CDA_201",   "CDA — Data 201\n(10 decks)", "repos/src/architecture/cda/apps/course-portal/", "CDA", -1, "CDA Library")


# ---------------------------------------------------------------------------
# 2. EDGE DEFINITIONS
# ---------------------------------------------------------------------------
# Each edge: source_id, target_id, edge_type ("prereq" | "companion")

EDGES = []

def edge(src, tgt, etype="prereq"):
    EDGES.append({"source": src, "target": tgt, "type": etype})


# ---- SL 1/2/3 prereq chain ----
edge("TM20", "TM10")
edge("TM30", "TM10")
edge("TM30", "TM20")

# ---- SL 1/2/3 cluster internal ----
for suffix, tm in [("10", "TM10"), ("20", "TM20"), ("30", "TM30")]:
    edge(f"SYL{suffix}",       tm)
    edge(f"EX{suffix}",        tm)
    edge(f"EXAM{suffix}PRE",   tm)
    edge(f"EXAM{suffix}POST",  tm)

# ---- Syllabus prereqs for SL 2/3 ----
edge("SYL20", "TM10")
edge("SYL30", "TM10")
edge("SYL30", "TM20")

# ---- SL 4 WFF tracks ----
for letter, _, _ in WFF_TRACKS:
    # TM prereqs
    edge(f"TM40{letter}", "TM10")
    edge(f"TM40{letter}", "TM20")
    edge(f"TM40{letter}", f"CG40{letter}")
    # Syllabus prereqs
    edge(f"SYL40{letter}", "TM10")
    edge(f"SYL40{letter}", "TM20")
    # Exercise prereq
    edge(f"EX40{letter}", f"TM40{letter}")
    # Exam prereqs
    edge(f"EXAM40{letter}PRE",  f"TM40{letter}")
    edge(f"EXAM40{letter}POST", f"TM40{letter}")

# ---- SL 4 Specialist tracks ----
for letter, _, _ in SPEC_TRACKS:
    # TM prereqs
    edge(f"TM40{letter}", "TM10")
    edge(f"TM40{letter}", "TM20")
    edge(f"TM40{letter}", "TM30")
    edge(f"TM40{letter}", f"CG40{letter}")
    # Syllabus prereqs
    edge(f"SYL40{letter}", "TM10")
    edge(f"SYL40{letter}", "TM20")
    edge(f"SYL40{letter}", "TM30")
    # Exercise prereq
    edge(f"EX40{letter}", f"TM40{letter}")
    # Exam prereqs
    edge(f"EXAM40{letter}PRE",  f"TM40{letter}")
    edge(f"EXAM40{letter}POST", f"TM40{letter}")

# ---- SL 5 Advanced tracks ----
for letter, _, _ in ADV_TRACKS:
    edge(f"TM50{letter}", f"TM40{letter}")
    edge(f"TM50{letter}", f"CG50{letter}")
    edge(f"SYL50{letter}", f"TM40{letter}")
    edge(f"EXAM50{letter}PRE",  f"TM50{letter}")
    edge(f"EXAM50{letter}POST", f"TM50{letter}")

# ---- Training management → base TMs ----
base_mgmt = ["MGMT_MTP","MGMT_POI","MGMT_CAD","MGMT_TEO","MGMT_ENROLL","MGMT_SCHED"]
for nid in base_mgmt:
    edge(nid, "TM10")
    edge(nid, "TM20")
    edge(nid, "TM30")

# FACULTY_DEVELOPMENT_PLAN → all SL 4x and syllabi
for letter, _, _ in WFF_TRACKS + SPEC_TRACKS:
    edge("MGMT_FACULTY", f"TM40{letter}")
    edge("MGMT_FACULTY", f"SYL40{letter}")
for letter, _, _ in ADV_TRACKS:
    edge("MGMT_FACULTY", f"TM50{letter}")
    edge("MGMT_FACULTY", f"SYL50{letter}")

# Lesson plan references
edge("LP_TM10", "TM10")
edge("LP_TM10", "DOC_TECHREF")
edge("LP_TM20", "TM20")
edge("LP_TM20", "DOC_NAMING")
edge("LP_TM30", "TM30")
for letter, _, _ in SPEC_TRACKS:
    edge("LP_TM40SPEC", f"TM40{letter}")

# ---- Doctrine referenced by SL 1/2/3 ----
edge("TM10", "DOC_TECHREF", "companion")
edge("TM20", "DOC_TECHREF", "companion")
edge("TM30", "DOC_TECHREF", "companion")
edge("EX20", "DOC_NAMING",  "companion")
edge("EX30", "DOC_NAMING",  "companion")

# ---- Cross-track companion refs (WFF) ----
edge("TM40A", "TM40F", "companion")
edge("TM40F", "TM40A", "companion")

for partner in ["TM40A","TM40B","TM40C","TM40E","TM40F"]:
    edge("TM40D", partner, "companion")

for partner in ["TM40A","TM40B","TM40C","TM40F"]:
    edge("TM40E", partner, "companion")

for partner in ["TM40G","TM40H","TM40M","TM40J","TM40K"]:
    edge("TM40F", partner, "companion")

# ---- Cross-track companion refs (Specialist) ----
edge("TM40G", "TM40H", "companion")
edge("TM40H", "TM40G", "companion")
edge("TM40G", "TM40M", "companion")
edge("TM40M", "TM40G", "companion")
edge("TM40K", "TM40H", "companion")
edge("TM40K", "TM40L", "companion")

# ---- Cross-track companion refs (Advanced) ----
edge("TM50G", "TM50H", "companion")
edge("TM50H", "TM50G", "companion")
edge("TM50G", "TM50M", "companion")
edge("TM50M", "TM50G", "companion")
edge("TM50H", "TM50M", "companion")
edge("TM50M", "TM50H", "companion")
edge("TM50H", "TM50J", "companion")
edge("TM50J", "TM50H", "companion")
edge("TM50H", "TM50K", "companion")
edge("TM50K", "TM50H", "companion")
edge("TM50H", "TM50L", "companion")
edge("TM50L", "TM50H", "companion")

# ---- HTML app refs ----
# mss_info_app/index.html → all SL 4x main + CG + syllabi + exams
for letter, _, _ in WFF_TRACKS + SPEC_TRACKS:
    edge("HTML_MSS", f"TM40{letter}",      "companion")
    edge("HTML_MSS", f"CG40{letter}",      "companion")
    edge("HTML_MSS", f"SYL40{letter}",     "companion")
    edge("HTML_MSS", f"EXAM40{letter}PRE", "companion")
    edge("HTML_MSS", f"EXAM40{letter}POST","companion")

# task_index.html → SL 4G-M, SL 5G-M
for letter, _, _ in SPEC_TRACKS:
    edge("HTML_TASKIDX", f"TM40{letter}", "companion")
for letter, _, _ in ADV_TRACKS:
    edge("HTML_TASKIDX", f"TM50{letter}", "companion")

# ---- CDA companion edges (prereq layer → TM core) ----
# Intro To Data decks are conceptual prereqs for SL 1 and SL 2
edge("CDA_INTRO", "TM10", "companion")
edge("CDA_INTRO", "TM20", "companion")
# Data 101 decks bridge SL 2 and SL 3
edge("CDA_101", "TM20", "companion")
edge("CDA_101", "TM30", "companion")
# Data 201 decks are prereqs for SL 3 and specialist SL 4 tracks
edge("CDA_201", "TM30", "companion")


# ---------------------------------------------------------------------------
# 3. LAYOUT COMPUTATION
# ---------------------------------------------------------------------------
# Node dimensions
NODE_W = 170
NODE_H = 50
V_GAP  = 10   # vertical gap between track rows within a tier
NODE_X_GAP = 14  # horizontal gap between nodes within a track row

def layout_nodes(nodes):
    """
    Vertical layout: tiers stack top-to-bottom (Doctrine → SL 5).
    Within each tier, each TRACK is one horizontal row of nodes.
    Tracks within a tier stack vertically (one row per track).
    Training Mgmt / HTML / README go in a sidebar on the right.
    CDA overlay nodes are placed above Doctrine (tier -1).
    """
    from collections import defaultdict

    SIDEBAR_TYPES = {"TMGMT", "HTML", "README"}
    flow_nodes    = [n for n in nodes if n["type"] not in SIDEBAR_TYPES]
    sidebar_nodes = [n for n in nodes if n["type"] in SIDEBAR_TYPES]

    # Group flow nodes by (tier/col, track), preserving insertion order per tier
    tier_track_groups = defaultdict(list)
    tier_tracks       = defaultdict(list)   # ordered track list per tier
    seen = set()
    for n in flow_nodes:
        key = (n["col"], n["track"])
        tier_track_groups[key].append(n)
        if key not in seen:
            tier_tracks[n["col"]].append(n["track"])
            seen.add(key)

    PITCH_X    = NODE_W + NODE_X_GAP   # x step between adjacent nodes in a row
    TIER_HDR_H = 28                    # reserved height above each tier for label
    TIER_GAP   = 40                    # vertical gap between tier bands
    TOP_MARGIN = 44
    LEFT_MARGIN = 30

    # Compute y baseline for each tier
    sorted_tiers = sorted(tier_tracks.keys())
    tier_y = {}
    y = TOP_MARGIN
    for tier in sorted_tiers:
        tier_y[tier] = y + TIER_HDR_H
        num_tracks = len(tier_tracks[tier])
        tier_h = num_tracks * (NODE_H + V_GAP) - V_GAP
        y += TIER_HDR_H + tier_h + TIER_GAP

    # Find max nodes in any single track row (globally — used by JS relayout)
    global_max_ni = max(
        len(tier_track_groups[(tier, track)])
        for tier, tracks in tier_tracks.items()
        for track in tracks
    )

    # Assign y and store ni (index within row); x is a placeholder, JS will relayout
    for tier, tracks in tier_tracks.items():
        base_y = tier_y[tier]
        tier_max_n = max(len(tier_track_groups[(tier, t)]) for t in tracks)
        for ti, track in enumerate(tracks):
            row_y = base_y + ti * (NODE_H + V_GAP)
            group = tier_track_groups[(tier, track)]
            for ni, node in enumerate(group):
                node["ni"]         = ni            # index within track row
                node["row_len"]    = len(group)    # nodes in this track row
                node["max_row_len"]= tier_max_n    # max row length in this tier
                node["x"]          = LEFT_MARGIN + ni * PITCH_X  # fallback
                node["y"]          = row_y
                node["is_sidebar"] = False

    # Sidebar: placeholder x, stacked vertically — JS will pin to right edge
    sy = TOP_MARGIN + TIER_HDR_H
    for node in sidebar_nodes:
        node["ni"]         = 0
        node["row_len"]    = 1
        node["max_row_len"]= 1
        node["x"]          = LEFT_MARGIN + global_max_ni * PITCH_X + 60  # placeholder
        node["y"]          = sy
        node["is_sidebar"] = True
        sy += NODE_H + V_GAP

    return nodes

NODES = layout_nodes(NODES)

# Tier header labels with layman names (embedded in JS)
TIER_HEADER_LABELS = {
    -1: "CDA SLIDE LIBRARY — Conceptual Prerequisites",
     0: "DOCTRINE & STANDARDS",
     1: "SL 1 — Foundry Basics  |  All Personnel",
     2: "SL 2 — No-Code Builder  |  Operator / Analyst",
     3: "SL 3 — Advanced Builder  |  Data Engineer",
     4: "SL 4 — WFF Analyst Tracks (A–F)   ·   Specialist Roles (G–M)",
     5: "SL 5 — Advanced Specialization  |  Expert Level",
}
tier_headers_json = json.dumps({str(k): v for k, v in TIER_HEADER_LABELS.items()})

# ---------------------------------------------------------------------------
# 3b. AUDIENCE TAGGING
# ---------------------------------------------------------------------------
# Tag each node with the audience(s) it is relevant to:
#   user      = SL 1 level Maven user / end operator
#   trainer   = instructor / training management staff
#   dev       = builder, developer, SL 2+ level
#   specialist = SL 4G-M / SL 5G-M specialist tracks only
SPEC_LETTERS = {"G","H","I","J","K","L"}
WFF_LETTERS  = {"A","B","C","D","E","F"}

for node in NODES:
    col   = node["col"]
    ntype = node["type"]
    nid   = node["id"]
    aud   = []

    if ntype == "DOCTRINE":
        aud = ["user", "trainer", "dev"]
    elif col == 1:          # SL 1 cluster
        aud = ["user", "trainer"]
    elif col == 2:          # SL 2 cluster
        aud = ["dev", "trainer"]
    elif col == 3:          # SL 3 cluster
        aud = ["dev", "trainer"]
    elif col == 4:          # SL 4 — split WFF vs Specialist
        is_spec = any(f"40{l}" in nid for l in SPEC_LETTERS)
        is_wff  = any(f"40{l}" in nid for l in WFF_LETTERS)
        if is_spec:
            aud = ["dev", "specialist"]
        elif is_wff:
            aud = ["user", "dev"]
        else:
            aud = ["dev"]
    elif col == 5:          # SL 5 Advanced
        aud = ["dev", "specialist"]
    elif col == 6:          # Training Mgmt / HTML / README
        if ntype == "TMGMT":
            aud = ["trainer"]
        else:
            aud = ["trainer", "dev"]
    elif col == -1:         # CDA Slide Library
        aud = ["user", "dev"]

    node["aud"] = aud

# Calculate SVG canvas dimensions from actual node positions
max_y = max(n["y"] for n in NODES) + NODE_H + 80
max_x = max(n["x"] for n in NODES) + NODE_W + 60
SVG_W = max(2000, max_x)
SVG_H = max(1400, max_y)


# ---------------------------------------------------------------------------
# 4. SERIALIZE TO JSON FOR EMBEDDING
# ---------------------------------------------------------------------------
nodes_json = json.dumps(NODES, separators=(",", ":"))
edges_json = json.dumps(EDGES, separators=(",", ":"))

print(f"Nodes: {len(NODES)}")
print(f"Edges: {len(EDGES)}")
print(f"SVG canvas: {SVG_W} x {SVG_H} px")


# ---------------------------------------------------------------------------
# 5. HTML GENERATION
# ---------------------------------------------------------------------------
HTML = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Maven Training Corpus — File Dependency Map</title>
<style>
  :root {{
    --bg: #0d1b2a;
    --header-bg: #0a1520;
    --text: #c8d8e8;
    --accent: #4a90d9;
    --border: #1e3a50;
    --banner-bg: #3a1a00;
    --banner-text: #ffcc44;
  }}
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  body {{
    background: var(--bg);
    color: var(--text);
    font-family: 'Courier New', Courier, monospace;
    height: 100vh;
    display: flex;
    flex-direction: column;
    overflow: hidden;
  }}
  #banner {{
    background: var(--banner-bg);
    color: var(--banner-text);
    text-align: center;
    font-size: 11px;
    font-weight: bold;
    letter-spacing: 3px;
    padding: 4px 0;
    border-bottom: 1px solid #7a3a00;
    flex-shrink: 0;
  }}
  #header {{
    background: var(--header-bg);
    border-bottom: 1px solid var(--border);
    padding: 8px 16px;
    flex-shrink: 0;
    display: flex;
    align-items: center;
    gap: 24px;
    flex-wrap: wrap;
  }}
  #header h1 {{
    font-size: 15px;
    font-weight: bold;
    color: #e8f4ff;
    letter-spacing: 1px;
  }}
  #header .subtitle {{
    font-size: 10px;
    color: #7a9ab8;
    letter-spacing: 1px;
    margin-top: 2px;
  }}
  #controls {{
    display: flex;
    align-items: center;
    gap: 16px;
    flex-wrap: wrap;
    margin-left: auto;
  }}
  .ctrl-group {{
    display: flex;
    align-items: center;
    gap: 6px;
    font-size: 11px;
  }}
  .ctrl-group label {{
    cursor: pointer;
    user-select: none;
  }}
  input[type=checkbox] {{ accent-color: var(--accent); cursor: pointer; }}
  #search-box {{
    background: #0d2035;
    border: 1px solid var(--border);
    color: var(--text);
    padding: 3px 8px;
    font-family: inherit;
    font-size: 11px;
    border-radius: 3px;
    width: 160px;
  }}
  #search-box:focus {{ outline: 1px solid var(--accent); }}
  #svg-container {{
    flex: 1;
    overflow: hidden;
    position: relative;
    cursor: grab;
  }}
  #svg-container.panning {{ cursor: grabbing; }}
  svg#depmap {{
    display: block;
    width: 100%;
    height: 100%;
  }}
  #tooltip {{
    position: absolute;
    background: #0a1a2e;
    border: 1px solid var(--accent);
    border-radius: 4px;
    padding: 8px 12px;
    font-size: 11px;
    color: #d0e8ff;
    pointer-events: none;
    display: none;
    max-width: 340px;
    z-index: 100;
    line-height: 1.5;
    box-shadow: 0 4px 16px rgba(0,0,0,0.7);
  }}
  #tooltip .tt-title {{
    font-weight: bold;
    color: #80c8ff;
    margin-bottom: 4px;
    font-size: 12px;
  }}
  #tooltip .tt-path {{
    color: #607090;
    font-size: 10px;
    margin-bottom: 6px;
    word-break: break-all;
  }}
  #tooltip .tt-section {{
    color: #7aaac8;
    font-size: 10px;
    font-weight: bold;
    margin-top: 4px;
    letter-spacing: 1px;
  }}
  #tooltip .tt-item {{
    color: #a0c0d8;
    font-size: 10px;
    padding-left: 8px;
  }}
  #legend {{
    background: var(--header-bg);
    border-top: 1px solid var(--border);
    padding: 5px 16px;
    display: flex;
    align-items: center;
    gap: 16px;
    flex-wrap: wrap;
    flex-shrink: 0;
    font-size: 10px;
  }}
  .legend-item {{
    display: flex;
    align-items: center;
    gap: 5px;
  }}
  .legend-swatch {{
    width: 16px;
    height: 10px;
    border-radius: 2px;
    flex-shrink: 0;
  }}
  .legend-line {{
    width: 24px;
    height: 2px;
    flex-shrink: 0;
  }}
  #stats-bar {{
    position: absolute;
    bottom: 8px;
    right: 12px;
    font-size: 10px;
    color: #405060;
    pointer-events: none;
  }}
</style>
</head>
<body>

<div id="banner">DRAFT — NOT FOR OFFICIAL USE</div>

<div id="header">
  <div>
    <div id="header-title">
      <h1>Maven Training Corpus — File Dependency Map</h1>
      <div class="subtitle">USAREUR-AF &nbsp;|&nbsp; C2DAO &nbsp;|&nbsp; 12 MAR 2026 &nbsp;|&nbsp;
        <span id="node-count">{len(NODES)}</span> files &nbsp;|&nbsp;
        <span id="edge-count">{len(EDGES)}</span> edges
      </div>
    </div>
  </div>
  <div id="controls">
    <div class="ctrl-group">
      <input type="text" id="search-box" placeholder="Search nodes…" oninput="handleSearch(this.value)">
    </div>
    <div class="ctrl-group" style="border-left:1px solid #1e3a50;padding-left:12px">
      <span style="color:#607080;font-size:10px;font-weight:bold;letter-spacing:1px;margin-right:4px">AUDIENCE:</span>
      <input type="checkbox" id="chk-aud-user" checked onchange="applyAudienceFilter()">
      <label for="chk-aud-user" style="color:#7ab8d8">User</label>
      &nbsp;
      <input type="checkbox" id="chk-aud-trainer" checked onchange="applyAudienceFilter()">
      <label for="chk-aud-trainer" style="color:#7ad8a8">Trainer</label>
      &nbsp;
      <input type="checkbox" id="chk-aud-dev" checked onchange="applyAudienceFilter()">
      <label for="chk-aud-dev" style="color:#d8a870">Dev</label>
    </div>
    <div class="ctrl-group" style="border-left:1px solid #1e3a50;padding-left:12px">
      <input type="checkbox" id="chk-aud-spec" checked onchange="applyAudienceFilter()">
      <label for="chk-aud-spec" style="color:#b888d8">Specialist</label>
    </div>
    <div class="ctrl-group" style="border-left:1px solid #1e3a50;padding-left:12px">
      <input type="checkbox" id="chk-prereq" checked onchange="toggleEdges()">
      <label for="chk-prereq">Prereq edges</label>
    </div>
    <div class="ctrl-group">
      <input type="checkbox" id="chk-companion" checked onchange="toggleEdges()">
      <label for="chk-companion">Companion edges</label>
    </div>
    <div class="ctrl-group" style="border-left:1px solid #1e3a50;padding-left:12px">
      <input type="checkbox" id="chk-cda" onchange="toggleCDA()">
      <label for="chk-cda" style="color:#c8a040">CDA Overlay</label>
    </div>
    <div class="ctrl-group" style="margin-left:8px">
      <button onclick="resetView()" style="background:#1a2a3a;border:1px solid #2a4a6a;color:#7aaad8;
        padding:3px 10px;font-family:inherit;font-size:11px;border-radius:3px;cursor:pointer;">
        Reset View
      </button>
    </div>
  </div>
</div>

<div id="svg-container">
  <svg id="depmap" xmlns="http://www.w3.org/2000/svg">
    <defs>
      <marker id="arrow-prereq" markerWidth="6" markerHeight="6"
              refX="5" refY="3" orient="auto" markerUnits="strokeWidth">
        <path d="M0,0 L0,6 L6,3 z" fill="#4a90d9"/>
      </marker>
      <marker id="arrow-companion" markerWidth="6" markerHeight="6"
              refX="5" refY="3" orient="auto" markerUnits="strokeWidth">
        <path d="M0,0 L0,6 L6,3 z" fill="#888888"/>
      </marker>
      <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
        <feGaussianBlur stdDeviation="3" result="blur"/>
        <feComposite in="SourceGraphic" in2="blur" operator="over"/>
      </filter>
      <filter id="highlight-glow" x="-30%" y="-30%" width="160%" height="160%">
        <feGaussianBlur stdDeviation="4" result="blur"/>
        <feFlood flood-color="#ffcc44" flood-opacity="0.4" result="color"/>
        <feComposite in="color" in2="blur" operator="in" result="glow"/>
        <feComposite in="SourceGraphic" in2="glow" operator="over"/>
      </filter>
    </defs>

    <!-- Main transform group for pan/zoom -->
    <g id="viewport">
      <g id="edges-companion-group"></g>
      <g id="edges-prereq-group"></g>
      <g id="nodes-group"></g>
      <g id="labels-group"></g>
      <!-- CDA overlay — hidden by default, toggled via checkbox -->
      <g id="cda-group" style="display:none">
        <g id="cda-edges-grp"></g>
        <g id="cda-nodes-grp"></g>
      </g>
    </g>
  </svg>

  <div id="tooltip"></div>
  <div id="stats-bar">Scroll to zoom · Drag to pan · Hover for details</div>
</div>

<div id="legend">
  <span style="color:#607080;font-weight:bold;letter-spacing:1px;">NODE TYPE:</span>
  <div class="legend-item"><div class="legend-swatch" style="background:#2a6496"></div>TM (Technical Manual)</div>
  <div class="legend-item"><div class="legend-swatch" style="background:#2e7d52"></div>Concepts Guide</div>
  <div class="legend-item"><div class="legend-swatch" style="background:#7b4da8"></div>Syllabus</div>
  <div class="legend-item"><div class="legend-swatch" style="background:#a85e2a"></div>Exam</div>
  <div class="legend-item"><div class="legend-swatch" style="background:#8a6a1a"></div>Exercise</div>
  <div class="legend-item"><div class="legend-swatch" style="background:#1a6a6a"></div>Doctrine/Standards</div>
  <div class="legend-item"><div class="legend-swatch" style="background:#4a4a7a"></div>Training Mgmt</div>
  <div class="legend-item"><div class="legend-swatch" style="background:#2a6a2a"></div>HTML App</div>
  <div class="legend-item"><div class="legend-swatch" style="background:#5a5a5a"></div>README</div>
  <div class="legend-item"><div class="legend-swatch" style="background:#7a4e00"></div>CDA Slide Library</div>
  &nbsp;&nbsp;
  <span style="color:#607080;font-weight:bold;letter-spacing:1px;">EDGES:</span>
  <div class="legend-item"><div class="legend-line" style="background:#4a90d9"></div>Prereq (solid)</div>
  <div class="legend-item"><div class="legend-line" style="background:#888;border-top:1px dashed #888;height:0"></div>Companion (dashed)</div>
</div>

<script>
// ============================================================
// DATA
// ============================================================
const NODES = {nodes_json};
const EDGES = {edges_json};

// Node type color map
const TYPE_COLOR = {{
  TM:      "#2a6496",
  CG:      "#2e7d52",
  SYL:     "#7b4da8",
  EXAM:    "#a85e2a",
  EX:      "#8a6a1a",
  DOCTRINE:"#1a6a6a",
  TMGMT:   "#4a4a7a",
  HTML:    "#2a6a2a",
  README:  "#5a5a5a",
  CDA:     "#7a4e00",
}};

const NODE_W = {NODE_W};
const NODE_H = {NODE_H};
const SVG_W  = {SVG_W};
const SVG_H  = {SVG_H};
const TIER_HEADERS = {tier_headers_json};

// ============================================================
// BUILD NODE INDEX & ADJACENCY
// ============================================================
const nodeById = {{}};
NODES.forEach(n => nodeById[n.id] = n);

const prereqsOf  = {{}};  // id -> [ids that this node depends on]
const dependents = {{}};  // id -> [ids that depend on this node]
NODES.forEach(n => {{ prereqsOf[n.id] = []; dependents[n.id] = []; }});
EDGES.forEach(e => {{
  if (e.type === "prereq") {{
    prereqsOf[e.source].push(e.target);
    dependents[e.target].push(e.source);
  }}
}});

// ============================================================
// SVG SETUP & VIEWPORT
// ============================================================
const svg    = document.getElementById("depmap");
const vpGrp  = document.getElementById("viewport");
const container = document.getElementById("svg-container");

let viewX = 0, viewY = 0, viewScale = 0.7;
let isPanning = false, panStartX, panStartY, vpStartX, vpStartY;

function applyTransform() {{
  vpGrp.setAttribute("transform",
    `translate(${{viewX}},${{viewY}}) scale(${{viewScale}})`);
}}

// ============================================================
// DYNAMIC LAYOUT — fills container width on load + resize
// ============================================================
function relayout() {{
  const W = container.clientWidth || window.innerWidth;
  const PAD = 24;
  const SIDEBAR_W = NODE_W + 32;   // sidebar column width
  const SIDEBAR_GAP = 48;          // gap between flow area and sidebar

  // Max nodes in any track row across all non-sidebar nodes
  let maxRowLen = 0;
  NODES.forEach(n => {{ if (!n.is_sidebar && n.row_len > maxRowLen) maxRowLen = n.row_len; }});
  if (maxRowLen < 1) maxRowLen = 1;

  // Flow area width (excludes sidebar)
  const flowW  = W - SIDEBAR_W - SIDEBAR_GAP - PAD * 2;
  // Pitch = space per node (center-to-center), capped at a readable max
  const pitchX = Math.min(Math.max(flowW / maxRowLen, NODE_W + 8), 400);
  const sidebarX = PAD + maxRowLen * pitchX + SIDEBAR_GAP;

  NODES.forEach(n => {{
    if (n.is_sidebar) {{
      n.x = sidebarX;
    }} else {{
      n.x = PAD + n.ni * pitchX;
    }}
  }});

  // Update DOM: move rects and text labels for each node
  document.querySelectorAll(".node-grp").forEach(g => {{
    const n = nodeById[g.getAttribute("data-id")];
    if (!n) return;
    const r = g.querySelector("rect");
    if (r) r.setAttribute("x", n.x);
    g.querySelectorAll("text").forEach(t => {{
      t.setAttribute("x", n.x + NODE_W / 2);
    }});
  }});

  // Re-draw edges since node positions changed
  renderEdges();
}}

window.addEventListener("resize", () => {{ relayout(); fitView(40); }});

function fitView(pad) {{
  pad = pad || 50;
  const W = container.clientWidth  || window.innerWidth;
  const H = container.clientHeight || window.innerHeight;

  // Compute bounding box of visible nodes
  let minX = Infinity, minY = Infinity, maxX = -Infinity, maxY = -Infinity;
  let count = 0;
  document.querySelectorAll(".node-grp").forEach(g => {{
    if (parseFloat(g.getAttribute("opacity") || "1") < 0.1) return;
    const n = nodeById[g.getAttribute("data-id")];
    if (!n) return;
    if (n.x < minX) minX = n.x;
    if (n.y < minY) minY = n.y;
    if (n.x + NODE_W > maxX) maxX = n.x + NODE_W;
    if (n.y + NODE_H > maxY) maxY = n.y + NODE_H;
    count++;
  }});
  if (!count) {{ minX = 0; minY = 0; maxX = SVG_W; maxY = SVG_H; }}

  const contentW = maxX - minX + pad * 2;
  const contentH = maxY - minY + pad * 2;
  viewScale = Math.min(W / contentW, H / contentH, 2.0);
  viewX = (W  - (minX + maxX) * viewScale) / 2;
  viewY = (H  - (minY + maxY) * viewScale) / 2;
  applyTransform();
}}

function resetView() {{
  fitView(50);
}}

// Zoom
container.addEventListener("wheel", e => {{
  e.preventDefault();
  const rect = container.getBoundingClientRect();
  const mx = e.clientX - rect.left;
  const my = e.clientY - rect.top;
  const delta = e.deltaY < 0 ? 1.12 : 0.89;
  const newScale = Math.min(3.0, Math.max(0.18, viewScale * delta));
  // Zoom toward mouse position
  viewX = mx - (mx - viewX) * (newScale / viewScale);
  viewY = my - (my - viewY) * (newScale / viewScale);
  viewScale = newScale;
  applyTransform();
}}, {{ passive: false }});

// Pan
container.addEventListener("mousedown", e => {{
  if (e.target === svg || e.target === vpGrp ||
      e.target.tagName === "line" || e.target.tagName === "path") {{
    isPanning = true;
    panStartX = e.clientX; panStartY = e.clientY;
    vpStartX = viewX; vpStartY = viewY;
    container.classList.add("panning");
  }}
}});
window.addEventListener("mousemove", e => {{
  if (!isPanning) return;
  viewX = vpStartX + (e.clientX - panStartX);
  viewY = vpStartY + (e.clientY - panStartY);
  applyTransform();
}});
window.addEventListener("mouseup", () => {{
  isPanning = false;
  container.classList.remove("panning");
}});

// ============================================================
// RENDER EDGES
// ============================================================
function makePath(src, tgt) {{
  // Adaptive bezier: vertical for tier-to-tier, horizontal for lateral/same-tier edges.
  const sxc = src.x + NODE_W / 2, syc = src.y + NODE_H / 2;
  const txc = tgt.x + NODE_W / 2, tyc = tgt.y + NODE_H / 2;
  const dx = Math.abs(txc - sxc), dy = Math.abs(tyc - syc);

  if (dx > dy * 1.5) {{
    // Primarily horizontal (lateral / sidebar edges)
    const sx = sxc > txc ? src.x : src.x + NODE_W;
    const tx = sxc > txc ? tgt.x + NODE_W : tgt.x;
    const cx1 = sx + (tx - sx) * 0.45, cx2 = tx - (tx - sx) * 0.45;
    return `M${{sx}},${{syc}} C${{cx1}},${{syc}} ${{cx2}},${{tyc}} ${{tx}},${{tyc}}`;
  }} else {{
    // Primarily vertical (tier-to-tier prereq edges)
    // Source is the dependent (below), target is the prereq (above)
    const sy = syc > tyc ? src.y : src.y + NODE_H;  // edge from top or bottom of src
    const ty = syc > tyc ? tgt.y + NODE_H : tgt.y;  // edge to bottom or top of tgt
    const cdy = Math.abs(ty - sy);
    const cy1 = sy + (ty - sy) * 0.45;
    const cy2 = ty - (ty - sy) * 0.45;
    return `M${{sxc}},${{sy}} C${{sxc}},${{cy1}} ${{txc}},${{cy2}} ${{txc}},${{ty}}`;
  }}
}}

function renderEdges() {{
  const prereqGrp    = document.getElementById("edges-prereq-group");
  const companionGrp = document.getElementById("edges-companion-group");
  const cdaEdgeGrp   = document.getElementById("cda-edges-grp");
  prereqGrp.innerHTML    = "";
  companionGrp.innerHTML = "";
  cdaEdgeGrp.innerHTML   = "";

  EDGES.forEach(e => {{
    const src = nodeById[e.source];
    const tgt = nodeById[e.target];
    if (!src || !tgt) return;

    const isCDA = (src.type === "CDA" || tgt.type === "CDA");

    const path = document.createElementNS("http://www.w3.org/2000/svg","path");
    const d = makePath(src, tgt);
    path.setAttribute("d", d);
    path.setAttribute("fill", "none");
    path.setAttribute("data-src", e.source);
    path.setAttribute("data-tgt", e.target);
    path.setAttribute("data-etype", e.type);

    if (isCDA) {{
      path.setAttribute("stroke", "#c8a040");
      path.setAttribute("stroke-width", "1.2");
      path.setAttribute("stroke-dasharray", "6,4");
      path.setAttribute("opacity", "0.7");
      path.setAttribute("marker-end", "url(#arrow-companion)");
      cdaEdgeGrp.appendChild(path);
    }} else if (e.type === "prereq") {{
      path.setAttribute("stroke", "#4a90d9");
      path.setAttribute("stroke-width", "1.4");
      path.setAttribute("opacity", "0.55");
      path.setAttribute("marker-end", "url(#arrow-prereq)");
      prereqGrp.appendChild(path);
    }} else {{
      path.setAttribute("stroke", "#8888aa");
      path.setAttribute("stroke-width", "0.8");
      path.setAttribute("stroke-dasharray", "5,4");
      path.setAttribute("opacity", "0.35");
      path.setAttribute("marker-end", "url(#arrow-companion)");
      companionGrp.appendChild(path);
    }}
  }});
}}

// ============================================================
// RENDER NODES
// ============================================================
function renderNodes() {{
  const grp = document.getElementById("nodes-group");
  grp.innerHTML = "";

  // Collect tracks per column for group labels
  const colTracks = {{}};
  NODES.forEach(n => {{
    if (!colTracks[n.col]) colTracks[n.col] = {{}};
    if (!colTracks[n.col][n.track]) {{
      colTracks[n.col][n.track] = n.y;  // y of first node in group
    }}
  }});

  // Draw track group labels
  const labGrp = document.getElementById("labels-group");
  labGrp.innerHTML = "";
  for (const [col, tracks] of Object.entries(colTracks)) {{
    for (const [track, topY] of Object.entries(tracks)) {{
      // Find x from the first node in this (col, track) group
      const sample = NODES.find(n => String(n.col) === col && n.track === track);
      if (!sample) continue;
      const lbl = document.createElementNS("http://www.w3.org/2000/svg","text");
      lbl.setAttribute("x", sample.x);
      lbl.setAttribute("y", topY - 5);
      lbl.setAttribute("fill", "#2a4a60");
      lbl.setAttribute("font-size", "8");
      lbl.setAttribute("font-family", "Courier New, monospace");
      lbl.setAttribute("letter-spacing", "0.5");
      lbl.textContent = track;
      labGrp.appendChild(lbl);
    }}
  }}

  // Draw nodes
  NODES.forEach(n => {{
    const g = document.createElementNS("http://www.w3.org/2000/svg","g");
    g.setAttribute("data-id", n.id);
    g.setAttribute("class", n.type === "CDA" ? "node-grp cda-node" : "node-grp");
    g.style.cursor = "pointer";

    const rect = document.createElementNS("http://www.w3.org/2000/svg","rect");
    rect.setAttribute("x", n.x);
    rect.setAttribute("y", n.y);
    rect.setAttribute("width",  NODE_W);
    rect.setAttribute("height", NODE_H);
    rect.setAttribute("rx", "4");
    rect.setAttribute("ry", "4");
    rect.setAttribute("fill", TYPE_COLOR[n.type] || "#333");
    rect.setAttribute("stroke", "#ffffff22");
    rect.setAttribute("stroke-width", "0.5");
    g.appendChild(rect);

    // Node label (split on newline)
    const lines = n.label.split("\\n");
    const isBold = (n.type === "TM" || n.type === "CG");
    const fontSize = lines.length > 1 ? 9.5 : 10.5;
    const lineH = 11;
    const totalH = lines.length * lineH;
    const startY = n.y + NODE_H / 2 - totalH / 2 + lineH * 0.75;

    lines.forEach((line, i) => {{
      const txt = document.createElementNS("http://www.w3.org/2000/svg","text");
      txt.setAttribute("x", n.x + NODE_W / 2);
      txt.setAttribute("y", startY + i * lineH);
      txt.setAttribute("text-anchor", "middle");
      txt.setAttribute("fill", "#ffffff");
      txt.setAttribute("font-size", fontSize);
      txt.setAttribute("font-family", "Courier New, monospace");
      if (isBold) txt.setAttribute("font-weight", "bold");
      txt.style.pointerEvents = "none";
      txt.textContent = line;
      g.appendChild(txt);
    }});

    // Hover events
    g.addEventListener("mouseenter", (e) => showTooltip(n, e));
    g.addEventListener("mousemove",  (e) => moveTooltip(e));
    g.addEventListener("mouseleave", hideTooltip);

    // Click → navigate to file
    g.addEventListener("click", () => {{
      if (n.path) window.open(n.path, "_blank");
    }});

    if (n.type === "CDA") {{
      document.getElementById("cda-nodes-grp").appendChild(g);
    }} else {{
      grp.appendChild(g);
    }}
  }});
}}

// ============================================================
// TOOLTIP
// ============================================================
const tooltip = document.getElementById("tooltip");

function showTooltip(node, e) {{
  const prereqs    = prereqsOf[node.id]  || [];
  const deps       = dependents[node.id] || [];
  const companions = EDGES
    .filter(ed => ed.type === "companion" &&
                  (ed.source === node.id || ed.target === node.id))
    .map(ed => ed.source === node.id ? ed.target : ed.source)
    .filter((v,i,a) => a.indexOf(v) === i);

  let html = `<div class="tt-title">${{node.label.replace("\\n"," ")}}</div>`;
  html += `<div class="tt-path">maven_training/${{node.path}}</div>`;
  html += `<div>Type: <span style="color:#80c8ff">${{node.type}}</span> &nbsp;|&nbsp; Track: <span style="color:#80c8ff">${{node.track}}</span></div>`;

  if (prereqs.length) {{
    html += `<div class="tt-section">PREREQS (${{prereqs.length}}):</div>`;
    prereqs.slice(0,8).forEach(id => {{
      const n2 = nodeById[id];
      html += `<div class="tt-item">→ ${{n2 ? n2.label.replace("\\n"," ") : id}}</div>`;
    }});
    if (prereqs.length > 8) html += `<div class="tt-item">… +${{prereqs.length-8}} more</div>`;
  }}
  if (deps.length) {{
    html += `<div class="tt-section">REQUIRED BY (${{deps.length}}):</div>`;
    deps.slice(0,6).forEach(id => {{
      const n2 = nodeById[id];
      html += `<div class="tt-item">← ${{n2 ? n2.label.replace("\\n"," ") : id}}</div>`;
    }});
    if (deps.length > 6) html += `<div class="tt-item">… +${{deps.length-6}} more</div>`;
  }}
  if (companions.length) {{
    html += `<div class="tt-section">COMPANION REFS (${{companions.length}}):</div>`;
    companions.slice(0,6).forEach(id => {{
      const n2 = nodeById[id];
      html += `<div class="tt-item">↔ ${{n2 ? n2.label.replace("\\n"," ") : id}}</div>`;
    }});
  }}

  tooltip.innerHTML = html;
  tooltip.style.display = "block";
  moveTooltip(e);

  // Highlight connected edges
  highlightNode(node.id);
}}

function moveTooltip(e) {{
  const rect = container.getBoundingClientRect();
  let tx = e.clientX - rect.left + 14;
  let ty = e.clientY - rect.top  - 10;
  // Clamp to container
  if (tx + 340 > rect.width)  tx = e.clientX - rect.left - 350;
  if (ty + 200 > rect.height) ty = e.clientY - rect.top  - 210;
  tooltip.style.left = tx + "px";
  tooltip.style.top  = ty + "px";
}}

function hideTooltip() {{
  tooltip.style.display = "none";
  clearHighlight();
}}

// ============================================================
// HIGHLIGHT
// ============================================================
function highlightNode(nodeId) {{
  // Dim all edges, highlight connected ones
  const allPaths = document.querySelectorAll("#edges-prereq-group path, #edges-companion-group path");
  allPaths.forEach(p => {{
    const src = p.getAttribute("data-src");
    const tgt = p.getAttribute("data-tgt");
    if (src === nodeId || tgt === nodeId) {{
      p.setAttribute("opacity", "0.95");
      p.setAttribute("stroke-width", p.getAttribute("data-etype") === "companion" ? "1.4" : "2.2");
    }} else {{
      p.setAttribute("opacity", "0.08");
    }}
  }});

  // Dim non-connected nodes
  const allNodes = document.querySelectorAll(".node-grp");
  const connected = new Set([nodeId]);
  EDGES.forEach(e => {{
    if (e.source === nodeId) connected.add(e.target);
    if (e.target === nodeId) connected.add(e.source);
  }});
  allNodes.forEach(g => {{
    const id = g.getAttribute("data-id");
    g.setAttribute("opacity", connected.has(id) ? "1" : "0.2");
  }});
}}

function clearHighlight() {{
  document.querySelectorAll("#edges-prereq-group path, #edges-companion-group path")
    .forEach(p => {{
      p.setAttribute("opacity", p.getAttribute("data-etype") === "prereq" ? "0.55" : "0.35");
      p.setAttribute("stroke-width", p.getAttribute("data-etype") === "prereq" ? "1.4" : "0.8");
    }});
  document.querySelectorAll(".node-grp").forEach(g => g.setAttribute("opacity","1"));
}}

// ============================================================
// TOGGLE EDGES
// ============================================================
function toggleEdges() {{
  const showPrereq    = document.getElementById("chk-prereq").checked;
  const showCompanion = document.getElementById("chk-companion").checked;
  document.getElementById("edges-prereq-group").style.display    = showPrereq    ? "" : "none";
  document.getElementById("edges-companion-group").style.display = showCompanion ? "" : "none";
}}

// ============================================================
// CDA OVERLAY TOGGLE
// ============================================================
function toggleCDA() {{
  const show = document.getElementById("chk-cda").checked;
  document.getElementById("cda-group").style.display = show ? "" : "none";
}}

// ============================================================
// AUDIENCE FILTER
// ============================================================
function applyAudienceFilter() {{
  const showUser    = document.getElementById("chk-aud-user").checked;
  const showTrainer = document.getElementById("chk-aud-trainer").checked;
  const showDev     = document.getElementById("chk-aud-dev").checked;
  const showSpec    = document.getElementById("chk-aud-spec").checked;

  document.querySelectorAll(".node-grp").forEach(g => {{
    const node = nodeById[g.getAttribute("data-id")];
    if (!node) return;
    const aud = node.aud || [];
    const isSpec = aud.includes("specialist");
    let visible = false;
    // Base visibility: any checked audience tag grants access
    if (showUser    && aud.includes("user"))    visible = true;
    if (showTrainer && aud.includes("trainer")) visible = true;
    if (showDev     && aud.includes("dev"))     visible = true;
    if (showSpec    && isSpec)                  visible = true;
    // Specialist override: always hide specialist nodes when Specialist is unchecked
    if (isSpec && !showSpec) visible = false;
    g.setAttribute("opacity", visible ? "1" : "0.05");
  }});
  fitView(50);
}}

// ============================================================
// SEARCH
// ============================================================
let searchTimeout = null;
function handleSearch(val) {{
  clearTimeout(searchTimeout);
  searchTimeout = setTimeout(() => applySearch(val.trim().toLowerCase()), 150);
}}

function applySearch(term) {{
  const allNodes = document.querySelectorAll(".node-grp");
  if (!term) {{
    allNodes.forEach(g => {{
      g.setAttribute("opacity","1");
      const r = g.querySelector("rect");
      if (r) r.setAttribute("filter","");
    }});
    return;
  }}
  allNodes.forEach(g => {{
    const id    = g.getAttribute("data-id").toLowerCase();
    const node  = nodeById[g.getAttribute("data-id")];
    const label = node ? node.label.toLowerCase() : "";
    const path  = node ? node.path.toLowerCase()  : "";
    const match = id.includes(term) || label.includes(term) || path.includes(term);
    g.setAttribute("opacity", match ? "1" : "0.1");
    const r = g.querySelector("rect");
    if (r) r.setAttribute("filter", match ? "url(#highlight-glow)" : "");
  }});
}}

// ============================================================
// TIER HEADER BANDS (horizontal bands with layman names)
// ============================================================
function renderTierHeaders() {{
  const labGrp = document.getElementById("labels-group");

  // Canvas background
  const bg = document.createElementNS("http://www.w3.org/2000/svg","rect");
  bg.setAttribute("x","0"); bg.setAttribute("y","0");
  bg.setAttribute("width",{SVG_W}); bg.setAttribute("height",{SVG_H});
  bg.setAttribute("fill","#0d1b2a");
  labGrp.insertBefore(bg, labGrp.firstChild);

  // Compute tier y-extents from NODES
  const tierMinY = {{}}, tierMaxY = {{}};
  NODES.forEach(n => {{
    const t = String(n.col);
    if (tierMinY[t] === undefined || n.y < tierMinY[t]) tierMinY[t] = n.y;
    const bot = n.y + NODE_H;
    if (tierMaxY[t] === undefined || bot > tierMaxY[t]) tierMaxY[t] = bot;
  }});

  const tierColors = {{
    "-1": "#0a180a",
    "0":  "#0c1c2a", "1": "#0e1f2e", "2": "#0c1c2a",
    "3":  "#0e1f2e", "4": "#0c1c2a", "5": "#0e1f2e",
  }};

  for (const [tier, label] of Object.entries(TIER_HEADERS)) {{
    if (tierMinY[tier] === undefined) continue;
    const yTop    = tierMinY[tier] - 30;
    const yBot    = tierMaxY[tier] + 14;
    const isCDA   = tier === "-1";
    const isTMGMT = false; // sidebar handled separately

    // Band background
    const band = document.createElementNS("http://www.w3.org/2000/svg","rect");
    band.setAttribute("x","0");
    band.setAttribute("y", yTop);
    band.setAttribute("width", {SVG_W});
    band.setAttribute("height", yBot - yTop);
    band.setAttribute("fill", tierColors[tier] || "#0d1b2a");
    labGrp.appendChild(band);

    // Top separator line
    const sep = document.createElementNS("http://www.w3.org/2000/svg","line");
    sep.setAttribute("x1","0"); sep.setAttribute("y1", yTop);
    sep.setAttribute("x2",{SVG_W}); sep.setAttribute("y2", yTop);
    sep.setAttribute("stroke", isCDA ? "#1a3a10" : "#1e3a50");
    sep.setAttribute("stroke-width","1");
    sep.setAttribute("stroke-dasharray","none");
    labGrp.appendChild(sep);

    // Tier label (layman name) — left-aligned, inside band above nodes
    const txt = document.createElementNS("http://www.w3.org/2000/svg","text");
    txt.setAttribute("x","34");
    txt.setAttribute("y", yTop + 18);
    txt.setAttribute("fill", isCDA ? "#4a8a40" : "#3a6a90");
    txt.setAttribute("font-size","11");
    txt.setAttribute("font-family","Courier New,monospace");
    txt.setAttribute("font-weight","bold");
    txt.setAttribute("letter-spacing","1.5");
    txt.textContent = label;
    labGrp.appendChild(txt);
  }}
}}

// ============================================================
// INIT
// ============================================================
renderTierHeaders();
renderEdges();
renderNodes();
relayout();
resetView();
</script>
</body>
</html>
"""

# Write output
out_dir = Path(__file__).resolve().parent.parent / "maven_training"
out_path = out_dir / "DEPENDENCY_MAP_summary.html"  # DO NOT change to DEPENDENCY_MAP.html — that is the real 7400+ line dep map
out_path.write_text(HTML, encoding="utf-8")
print(f"Written: {out_path}")
print(f"File size: {out_path.stat().st_size / 1024:.1f} KB")
