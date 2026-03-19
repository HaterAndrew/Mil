#!/usr/bin/env python3
"""
optimize_markdown.py — Token reduction and tiered-context optimization for maven_training/ corpus.

Operations applied per file type:
  TM files (TM_*.md):
    - Move BLUF from Chapter 1 body to compact header block (line 1-12)
    - Compress verbose publication header (HQ/date/version/distribution/authority) → 1 compact line
    - Remove Safety Summary prose, keep only WARNING/CAUTION/NOTE callouts
    - Remove TABLE OF CONTENTS section

  CONCEPTS_GUIDE files (CONCEPTS_GUIDE_*.md):
    - Move BLUF from Section 1 body to compact header block
    - Compress verbose publication header → 1 compact line
    - Remove TABLE OF CONTENTS section

  Doctrine / training_management / misc:
    - Remove TABLE OF CONTENTS sections only (prose is authoritative, not compressed)

Marker: Files already processed have '> *HQ USAREUR-AF' in first 20 lines — skipped on re-run.

Usage:
  python3 scripts/optimize_markdown.py              # all files, apply changes
  python3 scripts/optimize_markdown.py --dry-run    # report savings, no writes
  python3 scripts/optimize_markdown.py path/to/file # single file
"""

import re
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent / "maven_training"

# --- Patterns ---
RE_H1        = re.compile(r'^# (.+)')
RE_H2        = re.compile(r'^## (.+)')
RE_PREREQ    = re.compile(r'^\*\*PREREQUISITE(?:S| PUBLICATIONS)?:\*\*\s*(.*)', re.I)
RE_PURPOSE   = re.compile(r'^\*\*PURPOSE:\*\*\s*(.*)', re.I)
RE_HQ_NOISE  = re.compile(
    r'^\*\*HEADQUARTERS|^Wiesbaden,|^APO AE|^Unit 29351'
    r'|^HEADQUARTERS$|^UNITED STATES ARMY EUROPE'
    r'|^USAREUR-AF G6|^\d{4}$',
    re.I
)
RE_DISTRIB   = re.compile(r'^\*?\*?DISTRIBUTION RESTRICTION', re.I)
RE_AUTHORITY = re.compile(r'^\*\*AUTHORITY:', re.I)
RE_VERSION   = re.compile(r'^\*\*Version \d', re.I)
RE_TOC       = re.compile(r'^#{1,2}\s+TABLE OF CONTENTS\s*$', re.I)
RE_SAFETY    = re.compile(r'^## SAFETY SUMMARY\s*$', re.I)
RE_CALLOUT   = re.compile(r'^> \*\*(WARNING|CAUTION|NOTE):', re.I)
RE_CHAPTER   = re.compile(r'^#{1,3} (?:CHAPTER|SECTION|APPENDIX)', re.I)
RE_BLUF      = re.compile(r'^\*\*BLUF:\*\*\s*(.*)')
RE_SEP       = re.compile(r'^---+\s*$')
RE_PROCESSED = re.compile(r'^> \*HQ USAREUR-AF')  # idempotency marker


def first_sep(lines: list[str]) -> int:
    for i, l in enumerate(lines):
        if RE_SEP.match(l):
            return i
    return -1


def find_section_range(lines: list[str], header_re) -> tuple[int, int]:
    """Return [start, end) of a section starting with header_re. End = next ## or ---."""
    for i, l in enumerate(lines):
        if header_re.match(l):
            j = i + 1
            while j < len(lines):
                if RE_CHAPTER.match(lines[j]) or RE_TOC.match(lines[j]):
                    return i, j
                if RE_SEP.match(lines[j]):
                    return i, j + 1   # consume trailing ---
                j += 1
            return i, j
    return -1, -1


def extract_callouts(lines: list[str], start: int, end: int) -> list[str]:
    return [l for l in lines[start:end] if RE_CALLOUT.match(l)]


def find_bluf(lines: list[str], from_line: int = 0, search_limit: int = 150) -> tuple[int, str]:
    """Return (line_index, bluf_text) or (-1, '')."""
    for i in range(from_line, min(from_line + search_limit, len(lines))):
        m = RE_BLUF.match(lines[i])
        if m:
            bluf = m.group(1).strip()
            # Collect continuation lines (indented or plain prose, not a new block)
            j = i + 1
            while j < len(lines):
                nxt = lines[j].strip()
                if not nxt or nxt.startswith('#') or nxt.startswith('**') or nxt.startswith('>') or nxt.startswith('-'):
                    break
                bluf += ' ' + nxt
                j += 1
            return i, bluf
    return -1, ''


