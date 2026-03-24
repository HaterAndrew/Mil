#!/usr/bin/env python3
"""
check_platform_updates.py — Flag curriculum sections that may need revision
when Palantir ships a new Foundry release.

Source: Palantir public release notes at
  https://www.palantir.com/docs/foundry/release-notes/

The page embeds structured JSON (Next.js __NEXT_DATA__) with every release
entry: title, description, category, type (FEATURE/ENHANCEMENT/FIX), date.
This script extracts that data and matches keywords to TM sections.

Config files (auto-created on first run):
  scripts/platform_state.json       — last-reviewed date + cached entries
  scripts/platform_feature_map.json — keyword → TM section mapping

Run from repo root:
    python scripts/check_platform_updates.py                    # fetch current year
    python scripts/check_platform_updates.py --year 2025        # fetch a specific year
    python scripts/check_platform_updates.py --file notes.txt   # parse a local file
    python scripts/check_platform_updates.py --mark 2026-03-19  # mark a date as reviewed
    python scripts/check_platform_updates.py --report           # regenerate from cache
"""

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.error import URLError

ROOT = Path(__file__).resolve().parent.parent
SCRIPTS = ROOT / "scripts"
STATE_FILE = SCRIPTS / "platform_state.json"
FEATURE_MAP_FILE = SCRIPTS / "platform_feature_map.json"
REPORT_FILE = ROOT / "platform_update_report.md"

RELEASE_NOTES_URL = "https://www.palantir.com/docs/foundry/release-notes"

# ── Default feature→curriculum mapping ────────────────────────────────────
# Keys: lowercase keywords found in Palantir release note titles/descriptions
# Values: list of TM sections affected
DEFAULT_FEATURE_MAP = {
    "pipeline builder": ["TM-20", "TM-30"],
    "pipeline": ["TM-20", "TM-30", "TM-40L"],
    "ontology": ["TM-20", "TM-30", "TM-40K"],
    "workshop": ["TM-10", "TM-20", "TM-30"],
    "aip logic": ["TM-30"],
    "aip": ["TM-30", "TM-40H"],
    "agent studio": ["TM-30", "TM-40H"],
    "quiver": ["TM-20", "TM-30"],
    "contour": ["TM-20", "TM-30"],
    "code repositories": ["TM-40L", "TM-40O"],
    "code workbook": ["TM-40G", "TM-40L", "TM-40M"],
    "foundry ml": ["TM-40M", "TM-50M"],
    "model studio": ["TM-40M", "TM-50M"],
    "actions": ["TM-20", "TM-30"],
    "object type": ["TM-20", "TM-30"],
    "object views": ["TM-20", "TM-30"],
    "writeback": ["TM-20", "TM-30"],
    "automations": ["TM-30"],
    "autopilot": ["TM-30"],
    "machinery": ["TM-30"],
    "data connection": ["TM-40O"],
    "data integration": ["TM-40O"],
    "magritte": ["TM-40O"],
    "slate": ["TM-40L", "TM-40N"],
    "osdk": ["TM-40L", "TM-50L"],
    "developer console": ["TM-40L", "TM-40O"],
    "third-party": ["TM-40O"],
    "security": ["TM-10", "TM-30"],
    "markings": ["TM-10", "TM-30"],
    "permissions": ["TM-10", "TM-30"],
    "sensitive data": ["TM-10", "TM-30"],
    "gaia": ["TM-10"],
    "compass": ["TM-10"],
    "workflow lineage": ["TM-30", "TM-40J"],
    "scheduling": ["TM-40J"],
    "ci/cd": ["TM-40O", "TM-50O"],
    "compute module": ["TM-40O", "TM-50O"],
    "webhook": ["TM-40O"],
    "data health": ["TM-30"],
    "data quality": ["TM-30", "TM-40G"],
    "typeclass": ["TM-30"],
    "interface": ["TM-30"],
    "transforms": ["TM-40L", "TM-40O"],
    "functions": ["TM-40L"],
    "foundry branching": ["TM-20", "TM-30"],
    "marketplace": ["TM-40L", "TM-40O"],
    "document intelligence": ["TM-40H", "TM-40K"],
    "notepad": ["TM-10", "TM-20"],
}

DEFAULT_STATE = {
    "last_reviewed_date": "",
    "last_fetch_date": "",
    "cached_entries": [],
}


def load_json(path, default):
    if path.exists():
        return json.loads(path.read_text())
    return default.copy()


def save_json(path, data):
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")


