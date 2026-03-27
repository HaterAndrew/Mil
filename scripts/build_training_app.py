#!/usr/bin/env python3
"""Build training app data from TM markdown sources.

Parses TM-10, TM-20, TM-30 markdown files into structured JSON for the
training_app static HTML app. Extracts chapters, tasks (CONDITIONS/STANDARDS/
PROCEDURE), concept sections, and chapter intros.

Usage:
    python3 scripts/build_training_app.py
"""

import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TM_DIR = ROOT / "maven_training" / "tm"
OUT_FILE = ROOT / "maven_training" / "training_app" / "data" / "modules.json"

# Which TMs to parse for MVP (Pattern A: ## TASK / ### TASK)
MVP_TMS = [
    {
        "dir": "TM_10_maven_user",
        "file": "TM_10_MAVEN_USER.md",
        "id": "tm-10",
        "code": "TM-10",
        "slLevel": "SL 1",
        "title": "Maven User",
        "prereqs": [],
    },
    {
        "dir": "TM_20_builder",
        "file": "TM_20_BUILDER.md",
        "id": "tm-20",
        "code": "TM-20",
        "slLevel": "SL 2",
        "title": "Builder",
        "prereqs": ["tm-10"],
    },
    {
        "dir": "TM_30_advanced_builder",
        "file": "TM_30_ADVANCED_BUILDER.md",
        "id": "tm-30",
        "code": "TM-30",
        "slLevel": "SL 3",
        "title": "Advanced Builder",
        "prereqs": ["tm-20"],
    },
]

PREREQ_CHAIN = {
    "tm-10": {"prereqs": [], "next": ["tm-20"]},
    "tm-20": {"prereqs": ["tm-10"], "next": ["tm-30"]},
    "tm-30": {"prereqs": ["tm-20"], "next": []},
}

# Regex patterns
RE_CHAPTER = re.compile(r"^#{1,2}\s+CHAPTER\s+(\d+)\s*[—–-]\s*(.+)", re.IGNORECASE)
RE_TASK = re.compile(r"^#{2,3}\s+TASK\s+(\d+-\d+[A-Za-z]?):\s*(.+)", re.IGNORECASE)
RE_SECTION = re.compile(r"^#{2,3}\s+(\d+-\d+[a-z]?)\.\s+(.+)")
RE_FIELD = re.compile(r"^\*\*([A-Z][A-Z\s]+?):\*\*\s*(.*)")
RE_STEP = re.compile(r"^(\d+)\.\s+(.+)")
RE_CALLOUT = re.compile(
    r"^>\s*\*\*(NOTE|CAUTION|WARNING|BLUF)[:\s]*\*\*\s*(.*)", re.IGNORECASE
)
RE_CALLOUT_BARE = re.compile(
    r"^\*\*(NOTE|CAUTION|WARNING|BLUF)[:\s]*\*\*\s*(.*)", re.IGNORECASE
)
RE_BLUF = re.compile(r"^\*\*BLUF:\*\*\s*(.*)", re.IGNORECASE)


def parse_callouts(lines):
    """Extract callout boxes from a list of lines."""
    callouts = []
    i = 0
    while i < len(lines):
        line = lines[i]
        # Blockquote callouts: > **NOTE:** ...
        m = RE_CALLOUT.match(line)
        if not m:
            m = RE_CALLOUT_BARE.match(line)
        if m:
            ctype = m.group(1).upper()
            text = m.group(2).strip()
            # Continuation lines
            j = i + 1
            while j < len(lines):
                cont = lines[j]
                if cont.startswith("> ") and not RE_CALLOUT.match(cont):
                    text += " " + cont[2:].strip()
                    j += 1
                elif cont.strip() and not cont.startswith("#") and not RE_CALLOUT.match(cont) and not RE_CALLOUT_BARE.match(cont) and not RE_FIELD.match(cont):
                    # Only continue if it looks like flowing text
                    if cont.startswith("  ") or (not cont.startswith("*") and not cont.startswith("-") and not RE_STEP.match(cont)):
                        break
                    break
                else:
                    break
            callouts.append({"type": ctype, "text": text.strip()})
            i = j
            continue
        i += 1
    return callouts


def extract_intro(lines, max_paragraphs=3):
    """Extract the first few paragraphs as chapter intro."""
    paragraphs = []
    current = []
    for line in lines:
        stripped = line.strip()
        if not stripped:
            if current:
                paragraphs.append(" ".join(current))
                current = []
                if len(paragraphs) >= max_paragraphs:
                    break
        elif stripped.startswith("#"):
            break
        elif stripped.startswith("---"):
            if current:
                paragraphs.append(" ".join(current))
            break
        elif stripped.startswith("|") or stripped.startswith("```"):
            # Skip tables and code blocks for intro
            if current:
                paragraphs.append(" ".join(current))
            break
        else:
            current.append(stripped)
    if current and len(paragraphs) < max_paragraphs:
        paragraphs.append(" ".join(current))
    return "\n\n".join(paragraphs)


