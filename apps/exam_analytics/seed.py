"""Seed realistic demo data for the Exam Analytics Dashboard.

Generates 10 exam sessions across 5 courses with 8-15 trainees each,
spanning 6 months. Includes realistic score distributions, varying
difficulty patterns, and identifiable gain score trends.
"""

from __future__ import annotations

import random
from datetime import date, timedelta

from .db import ExamResult, ExamSession, QuestionScore, SessionLocal, init_db

# ---------------------------------------------------------------------------
# Course configurations — each has a distinct difficulty profile
# ---------------------------------------------------------------------------
COURSES = {
    "TM-40G": {
        "name": "ORSA",
        "cohorts": [
            {"label": "TM-40G FY26 Q1", "pre_date": date(2025, 10, 14), "post_date": date(2025, 10, 18)},
            {"label": "TM-40G FY26 Q2", "pre_date": date(2026, 1, 13), "post_date": date(2026, 1, 17)},
        ],
        # MC difficulty: probability of getting full marks per question (q1-q15)
        "mc_difficulty_pre": [0.4, 0.5, 0.3, 0.6, 0.2, 0.5, 0.3, 0.4, 0.5, 0.3, 0.4, 0.6, 0.2, 0.5, 0.4],
        "mc_difficulty_post": [0.8, 0.85, 0.7, 0.9, 0.6, 0.85, 0.65, 0.8, 0.85, 0.7, 0.75, 0.9, 0.5, 0.8, 0.75],
        # SA difficulty: mean fraction of points earned (q16-q20)
        "sa_difficulty_pre": [0.4, 0.3, 0.5, 0.2, 0.3],
        "sa_difficulty_post": [0.8, 0.7, 0.85, 0.6, 0.75],
        "n_students": [10, 12],
    },
    "TM-40H": {
        "name": "AI Engineer",
        "cohorts": [
            {"label": "TM-40H FY26 Q1", "pre_date": date(2025, 11, 4), "post_date": date(2025, 11, 8)},
            {"label": "TM-40H FY26 Q2", "pre_date": date(2026, 2, 10), "post_date": date(2026, 2, 14)},
        ],
        "mc_difficulty_pre": [0.3, 0.4, 0.2, 0.5, 0.3, 0.4, 0.2, 0.3, 0.4, 0.2, 0.3, 0.5, 0.2, 0.4, 0.3],
        "mc_difficulty_post": [0.7, 0.8, 0.6, 0.85, 0.7, 0.8, 0.55, 0.7, 0.75, 0.6, 0.7, 0.85, 0.5, 0.75, 0.65],
        "sa_difficulty_pre": [0.3, 0.2, 0.4, 0.15, 0.25],
        "sa_difficulty_post": [0.75, 0.65, 0.8, 0.55, 0.7],
        "n_students": [8, 10],
    },
    "TM-40K": {
        "name": "Knowledge Manager",
        "cohorts": [
            {"label": "TM-40K FY26 Q1", "pre_date": date(2025, 10, 21), "post_date": date(2025, 10, 24)},
        ],
        "mc_difficulty_pre": [0.5, 0.6, 0.4, 0.7, 0.3, 0.6, 0.4, 0.5, 0.6, 0.4, 0.5, 0.7, 0.3, 0.6, 0.5],
        "mc_difficulty_post": [0.85, 0.9, 0.8, 0.95, 0.7, 0.9, 0.75, 0.85, 0.9, 0.8, 0.85, 0.95, 0.65, 0.9, 0.85],
        "sa_difficulty_pre": [0.5, 0.4, 0.6, 0.3, 0.4],
        "sa_difficulty_post": [0.85, 0.8, 0.9, 0.7, 0.8],
        "n_students": [15],
    },
    "TM-40L": {
        "name": "Software Engineer",
        "cohorts": [
            {"label": "TM-40L FY26 Q1", "pre_date": date(2025, 11, 18), "post_date": date(2025, 11, 22)},
            {"label": "TM-40L FY26 Q2", "pre_date": date(2026, 2, 24), "post_date": date(2026, 2, 28)},
        ],
        # SWE: hardest exam — low pre scores, good but not great post
        "mc_difficulty_pre": [0.25, 0.3, 0.15, 0.4, 0.2, 0.3, 0.15, 0.25, 0.3, 0.15, 0.25, 0.4, 0.1, 0.3, 0.2],
        "mc_difficulty_post": [0.65, 0.7, 0.5, 0.8, 0.55, 0.7, 0.45, 0.65, 0.7, 0.5, 0.6, 0.8, 0.4, 0.65, 0.55],
        "sa_difficulty_pre": [0.2, 0.15, 0.3, 0.1, 0.2],
        "sa_difficulty_post": [0.65, 0.55, 0.7, 0.45, 0.6],
        "n_students": [8, 9],
    },
    "TM-40A": {
        "name": "Intelligence WFF",
        "cohorts": [
            {"label": "TM-40A FY26 Q2", "pre_date": date(2026, 1, 27), "post_date": date(2026, 1, 30)},
        ],
        "mc_difficulty_pre": [0.45, 0.55, 0.35, 0.65, 0.25, 0.55, 0.35, 0.45, 0.55, 0.35, 0.45, 0.65, 0.25, 0.55, 0.45],
        "mc_difficulty_post": [0.8, 0.88, 0.75, 0.92, 0.65, 0.88, 0.7, 0.82, 0.88, 0.75, 0.8, 0.92, 0.6, 0.85, 0.8],
        "sa_difficulty_pre": [0.45, 0.35, 0.55, 0.25, 0.35],
        "sa_difficulty_post": [0.82, 0.75, 0.88, 0.65, 0.78],
        "n_students": [11],
    },
}

