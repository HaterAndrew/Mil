#!/usr/bin/env python3
"""Generate synthetic training data for exercise directories.

Creates CSV datasets in maven_training/exercises/EX_*/training_data/ for
exercises that are missing data.  Each exercise type gets domain-appropriate
synthetic data scaled by TM level:
  - SL 1/2/3: 10-20 records (foundational)
  - SL 4:     50-100 records (intermediate)
  - SL 5:     200-500 records (advanced)

Dependencies: stdlib only (csv, random, pathlib, datetime).
"""

from __future__ import annotations

import csv
import random
import sys
from datetime import date, timedelta
from pathlib import Path

random.seed(42)

REPO_ROOT = Path(__file__).resolve().parent.parent
EXERCISES_DIR = REPO_ROOT / "maven_training" / "exercises"

# ---------------------------------------------------------------------------
# Shared reference data
# ---------------------------------------------------------------------------
UNITS = ["1-1 IN BN", "2-1 IN BN", "3-1 FA BN", "BSB 1BCT", "BEB 1BCT"]
EQUIPMENT_CLASSES = ["wheeled", "tracked", "comms", "aviation", "engineer"]
LOCATIONS = [
    "Clay Kaserne", "Smith Barracks", "Patch Barracks",
    "Panzer Kaserne", "Rose Barracks",
]


def _date_range(start: date, days: int) -> list[date]:
    return [start + timedelta(days=i) for i in range(days)]


def _random_dates(start: date, end: date, count: int) -> list[date]:
    span = (end - start).days
    return sorted(random.sample(_date_range(start, span), min(count, span)))


# ---------------------------------------------------------------------------
# Generator templates by exercise type
# ---------------------------------------------------------------------------

def gen_wff_intelligence(path: Path, n: int):
    """SIGACT/reporting data for intelligence exercises."""
    rows = []
    report_types = ["SIGACT", "INTREP", "SALUTE", "SPOT", "TIPPER"]
    priorities = ["ROUTINE", "PRIORITY", "IMMEDIATE", "FLASH"]
    start = date(2025, 6, 1)
    for d in _date_range(start, n):
        unit = random.choice(UNITS)
        rows.append({
            "date": d.isoformat(),
            "unit": unit,
            "report_type": random.choice(report_types),
            "priority": random.choice(priorities),
            "grid_ref": f"{random.randint(30, 50)}S{random.randint(100, 999)}{random.randint(100, 999)}",
            "classification": random.choice(["CUI"]),
            "analyst": f"analyst_{random.randint(1, 10):02d}",
            "processing_hours": round(random.uniform(0.5, 24.0), 1),
        })
    _write_csv(path / "sigact_reports.csv", rows)


def gen_wff_fires(path: Path, n: int):
    """Target list / fire mission data for fires exercises."""
    rows = []
    target_types = ["POINT", "LINEAR", "AREA"]
    statuses = ["NOMINATED", "VALIDATED", "APPROVED", "EXECUTED", "BDA_PENDING"]
    start = date(2025, 6, 1)
    for i in range(n):
        d = start + timedelta(days=random.randint(0, 90))
        rows.append({
            "target_id": f"TGT-{i+1:04d}",
            "date": d.isoformat(),
            "unit": random.choice(UNITS),
            "target_type": random.choice(target_types),
            "status": random.choice(statuses),
            "grid_ref": f"{random.randint(30, 50)}S{random.randint(100, 999)}{random.randint(100, 999)}",
            "priority": random.randint(1, 5),
            "effects_assessment": random.choice(["EFFECTIVE", "INEFFECTIVE", "PENDING"]),
        })
    _write_csv(path / "target_list.csv", rows)


