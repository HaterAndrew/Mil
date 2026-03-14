#!/usr/bin/env python3
"""
build_pdfs.py — Convert maven_training markdown files to Army doctrine-style PDFs.

Toolchain: Python `markdown` → styled HTML → Chrome CDP Page.printToPDF
           (CDP used instead of --print-to-pdf CLI flag so we get real
            header/footer templates that land in the margin area on every page.)
Output: maven_training/pdf/
"""

import base64
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
import hashlib
import json
import os
import re
import subprocess
import sys
import tempfile
import time

import markdown
from pathlib import Path

# Local modules extracted for maintainability
from chrome_cdp import html_file_to_pdf
from publication_css import PAGE_CSS

# ── Config ────────────────────────────────────────────────────────────────────
REPO_ROOT = Path(__file__).parent.parent
OUT_DIR   = REPO_ROOT / "maven_training" / "pdf"


def _find_chrome() -> str:
    """Return the path to a Chrome/Chromium binary, or raise RuntimeError."""
    import shutil
    candidates = ["google-chrome", "google-chrome-stable", "chromium-browser", "chromium"]
    for name in candidates:
        path = shutil.which(name)
        if path:
            return path
    raise RuntimeError(
        "No Chrome/Chromium binary found. Install google-chrome or chromium-browser "
        "and ensure it is on PATH before running this script."
    )


CHROME = _find_chrome()
PUB_DATE  = datetime.utcnow().strftime("%-d %B %Y").upper()
HQ_LINES  = [
    "HEADQUARTERS",
    "UNITED STATES ARMY EUROPE AND AFRICA",
    "(USAREUR-AF)",
    "Wiesbaden, Germany",
]
DIST_STMT = "DRAFT — NOT FOR OFFICIAL USE. FOR TRAINING PLANNING PURPOSES ONLY."

