#!/usr/bin/env python3
"""
Generate all synthetic training datasets for Maven Builder Training exercises.
Run from repo root: python scripts/generate_training_data.py
Outputs go into maven_training/exercises/EX-*/training_data/
"""

import csv
import json
import math
import os
import random
import textwrap
from datetime import date, timedelta

random.seed(42)  # Reproducible output

BASE = os.path.join(os.path.dirname(__file__), "..", "maven_training", "exercises")

def makedirs(path):
    os.makedirs(path, exist_ok=True)

def write_csv(path, fieldnames, rows):
    with open(path, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(rows)

def daterange(start, n_days):
    return [start + timedelta(days=i) for i in range(n_days)]

# ── EX-10: BCT Readiness ─────────────────────────────────────────────────────
def gen_ex10():
    out = os.path.join(BASE, "EX-10_operator_basics", "training_data")
    makedirs(out)
    start = date(2025, 9, 1)
    units = {
        "Unit_A": (85.0, 2.5),   # mean ~85%, small variance
        "Unit_B": (62.0, 3.5),   # anomaly — lowest readiness
        "Unit_C": (91.0, 1.8),   # highest readiness
    }
    categories = ["Motor Pool", "Comms", "Aviation", "Weapons"]
    steward = "training.poc@army.mil"
    rows = []
    for d in daterange(start, 90):
        for unit, (mean, std) in units.items():
            for cat in categories:
                # Unit B / Motor Pool is the designed anomaly
                cat_mod = -12.0 if (unit == "Unit_B" and cat == "Motor Pool") else 0.0
                pct = round(min(100.0, max(0.0, random.gauss(mean + cat_mod, std))), 1)
                rows.append({
                    "date": d.isoformat(),
                    "unit": unit,
                    "equipment_category": cat,
                    "readiness_pct": pct,
                    "data_steward": steward,
                    "last_updated": d.isoformat() + "T08:00:00Z",
                })
    write_csv(os.path.join(out, "EX-10_BCT_Readiness_Training_Data.csv"),
              ["date","unit","equipment_category","readiness_pct","data_steward","last_updated"], rows)
    print(f"  EX-10: {len(rows)} rows")

# ── EX-20: Vehicle Availability ───────────────────────────────────────────────
def gen_ex20():
    out = os.path.join(BASE, "EX-20_no_code_builder", "training_data")
    makedirs(out)
    start = date(2025, 9, 1)
    companies = ["A","B","C","D"]
    v_classes = ["wheeled","tracked"]
    rows = []
    baselines = {"A": 82.0, "B": 74.0, "C": 88.0, "D": 69.0}
    for d in daterange(start, 90):
        for co in companies:
            for vc in v_classes:
                offset = -5.0 if vc == "tracked" else 0.0
                pct = round(min(100.0, max(0.0, random.gauss(baselines[co] + offset, 3.0))), 1)
                rows.append({"date": d.isoformat(), "company": co,
                             "vehicle_class": vc, "availability_pct": pct})
    write_csv(os.path.join(out, "EX-20_Vehicle_Availability_Training_Data.csv"),
              ["date","company","vehicle_class","availability_pct"], rows)
    print(f"  EX-20: {len(rows)} rows")

# ── EX-30: SIGACT Analog ──────────────────────────────────────────────────────
def gen_ex30():
    out = os.path.join(BASE, "EX-30_advanced_builder", "training_data")
    makedirs(out)
    start = date(2025, 9, 1)
    event_types = ["IED","Patrol Contact","Observation","Cache","Other"]
    units = ["1-1 BN","1-2 BN","1-3 BN","2-1 BN","DIV CAV"]
    rows = []
    eid = 1
    for d in daterange(start, 60):
        n = random.randint(1, 4)
        for _ in range(n):
            lat = round(random.uniform(48.2, 49.8), 5)
            lon = round(random.uniform(7.5, 9.5), 5)
            unit = random.choice(units)
            rows.append({
                "event_id": f"EVT-{eid:04d}",
                "date": d.isoformat(),
                "lat": lat,
                "lon": lon,
                "event_type": random.choice(event_types),
                "unit": unit,
            })
            eid += 1

    # Inject 5 duplicate event_ids (reuse IDs 1–5)
    for i in range(1, 6):
        dup = dict(rows[i - 1])
        dup["date"] = (start + timedelta(days=45 + i)).isoformat()
        rows.append(dup)

    # Inject 3 null unit values
    for i in [10, 22, 35]:
        rows[i]["unit"] = None

    # Inject 2 null coordinate pairs
    for i in [7, 18]:
        rows[i]["lat"] = None
        rows[i]["lon"] = None

    # Pre-create completeness_flag column (empty — participants populate via AIP Logic)
    for r in rows:
        r["completeness_flag"] = ""

    write_csv(os.path.join(out, "EX-30_SIGACT_Analog_Training_Data.csv"),
              ["event_id","date","lat","lon","event_type","unit","completeness_flag"], rows)
    print(f"  EX-30: {len(rows)} rows (incl. 5 dupes, 3 null unit, 2 null coords)")

# ── EX-40F: BCT Ops Package ───────────────────────────────────────────────────
def gen_ex40f():
    out = os.path.join(BASE, "EX-40F_mission_command", "training_data",
                       "EX-40F_BCT_Ops_Training_Data")
    makedirs(out)
    start = date(2025, 9, 1)

    # unit_positions.geojson — 3 battalions with notional positions near Grafenwöhr, DE
    positions = {
        "1-1_BN": (49.6821, 11.9308),
        "1-2_BN": (49.7150, 11.8900),
        "1-3_BN": (49.6500, 11.9600),
    }
    geojson = {
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "properties": {"battalion": bn, "label": bn.replace("_"," ")},
                "geometry": {"type": "Point", "coordinates": [lon, lat]},
            }
            for bn, (lat, lon) in positions.items()
        ]
    }
    with open(os.path.join(out, "unit_positions.geojson"), "w") as f:
        json.dump(geojson, f, indent=2)

    # readiness_status.csv — daily per battalion, 30 days
    # 1-1: ~80%, 1-2: ~67% (below 70% threshold), 1-3: ~91%
    readiness_rows = []
    profiles = {"1-1_BN": (80.0, 2.5), "1-2_BN": (67.0, 2.0), "1-3_BN": (91.0, 1.5)}
    for d in daterange(start, 30):
        for bn, (mean, std) in profiles.items():
            readiness_rows.append({
                "date": d.isoformat(),
                "battalion": bn,
                "personnel_pct": round(min(100, max(0, random.gauss(mean + 5, std))), 1),
                "equip_pct": round(min(100, max(0, random.gauss(mean, std))), 1),
                "last_updated": d.isoformat() + "T06:00:00Z",
            })
    write_csv(os.path.join(out, "readiness_status.csv"),
              ["date","battalion","personnel_pct","equip_pct","last_updated"], readiness_rows)

    # operational_events.csv — 30 days, at least 1 event inside CCIR 2 sensitivity area
    # CCIR 2 area: Lat 48.5–49.5 N, Lon 8.0–9.0 E
    event_types = ["Patrol Contact","Observation","SIGACT","Cache","Admin"]
    op_rows = []
    eid = 1
    for d in daterange(start, 30):
        n = random.randint(0, 3)
        for _ in range(n):
            lat = round(random.uniform(49.0, 50.0), 5)
            lon = round(random.uniform(10.5, 12.5), 5)
            op_rows.append({"event_id": f"OPS-{eid:04d}", "date": d.isoformat(),
                            "lat": lat, "lon": lon,
                            "event_type": random.choice(event_types)})
            eid += 1
    # Inject CCIR 2 trigger event on day 8
    op_rows.append({"event_id": "OPS-CCIR2", "date": (start + timedelta(days=7)).isoformat(),
                    "lat": 49.0, "lon": 8.5, "event_type": "Patrol Contact"})
    write_csv(os.path.join(out, "operational_events.csv"),
              ["event_id","date","lat","lon","event_type"], op_rows)

    # personnel_strength.csv — 1-3 BN at 82% (below 85% — CCIR 3)
    strength_profiles = {"1-1_BN": (88.0, 1.5), "1-2_BN": (76.0, 2.0), "1-3_BN": (82.0, 1.8)}
    str_rows = []
    for d in daterange(start, 30):
        for bn, (mean, std) in strength_profiles.items():
            str_rows.append({"date": d.isoformat(), "battalion": bn,
                             "strength_pct": round(min(100, max(0, random.gauss(mean, std))), 1)})
    write_csv(os.path.join(out, "personnel_strength.csv"),
              ["date","battalion","strength_pct"], str_rows)

    print(f"  EX-40F: geojson + {len(readiness_rows)} readiness + "
          f"{len(op_rows)} ops events + {len(str_rows)} strength rows")