def remove_toc(lines: list[str]) -> tuple[list[str], int]:
    """Remove TABLE OF CONTENTS section. Returns (modified_lines, removed_count)."""
    out = []
    i = 0
    removed = 0
    while i < len(lines):
        if RE_TOC.match(lines[i]):
            # Also strip the preceding separator if present
            if out and RE_SEP.match(out[-1]):
                out.pop()
                removed += 1
            # Advance past ToC content until next chapter or trailing ---
            i += 1
            removed += 1  # count the ToC header itself
            while i < len(lines):
                if RE_CHAPTER.match(lines[i]):
                    break
                if RE_SEP.match(lines[i]):
                    i += 1   # consume trailing ---
                    removed += 1
                    break
                removed += 1
                i += 1
        else:
            out.append(lines[i])
            i += 1
    return out, removed


def transform_tm(lines: list[str]) -> tuple[list[str] | None, int]:
    """
    Full transformation for TM_*.md files.
    Returns (new_lines, lines_saved) or (None, 0) if skipped.
    """
    # Idempotency check
    if any(RE_PROCESSED.match(l) for l in lines[:20]):
        return None, 0

    header_end = first_sep(lines)
    if header_end < 0:
        return None, 0

    # -- Extract header metadata --
    h1 = next((RE_H1.match(l).group(1) for l in lines[:header_end] if RE_H1.match(l)), '')
    prereq_raw = next(
        (RE_PREREQ.match(l).group(1).strip() for l in lines[:header_end] if RE_PREREQ.match(l)), ''
    )

    # -- Safety Summary: extract callouts, determine range --
    safety_start, safety_end = find_section_range(lines, RE_SAFETY)
    callouts = []
    if safety_start >= 0:
        callouts = extract_callouts(lines, safety_start, safety_end)

    # -- ToC range --
    # We'll do ToC removal after reconstructing; just find content start
    post_header_start = safety_end if safety_end > safety_start >= 0 else header_end + 1

    toc_start = -1
    for i in range(post_header_start, min(post_header_start + 30, len(lines))):
        if RE_TOC.match(lines[i]):
            toc_start = i
            break

    content_start = post_header_start
    if toc_start >= 0:
        # Advance past ToC to content
        j = toc_start + 1
        while j < len(lines):
            if RE_CHAPTER.match(lines[j]):
                content_start = j
                break
            if RE_SEP.match(lines[j]):
                content_start = j + 1
                break
            j += 1

    # Skip stray separators/blanks at content start
    while content_start < len(lines) and (
        not lines[content_start].strip() or RE_SEP.match(lines[content_start])
    ):
        content_start += 1

    # -- Find BLUF in content --
    bluf_idx, bluf_text = find_bluf(lines, content_start, search_limit=120)

    # -- Build compact header --
    new_header = [f'# {h1}', '']

    if bluf_text:
        new_header.append(f'> **BLUF:** {bluf_text}')
    if prereq_raw:
        new_header.append(f'> **Prereqs:** {prereq_raw}')
    new_header.append('> *HQ USAREUR-AF · v1.0 · 2026 · DISTRIB: USG only · AUTH: C2DAO/UDRA v1.1*')
    new_header.append('')

    for c in callouts:
        new_header.append(c)
    if callouts:
        new_header.append('')

    new_header.append('---')
    new_header.append('')

    content_lines = lines[content_start:]
    result = new_header + content_lines
    lines_saved = len(lines) - len(result)
    return result, lines_saved


