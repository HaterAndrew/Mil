"""Seed realistic demo data for the Training Readiness Tracker.

Generates ~60 soldiers across 5 units (BDE-level) with realistic progression
through the MSS prereq chain, spanning 6 months of training history.
"""

from __future__ import annotations

import random
from datetime import date, timedelta

from .db import Completion, Course, SessionLocal, Trainee, init_db

# ---------------------------------------------------------------------------
# Realistic roster data — 5 units within a notional BDE
# ---------------------------------------------------------------------------
UNITS = ["1-1 IN BN", "2-1 IN BN", "3-1 FA BN", "BSB 1BCT", "BEB 1BCT"]

# (last, first, rank, mos)
SOLDIERS = [
    # --- 1-1 IN BN (12 soldiers) ---
    ("KELLY", "JAMES", "SGT", "17C", "1-1 IN BN"),
    ("CHEN", "SARAH", "CPT", "26B", "1-1 IN BN"),
    ("RODRIGUEZ", "MARIA", "SPC", "35F", "1-1 IN BN"),
    ("THOMPSON", "DAVID", "SSG", "25B", "1-1 IN BN"),
    ("JACKSON", "MICHAEL", "1LT", "26A", "1-1 IN BN"),
    ("PATEL", "PRIYA", "SGT", "17C", "1-1 IN BN"),
    ("MARTINEZ", "CARLOS", "SPC", "35T", "1-1 IN BN"),
    ("NGUYEN", "TRANG", "CPL", "25D", "1-1 IN BN"),
    ("BROWN", "ASHLEY", "SGT", "35F", "1-1 IN BN"),
    ("WILLIAMS", "ROBERT", "SFC", "25U", "1-1 IN BN"),
    ("DAVIS", "JENNIFER", "CW2", "255A", "1-1 IN BN"),
    ("WILSON", "BRANDON", "PFC", "25B", "1-1 IN BN"),

    # --- 2-1 IN BN (12 soldiers) ---
    ("GARCIA", "DANIEL", "SSG", "17C", "2-1 IN BN"),
    ("LEE", "SUNG", "CPT", "26B", "2-1 IN BN"),
    ("HARRIS", "KEISHA", "SGT", "35F", "2-1 IN BN"),
    ("CLARK", "THOMAS", "SPC", "25B", "2-1 IN BN"),
    ("LEWIS", "ANNA", "1LT", "26A", "2-1 IN BN"),
    ("ROBINSON", "MARCUS", "CPL", "25D", "2-1 IN BN"),
    ("WALKER", "JESSICA", "SGT", "17C", "2-1 IN BN"),
    ("HALL", "CHRISTOPHER", "SFC", "25U", "2-1 IN BN"),
    ("ALLEN", "BRITTANY", "SPC", "35T", "2-1 IN BN"),
    ("YOUNG", "PATRICK", "SSG", "25B", "2-1 IN BN"),
    ("KING", "SAMANTHA", "CW3", "255A", "2-1 IN BN"),
    ("WRIGHT", "DEVON", "PFC", "25B", "2-1 IN BN"),

    # --- 3-1 FA BN (12 soldiers) ---
    ("SCOTT", "ERIC", "SSG", "13F", "3-1 FA BN"),
    ("GREEN", "NICOLE", "CPT", "26B", "3-1 FA BN"),
    ("BAKER", "TIMOTHY", "SGT", "13J", "3-1 FA BN"),
    ("ADAMS", "LAURA", "SPC", "35F", "3-1 FA BN"),
    ("NELSON", "JAMES", "1LT", "13A", "3-1 FA BN"),
    ("CARTER", "MICHELLE", "CPL", "25D", "3-1 FA BN"),
    ("MITCHELL", "RAYMOND", "SGT", "13F", "3-1 FA BN"),
    ("PEREZ", "ANDREA", "SFC", "13J", "3-1 FA BN"),
    ("ROBERTS", "KEVIN", "SPC", "25B", "3-1 FA BN"),
    ("TURNER", "STEPHANIE", "SSG", "35F", "3-1 FA BN"),
    ("PHILLIPS", "BRIAN", "CW2", "131A", "3-1 FA BN"),
    ("CAMPBELL", "DIANA", "PFC", "25B", "3-1 FA BN"),

    # --- BSB 1BCT (12 soldiers) ---
    ("EVANS", "MATTHEW", "SSG", "25B", "BSB 1BCT"),
    ("EDWARDS", "CRYSTAL", "CPT", "90A", "BSB 1BCT"),
    ("COLLINS", "RYAN", "SGT", "25B", "BSB 1BCT"),
    ("STEWART", "PATRICIA", "SPC", "92A", "BSB 1BCT"),
    ("SANCHEZ", "JORGE", "1LT", "90A", "BSB 1BCT"),
    ("MORRIS", "KAITLYN", "CPL", "25D", "BSB 1BCT"),
    ("ROGERS", "WILLIAM", "SGT", "25U", "BSB 1BCT"),
    ("REED", "DANIELLE", "SFC", "92A", "BSB 1BCT"),
    ("COOK", "ANTHONY", "SPC", "25B", "BSB 1BCT"),
    ("MORGAN", "HEATHER", "SSG", "35F", "BSB 1BCT"),
    ("BELL", "GREGORY", "CW2", "255A", "BSB 1BCT"),
    ("MURPHY", "TIFFANY", "PFC", "25B", "BSB 1BCT"),

    # --- BEB 1BCT (12 soldiers) ---
    ("BAILEY", "ANDREW", "SSG", "12B", "BEB 1BCT"),
    ("RIVERA", "SOFIA", "CPT", "26B", "BEB 1BCT"),
    ("COOPER", "JUSTIN", "SGT", "25B", "BEB 1BCT"),
    ("RICHARDSON", "AMANDA", "SPC", "35F", "BEB 1BCT"),
    ("COX", "NATHANIEL", "1LT", "26A", "BEB 1BCT"),
    ("HOWARD", "MEGAN", "CPL", "25D", "BEB 1BCT"),
    ("WARD", "TYLER", "SGT", "25B", "BEB 1BCT"),
    ("TORRES", "ELENA", "SFC", "25U", "BEB 1BCT"),
    ("PETERSON", "DEREK", "SPC", "35T", "BEB 1BCT"),
    ("GRAY", "LINDSEY", "SSG", "35F", "BEB 1BCT"),
    ("RAMIREZ", "HECTOR", "CW3", "255A", "BEB 1BCT"),
    ("JAMES", "PAULA", "PFC", "25B", "BEB 1BCT"),
]