# ── EX-40G: PMCS Readiness (ORSA) ────────────────────────────────────────────
def gen_ex40g():
    out = os.path.join(BASE, "EX-40G_orsa", "training_data")
    makedirs(out)
    start = date(2025, 3, 1)
    equipment_classes = ["wheeled","tracked","aviation","comms"]
    # Battalion baselines with designed trends
    rows = []
    for i, d in enumerate(daterange(start, 180)):
        week = i / 7.0
        for eq in equipment_classes:
            # Aviation has highest variance (answer key: Task 1)
            variance = {"wheeled": 2.0, "tracked": 2.5, "aviation": 8.0, "comms": 1.5}[eq]
            # Battalion A: steady improving (+0.3%/week)
            a_base = 72.0 + 0.3 * week + random.gauss(0, variance)
            # Battalion B: flat, high variance (poor R² expected)
            b_base = 75.0 + random.gauss(0, variance * 2.5)
            # Battalion C: slow degrading (-0.2%/week)
            c_base = 82.0 - 0.2 * week + random.gauss(0, variance)
            for bn, val in [("Battalion_A", a_base), ("Battalion_B", b_base), ("Battalion_C", c_base)]:
                rows.append({"date": d.isoformat(), "battalion": bn,
                             "equipment_class": eq,
                             "readiness_pct": round(min(100.0, max(0.0, val)), 2)})
    write_csv(os.path.join(out, "EX-40G_PMCS_Training_Data.csv"),
              ["date","battalion","equipment_class","readiness_pct"], rows)
    print(f"  EX-40G: {len(rows)} rows")