def parse_task_block(lines):
    """Parse a task block starting after the TASK heading.

    Returns dict with conditions, standards, equipment, duration, steps, callouts.
    """
    task = {
        "conditions": "",
        "standards": "",
        "equipment": "",
        "duration": "",
        "steps": [],
        "callouts": [],
    }

    current_field = None
    current_text = []
    all_steps = []
    in_procedure = False

    for line in lines:
        stripped = line.strip()

        # Check for procedure sub-heading: **PROCEDURE — Sub-title:**
        # Must check BEFORE RE_FIELD since em-dash breaks the field regex
        proc_sub = re.match(
            r"^\*\*PROCEDURE\s*[—–\-]\s*(.+?):\*\*", stripped, re.IGNORECASE
        )
        if proc_sub:
            # Save previous field
            if current_field and current_field != "procedure":
                task[current_field] = " ".join(current_text).strip()
            in_procedure = True
            current_field = "procedure"
            current_text = []
            # Insert sub-procedure heading as a labeled step group
            sub_label = proc_sub.group(1).strip()
            all_steps.append(f"0. [[ {sub_label} ]]")
            continue

        # Check for field markers
        fm = RE_FIELD.match(stripped)
        if fm:
            field_name = fm.group(1).strip().lower()
            field_val = fm.group(2).strip()

            # Save previous field
            if current_field and current_field != "procedure":
                task[current_field] = " ".join(current_text).strip()

            if field_name == "procedure":
                in_procedure = True
                current_field = "procedure"
                current_text = []
                continue
            elif field_name in ("conditions", "standards", "equipment", "duration", "task"):
                if field_name == "task":
                    # TM-20 has a TASK: field — store as description
                    current_field = None
                    continue
                current_field = field_name
                current_text = [field_val] if field_val else []
                in_procedure = False
                continue

        if in_procedure:
            # Check for bold step group heading: **Step N — Title:**
            step_heading = re.match(
                r"^\*\*Step\s+(\d+)\s*[—–\-]\s*(.+?):\*\*$", stripped, re.IGNORECASE
            )
            if step_heading:
                sub_label = step_heading.group(2).strip()
                all_steps.append(f"0. [[ {sub_label} ]]")
                continue
            sm = RE_STEP.match(stripped)
            if sm:
                all_steps.append(stripped)
            elif stripped and all_steps:
                # Continuation of previous step or sub-step
                all_steps[-1] += " " + stripped
        elif current_field and current_field != "procedure":
            if stripped and not stripped.startswith("#"):
                current_text.append(stripped)

    # Save last field
    if current_field and current_field != "procedure":
        task[current_field] = " ".join(current_text).strip()

    task["steps"] = all_steps
    task["callouts"] = parse_callouts(lines)

    return task


