#!/usr/bin/env python3
"""check_sharepoint_sync.py — Diff index.html vs index_sharepoint.html.

Compares the two HTML variants to detect content drift. Only the CSP
meta tag and frame/connect-src policies should differ; all other content
must be identical.

Exit 0: files are in sync (CSP-only differences)
Exit 1: structural content has diverged

Run from repo root:
    python scripts/check_sharepoint_sync.py
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
INDEX_HTML = REPO_ROOT / "maven_training" / "mss_info_app" / "index.html"
INDEX_SP = REPO_ROOT / "maven_training" / "mss_info_app" / "index_sharepoint.html"

# Lines that are expected to differ (CSP and related meta tags)
CSP_PATTERN = re.compile(
    r'<meta\s+http-equiv=["\']Content-Security-Policy["\']',
    re.IGNORECASE,
)

# Normalize whitespace for comparison
def _normalize(line: str) -> str:
    """Collapse whitespace for comparison; strip trailing."""
    return re.sub(r"\s+", " ", line).strip()


def diff_files(path_a: Path, path_b: Path) -> tuple[list[str], list[str]]:
    """Compare two HTML files line by line.

    Returns (expected_diffs, unexpected_diffs).
    Expected diffs are CSP meta tag differences.
    Unexpected diffs are content divergence that needs fixing.
    """
    lines_a = path_a.read_text(encoding="utf-8").splitlines()
    lines_b = path_b.read_text(encoding="utf-8").splitlines()

    expected: list[str] = []
    unexpected: list[str] = []

    max_lines = max(len(lines_a), len(lines_b))

    for i in range(max_lines):
        line_a = lines_a[i] if i < len(lines_a) else "<EOF>"
        line_b = lines_b[i] if i < len(lines_b) else "<EOF>"

        norm_a = _normalize(line_a)
        norm_b = _normalize(line_b)

        if norm_a == norm_b:
            continue

        # Check if the difference is in a CSP meta tag
        if CSP_PATTERN.search(line_a) or CSP_PATTERN.search(line_b):
            expected.append(f"  L{i+1}: CSP policy (expected)")
            continue

        # Unexpected difference
        unexpected.append(
            f"  L{i+1}:\n"
            f"    index.html:            {norm_a[:120]}\n"
            f"    index_sharepoint.html:  {norm_b[:120]}"
        )

    # Line count difference
    if len(lines_a) != len(lines_b):
        unexpected.append(
            f"  Line count: index.html has {len(lines_a)}, "
            f"index_sharepoint.html has {len(lines_b)}"
        )

    return expected, unexpected


def main() -> int:
    for path, label in [(INDEX_HTML, "index.html"), (INDEX_SP, "index_sharepoint.html")]:
        if not path.exists():
            print(f"ERROR: {label} not found at {path}", file=sys.stderr)
            return 1

    expected, unexpected = diff_files(INDEX_HTML, INDEX_SP)

    print(f"Comparing index.html ({INDEX_HTML.stat().st_size:,} bytes) "
          f"vs index_sharepoint.html ({INDEX_SP.stat().st_size:,} bytes)")

    if expected:
        print(f"\nExpected differences ({len(expected)}):")
        for d in expected:
            print(d)

    if unexpected:
        print(f"\nUNEXPECTED DIFFERENCES ({len(unexpected)}):")
        for d in unexpected:
            print(d)
        print(f"\nFAILED — {len(unexpected)} content divergence(s) found.")
        return 1

    print("\nOK — files are in sync (CSP-only differences).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
