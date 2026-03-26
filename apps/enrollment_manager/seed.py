"""Seed realistic demo data for the Enrollment Manager.

Generates ~20 training classes across 3 months with ~80 enrollments and
~15 waitlist entries. Uses same soldier names as readiness_tracker where possible.
"""

from __future__ import annotations

import random
from datetime import date, timedelta

from .db import (
    COURSE_CATALOG,
    Enrollment,
    SessionLocal,
    TrainingClass,
    WaitlistEntry,
    init_db,
)

# ---------------------------------------------------------------------------
# Locations within USAREUR-AF AOR
# ---------------------------------------------------------------------------
LOCATIONS = ["Wiesbaden", "Grafenwoehr", "Vilseck", "Stuttgart", "Sembach"]

# ---------------------------------------------------------------------------
# Instructors
# ---------------------------------------------------------------------------
INSTRUCTORS = [
    "MAJ SMITH", "MAJ JOHNSON", "CW3 DAVIS", "CW3 WILLIAMS",
    "SFC HENDERSON", "MSG TAYLOR", "1SG BROOKS",
]

# ---------------------------------------------------------------------------
# Soldier roster — reuses names from readiness_tracker seed
# ---------------------------------------------------------------------------
SOLDIERS = [
    ("KELLY", "JAMES", "SGT", "1-1 IN BN"),
    ("CHEN", "SARAH", "CPT", "1-1 IN BN"),
    ("RODRIGUEZ", "MARIA", "SPC", "1-1 IN BN"),
    ("THOMPSON", "DAVID", "SSG", "1-1 IN BN"),
    ("JACKSON", "MICHAEL", "1LT", "1-1 IN BN"),
    ("PATEL", "PRIYA", "SGT", "1-1 IN BN"),
    ("MARTINEZ", "CARLOS", "SPC", "1-1 IN BN"),
    ("NGUYEN", "TRANG", "CPL", "1-1 IN BN"),
    ("BROWN", "ASHLEY", "SGT", "1-1 IN BN"),
    ("WILLIAMS", "ROBERT", "SFC", "1-1 IN BN"),
    ("DAVIS", "JENNIFER", "CW2", "1-1 IN BN"),
    ("WILSON", "BRANDON", "PFC", "1-1 IN BN"),
    ("GARCIA", "DANIEL", "SSG", "2-1 IN BN"),
    ("LEE", "SUNG", "CPT", "2-1 IN BN"),
    ("HARRIS", "KEISHA", "SGT", "2-1 IN BN"),
    ("CLARK", "THOMAS", "SPC", "2-1 IN BN"),
    ("LEWIS", "ANNA", "1LT", "2-1 IN BN"),
    ("ROBINSON", "MARCUS", "CPL", "2-1 IN BN"),
    ("WALKER", "JESSICA", "SGT", "2-1 IN BN"),
    ("HALL", "CHRISTOPHER", "SFC", "2-1 IN BN"),
    ("ALLEN", "BRITTANY", "SPC", "2-1 IN BN"),
    ("YOUNG", "PATRICK", "SSG", "2-1 IN BN"),
    ("KING", "SAMANTHA", "CW3", "2-1 IN BN"),
    ("WRIGHT", "DEVON", "PFC", "2-1 IN BN"),
    ("SCOTT", "ERIC", "SSG", "3-1 FA BN"),
    ("GREEN", "NICOLE", "CPT", "3-1 FA BN"),
    ("BAKER", "TIMOTHY", "SGT", "3-1 FA BN"),
    ("ADAMS", "LAURA", "SPC", "3-1 FA BN"),
    ("NELSON", "JAMES", "1LT", "3-1 FA BN"),
    ("CARTER", "MICHELLE", "CPL", "3-1 FA BN"),
    ("MITCHELL", "RAYMOND", "SGT", "3-1 FA BN"),
    ("PEREZ", "ANDREA", "SFC", "3-1 FA BN"),
    ("ROBERTS", "KEVIN", "SPC", "3-1 FA BN"),
    ("TURNER", "STEPHANIE", "SSG", "3-1 FA BN"),
    ("EVANS", "MATTHEW", "SSG", "BSB 1BCT"),
    ("EDWARDS", "CRYSTAL", "CPT", "BSB 1BCT"),
    ("COLLINS", "RYAN", "SGT", "BSB 1BCT"),
    ("STEWART", "PATRICIA", "SPC", "BSB 1BCT"),
    ("SANCHEZ", "JORGE", "1LT", "BSB 1BCT"),
    ("MORRIS", "KAITLYN", "CPL", "BSB 1BCT"),
    ("ROGERS", "WILLIAM", "SGT", "BSB 1BCT"),
    ("REED", "DANIELLE", "SFC", "BSB 1BCT"),
    ("BAILEY", "ANDREW", "SSG", "BEB 1BCT"),
    ("RIVERA", "SOFIA", "CPT", "BEB 1BCT"),
    ("COOPER", "JUSTIN", "SGT", "BEB 1BCT"),
    ("RICHARDSON", "AMANDA", "SPC", "BEB 1BCT"),
    ("COX", "NATHANIEL", "1LT", "BEB 1BCT"),
    ("HOWARD", "MEGAN", "CPL", "BEB 1BCT"),
    ("WARD", "TYLER", "SGT", "BEB 1BCT"),
    ("TORRES", "ELENA", "SFC", "BEB 1BCT"),
]