# ── Publication type metadata ─────────────────────────────────────────────────
PUB_TYPES = {
    "TM_10":        ("TECHNICAL MANUAL",                    "TM-10"),
    "TM_20":        ("TECHNICAL MANUAL",                    "TM-20"),
    "TM_30":        ("TECHNICAL MANUAL",                    "TM-30"),
    # WFF tracks (A–F, operational)
    "TM_40A":       ("TECHNICAL MANUAL",                    "TM-40A"),
    "TM_40B":       ("TECHNICAL MANUAL",                    "TM-40B"),
    "TM_40C":       ("TECHNICAL MANUAL",                    "TM-40C"),
    "TM_40D":       ("TECHNICAL MANUAL",                    "TM-40D"),
    "TM_40E":       ("TECHNICAL MANUAL",                    "TM-40E"),
    "TM_40F":       ("TECHNICAL MANUAL",                    "TM-40F"),
    # Technical specialist tracks (G–L)
    "TM_40G":       ("TECHNICAL MANUAL",                    "TM-40G"),
    "TM_40H":       ("TECHNICAL MANUAL",                    "TM-40H"),
    "TM_40I":       ("TECHNICAL MANUAL",                    "TM-40I"),
    "TM_40J":       ("TECHNICAL MANUAL",                    "TM-40J"),
    "TM_40K":       ("TECHNICAL MANUAL",                    "TM-40K"),
    "TM_40L":       ("TECHNICAL MANUAL",                    "TM-40L"),
    # Technical specialist advanced tracks (50G–L)
    "TM_50G":       ("TECHNICAL MANUAL",                    "TM-50G"),
    "TM_50H":       ("TECHNICAL MANUAL",                    "TM-50H"),
    "TM_50I":       ("TECHNICAL MANUAL",                    "TM-50I"),
    "TM_50J":       ("TECHNICAL MANUAL",                    "TM-50J"),
    "TM_50K":       ("TECHNICAL MANUAL",                    "TM-50K"),
    "TM_50L":       ("TECHNICAL MANUAL",                    "TM-50L"),
    "ADP":               ("ARMY DOCTRINE PUBLICATION",           "ADP 1"),
    "ADRP":              ("ARMY DOCTRINE REFERENCE PUBLICATION", "ADRP 1"),
    "DATA_LITERACY_S":   ("DATA LITERACY",                       "ADRP-SL"),   # senior leaders
    "DATA_LITERACY":     ("DATA LITERACY TECHNICAL REFERENCE",   "ADRP-TR"),   # full reference
    "GLOSS":             ("GLOSSARY",                            "GLOSSARY"),
    "NAMING":            ("STANDARDS AND GOVERNANCE",            "MSS-GOV"),
    "MTP":               ("MISSION TRAINING PLAN",               "MTP-MSS"),
    "POI":               ("PROGRAM OF INSTRUCTION",              "POI-MSS"),
    "TEO":               ("TRAINING AND EVALUATION OUTLINE",     "T&EO-MSS"),
    "CAD":               ("COURSE ADMINISTRATIVE DATA",          "CAD-MSS"),
    "POLICY":            ("POLICY LETTER",                       "USAREUR-AF G6"),
    "ENROLLMENT":        ("STANDARD OPERATING PROCEDURE",        "SOP-ENROLL"),
    "ANNUAL_TRAINING":   ("ANNUAL TRAINING SCHEDULE",            "ATS-FY26"),
    "FACULTY":           ("FACULTY DEVELOPMENT PLAN",            "FDP-MSS"),
    "COMPLETION":        ("CERTIFICATE TEMPLATES",               "CERT-MSS"),
    "LP_TEMPLATE":       ("LESSON PLAN TEMPLATE",                "LP-TEMPLATE"),
    "TM10_LESSON":       ("LESSON PLANS",                        "TM-10"),
    "TM20_LESSON":       ("LESSON PLANS",                        "TM-20"),
    "TM30_LESSON":       ("LESSON PLANS",                        "TM-30"),
    "TM40_SPECIALIST":   ("LESSON PLANS",                        "TM-40"),
    "CONCEPTS_GUIDE_TM40A": ("CONCEPTS GUIDE",                   "TM-40A"),
    "CONCEPTS_GUIDE_TM40B": ("CONCEPTS GUIDE",                   "TM-40B"),
    "CONCEPTS_GUIDE_TM40C": ("CONCEPTS GUIDE",                   "TM-40C"),
    "CONCEPTS_GUIDE_TM40D": ("CONCEPTS GUIDE",                   "TM-40D"),
    "CONCEPTS_GUIDE_TM40E": ("CONCEPTS GUIDE",                   "TM-40E"),
    "CONCEPTS_GUIDE_TM40F": ("CONCEPTS GUIDE",                   "TM-40F"),
    "CONCEPTS_GUIDE_TM40G": ("CONCEPTS GUIDE",                   "TM-40G"),
    "CONCEPTS_GUIDE_TM40H": ("CONCEPTS GUIDE",                   "TM-40H"),
    "CONCEPTS_GUIDE_TM40I": ("CONCEPTS GUIDE",                   "TM-40I"),
    "CONCEPTS_GUIDE_TM40J": ("CONCEPTS GUIDE",                   "TM-40J"),
    "CONCEPTS_GUIDE_TM40K": ("CONCEPTS GUIDE",                   "TM-40K"),
    "CONCEPTS_GUIDE_TM40L": ("CONCEPTS GUIDE",                   "TM-40L"),
    "CONCEPTS_GUIDE_TM50G": ("CONCEPTS GUIDE",                   "TM-50G"),
    "CONCEPTS_GUIDE_TM50H": ("CONCEPTS GUIDE",                   "TM-50H"),
    "CONCEPTS_GUIDE_TM50I": ("CONCEPTS GUIDE",                   "TM-50I"),
    "CONCEPTS_GUIDE_TM50J": ("CONCEPTS GUIDE",                   "TM-50J"),
    "CONCEPTS_GUIDE_TM50K": ("CONCEPTS GUIDE",                   "TM-50K"),
    "CONCEPTS_GUIDE_TM50L": ("CONCEPTS GUIDE",                   "TM-50L"),
    "SYLLABUS_TM10":     ("COURSE SYLLABUS",                     "TM-10"),
    "SYLLABUS_TM20":     ("COURSE SYLLABUS",                     "TM-20"),
    "SYLLABUS_TM30":     ("COURSE SYLLABUS",                     "TM-30"),
    "SYLLABUS_TM40G":    ("COURSE SYLLABUS",                     "TM-40G"),
    "SYLLABUS_TM40H":    ("COURSE SYLLABUS",                     "TM-40H"),
    "SYLLABUS_TM40I":    ("COURSE SYLLABUS",                     "TM-40I"),
    "SYLLABUS_TM40J":    ("COURSE SYLLABUS",                     "TM-40J"),
    "SYLLABUS_TM40K":    ("COURSE SYLLABUS",                     "TM-40K"),
    "SYLLABUS_TM40L":    ("COURSE SYLLABUS",                     "TM-40L"),
    "SYLLABUS_TM50G":    ("COURSE SYLLABUS",                     "TM-50G"),
    "SYLLABUS_TM50H":    ("COURSE SYLLABUS",                     "TM-50H"),
    "SYLLABUS_TM50I":    ("COURSE SYLLABUS",                     "TM-50I"),
    "SYLLABUS_TM50J":    ("COURSE SYLLABUS",                     "TM-50J"),
    "SYLLABUS_TM50K":    ("COURSE SYLLABUS",                     "TM-50K"),
    "SYLLABUS_TM50L":    ("COURSE SYLLABUS",                     "TM-50L"),
    "EX_50G":            ("PRACTICAL EXERCISE",                  "EX-50G"),
    "EX_50H":            ("PRACTICAL EXERCISE",                  "EX-50H"),
    "EX_50I":            ("PRACTICAL EXERCISE",                  "EX-50I"),
    "EX_50J":            ("PRACTICAL EXERCISE",                  "EX-50J"),
    "EX_50K":            ("PRACTICAL EXERCISE",                  "EX-50K"),
    "EX_50L":            ("PRACTICAL EXERCISE",                  "EX-50L"),
    "SELF_STUDY_TM30":   ("SELF-STUDY ADDENDUM",                 "TM-30"),
    "SELF_STUDY_TM40G":  ("SELF-STUDY ADDENDUM",                 "TM-40G"),
    "SELF_STUDY_TM40H":  ("SELF-STUDY ADDENDUM",                 "TM-40H"),
    "SELF_STUDY_TM40I":  ("SELF-STUDY ADDENDUM",                 "TM-40I"),
    "SELF_STUDY_TM40J":  ("SELF-STUDY ADDENDUM",                 "TM-40J"),
    "SELF_STUDY_TM40K":  ("SELF-STUDY ADDENDUM",                 "TM-40K"),
    "SELF_STUDY_TM40L":  ("SELF-STUDY ADDENDUM",                 "TM-40L"),
    "SELF_STUDY_TM50G":  ("SELF-STUDY ADDENDUM",                 "TM-50G"),
    "SELF_STUDY_TM50H":  ("SELF-STUDY ADDENDUM",                 "TM-50H"),
    "SELF_STUDY_TM50I":  ("SELF-STUDY ADDENDUM",                 "TM-50I"),
    "SELF_STUDY_TM50J":  ("SELF-STUDY ADDENDUM",                 "TM-50J"),
    "SELF_STUDY_TM50K":  ("SELF-STUDY ADDENDUM",                 "TM-50K"),
    "SELF_STUDY_TM50L":  ("SELF-STUDY ADDENDUM",                 "TM-50L"),
    "CHEAT":             ("QUICK REFERENCE CARD",                "MSS-QRC"),
    "README":            ("CURRICULUM INDEX",                    "MSS-IDX"),
    "QUICK_START":       ("QUICK START GUIDE",                   "MSS-QS"),
    "AAR_TEMPLATE":      ("AFTER-ACTION REVIEW TEMPLATE",        "AAR-MSS"),
    "CURRICULUM_MAINT":  ("STANDARD OPERATING PROCEDURE",        "SOP-MAINT"),
    # ── Architecture reference docs (ARCH_ prefix) ────────────────────────────
    "ARCH_CDA":          ("ARCHITECTURE REFERENCE",              "ODT-CDA"),
    "ARCH_GDAP":         ("ARCHITECTURE REFERENCE",              "ODT-GDAP"),
    "ARCH_MIM":          ("ARCHITECTURE REFERENCE",              "ODT-MIM"),
    "ARCH_EA":           ("ARCHITECTURE REFERENCE",              "ODT-EA"),
    "ARCH_ONTOLOGY":     ("ARCHITECTURE REFERENCE",              "ODT-ONT"),
    # ── Management / planning docs (MGMT_ prefix) ─────────────────────────────
    "MGMT_CG":           ("SENIOR LEADER GUIDANCE",              "ODT-CG"),
    "MGMT_ENTERPRISE":   ("ENTERPRISE PLAN",                     "ODT-ENT"),
    # ── Quick reference cards (REF_ prefix) ───────────────────────────────────
    "REF_":              ("QUICK REFERENCE",                     "ODT-REF"),
    "EX_10":             ("PRACTICAL EXERCISE",                  "EX-10"),
    "EX_20":             ("PRACTICAL EXERCISE",                  "EX-20"),
    "EX_30":             ("PRACTICAL EXERCISE",                  "EX-30"),
    "EX_40A":            ("PRACTICAL EXERCISE",                  "EX-40A"),
    "EX_40B":            ("PRACTICAL EXERCISE",                  "EX-40B"),
    "EX_40C":            ("PRACTICAL EXERCISE",                  "EX-40C"),
    "EX_40D":            ("PRACTICAL EXERCISE",                  "EX-40D"),
    "EX_40E":            ("PRACTICAL EXERCISE",                  "EX-40E"),
    "EX_40F":            ("PRACTICAL EXERCISE",                  "EX-40F"),
    "EX_40G":            ("PRACTICAL EXERCISE",                  "EX-40G"),
    "EX_40H":            ("PRACTICAL EXERCISE",                  "EX-40H"),
    "EX_40I":            ("PRACTICAL EXERCISE",                  "EX-40I"),
    "EX_40J":            ("PRACTICAL EXERCISE",                  "EX-40J"),
    "EX_40K":            ("PRACTICAL EXERCISE",                  "EX-40K"),
    "EX_40L":            ("PRACTICAL EXERCISE",                  "EX-40L"),
    "SYLLABUS_TM40A":    ("COURSE SYLLABUS",                     "TM-40A"),
    "SYLLABUS_TM40B":    ("COURSE SYLLABUS",                     "TM-40B"),
    "SYLLABUS_TM40C":    ("COURSE SYLLABUS",                     "TM-40C"),
    "SYLLABUS_TM40D":    ("COURSE SYLLABUS",                     "TM-40D"),
    "SYLLABUS_TM40E":    ("COURSE SYLLABUS",                     "TM-40E"),
    "SYLLABUS_TM40F":    ("COURSE SYLLABUS",                     "TM-40F"),
}

def get_pub_meta(stem: str):
    upper = stem.upper()
    for key, val in PUB_TYPES.items():
        if upper.startswith(key):
            return val
    return ("PUBLICATION", stem.replace("_", "-"))