# ── EX-40H: INTSUM Corpus ─────────────────────────────────────────────────────
INTSUM_TEMPLATES = [
    ("PATROL_CONTACT",
     "INTSUM {id} — PATROL CONTACT\nDTG: {dtg}\nUnit: {unit}\n\n"
     "Summary: Elements of {unit} conducted a patrol in grid {grid}. "
     "At approximately {time} local, the patrol encountered a small dismounted element "
     "moving along the {road} road. The element dispersed upon visual contact. "
     "No shots fired. Grid coordinates recorded. Report forwarded to S2 for pattern analysis.\n\n"
     "Significant Events: One patrol contact, no casualties, no weapons observed.\n"
     "Recommended Action: Monitor for pattern activity along {road} corridor. "
     "Increase patrol frequency in grid {grid} during period {period}."),

    ("IED_EVENT",
     "INTSUM {id} — IED EVENT\nDTG: {dtg}\nUnit: {unit}\n\n"
     "Summary: At {time} local, a suspected IED was identified by route clearance element "
     "in grid {grid} along {road}. EOD requested and responded within {response_time} minutes. "
     "Device rendered safe. No personnel casualties. Vehicle sustained minor damage.\n\n"
     "Device Description: Pressure-plate initiator, command wire, approx 5kg charge. "
     "Collected for exploitation. DNA swabs taken.\n"
     "Recommended Action: Restrict movement along {road} until EOD clearance complete. "
     "Disseminate grid data to adjacent units."),

    ("CACHE_DISCOVERY",
     "INTSUM {id} — CACHE DISCOVERY\nDTG: {dtg}\nUnit: {unit}\n\n"
     "Summary: During area reconnaissance, elements of {unit} discovered a concealed cache "
     "in grid {grid}. Contents included small arms ammunition, field rations, and communications "
     "equipment. Cache photographed, inventoried, and destroyed in place per SOP.\n\n"
     "Exploitation: Items photographed and catalogued. Serial numbers recorded where legible. "
     "No biometrics collected — gloves worn.\n"
     "Recommended Action: Submit cache report to higher S2. "
     "Conduct expanded search in 500m radius."),

    ("OBSERVATION_REPORT",
     "INTSUM {id} — OBSERVATION REPORT\nDTG: {dtg}\nUnit: {unit}\n\n"
     "Summary: OP {op_name} reported observation of {vehicle_count} unidentified vehicles "
     "moving in convoy formation along {road} at {time} local. "
     "Vehicles: {vehicle_type}. Movement direction: {direction}. "
     "No hostile action observed. Convoy cleared the AO within 22 minutes.\n\n"
     "Assessment: Likely civilian logistics movement. Pattern consistent with previous Thursday "
     "observations. Does not meet CCIR threshold at this time.\n"
     "Recommended Action: Continue monitoring. Report if vehicle type or pattern changes."),

    ("ADMIN",
     "INTSUM {id} — ADMINISTRATIVE UPDATE\nDTG: {dtg}\nUnit: {unit}\n\n"
     "Summary: No significant intelligence activity reported during this period. "
     "Routine patrol activity conducted in grids {grid} and {grid2}. "
     "All personnel returned to FOB without incident.\n\n"
     "Personnel Status: All elements accounted for. No medical events.\n"
     "Equipment Status: All vehicles operational. Radio checks completed on schedule.\n"
     "Recommended Action: Continue routine patrol posture. "
     "Next INTSUM due at {next_dtg}."),
]