# Trainee ID pool (DODIDs)
BASE_DODID = 1000000000


def _generate_mc_score(difficulty: float) -> int:
    """Generate MC score (0 or 2) based on difficulty probability."""
    return 2 if random.random() < difficulty else 0


def _generate_sa_score(difficulty: float) -> int:
    """Generate SA score (0-6) based on difficulty mean fraction."""
    # Use a clamped normal distribution centered on difficulty * 6
    mean = difficulty * 6
    score = round(random.gauss(mean, 1.2))
    return max(0, min(6, score))


def seed():
    """Insert rich demo data: 10 sessions, ~100+ individual exam results."""
    init_db()
    db = SessionLocal()
    try:
        if db.query(ExamSession).count() > 0:
            print("DB already has data -- skipping seed.")
            return

        random.seed(42)

        trainee_counter = 0
        total_results = 0
        total_sessions = 0

        for course_id, config in COURSES.items():
            for cohort_idx, cohort in enumerate(config["cohorts"]):
                n = config["n_students"][cohort_idx]

                # Create PRE session
                pre_session = ExamSession(
                    course_id=course_id,
                    form_type="PRE",
                    administration_date=cohort["pre_date"],
                    cohort_label=cohort["label"],
                )
                db.add(pre_session)
                db.flush()
                total_sessions += 1

                # Create POST session
                post_session = ExamSession(
                    course_id=course_id,
                    form_type="POST",
                    administration_date=cohort["post_date"],
                    cohort_label=cohort["label"],
                )
                db.add(post_session)
                db.flush()
                total_sessions += 1

                # Generate trainees for this cohort
                for student_i in range(n):
                    trainee_id = str(BASE_DODID + trainee_counter)
                    trainee_counter += 1

                    # Add per-student variance: some students are strong, some weak
                    # Student ability modifier: shifts all difficulties
                    ability = random.gauss(0, 0.1)

                    for session, mc_diff, sa_diff, form in [
                        (pre_session, config["mc_difficulty_pre"], config["sa_difficulty_pre"], "PRE"),
                        (post_session, config["mc_difficulty_post"], config["sa_difficulty_post"], "POST"),
                    ]:
                        mc_scores = []
                        sa_scores = []

                        # MC questions 1-15
                        for q in range(15):
                            adjusted_diff = max(0.05, min(0.95, mc_diff[q] + ability))
                            mc_scores.append(_generate_mc_score(adjusted_diff))

                        # SA questions 16-20
                        for q in range(5):
                            adjusted_diff = max(0.05, min(0.95, sa_diff[q] + ability))
                            sa_scores.append(_generate_sa_score(adjusted_diff))

                        total = sum(mc_scores) + sum(sa_scores)
                        pct = round(total / 60 * 100, 1)

                        if form == "PRE":
                            result_str = "DIAGNOSTIC"
                        elif total >= 42:
                            result_str = "PASS"
                        else:
                            result_str = "FAIL"

                        er = ExamResult(
                            session_id=session.id,
                            trainee_id=trainee_id,
                            total_score=total,
                            total_possible=60,
                            score_percent=pct,
                            result=result_str,
                        )
                        db.add(er)
                        db.flush()
                        total_results += 1

                        # MC question scores
                        for qnum, pts in enumerate(mc_scores, start=1):
                            db.add(QuestionScore(
                                result_id=er.id,
                                question_number=qnum,
                                question_type="MC",
                                points_possible=2,
                                points_awarded=pts,
                            ))

                        # SA question scores
                        for qnum, pts in enumerate(sa_scores, start=16):
                            db.add(QuestionScore(
                                result_id=er.id,
                                question_number=qnum,
                                question_type="SA",
                                points_possible=6,
                                points_awarded=pts,
                            ))

        db.commit()
        print(f"Seeded {total_sessions} exam sessions, {total_results} results "
              f"across {len(COURSES)} courses.")
    finally:
        db.close()


if __name__ == "__main__":
    seed()