# ── CDP header / footer templates ─────────────────────────────────────────────
# These are rendered by Chrome in the margin area on every page.
# Only inline styles work; the special <span class="X"> elements are replaced
# by Chrome with live values. Font size set on the outer div overrides the
# default 10px. Margin area height is controlled by marginTop/marginBottom
# passed to Page.printToPDF.

DRAFT_BAR_BG   = "#7A3800"
DRAFT_BAR_TEXT = "#FFD080"
FOOTER_BG      = "#071628"
FOOTER_TEXT    = "#8899BB"
GOLD_RULE      = "#C8971A"

def make_header(pub_number: str) -> str:
    # Outer div fills the full margin band; inner bar is absolutely pinned to
    # the top edge, leaving white space between bar bottom and content start.
    return (
        '<div style="position:relative;width:100%;height:100%;">'
        '<div style="'
        'position:absolute;top:0;left:0;right:0;height:32px;'
        f'background:{DRAFT_BAR_BG};'
        'display:flex;align-items:center;justify-content:space-between;'
        'padding:0 36px;'
        '-webkit-print-color-adjust:exact;color-adjust:exact;'
        'font-family:Arial,sans-serif;font-size:9px;font-weight:bold;'
        f'letter-spacing:0.12em;color:{DRAFT_BAR_TEXT};'
        '">'
        '<span>DRAFT — UNOFFICIAL</span>'
        f'<span>{pub_number} &nbsp;|&nbsp; USAREUR-AF OPERATIONAL DATA TEAM</span>'
        '<span>DRAFT — UNOFFICIAL</span>'
        '</div>'
        '</div>'
    )

FOOTER_TEMPLATE = (
    # Outer div fills the full margin band; inner bar is absolutely pinned to
    # the bottom edge, leaving white space between content end and bar top.
    '<div style="position:relative;width:100%;height:100%;">'
    '<div style="'
    'position:absolute;bottom:0;left:0;right:0;height:32px;'
    f'background:{FOOTER_BG};'
    f'border-top:2px solid {GOLD_RULE};'
    'display:flex;align-items:center;justify-content:space-between;'
    'padding:0 36px;'
    '-webkit-print-color-adjust:exact;color-adjust:exact;'
    'font-family:Arial,sans-serif;font-size:8px;'
    f'letter-spacing:0.04em;color:{FOOTER_TEXT};'
    '">'
    f'<span>USAREUR-AF / OPERATIONAL DATA TEAM &nbsp;|&nbsp; {PUB_DATE}</span>'
    '<span>Page <span class="pageNumber"></span> of <span class="totalPages"></span></span>'
    '</div>'
    '</div>'
)


# PAGE_CSS imported from publication_css.py (see top of file)


# ── Callout box post-processing (JS) ─────────────────────────────────────────
CALLOUT_JS = """
<script>
document.addEventListener('DOMContentLoaded', function() {
  var KW = '(WARNING|CAUTION|NOTE)';

  function makeCallout(type, bodyHtml) {
    var cls = 'callout-' + type.toLowerCase();
    return '<div class="' + cls + '">' +
           '<span class="callout-label">' + type + '</span>' +
           '<div class="callout-body">' + bodyHtml + '</div></div>';
  }

  // ── Blockquotes ────────────────────────────────────────────────
  // Handles: > **WARNING** text  or  > **WARNING:** text  or  > WARNING: text
  document.querySelectorAll('blockquote').forEach(function(bq) {
    var html = bq.innerHTML;
    var m;
    // Bold with optional colon inside or after the strong tag
    if ((m = html.match(new RegExp('^\\\\s*<p><strong>' + KW + ':?<\\/strong>:?\\\\s*', 'i')))) {
      var type = m[1].toUpperCase();
      var body = html.replace(new RegExp('^\\\\s*<p><strong>' + KW + ':?<\\/strong>:?\\\\s*', 'i'), '<p>');
      bq.outerHTML = makeCallout(type, body);
      return;
    }
    // Plain text: > WARNING: text
    if ((m = html.match(new RegExp('^\\\\s*<p>' + KW + '[:\\.]\\\\s*', 'i')))) {
      var type = m[1].toUpperCase();
      var body = html.replace(new RegExp('^\\\\s*<p>' + KW + '[:\\.]\\\\s*', 'i'), '<p>');
      bq.outerHTML = makeCallout(type, body);
    }
  });

  // ── Paragraphs ─────────────────────────────────────────────────
  document.querySelectorAll('p').forEach(function(p) {
    var html = p.innerHTML;
    var m;
    // Mode B: **WARNING** or **WARNING:** (bold, not in blockquote)
    if ((m = html.match(new RegExp('^<strong>' + KW + ':?<\\/strong>:?\\\\s*(.*)', 'is')))) {
      var type = m[1].toUpperCase();
      p.outerHTML = makeCallout(type, '<p>' + m[2] + '</p>');
      return;
    }
    // Mode A: plain "WARNING: text" or "NOTE: text" at start of paragraph
    if ((m = html.match(new RegExp('^' + KW + '[:\\.]\\\\s*(.*)', 'is')))) {
      var type = m[1].toUpperCase();
      p.outerHTML = makeCallout(type, '<p>' + m[2] + '</p>');
    }
  });
});
</script>
"""

# ── HTML template ─────────────────────────────────────────────────────────────
def build_html(body_html: str, pub_type: str, pub_number: str, title: str, subtitle: str = "") -> str:
    cover = f"""
<div class="cover">
  <div class="cover-topbar"><p>DRAFT — UNOFFICIAL — NOT FOR OPERATIONAL USE</p></div>
  <div class="cover-pub-type">{pub_type}</div>
  <div class="cover-pub-number">{pub_number}</div>
  <div class="cover-seal">
    <div class="cover-seal-star">&#9733;</div>
    <div class="cover-seal-text">USAREUR&#8209;AF</div>
  </div>
  <div class="cover-title">{title}</div>
  {"<div class='cover-subtitle'>" + subtitle + "</div>" if subtitle else ""}
  <div class="cover-spacer"></div>
  <div class="cover-hq">{"<br>".join(HQ_LINES)}</div>
  <div class="cover-dist">{DIST_STMT}</div>
  <div class="cover-date">{PUB_DATE}</div>
  <div class="cover-bottombar"><p>DRAFT — UNOFFICIAL — NOT FOR OPERATIONAL USE</p></div>
</div>
"""
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>{pub_number} — {title}</title>
  <style>{PAGE_CSS}</style>
