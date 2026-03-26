"""Seed realistic demo data for the Lessons Learned Pipeline.

Generates ~40 lessons with tags, action items, and comments spanning
6 months of training operations.
"""

from __future__ import annotations

import random
from datetime import UTC, date, datetime, timedelta

from .db import (
    ActionItem,
    Lesson,
    LessonComment,
    LessonTag,
    SessionLocal,
    TTP_CATEGORIES,
    ECHELONS,
    WFF_CATEGORIES,
    DOCTRINE_REFS,
    init_db,
)

# ---------------------------------------------------------------------------
# Realistic lesson titles and descriptions
# ---------------------------------------------------------------------------
LESSON_DATA = [
    (
        "Data pipeline latency exceeds SLA during surge operations",
        "During EXERCISE SABER STRIKE 26, data ingestion pipelines experienced 4x normal latency when multiple battalions submitted concurrent updates. Root cause: single-threaded ETL process without queue management.",
        "AAR", "AAR-2026-042",
    ),
    (
        "Visualization standards inconsistent across WFF dashboards",
        "Intelligence, fires, and sustainment dashboards use different color scales and chart types for identical metric categories. Users report confusion when switching between WFF views.",
        "FIELD_OBSERVATION", None,
    ),
    (
        "SL 4K students lack prerequisite data modeling knowledge",
        "Three of eight SL 4K students could not complete the entity resolution exercise within allotted time. Pre-assessment shows gap in relational data modeling fundamentals covered in SL 3.",
        "INSTRUCTOR_NOTE", "TM40K-CLS-003",
    ),
    (
        "Maven query performance degrades with large temporal datasets",
        "Queries spanning more than 90 days of operational data consistently timeout at the default 30-second threshold. Affects daily SITREP generation for BDE-level consumers.",
        "FIELD_OBSERVATION", None,
    ),
    (
        "AAR data collection form missing key taxonomy fields",
        "Current digital AAR collection form does not include fields for echelon, WFF, or TTP category. Manual tagging post-collection introduces 48-72 hour delay and inconsistent classification.",
        "AAR", "AAR-2026-018",
    ),
    (
        "Cross-functional analysis reveals fires-intelligence data gap",
        "Attempted cross-WFF analysis between fires and intelligence data layers failed due to incompatible entity keys. No shared reference identifier between DCGS-A exports and AFATDS data feeds.",
        "EXERCISE", "EX-COMBINED-RESOLVE-26",
    ),
    (
        "Student feedback: SL 4H lab environment insufficient",
        "AI Engineer track students report that the provided lab VM has insufficient GPU memory for the transformer fine-tuning exercise. Four of six students could not complete Lab 3.",
        "STUDENT_FEEDBACK", "TM40H-EVAL-Q2",
    ),
    (
        "Quality control process catches zero schema violations in Q1",
        "Automated schema validation pipeline detected zero violations in Q1 2026 across 12,000+ ingested records. Suggests either perfect data quality (unlikely) or misconfigured validators.",
        "FIELD_OBSERVATION", None,
    ),
    (
        "Dissemination lag between BDE and BN-level consumers",
        "Processed intelligence products take 6-8 hours to propagate from BDE analytical cell to BN-level Maven dashboards. Expected SLA is 2 hours.",
        "AAR", "AAR-2026-031",
    ),
    (
        "Platform admin credentials shared across multiple operators",
        "Audit revealed three separate units using shared service accounts for Maven platform administration. Violates least-privilege principles and prevents attribution of configuration changes.",
        "FIELD_OBSERVATION", None,
    ),
    (
        "Integration test failures during NIPR-SIPR data bridge exercise",
        "Bi-directional data synchronization between NIPR and SIPR Maven instances failed 40% of transfer attempts. Error logs indicate certificate rotation timing mismatch.",
        "EXERCISE", "EX-CYBER-GUARD-26",
    ),
    (
        "Battalion S2 shops underutilize advanced builder capabilities",
        "Observation across 5 BN S2 sections shows that SL 3 qualified analysts use less than 20% of available advanced builder features. Default to basic query/filter patterns from SL 1.",
        "FIELD_OBSERVATION", None,
    ),
    (
        "SL 4G ORSA students excel at statistical methods but struggle with operational context",
        "ORSA track students consistently score well on statistical methodology assessments but perform poorly when asked to translate analytical results into operationally relevant recommendations.",
        "INSTRUCTOR_NOTE", "TM40G-CLS-005",
    ),
    (
        "Successful rapid dashboard deployment for DEFENDER 26",
        "Team deployed 4 custom operational dashboards within 72 hours of exercise STARTEX. Pre-built templates from SL 3 curriculum accelerated development. Recommend maintaining template library.",
        "AAR", "AAR-2026-055",
    ),
    (
        "Data collection at company level hampered by connectivity",
        "Company-level data collectors in field environment experienced intermittent TACNET connectivity, resulting in 30% data loss during movement phases. No offline caching mechanism available.",
        "EXERCISE", "EX-SABER-STRIKE-26",
    ),
    (
        "Sustainment data feeds lack standardized unit identifiers",
        "GCSS-Army export files use different unit identification schemes than Maven platform. Manual crosswalk required for each data refresh, consuming 2 hours per sustainment analyst per day.",
        "FIELD_OBSERVATION", None,
    ),
    (
        "Instructor development gap in advanced ML concepts",
        "Only 2 of 5 certified SL 4M instructors can effectively teach the ensemble methods module. Remaining instructors default to reading slides. Faculty development program needed.",
        "INSTRUCTOR_NOTE", "FACULTY-DEV-2026",
    ),
    (
        "Protection WFF dashboard successfully integrated CBRN sensor feeds",
        "SL 4E qualified analyst successfully integrated real-time CBRN sensor data into protection dashboard during CBRN EXERCISE TOXIC LANCE. Reduced manual reporting time by 75%.",
        "AAR", "AAR-2026-063",
    ),
    (
        "Student retention rates drop after SL 2 to SL 3 transition",
        "Analysis of 6 cohorts shows 35% of SL 2 graduates do not enroll in SL 3 within 90 days. Primary reported reason: insufficient unit support for training time allocation.",
        "STUDENT_FEEDBACK", "ENROLLMENT-ANALYSIS-Q1",
    ),
    (
        "Mission command COP visualization renders slowly on tactical displays",
        "Common Operating Picture built for mission command track renders in 45+ seconds on standard tactical workstations. Exceeds 10-second usability threshold for real-time decision support.",
        "FIELD_OBSERVATION", None,
    ),
    (
        "Data processing scripts fail silently on malformed date fields",
        "ETL pipeline for daily LOGSTAT ingestion silently drops records with non-ISO date formats. No alerting mechanism; discovered only during monthly reconciliation audit.",
        "FIELD_OBSERVATION", None,
    ),
    (
        "Cross-WFF correlation analysis identifies movement-sustainment dependency",
        "Novel analysis by SL 5G student identified strong correlation between movement tempo and sustainment demand signals 48 hours in advance. Potential predictive model for logistics planning.",
        "EXERCISE", "EX-COMBINED-RESOLVE-26",
    ),
    (
        "SL 4J program managers need more hands-on technical exposure",
        "Program manager track students consistently request more technical lab time. Current 60/40 lecture/lab split should shift to 40/60 based on end-of-course evaluations.",
        "STUDENT_FEEDBACK", "TM40J-EVAL-Q1",
    ),
    (
        "Analysis products lack standardized metadata headers",
        "Intelligence and fires analysis products published to Maven have no consistent metadata schema. Consumers cannot programmatically filter by classification, time window, or AOR.",
        "FIELD_OBSERVATION", None,
    ),
    (
        "Effective use of data quality scorecards at Division level",
        "Division G2 implemented weekly data quality scorecard based on SL 4K curriculum. Improved source data completeness from 62% to 91% within 8 weeks.",
        "AAR", "AAR-2026-072",
    ),
    (
        "Software engineer track needs updated API security module",
        "SL 4L API security lab uses deprecated authentication patterns. Industry standard moved to OAuth 2.1 and PKCE flows; curriculum references OAuth 2.0 implicit grant.",
        "INSTRUCTOR_NOTE", "TM40L-REVIEW-Q2",
    ),
    (
        "Field observation: operators bypass data validation to meet deadlines",
        "Under time pressure during exercise play, operators routinely disable client-side validation to force-submit incomplete records. Downstream data quality severely impacted.",
        "FIELD_OBSERVATION", None,
    ),
    (
        "Echelon-appropriate data granularity not enforced in dashboards",
        "Theater-level dashboard displays squad-level detail by default, overwhelming decision makers. No role-based filtering to constrain data presentation by echelon.",
        "FIELD_OBSERVATION", None,
    ),
    (
        "Student feedback: SL 4G statistics prerequisites insufficient",
        "ORSA students without undergraduate statistics background struggle in weeks 2-4. Recommend adding optional pre-course statistics refresher module.",
        "STUDENT_FEEDBACK", "TM40G-EVAL-Q2",
    ),
    (
        "Fires WFF data integration successful with JADOCS prototype",
        "Prototype JADOCS integration developed during SL 4B demonstrated automated joint fires data flow. Reduced manual data entry from 45 minutes to 5 minutes per fire mission.",
        "EXERCISE", "EX-FIRES-FOCUS-26",
    ),
    (
        "Knowledge management taxonomy misaligned with operational vocabulary",
        "SL 4K taxonomy uses academic data management terminology that field operators do not recognize. Recommend glossary alignment pass with operational SMEs.",
        "INSTRUCTOR_NOTE", "TM40K-CLS-004",
    ),
    (
        "Successful multi-domain data fusion during PACIFIC PATHWAYS",
        "Team achieved first-ever automated fusion of maritime, air, and ground domain data in Maven platform. Processing time: 12 minutes for 3-domain correlation. Manual process: 4+ hours.",
        "AAR", "AAR-2026-081",
    ),
    (
        "Data collection SOPs need echelon-specific variants",
        "Single data collection SOP applied across all echelons creates friction. Squad-level collectors report excessive field requirements; BDE-level analysts report insufficient granularity.",
        "FIELD_OBSERVATION", None,
    ),
    (
        "SL 5H advanced AI students produce deployment-ready models",
        "Three of five SL 5H students produced ML models that passed operational testing and were deployed to production. Highest conversion rate of any advanced track cohort.",
        "INSTRUCTOR_NOTE", "TM50H-CLS-002",
    ),
    (
        "Integration between Maven and CPOF requires manual data export",
        "No automated data bridge between Maven analytical products and CPOF mission command displays. Operators resort to screenshot-and-email workflow, defeating automation intent.",
        "FIELD_OBSERVATION", None,
    ),
    (
        "Quality control metrics dashboard adopted by 3 divisions",
        "Data quality scorecard template developed in SL 4K now deployed at 3 USAREUR-AF divisions. Consistent metrics enable cross-division quality benchmarking for first time.",
        "AAR", "AAR-2026-089",
    ),
    (
        "Student feedback: exercise scenarios need classified data equivalents",
        "Students report that unclassified exercise data lacks the complexity of operational data. Recommend developing synthetic datasets that mirror classified data structures and volumes.",
        "STUDENT_FEEDBACK", "ALL-TRACK-EVAL-Q1",
    ),
    (
        "Processing bottleneck at GEOINT layer fusion step",
        "GEOINT data layer fusion consumes 80% of total processing time in the intelligence analysis pipeline. Single-node processing architecture cannot parallelize spatial joins.",
        "FIELD_OBSERVATION", None,
    ),
    (
        "Movement and maneuver tracker improves BDE battle rhythm",
        "SL 4C qualified analyst built automated movement tracker that replaced 3 manual Excel trackers. BDE S3 reports 2-hour reduction in daily battle rhythm update cycle.",
        "AAR", "AAR-2026-094",
    ),
    (
        "Doctrine references in curriculum need annual review cycle",
        "Multiple curriculum modules reference superseded doctrine publications. ADP 3-0 update (2025) not yet reflected in SL 4A through SL 4F course materials.",
        "INSTRUCTOR_NOTE", "CURRICULUM-REVIEW-2026",
    ),
]