def gen_ex40h():
    corpus_out = os.path.join(BASE, "EX-40H_ai_engineer", "training_data", "EX-40H_INTSUM_Corpus")
    makedirs(corpus_out)

    units = ["1-1 BN","1-2 BN","1-3 BN","2-1 BN","DIV CAV","1-4 BN","2-2 BN"]
    roads = ["ROUTE IRON","ROUTE COPPER","ROUTE AMBER","ROUTE DELTA","ROUTE GOLD"]
    directions = ["NORTH","SOUTH","EAST","WEST","NORTHWEST","NORTHEAST"]
    v_types = ["MTVR","LMTV","FMTV","HET","Unknown wheeled"]
    op_names = ["OP EAGLE","OP HAWK","OP VIPER","OP WOLF","OP RAVEN"]

    ground_truth_types = ["PATROL_CONTACT","IED_EVENT","CACHE_DISCOVERY",
                          "OBSERVATION_REPORT","ADMIN"]
    gt_rows = []
    doc_records = []  # for dataset representation (doc_id, date, content)

    # Generate 30 documents (reduced from 200 for tractability; real corpus would be generated same way)
    n_docs = 30
    start = date(2025, 6, 1)
    selected_gt_ids = []  # first 10 will be ground truth

    for i in range(1, n_docs + 1):
        d = start + timedelta(days=random.randint(0, 180))
        template_event, template_text = random.choice(INTSUM_TEMPLATES)
        dtg = d.strftime("%d%H%MZ %b %Y").upper()
        doc_id = f"INTSUM_{d.strftime('%Y%m%d')}_{i:03d}"
        grid = f"{random.randint(32,37)}T{random.randint(100000,999999)}"
        content = template_text.format(
            id=doc_id, dtg=dtg, unit=random.choice(units),
            time=f"{random.randint(6,22):02d}{random.randint(0,5)*10:02d}",
            road=random.choice(roads), grid=grid,
            grid2=f"{random.randint(32,37)}T{random.randint(100000,999999)}",
            period=f"0600-1800",
            response_time=random.randint(12, 45),
            vehicle_count=random.randint(3,12),
            vehicle_type=random.choice(v_types),
            direction=random.choice(directions),
            op_name=random.choice(op_names),
            next_dtg=(d + timedelta(hours=6)).strftime("%d%H%MZ %b %Y").upper(),
        )
        fname = os.path.join(corpus_out, f"{doc_id}.txt")
        with open(fname, "w") as f:
            f.write(content)
        doc_records.append({"doc_id": doc_id, "date": d.isoformat(), "content": content[:200] + "..."})
        if i <= 10:
            gt_rows.append({"doc_id": doc_id, "event_type": template_event})

    # Write ground truth CSV (10 docs)
    gt_out = os.path.join(BASE, "EX-40H_ai_engineer", "training_data")
    write_csv(os.path.join(gt_out, "EX-40H_GroundTruth_10docs.csv"),
              ["doc_id","event_type"], gt_rows)

    print(f"  EX-40H: {n_docs} INTSUM .txt files + ground truth CSV (10 docs)")

# ── EX-40I: PMCS NMC Classification ──────────────────────────────────────────
def gen_ex40i():
    out = os.path.join(BASE, "EX-40I_ml_engineer", "training_data")
    makedirs(out)
    start = date(2024, 1, 1)
    equipment_classes = ["wheeled","tracked","aviation","comms","engineer"]
    units = ["1-1 BN","1-2 BN","1-3 BN","2-1 BN","DIV CAV","HHC","BSB"]
    eq_id_counter = 1
    rows = []
    n = 5000
    for i in range(n):
        d = start + timedelta(days=random.randint(0, 365))
        eq_id = f"EQ-{eq_id_counter:05d}"
        # Rotate equipment IDs so same equipment appears multiple times
        eq_id_counter = (eq_id_counter % 800) + 1
        eq_class = random.choice(equipment_classes)
        days_since = random.randint(1, 180) if random.random() > 0.05 else None  # ~5% null
        m30 = random.randint(0, 8)
        m60 = m30 + random.randint(0, 6)
        m90 = m60 + random.randint(0, 5)
        # ~10% positive NMC rate overall — slightly higher for aviation + tracked
        base_prob = 0.06
        if eq_class == "aviation":
            base_prob = 0.10
        elif eq_class == "tracked":
            base_prob = 0.08
        if days_since is not None and days_since > 120:
            base_prob += 0.04
        if m30 >= 6:
            base_prob += 0.03
        nmc = random.random() < base_prob
        rows.append({
            "equipment_id": eq_id,
            "date": d.isoformat(),
            "days_since_last_service": days_since,
            "maintenance_count_30d": m30,
            "maintenance_count_60d": m60,
            "maintenance_count_90d": m90,
            "equipment_class": eq_class,
            "unit": random.choice(units),
            "nmc_within_7d": nmc,
        })
    write_csv(os.path.join(out, "EX-40I_PMCS_NMC_Training_Data.csv"),
              ["equipment_id","date","days_since_last_service",
               "maintenance_count_30d","maintenance_count_60d","maintenance_count_90d",
               "equipment_class","unit","nmc_within_7d"], rows)
    pos = sum(1 for r in rows if r["nmc_within_7d"])
    print(f"  EX-40I: {n} rows, {pos} positive NMC ({100*pos/n:.1f}%)")

