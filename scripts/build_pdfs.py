#!/usr/bin/env python3
"""
build_pdfs.py — Convert maven_training markdown files to Army doctrine-style PDFs.

Toolchain: Python `markdown` → styled HTML → Chrome CDP Page.printToPDF
           (CDP used instead of --print-to-pdf CLI flag so we get real
            header/footer templates that land in the margin area on every page.)
Output: maven_training/pdf/
"""

import base64
import json
import os
import re
import socket
import subprocess
import sys
import tempfile
import time
import urllib.request

import markdown
import websocket
from pathlib import Path

# ── Config ────────────────────────────────────────────────────────────────────
REPO_ROOT = Path(__file__).parent.parent
OUT_DIR   = REPO_ROOT / "maven_training" / "pdf"
CHROME    = "google-chrome"
PUB_DATE  = "11 MARCH 2026"
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
    "TM_40A":       ("TECHNICAL MANUAL",                    "TM-40A"),
    "TM_40B":       ("TECHNICAL MANUAL",                    "TM-40B"),
    "TM_40C":       ("TECHNICAL MANUAL",                    "TM-40C"),
    "TM_40D":       ("TECHNICAL MANUAL",                    "TM-40D"),
    "TM_40E":       ("TECHNICAL MANUAL",                    "TM-40E"),
    "TM_40F":       ("TECHNICAL MANUAL",                    "TM-40F"),
    "TM_50A":       ("TECHNICAL MANUAL",                    "TM-50A"),
    "TM_50B":       ("TECHNICAL MANUAL",                    "TM-50B"),
    "TM_50C":       ("TECHNICAL MANUAL",                    "TM-50C"),
    "TM_50D":       ("TECHNICAL MANUAL",                    "TM-50D"),
    "TM_50E":       ("TECHNICAL MANUAL",                    "TM-50E"),
    "TM_50F":       ("TECHNICAL MANUAL",                    "TM-50F"),
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
    "CONCEPTS_GUIDE_TM50A": ("CONCEPTS GUIDE",                   "TM-50A"),
    "CONCEPTS_GUIDE_TM50B": ("CONCEPTS GUIDE",                   "TM-50B"),
    "CONCEPTS_GUIDE_TM50C": ("CONCEPTS GUIDE",                   "TM-50C"),
    "CONCEPTS_GUIDE_TM50D": ("CONCEPTS GUIDE",                   "TM-50D"),
    "CONCEPTS_GUIDE_TM50E": ("CONCEPTS GUIDE",                   "TM-50E"),
    "CONCEPTS_GUIDE_TM50F": ("CONCEPTS GUIDE",                   "TM-50F"),
    "SYLLABUS_TM10":     ("COURSE SYLLABUS",                     "TM-10"),
    "SYLLABUS_TM20":     ("COURSE SYLLABUS",                     "TM-20"),
    "SYLLABUS_TM30":     ("COURSE SYLLABUS",                     "TM-30"),
    "SYLLABUS_TM40A":    ("COURSE SYLLABUS",                     "TM-40A"),
    "SYLLABUS_TM40B":    ("COURSE SYLLABUS",                     "TM-40B"),
    "SYLLABUS_TM40C":    ("COURSE SYLLABUS",                     "TM-40C"),
    "SYLLABUS_TM40D":    ("COURSE SYLLABUS",                     "TM-40D"),
    "SYLLABUS_TM40E":    ("COURSE SYLLABUS",                     "TM-40E"),
    "SYLLABUS_TM40F":    ("COURSE SYLLABUS",                     "TM-40F"),
    "CHEAT":             ("QUICK REFERENCE CARD",                "MSS-QRC"),
    "README":            ("CURRICULUM INDEX",                    "MSS-IDX"),
    "QUICK_START":       ("QUICK START GUIDE",                   "MSS-QS"),
    "AAR_TEMPLATE":      ("AFTER-ACTION REVIEW TEMPLATE",        "AAR-MSS"),
    "CURRICULUM_MAINT":  ("STANDARD OPERATING PROCEDURE",        "SOP-MAINT"),
    "EX_10":             ("PRACTICAL EXERCISE",                  "EX-10"),
    "EX_20":             ("PRACTICAL EXERCISE",                  "EX-20"),
    "EX_30":             ("PRACTICAL EXERCISE",                  "EX-30"),
    "EX_40A":            ("PRACTICAL EXERCISE",                  "EX-40A"),
    "EX_40B":            ("PRACTICAL EXERCISE",                  "EX-40B"),
    "EX_40C":            ("PRACTICAL EXERCISE",                  "EX-40C"),
    "EX_40D":            ("PRACTICAL EXERCISE",                  "EX-40D"),
    "EX_40E":            ("PRACTICAL EXERCISE",                  "EX-40E"),
    "EX_40F":            ("PRACTICAL EXERCISE",                  "EX-40F"),
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


