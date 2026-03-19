"""SQLAlchemy database layer and markdown indexing logic for Glossary Search.

Parses markdown files from the maven_training corpus and extracts
term-definition pairs into a local SQLite database for full-text search.
"""

from __future__ import annotations

import re
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

from sqlalchemy import (
    Column,
    DateTime,
    Integer,
    String,
    Text,
    create_engine,
    func,
    or_,
)
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker

DB_PATH = Path(__file__).parent / "glossary_search.db"

# ---------------------------------------------------------------------------
# ORM Model
# ---------------------------------------------------------------------------


class Base(DeclarativeBase):
    pass


class Term(Base):
    """Indexed glossary/doctrine term."""

    __tablename__ = "terms"

    id = Column(Integer, primary_key=True, autoincrement=True)
    term = Column(String(200), nullable=False, index=True)
    definition = Column(Text, nullable=False)
    source_file = Column(String(200), nullable=False)
    source_line = Column(Integer, nullable=False)
    category = Column(String(20), nullable=False, index=True)
    indexed_at = Column(DateTime, default=lambda: datetime.now(timezone.utc))


# ---------------------------------------------------------------------------
# Engine / Session factory
# ---------------------------------------------------------------------------

_engine = None
_SessionLocal = None


def _get_engine():
    global _engine
    if _engine is None:
        _engine = create_engine(
            f"sqlite:///{DB_PATH}",
            connect_args={"check_same_thread": False},
            echo=False,
        )
    return _engine


def get_session() -> Session:
    global _SessionLocal
    if _SessionLocal is None:
        _SessionLocal = sessionmaker(bind=_get_engine())
    return _SessionLocal()


def init_db() -> None:
    """Create tables if they do not exist."""
    Base.metadata.create_all(_get_engine())


# ---------------------------------------------------------------------------
# Markdown Parsing — extracts term→definition pairs
# ---------------------------------------------------------------------------

# Patterns matched (in priority order):
#   1. **Term**: Definition  /  **Term** — Definition  (bold-lead lines)
#   2. - **ACRONYM** — Definition  /  - **ACRONYM**: Definition  (list items)
#   3. | Term | Definition |  (markdown table rows, skip header/separator)
#   4. ### Term\n<paragraph>  (heading followed by definition paragraph)

_RE_BOLD_COLON = re.compile(
    r"^\*\*(.+?)\*\*\s*[:—–-]\s*(.+)", re.MULTILINE
)
_RE_LIST_BOLD = re.compile(
    r"^[-*]\s+\*\*(.+?)\*\*\s*[:—–-]\s*(.+)", re.MULTILINE
)
_RE_TABLE_ROW = re.compile(
    r"^\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|", re.MULTILINE
)
_RE_TABLE_SEP = re.compile(r"^\|[\s:_-]+\|")
_RE_HEADING3 = re.compile(r"^###\s+(.+)", re.MULTILINE)

# Source files to scan (relative to maven_training root)
_TARGET_PATHS = [
    "doctrine/GLOSSARY_data_foundry.md",
    "doctrine/DATA_LITERACY_technical_reference.md",
    "doctrine/DATA_LITERACY_senior_leaders.md",
    "doctrine/CDA_CONSTRAINTS_AND_DIRECTIVES.md",
    "doctrine/CG_GUIDANCE.md",
    "doctrine/ONTOLOGY_DESIGN_PRINCIPLES.md",
    "quick_reference/cheatsheet.md",
]


def _classify_term(term: str, source_file: str) -> str:
    """Heuristic to assign a category based on term form and source file."""
    # All-caps or well-known acronym pattern (2-8 uppercase letters, optional parens)
    if re.fullmatch(r"[A-Z][A-Z0-9/]{1,9}(\s*\(.*?\))?", term.strip()):
        return "ACRONYM"
    if "GLOSSARY" in source_file.upper():
        return "GLOSSARY"
    if "CONSTRAINT" in source_file.upper() or "CG_GUIDANCE" in source_file.upper():
        return "DOCTRINE"
    return "CONCEPT"


