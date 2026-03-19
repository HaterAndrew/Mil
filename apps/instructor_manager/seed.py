"""Seed realistic demo data for the Instructor Certification Manager.

Generates ~15 instructors across 5 units with certifications spanning
multiple courses, including expiring and expired certs, plus 6 months
of teaching history.
"""

from __future__ import annotations

import random
from datetime import date, timedelta

from .db import Certification, Instructor, SessionLocal, TeachingHistory, init_db

# ---------------------------------------------------------------------------
# Realistic instructor roster — 15 instructors across 5 BDE units
# ---------------------------------------------------------------------------
UNITS = ["1-1 IN BN", "2-1 IN BN", "3-1 FA BN", "BSB 1BCT", "BEB 1BCT"]

# (instructor_id, last, first, rank, mos, unit, email, phone, status)
INSTRUCTORS = [
    # 1-1 IN BN — 3 instructors
    ("INST-001", "MORRISON", "KYLE", "CW3", "255A", "1-1 IN BN", None, None, "ACTIVE"),
    ("INST-002", "CHEN", "LINDA", "MAJ", "26B", "1-1 IN BN", None, None, "ACTIVE"),
    ("INST-003", "BROOKS", "TERRENCE", "SFC", "25B", "1-1 IN BN", None, None, "ACTIVE"),

    # 2-1 IN BN — 3 instructors
    ("INST-004", "TANAKA", "KENJI", "CW2", "255A", "2-1 IN BN", None, None, "ACTIVE"),
    ("INST-005", "WILLIAMS", "DANA", "CPT", "26A", "2-1 IN BN", None, None, "ACTIVE"),
    ("INST-006", "HENDERSON", "MARCUS", "MSG", "17C", "2-1 IN BN", None, None, "TDY"),

    # 3-1 FA BN — 3 instructors
    ("INST-007", "PETROV", "ALEXEI", "MAJ", "26B", "3-1 FA BN", None, None, "ACTIVE"),
    ("INST-008", "GARCIA", "ELENA", "SFC", "13F", "3-1 FA BN", None, None, "ACTIVE"),
    ("INST-009", "TAYLOR", "JAMES", "CW3", "131A", "3-1 FA BN", None, None, "ACTIVE"),

    # BSB 1BCT — 3 instructors
    ("INST-010", "OKAFOR", "CHIOMA", "CPT", "90A", "BSB 1BCT", None, None, "ACTIVE"),
    ("INST-011", "DAVIS", "MICHAEL", "MSG", "25U", "BSB 1BCT", None, None, "ACTIVE"),
    ("INST-012", "MARTINEZ", "ROSA", "SFC", "92A", "BSB 1BCT", None, None, "INACTIVE"),

    # BEB 1BCT — 3 instructors
    ("INST-013", "NGUYEN", "TRANG", "CW2", "255A", "BEB 1BCT", None, None, "ACTIVE"),
    ("INST-014", "JACKSON", "DERRICK", "MAJ", "26B", "BEB 1BCT", None, None, "ACTIVE"),
    ("INST-015", "KOWALSKI", "ANNA", "SSG", "35F", "BEB 1BCT", None, None, "ACTIVE"),
]

# Certifying authorities
AUTHORITIES = [
    "COL RICHARDSON, BDE CDR",
    "LTC FOSTER, S3",
    "CW4 PEREZ, MSS PM",
    "MAJ THOMPSON, G3 TRNG",
]

# Locations for teaching events
LOCATIONS = [
    "Clay Kaserne, Wiesbaden",
    "Smith Barracks, Baumholder",
    "Grafenwoehr TC",
    "Hohenfels TC",
    "Vilseck, Rose Barracks",
]

RATINGS = ["EXCELLENT", "SATISFACTORY", "SATISFACTORY", "EXCELLENT", "NEEDS_IMPROVEMENT"]


def _random_date(start: date, end: date) -> date:
    """Random date between start and end inclusive."""
    delta = (end - start).days
    return start + timedelta(days=random.randint(0, max(delta, 0)))


