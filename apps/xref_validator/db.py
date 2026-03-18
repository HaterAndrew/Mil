"""Cross-Reference Validator — database models, scan logic, and validators.

Scans the maven_training documentation corpus for broken links, stale TM
references, chapter-reference errors, and prereq-chain inconsistencies.
Results are persisted in a local SQLite database for trend analysis.
"""

from __future__ import annotations

import glob
import os
import re
import urllib.parse
from collections import Counter
from datetime import UTC, datetime
from pathlib import Path

from sqlalchemy import (
    Column,
    DateTime,
    ForeignKey,
    Integer,
    String,
    Text,
    create_engine,
    event,
)
from sqlalchemy.orm import (
    DeclarativeBase,
    Session,
    relationship,
    sessionmaker,
)

from .models import (
    IssueType,
    ScanHistoryItem,
    ScanResult,
    Severity,
    ValidationIssue,
)

# ---------------------------------------------------------------------------
# Database path — sits next to this file; *.db is gitignored
# ---------------------------------------------------------------------------
DB_PATH = Path(__file__).parent / "xref_validator.db"
DATABASE_URL = f"sqlite:///{DB_PATH}"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})


@event.listens_for(engine, "connect")
def _set_sqlite_pragmas(dbapi_conn, _connection_record):
    cursor = dbapi_conn.cursor()
    cursor.execute("PRAGMA journal_mode=WAL")
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()


SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)


class Base(DeclarativeBase):
    pass


# ---------------------------------------------------------------------------
# ORM models
# ---------------------------------------------------------------------------
class ScanRecord(Base):
    __tablename__ = "scans"

    id = Column(Integer, primary_key=True, autoincrement=True)
    timestamp = Column(DateTime, nullable=False, default=lambda: datetime.now(UTC))
    root_path = Column(String(500), nullable=False)
    total_files = Column(Integer, nullable=False, default=0)
    issues_found = Column(Integer, nullable=False, default=0)

    issues = relationship(
        "IssueRecord", back_populates="scan", cascade="all, delete-orphan"
    )


class IssueRecord(Base):
    __tablename__ = "issues"

    id = Column(Integer, primary_key=True, autoincrement=True)
    scan_id = Column(Integer, ForeignKey("scans.id", ondelete="CASCADE"), nullable=False)
    file_path = Column(String(500), nullable=False)
    line_number = Column(Integer, nullable=False, default=0)
    issue_type = Column(String(30), nullable=False)
    severity = Column(String(10), nullable=False)
    description = Column(Text, nullable=False)
    suggested_fix = Column(Text, nullable=False, default="")

    scan = relationship("ScanRecord", back_populates="issues")


def init_db():
    """Create tables if they don't exist."""
    Base.metadata.create_all(bind=engine)