def _parse_glossary_style(text: str, filename: str) -> list[dict]:
    """Parse the primary glossary format: bold term, then multi-line definition.

    The glossary uses a pattern of:
        **Term**
        *Foundry Equivalent: ...*
        Definition: paragraph...
        Example: paragraph...

    Separated by --- lines.
    """
    entries: list[dict] = []
    # Split on horizontal-rule separators
    blocks = re.split(r"\n---+\n", text)
    for block in blocks:
        block = block.strip()
        if not block:
            continue
        # Look for a leading bold term (standalone on a line)
        m = re.match(r"^\*\*(.+?)\*\*\s*$", block, re.MULTILINE)
        if not m:
            continue
        term = m.group(1).strip()
        # Everything after the term line is the definition body
        body = block[m.end():].strip()
        if not body or len(body) < 10:
            continue
        # Find line number in original text
        term_pos = text.find(f"**{term}**")
        line_no = text[:term_pos].count("\n") + 1 if term_pos >= 0 else 1
        entries.append({
            "term": term,
            "definition": body,
            "source_line": line_no,
            "category": _classify_term(term, filename),
        })
    return entries


def _parse_bold_lead(text: str, filename: str) -> list[dict]:
    """Extract terms from **Term**: Definition or **Term** — Definition lines."""
    entries: list[dict] = []
    for m in _RE_BOLD_COLON.finditer(text):
        term = m.group(1).strip()
        defn = m.group(2).strip()
        if len(defn) < 5:
            continue
        line_no = text[: m.start()].count("\n") + 1
        entries.append({
            "term": term,
            "definition": defn,
            "source_line": line_no,
            "category": _classify_term(term, filename),
        })
    return entries


def _parse_list_bold(text: str, filename: str) -> list[dict]:
    """Extract terms from list items: - **TERM** — definition."""
    entries: list[dict] = []
    for m in _RE_LIST_BOLD.finditer(text):
        term = m.group(1).strip()
        defn = m.group(2).strip()
        if len(defn) < 5:
            continue
        line_no = text[: m.start()].count("\n") + 1
        entries.append({
            "term": term,
            "definition": defn,
            "source_line": line_no,
            "category": _classify_term(term, filename),
        })
    return entries


def _parse_table_rows(text: str, filename: str) -> list[dict]:
    """Extract terms from markdown table rows (skip header separators)."""
    entries: list[dict] = []
    for m in _RE_TABLE_ROW.finditer(text):
        line = text[: m.start()].count("\n") + 1
        # Skip separator rows (---) and header rows
        full_line = m.group(0).strip()
        if _RE_TABLE_SEP.match(full_line):
            continue
        term = m.group(1).strip()
        defn = m.group(2).strip()
        # Skip if term looks like a header label or is very short
        if term.lower() in ("term", "name", "field", "need", "publication",
                            "step", "id", "speaker", "source", "document",
                            "date", "format", "authority", "initiative"):
            continue
        if len(defn) < 5 or len(term) < 2:
            continue
        entries.append({
            "term": term,
            "definition": defn,
            "source_line": line,
            "category": _classify_term(term, filename),
        })
    return entries


def _parse_heading3(text: str, filename: str) -> list[dict]:
    """Extract terms from ### Heading followed by paragraph text."""
    entries: list[dict] = []
    matches = list(_RE_HEADING3.finditer(text))
    for i, m in enumerate(matches):
        term = m.group(1).strip()
        # Grab text between this heading and the next heading or end
        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(text)
        body = text[start:end].strip()
        # Strip sub-headings and stop at next ---
        body = body.split("---")[0].strip()
        if len(body) < 15:
            continue
        line_no = text[: m.start()].count("\n") + 1
        entries.append({
            "term": term,
            "definition": body[:2000],
            "source_line": line_no,
            "category": _classify_term(term, filename),
        })
    return entries


def _parse_file(filepath: Path) -> list[dict]:
    """Parse a single markdown file and return term entries."""
    text = filepath.read_text(encoding="utf-8", errors="replace")
    filename = filepath.name
    seen_terms: set[str] = set()
    all_entries: list[dict] = []

    # Try glossary-style first (block-separated bold terms) for GLOSSARY files
    if "GLOSSARY" in filename.upper():
        glossary_entries = _parse_glossary_style(text, filename)
        for e in glossary_entries:
            key = e["term"].lower()
            if key not in seen_terms:
                seen_terms.add(key)
                all_entries.append(e)

    # Then try the other patterns for remaining terms
    for parser in (_parse_list_bold, _parse_bold_lead, _parse_table_rows, _parse_heading3):
        for e in parser(text, filename):
            key = e["term"].lower()
            if key not in seen_terms:
                seen_terms.add(key)
                all_entries.append(e)

    return all_entries


