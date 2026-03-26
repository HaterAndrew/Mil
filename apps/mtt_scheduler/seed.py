"""Seed realistic demo data for the MTT Scheduler.

Generates 5 venues, 8 instructors, 12 events, and 5-15 enrollments per event
to simulate a theater-wide MSS MTT schedule across the USAREUR-AF AOR.
"""

from __future__ import annotations

import random
from datetime import date, timedelta

from .db import Enrollment, Event, Instructor, SessionLocal, Venue, init_db


# ---------------------------------------------------------------------------
# AOR venues
# ---------------------------------------------------------------------------
VENUES = [
    {
        "name": "Tower Barracks Training Center",
        "location": "Grafenwoehr, Germany",
        "capacity": 30,
        "has_network": True,
        "has_sipr": True,
        "notes": "Primary USAREUR-AF training facility. 7th ATC footprint.",
    },
    {
        "name": "Rose Barracks Classroom B",
        "location": "Vilseck, Germany",
        "capacity": 20,
        "has_network": True,
        "has_sipr": False,
        "notes": "2CR footprint. NIPR only.",
    },
    {
        "name": "Clay Kaserne Digital Lab",
        "location": "Wiesbaden, Germany",
        "capacity": 25,
        "has_network": True,
        "has_sipr": True,
        "notes": "USAREUR-AF HQ. Full SIPR/NIPR capability.",
    },
    {
        "name": "Caserma Del Din SCIF Annex",
        "location": "Vicenza, Italy",
        "capacity": 15,
        "has_network": True,
        "has_sipr": True,
        "notes": "SETAF-AF footprint. Limited seating.",
    },
    {
        "name": "Camp Kosciuszko Conf Room",
        "location": "Poznan, Poland",
        "capacity": 20,
        "has_network": True,
        "has_sipr": False,
        "notes": "V Corps forward. NIPR only. Requires coordination with Polish host nation.",
    },
]

# ---------------------------------------------------------------------------
# Instructor pool
# ---------------------------------------------------------------------------
INSTRUCTORS = [
    {
        "name": "FOSTER",
        "rank": "CW3",
        "unit": "USAREUR-AF ODT",
        "qualifications": ["SL 1", "SL 2", "SL 3", "SL 4G", "SL 4H"],
        "available_from": date(2026, 3, 1),
        "available_to": date(2026, 7, 31),
    },
    {
        "name": "BROOKS",
        "rank": "MAJ",
        "unit": "USAREUR-AF ODT",
        "qualifications": ["SL 1", "SL 2", "SL 3", "SL 4A", "SL 4F"],
        "available_from": date(2026, 3, 1),
        "available_to": date(2026, 7, 31),
    },
    {
        "name": "CHAPMAN",
        "rank": "SFC",
        "unit": "USAREUR-AF ODT",
        "qualifications": ["SL 1", "SL 2", "SL 3"],
        "available_from": date(2026, 3, 15),
        "available_to": date(2026, 6, 30),
    },
    {
        "name": "REYES",
        "rank": "CW2",
        "unit": "USAREUR-AF ODT",
        "qualifications": ["SL 1", "SL 2", "SL 3", "SL 4L"],
        "available_from": date(2026, 3, 1),
        "available_to": date(2026, 7, 31),
    },
    {
        "name": "OKAFOR",
        "rank": "MSG",
        "unit": "7th ATC",
        "qualifications": ["SL 1", "SL 2"],
        "available_from": date(2026, 4, 1),
        "available_to": date(2026, 6, 30),
    },
    {
        "name": "SCHMIDT",
        "rank": "CPT",
        "unit": "USAREUR-AF ODT",
        "qualifications": ["SL 1", "SL 2", "SL 3", "SL 4J", "SL 4K"],
        "available_from": date(2026, 3, 1),
        "available_to": date(2026, 7, 31),
    },
    {
        "name": "PARK",
        "rank": "CW2",
        "unit": "V Corps",
        "qualifications": ["SL 1", "SL 2", "SL 3", "SL 4M"],
        "available_from": date(2026, 4, 15),
        "available_to": date(2026, 7, 15),
    },
    {
        "name": "WILLIAMS",
        "rank": "SFC",
        "unit": "SETAF-AF",
        "qualifications": ["SL 1", "SL 2"],
        "available_from": date(2026, 3, 1),
        "available_to": date(2026, 5, 31),
    },
]