def transform_concepts(lines: list[str]) -> tuple[list[str] | None, int]:
    """
    Transformation for CONCEPTS_GUIDE_*.md files.
    Compact header + remove ToC.
    """
    if any(RE_PROCESSED.match(l) for l in lines[:20]):
        return None, 0

    header_end = first_sep(lines)
    if header_end < 0:
        return None, 0

    # Extract metadata
    h1 = next((RE_H1.match(l).group(1) for l in lines[:header_end] if RE_H1.match(l)), '')
    h2_parts = [RE_H2.match(l).group(1) for l in lines[:header_end]
                if RE_H2.match(l) and not RE_SAFETY.match(l) and not RE_TOC.match(l)]

    prereq_raw = next(
        (RE_PREREQ.match(l).group(1).strip() for l in lines[:header_end] if RE_PREREQ.match(l)), ''
    )
    purpose_raw = next(
        (RE_PURPOSE.match(l).group(1).strip() for l in lines[:header_end] if RE_PURPOSE.match(l)), ''
    )

    # Find content start (past header + ToC)
    toc_start = -1
    for i in range(header_end, min(header_end + 25, len(lines))):
        if RE_TOC.match(lines[i]):
            toc_start = i
            break

    content_start = header_end + 1
    if toc_start >= 0:
        j = toc_start + 1
        while j < len(lines):
            if RE_CHAPTER.match(lines[j]) or RE_H2.match(lines[j]):
                content_start = j
                break
            if RE_SEP.match(lines[j]):
                content_start = j + 1
                break
            j += 1

    while content_start < len(lines) and (
        not lines[content_start].strip() or RE_SEP.match(lines[content_start])
    ):
        content_start += 1

    # Find BLUF in first section
    bluf_idx, bluf_text = find_bluf(lines, content_start, search_limit=80)

    # Build compact header
    subtitle = ' · '.join(h2_parts) if h2_parts else ''
    title_line = f'# {h1}' + (f' — {subtitle}' if subtitle else '')

    new_header = [title_line, '']
    if bluf_text:
        new_header.append(f'> **BLUF:** {bluf_text}')
    if prereq_raw:
        new_header.append(f'> **Prereqs:** {prereq_raw}')
    if purpose_raw:
        new_header.append(f'> **Purpose:** {purpose_raw}')
    new_header.append('> *HQ USAREUR-AF · v1.0 · 2026 · DISTRIB: USG only*')
    new_header.append('')
    new_header.append('---')
    new_header.append('')

    content_lines = lines[content_start:]
    result = new_header + content_lines
    lines_saved = len(lines) - len(result)
    return result, lines_saved


def transform_toc_only(lines: list[str]) -> tuple[list[str] | None, int]:
    """Remove ToC from any file without restructuring the header."""
    result, removed = remove_toc(lines)
    if removed == 0:
        return None, 0
    return result, removed


# --- File routing ---

def classify_file(path: Path) -> str:
    name = path.name
    if re.match(r'TM_\d+[A-Z]?_', name) and not name.startswith('CONCEPTS'):
        return 'tm'
    if name.startswith('CONCEPTS_GUIDE_'):
        return 'concepts'
    # Everything else: ToC removal only
    return 'toc_only'


def process_file(path: Path, dry_run: bool = False) -> tuple[int, str]:
    """
    Process one file. Returns (lines_saved, status).
    status: 'changed', 'skipped', 'error'
    """
    try:
        text = path.read_text(encoding='utf-8')
    except Exception as e:
        return 0, f'error: {e}'

    lines = text.splitlines()
    kind = classify_file(path)

    if kind == 'tm':
        new_lines, saved = transform_tm(lines)
    elif kind == 'concepts':
        new_lines, saved = transform_concepts(lines)
    else:
        new_lines, saved = transform_toc_only(lines)

    if new_lines is None or saved <= 0:
        return 0, 'skipped'

    if not dry_run:
        path.write_text('\n'.join(new_lines) + '\n', encoding='utf-8')

    return saved, 'changed'


def collect_targets(base: Path) -> list[Path]:
    """Collect all target .md files (exclude node_modules, _archive, _archive_pre_review)."""
    exclude = {'node_modules', '_archive', '_archive_pre_review', 'training_data'}
    targets = []
    for p in base.rglob('*.md'):
        if any(part in exclude for part in p.parts):
            continue
        targets.append(p)
    return sorted(targets)


def main():
    dry_run = '--dry-run' in sys.argv
    args = [a for a in sys.argv[1:] if not a.startswith('--')]

    if args:
        targets = [Path(a).resolve() for a in args]
    else:
        targets = collect_targets(BASE)

    total_saved = 0
    changed = 0
    skipped = 0
    errors = 0

    for path in targets:
        saved, status = process_file(path, dry_run=dry_run)
        rel = path.relative_to(BASE.parent) if BASE.parent in path.parents else path
        if status == 'changed':
            total_saved += saved
            changed += 1
            sign = '[DRY]' if dry_run else '[OK]'
            print(f'{sign} {rel}  -{saved} lines')
        elif status == 'error':
            errors += 1
            print(f'[ERR] {rel}  {saved}')
        else:
            skipped += 1

    print()
    print(f'Files changed: {changed}  |  Skipped: {skipped}  |  Errors: {errors}')
    print(f'Total lines removed: {total_saved}')
    if dry_run:
        print('(dry run — no files written)')


if __name__ == '__main__':
    main()