# Submitters — mix of ranks and roles
SUBMITTERS = [
    "MAJ Torres", "CPT Chen", "CW3 Williams", "SFC Henderson",
    "MAJ Smith", "CPT Patel", "1LT Jackson", "CW2 Davis",
    "MSG Taylor", "CPT Rivera", "MAJ Garcia", "SFC Brooks",
]

# Comment authors
COMMENTERS = [
    "MAJ Torres", "CPT Chen", "CW3 Williams", "LTC Ford",
    "COL Stewart", "CW4 Kim", "MAJ Smith", "CPT Patel",
]

# Comment templates
COMMENT_TEMPLATES = [
    "Concur with this observation. We saw similar issues during our last rotation.",
    "Recommend prioritizing this for the next curriculum review board.",
    "This aligns with feedback from the SL 4K cohort. Cross-referencing with their AARs.",
    "Action item assigned to S6 section for technical resolution.",
    "Validated by independent observation during EXERCISE COMBINED RESOLVE.",
    "Escalating to TRADOC POC for potential doctrine update.",
    "Adding this to the quarterly training management review agenda.",
    "Similar finding reported by 2-1 IN BN. Consolidating observations.",
    "Disagree with priority assessment. Recommend upgrading to HIGH based on impact scope.",
    "Closing loop on this — fix deployed in latest platform update.",
    "Student evaluations from last 3 cohorts corroborate this finding.",
    "Forwarding to faculty development team for instructor remediation plan.",
    "This is a known limitation. Workaround documented in JIRA ticket MSS-2847.",
    "Recommend adding this as a scenario inject for the next training exercise.",
    "Good capture. Tagging for inclusion in the annual lessons learned digest.",
]

