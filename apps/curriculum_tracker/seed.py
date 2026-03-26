"""Seed realistic demo data for the Curriculum Tracker.

Scans the actual maven_training/ directory for real file paths and hashes.
Falls back to generated data if the directory doesn't exist at runtime.
Adds review cycles and changelog entries spanning 6 months.
"""

from __future__ import annotations

import hashlib
import os
import random
from datetime import UTC, date, datetime, timedelta
from pathlib import Path

from .db import (
    ChangeLog,
    Document,
    ReviewCycle,
    SessionLocal,
    init_db,
    _classify_doc_type,
    _extract_course_id,
    _extract_title,
    _compute_sha256,
)

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------
REVIEWERS = ["MAJ SMITH", "CW3 DAVIS", "SFC HENDERSON", "MSG TAYLOR", "MAJ JOHNSON"]

REVIEW_TYPES = ["SCHEDULED", "AD_HOC", "POST_EXERCISE"]
REVIEW_STATUSES = ["APPROVED", "CHANGES_REQUIRED", "IN_REVIEW", "OVERDUE"]

# Repo root — two levels up from this file
_REPO_ROOT = Path(__file__).resolve().parent.parent.parent
MAVEN_TRAINING_PATH = _REPO_ROOT / "maven_training"

# Fallback fake documents if maven_training/ doesn't exist
FAKE_DOCS = [
    ("maven_training/tm/TM_10_maven_user/TM_10_MAVEN_USER.md", "TM", "SL 1"),
    ("maven_training/tm/TM_20_builder/TM_20_BUILDER.md", "TM", "SL 2"),
    ("maven_training/tm/TM_20_builder/CONCEPTS_GUIDE_TM20_BUILDER.md", "TM", "SL 2"),
    ("maven_training/tm/TM_30_advanced_builder/TM_30_ADVANCED_BUILDER.md", "TM", "SL 3"),
    ("maven_training/tm/TM_30_advanced_builder/CONCEPTS_GUIDE_TM30_ADVANCED_BUILDER.md", "TM", "SL 3"),
    ("maven_training/tm/TM_30_advanced_builder/SELF_STUDY_ADDENDUM.md", "TM", "SL 3"),
    ("maven_training/tm/TM_40A_intelligence/TM_40A_INTELLIGENCE.md", "TM", "SL 4A"),
    ("maven_training/tm/TM_40A_intelligence/CONCEPTS_GUIDE_TM40A_INTELLIGENCE.md", "TM", "SL 4A"),
    ("maven_training/tm/TM_40B_fires/TM_40B_FIRES.md", "TM", "SL 4B"),
    ("maven_training/tm/TM_40B_fires/CONCEPTS_GUIDE_TM40B_FIRES.md", "TM", "SL 4B"),
    ("maven_training/tm/TM_40C_movement_maneuver/TM_40C_MOVEMENT_MANEUVER.md", "TM", "SL 4C"),
    ("maven_training/tm/TM_40D_sustainment/TM_40D_SUSTAINMENT.md", "TM", "SL 4D"),
    ("maven_training/tm/TM_40E_protection/TM_40E_PROTECTION.md", "TM", "SL 4E"),
    ("maven_training/tm/TM_40F_mission_command/TM_40F_MISSION_COMMAND.md", "TM", "SL 4F"),
    ("maven_training/tm/TM_40G_orsa/TM_40G_ORSA.md", "TM", "SL 4G"),
    ("maven_training/tm/TM_40H_ai_engineer/TM_40H_AI_ENGINEER.md", "TM", "SL 4H"),
    ("maven_training/tm/TM_40M_ml_engineer/TM_40M_ML_ENGINEER.md", "TM", "SL 4M"),
    ("maven_training/tm/TM_40J_program_manager/TM_40J_PROGRAM_MANAGER.md", "TM", "SL 4J"),
    ("maven_training/tm/TM_40K_knowledge_manager/CONCEPTS_GUIDE_TM40K_KNOWLEDGE_MANAGER.md", "TM", "SL 4K"),
    ("maven_training/tm/TM_40L_software_engineer/TM_40L_SOFTWARE_ENGINEER.md", "TM", "SL 4L"),
    ("maven_training/tm/TM_50G_orsa_advanced/TM_50G_ORSA_ADVANCED.md", "TM", "SL 5G"),
    ("maven_training/tm/TM_50H_ai_engineer_advanced/TM_50H_AI_ENGINEER_ADVANCED.md", "TM", "SL 5H"),
    ("maven_training/tm/TM_50M_ml_engineer_advanced/TM_50M_ML_ENGINEER_ADVANCED.md", "TM", "SL 5M"),
    ("maven_training/tm/TM_50J_program_manager_advanced/TM_50J_PROGRAM_MANAGER_ADVANCED.md", "TM", "SL 5J"),
    ("maven_training/tm/TM_50K_knowledge_manager_advanced/TM_50K_KNOWLEDGE_MANAGER_ADVANCED.md", "TM", "SL 5K"),
    ("maven_training/tm/TM_50L_software_engineer_advanced/TM_50L_SOFTWARE_ENGINEER_ADVANCED.md", "TM", "SL 5L"),
    ("maven_training/syllabi/SYLLABUS_TM10.md", "SYLLABUS", "SL 1"),
    ("maven_training/syllabi/SYLLABUS_TM20.md", "SYLLABUS", "SL 2"),
    ("maven_training/syllabi/SYLLABUS_TM30.md", "SYLLABUS", "SL 3"),
    ("maven_training/syllabi/SYLLABUS_TM40J.md", "SYLLABUS", "SL 4J"),
    ("maven_training/syllabi/SYLLABUS_TM40M.md", "SYLLABUS", "SL 4M"),
    ("maven_training/syllabi/SYLLABUS_TM50G.md", "SYLLABUS", "SL 5G"),
    ("maven_training/syllabi/SYLLABUS_TM50H.md", "SYLLABUS", "SL 5H"),
    ("maven_training/syllabi/SYLLABUS_TM50L.md", "SYLLABUS", "SL 5L"),
    ("maven_training/syllabi/SYLLABUS_TM50M.md", "SYLLABUS", "SL 5M"),
    ("maven_training/exercises/EX_10_operator_basics/EXERCISE.md", "EXERCISE", "SL 1"),
    ("maven_training/exercises/EX_30_advanced_builder/EXERCISE.md", "EXERCISE", "SL 3"),
    ("maven_training/exercises/EX_40G_orsa/EXERCISE.md", "EXERCISE", "SL 4G"),
    ("maven_training/exercises/EX_40H_ai_engineer/EXERCISE.md", "EXERCISE", "SL 4H"),
    ("maven_training/exercises/EX_40J_program_manager/EXERCISE.md", "EXERCISE", "SL 4J"),
    ("maven_training/exercises/exams/EXAM_TM30_POST.md", "EXAM", "SL 3"),
    ("maven_training/exercises/exams/EXAM_TM40J_PRE.md", "EXAM", "SL 4J"),
    ("maven_training/exercises/exams/EXAM_TM40M_POST.md", "EXAM", "SL 4M"),
    ("maven_training/exercises/exams/EXAM_TM40M_PRE.md", "EXAM", "SL 4M"),
    ("maven_training/doctrine/cda_doctrine/CDA_OVERVIEW.md", "DOCTRINE", None),
    ("maven_training/doctrine/gdap/GDAP_OVERVIEW.md", "DOCTRINE", None),
    ("maven_training/doctrine/gdap/GDAP_VISION.md", "DOCTRINE", None),
    ("maven_training/doctrine/mim/MIM_OVERVIEW.md", "DOCTRINE", None),
    ("maven_training/training_management/INSTRUCTOR_OVERVIEW.md", "ADMIN", None),
    ("maven_training/training_management/ENROLLMENT_SOP.md", "ADMIN", None),
    ("maven_training/training_management/CURRICULUM_MAINTENANCE_SOP.md", "ADMIN", None),
]