# Evaluators
EVALUATORS = [
    "MAJ SMITH", "MAJ JOHNSON", "CW3 DAVIS", "CW3 WILLIAMS",
    "SFC HENDERSON", "MSG TAYLOR", "1SG BROOKS",
]

# ---------------------------------------------------------------------------
# Training progression profiles — define how far each soldier has progressed
# ---------------------------------------------------------------------------
# Profile key: list of courses completed (in order). Prereqs enforced.
PROFILES = {
    # Foundation only
    "tm10_only": ["SL 1"],
    "tm10_nogo": [],  # attempted SL 1, got NO_GO
    "tm20": ["SL 1", "SL 2"],
    "tm30": ["SL 1", "SL 2", "SL 3"],
    "fbc": ["SL 1", "SL 2", "FBC"],

    # WFF tracks (A-F)
    "wff_a": ["SL 1", "SL 2", "SL 3", "SL 4A"],
    "wff_b": ["SL 1", "SL 2", "SL 3", "SL 4B"],
    "wff_c": ["SL 1", "SL 2", "SL 3", "SL 4C"],
    "wff_d": ["SL 1", "SL 2", "SL 3", "SL 4D"],
    "wff_e": ["SL 1", "SL 2", "SL 3", "SL 4E"],
    "wff_f": ["SL 1", "SL 2", "SL 3", "SL 4F"],

    # Specialist tracks (G-O)
    "spec_g": ["SL 1", "SL 2", "SL 3", "SL 4G"],
    "spec_h": ["SL 1", "SL 2", "SL 3", "SL 4H"],
    "spec_i": ["SL 1", "SL 2", "SL 3", "SL 4M"],
    "spec_j": ["SL 1", "SL 2", "SL 3", "SL 4J"],
    "spec_k": ["SL 1", "SL 2", "SL 3", "SL 4K"],
    "spec_l": ["SL 1", "SL 2", "SL 3", "SL 4L"],

    # Advanced (SL 5)
    "adv_g": ["SL 1", "SL 2", "SL 3", "SL 4G", "SL 5G"],
    "adv_h": ["SL 1", "SL 2", "SL 3", "SL 4H", "SL 5H"],
    "adv_l": ["SL 1", "SL 2", "SL 3", "SL 4L", "SL 5L"],

    # Multi-track (soldiers who took WFF + specialist)
    "multi_ag": ["SL 1", "SL 2", "SL 3", "SL 4A", "SL 4G"],
    "multi_bh": ["SL 1", "SL 2", "SL 3", "SL 4B", "SL 4H"],
    "multi_fl": ["SL 1", "SL 2", "SL 3", "SL 4F", "SL 4L"],

    # Brand new — no courses yet
    "new": [],
}