# ---------------------------------------------------------------------------
# Events — 12 MTT events over the next 4 months
# ---------------------------------------------------------------------------
EVENTS = [
    # --- COMPLETE events (past) ---
    {
        "name": "SL 1 Maven User — Grafenwoehr Cycle 1",
        "course_id": "SL 1",
        "location": "Grafenwoehr, Germany",
        "venue_idx": 0,
        "start_date": date(2026, 3, 3),
        "end_date": date(2026, 3, 4),
        "max_capacity": 25,
        "status": "COMPLETE",
        "notes": "Inaugural MTT event. 7th ATC support.",
        "instructor_idxs": [2, 4],
        "enroll_count": 15,
    },
    {
        "name": "SL 1 Maven User — Wiesbaden Cycle 1",
        "course_id": "SL 1",
        "location": "Wiesbaden, Germany",
        "venue_idx": 2,
        "start_date": date(2026, 3, 10),
        "end_date": date(2026, 3, 11),
        "max_capacity": 20,
        "status": "COMPLETE",
        "notes": "HQ staff priority. CG directed.",
        "instructor_idxs": [1, 5],
        "enroll_count": 12,
    },
    # --- ACTIVE events (currently running) ---
    {
        "name": "SL 2 Builder — Grafenwoehr Cycle 1",
        "course_id": "SL 2",
        "location": "Grafenwoehr, Germany",
        "venue_idx": 0,
        "start_date": date(2026, 3, 14),
        "end_date": date(2026, 3, 25),
        "max_capacity": 20,
        "status": "ACTIVE",
        "notes": "Prereq: SL 1 GO. Foundry build environment required.",
        "instructor_idxs": [0, 2],
        "enroll_count": 14,
    },
    {
        "name": "SL 1 Maven User — Vicenza Cycle 1",
        "course_id": "SL 1",
        "location": "Vicenza, Italy",
        "venue_idx": 3,
        "start_date": date(2026, 3, 17),
        "end_date": date(2026, 3, 18),
        "max_capacity": 15,
        "status": "ACTIVE",
        "notes": "SETAF-AF priority enrollment.",
        "instructor_idxs": [7],
        "enroll_count": 10,
    },
    # --- PLANNED events (upcoming) ---
    {
        "name": "SL 1 Maven User — Poznan Cycle 1",
        "course_id": "SL 1",
        "location": "Poznan, Poland",
        "venue_idx": 4,
        "start_date": date(2026, 4, 7),
        "end_date": date(2026, 4, 8),
        "max_capacity": 20,
        "status": "PLANNED",
        "notes": "V Corps forward. Host nation coord in progress.",
        "instructor_idxs": [4, 6],
        "enroll_count": 8,
    },
    {
        "name": "SL 2 Builder — Wiesbaden Cycle 1",
        "course_id": "SL 2",
        "location": "Wiesbaden, Germany",
        "venue_idx": 2,
        "start_date": date(2026, 4, 14),
        "end_date": date(2026, 4, 25),
        "max_capacity": 20,
        "status": "PLANNED",
        "notes": "Second SL 2 iteration. HQ personnel priority.",
        "instructor_idxs": [0, 3],
        "enroll_count": 6,
    },
    {
        "name": "SL 3 Advanced Builder — Grafenwoehr Cycle 1",
        "course_id": "SL 3",
        "location": "Grafenwoehr, Germany",
        "venue_idx": 0,
        "start_date": date(2026, 4, 28),
        "end_date": date(2026, 5, 9),
        "max_capacity": 15,
        "status": "PLANNED",
        "notes": "Prereq: SL 2 GO. SIPR access required.",
        "instructor_idxs": [0, 1],
        "enroll_count": 5,
    },
    {
        "name": "SL 1 Maven User — Vilseck Cycle 1",
        "course_id": "SL 1",
        "location": "Vilseck, Germany",
        "venue_idx": 1,
        "start_date": date(2026, 5, 5),
        "end_date": date(2026, 5, 6),
        "max_capacity": 20,
        "status": "PLANNED",
        "notes": "2CR footprint. NIPR classroom.",
        "instructor_idxs": [2, 7],
        "enroll_count": 5,
    },
    {
        "name": "SL 2 Builder — Vicenza Cycle 1",
        "course_id": "SL 2",
        "location": "Vicenza, Italy",
        "venue_idx": 3,
        "start_date": date(2026, 5, 12),
        "end_date": date(2026, 5, 23),
        "max_capacity": 12,
        "status": "PLANNED",
        "notes": "SETAF-AF builder cohort. Small class size due to venue.",
        "instructor_idxs": [3, 5],
        "enroll_count": 7,
    },
    {
        "name": "SL 4A Intelligence WFF — Grafenwoehr",
        "course_id": "SL 4A",
        "location": "Grafenwoehr, Germany",
        "venue_idx": 0,
        "start_date": date(2026, 5, 26),
        "end_date": date(2026, 6, 3),
        "max_capacity": 15,
        "status": "PLANNED",
        "notes": "First WFF MTT event. Prereq: SL 3 GO.",
        "instructor_idxs": [1],
        "enroll_count": 5,
    },
    {
        "name": "SL 4G ORSA — Wiesbaden",
        "course_id": "SL 4G",
        "location": "Wiesbaden, Germany",
        "venue_idx": 2,
        "start_date": date(2026, 6, 8),
        "end_date": date(2026, 6, 19),
        "max_capacity": 12,
        "status": "PLANNED",
        "notes": "Specialist track. Prereq: SL 3 GO. ORSA-qualified instructor required.",
        "instructor_idxs": [0],
        "enroll_count": 5,
    },
    {
        "name": "SL 1 Maven User — Grafenwoehr Cycle 2",
        "course_id": "SL 1",
        "location": "Grafenwoehr, Germany",
        "venue_idx": 0,
        "start_date": date(2026, 6, 22),
        "end_date": date(2026, 6, 23),
        "max_capacity": 25,
        "status": "PLANNED",
        "notes": "Second cycle. Open enrollment.",
        "instructor_idxs": [2, 4],
        "enroll_count": 5,
    },
]