def seed():
    """Insert demo data: ~15 instructors, certifications, and teaching history."""
    init_db()
    db = SessionLocal()
    try:
        if db.query(Instructor).count() > 0:
            print("DB already has data -- skipping seed.")
            return

        random.seed(42)  # deterministic for reproducible demos

        # Reference date for building timelines
        ref_date = date(2026, 3, 15)

        # --- Insert instructors ---
        for (iid, last, first, rank, mos, unit, email, phone, inst_status) in INSTRUCTORS:
            db.add(Instructor(
                instructor_id=iid,
                last_name=last,
                first_name=first,
                rank=rank,
                unit=unit,
                mos=mos,
                email=email,
                phone=phone,
                status=inst_status,
            ))
        db.flush()

        # --- Certification assignments ---
        # Each tuple: (instructor_id, course_id, cert_offset_days_ago, duration_days, status_override)
        # cert_offset_days_ago: how many days before ref_date the cert was granted
        # duration_days: how long the cert is valid
        # status_override: None = auto-calculate, else force this status
        cert_specs = [
            # INST-001 Morrison — certified TM-10, TM-20, TM-30, TM-40G (multi-course)
            ("INST-001", "TM-10", 350, 730, None),
            ("INST-001", "TM-20", 300, 730, None),
            ("INST-001", "TM-30", 250, 730, None),
            ("INST-001", "TM-40G", 180, 365, None),

            # INST-002 Chen — TM-10, TM-20, TM-40A; TM-40H expiring in 20 days
            ("INST-002", "TM-10", 400, 730, None),
            ("INST-002", "TM-20", 350, 730, None),
            ("INST-002", "TM-40A", 200, 365, None),
            ("INST-002", "TM-40H", 345, 365, None),  # expires ~20 days from ref

            # INST-003 Brooks — TM-10 only, cert expiring in 15 days
            ("INST-003", "TM-10", 350, 365, None),  # expires ~15 days from ref

            # INST-004 Tanaka — TM-10, TM-20, TM-30, TM-40H, TM-50H
            ("INST-004", "TM-10", 500, 730, None),
            ("INST-004", "TM-20", 400, 730, None),
            ("INST-004", "TM-30", 300, 730, None),
            ("INST-004", "TM-40H", 200, 365, None),
            ("INST-004", "TM-50H", 100, 365, None),

            # INST-005 Williams — TM-10, TM-20, TM-40J; TM-30 expired
            ("INST-005", "TM-10", 600, 730, None),
            ("INST-005", "TM-20", 500, 730, None),
            ("INST-005", "TM-30", 400, 365, "EXPIRED"),
            ("INST-005", "TM-40J", 150, 365, None),

            # INST-006 Henderson (TDY) — TM-10, TM-20
            ("INST-006", "TM-10", 300, 730, None),
            ("INST-006", "TM-20", 200, 730, None),

            # INST-007 Petrov — TM-10, TM-20, TM-30, TM-40B (fires-focused)
            ("INST-007", "TM-10", 500, 730, None),
            ("INST-007", "TM-20", 400, 730, None),
            ("INST-007", "TM-30", 300, 730, None),
            ("INST-007", "TM-40B", 200, 365, None),

            # INST-008 Garcia — TM-10, TM-40B; cert expiring in 25 days
            ("INST-008", "TM-10", 340, 365, None),  # expires ~25 days from ref
            ("INST-008", "TM-40B", 340, 365, None),  # also expiring soon

            # INST-009 Taylor — TM-10, TM-20, TM-30, TM-40F
            ("INST-009", "TM-10", 400, 730, None),
            ("INST-009", "TM-20", 300, 730, None),
            ("INST-009", "TM-30", 200, 730, None),
            ("INST-009", "TM-40F", 150, 365, None),

            # INST-010 Okafor — TM-10, TM-20, TM-40D (sustainment)
            ("INST-010", "TM-10", 400, 730, None),
            ("INST-010", "TM-20", 300, 730, None),
            ("INST-010", "TM-40D", 200, 365, None),

            # INST-011 Davis — TM-10, TM-20, TM-30; pending TM-40K
            ("INST-011", "TM-10", 500, 730, None),
            ("INST-011", "TM-20", 400, 730, None),
            ("INST-011", "TM-30", 300, 730, None),
            ("INST-011", "TM-40K", 10, 365, "PENDING"),

            # INST-012 Martinez (INACTIVE) — TM-10 expired
            ("INST-012", "TM-10", 500, 365, "EXPIRED"),

            # INST-013 Nguyen — TM-10, TM-20, TM-30, TM-40L, TM-50L
            ("INST-013", "TM-10", 600, 730, None),
            ("INST-013", "TM-20", 500, 730, None),
            ("INST-013", "TM-30", 400, 730, None),
            ("INST-013", "TM-40L", 200, 365, None),
            ("INST-013", "TM-50L", 100, 365, None),

            # INST-014 Jackson — TM-10, TM-20, TM-40J, TM-50J
            ("INST-014", "TM-10", 500, 730, None),
            ("INST-014", "TM-20", 400, 730, None),
            ("INST-014", "TM-40J", 200, 365, None),
            ("INST-014", "TM-50J", 100, 365, None),

            # INST-015 Kowalski — TM-10, TM-20; cert expiring in 10 days
            ("INST-015", "TM-10", 355, 365, None),  # expires ~10 days from ref
            ("INST-015", "TM-20", 200, 365, None),
        ]

        total_certs = 0
        for iid, course_id, offset_ago, duration, status_override in cert_specs:
            cert_date = ref_date - timedelta(days=offset_ago)
            exp_date = cert_date + timedelta(days=duration)

            # Auto-calculate status if not overridden
            if status_override:
                cert_status = status_override
            elif exp_date < ref_date:
                cert_status = "EXPIRED"
            else:
                cert_status = "CURRENT"

            db.add(Certification(
                instructor_id=iid,
                course_id=course_id,
                certified_date=cert_date,
                expiration_date=exp_date,
                certifying_authority=random.choice(AUTHORITIES),
                status=cert_status,
            ))
            total_certs += 1

        # --- Teaching history spanning 6 months ---
        # Generate 2-6 teaching events per active instructor
        teaching_start = ref_date - timedelta(days=180)
        total_events = 0

        for (iid, last, first, rank, mos, unit, email, phone, inst_status) in INSTRUCTORS:
            if inst_status != "ACTIVE":
                continue

            # Determine which courses this instructor is certified for
            certified_courses = [
                spec[1] for spec in cert_specs
                if spec[0] == iid and (spec[4] != "EXPIRED" and spec[4] != "PENDING")
            ]
            if not certified_courses:
                continue

            num_events = random.randint(2, 6)
            for _ in range(num_events):
                event_date = _random_date(teaching_start, ref_date)
                course_id = random.choice(certified_courses)
                db.add(TeachingHistory(
                    instructor_id=iid,
                    course_id=course_id,
                    event_date=event_date,
                    location=random.choice(LOCATIONS),
                    students_count=random.randint(8, 25),
                    rating=random.choice(RATINGS),
                    notes=None,
                ))
                total_events += 1

        db.commit()
        print(
            f"Seeded {len(INSTRUCTORS)} instructors, {total_certs} certifications, "
            f"{total_events} teaching events across {len(UNITS)} units."
        )
    finally:
        db.close()


if __name__ == "__main__":
    seed()
