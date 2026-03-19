#!/usr/bin/env python3
"""Check HTML ↔ React content sync.

Compares structural content between the HTML source of truth and React TSX
panels.  Focuses on high-signal content: course codes, section titles, and
prerequisite chains.  Ignores formatting differences (bullet styles, PDF
links, JSX expressions).

Dependencies: stdlib only (html.parser, re, pathlib).
"""

from __future__ import annotations

import re
import sys
from html.parser import HTMLParser
from pathlib import Path

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
REPO_ROOT = Path(__file__).resolve().parent.parent
HTML_FILE = REPO_ROOT / "maven_training" / "mss_info_app" / "index.html"
TSX_DIR = REPO_ROOT / "maven_training" / "mss_widget" / "src" / "panels"

# Course code pattern (TM-10, TM-40G, FBC, TM-SL, etc.)
_COURSE_RE = re.compile(r"\bTM[-\s]?\d{2}[A-O]?\b|\bFBC\b|\bTM[-\s]?SL\b")

# Classes that hold structural content (titles, badges — should match exactly)
TITLE_CLASSES = {"section-badge", "section-title"}

# Classes that hold body content (compared by course-code extraction only)
BODY_CLASSES = {
    "section-subtitle",
    "callout-body",
    "path-tm",
    "path-name",
    "track-tm",
    "track-name",
    "track-prereq",
    "track-audience",
    "task-header",
}

ALL_CLASSES = TITLE_CLASSES | BODY_CLASSES


# ---------------------------------------------------------------------------
# HTML extractor (stdlib html.parser)
# ---------------------------------------------------------------------------
class _ContentExtractor(HTMLParser):
    """Extract text from elements matching target CSS classes."""

    def __init__(self, target_classes: set[str]):
        super().__init__()
        self._targets = target_classes
        self._capture = False
        self._depth = 0
        self._current_class: str | None = None
        self._buf: list[str] = []
        self.atoms: dict[str, list[str]] = {c: [] for c in target_classes}

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]):
        if self._capture:
            self._depth += 1
            return
        cls_val = dict(attrs).get("class", "") or ""
        for target in self._targets:
            if target in cls_val.split():
                self._capture = True
                self._depth = 1
                self._current_class = target
                self._buf = []
                return

    def handle_endtag(self, tag: str):
        if self._capture:
            self._depth -= 1
            if self._depth <= 0:
                text = _norm(" ".join(self._buf))
                if text and self._current_class:
                    self.atoms[self._current_class].append(text)
                self._capture = False
                self._current_class = None
                self._buf = []

    def handle_data(self, data: str):
        if self._capture:
            self._buf.append(data)


def extract_html(path: Path) -> dict[str, list[str]]:
    """Return {class_name: [text, ...]} from the HTML file."""
    parser = _ContentExtractor(ALL_CLASSES)
    parser.feed(path.read_text(encoding="utf-8"))
    return parser.atoms


# ---------------------------------------------------------------------------
# TSX extractor (regex-based)
# ---------------------------------------------------------------------------
_TSX_PATTERN = re.compile(
    r'className="([^"]*)"[^>]*>'
    r'(.*?)'
    r'</',
    re.DOTALL,
)


def extract_tsx(directory: Path) -> dict[str, list[str]]:
    """Return {class_name: [text, ...]} from all .tsx files."""
    atoms: dict[str, list[str]] = {c: [] for c in ALL_CLASSES}
    for tsx_file in sorted(directory.glob("*.tsx")):
        content = tsx_file.read_text(encoding="utf-8")
        for match in _TSX_PATTERN.finditer(content):
            class_val = match.group(1)
            raw_text = match.group(2)
            for target in ALL_CLASSES:
                if target in class_val.split():
                    clean = re.sub(r"<[^>]+>", " ", raw_text)
                    clean = _norm(clean)
                    if clean:
                        atoms[target].append(clean)
                    break
    return atoms


# ---------------------------------------------------------------------------
# Normalisation
# ---------------------------------------------------------------------------
def _norm(s: str) -> str:
    """Aggressive normalisation to eliminate formatting noise."""
    s = re.sub(r"&[a-zA-Z]+;|&#\d+;", " ", s)        # HTML entities
    s = re.sub(r"\{[^}]*\}", "", s)                     # JSX expressions
    s = re.sub(r"Open PDF\s*→?", "", s)                 # PDF link text
    s = re.sub(r"View TM-\d+\s*Series", "", s)          # Nav link text
    s = re.sub(r"[•·|→←]", " ", s)                      # bullet/arrow chars
    s = re.sub(r"\s+", " ", s).strip()
    return s


def _extract_courses(texts: list[str]) -> set[str]:
    """Pull all TM-XX course codes from a list of text strings."""
    codes: set[str] = set()
    for t in texts:
        # Normalize TM 40G → TM-40G
        normalized = re.sub(r"TM\s+", "TM-", t)
        codes.update(m.replace(" ", "-") for m in _COURSE_RE.findall(normalized))
    return codes