# ---------------------------------------------------------------------------
# Public Indexing API
# ---------------------------------------------------------------------------


def index_glossary(root_path: str | Path) -> int:
    """Parse target markdown files and insert term entries into the DB.

    Returns the number of terms indexed.
    """
    root = Path(root_path)
    init_db()
    session = get_session()
    count = 0

    for rel_path in _TARGET_PATHS:
        fpath = root / rel_path
        if not fpath.exists():
            continue
        entries = _parse_file(fpath)
        for e in entries:
            term = Term(
                term=e["term"],
                definition=e["definition"],
                source_file=rel_path,
                source_line=e["source_line"],
                category=e["category"],
            )
            session.add(term)
            count += 1

    # Also scan for any additional .md files in doctrine/ and quick_reference/
    for subdir in ("doctrine", "quick_reference"):
        scan_dir = root / subdir
        if not scan_dir.is_dir():
            continue
        for md_file in scan_dir.rglob("*.md"):
            rel = str(md_file.relative_to(root))
            if rel in _TARGET_PATHS:
                continue  # already processed
            entries = _parse_file(md_file)
            for e in entries:
                term = Term(
                    term=e["term"],
                    definition=e["definition"],
                    source_file=rel,
                    source_line=e["source_line"],
                    category=e["category"],
                )
                session.add(term)
                count += 1

    session.commit()
    session.close()
    return count


def reindex(root_path: str | Path) -> int:
    """Drop all terms and rebuild the index from source files."""
    init_db()
    session = get_session()
    session.query(Term).delete()
    session.commit()
    session.close()
    return index_glossary(root_path)


# ---------------------------------------------------------------------------
# Search & Query API
# ---------------------------------------------------------------------------


def search_terms(
    query: str,
    category: Optional[str] = None,
    limit: int = 20,
) -> tuple[list[Term], float]:
    """Case-insensitive LIKE search on term and definition columns.

    Returns (results, elapsed_ms).
    """
    init_db()
    session = get_session()
    t0 = time.perf_counter()

    pattern = f"%{query}%"
    q = session.query(Term).filter(
        or_(
            Term.term.ilike(pattern),
            Term.definition.ilike(pattern),
        )
    )
    if category:
        q = q.filter(Term.category == category)

    # Rank: exact term match first, then term-contains, then definition-only
    results = q.order_by(
        # SQLite doesn't have native ranking; approximate via CASE ordering
        func.length(Term.term),  # shorter (more specific) terms first
    ).limit(limit).all()

    elapsed = (time.perf_counter() - t0) * 1000
    session.close()
    return results, elapsed


def get_categories() -> list[dict]:
    """Return distinct categories with term counts."""
    init_db()
    session = get_session()
    rows = (
        session.query(Term.category, func.count(Term.id))
        .group_by(Term.category)
        .order_by(func.count(Term.id).desc())
        .all()
    )
    session.close()
    return [{"category": cat, "count": cnt} for cat, cnt in rows]


def get_all_terms(category: Optional[str] = None) -> list[Term]:
    """Retrieve all terms, optionally filtered by category, sorted alphabetically."""
    init_db()
    session = get_session()
    q = session.query(Term)
    if category:
        q = q.filter(Term.category == category)
    results = q.order_by(Term.term).all()
    session.close()
    return results


def get_term_by_id(term_id: int) -> Optional[Term]:
    """Retrieve a single term by primary key."""
    init_db()
    session = get_session()
    result = session.query(Term).filter(Term.id == term_id).first()
    session.close()
    return result


def get_stats() -> dict:
    """Return aggregate index statistics."""
    init_db()
    session = get_session()
    total = session.query(func.count(Term.id)).scalar() or 0
    by_cat = (
        session.query(Term.category, func.count(Term.id))
        .group_by(Term.category)
        .order_by(func.count(Term.id).desc())
        .all()
    )
    source_files = (
        session.query(func.count(func.distinct(Term.source_file))).scalar() or 0
    )
    session.close()
    return {
        "total_terms": total,
        "by_category": [{"category": c, "count": n} for c, n in by_cat],
        "source_files": source_files,
    }