# ── EX-40J: Project Record Package ───────────────────────────────────────────
def gen_ex40j():
    out = os.path.join(BASE, "EX-40J_program_manager", "training_data",
                       "EX-40J_Project_Record_Package")
    makedirs(out)

    charter = textwrap.dedent("""\
    # EX-40J TRAINING — Project Charter
    ## LOGSTAT Aggregation Pipeline
    Classification: UNCLASSIFIED // TRAINING USE ONLY

    ### Project Overview
    Automate daily aggregation of logistics status (LOGSTAT) reports from three
    battalion-level source systems into a single theater-level dashboard on MSS.
    Currently, S4 staff manually compile LOGSTATs each morning — estimated 2.5 hours/day.

    ### Scope
    - Ingest: 3 source APIs (BSB, FSB, CSSB logistics systems)
    - Transform: Normalize equipment class codes, compute availability percentages
    - Load: Write to theater LOGSTAT dataset on MSS
    - Visualize: Automated dashboard refresh, G4 Viewer access

    ### Stakeholders
    - Sponsor: G4 (COL Harrington)
    - Product Owner: S4 OIC (CPT Delacroix)
    - Technical Lead: Data team PM (participant role)
    - End Users: G4 staff, G3 planners
    - Platform: MSS data team (API access approval required)

    ### Success Criteria
    1. Daily LOGSTAT dashboard available by 0600 without manual intervention
    2. Data latency < 2 hours from source system update
    3. User acceptance testing (UAT) passed by G4 staff
    4. G3-directed delivery date: D+14 (Week 8 of project)

    ### Out of Scope
    - Real-time push (batch daily is acceptable)
    - Source system modifications
    - Historical backfill beyond 90 days

    ### Constraints
    - No direct database access to source systems — API only
    - MSS tenant provisioning required before ingestion build can begin
    - G3-directed deadline is fixed; no scope relief available
    """)

    milestone_tracker = textwrap.dedent("""\
    # EX-40J TRAINING — Milestone Tracker
    ## LOGSTAT Aggregation Pipeline — 8-Week Project Plan
    Classification: UNCLASSIFIED // TRAINING USE ONLY

    Current Week: **6 of 8**
    Last Updated: Week 6 Check-in

    | Week | Milestone | Status | Notes |
    |------|-----------|--------|-------|
    | 1 | Project kickoff; stakeholder alignment | COMPLETE | Charter signed by G4 |
    | 2 | Source API access provisioned (all 3 systems) | COMPLETE | MSS team approved access |
    | 3 | Pipeline skeleton built; ingestion of BSB API tested | COMPLETE | BSB API working |
    | 4 | API integration complete (all 3 sources) | **MISSED** | FSB/CSSB rate-limited — see Ticket #EX40J-007 |
    | 5 | Transform and normalization complete | IN PROGRESS | Blocked on full API access |
    | 6 | Load to MSS dataset; schema validated | IN PROGRESS | Partial — only BSB data |
    | 7 | UAT with G4 end-users | AT RISK | Depends on Week 4/5 completion |
    | 8 | G3 delivery date — dashboard live | DEADLINE | Fixed per G3 OPORD |

    ### Schedule Risk Summary
    - **Critical Path:** Week 4 slip → Week 5 slip → Week 7 UAT at risk → Week 8 deadline at risk
    - **Slip Impact:** If Week 7 UAT is delayed by even 1 week, Week 8 delivery is not achievable in current execution plan
    - **Commander Approval Required:** Yes — any schedule change affecting G3 deadline requires CDR approval

    ### Planned vs. Actual
    | Week | Planned % Complete | Actual % Complete |
    |------|--------------------|-------------------|
    | 1    | 12%                | 12%               |
    | 2    | 25%                | 25%               |
    | 3    | 38%                | 38%               |
    | 4    | 52%                | 35%               |
    | 5    | 65%                | 44%               |
    | 6    | 78%                | 51%               |
    """)

    open_tickets = textwrap.dedent("""\
    # EX-40J TRAINING — Open Tickets
    ## LOGSTAT Aggregation Pipeline
    Classification: UNCLASSIFIED // TRAINING USE ONLY

    ---

    ### Ticket #EX40J-004
    **Title:** BSB API returns inconsistent equipment class codes
    **Priority:** Medium
    **Status:** In Progress
    **Opened:** Week 3
    **Description:** BSB API returns equipment class as free text (e.g., "Wheeled Veh", "wheeled vehicle",
    "WHEELED") — normalization transform handles ~90% of cases but edge cases remain.
    **Action Required:** Add additional normalization rules; run against full 90-day backfill to validate.

    ---

    ### Ticket #EX40J-007 ← CRITICAL BLOCKER
    **Title:** FSB and CSSB APIs rate-limited — cannot complete integration
    **Priority:** HIGH — SCHEDULE BLOCKER
    **Status:** Open — No resolution
    **Opened:** Week 4
    **Description:** FSB and CSSB logistics APIs are rate-limited to 100 requests/hour.
    The pipeline as designed requires approximately 2,000 requests/hour to ingest
    all equipment records within the 2-hour latency window.
    Current status: Integration halted. Week 4 milestone missed as a result.
    **Downstream Impact:** Week 5 transform incomplete, Week 7 UAT delayed, Week 8 deadline at risk.
    **Action Required:** Identify workaround or escalate to source system owners for rate limit increase.
    Note: A batched overnight run approach has not yet been evaluated.

    ---

    ### Ticket #EX40J-011
    **Title:** MSS dataset schema validation — null handling
    **Priority:** Low
    **Status:** Open
    **Opened:** Week 6
    **Description:** When source record has null equipment_available field, the load step
    fails silently (writes null instead of defaulting to 0). Affects dashboard readiness %
    calculation for records with incomplete data.
    **Action Required:** Add null coalesce in transform; rerun BSB backfill after fix.

    ---

    ### Ticket #EX40J-015
    **Title:** Dashboard date filter default shows last 7 days — G4 wants last 30
    **Priority:** Low
    **Status:** Open
    **Opened:** Week 6
    **Description:** Minor UX issue. G4 POC prefers 30-day default view.
    **Action Required:** Update Workshop dashboard default filter after UAT.
    """)

    pipeline_def = textwrap.dedent("""\
    # EX-40J TRAINING — Pipeline Definition
    ## LOGSTAT Aggregation Pipeline — Technical Description
    Classification: UNCLASSIFIED // TRAINING USE ONLY

    ### What It Does
    This pipeline ingests daily logistics status (LOGSTAT) data from three battalion-level
    source systems, normalizes the data to a common schema, and loads it into the theater
    LOGSTAT dataset on MSS for G4 dashboard consumption.

    ### Tech Stack
    - **Platform:** MSS (Maven Smart System) Python Transforms
    - **Ingestion:** REST API calls to BSB, FSB, CSSB logistics systems
    - **Transform:** Python (pandas) — normalization, null handling, deduplication
    - **Load:** Foundry Output dataset (overwrite daily)
    - **Visualization:** Workshop dashboard (G4 Viewer access)

    ### Source Systems
    | System | Owner | API Type | Auth | Rate Limit |
    |--------|-------|----------|------|------------|
    | BSB Logistics API | BSB S4 | REST/JSON | API Key | 10,000 req/hr |
    | FSB Logistics API | FSB S4 | REST/JSON | API Key | 100 req/hr ← BLOCKER |
    | CSSB Logistics API | CSSB S4 | REST/JSON | API Key | 100 req/hr ← BLOCKER |

    ### Output Schema
    | Field | Type | Description |
    |-------|------|-------------|
    | report_date | DATE | Date of LOGSTAT report |
    | battalion | STRING | Unit identifier |
    | equipment_class | STRING | Normalized equipment category |
    | equipment_total | INT | Total equipment in class |
    | equipment_available | INT | Available (not NMC) |
    | availability_pct | FLOAT | available / total × 100 |
    | source_system | STRING | Which API provided this record |
    | ingested_at | TIMESTAMP | Pipeline run timestamp |

    ### Run Schedule
    - Daily at 0400 local (to produce dashboard ready by 0600)
    - Triggered by MSS scheduler
    - Retry: 2 attempts on failure, then alert to data team

    ### Known Issues
    - See open tickets #EX40J-004, #EX40J-007 (critical), #EX40J-011, #EX40J-015
    """)

    for fname, content in [
        ("project_charter.md", charter),
        ("milestone_tracker.md", milestone_tracker),
        ("open_tickets.md", open_tickets),
        ("pipeline_definition.md", pipeline_def),
    ]:
        with open(os.path.join(out, fname), "w") as f:
            f.write(content)
    print("  EX-40J: 4 project record files")