# ── Page CSS ──────────────────────────────────────────────────────────────────
PAGE_CSS = """
/* ================================================================
   USAREUR-AF MAVEN PUBLICATION STYLESHEET
   Army doctrine look + USAREUR-AF command colors (all Arial)
   ================================================================ */

:root {
  --navy:      #0C2340;
  --navy-dark: #071628;
  --navy-mid:  #163A6C;
  --gold:      #C8971A;
  --gold-lt:   #E0B840;
  --gold-pale: #FDF5DC;
  --text:      #111827;
  --gray-50:   #F8F9FC;
  --gray-100:  #E5E8F0;
  --gray-300:  #B0B8D0;
  --gray-500:  #6B7898;
  --warn-bg:   #FFF8E1;
  --warn-brd:  #C8971A;
  --caut-bg:   #FFF3E0;
  --caut-brd:  #C84000;
  --note-bg:   #E8EEF8;
  --note-brd:  #163A6C;
}

* { box-sizing: border-box; margin: 0; padding: 0; }

/* ── Diagonal DRAFT watermark on every page ───────────────────── */
body::before {
  content: "DRAFT";
  position: fixed;
  top: 45%;
  left: 50%;
  transform: translate(-50%, -50%) rotate(-40deg);
  font-family: Arial, sans-serif;
  font-size: 100pt;
  font-weight: bold;
  color: rgba(200, 151, 26, 0.09);
  letter-spacing: 0.3em;
  pointer-events: none;
  z-index: 0;
  white-space: nowrap;
}

/* ── Body ────────────────────────────────────────────────────── */
body {
  font-family: Arial, 'Helvetica Neue', sans-serif;
  font-size: 10.5pt;
  line-height: 1.65;
  color: var(--text);
  background: white;
}

/* ── Cover page ──────────────────────────────────────────────── */
.cover {
  page-break-after: always;
  min-height: 8.5in;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 0 0.6in 0.3in;
  text-align: center;
  position: relative;
  z-index: 1;
}
.cover-topbar {
  width: calc(100% + 1.2in);
  margin-left: -0.6in;
  background: #7A3800;
  padding: 0.1in 0.4in;
  margin-bottom: 0.4in;
  -webkit-print-color-adjust: exact;
  color-adjust: exact;
}
.cover-topbar p {
  color: #FFD080;
  font-family: Arial, sans-serif;
  font-size: 9.5pt;
  font-weight: bold;
  letter-spacing: 0.18em;
  text-align: center;
}
.cover-pub-type {
  font-size: 10pt;
  font-weight: bold;
  letter-spacing: 0.2em;
  color: var(--gray-500);
  text-transform: uppercase;
  margin-bottom: 0.06in;
}
.cover-pub-number {
  font-size: 24pt;
  font-weight: bold;
  color: var(--navy);
  letter-spacing: 0.05em;
  margin-bottom: 0.25in;
}
/* Decorative seal ring */
.cover-seal {
  width: 1.5in;
  height: 1.5in;
  border: 3px solid var(--navy);
  border-radius: 50%;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  margin: 0.1in auto 0.3in;
  background: white;
  box-shadow: 0 0 0 7px var(--gold), 0 0 0 11px var(--navy);
  -webkit-print-color-adjust: exact;
  color-adjust: exact;
}
.cover-seal-star {
  font-size: 38pt;
  color: var(--navy);
  line-height: 1;
}
.cover-seal-text {
  font-size: 5.5pt;
  font-weight: bold;
  letter-spacing: 0.1em;
  color: var(--navy-mid);
  text-transform: uppercase;
  margin-top: 2px;
}
.cover-title {
  font-size: 17pt;
  font-weight: bold;
  color: var(--navy);
  line-height: 1.25;
  margin: 0.12in 0 0.08in;
  border-top: 3px solid var(--gold);
  border-bottom: 3px solid var(--gold);
  padding: 0.12in 0;
  width: 100%;
  -webkit-print-color-adjust: exact;
  color-adjust: exact;
}
.cover-subtitle {
  font-size: 11pt;
  color: var(--navy-mid);
  margin-bottom: 0.3in;
  font-style: italic;
}
.cover-spacer { flex: 1; }
.cover-hq {
  font-size: 9.5pt;
  line-height: 1.8;
  color: var(--navy);
}
.cover-dist {
  font-size: 7.5pt;
  color: var(--gray-500);
  margin: 0.1in 0 0.15in;
  letter-spacing: 0.04em;
}
.cover-date {
  font-size: 10pt;
  font-weight: bold;
  color: var(--navy-mid);
  margin-bottom: 0.2in;
}
.cover-bottombar {
  width: calc(100% + 1.2in);
  margin-left: -0.6in;
  background: #7A3800;
  padding: 0.1in 0.4in;
  -webkit-print-color-adjust: exact;
  color-adjust: exact;
}
.cover-bottombar p {
  color: #FFD080;
  font-size: 9.5pt;
  font-weight: bold;
  letter-spacing: 0.18em;
  text-align: center;
}

/* ── Body content wrapper ────────────────────────────────────── */
.body-content { padding-top: 0.25in; }

/* ── Headings ────────────────────────────────────────────────── */
h1 {
  font-size: 17pt;
  font-weight: bold;
  color: var(--navy);
  border-bottom: 3px solid var(--gold);
  padding-top: 0.35in;
  padding-bottom: 0.09in;
  margin: 0 0 0.18in;
  page-break-after: avoid;
  text-transform: uppercase;
  letter-spacing: 0.02em;
  -webkit-print-color-adjust: exact;
  color-adjust: exact;
}
h2 {
  font-size: 13pt;
  font-weight: bold;
  color: white;
  background: var(--navy);
  background-clip: padding-box;
  border-left: 5px solid var(--gold);
  border-top: 0.25in solid transparent;
  padding: 0.07in 0.12in;
  margin: 0.12in 0 0.12in;
  page-break-after: avoid;
  text-transform: uppercase;
  letter-spacing: 0.02em;
  -webkit-print-color-adjust: exact;
  color-adjust: exact;
}
h3 {
  font-size: 11pt;
  font-weight: bold;
  color: var(--navy-mid);
  border-bottom: 1.5px solid var(--gray-100);
  padding-bottom: 0.04in;
  margin: 0.28in 0 0.1in;
  page-break-after: avoid;
}
h4 {
  font-size: 10.5pt;
  font-weight: bold;
  color: var(--navy-mid);
  margin: 0.2in 0 0.07in;
  page-break-after: avoid;
}
h5, h6 {
  font-size: 10pt;
  font-weight: bold;
  color: var(--gray-500);
  margin: 0.15in 0 0.05in;
  page-break-after: avoid;
}

/* ── Paragraphs ──────────────────────────────────────────────── */
p { margin: 0.07in 0; orphans: 3; widows: 3; }

/* ── Lists ───────────────────────────────────────────────────── */
ul, ol { padding-left: 1.4em; margin: 0.05in 0; }
li { margin: 0.04in 0; }

/* ── Links ───────────────────────────────────────────────────── */
a { color: var(--navy-mid); }

/* ── Horizontal rule ─────────────────────────────────────────── */
hr {
  border: none;
  border-top: 2px solid var(--gold);
  margin: 0.22in 0;
  -webkit-print-color-adjust: exact;
  color-adjust: exact;
}

/* ── Tables ──────────────────────────────────────────────────── */
table {
  border-collapse: collapse;
  width: 100%;
  font-size: 9.5pt;
  margin: 0.12in 0;
  page-break-inside: avoid;
}
thead tr th {
  background: var(--navy);
  color: white;
  font-size: 9pt;
  font-weight: bold;
  padding: 6px 10px;
  text-align: left;
  letter-spacing: 0.02em;
  border: 1px solid var(--navy-dark);
  -webkit-print-color-adjust: exact;
  color-adjust: exact;
}
tbody tr td {
  padding: 5px 10px;
  border: 1px solid var(--gray-100);
  vertical-align: top;
  word-break: break-word;
  overflow-wrap: break-word;
}
tbody tr:nth-child(even) td {
  background: var(--gray-50);
  -webkit-print-color-adjust: exact;
  color-adjust: exact;
}

/* ── Code ────────────────────────────────────────────────────── */
code {
  font-family: 'Courier New', 'Lucida Console', monospace;
  font-size: 9pt;
  background: var(--gray-50);
  border: 1px solid var(--gray-100);
  padding: 1px 4px;
  border-radius: 2px;
  color: #1a237e;
  -webkit-print-color-adjust: exact;
  color-adjust: exact;
}
pre {
  background: #F3F5FA;
  border-left: 4px solid var(--navy-mid);
  padding: 0.1in 0.15in;
  font-size: 8pt;
  line-height: 1.4;
  white-space: pre-wrap;
  word-break: break-word;
  overflow-wrap: anywhere;
  page-break-inside: avoid;
  margin: 0.1in 0;
  -webkit-print-color-adjust: exact;
  color-adjust: exact;
}
pre code { background: none; border: none; padding: 0; }

/* ── WARNING / CAUTION / NOTE callout boxes ──────────────────── */
.callout-warning {
  border: 2px solid var(--warn-brd);
  background: var(--warn-bg);
  margin: 0.1in 0;
  padding: 0.08in 0.15in;
  page-break-inside: avoid;
  -webkit-print-color-adjust: exact;
  color-adjust: exact;
}
.callout-caution {
  border: 2px solid var(--caut-brd);
  background: var(--caut-bg);
  margin: 0.1in 0;
  padding: 0.08in 0.15in;
  page-break-inside: avoid;
  -webkit-print-color-adjust: exact;
  color-adjust: exact;
}
.callout-note {
  border: 2px solid var(--note-brd);
  background: var(--note-bg);
  margin: 0.1in 0;
  padding: 0.08in 0.15in;
  page-break-inside: avoid;
  -webkit-print-color-adjust: exact;
  color-adjust: exact;
}
.callout-label {
  font-size: 9pt;
  font-weight: bold;
  letter-spacing: 0.12em;
  text-align: center;
  display: block;
  margin-bottom: 4px;
  padding-bottom: 4px;
  border-bottom: 1px solid currentColor;
}
.callout-warning .callout-label { color: #7A4000; border-color: var(--warn-brd); }
.callout-caution .callout-label { color: #8B2000; border-color: var(--caut-brd); }
.callout-note    .callout-label { color: var(--navy-mid); border-color: var(--note-brd); }
.callout-body { font-size: 10pt; }
"""

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