# ---------------------------------------------------------------------------
# Soldier names for enrollment
# ---------------------------------------------------------------------------
SOLDIER_NAMES = [
    ("SGT", "KELLY, JAMES", "1-1 IN BN"),
    ("CPT", "CHEN, SARAH", "1-1 IN BN"),
    ("SPC", "RODRIGUEZ, MARIA", "1-1 IN BN"),
    ("SSG", "THOMPSON, DAVID", "1-1 IN BN"),
    ("1LT", "JACKSON, MICHAEL", "1-1 IN BN"),
    ("SGT", "PATEL, PRIYA", "2-1 IN BN"),
    ("SPC", "MARTINEZ, CARLOS", "2-1 IN BN"),
    ("CPL", "NGUYEN, TRANG", "2-1 IN BN"),
    ("SGT", "BROWN, ASHLEY", "3-1 FA BN"),
    ("SFC", "WILLIAMS, ROBERT", "3-1 FA BN"),
    ("CW2", "DAVIS, JENNIFER", "BSB 1BCT"),
    ("PFC", "WILSON, BRANDON", "BSB 1BCT"),
    ("SSG", "GARCIA, DANIEL", "2CR"),
    ("CPT", "LEE, SUNG", "2CR"),
    ("SGT", "HARRIS, KEISHA", "SETAF-AF"),
    ("SPC", "CLARK, THOMAS", "SETAF-AF"),
    ("1LT", "LEWIS, ANNA", "V Corps"),
    ("CPL", "ROBINSON, MARCUS", "V Corps"),
    ("SGT", "WALKER, JESSICA", "BDE 173"),
    ("SFC", "HALL, CHRISTOPHER", "BDE 173"),
    ("SPC", "ALLEN, BRITTANY", "12th CAB"),
    ("SSG", "YOUNG, PATRICK", "12th CAB"),
    ("CW3", "KING, SAMANTHA", "21st TSC"),
    ("PFC", "WRIGHT, DEVON", "21st TSC"),
    ("SSG", "SCOTT, ERIC", "7th ATC"),
    ("CPT", "GREEN, NICOLE", "7th ATC"),
    ("SGT", "BAKER, TIMOTHY", "HHC USAREUR-AF"),
    ("SPC", "ADAMS, LAURA", "HHC USAREUR-AF"),
    ("1LT", "NELSON, JAMES", "1-1 IN BN"),
    ("CPL", "CARTER, MICHELLE", "2-1 IN BN"),
]