</head>
<body>
  {cover}
  <div class="body-content">
{body_html}
  </div>
{CALLOUT_JS}
</body>
</html>"""


# ── Metadata extraction ───────────────────────────────────────────────────────
def extract_title(md_text: str):
    title = subtitle = ""
    for line in md_text.splitlines():
        line = line.strip()
        if line.startswith("# ") and not title:
            title = line.lstrip("# ").strip()
        elif line.startswith("## ") and title and not subtitle:
            subtitle = line.lstrip("# ").strip()
            break
    return title or "PUBLICATION", subtitle


def md_to_body_html(md_path: Path):
    text = md_path.read_text(encoding="utf-8")
    title, subtitle = extract_title(text)

    # Convert GFM task list syntax — Python markdown lib doesn't support it natively.
    # Replace before conversion so the symbols render cleanly in the PDF.
    text = re.sub(r'^(\s*)-\s+\[x\]\s+', r'\1- ☑ ', text, flags=re.MULTILINE | re.IGNORECASE)
    text = re.sub(r'^(\s*)-\s+\[ \]\s+', r'\1- ☐ ', text, flags=re.MULTILINE)

    # Merge paired chapter headings: consecutive H1s where the first is a bare chapter number
    # e.g.  "# CHAPTER 1\n# FOUNDATIONS OF DATA LITERACY"
    # → "# CHAPTER 1 — FOUNDATIONS OF DATA LITERACY"
    text = re.sub(
        r'^(# CHAPTER \d+)\s*\n(# )(.+)',
        lambda m: f'{m.group(1)} — {m.group(3)}',
        text,
        flags=re.MULTILINE,
    )

    body = markdown.markdown(
        text,
        extensions=["tables", "fenced_code", "toc", "attr_list"],
    )
    return body, title, subtitle


# CDP functions are in scripts/chrome_cdp.py — html_file_to_pdf imported at top


# ── Conversion helpers ────────────────────────────────────────────────────────
def convert_md(src_rel: str, out_stem: str) -> bool:
    src = REPO_ROOT / src_rel
    if not src.exists():
        print(f"  SKIP  {src_rel}")
        return False
    pub_type, pub_number = get_pub_meta(out_stem)
    body_html, title, subtitle = md_to_body_html(src)
    full_html = build_html(body_html, pub_type, pub_number, title, subtitle)
    with tempfile.NamedTemporaryFile(
        suffix=".html", mode="w", encoding="utf-8", delete=False
    ) as tmp:
        tmp.write(full_html)
        tmp_path = Path(tmp.name)
    pdf_path = OUT_DIR / f"{out_stem}.pdf"
    ok = html_file_to_pdf(tmp_path, pdf_path, make_header(pub_number), FOOTER_TEMPLATE, CHROME)
    tmp_path.unlink(missing_ok=True)
    print(f"  {'OK  ' if ok else 'FAIL'} {out_stem}.pdf")
    return ok


def convert_html_direct(src_rel: str, out_stem: str, pub_number: str = "MSS-HUB") -> bool:
    src = REPO_ROOT / src_rel
    if not src.exists():
        print(f"  SKIP  {src_rel}")
        return False
    pdf_path = OUT_DIR / f"{out_stem}.pdf"
    ok = html_file_to_pdf(src, pdf_path, make_header(pub_number), FOOTER_TEMPLATE, CHROME)
    print(f"  {'OK  ' if ok else 'FAIL'} {out_stem}.pdf")
    return ok


# ── Target list ───────────────────────────────────────────────────────────────
MD_TARGETS = [
    # ── Index & quick start ───────────────────────────────────────────────────
    ("maven_training/README.md",                                                        "00_README"),
    ("maven_training/QUICK_START.md",                                                   "QUICK_START"),
    # ── Index & doctrine ─────────────────────────────────────────────────────
    ("maven_training/doctrine/DATA_LITERACY_senior_leaders.md",                        "DATA_LITERACY_senior_leaders"),
    ("maven_training/doctrine/DATA_LITERACY_technical_reference.md",                   "DATA_LITERACY_technical_reference"),
    ("maven_training/doctrine/GLOSSARY_data_foundry.md",                               "GLOSSARY_data_foundry"),
    ("maven_training/standards/NAMING_AND_GOVERNANCE_STANDARDS.md",                    "NAMING_AND_GOVERNANCE_STANDARDS"),
    ("maven_training/quick_reference/cheatsheet.md",                                   "CHEATSHEET"),
    # ── Training management ───────────────────────────────────────────────────
    ("maven_training/training_management/MTP_MSS.md",                                  "MTP_MSS"),
    ("maven_training/training_management/POI_MSS.md",                                  "POI_MSS"),
    ("maven_training/training_management/TEO_MSS.md",                                  "TEO_MSS"),
    ("maven_training/training_management/CAD_MSS.md",                                  "CAD_MSS"),
    ("maven_training/training_management/POLICY_LETTER.md",                            "POLICY_LETTER"),
    ("maven_training/training_management/ENROLLMENT_SOP.md",                           "ENROLLMENT_SOP"),
    ("maven_training/training_management/ANNUAL_TRAINING_SCHEDULE.md",                 "ANNUAL_TRAINING_SCHEDULE"),
    ("maven_training/training_management/FACULTY_DEVELOPMENT_PLAN.md",                 "FACULTY_DEVELOPMENT_PLAN"),
    ("maven_training/training_management/COMPLETION_CERTIFICATE.md",                   "COMPLETION_CERTIFICATE"),
    ("maven_training/training_management/AAR_TEMPLATE.md",                             "AAR_TEMPLATE"),
    ("maven_training/training_management/CURRICULUM_MAINTENANCE_SOP.md",               "CURRICULUM_MAINTENANCE_SOP"),
    # ── Lesson plans ──────────────────────────────────────────────────────────
    ("maven_training/training_management/lesson_plans/LP_TEMPLATE.md",                 "LP_TEMPLATE"),
    ("maven_training/training_management/lesson_plans/TM10/TM10_LESSON_PLANS.md",      "TM10_LESSON_PLANS"),
    ("maven_training/training_management/lesson_plans/TM20_LESSON_PLAN_OUTLINES.md",   "TM20_LESSON_PLAN_OUTLINES"),
    ("maven_training/training_management/lesson_plans/TM30_LESSON_PLAN_OUTLINES.md",   "TM30_LESSON_PLAN_OUTLINES"),
    ("maven_training/training_management/lesson_plans/TM40_SPECIALIST_LESSON_PLAN_OUTLINES.md", "TM40_SPECIALIST_LESSON_PLAN_OUTLINES"),
    # ── Syllabi ───────────────────────────────────────────────────────────────
    ("maven_training/syllabi/SYLLABUS_TM10.md",                                        "SYLLABUS_TM10"),
    ("maven_training/syllabi/SYLLABUS_TM20.md",                                        "SYLLABUS_TM20"),
    ("maven_training/syllabi/SYLLABUS_TM30.md",                                        "SYLLABUS_TM30"),
    # WFF syllabi (A–F)
    ("maven_training/syllabi/SYLLABUS_TM40A.md",                                       "SYLLABUS_TM40A"),
    ("maven_training/syllabi/SYLLABUS_TM40B.md",                                       "SYLLABUS_TM40B"),
    ("maven_training/syllabi/SYLLABUS_TM40C.md",                                       "SYLLABUS_TM40C"),
    ("maven_training/syllabi/SYLLABUS_TM40D.md",                                       "SYLLABUS_TM40D"),
    ("maven_training/syllabi/SYLLABUS_TM40E.md",                                       "SYLLABUS_TM40E"),
    ("maven_training/syllabi/SYLLABUS_TM40F.md",                                       "SYLLABUS_TM40F"),
    ("maven_training/syllabi/SYLLABUS_TM40G.md",                                       "SYLLABUS_TM40G"),
    ("maven_training/syllabi/SYLLABUS_TM40H.md",                                       "SYLLABUS_TM40H"),
    ("maven_training/syllabi/SYLLABUS_TM40I.md",                                       "SYLLABUS_TM40I"),
    ("maven_training/syllabi/SYLLABUS_TM40J.md",                                       "SYLLABUS_TM40J"),
    ("maven_training/syllabi/SYLLABUS_TM40K.md",                                       "SYLLABUS_TM40K"),
    ("maven_training/syllabi/SYLLABUS_TM40L.md",                                       "SYLLABUS_TM40L"),
    # TM-50 syllabi
    ("maven_training/syllabi/SYLLABUS_TM50G.md",                                       "SYLLABUS_TM50G"),
    ("maven_training/syllabi/SYLLABUS_TM50H.md",                                       "SYLLABUS_TM50H"),
    ("maven_training/syllabi/SYLLABUS_TM50I.md",                                       "SYLLABUS_TM50I"),
    ("maven_training/syllabi/SYLLABUS_TM50J.md",                                       "SYLLABUS_TM50J"),
    ("maven_training/syllabi/SYLLABUS_TM50K.md",                                       "SYLLABUS_TM50K"),
    ("maven_training/syllabi/SYLLABUS_TM50L.md",                                       "SYLLABUS_TM50L"),
    # ── Practical exercises ───────────────────────────────────────────────────
    ("maven_training/exercises/EX-10_operator_basics/EXERCISE.md",                     "EX_10_OPERATOR_BASICS"),
    ("maven_training/exercises/EX-20_no_code_builder/EXERCISE.md",                     "EX_20_NO_CODE_BUILDER"),
    ("maven_training/exercises/EX-30_advanced_builder/EXERCISE.md",                    "EX_30_ADVANCED_BUILDER"),
    # WFF exercises (A–F)
    ("maven_training/exercises/EX-40A_intelligence/EXERCISE.md",                       "EX_40A_INTELLIGENCE"),
    ("maven_training/exercises/EX-40B_fires/EXERCISE.md",                              "EX_40B_FIRES"),
    ("maven_training/exercises/EX-40C_movement_maneuver/EXERCISE.md",                  "EX_40C_MOVEMENT_MANEUVER"),
    ("maven_training/exercises/EX-40D_sustainment/EXERCISE.md",                        "EX_40D_SUSTAINMENT"),
    ("maven_training/exercises/EX-40E_protection/EXERCISE.md",                         "EX_40E_PROTECTION"),
    ("maven_training/exercises/EX-40F_mission_command/EXERCISE.md",                    "EX_40F_MISSION_COMMAND"),
    ("maven_training/exercises/EX-40G_orsa/EXERCISE.md",                               "EX_40G_ORSA"),
    ("maven_training/exercises/EX-40H_ai_engineer/EXERCISE.md",                        "EX_40H_AI_ENGINEER"),
    ("maven_training/exercises/EX-40I_ml_engineer/EXERCISE.md",                        "EX_40I_ML_ENGINEER"),
    ("maven_training/exercises/EX-40J_program_manager/EXERCISE.md",                    "EX_40J_PROGRAM_MANAGER"),
    ("maven_training/exercises/EX-40K_knowledge_manager/EXERCISE.md",                  "EX_40K_KNOWLEDGE_MANAGER"),
    ("maven_training/exercises/EX-40L_software_engineer/EXERCISE.md",                  "EX_40L_SOFTWARE_ENGINEER"),
    # TM-50 exercises
    ("maven_training/exercises/EX-50G_orsa/EXERCISE.md",                               "EX_50G_ORSA"),
    ("maven_training/exercises/EX-50H_ai_engineer/EXERCISE.md",                        "EX_50H_AI_ENGINEER"),
    ("maven_training/exercises/EX-50I_ml_engineer/EXERCISE.md",                        "EX_50I_ML_ENGINEER"),
    ("maven_training/exercises/EX-50J_program_manager/EXERCISE.md",                    "EX_50J_PROGRAM_MANAGER"),
    ("maven_training/exercises/EX-50K_knowledge_manager/EXERCISE.md",                  "EX_50K_KNOWLEDGE_MANAGER"),
    ("maven_training/exercises/EX-50L_software_engineer/EXERCISE.md",                  "EX_50L_SOFTWARE_ENGINEER"),
    # ── Assessments (pre/post exams) ──────────────────────────────────────────
    ("maven_training/exercises/exams/EXAM_TM10_PRE.md",                                "EXAM_TM10_PRE"),
    ("maven_training/exercises/exams/EXAM_TM10_POST.md",                               "EXAM_TM10_POST"),
    ("maven_training/exercises/exams/EXAM_TM20_PRE.md",                                "EXAM_TM20_PRE"),
    ("maven_training/exercises/exams/EXAM_TM20_POST.md",                               "EXAM_TM20_POST"),
    ("maven_training/exercises/exams/EXAM_TM30_PRE.md",                                "EXAM_TM30_PRE"),
    ("maven_training/exercises/exams/EXAM_TM30_POST.md",                               "EXAM_TM30_POST"),
    # WFF exams (A–F)
    ("maven_training/exercises/exams/EXAM_TM40A_PRE.md",                               "EXAM_TM40A_PRE"),
    ("maven_training/exercises/exams/EXAM_TM40A_POST.md",                              "EXAM_TM40A_POST"),
    ("maven_training/exercises/exams/EXAM_TM40B_PRE.md",                               "EXAM_TM40B_PRE"),
    ("maven_training/exercises/exams/EXAM_TM40B_POST.md",                              "EXAM_TM40B_POST"),
    ("maven_training/exercises/exams/EXAM_TM40C_PRE.md",                               "EXAM_TM40C_PRE"),
    ("maven_training/exercises/exams/EXAM_TM40C_POST.md",                              "EXAM_TM40C_POST"),
    ("maven_training/exercises/exams/EXAM_TM40D_PRE.md",                               "EXAM_TM40D_PRE"),
    ("maven_training/exercises/exams/EXAM_TM40D_POST.md",                              "EXAM_TM40D_POST"),
    ("maven_training/exercises/exams/EXAM_TM40E_PRE.md",                               "EXAM_TM40E_PRE"),
    ("maven_training/exercises/exams/EXAM_TM40E_POST.md",                              "EXAM_TM40E_POST"),
    ("maven_training/exercises/exams/EXAM_TM40F_PRE.md",                               "EXAM_TM40F_PRE"),
    ("maven_training/exercises/exams/EXAM_TM40F_POST.md",                              "EXAM_TM40F_POST"),
    ("maven_training/exercises/exams/EXAM_TM40G_PRE.md",                               "EXAM_TM40G_PRE"),
    ("maven_training/exercises/exams/EXAM_TM40G_POST.md",                              "EXAM_TM40G_POST"),
    ("maven_training/exercises/exams/EXAM_TM40H_PRE.md",                               "EXAM_TM40H_PRE"),
    ("maven_training/exercises/exams/EXAM_TM40H_POST.md",                              "EXAM_TM40H_POST"),
    ("maven_training/exercises/exams/EXAM_TM40I_PRE.md",                               "EXAM_TM40I_PRE"),
    ("maven_training/exercises/exams/EXAM_TM40I_POST.md",                              "EXAM_TM40I_POST"),
    ("maven_training/exercises/exams/EXAM_TM40J_PRE.md",                               "EXAM_TM40J_PRE"),
    ("maven_training/exercises/exams/EXAM_TM40J_POST.md",                              "EXAM_TM40J_POST"),
    ("maven_training/exercises/exams/EXAM_TM40K_PRE.md",                               "EXAM_TM40K_PRE"),
    ("maven_training/exercises/exams/EXAM_TM40K_POST.md",                              "EXAM_TM40K_POST"),
    ("maven_training/exercises/exams/EXAM_TM40L_PRE.md",                               "EXAM_TM40L_PRE"),
    ("maven_training/exercises/exams/EXAM_TM40L_POST.md",                              "EXAM_TM40L_POST"),
    ("maven_training/exercises/exams/EXAM_TM50G_PRE.md",                               "EXAM_TM50G_PRE"),
    ("maven_training/exercises/exams/EXAM_TM50G_POST.md",                              "EXAM_TM50G_POST"),
    ("maven_training/exercises/exams/EXAM_TM50H_PRE.md",                               "EXAM_TM50H_PRE"),
    ("maven_training/exercises/exams/EXAM_TM50H_POST.md",                              "EXAM_TM50H_POST"),
    ("maven_training/exercises/exams/EXAM_TM50I_PRE.md",                               "EXAM_TM50I_PRE"),
    ("maven_training/exercises/exams/EXAM_TM50I_POST.md",                              "EXAM_TM50I_POST"),
    ("maven_training/exercises/exams/EXAM_TM50J_PRE.md",                               "EXAM_TM50J_PRE"),
    ("maven_training/exercises/exams/EXAM_TM50J_POST.md",                              "EXAM_TM50J_POST"),
    ("maven_training/exercises/exams/EXAM_TM50K_PRE.md",                               "EXAM_TM50K_PRE"),
    ("maven_training/exercises/exams/EXAM_TM50K_POST.md",                              "EXAM_TM50K_POST"),
    ("maven_training/exercises/exams/EXAM_TM50L_PRE.md",                               "EXAM_TM50L_PRE"),
    ("maven_training/exercises/exams/EXAM_TM50L_POST.md",                              "EXAM_TM50L_POST"),
    # ── Technical manuals ─────────────────────────────────────────────────────
    ("maven_training/tm/TM_10_maven_user/TM_10_MAVEN_USER.md",                         "TM_10_MAVEN_USER"),
    ("maven_training/tm/TM_20_builder/TM_20_BUILDER.md",                               "TM_20_BUILDER"),
    ("maven_training/tm/TM_30_advanced_builder/TM_30_ADVANCED_BUILDER.md",             "TM_30_ADVANCED_BUILDER"),
    # WFF tracks (A–F, operational)
    ("maven_training/tm/TM_40A_intelligence/TM_40A_INTELLIGENCE.md",                   "TM_40A_INTELLIGENCE"),
    ("maven_training/tm/TM_40A_intelligence/CONCEPTS_GUIDE_TM40A_INTELLIGENCE.md",     "CONCEPTS_GUIDE_TM40A_INTELLIGENCE"),
    ("maven_training/tm/TM_40B_fires/TM_40B_FIRES.md",                                 "TM_40B_FIRES"),
    ("maven_training/tm/TM_40B_fires/CONCEPTS_GUIDE_TM40B_FIRES.md",                   "CONCEPTS_GUIDE_TM40B_FIRES"),
    ("maven_training/tm/TM_40C_movement_maneuver/TM_40C_MOVEMENT_MANEUVER.md",         "TM_40C_MOVEMENT_MANEUVER"),
    ("maven_training/tm/TM_40C_movement_maneuver/CONCEPTS_GUIDE_TM40C_MOVEMENT_MANEUVER.md","CONCEPTS_GUIDE_TM40C_MOVEMENT_MANEUVER"),
    ("maven_training/tm/TM_40D_sustainment/TM_40D_SUSTAINMENT.md",                     "TM_40D_SUSTAINMENT"),
    ("maven_training/tm/TM_40D_sustainment/CONCEPTS_GUIDE_TM40D_SUSTAINMENT.md",       "CONCEPTS_GUIDE_TM40D_SUSTAINMENT"),
    ("maven_training/tm/TM_40E_protection/TM_40E_PROTECTION.md",                       "TM_40E_PROTECTION"),
    ("maven_training/tm/TM_40E_protection/CONCEPTS_GUIDE_TM40E_PROTECTION.md",         "CONCEPTS_GUIDE_TM40E_PROTECTION"),
    ("maven_training/tm/TM_40F_mission_command/TM_40F_MISSION_COMMAND.md",             "TM_40F_MISSION_COMMAND"),
    ("maven_training/tm/TM_40F_mission_command/CONCEPTS_GUIDE_TM40F_MISSION_COMMAND.md","CONCEPTS_GUIDE_TM40F_MISSION_COMMAND"),
    # Technical specialist tracks (G–L)
    ("maven_training/tm/TM_40G_orsa/TM_40G_ORSA.md",                                   "TM_40G_ORSA"),
    ("maven_training/tm/TM_40G_orsa/CONCEPTS_GUIDE_TM40G_ORSA.md",                     "CONCEPTS_GUIDE_TM40G_ORSA"),
    ("maven_training/tm/TM_40H_ai_engineer/TM_40H_AI_ENGINEER.md",                     "TM_40H_AI_ENGINEER"),
    ("maven_training/tm/TM_40H_ai_engineer/CONCEPTS_GUIDE_TM40H_AI_ENGINEER.md",       "CONCEPTS_GUIDE_TM40H_AI_ENGINEER"),
    ("maven_training/tm/TM_40I_ml_engineer/TM_40I_ML_ENGINEER.md",                     "TM_40I_ML_ENGINEER"),
    ("maven_training/tm/TM_40I_ml_engineer/CONCEPTS_GUIDE_TM40I_ML_ENGINEER.md",       "CONCEPTS_GUIDE_TM40I_ML_ENGINEER"),
    ("maven_training/tm/TM_40J_program_manager/TM_40J_PROGRAM_MANAGER.md",             "TM_40J_PROGRAM_MANAGER"),
    ("maven_training/tm/TM_40J_program_manager/CONCEPTS_GUIDE_TM40J_PROGRAM_MANAGER.md","CONCEPTS_GUIDE_TM40J_PROGRAM_MANAGER"),
    ("maven_training/tm/TM_40K_knowledge_manager/TM_40K_KNOWLEDGE_MANAGER.md",         "TM_40K_KNOWLEDGE_MANAGER"),
    ("maven_training/tm/TM_40K_knowledge_manager/CONCEPTS_GUIDE_TM40K_KNOWLEDGE_MANAGER.md","CONCEPTS_GUIDE_TM40K_KNOWLEDGE_MANAGER"),
    ("maven_training/tm/TM_40L_software_engineer/TM_40L_SOFTWARE_ENGINEER.md",         "TM_40L_SOFTWARE_ENGINEER"),
    ("maven_training/tm/TM_40L_software_engineer/CONCEPTS_GUIDE_TM40L_SOFTWARE_ENGINEER.md","CONCEPTS_GUIDE_TM40L_SOFTWARE_ENGINEER"),
    # Technical specialist advanced tracks (50G–L)
    ("maven_training/tm/TM_50G_orsa_advanced/TM_50G_ORSA_ADVANCED.md",                 "TM_50G_ORSA_ADVANCED"),
    ("maven_training/tm/TM_50G_orsa_advanced/CONCEPTS_GUIDE_TM50G_ORSA_ADVANCED.md",   "CONCEPTS_GUIDE_TM50G_ORSA_ADVANCED"),
    ("maven_training/tm/TM_50H_ai_engineer_advanced/TM_50H_AI_ENGINEER_ADVANCED.md",   "TM_50H_AI_ENGINEER_ADVANCED"),
    ("maven_training/tm/TM_50H_ai_engineer_advanced/CONCEPTS_GUIDE_TM50H_AI_ENGINEER_ADVANCED.md","CONCEPTS_GUIDE_TM50H_AI_ENGINEER_ADVANCED"),
    ("maven_training/tm/TM_50I_ml_engineer_advanced/TM_50I_ML_ENGINEER_ADVANCED.md",   "TM_50I_ML_ENGINEER_ADVANCED"),
    ("maven_training/tm/TM_50I_ml_engineer_advanced/CONCEPTS_GUIDE_TM50I_ML_ENGINEER_ADVANCED.md","CONCEPTS_GUIDE_TM50I_ML_ENGINEER_ADVANCED"),
    ("maven_training/tm/TM_50J_program_manager_advanced/TM_50J_PROGRAM_MANAGER_ADVANCED.md","TM_50J_PROGRAM_MANAGER_ADVANCED"),
    ("maven_training/tm/TM_50J_program_manager_advanced/CONCEPTS_GUIDE_TM50J_PROGRAM_MANAGER_ADVANCED.md","CONCEPTS_GUIDE_TM50J_PROGRAM_MANAGER_ADVANCED"),
    ("maven_training/tm/TM_50K_knowledge_manager_advanced/TM_50K_KNOWLEDGE_MANAGER_ADVANCED.md","TM_50K_KNOWLEDGE_MANAGER_ADVANCED"),
    ("maven_training/tm/TM_50K_knowledge_manager_advanced/CONCEPTS_GUIDE_TM50K_KNOWLEDGE_MANAGER_ADVANCED.md","CONCEPTS_GUIDE_TM50K_KNOWLEDGE_MANAGER_ADVANCED"),
    ("maven_training/tm/TM_50L_software_engineer_advanced/TM_50L_SOFTWARE_ENGINEER_ADVANCED.md","TM_50L_SOFTWARE_ENGINEER_ADVANCED"),
    ("maven_training/tm/TM_50L_software_engineer_advanced/CONCEPTS_GUIDE_TM50L_SOFTWARE_ENGINEER_ADVANCED.md","CONCEPTS_GUIDE_TM50L_SOFTWARE_ENGINEER_ADVANCED"),
    # ── Self-study addenda (Palantir Developers reference library) ────────────
    ("maven_training/tm/TM_30_advanced_builder/SELF_STUDY_ADDENDUM.md",                "SELF_STUDY_TM30_ADVANCED_BUILDER"),
    ("maven_training/tm/TM_40G_orsa/SELF_STUDY_ADDENDUM.md",                          "SELF_STUDY_TM40G_ORSA"),
    ("maven_training/tm/TM_40H_ai_engineer/SELF_STUDY_ADDENDUM.md",                   "SELF_STUDY_TM40H_AI_ENGINEER"),
    ("maven_training/tm/TM_40I_ml_engineer/SELF_STUDY_ADDENDUM.md",                   "SELF_STUDY_TM40I_ML_ENGINEER"),
    ("maven_training/tm/TM_40J_program_manager/SELF_STUDY_ADDENDUM.md",               "SELF_STUDY_TM40J_PROGRAM_MANAGER"),
    ("maven_training/tm/TM_40K_knowledge_manager/SELF_STUDY_ADDENDUM.md",             "SELF_STUDY_TM40K_KNOWLEDGE_MANAGER"),
    ("maven_training/tm/TM_40L_software_engineer/SELF_STUDY_ADDENDUM.md",             "SELF_STUDY_TM40L_SOFTWARE_ENGINEER"),
    ("maven_training/tm/TM_50G_orsa_advanced/SELF_STUDY_ADDENDUM.md",                 "SELF_STUDY_TM50G_ORSA_ADVANCED"),
    ("maven_training/tm/TM_50H_ai_engineer_advanced/SELF_STUDY_ADDENDUM.md",          "SELF_STUDY_TM50H_AI_ENGINEER_ADVANCED"),
    ("maven_training/tm/TM_50I_ml_engineer_advanced/SELF_STUDY_ADDENDUM.md",          "SELF_STUDY_TM50I_ML_ENGINEER_ADVANCED"),
    ("maven_training/tm/TM_50J_program_manager_advanced/SELF_STUDY_ADDENDUM.md",      "SELF_STUDY_TM50J_PROGRAM_MANAGER_ADVANCED"),
    ("maven_training/tm/TM_50K_knowledge_manager_advanced/SELF_STUDY_ADDENDUM.md",    "SELF_STUDY_TM50K_KNOWLEDGE_MANAGER_ADVANCED"),
    ("maven_training/tm/TM_50L_software_engineer_advanced/SELF_STUDY_ADDENDUM.md",    "SELF_STUDY_TM50L_SOFTWARE_ENGINEER_ADVANCED"),
    # ── Architecture Reference — CDA Doctrine ─────────────────────────────────
    ("maven_training/doctrine/CDA_CONSTRAINTS_AND_DIRECTIVES.md",                          "ARCH_CDA_CONSTRAINTS_AND_DIRECTIVES"),
    ("maven_training/doctrine/cda_doctrine/CDA_OVERVIEW.md",                               "ARCH_CDA_OVERVIEW"),
    ("maven_training/doctrine/cda_doctrine/CDA_DOCTRINE_OVERVIEW.md",                      "ARCH_CDA_DOCTRINE_OVERVIEW"),
    ("maven_training/doctrine/cda_doctrine/CDA_DOCTRINE_AGENT.md",                         "ARCH_CDA_DOCTRINE_AGENT"),
    ("maven_training/doctrine/cda_doctrine/CDA_IDENTITY_VS_CLASSIFICATION.md",             "ARCH_CDA_IDENTITY_VS_CLASSIFICATION"),
    ("maven_training/doctrine/cda_doctrine/CDA_AVT25_ASSESSMENT.md",                       "ARCH_CDA_AVT25_ASSESSMENT"),
    ("maven_training/doctrine/cda_doctrine/agents/CDA_AGENTS_OVERVIEW.md",                 "ARCH_CDA_AGENTS_OVERVIEW"),
    ("maven_training/doctrine/cda_doctrine/agents/CDA_AGENTS_CORE_PRINCIPLES.md",          "ARCH_CDA_AGENTS_CORE_PRINCIPLES"),
    ("maven_training/doctrine/cda_doctrine/agents/CDA_AGENTS_ONTOLOGY_ENGINEER.md",        "ARCH_CDA_AGENTS_ONTOLOGY_ENGINEER"),
    ("maven_training/doctrine/cda_doctrine/agents/CDA_AGENTS_ENTITY_RESOLUTION.md",        "ARCH_CDA_AGENTS_ENTITY_RESOLUTION"),
    ("maven_training/doctrine/cda_doctrine/agents/CDA_AGENTS_INGESTION_INTEGRATION.md",    "ARCH_CDA_AGENTS_INGESTION_INTEGRATION"),
    ("maven_training/doctrine/cda_doctrine/canon/CANON_ADP_CROSSWALK.md",                  "ARCH_CDA_CANON_ADP_CROSSWALK"),
    ("maven_training/doctrine/cda_doctrine/canon/CANON_CONDITIONS_INDICATORS_THRESHOLDS.md","ARCH_CDA_CANON_CONDITIONS"),
    ("maven_training/doctrine/cda_doctrine/canon/CANON_ENGAGEMENT.md",                     "ARCH_CDA_CANON_ENGAGEMENT"),
    ("maven_training/doctrine/cda_doctrine/canon/CANON_INFORMATION.md",                    "ARCH_CDA_CANON_INFORMATION"),
    # ── Architecture Reference — GDAP ─────────────────────────────────────────
    ("maven_training/doctrine/gdap/GDAP_OVERVIEW.md",                                      "ARCH_GDAP_OVERVIEW"),
    ("maven_training/doctrine/gdap/GDAP_VISION.md",                                        "ARCH_GDAP_VISION"),
    ("maven_training/doctrine/gdap/GDAP_PERSISTENCE_STRATEGY.md",                          "ARCH_GDAP_PERSISTENCE_STRATEGY"),
    ("maven_training/doctrine/gdap/GDAP_ACCEPTANCE_TESTS.md",                              "ARCH_GDAP_ACCEPTANCE_TESTS"),
    ("maven_training/doctrine/gdap/GDAP_ADR_0001_LLAMAINDEX.md",                           "ARCH_GDAP_ADR_0001_LLAMAINDEX"),
    # ── Architecture Reference — MIM ─────────────────────────────────────────
    ("maven_training/doctrine/mim/MIM_OVERVIEW.md",                                        "ARCH_MIM_OVERVIEW"),
    ("maven_training/doctrine/mim/MIM_STANDARD.md",                                        "ARCH_MIM_STANDARD"),
    ("maven_training/doctrine/mim/MIM_STATE.md",                                           "ARCH_MIM_STATE"),
    ("maven_training/doctrine/mim/MIM_ACADEMICS.md",                                       "ARCH_MIM_ACADEMICS"),
    ("maven_training/doctrine/mim/MIM_DECISION_RECORDS.md",                                "ARCH_MIM_DECISION_RECORDS"),
    ("maven_training/doctrine/mim/MIM_FUTURE_CLASSES.md",                                  "ARCH_MIM_FUTURE_CLASSES"),
    ("maven_training/doctrine/mim/MIM_ONTOLOGY_DOCS.md",                                   "ARCH_MIM_ONTOLOGY_DOCS"),
    # ── Architecture Reference — Ontology Design ──────────────────────────────
    ("maven_training/doctrine/ONTOLOGY_DESIGN_PRINCIPLES.md",                              "ARCH_ONTOLOGY_DESIGN_PRINCIPLES"),
    # ── Architecture Reference — Enterprise Architecture ──────────────────────
    ("maven_training/doctrine/enterprise_architecture/EA_00_REFERENCE_CARD.md",            "ARCH_EA_00_REFERENCE_CARD"),
    ("maven_training/doctrine/enterprise_architecture/EA_01_FOUNDATION.md",                "ARCH_EA_01_FOUNDATION"),
    ("maven_training/doctrine/enterprise_architecture/EA_02_SCHOOLS_OF_THOUGHT.md",        "ARCH_EA_02_SCHOOLS_OF_THOUGHT"),
    ("maven_training/doctrine/enterprise_architecture/EA_03_ARTIFACTS_AND_VIEWS.md",       "ARCH_EA_03_ARTIFACTS_AND_VIEWS"),
    ("maven_training/doctrine/enterprise_architecture/EA_04_GOVERNANCE.md",                "ARCH_EA_04_GOVERNANCE"),
    ("maven_training/doctrine/enterprise_architecture/EA_05_MILITARY_APPLICATION.md",      "ARCH_EA_05_MILITARY_APPLICATION"),
    # ── Quick Reference — CDA ────────────────────────────────────────────────
    ("maven_training/quick_reference/cda_reference/DOCTRINE_ELEMENT_FOUNDRY_MAPPING.md",   "REF_DOCTRINE_ELEMENT_FOUNDRY_MAPPING"),
    ("maven_training/quick_reference/cda_reference/EA_VS_DA.md",                           "REF_EA_VS_DA"),
    ("maven_training/quick_reference/cda_reference/ENTERPRISE_DATA_COMPASS.md",            "REF_ENTERPRISE_DATA_COMPASS"),
    ("maven_training/quick_reference/cda_reference/LESSONS_LEARNED.md",                    "REF_LESSONS_LEARNED"),
    ("maven_training/quick_reference/cda_reference/PLAN_FOR_SUCCESS.md",                   "REF_PLAN_FOR_SUCCESS"),
    # ── Management / Planning ────────────────────────────────────────────────
    ("maven_training/doctrine/CG_GUIDANCE.md",                                             "MGMT_CG_GUIDANCE"),
    ("maven_training/training_management/ENTERPRISE_V10_PLAN.md",                          "MGMT_ENTERPRISE_V10_PLAN"),
    ("maven_training/training_management/ENTERPRISE_IMPLEMENTATION_PLAN.md",               "MGMT_ENTERPRISE_IMPLEMENTATION_PLAN"),
]
HTML_TARGETS = [
    ("maven_training/mss_info_app/index.html", "MSS_TRAINING_HUB"),
]


# ── Incremental build helpers ──────────────────────────────────────────────────
MANIFEST_PATH = OUT_DIR / ".manifest.json"


def _file_hash(path: Path) -> str:
    """Return the SHA-256 hex digest of a file's contents."""
    h = hashlib.sha256()
    h.update(path.read_bytes())
    return h.hexdigest()