# Distribution: assign profiles to soldiers (index into SOLDIERS list)
# Roughly: ~30% foundation, ~25% WFF, ~25% specialist, ~10% advanced, ~10% new/nogo
ASSIGNMENTS = [
    # 1-1 IN BN — strong unit, several at specialist/advanced level
    "adv_g", "multi_ag", "tm30", "spec_l", "adv_h", "wff_a",
    "tm20", "spec_k", "wff_f", "multi_fl", "spec_j", "tm10_only",

    # 2-1 IN BN — moderate progress, some stuck at foundation
    "spec_g", "wff_b", "tm30", "tm20", "wff_a", "tm10_only",
    "spec_h", "tm30", "tm10_nogo", "wff_c", "adv_l", "new",

    # 3-1 FA BN — fires-heavy unit, lots of WFF-B
    "wff_b", "spec_g", "wff_b", "tm20", "wff_b", "tm10_only",
    "wff_f", "tm30", "tm10_only", "wff_e", "spec_j", "new",

    # BSB 1BCT — sustainment-focused, good SL 4D/SL 4J representation
    "wff_d", "spec_j", "wff_d", "tm20", "tm30", "tm10_only",
    "spec_k", "wff_d", "tm10_nogo", "fbc", "multi_bh", "new",

    # BEB 1BCT — engineering/protection focused
    "wff_e", "spec_l", "wff_c", "tm20", "wff_e", "tm10_only",
    "spec_i", "tm30", "tm10_only", "wff_e", "spec_h", "new",
]


def _random_date(start: date, end: date) -> date:
    """Random date between start and end inclusive."""
    delta = (end - start).days
    return start + timedelta(days=random.randint(0, max(delta, 0)))


def seed():
    """Insert rich demo data: 60 soldiers, ~250+ completions."""
    init_db()
    db = SessionLocal()
    try:
        if db.query(Trainee).count() > 0:
            print("DB already has data -- skipping seed.")
            return

        random.seed(42)  # deterministic for reproducible demos

        # Base date for training timeline: training started ~6 months ago
        timeline_start = date(2025, 9, 1)

        # Course timing offsets (days from soldier's start date)
        # Simulates realistic gaps between course completions
        COURSE_OFFSETS = {
            "SL 1": (0, 5),       # day 0-5
            "SL 2": (14, 30),     # 2-4 weeks later
            "SL 3": (45, 75),     # 6-10 weeks after SL 2
            "FBC": (30, 60),       # parallel to SL 3 timeline
            "SL 4A": (80, 120),
            "SL 4B": (80, 120),
            "SL 4C": (80, 120),
            "SL 4D": (80, 120),
            "SL 4E": (80, 120),
            "SL 4F": (80, 120),
            "SL 4G": (90, 130),
            "SL 4H": (90, 130),
            "SL 4M": (90, 130),
            "SL 4J": (80, 110),
            "SL 4K": (80, 110),
            "SL 4L": (90, 130),
            "SL 5G": (140, 180),
            "SL 5H": (140, 180),
            "SL 5M": (140, 180),
            "SL 5J": (120, 160),
            "SL 5K": (120, 160),
            "SL 5L": (140, 180),
        }

        # Create DODIDs deterministically
        dodids = [f"{1000000000 + i}" for i in range(len(SOLDIERS))]

        # Insert trainees
        for idx, (last, first, rank, mos, unit) in enumerate(SOLDIERS):
            db.add(Trainee(
                dodid=dodids[idx],
                last_name=last,
                first_name=first,
                rank=rank,
                unit=unit,
                mos=mos,
            ))
        db.flush()

        # Insert completions based on profile assignments
        total_completions = 0
        nogo_count = 0

        for idx, profile_key in enumerate(ASSIGNMENTS):
            if idx >= len(SOLDIERS):
                break

            dodid = dodids[idx]
            courses = PROFILES[profile_key]

            # Each soldier starts training at a slightly different time
            soldier_start = timeline_start + timedelta(days=random.randint(0, 60))

            for course_id in courses:
                offset_min, offset_max = COURSE_OFFSETS.get(course_id, (0, 30))
                eval_date = soldier_start + timedelta(days=random.randint(offset_min, offset_max))

                # Cap at today
                if eval_date > date.today():
                    eval_date = date.today()

                db.add(Completion(
                    dodid=dodid,
                    course_id=course_id,
                    result="GO",
                    evaluation_date=eval_date,
                    evaluator_name=random.choice(EVALUATORS),
                ))
                total_completions += 1

            # Special handling for NO_GO profiles
            if profile_key == "tm10_nogo":
                eval_date = soldier_start + timedelta(days=random.randint(0, 5))
                db.add(Completion(
                    dodid=dodid,
                    course_id="SL 1",
                    result="NO_GO",
                    evaluation_date=eval_date,
                    evaluator_name=random.choice(EVALUATORS),
                ))
                total_completions += 1
                nogo_count += 1

        db.commit()
        print(f"Seeded {len(SOLDIERS)} trainees, {total_completions} completions "
              f"({nogo_count} NO_GO) across {len(UNITS)} units.")
    finally:
        db.close()


if __name__ == "__main__":
    seed()
