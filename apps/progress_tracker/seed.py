"""Seed realistic demo data for the Progress Tracker.

Creates milestones for ~40 soldiers and goals for ~20 soldiers, reusing
the same 60-soldier roster from readiness_tracker (DODIDs 1000000000+).
Deterministic via random.seed(42).
"""

from __future__ import annotations

import random
from datetime import date, timedelta

from .db import Goal, Milestone, SessionLocal, init_db

# ---------------------------------------------------------------------------
# Reuse readiness_tracker soldier DODIDs (1000000000 through 1000000059)
# ---------------------------------------------------------------------------
DODIDS = [f"{1000000000 + i}" for i in range(60)]

# Course progression paths for milestone assignment — realistic training plans
MILESTONE_PLANS: list[list[str]] = [
    # Foundation path
    ["SL 1", "SL 2", "SL 3"],
    ["SL 1", "SL 2"],
    ["SL 1"],
    # WFF tracks
    ["SL 3", "SL 4A"],
    ["SL 3", "SL 4B"],
    ["SL 3", "SL 4C"],
    ["SL 3", "SL 4D"],
    ["SL 3", "SL 4E"],
    ["SL 3", "SL 4F"],
    # Specialist tracks
    ["SL 3", "SL 4G"],
    ["SL 3", "SL 4H"],
    ["SL 3", "SL 4M"],
    ["SL 3", "SL 4J"],
    ["SL 3", "SL 4K"],
    ["SL 3", "SL 4L"],
    # Advanced tracks
    ["SL 4G", "SL 5G"],
    ["SL 4H", "SL 5H"],
    ["SL 4L", "SL 5L"],
    # Full pipeline
    ["SL 1", "SL 2", "SL 3", "SL 4A", "SL 4G"],
    ["SL 1", "SL 2", "SL 3", "SL 4B", "SL 4H"],
]

# Notes for realistic milestone entries
NOTES = [
    "Scheduled for next MTT cycle",
    "Self-study in progress",
    "Commander priority",
    "Awaiting evaluator availability",
    "Unit training schedule conflict",
    "Enrolled in upcoming class",
    "Rescheduled from previous quarter",
    None,
    None,
    None,
]

# Goal target courses for soldiers who haven't reached them yet
GOAL_COURSES = [
    "SL 2", "SL 3", "SL 4A", "SL 4B", "SL 4C",
    "SL 4G", "SL 4H", "SL 4M", "SL 4J", "SL 4K", "SL 4L",
    "SL 5G", "SL 5H", "SL 5L",
]


def seed():
    """Insert demo milestones and goals."""
    init_db()
    db = SessionLocal()
    try:
        if db.query(Milestone).count() > 0:
            print("Progress tracker DB already has data -- skipping seed.")
            return

        random.seed(42)

        today = date.today()
        milestone_count = 0
        goal_count = 0

        # Assign milestones to ~40 soldiers (indices 0-39)
        for idx in range(40):
            dodid = DODIDS[idx]
            plan = random.choice(MILESTONE_PLANS)

            for step, course_id in enumerate(plan):
                # Spread target dates over next 3 months
                # Earlier courses get earlier dates, later courses get later dates
                base_offset = step * 21 + random.randint(-7, 14)
                target = today + timedelta(days=base_offset)

                # Mix in some overdue items (target in the past)
                if random.random() < 0.15:
                    target = today - timedelta(days=random.randint(5, 45))

                # Mix in some completed items
                is_complete = random.random() < 0.25

                if is_complete:
                    status = "COMPLETE"
                elif target < today:
                    status = "OVERDUE"
                elif (target - today).days <= 14:
                    status = "AT_RISK"
                else:
                    status = "ON_TRACK"

                db.add(Milestone(
                    dodid=dodid,
                    course_id=course_id,
                    target_date=target,
                    status=status,
                    notes=random.choice(NOTES),
                ))
                milestone_count += 1

        # Assign goals to ~20 soldiers (indices 5-24, overlapping with milestone holders)
        for idx in range(5, 25):
            dodid = DODIDS[idx]
            target_course = random.choice(GOAL_COURSES)
            # Goal target date 1-4 months out
            target = today + timedelta(days=random.randint(30, 120))
            achieved = random.random() < 0.15  # ~15% already achieved

            db.add(Goal(
                dodid=dodid,
                target_course=target_course,
                target_date=target,
                achieved=achieved,
            ))
            goal_count += 1

        db.commit()
        print(f"Seeded {milestone_count} milestones and {goal_count} goals "
              f"for progress tracker.")
    finally:
        db.close()


if __name__ == "__main__":
    seed()
