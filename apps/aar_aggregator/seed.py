"""Seed realistic demo data for the AAR Aggregator.

Generates 18 AARs spanning 6 months across TM-10 through TM-40 training events
with realistic sustains, improves (with recurring issues), evaluations,
curriculum discrepancies, and environment issues.
"""

from __future__ import annotations

import random
from datetime import date, timedelta

from .db import (
    AAR,
    CurriculumDiscrepancy,
    EnvironmentIssue,
    ImproveItem,
    SessionLocal,
    StudentEvaluation,
    SustainItem,
    init_db,
)

# ---------------------------------------------------------------------------
# Instructors
# ---------------------------------------------------------------------------
INSTRUCTORS = [
    "MAJ SMITH", "MAJ JOHNSON", "CW3 DAVIS", "CW3 WILLIAMS",
    "SFC HENDERSON", "MSG TAYLOR", "1SG BROOKS", "CPT CHEN",
    "CW2 PHILLIPS", "SGT KELLY",
]

LOCATIONS = [
    "MSS sandbox environment",
    "Live training instance",
    "MSS production (read-only)",
    "Classified training enclave",
    "Remote / VTC-enabled classroom",
]

# Trainee name pool for evaluations
TRAINEE_NAMES = [
    "SGT JONES", "SPC WILLIAMS", "CPL MARTINEZ", "SGT HARRIS",
    "SPC CLARK", "1LT LEWIS", "SGT WALKER", "SPC ALLEN",
    "CPL ROBINSON", "SGT BAKER", "SPC ADAMS", "SGT MITCHELL",
    "CPL CARTER", "SPC ROBERTS", "SGT TURNER", "SPC COOK",
    "CPL MORRIS", "SGT ROGERS", "SPC REED", "SGT COOPER",
    "CPL HOWARD", "SPC PETERSON", "SGT WARD", "SPC GRAY",
]

# ---------------------------------------------------------------------------
# Recurring issues — these appear across multiple AARs to show trends
# ---------------------------------------------------------------------------
RECURRING_ISSUES = {
    "env_access": {
        "problem": "Environment access delayed start by 30 minutes",
        "proposed_fix": "Pre-provision accounts 48 hrs before class",
        "category": "MISSION_COMMAND",
        "priority": "H",
    },
    "env_access_v2": {
        "problem": "Environment access delayed start by 30 minutes",
        "proposed_fix": "Automate account provisioning via script",
        "category": "MISSION_COMMAND",
        "priority": "H",
    },
    "bandwidth": {
        "problem": "Network bandwidth insufficient for concurrent users in training environment",
        "proposed_fix": "Request dedicated bandwidth allocation for training days",
        "category": "PROTECTION",
        "priority": "H",
    },
    "tm_outdated": {
        "problem": "TM references deprecated UI elements no longer present in current build",
        "proposed_fix": "Update TM screenshots and step descriptions to match current build",
        "category": "INTELLIGENCE",
        "priority": "M",
    },
    "time_governance": {
        "problem": "Governance module needs more time -- currently compressed",
        "proposed_fix": "Expand to full half-day block",
        "category": "PROTECTION",
        "priority": "M",
    },
    "aip_rushed": {
        "problem": "AIP section felt rushed at end of day",
        "proposed_fix": "Move AIP overview to morning block",
        "category": "INTELLIGENCE",
        "priority": "M",
    },
    "data_quality": {
        "problem": "Students struggled with data quality assessment tasks without real-world examples",
        "proposed_fix": "Develop scenario-based data quality exercise with sanitized operational data",
        "category": "INTELLIGENCE",
        "priority": "M",
    },
}