def gen_wff_maneuver(path: Path, n: int):
    """Movement and maneuver tracking data."""
    rows = []
    op_types = ["MOVEMENT_TO_CONTACT", "ATTACK", "DEFEND", "RETROGRADE", "SCREEN"]
    start = date(2025, 6, 1)
    for d in _date_range(start, n):
        unit = random.choice(UNITS)
        rows.append({
            "date": d.isoformat(),
            "unit": unit,
            "operation_type": random.choice(op_types),
            "vehicles_available": random.randint(8, 30),
            "vehicles_mission_capable": random.randint(5, 28),
            "personnel_strength_pct": round(random.uniform(75.0, 100.0), 1),
            "phase_line_reached": random.choice(["PL_ALPHA", "PL_BRAVO", "PL_CHARLIE"]),
            "supply_status": random.choice(["GREEN", "AMBER", "RED"]),
        })
    _write_csv(path / "maneuver_tracking.csv", rows)


def gen_wff_sustainment(path: Path, n: int):
    """Logistics and supply chain data."""
    rows = []
    supply_classes = ["CL_I", "CL_III", "CL_V", "CL_IX"]
    start = date(2025, 6, 1)
    for d in _date_range(start, n):
        unit = random.choice(UNITS)
        for sc in random.sample(supply_classes, random.randint(2, 4)):
            rows.append({
                "date": d.isoformat(),
                "unit": unit,
                "supply_class": sc,
                "on_hand_days": round(random.uniform(1.0, 14.0), 1),
                "required_days": 7.0,
                "status": "GREEN" if random.random() > 0.3 else random.choice(["AMBER", "RED"]),
                "last_resupply": (d - timedelta(days=random.randint(1, 7))).isoformat(),
            })
    _write_csv(path / "supply_status.csv", rows)


def gen_wff_protection(path: Path, n: int):
    """Force protection and threat data."""
    rows = []
    threat_types = ["IDF", "VBIED", "SAF", "CYBER", "INSIDER"]
    fpcon_levels = ["NORMAL", "ALPHA", "BRAVO", "CHARLIE"]
    start = date(2025, 6, 1)
    for d in _date_range(start, n):
        rows.append({
            "date": d.isoformat(),
            "location": random.choice(LOCATIONS),
            "fpcon_level": random.choice(fpcon_levels),
            "threat_type": random.choice(threat_types),
            "incidents_reported": random.randint(0, 5),
            "access_control_checks": random.randint(50, 300),
            "anomalies_detected": random.randint(0, 3),
        })
    _write_csv(path / "force_protection.csv", rows)


def gen_wff_mission_command(path: Path, n: int):
    """C2 system status and decision tracking data."""
    rows = []
    systems = ["CPCE", "AFATDS", "DCGS-A", "GCCS-A", "TIGR"]
    start = date(2025, 6, 1)
    for d in _date_range(start, n):
        for sys_name in random.sample(systems, random.randint(3, 5)):
            rows.append({
                "date": d.isoformat(),
                "location": random.choice(LOCATIONS),
                "system": sys_name,
                "status": random.choice(["OPERATIONAL", "DEGRADED", "DOWN"]),
                "uptime_pct": round(random.uniform(85.0, 100.0), 1),
                "users_active": random.randint(5, 50),
                "data_feeds_active": random.randint(2, 15),
            })
    _write_csv(path / "c2_system_status.csv", rows)


def gen_specialist_generic(path: Path, n: int, domain: str):
    """Generic metric dataset for specialist tracks without domain-specific templates."""
    rows = []
    start = date(2025, 6, 1)
    for d in _date_range(start, n):
        unit = random.choice(UNITS)
        rows.append({
            "date": d.isoformat(),
            "unit": unit,
            "domain": domain,
            "metric_value": round(random.uniform(50.0, 100.0), 2),
            "threshold": 80.0,
            "status": "PASS" if random.random() > 0.2 else "FAIL",
            "records_processed": random.randint(100, 10000),
            "anomalies_flagged": random.randint(0, 20),
        })
    _write_csv(path / f"{domain.lower()}_metrics.csv", rows)