# DODIDs match readiness_tracker seed (deterministic offset)
DODIDS = [f"{1000000000 + i}" for i in range(len(SOLDIERS))]


# ---------------------------------------------------------------------------
# Class definitions — ~20 classes over the next 3 months
# ---------------------------------------------------------------------------
def _build_classes(base_date: date) -> list[dict]:
    """Build a list of ~20 training class dicts.

    Mix of SL 1 through SL 4 level courses with varying sizes.
    """
    classes = [
        # --- SL 1 classes (large, foundational) ---
        {
            "course_id": "SL 1", "class_name": "SL 1 Maven User (Wiesbaden Mar)",
            "start_date": base_date + timedelta(days=3),
            "end_date": base_date + timedelta(days=4),
            "location": "Wiesbaden", "max_seats": 40,
            "instructor": "MAJ SMITH", "status": "SCHEDULED",
        },
        {
            "course_id": "SL 1", "class_name": "SL 1 Maven User (Grafenwoehr Apr)",
            "start_date": base_date + timedelta(days=30),
            "end_date": base_date + timedelta(days=31),
            "location": "Grafenwoehr", "max_seats": 40,
            "instructor": "MAJ JOHNSON", "status": "SCHEDULED",
        },
        {
            "course_id": "SL 1", "class_name": "SL 1 Maven User (Stuttgart May)",
            "start_date": base_date + timedelta(days=60),
            "end_date": base_date + timedelta(days=61),
            "location": "Stuttgart", "max_seats": 30,
            "instructor": "SFC HENDERSON", "status": "SCHEDULED",
        },
        # --- SL 2 classes ---
        {
            "course_id": "SL 2", "class_name": "SL 2 Builder (Wiesbaden Apr)",
            "start_date": base_date + timedelta(days=14),
            "end_date": base_date + timedelta(days=18),
            "location": "Wiesbaden", "max_seats": 30,
            "instructor": "CW3 DAVIS", "status": "SCHEDULED",
        },
        {
            "course_id": "SL 2", "class_name": "SL 2 Builder (Vilseck Apr)",
            "start_date": base_date + timedelta(days=35),
            "end_date": base_date + timedelta(days=39),
            "location": "Vilseck", "max_seats": 20,
            "instructor": "CW3 WILLIAMS", "status": "SCHEDULED",
        },
        {
            "course_id": "SL 2", "class_name": "SL 2 Builder (Sembach May)",
            "start_date": base_date + timedelta(days=65),
            "end_date": base_date + timedelta(days=69),
            "location": "Sembach", "max_seats": 30,
            "instructor": "MAJ SMITH", "status": "SCHEDULED",
        },
        # --- SL 3 classes ---
        {
            "course_id": "SL 3", "class_name": "SL 3 Advanced Builder (Grafenwoehr Apr)",
            "start_date": base_date + timedelta(days=21),
            "end_date": base_date + timedelta(days=25),
            "location": "Grafenwoehr", "max_seats": 20,
            "instructor": "CW3 DAVIS", "status": "SCHEDULED",
        },
        {
            "course_id": "SL 3", "class_name": "SL 3 Advanced Builder (Wiesbaden May)",
            "start_date": base_date + timedelta(days=50),
            "end_date": base_date + timedelta(days=54),
            "location": "Wiesbaden", "max_seats": 20,
            "instructor": "MSG TAYLOR", "status": "SCHEDULED",
        },
        # --- SL 4 specialist classes ---
        {
            "course_id": "SL 4A", "class_name": "SL 4A Intelligence WFF (Wiesbaden Apr)",
            "start_date": base_date + timedelta(days=28),
            "end_date": base_date + timedelta(days=31),
            "location": "Wiesbaden", "max_seats": 20,
            "instructor": "MAJ JOHNSON", "status": "SCHEDULED",
        },
        {
            "course_id": "SL 4B", "class_name": "SL 4B Fires WFF (Grafenwoehr Apr)",
            "start_date": base_date + timedelta(days=35),
            "end_date": base_date + timedelta(days=38),
            "location": "Grafenwoehr", "max_seats": 20,
            "instructor": "1SG BROOKS", "status": "SCHEDULED",
        },
        {
            "course_id": "SL 4D", "class_name": "SL 4D Sustainment WFF (Stuttgart May)",
            "start_date": base_date + timedelta(days=55),
            "end_date": base_date + timedelta(days=58),
            "location": "Stuttgart", "max_seats": 20,
            "instructor": "SFC HENDERSON", "status": "SCHEDULED",
        },
        {
            "course_id": "SL 4G", "class_name": "SL 4G ORSA (Wiesbaden May)",
            "start_date": base_date + timedelta(days=42),
            "end_date": base_date + timedelta(days=46),
            "location": "Wiesbaden", "max_seats": 20,
            "instructor": "CW3 WILLIAMS", "status": "SCHEDULED",
        },
        {
            "course_id": "SL 4H", "class_name": "SL 4H AI Engineer (Sembach May)",
            "start_date": base_date + timedelta(days=48),
            "end_date": base_date + timedelta(days=52),
            "location": "Sembach", "max_seats": 20,
            "instructor": "CW3 DAVIS", "status": "SCHEDULED",
        },
        {
            "course_id": "SL 4J", "class_name": "SL 4J Program Manager (Vilseck May)",
            "start_date": base_date + timedelta(days=70),
            "end_date": base_date + timedelta(days=73),
            "location": "Vilseck", "max_seats": 20,
            "instructor": "MAJ SMITH", "status": "SCHEDULED",
        },
        {
            "course_id": "SL 4L", "class_name": "SL 4L Software Engineer (Wiesbaden Jun)",
            "start_date": base_date + timedelta(days=75),
            "end_date": base_date + timedelta(days=79),
            "location": "Wiesbaden", "max_seats": 20,
            "instructor": "MSG TAYLOR", "status": "SCHEDULED",
        },
        # --- FBC ---
        {
            "course_id": "FBC", "class_name": "FBC Foundry Bootcamp (Grafenwoehr Apr)",
            "start_date": base_date + timedelta(days=25),
            "end_date": base_date + timedelta(days=29),
            "location": "Grafenwoehr", "max_seats": 20,
            "instructor": "1SG BROOKS", "status": "SCHEDULED",
        },
        # --- SL 4E (full class — will have waitlist) ---
        {
            "course_id": "SL 4E", "class_name": "SL 4E Protection WFF (Vilseck Apr)",
            "start_date": base_date + timedelta(days=32),
            "end_date": base_date + timedelta(days=35),
            "location": "Vilseck", "max_seats": 20,
            "instructor": "MAJ JOHNSON", "status": "SCHEDULED",
        },
        # --- Completed class ---
        {
            "course_id": "SL 1", "class_name": "SL 1 Maven User (Wiesbaden Feb — COMPLETED)",
            "start_date": base_date - timedelta(days=30),
            "end_date": base_date - timedelta(days=29),
            "location": "Wiesbaden", "max_seats": 30,
            "instructor": "MAJ SMITH", "status": "COMPLETED",
        },
        # --- Cancelled class ---
        {
            "course_id": "SL 3", "class_name": "SL 3 Advanced Builder (Stuttgart — CANCELLED)",
            "start_date": base_date + timedelta(days=40),
            "end_date": base_date + timedelta(days=44),
            "location": "Stuttgart", "max_seats": 20,
            "instructor": None, "status": "CANCELLED",
        },
        # --- One more SL 4M class ---
        {
            "course_id": "SL 4M", "class_name": "SL 4M ML Engineer (Wiesbaden Jun)",
            "start_date": base_date + timedelta(days=80),
            "end_date": base_date + timedelta(days=84),
            "location": "Wiesbaden", "max_seats": 20,
            "instructor": "CW3 DAVIS", "status": "SCHEDULED",
        },
    ]
    return classes