def _load_manifest() -> dict:
    """Load the source-file hash manifest; return empty dict if missing."""
    if MANIFEST_PATH.exists():
        try:
            return json.loads(MANIFEST_PATH.read_text())
        except Exception:
            return {}
    return {}


def _save_manifest(manifest: dict):
    """Persist the manifest and write a human-readable SHA-256 sidecar."""
    MANIFEST_PATH.write_text(json.dumps(manifest, indent=2))
    # Also write a plain-text manifest for external verification
    sha_path = OUT_DIR / "pdf_manifest.sha256"
    lines = []
    for pdf_path in sorted(OUT_DIR.glob("*.pdf")):
        lines.append(f"{_file_hash(pdf_path)}  {pdf_path.name}")
    sha_path.write_text("\n".join(lines) + "\n")


def _should_rebuild(src: Path, stem: str, manifest: dict) -> bool:
    """Return True if the source has changed since the last successful build."""
    if not src.exists():
        return False                        # source missing — will SKIP
    if not (OUT_DIR / f"{stem}.pdf").exists():
        return True                         # PDF missing — always build
    current_hash = _file_hash(src)
    return manifest.get(str(src)) != current_hash


# ── Main ──────────────────────────────────────────────────────────────────────
def main():
    import argparse
    parser = argparse.ArgumentParser(description="Build USAREUR-AF Maven PDFs")
    parser.add_argument("--workers", type=int, default=4,
                        help="Parallel Chrome workers (default: 4)")
    parser.add_argument("--force", action="store_true",
                        help="Rebuild all PDFs even if source is unchanged")
    args = parser.parse_args()

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    manifest = {} if args.force else _load_manifest()
    print(f"Output: {OUT_DIR}  workers={args.workers}  force={args.force}\n")

    # Collect all build tasks: (callable, src_path, stem)
    tasks = []
    for rel, stem in MD_TARGETS:
        src = REPO_ROOT / rel
        if not src.exists():
            print(f"  SKIP  {rel}")
            continue
        if not args.force and not _should_rebuild(src, stem, manifest):
            print(f"  --    {stem}.pdf  (unchanged)")
            continue
        tasks.append((convert_md, rel, stem))
    for rel, stem in HTML_TARGETS:
        src = REPO_ROOT / rel
        if not src.exists():
            print(f"  SKIP  {rel}")
            continue
        if not args.force and not _should_rebuild(src, stem, manifest):
            print(f"  --    {stem}.pdf  (unchanged)")
            continue
        tasks.append((convert_html_direct, rel, stem))

    if not tasks:
        print("Nothing to rebuild — all PDFs are up to date.")
        _save_manifest(manifest)
        return

    print(f"Building {len(tasks)} PDFs with {args.workers} parallel worker(s)...\n")
    ok = fail = 0
    updated_manifest = dict(manifest)

    # Run builds in parallel; Chrome spawns per-task so workers are independent
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = {
            pool.submit(fn, rel, stem): (rel, stem)
            for fn, rel, stem in tasks
        }
        for future in as_completed(futures):
            rel, stem = futures[future]
            try:
                success = future.result()
            except Exception as exc:
                print(f"  FAIL  {stem}.pdf  ({exc})")
                success = False
            if success:
                ok += 1
                src = REPO_ROOT / rel
                if src.exists():
                    updated_manifest[str(src)] = _file_hash(src)
            else:
                fail += 1

    _save_manifest(updated_manifest)
    print(f"\nDone: {ok} built, {fail} failed.")
    if fail:
        sys.exit(1)


if __name__ == "__main__":
    main()