def gen_advanced(path: Path, n: int, domain: str):
    """Larger, more complex dataset for SL 5 advanced exercises."""
    rows = []
    start = date(2025, 1, 1)
    for d in _date_range(start, n):
        for unit in random.sample(UNITS, random.randint(2, 5)):
            rows.append({
                "date": d.isoformat(),
                "unit": unit,
                "domain": domain,
                "metric_primary": round(random.gauss(75.0, 12.0), 2),
                "metric_secondary": round(random.gauss(80.0, 8.0), 2),
                "threshold_primary": 70.0,
                "threshold_secondary": 75.0,
                "sample_size": random.randint(50, 500),
                "confidence_interval": round(random.uniform(0.90, 0.99), 2),
                "trend": random.choice(["IMPROVING", "STABLE", "DECLINING"]),
                "records_analyzed": random.randint(1000, 50000),
            })
    _write_csv(path / f"{domain.lower()}_analysis.csv", rows)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
def _write_csv(filepath: Path, rows: list[dict]):
    """Write a list of dicts to CSV."""
    if not rows:
        return
    filepath.parent.mkdir(parents=True, exist_ok=True)
    with open(filepath, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)
    print(f"  {filepath.name}: {len(rows)} rows ({filepath.stat().st_size // 1024} KB)")


# ---------------------------------------------------------------------------
# Exercise → generator mapping
# ---------------------------------------------------------------------------
EXERCISE_GENERATORS: dict[str, tuple] = {
    # WFF tracks (SL 4A–F): 60-90 days of data
    "EX_40A_intelligence":      (gen_wff_intelligence, 90),
    "EX_40B_fires":             (gen_wff_fires, 80),
    "EX_40C_movement_maneuver": (gen_wff_maneuver, 60),
    "EX_40D_sustainment":       (gen_wff_sustainment, 60),
    "EX_40E_protection":        (gen_wff_protection, 60),
    "EX_40F_mission_command":   (gen_wff_mission_command, 45),
    # Specialist tracks missing data (SL 4)
    "EX_40J_program_manager":   (lambda p, n: gen_specialist_generic(p, n, "program_management"), 60),
    "EX_40K_knowledge_manager": (lambda p, n: gen_specialist_generic(p, n, "knowledge_management"), 60),
    "EX_40N_ux_designer":       (lambda p, n: gen_specialist_generic(p, n, "ux_design"), 60),
    "EX_40O_platform_engineer": (lambda p, n: gen_specialist_generic(p, n, "platform_engineering"), 60),
    # Advanced tracks (SL 5): 180 days of data
    "EX_50G_orsa":              (lambda p, n: gen_advanced(p, n, "orsa"), 180),
    "EX_50H_ai_engineer":       (lambda p, n: gen_advanced(p, n, "ai_engineering"), 180),
    "EX_50J_program_manager":   (lambda p, n: gen_advanced(p, n, "program_management"), 180),
    "EX_50K_knowledge_manager": (lambda p, n: gen_advanced(p, n, "knowledge_management"), 180),
    "EX_50L_software_engineer": (lambda p, n: gen_advanced(p, n, "software_engineering"), 180),
    "EX_50M_ml_engineer":       (lambda p, n: gen_advanced(p, n, "ml_engineering"), 180),
    "EX_50N_ux_designer":       (lambda p, n: gen_advanced(p, n, "ux_design"), 180),
    "EX_50O_platform_engineer": (lambda p, n: gen_advanced(p, n, "platform_engineering"), 180),
}


def main() -> int:
    if not EXERCISES_DIR.is_dir():
        print(f"ERROR: Exercises directory not found: {EXERCISES_DIR}", file=sys.stderr)
        return 1

    generated = 0
    skipped = 0

    for ex_name, (gen_fn, n_days) in sorted(EXERCISE_GENERATORS.items()):
        ex_dir = EXERCISES_DIR / ex_name
        if not ex_dir.is_dir():
            print(f"SKIP: {ex_name} — exercise directory not found")
            skipped += 1
            continue

        data_dir = ex_dir / "training_data"
        existing_csvs = list(data_dir.glob("*.csv")) if data_dir.exists() else []
        if existing_csvs:
            print(f"SKIP: {ex_name} — {len(existing_csvs)} CSV(s) already exist")
            skipped += 1
            continue

        print(f"GENERATE: {ex_name}")
        gen_fn(data_dir, n_days)
        generated += 1

    print(f"\nDone: {generated} generated, {skipped} skipped")
    return 0


if __name__ == "__main__":
    sys.exit(main())