# Action item description templates
ACTION_TEMPLATES = [
    "Update ETL pipeline to handle concurrent batch submissions",
    "Standardize dashboard color scales across all WFF views",
    "Develop pre-assessment module for SL 4K prerequisites",
    "Implement query timeout scaling based on date range",
    "Add taxonomy fields to digital AAR collection form",
    "Create shared entity reference mapping between DCGS-A and AFATDS",
    "Provision GPU-enabled lab VMs for SL 4H exercises",
    "Audit and reconfigure schema validation rules",
    "Reduce BDE-to-BN dissemination pipeline to 2-hour SLA",
    "Implement individual service accounts per operator",
    "Resolve certificate rotation timing for NIPR-SIPR bridge",
    "Develop advanced builder feature adoption training module",
    "Create operational context translation guide for ORSA students",
    "Maintain and version-control dashboard template library",
    "Implement offline data caching for field collectors",
    "Build automated GCSS-Army unit identifier crosswalk",
    "Schedule faculty development workshop for ML instructors",
    "Optimize COP rendering for tactical display specifications",
    "Add alerting for silently dropped ETL records",
    "Create role-based echelon filters for all dashboards",
    "Develop synthetic classified-equivalent training datasets",
    "Parallelize GEOINT spatial join processing",
    "Conduct annual doctrine reference alignment review",
    "Shift SL 4J lab/lecture ratio to 40/60",
    "Develop optional statistics refresher for SL 4G pre-course",
]