# ---------------------------------------------------------------------------
# Unique issues (appear in single AARs only)
# ---------------------------------------------------------------------------
UNIQUE_ISSUES = [
    {"problem": "Projector failed mid-class; switched to backup laptop display",
     "proposed_fix": "Stage backup display equipment", "category": "SUSTAINMENT", "priority": "L"},
    {"problem": "Exercise scenario lacked sufficient complexity for advanced students",
     "proposed_fix": "Add tiered difficulty levels to exercises", "category": None, "priority": "M"},
    {"problem": "Student prerequisite knowledge varied widely within cohort",
     "proposed_fix": "Implement readiness assessment before course start", "category": None, "priority": "M"},
    {"problem": "Live demo failed due to data pipeline change between class prep and execution",
     "proposed_fix": "Snapshot demo environment 24 hrs before class", "category": "MISSION_COMMAND", "priority": "H"},
    {"problem": "Insufficient hands-on time for transform configuration",
     "proposed_fix": "Reduce lecture time, increase lab time by 30 min", "category": None, "priority": "M"},
    {"problem": "Fire support coordinator section lacked fires-specific examples",
     "proposed_fix": "Develop FIRES WFF scenario data for exercises", "category": "FIRES", "priority": "M"},
    {"problem": "Student workstations had outdated browser version blocking MSS access",
     "proposed_fix": "Add browser version check to pre-class checklist", "category": "SUSTAINMENT", "priority": "M"},
    {"problem": "Movement and maneuver dataset too small to demonstrate meaningful analysis",
     "proposed_fix": "Generate larger synthetic M&M dataset for training", "category": "MOVEMENT_MANEUVER", "priority": "M"},
    {"problem": "Classification markings on training materials inconsistent with local SOP",
     "proposed_fix": "Review all training materials for marking compliance", "category": "PROTECTION", "priority": "H"},
    {"problem": "No offline fallback when network connectivity dropped during exercise",
     "proposed_fix": "Develop offline exercise packet as contingency", "category": "SUSTAINMENT", "priority": "M"},
]

# ---------------------------------------------------------------------------
# Sustain item templates
# ---------------------------------------------------------------------------
SUSTAIN_TEMPLATES = [
    "Dashboard walkthrough was well-received; students appreciated real data examples",
    "Pairing experienced operators with new users improved learning speed",
    "Printed quick-reference cards helped during hands-on exercises",
    "Governance discussion was the highlight -- students connected theory to practice",
    "Live environment gave students realistic experience with production workflows",
    "Instructor ratio (1:{n}) kept all students engaged during lab exercises",
    "Pre-class materials (self-study addendum) prepared students well for day 1",
    "Hands-on exercises were the most effective learning vehicle",
    "Small cohort size enabled personalized instruction and mentoring",
    "Real-world scenario exercises drove strong class discussion",
    "Break schedule kept energy levels high throughout the training day",
    "AAR format at end of each day helped consolidate learning",
    "Cross-functional teams during exercises promoted knowledge sharing",
    "Use of sanitized operational data made exercises immediately relevant",
    "Instructor subject matter expertise was exceptional",
    "Interactive polling during lecture segments maintained engagement",
    "Step-by-step lab guides reduced student confusion during complex tasks",
]

# ---------------------------------------------------------------------------
# Curriculum discrepancy templates
# ---------------------------------------------------------------------------
DISCREPANCY_TEMPLATES = [
    {"document": "TM-30 Section 4.2", "section_page": "p. 23",
     "issue_description": "Pipeline promotion steps reference deprecated API endpoint", "severity": "H"},
    {"document": "TM-10 Chapter 3", "section_page": "pp. 12-15",
     "issue_description": "Screenshots show old UI; navigation steps no longer match", "severity": "M"},
    {"document": "TM-20 Section 6.1", "section_page": "p. 41",
     "issue_description": "Transform syntax example uses deprecated function name", "severity": "H"},
    {"document": "TM-40A Exercise Guide", "section_page": "p. 8",
     "issue_description": "Intelligence scenario references data source no longer available in sandbox", "severity": "M"},
    {"document": "TM-40G Section 2.3", "section_page": "p. 15",
     "issue_description": "Statistical method reference cites wrong formula for normalized gain", "severity": "H"},
    {"document": "SYLLABUS_TM30 Appendix B", "section_page": "p. 3",
     "issue_description": "Equipment list missing required software version numbers", "severity": "L"},
    {"document": "TM-40B Exercise 2", "section_page": "p. 6",
     "issue_description": "Fire mission dataset column headers don't match exercise instructions", "severity": "M"},
    {"document": "TM-20 Section 3.4", "section_page": "p. 28",
     "issue_description": "Code block references Python 3.8 syntax; training env runs 3.12", "severity": "L"},
]