# ── EX-40K: AAR Backlog ───────────────────────────────────────────────────────
AAR_OBSERVATIONS = [
    ("COMMAND_AND_CONTROL", "H",
     "Command post communications experienced 45-minute outage during EXORD execution due to "
     "generator failure. No backup power source was pre-positioned.",
     "Pre-position a backup generator and conduct weekly power-off drills for CP equipment."),
    ("SUSTAINMENT", "H",
     "Class III(B) resupply convoy was delayed 6 hours due to route clearance not being "
     "synchronized with the maneuver plan.",
     "Integrate route clearance into the logistics synchronization matrix during MDMP."),
    ("FIRES", "M",
     "Fire mission processing times averaged 18 minutes — above the 10-minute standard. "
     "Contributing factor: paper-based call-for-fire during digital system outage.",
     "Conduct quarterly analog fire mission drills to maintain proficiency independent of digital systems."),
    ("INTELLIGENCE", "H",
     "ISR assets were not properly integrated into the R&S plan. Two named areas of interest "
     "had no coverage during the critical 6-hour window before H-hour.",
     "Assign ISR assets to NAIs during MDMP and validate coverage in the collection plan."),
    ("MOVEMENT_AND_MANEUVER", "M",
     "Lead element crossed the LD 22 minutes late due to last-minute vehicle maintenance failure. "
     "No vehicle recovery asset was forward-positioned.",
     "Position recovery assets at the LD no later than H-2. Add vehicle status check to D-1 REDCON brief."),
    ("PROTECTION", "H",
     "Force protection measures at the patrol base were not established IAW the OPORD. "
     "Perimeter sectors were not assigned in writing.",
     "Sector sketches and range cards must be completed and submitted to the CP within 30 minutes of occupation."),
    ("COMMAND_AND_CONTROL", "H",  # Record #7 — CONFLICT on radio frequency deconfliction
     "During joint operations with adjacent unit, radio frequency deconfliction was ad hoc and "
     "resulted in two units transmitting on the same frequency simultaneously for 11 minutes.",
     "Assign frequency blocks by echelon in the OPORD; do not allow ad hoc frequency coordination."),
    ("SUSTAINMENT", "L",
     "LOGSTAT submissions were consistently 2 hours late. S4 staff cited difficulty aggregating "
     "data from subordinate units using the manual reporting process.",
     "Implement digital LOGSTAT collection tool and establish a hard cutoff time for subordinate submissions."),
    ("FIRES", "M",
     "Suppression of enemy air defense (SEAD) was not properly synchronized with the air assault. "
     "Attack helicopter ingress route passed through an uncleared air corridor.",
     "Include SEAD timing and air corridor deconfliction in the air mission brief and synchronization matrix."),
    ("INTELLIGENCE", "M",
     "Debriefs for returning patrols were inconsistently conducted. Patrol leaders reported "
     "contact but the information was not formally entered into the intelligence system.",
     "Standardize debrief SOP and require digital entry into the intel system within 1 hour of patrol return."),
    ("MOVEMENT_AND_MANEUVER", "H",
     "Two vehicle crews became disoriented during night navigation. GPS systems were not "
     "programmed with waypoints before movement.",
     "Require a pre-movement check that includes GPS programming verification by the platoon sergeant."),
    ("PROTECTION", "M",
     "Chemical alarm maintenance was overdue for 3 of 8 units inspected. No tracking system "
     "was in place for sensor calibration dates.",
     "Establish a unit-level CBRN equipment maintenance tracker with 30-day calibration reminders."),
    ("SUSTAINMENT", "H",
     "Medical evacuation was delayed 34 minutes because the 9-line MEDEVAC was submitted "
     "over voice with errors. Requestor had not practiced the format.",
     "Include 9-line MEDEVAC drills in weekly sustainment training. Laminated cards issued to all leaders."),
    ("COMMAND_AND_CONTROL", "M",
     "Brigade and battalion command posts had conflicting understanding of the R2 line position. "
     "The graphics were not updated after the FRAGORD was published.",
     "Require graphics update confirmation back-brief from all subordinate CPs within 2 hours of FRAGORD publication."),
    ("COMMAND_AND_CONTROL", "H",  # Record #14 — CONFLICT on radio frequency deconfliction
     "Radio frequency conflicts with the adjacent battalion caused significant communication "
     "delays. A faster coordination mechanism is needed at battalion level.",
     "Allow battalion S6 to coordinate directly with adjacent units for faster frequency deconfliction."),
    ("FIRES", "L",
     "Observers submitted fire missions using incorrect grid zone designator. Training on "
     "UTM grid systems is insufficient for new observers.",
     "Add UTM grid exercise to all fire observer certification courses. Use paper maps as backup."),
    ("INTELLIGENCE", "H",
     "Enemy course of action analysis did not include a non-kinetic threat vector. "
     "S2 staff focused exclusively on direct action threat.",
     "Expand IPB template to include OPSEC, EW, and influence operation threat vectors as required by FM 2-0."),
    ("SUSTAINMENT", "M",
     "Class V (ammunition) accountability at the ASP showed a 3% discrepancy after "
     "the live-fire exercise. No hand receipt was conducted after ammunition draw.",
     "Mandate hand receipts for all Class V draws exceeding 100 rounds. Conduct reconciliation within 2 hours of ceasefire."),
    ("MOVEMENT_AND_MANEUVER", "H",
     "Breach of the obstacle was delayed 40 minutes because the FASCAM minefield was "
     "not included in the obstacle overlay provided to the breach force.",
     "All engineer obstacle records must be integrated into the combined arms overlay before the order is issued."),
    ("PROTECTION", "H",
     "Fratricide prevention measures broke down during the consolidation phase. "
     "Two friendly elements entered the same grid without notification.",
     "Require confirmation of sector clearance before any element moves into an adjacent element's sector during consolidation."),
]