def seed():
    """Insert demo data: 5 venues, 8 instructors, 12 events, ~120 enrollments."""
    init_db()
    db = SessionLocal()
    try:
        if db.query(Event).count() > 0:
            print("DB already has data -- skipping seed.")
            return

        random.seed(42)

        # --- Venues ---
        venue_objs = []
        for v in VENUES:
            venue = Venue(**v)
            db.add(venue)
            venue_objs.append(venue)
        db.flush()
        print(f"  Created {len(venue_objs)} venues.")

        # --- Instructors ---
        inst_objs = []
        for i in INSTRUCTORS:
            inst = Instructor(
                name=i["name"],
                rank=i["rank"],
                unit=i["unit"],
                available_from=i["available_from"],
                available_to=i["available_to"],
            )
            inst.set_qualifications(i["qualifications"])
            db.add(inst)
            inst_objs.append(inst)
        db.flush()
        print(f"  Created {len(inst_objs)} instructors.")

        # --- Events + instructor assignments ---
        event_objs = []
        for ev_data in EVENTS:
            ev = Event(
                name=ev_data["name"],
                course_id=ev_data["course_id"],
                location=ev_data["location"],
                venue_id=venue_objs[ev_data["venue_idx"]].id,
                start_date=ev_data["start_date"],
                end_date=ev_data["end_date"],
                max_capacity=ev_data["max_capacity"],
                status=ev_data["status"],
                notes=ev_data["notes"],
            )
            db.add(ev)
            db.flush()

            # Assign instructors
            for inst_idx in ev_data["instructor_idxs"]:
                ev.instructors.append(inst_objs[inst_idx])

            event_objs.append(ev)
        db.flush()
        print(f"  Created {len(event_objs)} events.")

        # --- Enrollments ---
        total_enrollments = 0
        dodid_counter = 2000000000

        for ev_idx, ev_data in enumerate(EVENTS):
            ev = event_objs[ev_idx]
            count = ev_data["enroll_count"]

            # Shuffle soldier pool and pick enrollees
            pool = list(range(len(SOLDIER_NAMES)))
            random.shuffle(pool)
            selected = pool[:count]

            for s_idx in selected:
                rank, name, unit = SOLDIER_NAMES[s_idx]
                dodid = str(dodid_counter)
                dodid_counter += 1

                # Determine enrollment status based on event status
                if ev.status == "COMPLETE":
                    # Most complete, a few no-shows
                    roll = random.random()
                    if roll < 0.8:
                        enroll_status = "COMPLETE"
                    elif roll < 0.93:
                        enroll_status = "NO_SHOW"
                    else:
                        enroll_status = "DROPPED"
                elif ev.status == "ACTIVE":
                    enroll_status = "ENROLLED"
                else:
                    enroll_status = "ENROLLED"

                enrollment = Enrollment(
                    event_id=ev.id,
                    dodid=dodid,
                    soldier_name=name,
                    soldier_rank=rank,
                    soldier_unit=unit,
                    status=enroll_status,
                )
                db.add(enrollment)
                total_enrollments += 1

        db.commit()
        print(f"  Created {total_enrollments} enrollments.")
        print(f"Seed complete: {len(venue_objs)} venues, {len(inst_objs)} instructors, "
              f"{len(event_objs)} events, {total_enrollments} enrollments.")
    finally:
        db.close()


if __name__ == "__main__":
    seed()