def _random_date(start: date, end: date) -> date:
    """Random date between start and end inclusive."""
    delta = (end - start).days
    return start + timedelta(days=random.randint(0, max(delta, 0)))


def _fake_hash() -> str:
    """Generate a fake SHA-256 hash for demo data."""
    return hashlib.sha256(str(random.random()).encode()).hexdigest()


def _scan_real_directory(db) -> list[Document]:
    """Scan actual maven_training/ and insert documents with real hashes."""
    docs = []
    base = MAVEN_TRAINING_PATH

    for root, _dirs, files in os.walk(base):
        for fname in files:
            if not fname.endswith(".md"):
                continue

            full_path = os.path.join(root, fname)
            rel_path = os.path.relpath(full_path, base.parent)
            file_hash = _compute_sha256(full_path)
            mod_time = datetime.fromtimestamp(
                os.path.getmtime(full_path), tz=UTC
            )

            doc = Document(
                file_path=rel_path,
                doc_type=_classify_doc_type(rel_path),
                course_id=_extract_course_id(rel_path),
                title=_extract_title(fname),
                file_hash=file_hash,
                last_modified=mod_time,
            )
            db.add(doc)
            docs.append(doc)

    db.flush()
    return docs


def _insert_fake_documents(db) -> list[Document]:
    """Insert ~50 fake document entries as fallback."""
    docs = []
    for file_path, doc_type, course_id in FAKE_DOCS:
        doc = Document(
            file_path=file_path,
            doc_type=doc_type,
            course_id=course_id,
            title=_extract_title(Path(file_path).name),
            file_hash=_fake_hash(),
            last_modified=datetime.now(UTC) - timedelta(days=random.randint(1, 180)),
        )
        db.add(doc)
        docs.append(doc)

    db.flush()
    return docs