def gen_ex40k():
    out = os.path.join(BASE, "EX-40K_knowledge_manager", "training_data", "EX-40K_AAR_Backlog")
    makedirs(out)
    start = date(2024, 8, 1)
    units = ["1-1 BN","1-2 BN","1-3 BN","2-1 BN","DIV CAV","HHC BSB","1-4 BN"]
    exercises = ["COMBINED RESOLVE","SABER STRIKE","LIGHTNING FORGE","ALLIED SPIRIT","DEFENDER 25"]

    for idx, (category, priority, observation, recommendation) in enumerate(AAR_OBSERVATIONS, start=1):
        d = start + timedelta(days=random.randint(0, 300))
        unit = random.choice(units)
        ex = random.choice(exercises)
        content = textwrap.dedent(f"""\
        AFTER-ACTION REPORT (AAR) — RECORD {idx:02d}
        Classification: UNCLASSIFIED // TRAINING USE ONLY

        date: {d.isoformat()}
        unit: {unit}
        exercise_name: {ex}
        category: {category}
        priority: {priority}

        OBSERVATION:
        {observation}

        RECOMMENDATION:
        {recommendation}

        OPR: {unit} S3
        Submitted by: Training NCO
        """)
        fname = os.path.join(out, f"AAR_{idx:02d}_{d.strftime('%Y%m%d')}_{unit.replace(' ','_')}.txt")
        with open(fname, "w") as f:
            f.write(content)
    print(f"  EX-40K: 20 AAR .txt files (records #7 and #14 contain conflicting recommendations)")