# ---------------------------------------------------------------------------
# AAR definitions — 18 training events across 6 months
# ---------------------------------------------------------------------------
AAR_EVENTS = [
    # TM-10 events (foundation — high volume)
    {"date": date(2025, 10, 6), "tm_levels": ["TM-10"], "exercises": ["EX_10"],
     "location": 0, "students": 15, "instructors": [0, 9],
     "recurring_issues": ["env_access"], "unique_issues": [0],
     "discrepancies": [1], "env_issue": True, "go_rate": 0.87},

    {"date": date(2025, 11, 3), "tm_levels": ["TM-10"], "exercises": ["EX_10"],
     "location": 0, "students": 12, "instructors": [0, 5],
     "recurring_issues": ["env_access_v2"], "unique_issues": [2],
     "discrepancies": [], "env_issue": True, "go_rate": 0.92},

    {"date": date(2025, 12, 9), "tm_levels": ["TM-10"], "exercises": ["EX_10"],
     "location": 4, "students": 10, "instructors": [1, 9],
     "recurring_issues": ["bandwidth"], "unique_issues": [],
     "discrepancies": [1], "env_issue": True, "go_rate": 0.80},

    {"date": date(2026, 1, 13), "tm_levels": ["TM-10"], "exercises": ["EX_10"],
     "location": 0, "students": 14, "instructors": [0, 5],
     "recurring_issues": ["env_access"], "unique_issues": [],
     "discrepancies": [], "env_issue": False, "go_rate": 0.93},

    {"date": date(2026, 2, 10), "tm_levels": ["TM-10"], "exercises": ["EX_10"],
     "location": 0, "students": 11, "instructors": [7, 9],
     "recurring_issues": [], "unique_issues": [6],
     "discrepancies": [], "env_issue": False, "go_rate": 0.91},

    # TM-20 events
    {"date": date(2025, 10, 20), "tm_levels": ["TM-20"], "exercises": ["EX_20"],
     "location": 1, "students": 10, "instructors": [0, 2],
     "recurring_issues": ["tm_outdated"], "unique_issues": [4],
     "discrepancies": [2], "env_issue": False, "go_rate": 0.90},

    {"date": date(2025, 12, 1), "tm_levels": ["TM-20"], "exercises": ["EX_20"],
     "location": 1, "students": 8, "instructors": [1, 2],
     "recurring_issues": ["tm_outdated", "bandwidth"], "unique_issues": [],
     "discrepancies": [7], "env_issue": True, "go_rate": 0.88},

    {"date": date(2026, 2, 3), "tm_levels": ["TM-20"], "exercises": ["EX_20"],
     "location": 1, "students": 9, "instructors": [0, 3],
     "recurring_issues": ["aip_rushed"], "unique_issues": [3],
     "discrepancies": [2], "env_issue": False, "go_rate": 0.89},

    # TM-30 events
    {"date": date(2025, 11, 17), "tm_levels": ["TM-30"], "exercises": ["EX_30"],
     "location": 1, "students": 6, "instructors": [0, 2],
     "recurring_issues": ["time_governance", "env_access"], "unique_issues": [],
     "discrepancies": [0], "env_issue": True, "go_rate": 0.83},

    {"date": date(2026, 1, 27), "tm_levels": ["TM-30"], "exercises": ["EX_30"],
     "location": 1, "students": 7, "instructors": [1, 3],
     "recurring_issues": ["time_governance", "data_quality"], "unique_issues": [1],
     "discrepancies": [0, 5], "env_issue": False, "go_rate": 0.86},

    {"date": date(2026, 3, 3), "tm_levels": ["TM-30"], "exercises": ["EX_30"],
     "location": 1, "students": 8, "instructors": [0, 2, 3],
     "recurring_issues": ["time_governance"], "unique_issues": [],
     "discrepancies": [0], "env_issue": False, "go_rate": 0.88},

    # TM-40 WFF events
    {"date": date(2025, 12, 15), "tm_levels": ["TM-40A"], "exercises": ["EX_40A"],
     "location": 3, "students": 8, "instructors": [0, 4],
     "recurring_issues": ["data_quality"], "unique_issues": [],
     "discrepancies": [3], "env_issue": False, "go_rate": 0.88},

    {"date": date(2026, 1, 20), "tm_levels": ["TM-40B"], "exercises": ["EX_40B"],
     "location": 1, "students": 6, "instructors": [1, 4],
     "recurring_issues": [], "unique_issues": [5],
     "discrepancies": [6], "env_issue": False, "go_rate": 0.83},

    {"date": date(2026, 2, 17), "tm_levels": ["TM-40E"], "exercises": ["EX_40E"],
     "location": 1, "students": 7, "instructors": [0, 5],
     "recurring_issues": ["bandwidth"], "unique_issues": [8],
     "discrepancies": [], "env_issue": True, "go_rate": 0.86},

    # TM-40 Specialist events
    {"date": date(2025, 11, 10), "tm_levels": ["TM-40G"], "exercises": ["EX_40G"],
     "location": 1, "students": 8, "instructors": [2, 6],
     "recurring_issues": ["aip_rushed"], "unique_issues": [],
     "discrepancies": [4], "env_issue": False, "go_rate": 0.88},

    {"date": date(2026, 1, 6), "tm_levels": ["TM-40H"], "exercises": ["EX_40H"],
     "location": 1, "students": 6, "instructors": [2, 8],
     "recurring_issues": [], "unique_issues": [1, 9],
     "discrepancies": [], "env_issue": False, "go_rate": 0.83},

    {"date": date(2026, 2, 24), "tm_levels": ["TM-40K"], "exercises": ["EX_40K"],
     "location": 1, "students": 10, "instructors": [0, 3, 6],
     "recurring_issues": ["data_quality"], "unique_issues": [7],
     "discrepancies": [], "env_issue": False, "go_rate": 0.90},

    {"date": date(2026, 3, 10), "tm_levels": ["TM-40L"], "exercises": ["EX_40L"],
     "location": 1, "students": 7, "instructors": [2, 8],
     "recurring_issues": ["env_access"], "unique_issues": [3],
     "discrepancies": [], "env_issue": True, "go_rate": 0.86},
]