def seed():
    """Insert demo data: documents from real directory scan (or fallback),
    review cycles, and changelog entries spanning 6 months."""
    init_db()
    db = SessionLocal()
    try:
        if db.query(Document).count() > 0:
            print("DB already has data -- skipping seed.")
            return

        random.seed(42)

        # --- Insert documents ---
        if MAVEN_TRAINING_PATH.exists():
            print(f"Scanning real directory: {MAVEN_TRAINING_PATH}")
            docs = _scan_real_directory(db)
            print(f"  Found {len(docs)} .md files")
        else:
            print("maven_training/ not found — using fallback data")
            docs = _insert_fake_documents(db)
            print(f"  Inserted {len(docs)} fake documents")

        # --- Generate review cycles ---
        # Not every doc gets a review; ~70% get at least one
        timeline_start = date(2025, 9, 1)
        timeline_end = date(2026, 3, 15)

        review_count = 0
        for doc in docs:
            if random.random() > 0.70:
                continue  # ~30% never reviewed

            # 1-3 reviews per document over the 6-month window
            num_reviews = random.randint(1, 3)
            for i in range(num_reviews):
                review_date = _random_date(timeline_start, timeline_end)

                # Status distribution: 50% APPROVED, 15% CHANGES_REQUIRED,
                # 20% IN_REVIEW, 15% OVERDUE
                roll = random.random()
                if roll < 0.50:
                    status = "APPROVED"
                elif roll < 0.65:
                    status = "CHANGES_REQUIRED"
                elif roll < 0.85:
                    status = "IN_REVIEW"
                else:
                    status = "OVERDUE"

                # Set next_review_date for non-final reviews
                next_review = None
                if status in ("APPROVED", "CHANGES_REQUIRED"):
                    next_review = review_date + timedelta(days=random.choice([90, 120, 180]))
                elif status == "IN_REVIEW":
                    # Some IN_REVIEW have upcoming next dates, some are past due
                    next_review = review_date + timedelta(days=random.randint(14, 60))
                elif status == "OVERDUE":
                    # Overdue: next_review_date is in the past
                    next_review = review_date - timedelta(days=random.randint(7, 60))

                notes_options = [
                    None,
                    "Content current and accurate",
                    "Minor formatting updates needed",
                    "References need updating per latest ADP",
                    "Diagrams outdated — request SME review",
                    "Aligned with CURRICULUM_MAINTENANCE_SOP v2.1",
                    "Post-exercise AAR incorporated",
                    "Cross-references verified against DEPENDENCY_MAP",
                ]

                review = ReviewCycle(
                    doc_id=doc.doc_id,
                    review_type=random.choice(REVIEW_TYPES),
                    reviewer_name=random.choice(REVIEWERS),
                    review_date=review_date,
                    status=status,
                    notes=random.choice(notes_options),
                    next_review_date=next_review,
                )
                db.add(review)
                review_count += 1

        # --- Generate changelog entries ---
        # Each doc gets an initial entry + 0-3 change entries over 6 months
        changelog_count = 0

        change_summaries = [
            "Initial scan -- document discovered",
            "Content updated: section headers restructured",
            "Added cross-references to DEPENDENCY_MAP",
            "Fixed broken internal links",
            "Updated terminology per GLOSSARY_data_foundry",
            "Incorporated instructor feedback from AAR",
            "Version bump: aligned with TM restructure",
            "Minor editorial corrections",
            "Added learning objectives per POI requirements",
            "Updated diagrams and figures",
        ]

        for doc in docs:
            # Initial entry
            initial_date = datetime.combine(
                _random_date(timeline_start, timeline_start + timedelta(days=30)),
                datetime.min.time(),
            ).replace(tzinfo=UTC)

            db.add(ChangeLog(
                doc_id=doc.doc_id,
                change_date=initial_date,
                previous_hash=None,
                new_hash=doc.file_hash,
                change_summary="Initial scan -- document discovered",
                changed_by=None,
            ))
            changelog_count += 1

            # Additional changes for ~40% of documents
            if random.random() < 0.40:
                num_changes = random.randint(1, 3)
                for _ in range(num_changes):
                    change_date = datetime.combine(
                        _random_date(
                            timeline_start + timedelta(days=30),
                            timeline_end,
                        ),
                        datetime.min.time(),
                    ).replace(tzinfo=UTC)

                    prev_hash = _fake_hash()
                    new_hash = _fake_hash()

                    db.add(ChangeLog(
                        doc_id=doc.doc_id,
                        change_date=change_date,
                        previous_hash=prev_hash,
                        new_hash=new_hash,
                        change_summary=random.choice(change_summaries[1:]),
                        changed_by=random.choice(REVIEWERS),
                    ))
                    changelog_count += 1

        db.commit()
        print(f"Seeded {len(docs)} documents, {review_count} reviews, "
              f"{changelog_count} changelog entries.")

    finally:
        db.close()


if __name__ == "__main__":
    seed()