# ── Chrome CDP printer ────────────────────────────────────────────────────────
def _free_port():
    with socket.socket() as s:
        s.bind(("", 0))
        return s.getsockname()[1]


def _wait_for_browser_ws(port: int, retries: int = 20) -> str:
    """Return the browser-level WebSocket URL from /json/version."""
    for _ in range(retries):
        try:
            data = json.loads(
                urllib.request.urlopen(f"http://localhost:{port}/json/version", timeout=2).read()
            )
            return data["webSocketDebuggerUrl"]
        except Exception:
            time.sleep(0.4)
    raise RuntimeError(f"Chrome CDP not ready on port {port}")


def _send(ws, method: str, params: dict = None, cmd_id: int = 1,
          session_id: str = None, timeout: int = 90) -> dict:
    """Send a CDP command and wait for its response (skipping events)."""
    msg = {"id": cmd_id, "method": method, "params": params or {}}
    if session_id:
        msg["sessionId"] = session_id
    ws.send(json.dumps(msg))
    deadline = time.time() + timeout
    while time.time() < deadline:
        raw = ws.recv()
        resp = json.loads(raw)
        if resp.get("id") == cmd_id and resp.get("sessionId", session_id) == session_id:
            if "error" in resp:
                raise RuntimeError(f"CDP error in {method}: {resp['error']}")
            return resp.get("result", {})
    raise TimeoutError(f"CDP timeout waiting for {method}")