# ── EX-40L: Personnel Readiness Feed ──────────────────────────────────────────
def gen_ex40l():
    out = os.path.join(BASE, "EX-40L_software_engineer", "training_data")
    makedirs(out)
    statuses = ["READY","PARTIALLY_READY","NOT_READY"]
    units_clean = ["1-1 BN","1-2 BN","1-3 BN","2-1 BN","DIV CAV","HHC","BSB"]
    # Mixed-case and trailing-space variants to require normalization
    units_dirty = ["1-1 bn ","1-2 BN","1-3 Bn","2-1 BN ","DIV CAV","hhc","BSB "]
    rows = []
    for i in range(1, 1001):
        pid = f"P-{i:05d}"
        d = date(2025, 1, 1) + timedelta(days=random.randint(0, 180))
        unit = random.choice(units_clean) if i > 50 else random.choice(units_dirty)
        status = random.choices(statuses, weights=[60, 25, 15])[0]
        equip = random.randint(1, 6) if random.random() > 0.07 else None  # ~7% null
        med = random.random() < 0.12
        rows.append({
            "personnel_id": pid,
            "unit": unit,
            "readiness_status": status,
            "last_updated": d.isoformat(),
            "equipment_assigned": equip,
            "medical_flag": med,
        })

    # Inject ~50 validation failures
    # Null personnel_id (10 records)
    for i in range(0, 10):
        rows[i * 3]["personnel_id"] = None

    # Invalid status values (15 records)
    bad_statuses = ["ready","N/A","UNKNOWN","3","PARTIAL"]
    for i in range(5, 20):
        rows[i * 4 + 1]["readiness_status"] = random.choice(bad_statuses)

    # Unparseable dates (10 records)
    bad_dates = ["01/15/2025","March 2025","2025-15-01","TBD","20250115"]
    for i in range(3, 13):
        rows[i * 7]["last_updated"] = random.choice(bad_dates)

    # Mixed-case unit names for rows 50-100 (already handled above)

    write_csv(os.path.join(out, "EX-40L_Personnel_Readiness_Feed.csv"),
              ["personnel_id","unit","readiness_status","last_updated",
               "equipment_assigned","medical_flag"], rows)
    bad = (10 + 15 + 10)
    print(f"  EX-40L: 1000 rows ({bad} validation failures: null IDs, bad status, bad dates)")

if __name__ == "__main__":
    print("Generating training datasets...")
    gen_ex10()
    gen_ex20()
    gen_ex30()
    gen_ex40f()
    gen_ex40g()
    gen_ex40h()
    gen_ex40i()
    gen_ex40j()
    gen_ex40k()
    gen_ex40l()
    print("\nDone. All datasets written to maven_training/exercises/EX-*/training_data/")