def init_files():
    """Create config files with defaults if they don't exist."""
    if not FEATURE_MAP_FILE.exists():
        save_json(FEATURE_MAP_FILE, DEFAULT_FEATURE_MAP)
        print(f"  Created {FEATURE_MAP_FILE.relative_to(ROOT)}")
    if not STATE_FILE.exists():
        save_json(STATE_FILE, DEFAULT_STATE)
        print(f"  Created {STATE_FILE.relative_to(ROOT)}")


# ── Palantir release notes fetcher ───────────────────────────────────────

def parse_date(date_str):
    """Parse 'March 19, 2026' → '2026-03-19'."""
    for fmt in ("%B %d, %Y", "%Y-%m-%d", "%b %d, %Y"):
        try:
            return datetime.strptime(date_str.strip(), fmt).strftime("%Y-%m-%d")
        except ValueError:
            continue
    return ""


def fetch_palantir(year=None):
    """Fetch Palantir release notes. Returns flat list of entry dicts.

    The page at /docs/foundry/release-notes/ (or /release-notes/YYYY/)
    embeds a __NEXT_DATA__ JSON blob with all release entries.
    """
    if year:
        url = f"{RELEASE_NOTES_URL}/{year}/"
    else:
        url = RELEASE_NOTES_URL
    print(f"  Fetching: {url}")

    req = Request(url, headers={
        "User-Agent": "MavenTraining/1.0",
        "Accept": "text/html",
    })
    try:
        with urlopen(req, timeout=20) as resp:
            raw = resp.read().decode("utf-8", errors="replace")
    except URLError as e:
        print(f"  ERROR: Could not fetch {url}: {e}")
        return []

    # Extract __NEXT_DATA__ JSON
    m = re.search(r"__NEXT_DATA__[^>]*>(.*?)</script>", raw, re.DOTALL)
    if not m:
        print("  ERROR: Could not find __NEXT_DATA__ in page")
        return []

    try:
        data = json.loads(m.group(1))
    except json.JSONDecodeError as e:
        print(f"  ERROR: Failed to parse JSON: {e}")
        return []

    releases = (
        data.get("props", {}).get("pageProps", {}).get("releases", [])
    )
    if not releases:
        print("  WARNING: No releases found in page data")
        return []

    # Flatten: each release date has multiple releaseNotes
    entries = []
    for rel in releases:
        date_str = rel.get("date", "")
        iso_date = parse_date(date_str)
        for note in rel.get("releaseNotes", []):
            entries.append({
                "title": note.get("title", "").strip(),
                "description": note.get("description", "").strip(),
                "category": note.get("categoryTitle", "").strip(),
                "type": note.get("type", "").strip(),
                "date": iso_date,
                "date_display": date_str,
                "app": note.get("applicationTitle", "").strip(),
            })

    return entries


def parse_local_file(filepath):
    """Read a local file. If HTML with __NEXT_DATA__, parse as Palantir page."""
    p = Path(filepath)
    if not p.exists():
        print(f"  ERROR: File not found: {filepath}")
        return []
    text = p.read_text(errors="replace")

    # Check for __NEXT_DATA__ (saved Palantir HTML)
    m = re.search(r"__NEXT_DATA__[^>]*>(.*?)</script>", text, re.DOTALL)
    if m:
        try:
            data = json.loads(m.group(1))
            releases = data.get("props", {}).get("pageProps", {}).get("releases", [])
            entries = []
            for rel in releases:
                date_str = rel.get("date", "")
                iso_date = parse_date(date_str)
                for note in rel.get("releaseNotes", []):
                    entries.append({
                        "title": note.get("title", "").strip(),
                        "description": note.get("description", "").strip(),
                        "category": note.get("categoryTitle", "").strip(),
                        "type": note.get("type", "").strip(),
                        "date": iso_date,
                        "date_display": date_str,
                        "app": note.get("applicationTitle", "").strip(),
                    })
            return entries
        except json.JSONDecodeError:
            pass

    # Plain text fallback: one entry per line or section
    return [{"title": "Local notes", "description": text[:3000],
             "category": "", "type": "", "date": "", "date_display": "",
             "app": ""}]


# ── Matching and reporting ───────────────────────────────────────────────