def parse_tm(tm_config):
    """Parse a single TM markdown file into structured module data."""
    filepath = TM_DIR / tm_config["dir"] / tm_config["file"]
    if not filepath.exists():
        print(f"  WARNING: {filepath} not found, skipping")
        return None

    text = filepath.read_text(encoding="utf-8")
    all_lines = text.splitlines()

    module = {
        "id": tm_config["id"],
        "code": tm_config["code"],
        "slLevel": tm_config["slLevel"],
        "title": tm_config["title"],
        "contentType": "procedural",
        "prereqs": tm_config["prereqs"],
        "conceptsGuide": None,
        "slideDecks": [],
        "selfStudyResources": [],
        "chapters": [],
    }

    # Split into chapter blocks
    chapter_starts = []
    for i, line in enumerate(all_lines):
        m = RE_CHAPTER.match(line)
        if m:
            chapter_starts.append((i, int(m.group(1)), m.group(2).strip()))

    if not chapter_starts:
        print(f"  WARNING: No chapters found in {filepath.name}")
        return module

    # Process each chapter
    for idx, (start_line, ch_num, ch_title) in enumerate(chapter_starts):
        end_line = chapter_starts[idx + 1][0] if idx + 1 < len(chapter_starts) else len(all_lines)
        ch_lines = all_lines[start_line + 1 : end_line]

        chapter = {
            "id": f"{tm_config['id'].replace('-', '')}-ch{ch_num}",
            "number": ch_num,
            "title": ch_title,
            "chapterType": "enabling",  # default, upgraded to "performance" if tasks found
            "intro": "",
            "objective": "",
            "units": [],
        }

        # Find all tasks and sections within this chapter
        unit_starts = []  # (line_offset, type, ref, title)
        for j, line in enumerate(ch_lines):
            tm = RE_TASK.match(line)
            if tm:
                unit_starts.append((j, "task", tm.group(1), tm.group(2).strip()))
                continue
            sm = RE_SECTION.match(line)
            if sm:
                unit_starts.append((j, "concept", sm.group(1), sm.group(2).strip()))

        # Extract chapter intro from lines before first unit
        intro_end = unit_starts[0][0] if unit_starts else len(ch_lines)
        intro_lines = ch_lines[:intro_end]
        chapter["intro"] = extract_intro(intro_lines)

        # Extract BLUF from intro if present
        for line in intro_lines[:10]:
            bm = RE_BLUF.match(line.strip())
            if bm:
                chapter["objective"] = bm.group(1).strip()
                break

        # Process each unit
        for uidx, (u_start, u_type, u_ref, u_title) in enumerate(unit_starts):
            u_end = unit_starts[uidx + 1][0] if uidx + 1 < len(unit_starts) else len(ch_lines)
            u_lines = ch_lines[u_start + 1 : u_end]

            if u_type == "task":
                chapter["chapterType"] = "performance"
                task_data = parse_task_block(u_lines)
                unit = {
                    "type": "task",
                    "id": f"{tm_config['id'].replace('-', '')}-task-{u_ref.lower()}",
                    "ref": f"TASK {u_ref}",
                    "title": u_title,
                    "conditions": task_data["conditions"],
                    "standards": task_data["standards"],
                    "equipment": task_data["equipment"],
                    "duration": task_data["duration"],
                    "steps": task_data["steps"],
                    "callouts": task_data["callouts"],
                }
                chapter["units"].append(unit)
            else:
                # Concept section
                content = extract_intro(u_lines, max_paragraphs=5)
                bluf = ""
                for line in u_lines[:5]:
                    bm = RE_BLUF.match(line.strip())
                    if bm:
                        bluf = bm.group(1).strip()
                        break
                callouts = parse_callouts(u_lines)
                unit = {
                    "type": "concept",
                    "id": f"{tm_config['id'].replace('-', '')}-{u_ref.lower().replace('.', '')}",
                    "ref": u_ref,
                    "title": u_title,
                    "bluf": bluf,
                    "content": content,
                    "callouts": callouts,
                }
                chapter["units"].append(unit)

        # Set chapter objective from first task standards if not set from BLUF
        if not chapter["objective"]:
            for u in chapter["units"]:
                if u["type"] == "task" and u.get("standards"):
                    chapter["objective"] = u["standards"]
                    break

        module["chapters"].append(chapter)

    return module


def load_alignment_map():
    """Load alignment_map.json to get slide deck mappings."""
    amap_path = ROOT / "maven_training" / "source_material" / "course_portal" / "alignment_map.json"
    if not amap_path.exists():
        return {}
    data = json.loads(amap_path.read_text(encoding="utf-8"))
    # Build TM level -> deck IDs mapping
    mapping = {}
    for entry in data:
        tm_level = entry.get("maven_tm_level", "")
        if tm_level:
            mapping.setdefault(tm_level, []).append(entry.get("id", ""))
        for also in entry.get("maven_tm_also_supports", []):
            if also:
                mapping.setdefault(also, []).append(entry.get("id", ""))
    return mapping


def main():
    print("Building training app data...")
    print(f"  TM source: {TM_DIR}")
    print(f"  Output:    {OUT_FILE}")

    # Load alignment map for slide deck links
    deck_map = load_alignment_map()

    modules = []
    total_tasks = 0
    total_concepts = 0

    for tm_config in MVP_TMS:
        print(f"\n  Parsing {tm_config['code']} ({tm_config['file']})...")
        module = parse_tm(tm_config)
        if module is None:
            continue

        # Attach slide decks from alignment map
        module["slideDecks"] = deck_map.get(tm_config["code"], [])

        # Count units
        task_count = 0
        concept_count = 0
        for ch in module["chapters"]:
            for u in ch["units"]:
                if u["type"] == "task":
                    task_count += 1
                else:
                    concept_count += 1

        print(f"    {len(module['chapters'])} chapters, {task_count} tasks, {concept_count} concept sections")
        total_tasks += task_count
        total_concepts += concept_count
        modules.append(module)

    output = {
        "generated": datetime.now(timezone.utc).isoformat(),
        "prereqChain": PREREQ_CHAIN,
        "modules": modules,
    }

    OUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUT_FILE.write_text(json.dumps(output, indent=2, ensure_ascii=False), encoding="utf-8")

    print(f"\n  Done. {len(modules)} modules, {total_tasks} tasks, {total_concepts} concepts")
    print(f"  Output: {OUT_FILE}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