def _norm_title(s: str) -> str:
    """Extra normalisation for title comparison (case-insensitive, strip noise)."""
    s = _norm(s)
    s = re.sub(r"\s*—\s*", " ", s)       # em-dash to space
    s = re.sub(r"[^\w\s]", "", s)         # strip punctuation
    return re.sub(r"\s+", " ", s).strip().upper()


# ---------------------------------------------------------------------------
# Comparison
# ---------------------------------------------------------------------------
def compare(
    html_atoms: dict[str, list[str]],
    tsx_atoms: dict[str, list[str]],
) -> tuple[list[str], list[str]]:
    """Return (errors, warnings) lists."""
    errors: list[str] = []
    warnings: list[str] = []

    # 1. Section badges (exact match after normalisation)
    html_badges = {_norm_title(b) for b in html_atoms.get("section-badge", [])}
    tsx_badges = {_norm_title(b) for b in tsx_atoms.get("section-badge", [])}
    for b in sorted(html_badges - tsx_badges):
        errors.append(f"[section-badge] HTML only: {b}")
    for b in sorted(tsx_badges - html_badges):
        errors.append(f"[section-badge] React only: {b}")

    # 2. Section titles (normalised comparison)
    html_titles = {_norm_title(t) for t in html_atoms.get("section-title", [])}
    tsx_titles = {_norm_title(t) for t in tsx_atoms.get("section-title", [])}
    for t in sorted(html_titles - tsx_titles):
        errors.append(f"[section-title] HTML only: {t}")
    for t in sorted(tsx_titles - html_titles):
        errors.append(f"[section-title] React only: {t}")

    # 3. Course codes across all body content
    html_body_text: list[str] = []
    tsx_body_text: list[str] = []
    for cls in BODY_CLASSES:
        html_body_text.extend(html_atoms.get(cls, []))
        tsx_body_text.extend(tsx_atoms.get(cls, []))

    html_courses = _extract_courses(html_body_text)
    tsx_courses = _extract_courses(tsx_body_text)

    for c in sorted(html_courses - tsx_courses):
        errors.append(f"[course-code] HTML only: {c}")
    for c in sorted(tsx_courses - html_courses):
        errors.append(f"[course-code] React only: {c}")

    # 4. Track names (normalised comparison)
    html_tracks = {_norm_title(t) for t in html_atoms.get("track-name", [])}
    tsx_tracks = {_norm_title(t) for t in tsx_atoms.get("track-name", [])}
    for t in sorted(html_tracks - tsx_tracks):
        warnings.append(f"[track-name] HTML only: {t}")
    for t in sorted(tsx_tracks - html_tracks):
        warnings.append(f"[track-name] React only: {t}")

    # 5. Prereq chains — extract prereq relationships
    html_prereqs = _extract_prereq_pairs(html_atoms.get("track-prereq", []))
    tsx_prereqs = _extract_prereq_pairs(tsx_atoms.get("track-prereq", []))
    for p in sorted(html_prereqs - tsx_prereqs):
        errors.append(f"[prereq-chain] HTML only: {p}")
    for p in sorted(tsx_prereqs - html_prereqs):
        errors.append(f"[prereq-chain] React only: {p}")

    return errors, warnings


def _extract_prereq_pairs(texts: list[str]) -> set[str]:
    """Extract 'Prereq: X → Advanced: Y' relationships from prereq text."""
    pairs: set[str] = set()
    for t in texts:
        normalized = re.sub(r"TM\s+", "TM-", t)
        codes = _COURSE_RE.findall(normalized)
        if len(codes) >= 2:
            pairs.add(f"{codes[0]} → {codes[1]}")
        elif codes:
            pairs.add(f"requires {codes[0]}")
    return pairs


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main() -> int:
    strict = "--strict" in sys.argv

    if not HTML_FILE.exists():
        print(f"ERROR: HTML file not found: {HTML_FILE}", file=sys.stderr)
        return 1
    if not TSX_DIR.is_dir():
        print(f"ERROR: TSX panels directory not found: {TSX_DIR}", file=sys.stderr)
        return 1

    html_atoms = extract_html(HTML_FILE)
    tsx_atoms = extract_tsx(TSX_DIR)

    html_total = sum(len(v) for v in html_atoms.values())
    tsx_total = sum(len(v) for v in tsx_atoms.values())
    print(f"Extracted {html_total} HTML atoms, {tsx_total} React atoms")

    errors, warnings = compare(html_atoms, tsx_atoms)

    if errors:
        print(f"\nERRORS — {len(errors)} structural mismatch(es):\n")
        for e in errors:
            print(f"  {e}")

    if warnings:
        print(f"\nWARNINGS — {len(warnings)} content difference(s):\n")
        for w in warnings:
            print(f"  {w}")

    if not errors and not warnings:
        print("OK — HTML and React content are in sync.")
        return 0

    print(f"\nTotal: {len(errors)} error(s), {len(warnings)} warning(s)")

    # --strict: fail on any errors.  Default: report only (exit 0).
    if strict and errors:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