def match_features(entries, feature_map, last_reviewed_date):
    """Match entry text against feature keywords. Returns affected sections."""
    hits = {}  # TM section → list of (keyword, title, date, category, type)

    for entry in entries:
        # Skip entries at or before the last-reviewed date
        if last_reviewed_date and entry["date"] and entry["date"] <= last_reviewed_date:
            continue

        combined = f"{entry['title']} {entry['description']} {entry['category']} {entry['app']}".lower()
        for keyword, sections in feature_map.items():
            if keyword.lower() in combined:
                for sec in sections:
                    hits.setdefault(sec, [])
                    hits[sec].append((
                        keyword,
                        entry["title"],
                        entry["date"],
                        entry["category"],
                        entry["type"],
                    ))

    # Deduplicate
    for sec in hits:
        seen = set()
        deduped = []
        for item in hits[sec]:
            key = (item[0], item[1])
            if key not in seen:
                seen.add(key)
                deduped.append(item)
        hits[sec] = deduped

    return hits


def generate_report(hits, entries, state):
    """Generate a Markdown report of flagged curriculum sections."""
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    last_date = state.get("last_reviewed_date", "N/A") or "N/A"

    # Count entries after cutoff
    cutoff = state.get("last_reviewed_date", "")
    new_count = sum(1 for e in entries if not cutoff or not e["date"] or e["date"] > cutoff)

    lines = [
        "# Platform Update — Curriculum Review Flag",
        "",
        f"**Generated:** {now}",
        f"**Last reviewed through:** {last_date}",
        f"**Total entries fetched:** {len(entries)}",
        f"**New entries since last review:** {new_count}",
        f"**Source:** [Palantir Foundry Release Notes]({RELEASE_NOTES_URL})",
        "",
    ]

    if not hits:
        lines.append("No curriculum sections flagged. All clear.")
        lines.append("")
    else:
        lines.append(f"**{len(hits)} section(s) flagged for review:**")
        lines.append("")

        for sec in sorted(hits.keys()):
            reasons = hits[sec]
            lines.append(f"## {sec}")
            lines.append("")
            lines.append("| Keyword | Release Note | Date | Category | Type |")
            lines.append("|---------|-------------|------|----------|------|")
            for keyword, title, date, category, rtype in reasons:
                lines.append(f"| {keyword} | {title} | {date} | {category} | {rtype} |")
            lines.append("")

    lines.append("---")
    lines.append(
        "After review, run: `python scripts/check_platform_updates.py --mark YYYY-MM-DD`"
    )
    lines.append("")

    report = "\n".join(lines)
    REPORT_FILE.write_text(report)
    return report


def main():
    parser = argparse.ArgumentParser(
        description="Flag curriculum sections affected by Foundry platform updates"
    )
    parser.add_argument(
        "--year",
        help="Fetch a specific year (e.g. 2025). Default: current year page.",
    )
    parser.add_argument(
        "--file", "-f",
        help="Parse a local file (saved HTML or plaintext) instead of fetching",
    )
    parser.add_argument(
        "--mark", "-m",
        help="Mark a date as reviewed (YYYY-MM-DD, e.g. 2026-03-19)",
    )
    parser.add_argument(
        "--report", "-r",
        action="store_true",
        help="Regenerate report from cached entries",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print report to stdout instead of writing file",
    )
    args = parser.parse_args()

    init_files()
    state = load_json(STATE_FILE, DEFAULT_STATE)
    feature_map = load_json(FEATURE_MAP_FILE, DEFAULT_FEATURE_MAP)

    # -- Mark date as reviewed --
    if args.mark:
        state["last_reviewed_date"] = args.mark
        save_json(STATE_FILE, state)
        print(f"  Marked {args.mark} as reviewed")
        return

    # -- Fetch or load entries --
    if args.report:
        entries = state.get("cached_entries", [])
        if not entries:
            print("  No cached entries. Run without --report first.")
            sys.exit(1)
    elif args.file:
        print(f"  Parsing local file: {args.file}")
        entries = parse_local_file(args.file)
    else:
        entries = fetch_palantir(args.year)

    if not entries:
        print("  No release entries found.")
        sys.exit(1)

    print(f"  Found {len(entries)} release entries")

    # Cache entries
    state["cached_entries"] = entries
    state["last_fetch_date"] = datetime.now(timezone.utc).isoformat()
    save_json(STATE_FILE, state)

    # Match against feature map
    last_date = state.get("last_reviewed_date", "")
    hits = match_features(entries, feature_map, last_date)

    # Generate report
    report = generate_report(hits, entries, state)

    if args.dry_run:
        print(report)
    else:
        print(f"  Report written to: {REPORT_FILE.relative_to(ROOT)}")
        print(f"  {len(hits)} section(s) flagged")


if __name__ == "__main__":
    main()
