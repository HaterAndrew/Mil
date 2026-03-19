"""
publication_css.py — USAREUR-AF Maven publication stylesheet.

Imported by build_pdfs.py and injected inline into generated HTML so Chrome
headless can use it without loading external files.
"""

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