def get_db():
    """FastAPI dependency — yields a SQLAlchemy session."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ---------------------------------------------------------------------------
# Authoritative prereq chain
# ---------------------------------------------------------------------------
PREREQ_CHAIN: dict[str, list[str]] = {
    "TM-10": [],
    "TM-20": ["TM-10"],
    "TM-30": ["TM-20"],
    "BSP": ["TM-20"],
    "TM-40A": ["TM-30"],
    "TM-40B": ["TM-30"],
    "TM-40C": ["TM-30"],
    "TM-40D": ["TM-30"],
    "TM-40E": ["TM-30"],
    "TM-40F": ["TM-30"],
    "TM-40G": ["TM-30"],
    "TM-40H": ["TM-30"],
    "TM-40M": ["TM-30"],
    "TM-40J": ["TM-30"],
    "TM-40K": ["TM-30"],
    "TM-40L": ["TM-30"],
    "TM-50G": ["TM-40G"],
    "TM-50H": ["TM-40H"],
    "TM-50M": ["TM-40M"],
    "TM-50J": ["TM-40J"],
    "TM-50K": ["TM-40K"],
    "TM-50L": ["TM-40L"],
}

# Valid TM identifiers
VALID_TM_IDS = set(PREREQ_CHAIN.keys())

# Stale TM-50 IDs (A-F never existed)
STALE_TM50_PATTERN = re.compile(r"\bTM[-\s]?50\s*[A-F]\b", re.IGNORECASE)

# Old scheme: TM-40A = ORSA (now TM-40A = Intelligence WFF, ORSA = TM-40G)
# Only flag when TM-40A is directly equated to ORSA (e.g., "TM-40A (ORSA)",
# "TM-40A=ORSA", "TM-40A ORSA"), NOT when both appear on the same line
# in separate contexts (e.g., "TM-40A (Intelligence) supports ORSA products")
OLD_40A_ORSA_PATTERN = re.compile(
    r"\bTM[-\s]?40\s*A\s*[\(=]\s*(?:ORSA|Operations Research)", re.IGNORECASE
)

# Generic TM reference pattern (e.g., TM-10, TM-40G, TM-50L)
TM_REF_PATTERN = re.compile(r"\bTM[-\s]?(\d{2})([A-M])?\b", re.IGNORECASE)

# Markdown link pattern: [text](target)
MD_LINK_PATTERN = re.compile(r"\[([^\]]*)\]\(([^)]+)\)")

# Chapter reference patterns: "Chapter 3", "Ch 5", "Ch. 7"
CHAPTER_REF_PATTERN = re.compile(
    r"\b(?:Chapter|Ch\.?)\s+(\d+)\b", re.IGNORECASE
)

# Heading pattern to count chapters in a doc (# Chapter N or ## Chapter N)
CHAPTER_HEADING_PATTERN = re.compile(
    r"^#{1,3}\s+(?:Chapter|Ch\.?)\s+(\d+)\b", re.MULTILINE | re.IGNORECASE
)

# Prereq statement patterns — formal declarations only
# Matches: "Prerequisite: TM-30", "Prerequisites: TM-10, TM-20",
#           "Prereq TM-30 (Required)", table cells like "| TM-30 (Required) |"
# Does NOT match body text like "builds on concepts from TM-10"
PREREQ_STATEMENT_PATTERN = re.compile(
    r"(?:"
    r"(?:prerequisites?|prereqs?)\s*[:;]\s*"  # "Prerequisite: TM-XX"
    r"|(?:prerequisites?|prereqs?)\s+(?:is|are)\s+"  # "Prerequisite is TM-XX"
    r"|(?:requires?|required)\s*[:;]\s*"  # "Required: TM-XX"
    r"|\|\s*(?:TM[-\s]?\d{2}[A-M]?)\s*\((?:Required|Req)\)"  # "| TM-30 (Required)"
    r")"
    r"[^.\n]*?(TM[-\s]?\d{2}[A-M]?)",
    re.IGNORECASE,
)


# ---------------------------------------------------------------------------
# Utility: collect files matching glob patterns
# ---------------------------------------------------------------------------
# Directories to skip during scanning (third-party code, build artifacts)
SKIP_DIRS = {"node_modules", ".git", "__pycache__", ".venv", "venv"}


def _collect_files(root_path: str, patterns: list[str]) -> list[Path]:
    """Return sorted list of files matching any of the glob patterns."""
    root = Path(root_path)
    if not root.is_dir():
        return []
    files: set[Path] = set()
    for pattern in patterns:
        for match in root.glob(pattern):
            # Skip files inside excluded directories
            if any(part in SKIP_DIRS for part in match.parts):
                continue
            if match.is_file():
                files.add(match)
    return sorted(files)


def _read_lines(file_path: Path) -> list[str]:
    """Read a file and return lines. Handles encoding errors gracefully."""
    try:
        return file_path.read_text(encoding="utf-8", errors="replace").splitlines()
    except OSError:
        return []


# ---------------------------------------------------------------------------
# Validator: Markdown links
# ---------------------------------------------------------------------------
def scan_markdown_links(file_path: Path, root_path: Path) -> list[ValidationIssue]:
    """Find all markdown links [text](target) and verify targets exist.

    Only checks relative file links — skips http/https, mailto, anchors (#).
    """
    issues: list[ValidationIssue] = []
    lines = _read_lines(file_path)
    rel_path = str(file_path.relative_to(root_path))

    for line_num, line in enumerate(lines, start=1):
        for match in MD_LINK_PATTERN.finditer(line):
            link_text = match.group(1)
            target = match.group(2).strip()

            # Skip external URLs, anchors, mailto, data URIs
            if any(target.startswith(prefix) for prefix in (
                "http://", "https://", "mailto:", "#", "data:", "javascript:",
            )):
                continue

            # Strip any anchor fragment from the target
            target_no_anchor = target.split("#")[0]
            if not target_no_anchor:
                # Pure anchor link (#something) — skip
                continue

            # URL-decode the target path
            target_decoded = urllib.parse.unquote(target_no_anchor)

            # Resolve relative to the file's parent directory
            resolved = (file_path.parent / target_decoded).resolve()

            if not resolved.exists():
                issues.append(ValidationIssue(
                    file_path=rel_path,
                    line_number=line_num,
                    issue_type=IssueType.BROKEN_LINK,
                    severity=Severity.ERROR,
                    description=(
                        f"Broken link: [{link_text}]({target}) — "
                        f"target does not exist: {target_decoded}"
                    ),
                    suggested_fix=f"Verify path or remove dead link to '{target_decoded}'",
                ))

    return issues


# ---------------------------------------------------------------------------
# Validator: Chapter references
# ---------------------------------------------------------------------------
def scan_chapter_refs(file_path: Path, root_path: Path) -> list[ValidationIssue]:
    """Find 'Chapter N' or 'Ch N' references in a markdown file.

    Checks that the referenced chapter number exists as a heading in the
    same document. Only applies to .md files.
    """
    issues: list[ValidationIssue] = []
    if file_path.suffix.lower() != ".md":
        return issues

    content = file_path.read_text(encoding="utf-8", errors="replace")
    lines = content.splitlines()
    rel_path = str(file_path.relative_to(root_path))

    # Find all chapter headings in this document
    chapter_headings: set[int] = set()
    for m in CHAPTER_HEADING_PATTERN.finditer(content):
        chapter_headings.add(int(m.group(1)))

    # If no chapter headings exist, skip — not a chapter-structured doc
    if not chapter_headings:
        return issues

    max_chapter = max(chapter_headings) if chapter_headings else 0

    # Pattern to detect cross-document chapter refs like "TM-20, Chapter 8"
    # or "TM-10 Ch 6" — these reference another document, not this one
    cross_doc_ref = re.compile(
        r"TM-\d+\w*[,\s]+(?:Chapter|Ch\.?)\s+\d+", re.IGNORECASE
    )

    for line_num, line in enumerate(lines, start=1):
        # Skip lines that are headings themselves (those define chapters)
        stripped = line.strip()
        if stripped.startswith("#"):
            continue

        for m in CHAPTER_REF_PATTERN.finditer(line):
            ref_num = int(m.group(1))

            # Check if this is a cross-document reference (e.g., "TM-20 Ch 8")
            # by looking at surrounding context — skip if another TM is named
            match_start = m.start()
            context_before = line[max(0, match_start - 30):match_start + len(m.group(0))]
            if cross_doc_ref.search(context_before):
                continue

            if ref_num not in chapter_headings:
                sev = Severity.ERROR if ref_num > max_chapter else Severity.WARNING
                issues.append(ValidationIssue(
                    file_path=rel_path,
                    line_number=line_num,
                    issue_type=IssueType.CHAPTER_REF_ERROR,
                    severity=sev,
                    description=(
                        f"Chapter reference 'Ch {ref_num}' not found in document headings. "
                        f"Available chapters: {sorted(chapter_headings)}"
                    ),
                    suggested_fix=(
                        f"Update to a valid chapter number or add Chapter {ref_num} heading"
                    ),
                ))

    return issues


# ---------------------------------------------------------------------------
# Validator: TM references
# ---------------------------------------------------------------------------
def scan_tm_refs(file_path: Path, root_path: Path) -> list[ValidationIssue]:
    """Find TM-XX references and validate against the known course catalog.

    Flags:
    - TM-50A through TM-50F (these never existed)
    - Old TM-40A=ORSA association (TM-40A is now Intelligence WFF)
    - Any TM reference not in the PREREQ_CHAIN
    """
    issues: list[ValidationIssue] = []
    lines = _read_lines(file_path)
    rel_path = str(file_path.relative_to(root_path))

    for line_num, line in enumerate(lines, start=1):
        # Check for stale TM-50A through TM-50F
        for m in STALE_TM50_PATTERN.finditer(line):
            issues.append(ValidationIssue(
                file_path=rel_path,
                line_number=line_num,
                issue_type=IssueType.STALE_REF,
                severity=Severity.ERROR,
                description=(
                    f"Stale reference: '{m.group()}' — TM-50A through TM-50F do not exist. "
                    f"TM-50 is only G through M."
                ),
                suggested_fix="Remove or replace with valid TM-50G through TM-50M",
            ))

        # Check for old TM-40A=ORSA association
        for m in OLD_40A_ORSA_PATTERN.finditer(line):
            issues.append(ValidationIssue(
                file_path=rel_path,
                line_number=line_num,
                issue_type=IssueType.STALE_REF,
                severity=Severity.ERROR,
                description=(
                    f"Stale reference: '{m.group()}' — TM-40A is now Intelligence WFF, "
                    f"not ORSA. ORSA is TM-40G."
                ),
                suggested_fix="Replace TM-40A (ORSA context) with TM-40G",
            ))

        # Check all TM-XX references against catalog
        for m in TM_REF_PATTERN.finditer(line):
            number = m.group(1)
            suffix = (m.group(2) or "").upper()
            tm_id = f"TM-{number}{suffix}"

            # Normalize: only check TM-10, TM-20, TM-30, TM-40X, TM-50X
            if number in ("10", "20", "30") and not suffix:
                continue  # These are always valid without suffix
            if number in ("40", "50") and not suffix:
                # Bare TM-40 or TM-50 — acceptable as a series reference
                continue
            if tm_id in VALID_TM_IDS:
                continue

            # Unknown TM reference
            issues.append(ValidationIssue(
                file_path=rel_path,
                line_number=line_num,
                issue_type=IssueType.STALE_REF,
                severity=Severity.WARNING,
                description=(
                    f"Unrecognized TM reference: '{tm_id}' — "
                    f"not in the known course catalog"
                ),
                suggested_fix=(
                    f"Verify '{tm_id}' is correct or update to a valid TM identifier"
                ),
            ))

    return issues


# ---------------------------------------------------------------------------
# Validator: Prereq consistency
# ---------------------------------------------------------------------------
def _get_transitive_prereqs(tm_id: str) -> set[str]:
    """Walk the PREREQ_CHAIN backwards to get all transitive prereqs."""
    result: set[str] = set()
    queue = list(PREREQ_CHAIN.get(tm_id, []))
    while queue:
        prereq = queue.pop(0)
        if prereq not in result:
            result.add(prereq)
            queue.extend(PREREQ_CHAIN.get(prereq, []))
    return result


def scan_prereq_consistency(root_path: Path) -> list[ValidationIssue]:
    """Check that prereq statements in docs match the authoritative chain.

    Looks for formal prereq declarations (e.g., "Prerequisites: TM-30") and
    validates they align with PREREQ_CHAIN. Accepts both direct and transitive
    prereqs (e.g., TM-40G listing TM-10 is valid because TM-10→TM-20→TM-30→TM-40G).
    Self-references (doc references its own TM) are also ignored.
    """
    issues: list[ValidationIssue] = []
    root = Path(root_path)

    # Scan all markdown files (skip excluded dirs)
    for file_path in root.rglob("*.md"):
        if not file_path.is_file():
            continue
        if any(part in SKIP_DIRS for part in file_path.parts):
            continue
        lines = _read_lines(file_path)
        rel_path = str(file_path.relative_to(root))

        # Determine which TM this file is about (from filename or path)
        file_tm = _identify_file_tm(file_path)

        # Pattern for exam answer choices (e.g., "A. TM-40G ...", "C. ...")
        exam_answer_pattern = re.compile(r"^\s*[A-F][.)]\s+")

        for line_num, line in enumerate(lines, start=1):
            # Skip exam answer choice lines — prereq mentions describe
            # other courses, not this document's own prereqs
            if exam_answer_pattern.match(line):
                continue

            for m in PREREQ_STATEMENT_PATTERN.finditer(line):
                stated_prereq_raw = m.group(1).strip()
                # Normalize TM reference
                stated_prereq = _normalize_tm_ref(stated_prereq_raw)

                if not file_tm or file_tm not in PREREQ_CHAIN:
                    continue

                # Skip self-references (doc mentioning its own course)
                if stated_prereq == file_tm:
                    continue

                expected_prereqs = PREREQ_CHAIN[file_tm]
                # Also accept transitive prereqs (full chain)
                all_valid_prereqs = _get_transitive_prereqs(file_tm)

                # If the stated prereq is not in the expected chain
                if stated_prereq and stated_prereq not in all_valid_prereqs:
                    # Only flag if the stated prereq is a valid TM
                    if stated_prereq in VALID_TM_IDS or stated_prereq in ("TM-10", "TM-20", "TM-30"):
                        issues.append(ValidationIssue(
                            file_path=rel_path,
                            line_number=line_num,
                            issue_type=IssueType.PREREQ_MISMATCH,
                            severity=Severity.WARNING,
                            description=(
                                f"Prereq mismatch in {file_tm} doc: states '{stated_prereq}' "
                                f"as prereq, but authoritative chain says "
                                f"{expected_prereqs or 'none'}"
                            ),
                            suggested_fix=(
                                f"Update prereq statement to match authoritative chain: "
                                f"{file_tm} requires {expected_prereqs or 'none'}"
                            ),
                        ))

    return issues


def _identify_file_tm(file_path: Path) -> str | None:
    """Try to determine which TM course a file belongs to based on path/name."""
    path_str = str(file_path).upper()

    # Check directory names and filenames for TM identifiers
    # Look for patterns like TM_40G, TM-40G, TM40G in the path
    tm_dir_pattern = re.compile(r"TM[-_\s]?(\d{2})[-_\s]?([A-M])?", re.IGNORECASE)
    matches = list(tm_dir_pattern.finditer(path_str))

    if matches:
        # Use the most specific (last) match
        last = matches[-1]
        number = last.group(1)
        suffix = (last.group(2) or "").upper()
        return f"TM-{number}{suffix}" if suffix else f"TM-{number}"

    return None


def _normalize_tm_ref(raw: str) -> str:
    """Normalize a TM reference string like 'TM 20' or 'TM-40G' to 'TM-20'."""
    m = re.match(r"TM[-\s]?(\d{2})([A-L])?", raw, re.IGNORECASE)
    if not m:
        return raw
    number = m.group(1)
    suffix = (m.group(2) or "").upper()
    return f"TM-{number}{suffix}" if suffix else f"TM-{number}"


# ---------------------------------------------------------------------------
# Orchestrator: full scan
# ---------------------------------------------------------------------------
def run_full_scan(
    root_path: str,
    patterns: list[str] | None = None,
) -> ScanResult:
    """Run all validators against the corpus and store results in the DB.

    Returns a ScanResult with all issues found.
    """
    if patterns is None:
        patterns = ["**/*.md", "**/*.html"]

    init_db()
    root = Path(root_path)
    files = _collect_files(root_path, patterns)

    all_issues: list[ValidationIssue] = []

    for file_path in files:
        # Markdown link validation
        all_issues.extend(scan_markdown_links(file_path, root))

        # Chapter reference validation (markdown only)
        if file_path.suffix.lower() == ".md":
            all_issues.extend(scan_chapter_refs(file_path, root))

        # TM reference validation
        all_issues.extend(scan_tm_refs(file_path, root))

    # Prereq consistency (corpus-wide)
    all_issues.extend(scan_prereq_consistency(root))

    # Summarize
    type_counts: dict[str, int] = Counter()
    severity_counts: dict[str, int] = Counter()
    for issue in all_issues:
        type_counts[issue.issue_type.value] += 1
        severity_counts[issue.severity.value] += 1

    # Persist to DB
    db = SessionLocal()
    try:
        scan_rec = ScanRecord(
            timestamp=datetime.now(UTC),
            root_path=root_path,
            total_files=len(files),
            issues_found=len(all_issues),
        )
        db.add(scan_rec)
        db.flush()  # get the scan ID

        for issue in all_issues:
            db.add(IssueRecord(
                scan_id=scan_rec.id,
                file_path=issue.file_path,
                line_number=issue.line_number,
                issue_type=issue.issue_type.value,
                severity=issue.severity.value,
                description=issue.description,
                suggested_fix=issue.suggested_fix,
            ))

        db.commit()
        scan_id = scan_rec.id
    finally:
        db.close()

    return ScanResult(
        scan_id=scan_id,
        timestamp=datetime.now(UTC),
        total_files=len(files),
        issues_found=len(all_issues),
        issues=all_issues,
        summary_by_type=dict(type_counts),
        summary_by_severity=dict(severity_counts),
    )


# ---------------------------------------------------------------------------
# Query helpers
# ---------------------------------------------------------------------------
def get_scan_history() -> list[ScanHistoryItem]:
    """Return all past scans, most recent first."""
    init_db()
    db = SessionLocal()
    try:
        records = (
            db.query(ScanRecord)
            .order_by(ScanRecord.timestamp.desc())
            .all()
        )
        return [
            ScanHistoryItem(
                scan_id=r.id,
                timestamp=r.timestamp,
                total_files=r.total_files,
                issues_found=r.issues_found,
            )
            for r in records
        ]
    finally:
        db.close()


def get_scan_result(scan_id: int) -> ScanResult | None:
    """Load a full scan result by ID."""
    init_db()
    db = SessionLocal()
    try:
        rec = db.query(ScanRecord).filter(ScanRecord.id == scan_id).first()
        if not rec:
            return None

        issue_records = (
            db.query(IssueRecord)
            .filter(IssueRecord.scan_id == scan_id)
            .all()
        )

        issues = [
            ValidationIssue(
                file_path=ir.file_path,
                line_number=ir.line_number,
                issue_type=IssueType(ir.issue_type),
                severity=Severity(ir.severity),
                description=ir.description,
                suggested_fix=ir.suggested_fix,
            )
            for ir in issue_records
        ]

        type_counts: dict[str, int] = Counter()
        severity_counts: dict[str, int] = Counter()
        for issue in issues:
            type_counts[issue.issue_type.value] += 1
            severity_counts[issue.severity.value] += 1

        return ScanResult(
            scan_id=rec.id,
            timestamp=rec.timestamp,
            total_files=rec.total_files,
            issues_found=rec.issues_found,
            issues=issues,
            summary_by_type=dict(type_counts),
            summary_by_severity=dict(severity_counts),
        )
    finally:
        db.close()


def get_filtered_issues(
    scan_id: int | None = None,
    issue_type: str | None = None,
    severity: str | None = None,
) -> list[ValidationIssue]:
    """Return issues with optional type/severity filters.

    If scan_id is None, uses the latest scan.
    """
    init_db()
    db = SessionLocal()
    try:
        # Determine scan_id
        if scan_id is None:
            latest = (
                db.query(ScanRecord)
                .order_by(ScanRecord.timestamp.desc())
                .first()
            )
            if not latest:
                return []
            scan_id = latest.id

        query = db.query(IssueRecord).filter(IssueRecord.scan_id == scan_id)

        if issue_type:
            query = query.filter(IssueRecord.issue_type == issue_type)
        if severity:
            query = query.filter(IssueRecord.severity == severity)

        records = query.all()
        return [
            ValidationIssue(
                file_path=r.file_path,
                line_number=r.line_number,
                issue_type=IssueType(r.issue_type),
                severity=Severity(r.severity),
                description=r.description,
                suggested_fix=r.suggested_fix,
            )
            for r in records
        ]
    finally:
        db.close()