def seed():
    """Insert 18 AARs with full child data."""
    init_db()
    db = SessionLocal()
    try:
        if db.query(AAR).count() > 0:
            print("DB already has data -- skipping seed.")
            return

        random.seed(42)
        total_sustains = 0
        total_improves = 0
        total_evals = 0
        total_discs = 0

        for event in AAR_EVENTS:
            instructor_names = [INSTRUCTORS[i] for i in event["instructors"]]
            location = LOCATIONS[event["location"]]
            n_students = event["students"]

            # Generate objectives text based on TM level
            tm = event["tm_levels"][0]
            planned = _generate_objectives(tm)
            actual = _generate_execution(tm, n_students, event["go_rate"])

            aar = AAR(
                date=event["date"],
                tm_levels=event["tm_levels"],
                exercises=event["exercises"],
                location=location,
                student_count=n_students,
                instructor_names=instructor_names,
                planned_objectives=planned,
                actual_execution=actual,
                instructor_recommendations=_generate_recommendations(event),
                submitted_by=instructor_names[0],
            )
            db.add(aar)
            db.flush()

            # Sustains (3-5 per AAR)
            n_sustains = random.randint(3, 5)
            chosen_sustains = random.sample(SUSTAIN_TEMPLATES, n_sustains)
            for text in chosen_sustains:
                text = text.replace("{n}", str(max(2, n_students // len(instructor_names))))
                db.add(SustainItem(aar_id=aar.id, item_text=text))
                total_sustains += 1

            # Improve items — recurring + unique
            for issue_key in event["recurring_issues"]:
                issue = RECURRING_ISSUES[issue_key]
                db.add(ImproveItem(
                    aar_id=aar.id,
                    problem=issue["problem"],
                    proposed_fix=issue["proposed_fix"],
                    owner=random.choice(["C2DAO", "Lead Instructor", "Curriculum Team", "S6"]),
                    priority=issue["priority"],
                    category=issue["category"],
                ))
                total_improves += 1

            for issue_idx in event["unique_issues"]:
                issue = UNIQUE_ISSUES[issue_idx]
                db.add(ImproveItem(
                    aar_id=aar.id,
                    problem=issue["problem"],
                    proposed_fix=issue["proposed_fix"],
                    owner=random.choice(["Lead Instructor", "Curriculum Team", "S6", "S3"]),
                    priority=issue["priority"],
                    category=issue["category"],
                ))
                total_improves += 1

            # Student evaluations
            eval_names = random.sample(TRAINEE_NAMES, min(n_students, len(TRAINEE_NAMES)))
            for i, name in enumerate(eval_names):
                is_go = random.random() < event["go_rate"]
                notes = ""
                if not is_go:
                    notes = random.choice([
                        "Could not complete filter exercise; remediation scheduled",
                        "Needs additional time on transform configuration",
                        "Did not meet standard on governance tasks; retest next iteration",
                        "Strong conceptually but struggled with hands-on lab portion",
                        "Absent day 2; incomplete; reschedule for next cohort",
                    ])
                else:
                    notes = random.choice([
                        "Strong performer", "Exceeded expectations",
                        "Good progress throughout the course",
                        "Met all standards", "Solid understanding demonstrated",
                        "Excellent class participation", "",
                    ])

                db.add(StudentEvaluation(
                    aar_id=aar.id,
                    trainee_name=name,
                    tm_level=tm,
                    result="GO" if is_go else "NO_GO",
                    notes=notes,
                ))
                total_evals += 1

            # Curriculum discrepancies
            for disc_idx in event["discrepancies"]:
                disc = DISCREPANCY_TEMPLATES[disc_idx]
                db.add(CurriculumDiscrepancy(
                    aar_id=aar.id,
                    document=disc["document"],
                    section_page=disc["section_page"],
                    issue_description=disc["issue_description"],
                    severity=disc["severity"],
                ))
                total_discs += 1

            # Environment issues
            if event["env_issue"]:
                env = _generate_env_issue(event)
                db.add(EnvironmentIssue(
                    aar_id=aar.id,
                    issue=env["issue"],
                    impact=env["impact"],
                    resolution=env["resolution"],
                ))

        db.commit()
        print(f"Seeded {len(AAR_EVENTS)} AARs: {total_sustains} sustains, "
              f"{total_improves} improves, {total_evals} evaluations, "
              f"{total_discs} discrepancies.")
    finally:
        db.close()


def _generate_objectives(tm_level: str) -> str:
    """Generate realistic planned objectives based on TM level."""
    objectives = {
        "TM-10": ("Complete all TM-10 ELOs: navigate MSS interface, view datasets, "
                   "read/interpret dashboards, apply filters, verify data currency, "
                   "respond to misrouted data per AIP procedures."),
        "TM-20": ("Complete all TM-20 ELOs: create data connections, build basic "
                   "pipelines, configure transforms, document pipeline changes, "
                   "complete data quality checklist."),
        "TM-30": ("Complete all TM-30 ELOs: build complex pipelines, implement "
                   "governance controls, configure access management, promote "
                   "pipeline to production, complete C2DAO governance checklist."),
        "TM-40A": ("Complete TM-40A ELOs: apply intelligence WFF concepts to MSS, "
                    "build intelligence-focused dashboards, configure intel data flows, "
                    "demonstrate understanding of intel data governance."),
        "TM-40B": ("Complete TM-40B ELOs: configure fire support data pipelines, "
                    "build fires-specific dashboards, integrate targeting data, "
                    "demonstrate fires data quality assessment."),
        "TM-40E": ("Complete TM-40E ELOs: configure protection data flows, build "
                    "force protection dashboards, implement security classification "
                    "controls, demonstrate protection data governance."),
        "TM-40G": ("Complete TM-40G ELOs: apply ORSA methods in MSS, build "
                    "analytical models, configure statistical pipelines, demonstrate "
                    "operational research data analysis techniques."),
        "TM-40H": ("Complete TM-40H ELOs: implement AI/ML pipelines in MSS, "
                    "configure model training workflows, build AI-powered dashboards, "
                    "demonstrate responsible AI practices."),
        "TM-40K": ("Complete TM-40K ELOs: build knowledge management systems in MSS, "
                    "configure taxonomy structures, implement search and discovery, "
                    "demonstrate KM governance processes."),
        "TM-40L": ("Complete TM-40L ELOs: use Platform SDK for MSS development, "
                    "implement custom applications, configure CI/CD pipelines, "
                    "demonstrate software engineering best practices in MSS."),
    }
    return objectives.get(tm_level, f"Complete all {tm_level} end-of-lesson objectives.")


def _generate_execution(tm_level: str, n_students: int, go_rate: float) -> str:
    """Generate realistic execution summary."""
    n_go = round(n_students * go_rate)
    n_nogo = n_students - n_go

    base = f"{n_go} of {n_students} students completed all objectives."
    if n_nogo > 0:
        base += f" {n_nogo} student{'s' if n_nogo > 1 else ''} required additional mentoring"
        base += random.choice([
            " and will be rescheduled for the next iteration.",
            "; remediation training scheduled.",
            " on specific task areas.",
        ])

    extras = random.choice([
        " Class discussion exceeded expectations on governance topics.",
        " Hands-on lab exercises drove strong engagement.",
        " Session ran slightly long due to excellent class discussion.",
        " All exercises completed within allocated time.",
        " Students demonstrated strong foundational knowledge.",
    ])

    return base + extras


def _generate_recommendations(event: dict) -> str:
    """Generate instructor recommendations based on event issues."""
    recs = []
    if event["env_issue"]:
        recs.append("Pre-stage all environment access credentials 48 hrs before class.")
    if event["go_rate"] < 0.85:
        recs.append("Consider adding pre-class readiness assessment to identify gaps early.")
    if event["students"] > 12:
        recs.append("Request additional instructor for cohorts exceeding 12 students.")

    recs.append(random.choice([
        "Continue pairing experienced operators with new students.",
        "Increase hands-on exercise time by reducing lecture blocks.",
        "Develop additional scenario-based exercises for advanced students.",
        "Consider splitting cohort into breakout groups for lab exercises.",
    ]))

    return " ".join(recs)


def _generate_env_issue(event: dict) -> dict:
    """Generate a realistic environment issue."""
    issues = [
        {"issue": "Sandbox login credentials not pre-staged",
         "impact": "30-minute delay at start of training",
         "resolution": "Coordinated with C2DAO for pre-staging next iteration"},
        {"issue": "Network bandwidth degradation during peak training hours",
         "impact": "Slow dashboard loading; 2 students unable to complete timed exercise",
         "resolution": "S6 investigating dedicated bandwidth allocation"},
        {"issue": "Training environment data refresh failed overnight",
         "impact": "Stale data in exercises; instructor had to improvise workaround",
         "resolution": "Automated data refresh script added to pre-class checklist"},
        {"issue": "Browser compatibility issue with training environment",
         "impact": "3 workstations required browser update before students could log in",
         "resolution": "Added browser version check to environment setup SOP"},
    ]
    return random.choice(issues)


if __name__ == "__main__":
    seed()