# Assignees for action items
ASSIGNEES = [
    "S6 Section", "Training Branch", "Platform Team", "CPT Chen",
    "CW3 Williams", "MAJ Torres", "Faculty Dev Team", "Data Eng Cell",
    None, None,  # Some unassigned
]


def _random_date(start: date, end: date) -> date:
    """Random date between start and end inclusive."""
    delta = (end - start).days
    return start + timedelta(days=random.randint(0, max(delta, 0)))


def seed():
    """Insert demo data: ~40 lessons, ~25 action items, ~30 comments."""
    init_db()
    db = SessionLocal()
    try:
        if db.query(Lesson).count() > 0:
            print("DB already has data -- skipping seed.")
            return

        random.seed(42)  # deterministic for reproducible demos

        # Timeline: lessons spanning 6 months
        timeline_start = date(2025, 10, 1)
        timeline_end = date(2026, 3, 15)

        # --- Create lessons ---
        lessons = []
        for i, (title, desc, src_type, src_ref) in enumerate(LESSON_DATA):
            submit_dt = _random_date(timeline_start, timeline_end)

            # Assign status based on age — older lessons more likely to be progressed
            days_old = (timeline_end - submit_dt).days
            if days_old > 120:
                status_choice = random.choice(["IMPLEMENTED", "ARCHIVED", "ACTIONABLE"])
            elif days_old > 60:
                status_choice = random.choice(["VALIDATED", "ACTIONABLE", "IMPLEMENTED"])
            elif days_old > 30:
                status_choice = random.choice(["NEW", "VALIDATED", "ACTIONABLE"])
            else:
                status_choice = random.choice(["NEW", "NEW", "VALIDATED"])

            priority = random.choice(["HIGH", "HIGH", "MEDIUM", "MEDIUM", "MEDIUM", "LOW"])

            lesson = Lesson(
                title=title,
                description=desc,
                source_type=src_type,
                source_reference=src_ref,
                submitted_by=random.choice(SUBMITTERS),
                submit_date=submit_dt,
                status=status_choice,
                priority=priority,
            )
            db.add(lesson)
            db.flush()  # Get the lesson.id
            lessons.append(lesson)

        # --- Tag each lesson (2-4 tags per lesson) ---
        course_ids = ["SL 4G", "SL 4H", "SL 4M", "SL 4J", "SL 4K", "SL 4L",
                       "SL 5G", "SL 5H", "SL 4A", "SL 4B", "SL 4C", "SL 4D",
                       "SL 4E", "SL 4F", "SL 3"]

        for lesson in lessons:
            tags_added: set[tuple[str, str]] = set()

            # Always add a TTP category tag
            ttp = random.choice(TTP_CATEGORIES)
            tags_added.add(("TTP_CATEGORY", ttp))
            db.add(LessonTag(lesson_id=lesson.id, tag_type="TTP_CATEGORY", tag_value=ttp))

            # Always add a WFF tag
            wff = random.choice(WFF_CATEGORIES)
            tags_added.add(("WFF", wff))
            db.add(LessonTag(lesson_id=lesson.id, tag_type="WFF", tag_value=wff))

            # 60% chance of echelon tag
            if random.random() < 0.6:
                ech = random.choice(ECHELONS)
                key = ("ECHELON", ech)
                if key not in tags_added:
                    tags_added.add(key)
                    db.add(LessonTag(lesson_id=lesson.id, tag_type="ECHELON", tag_value=ech))

            # 50% chance of doctrine ref tag
            if random.random() < 0.5:
                doc = random.choice(DOCTRINE_REFS)
                key = ("DOCTRINE_REF", doc)
                if key not in tags_added:
                    tags_added.add(key)
                    db.add(LessonTag(lesson_id=lesson.id, tag_type="DOCTRINE_REF", tag_value=doc))

            # 40% chance of course ID tag
            if random.random() < 0.4:
                cid = random.choice(course_ids)
                key = ("COURSE_ID", cid)
                if key not in tags_added:
                    tags_added.add(key)
                    db.add(LessonTag(lesson_id=lesson.id, tag_type="COURSE_ID", tag_value=cid))

        # --- Create action items (~25 total) ---
        action_count = 0
        action_lessons = random.sample(lessons, min(25, len(lessons)))
        for j, lesson in enumerate(action_lessons):
            if action_count >= 25:
                break

            action_desc = ACTION_TEMPLATES[j % len(ACTION_TEMPLATES)]
            due = lesson.submit_date + timedelta(days=random.randint(14, 90))

            # Status distribution: mix of OPEN, IN_PROGRESS, COMPLETED
            if lesson.status in ("IMPLEMENTED", "ARCHIVED"):
                act_status = random.choice(["COMPLETED", "COMPLETED", "CANCELLED"])
                comp_date = _random_date(lesson.submit_date + timedelta(days=14), timeline_end)
            elif lesson.status == "ACTIONABLE":
                act_status = random.choice(["OPEN", "IN_PROGRESS", "COMPLETED"])
                comp_date = (
                    _random_date(lesson.submit_date + timedelta(days=14), timeline_end)
                    if act_status == "COMPLETED" else None
                )
            else:
                act_status = random.choice(["OPEN", "OPEN", "IN_PROGRESS"])
                comp_date = None

            db.add(ActionItem(
                lesson_id=lesson.id,
                description=action_desc,
                assigned_to=random.choice(ASSIGNEES),
                due_date=due,
                status=act_status,
                completed_date=comp_date,
            ))
            action_count += 1

        # --- Create comments (~30 total) ---
        comment_count = 0
        comment_lessons = random.choices(lessons, k=30)
        for lesson in comment_lessons:
            if comment_count >= 30:
                break

            comment_dt = datetime.combine(
                _random_date(lesson.submit_date, timeline_end),
                datetime.min.time(),
            ).replace(tzinfo=UTC)

            db.add(LessonComment(
                lesson_id=lesson.id,
                author=random.choice(COMMENTERS),
                comment_text=random.choice(COMMENT_TEMPLATES),
                comment_date=comment_dt,
            ))
            comment_count += 1

        db.commit()
        print(
            f"Seeded {len(lessons)} lessons, {action_count} action items, "
            f"{comment_count} comments."
        )
    finally:
        db.close()


if __name__ == "__main__":
    seed()