def seed():
    """Insert demo data: ~20 classes, ~80 enrollments, ~15 waitlist entries."""
    init_db()
    db = SessionLocal()
    try:
        if db.query(TrainingClass).count() > 0:
            print("DB already has data -- skipping seed.")
            return

        random.seed(42)  # deterministic for reproducible demos

        # Base date: use a date near "today" for realistic upcoming classes
        base_date = date(2026, 3, 17)

        # --- Create training classes ---
        class_defs = _build_classes(base_date)
        class_objects = []
        for cd in class_defs:
            tc = TrainingClass(
                course_id=cd["course_id"],
                class_name=cd["class_name"],
                start_date=cd["start_date"],
                end_date=cd["end_date"],
                location=cd["location"],
                max_seats=cd["max_seats"],
                instructor_name=cd.get("instructor"),
                status=cd["status"],
            )
            db.add(tc)
            class_objects.append(tc)

        db.flush()  # assign class_ids

        # --- Enrollment assignments ---
        # Map class index to list of soldier indices to enroll
        # Classes 0-2: SL 1 (large), 3-5: SL 2, 6-7: SL 3, 8-14: SL 4 variants,
        # 15: FBC, 16: SL 4E (full+waitlist), 17: completed, 18: cancelled, 19: SL 4M

        enrollment_map: dict[int, list[int]] = {
            # SL 1 Wiesbaden Mar — partially filled (~15 of 40)
            0: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 34, 35, 36],
            # SL 1 Grafenwoehr Apr — partially filled (~12 of 40)
            1: [12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23],
            # SL 1 Stuttgart May — lightly filled (~8 of 30)
            2: [24, 25, 26, 27, 28, 29, 30, 31],
            # SL 2 Wiesbaden Apr — nearly full (~18 of 30)
            3: list(range(0, 18)),
            # SL 2 Vilseck Apr — full (20 of 20) — will trigger waitlist scenario
            4: list(range(0, 20)),
            # SL 2 Sembach May — lightly filled (~6 of 30)
            5: [24, 25, 26, 34, 35, 36],
            # SL 3 Grafenwoehr Apr — moderate (~10 of 20)
            6: [0, 1, 3, 4, 12, 13, 16, 24, 25, 34],
            # SL 3 Wiesbaden May — light (~5 of 20)
            7: [5, 6, 14, 15, 26],
            # SL 4A Intelligence — light (~6 of 20)
            8: [0, 1, 4, 12, 13, 16],
            # SL 4B Fires — light (~5 of 20)
            9: [24, 25, 26, 28, 30],
            # SL 4D Sustainment — moderate (~8 of 20)
            10: [34, 35, 36, 37, 38, 39, 40, 41],
            # SL 4G ORSA — moderate (~7 of 20)
            11: [0, 3, 9, 12, 19, 24, 34],
            # SL 4H AI Engineer — moderate (~6 of 20)
            12: [1, 4, 13, 16, 25, 43],
            # SL 4J Program Manager — light (~4 of 20)
            13: [3, 12, 35, 38],
            # SL 4L Software Engineer — light (~5 of 20)
            14: [0, 1, 13, 25, 44],
            # FBC Grafenwoehr — moderate (~8 of 20)
            15: [7, 8, 17, 18, 20, 21, 29, 30],
            # SL 4E Protection Vilseck — FULL (20 of 20, will also get waitlist entries)
            16: list(range(0, 20)),
            # Completed SL 1 — all enrolled marked COMPLETED
            17: [0, 1, 2, 3, 4, 5, 12, 13, 14, 24, 25, 34, 35, 42, 43],
            # Cancelled — no enrollments
            18: [],
            # SL 4M ML Engineer — light (~4 of 20)
            19: [1, 4, 25, 43],
        }

        total_enrollments = 0
        for class_idx, soldier_indices in enrollment_map.items():
            tc = class_objects[class_idx]
            for seat_num, si in enumerate(soldier_indices, start=1):
                if si >= len(SOLDIERS):
                    continue
                last, first, rank, unit = SOLDIERS[si]

                # For the completed class, mark enrollments as COMPLETED
                enroll_status = "COMPLETED" if tc.status == "COMPLETED" else "ENROLLED"

                # Enrollment date: a few days before class start
                enroll_date = tc.start_date - timedelta(days=random.randint(5, 30))
                if enroll_date < date(2026, 1, 1):
                    enroll_date = date(2026, 1, 1)

                enrollment = Enrollment(
                    class_id=tc.class_id,
                    dodid=DODIDS[si],
                    last_name=last,
                    first_name=first,
                    rank=rank,
                    unit=unit,
                    enrollment_date=enroll_date,
                    status=enroll_status,
                    seat_number=seat_num,
                )
                db.add(enrollment)
                total_enrollments += 1

        db.flush()

        # --- Waitlist entries ---
        # Add waitlist entries for class 16 (SL 4E full) and class 4 (SL 2 Vilseck full)
        waitlist_entries_data = [
            # SL 4E waitlist — soldiers who didn't get a seat
            (16, 42, 2),  # BAILEY — high priority
            (16, 43, 1),  # RIVERA
            (16, 44, 0),  # COOPER
            (16, 45, 0),  # RICHARDSON
            (16, 46, 1),  # COX
            (16, 47, 0),  # HOWARD
            (16, 48, 0),  # WARD
            (16, 49, 2),  # TORRES — high priority
            # SL 2 Vilseck waitlist
            (4, 32, 1),   # ROBERTS
            (4, 33, 0),   # TURNER
            (4, 37, 0),   # STEWART
            (4, 38, 1),   # SANCHEZ
            (4, 39, 0),   # MORRIS
            (4, 40, 0),   # ROGERS
            (4, 41, 0),   # REED
        ]

        total_waitlist = 0
        for class_idx, si, priority in waitlist_entries_data:
            if si >= len(SOLDIERS):
                continue
            tc = class_objects[class_idx]
            last, first, rank, unit = SOLDIERS[si]

            entry = WaitlistEntry(
                class_id=tc.class_id,
                dodid=DODIDS[si],
                last_name=last,
                first_name=first,
                rank=rank,
                unit=unit,
                request_date=tc.start_date - timedelta(days=random.randint(3, 15)),
                priority=priority,
                status="WAITING",
            )
            db.add(entry)
            total_waitlist += 1

        db.commit()
        print(
            f"Seeded {len(class_defs)} training classes, {total_enrollments} enrollments, "
            f"{total_waitlist} waitlist entries."
        )
    finally:
        db.close()


if __name__ == "__main__":
    seed()