def html_file_to_pdf(html_path: Path, pdf_path: Path, header_html: str, footer_html: str) -> bool:
    port = _free_port()
    proc = subprocess.Popen(
        [
            CHROME,
            f"--remote-debugging-port={port}",
            "--headless=new",
            "--disable-gpu",
            "--no-sandbox",
            "--disable-dev-shm-usage",
            "--disable-extensions",
            "--remote-allow-origins=*",
            f"--user-data-dir=/tmp/chrome-pdf-{port}",
        ],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    try:
        browser_ws = _wait_for_browser_ws(port)
        ws = websocket.create_connection(browser_ws, timeout=30)
        try:
            # Create a new page target
            r = _send(ws, "Target.createTarget", {"url": "about:blank"}, cmd_id=1)
            target_id = r["targetId"]

            # Attach to it with flat session protocol
            r = _send(ws, "Target.attachToTarget",
                      {"targetId": target_id, "flatten": True}, cmd_id=2)
            sid = r["sessionId"]

            # Enable Page domain on the session
            _send(ws, "Page.enable", cmd_id=3, session_id=sid)

            # Navigate to the HTML file
            _send(ws, "Page.navigate",
                  {"url": f"file://{html_path.resolve()}"},
                  cmd_id=4, session_id=sid)

            # Poll readyState until complete
            for _ in range(40):
                r = _send(ws, "Runtime.evaluate",
                          {"expression": "document.readyState", "returnByValue": True},
                          cmd_id=5, session_id=sid)
                if r.get("result", {}).get("value") == "complete":
                    break
                time.sleep(0.4)
            time.sleep(0.5)  # let JS post-processing run

            result = _send(
                ws,
                "Page.printToPDF",
                {
                    "landscape":           False,
                    "displayHeaderFooter": True,
                    "headerTemplate":      header_html,
                    "footerTemplate":      footer_html,
                    "printBackground":     True,
                    "scale":               1.0,
                    "paperWidth":          8.5,
                    "paperHeight":         11.0,
                    "marginTop":           0.72,
                    "marginBottom":        0.58,
                    "marginLeft":          0.85,
                    "marginRight":         0.85,
                    "transferMode":        "ReturnAsBase64",
                },
                cmd_id=6, session_id=sid, timeout=120,
            )
        finally:
            ws.close()

        pdf_path.write_bytes(base64.b64decode(result["data"]))
        return True
    except Exception as exc:
        print(f"      ERROR: {exc}")
        return False
    finally:
        proc.terminate()
        proc.wait(timeout=5)


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
    ok = html_file_to_pdf(tmp_path, pdf_path, make_header(pub_number), FOOTER_TEMPLATE)
    tmp_path.unlink(missing_ok=True)
    print(f"  {'OK  ' if ok else 'FAIL'} {out_stem}.pdf")
    return ok


def convert_html_direct(src_rel: str, out_stem: str, pub_number: str = "MSS-HUB") -> bool:
    src = REPO_ROOT / src_rel
    if not src.exists():
        print(f"  SKIP  {src_rel}")
        return False
    pdf_path = OUT_DIR / f"{out_stem}.pdf"
    ok = html_file_to_pdf(src, pdf_path, make_header(pub_number), FOOTER_TEMPLATE)
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
    ("maven_training/syllabi/SYLLABUS_TM40A.md",                                       "SYLLABUS_TM40A"),
    ("maven_training/syllabi/SYLLABUS_TM40B.md",                                       "SYLLABUS_TM40B"),
    ("maven_training/syllabi/SYLLABUS_TM40C.md",                                       "SYLLABUS_TM40C"),
    ("maven_training/syllabi/SYLLABUS_TM40D.md",                                       "SYLLABUS_TM40D"),
    ("maven_training/syllabi/SYLLABUS_TM40E.md",                                       "SYLLABUS_TM40E"),
    ("maven_training/syllabi/SYLLABUS_TM40F.md",                                       "SYLLABUS_TM40F"),
    # ── Practical exercises ───────────────────────────────────────────────────
    ("maven_training/exercises/EX-10_operator_basics/EXERCISE.md",                     "EX_10_OPERATOR_BASICS"),
    ("maven_training/exercises/EX-20_no_code_builder/EXERCISE.md",                     "EX_20_NO_CODE_BUILDER"),
    ("maven_training/exercises/EX-30_advanced_builder/EXERCISE.md",                    "EX_30_ADVANCED_BUILDER"),
    ("maven_training/exercises/EX-40A_orsa/EXERCISE.md",                               "EX_40A_ORSA"),
    ("maven_training/exercises/EX-40B_ai_engineer/EXERCISE.md",                        "EX_40B_AI_ENGINEER"),
    ("maven_training/exercises/EX-40C_ml_engineer/EXERCISE.md",                        "EX_40C_ML_ENGINEER"),
    ("maven_training/exercises/EX-40D_program_manager/EXERCISE.md",                    "EX_40D_PROGRAM_MANAGER"),
    ("maven_training/exercises/EX-40E_knowledge_manager/EXERCISE.md",                  "EX_40E_KNOWLEDGE_MANAGER"),
    ("maven_training/exercises/EX-40F_software_engineer/EXERCISE.md",                  "EX_40F_SOFTWARE_ENGINEER"),
    # ── Assessments (pre/post exams) ──────────────────────────────────────────
    ("maven_training/exercises/exams/EXAM_TM10_PRE.md",                                "EXAM_TM10_PRE"),
    ("maven_training/exercises/exams/EXAM_TM10_POST.md",                               "EXAM_TM10_POST"),
    ("maven_training/exercises/exams/EXAM_TM20_PRE.md",                                "EXAM_TM20_PRE"),
    ("maven_training/exercises/exams/EXAM_TM20_POST.md",                               "EXAM_TM20_POST"),
    ("maven_training/exercises/exams/EXAM_TM30_PRE.md",                                "EXAM_TM30_PRE"),
    ("maven_training/exercises/exams/EXAM_TM30_POST.md",                               "EXAM_TM30_POST"),
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
    ("maven_training/exercises/exams/EXAM_TM50A_PRE.md",                               "EXAM_TM50A_PRE"),
    ("maven_training/exercises/exams/EXAM_TM50A_POST.md",                              "EXAM_TM50A_POST"),
    ("maven_training/exercises/exams/EXAM_TM50B_PRE.md",                               "EXAM_TM50B_PRE"),
    ("maven_training/exercises/exams/EXAM_TM50B_POST.md",                              "EXAM_TM50B_POST"),
    ("maven_training/exercises/exams/EXAM_TM50C_PRE.md",                               "EXAM_TM50C_PRE"),
    ("maven_training/exercises/exams/EXAM_TM50C_POST.md",                              "EXAM_TM50C_POST"),
    ("maven_training/exercises/exams/EXAM_TM50D_PRE.md",                               "EXAM_TM50D_PRE"),
    ("maven_training/exercises/exams/EXAM_TM50D_POST.md",                              "EXAM_TM50D_POST"),
    ("maven_training/exercises/exams/EXAM_TM50E_PRE.md",                               "EXAM_TM50E_PRE"),
    ("maven_training/exercises/exams/EXAM_TM50E_POST.md",                              "EXAM_TM50E_POST"),
    ("maven_training/exercises/exams/EXAM_TM50F_PRE.md",                               "EXAM_TM50F_PRE"),
    ("maven_training/exercises/exams/EXAM_TM50F_POST.md",                              "EXAM_TM50F_POST"),
    # ── Technical manuals ─────────────────────────────────────────────────────
    ("maven_training/tm/TM_10_maven_user/TM_10_MAVEN_USER.md",                         "TM_10_MAVEN_USER"),
    ("maven_training/tm/TM_20_builder/TM_20_BUILDER.md",                               "TM_20_BUILDER"),
    ("maven_training/tm/TM_30_advanced_builder/TM_30_ADVANCED_BUILDER.md",             "TM_30_ADVANCED_BUILDER"),
    ("maven_training/tm/TM_40A_orsa/TM_40A_ORSA.md",                                   "TM_40A_ORSA"),
    ("maven_training/tm/TM_40A_orsa/CONCEPTS_GUIDE_TM40A_ORSA.md",                     "CONCEPTS_GUIDE_TM40A_ORSA"),
    ("maven_training/tm/TM_40B_ai_engineer/TM_40B_AI_ENGINEER.md",                     "TM_40B_AI_ENGINEER"),
    ("maven_training/tm/TM_40B_ai_engineer/CONCEPTS_GUIDE_TM40B_AI_ENGINEER.md",       "CONCEPTS_GUIDE_TM40B_AI_ENGINEER"),
    ("maven_training/tm/TM_40C_ml_engineer/TM_40C_ML_ENGINEER.md",                     "TM_40C_ML_ENGINEER"),
    ("maven_training/tm/TM_40C_ml_engineer/CONCEPTS_GUIDE_TM40C_ML_ENGINEER.md",       "CONCEPTS_GUIDE_TM40C_ML_ENGINEER"),
    ("maven_training/tm/TM_40D_program_manager/TM_40D_PROGRAM_MANAGER.md",             "TM_40D_PROGRAM_MANAGER"),
    ("maven_training/tm/TM_40D_program_manager/CONCEPTS_GUIDE_TM40D_PROGRAM_MANAGER.md","CONCEPTS_GUIDE_TM40D_PROGRAM_MANAGER"),
    ("maven_training/tm/TM_40E_knowledge_manager/TM_40E_KNOWLEDGE_MANAGER.md",         "TM_40E_KNOWLEDGE_MANAGER"),
    ("maven_training/tm/TM_40E_knowledge_manager/CONCEPTS_GUIDE_TM40E_KNOWLEDGE_MANAGER.md","CONCEPTS_GUIDE_TM40E_KNOWLEDGE_MANAGER"),
    ("maven_training/tm/TM_40F_software_engineer/TM_40F_SOFTWARE_ENGINEER.md",         "TM_40F_SOFTWARE_ENGINEER"),
    ("maven_training/tm/TM_40F_software_engineer/CONCEPTS_GUIDE_TM40F_SOFTWARE_ENGINEER.md","CONCEPTS_GUIDE_TM40F_SOFTWARE_ENGINEER"),
    ("maven_training/tm/TM_50A_orsa_advanced/TM_50A_ORSA_ADVANCED.md",                 "TM_50A_ORSA_ADVANCED"),
    ("maven_training/tm/TM_50A_orsa_advanced/CONCEPTS_GUIDE_TM50A_ORSA_ADVANCED.md",   "CONCEPTS_GUIDE_TM50A_ORSA_ADVANCED"),
    ("maven_training/tm/TM_50B_ai_engineer_advanced/TM_50B_AI_ENGINEER_ADVANCED.md",   "TM_50B_AI_ENGINEER_ADVANCED"),
    ("maven_training/tm/TM_50B_ai_engineer_advanced/CONCEPTS_GUIDE_TM50B_AI_ENGINEER_ADVANCED.md","CONCEPTS_GUIDE_TM50B_AI_ENGINEER_ADVANCED"),
    ("maven_training/tm/TM_50C_ml_engineer_advanced/TM_50C_ML_ENGINEER_ADVANCED.md",   "TM_50C_ML_ENGINEER_ADVANCED"),
    ("maven_training/tm/TM_50C_ml_engineer_advanced/CONCEPTS_GUIDE_TM50C_ML_ENGINEER_ADVANCED.md","CONCEPTS_GUIDE_TM50C_ML_ENGINEER_ADVANCED"),
    ("maven_training/tm/TM_50D_program_manager_advanced/TM_50D_PROGRAM_MANAGER_ADVANCED.md","TM_50D_PROGRAM_MANAGER_ADVANCED"),
    ("maven_training/tm/TM_50D_program_manager_advanced/CONCEPTS_GUIDE_TM50D_PROGRAM_MANAGER_ADVANCED.md","CONCEPTS_GUIDE_TM50D_PROGRAM_MANAGER_ADVANCED"),
    ("maven_training/tm/TM_50E_knowledge_manager_advanced/TM_50E_KNOWLEDGE_MANAGER_ADVANCED.md","TM_50E_KNOWLEDGE_MANAGER_ADVANCED"),
    ("maven_training/tm/TM_50E_knowledge_manager_advanced/CONCEPTS_GUIDE_TM50E_KNOWLEDGE_MANAGER_ADVANCED.md","CONCEPTS_GUIDE_TM50E_KNOWLEDGE_MANAGER_ADVANCED"),
    ("maven_training/tm/TM_50F_software_engineer_advanced/TM_50F_SOFTWARE_ENGINEER_ADVANCED.md","TM_50F_SOFTWARE_ENGINEER_ADVANCED"),
    ("maven_training/tm/TM_50F_software_engineer_advanced/CONCEPTS_GUIDE_TM50F_SOFTWARE_ENGINEER_ADVANCED.md","CONCEPTS_GUIDE_TM50F_SOFTWARE_ENGINEER_ADVANCED"),
]
HTML_TARGETS = [
    ("maven_training/mss_info_app/index.html", "MSS_TRAINING_HUB"),
]


# ── Main ──────────────────────────────────────────────────────────────────────
def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    print(f"Output: {OUT_DIR}\n")
    ok = fail = 0

    print("=== Markdown → PDF ===")
    for rel, stem in MD_TARGETS:
        if convert_md(rel, stem): ok += 1
        else: fail += 1

    print("\n=== HTML → PDF ===")
    for rel, stem in HTML_TARGETS:
        if convert_html_direct(rel, stem): ok += 1
        else: fail += 1

    print(f"\nDone: {ok} OK, {fail} failed.")
    if fail:
        sys.exit(1)

if __name__ == "__main__":
    main()
