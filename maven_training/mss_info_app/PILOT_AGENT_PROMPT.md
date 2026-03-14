# MSS Training Hub — Agent Build Instructions
## For: Foundry Pilot / AI Agent in Palantir Foundry Workshop

---

## TASK OVERVIEW

You are being asked to build the **MSS Training Hub** — a single-page web application serving as the central information portal for the USAREUR-AF Maven Smart System (MSS) training curriculum. The attached file (`index.html`) is the reference implementation. Your job is to faithfully reproduce it in the Foundry Workshop environment.

**If you can embed raw HTML/CSS/JS directly:** use the attached `index.html` as-is — it is fully self-contained (no external dependencies, no build step, one file).

**If you must build in React/TSX:** use these instructions to reconstruct the app component by component.

---

## WHAT THIS APP IS

A static single-page application (SPA) with:
- A full-screen **splash screen** (animated star-field canvas, command branding, enter button)
- A **sticky collapsible sidebar** navigation (240px wide, collapses to 52px icon-only)
- A **header** with USAREUR-AF command branding (crest SVG, title, meta block, version strip)
- A **content area** that shows one panel at a time, driven by sidebar nav clicks
- A **footer** with classification notice and version info

**No backend. No API calls. All data is static HTML. All navigation is vanilla JS `showPanel()` calls.**

---

## DESIGN SYSTEM

### Command Colors (CSS custom properties)
```css
--navy:          #0C2340;   /* primary background */
--navy-dark:     #071628;
--navy-light:    #163A6C;
--navy-mid:      #1E4A88;
--navy-pale:     #EEF2FA;
--gold:          #C8971A;   /* primary accent */
--gold-light:    #E0B840;
--gold-dark:     #9A7010;
--gold-pale:     #FDF5DC;
--white:         #FFFFFF;
--off-white:     #F3F5FA;
--gray-50:       #EFF1F8;
--gray-100:      #E0E4EF;
--gray-200:      #C4CAE0;
--gray-400:      #7A88A8;
--gray-600:      #485878;
--gray-700:      #303C58;
--gray-900:      #0A1628;
--warning-red:   #8A1A1A;
--caution-amber: #B86810;
--note-teal:     #0A5C70;
--planned-slate: #3A4A6A;
--green-ok:      #1A5C28;
--radius:        3px;
--radius-lg:     6px;
```

### Typography
- **Body:** `Inter, system-ui, Arial, sans-serif` — 14px base, 1.65 line-height
- **UI labels/headings:** `Arial, Helvetica, sans-serif` — uppercase, tracked
- **Monospace:** `'Courier New', Courier, monospace` — header meta, code blocks, footer
- h2: 18px, navy, bold, 1px bottom border (gray-100)
- h3: 14px, gray-900, semibold

---

## PAGE LAYOUT (top to bottom)

```
┌──────────────────────────────────────────────────────────┐
│  UNCLASSIFIED banner — green (#1E6B2A), white text, top  │
├──────────────────────────────────────────────────────────┤
│  HEADER — navy gradient, gold bottom border (3px)        │
│  [crest SVG]  [command label / title / subtitle]  [meta] │
├──────────────────────────────────────────────────────────┤
│  HEADER STRIP — version/date info, navy-dark bg          │
├────────────┬─────────────────────────────────────────────┤
│            │                                             │
│  SIDEBAR   │  CONTENT AREA                               │
│  240px     │  max-width 1100px, padded 28px/32px         │
│  navy-dark │  One .panel div active at a time            │
│  sticky    │  Panel switch: fade-in animation            │
│  100vh     │                                             │
├────────────┴─────────────────────────────────────────────┤
│  FOOTER — navy-dark, gold monospaced text                │
│  UNCLASSIFIED banner — bottom                            │
└──────────────────────────────────────────────────────────┘
```

---

## SPLASH SCREEN

Full-viewport overlay (`position:fixed; inset:0; z-index:9999`). Background: `#050C18`. Dismissed by clicking the enter button — fades out (opacity transition 0.8s), then `display:none`.

Elements (layered by z-index):
1. `<canvas id="starCanvas">` — animated ~140 white star dots, slow parallax drift, `requestAnimationFrame` loop
2. Radial glow — centered gold/navy gradient circle (`position:absolute`, pointer-events none)
3. Scanline sweep — thin 2px gold horizontal line, `animation: scanDown 6s linear infinite` top-to-bottom
4. Top + bottom classification banners: `UNCLASSIFIED` in green, white text, uppercase tracked
5. Center content block (above canvas):
   - USAREUR-AF crest/logo image
   - Command label: `USAREUR-AF` (gold, tiny, tracked uppercase)
   - Main title: `MSS Training Hub` (large white bold)
   - Subtitle: version/date (monospace, dim)
   - **Enter button**: navy border, gold text, arrow `→`, outer glow pulse animation
   - Footer meta: system/classification text (tiny monospace, very dim)

---

## HEADER

```html
<div class="banner-unclass">UNCLASSIFIED</div>
<header>
  <div class="header-inner">
    <img src="USAREUR_Insignia.svg" class="crest" alt="USAREUR-AF Crest">
    <div class="header-text">
      <div class="header-command">HQ USAREUR-AF · Army Europe and Africa</div>
      <div class="header-title">MSS Training Hub</div>
      <div class="header-subtitle">Maven Smart System · Palantir Foundry · Operational Data Training</div>
    </div>
    <div class="header-meta">
      <div class="badge">USAREUR-AF</div>
      <div>MSS TRAINING HUB</div>
      <div>VERSION 3.0 · MARCH 2026</div>
      <div>UNCLASSIFIED</div>
    </div>
  </div>
  <div class="header-strip">
    <div class="header-strip-inner">
      <span>USAREUR-AF · OPERATIONAL DATA TEAM</span>
      <span>MSS TRAINING HUB · V3.0 · MARCH 2026 · UNCLASSIFIED</span>
    </div>
  </div>
</header>
```

Header: `linear-gradient(155deg, navy-dark 0%, navy 50%, navy-light 100%)`. Gold 3px bottom border. Subtle diagonal stripe texture overlay via `::before` pseudo-element.

---

## SIDEBAR NAVIGATION

```
[≡ toggle btn]

[★ QUICK REF]          ← pinned item (gold accent, always visible)

▼ OVERVIEW
   HOME
   TRAINING SCHEDULE

▼ CORE TRAINING
   TM-10 — Maven User
   TM-20 — Builder
   TM-30 — Advanced Builder

▼ TM-40 & TM-50 SPECIALIST
   ► WFF Tracks (A–F)
   ► Technical Tracks (G–L)
   ► Advanced Tracks (TM-50)

▼ REFERENCE
   Draft Publications
   All Documents
   Task Index

▼ SUPPORT
   Help & Support
```

- Collapsible sidebar: toggle collapses to 52px (icons only, text hidden)
- Each nav item: `data-panel="<panelId>"` attribute → `showPanel()` on click
- Active item: gold left border highlight
- Groups collapse/expand by clicking group header
- Mobile: sidebar becomes drawer with dark overlay backdrop

---

## TAB PANELS

All panels are `<div id="panel-{id}" class="panel">`. CSS: `.panel { display:none }` / `.panel.active { display:block }`. Panel switch triggers CSS keyframe animation (fade + translateY 8px→0, 0.28s ease).

### Panel Inventory

| Panel ID      | Badge              | Title                                                 |
|---------------|--------------------|-------------------------------------------------------|
| `home`        | HOME               | MSS Training Curriculum — USAREUR-AF                  |
| `schedule`    | SCHEDULE           | Upcoming Training — USAREUR-AF                        |
| `tm10`        | TM-10              | Maven User Manual — All Personnel                     |
| `tm20`        | TM-20              | No-Code Builder Manual — All Staff                    |
| `tm30`        | TM-30              | Advanced Builder Manual — Data-Adjacent Specialists   |
| `specialists` | SPECIALIST TRACKS  | TM-40 & TM-50 Series — WFF & Technical Tracks         |
| `tm40`        | TM-40 / TM-50      | Technical Specialist Tracks — Developer Manuals       |
| `tm50`        | TM-50 ADVANCED     | Advanced Developer Tracks                             |
| `doctrine`    | DRAFT PUBS         | Draft Data Literacy Publications                      |
| `documents`   | ALL DOCUMENTS      | All Training Publications                             |
| `taskindex`   | TASK INDEX         | What Do You Want To Do? (task-based index)            |
| `quickref`    | QUICK REF          | Quick Reference (pinned)                              |
| `support`     | SUPPORT            | Getting Help — USAREUR-AF                             |

### Default active panel on load: `home`

---

## KEY PANEL CONTENT

### HOME
- `info` callout: "New to MSS? Start with Quick Start guide"
- `bluf` callout: find your level, follow the path
- **Find Your Level table**: role description → recommended TM → clickable chip → navigate panel
  - Rows: Any personnel (TM-10), All staff (TM-20), Data-adjacent (TM-30), Technical specialist (TM-40G–L), WFF specialist (TM-40A–F), Senior leader (Doctrine), Data literacy background
- **Learning path diagram**: vertical chain TM-10 → TM-20 → TM-30 → branch to TM-40 WFF / TM-40 Specialist → TM-50
- `note` callout: "Not finding what you need? Contact data steward."

### SCHEDULE
- `caution` callout: must request account before class, 24-hour provisioning
- Upcoming training table: TM code, Course Title, Dates, Location, Seats (color-coded), Register link
  - Seat counts: `.seat-open` (green), `.seat-low` (amber), `.seat-full` (red)

### TM-10 (Maven User Manual)
- `bluf` + `caution` (request account first) callouts
- Section 1: Getting Access (5-step numbered procedure)
- `note` callout: What is a data steward?
- Section 2: What is MSS? — 3 cards (MSS Does / MSS Is Not / USAREUR-AF Mission Areas)
- Section 3: Security Responsibilities — `warning` callout (legal ref), numbered rules
- Sections 4–6: Navigation, Data Consumption, Acceptable Use (prose + lists)

### TM-20 (No-Code Builder)
- `bluf` callout
- Stack diagram: Raw Data → Dataset → Pipeline → Application → User (navy → gold → gray layers)
- Sections: Workshop basics, building dashboards, data connections, forms, publishing
- PDF link card

### TM-30 (Advanced Builder)
- `bluf` callout
- Sections: Pipeline authoring, Foundry Transforms, ontology basics, advanced Workshop widgets
- Code blocks: Python transform examples
- PDF link card

### SPECIALIST TRACKS (panel: `specialists`)
- `bluf` callout: explains WFF (A–F, TM-20 prereq) vs Technical (G–L, TM-30 prereq)
- **Role/MOS routing table**: role → recommended track → advanced track
  - Rows grouped by WFF / Technical with section dividers
- **WFF Track cards grid** (TM-40A through TM-40F): each `.track-card` with navy header, gold left border, track title, audience, prereq chip "TM-20 Req.", PDF link
- **Technical Track cards grid** (TM-40G through TM-40L): same pattern, chip "TM-30 Req."
- CTA button → navigate to `tm40` panel

### TM-40 (Technical Specialist)
- Track cards: TM-40G (ORSA), TM-40H (AI Engineer), TM-40I (ML Engineer), TM-40J (Program Manager), TM-40K (Knowledge Manager), TM-40L (Software Engineer)
- Each card: description, audience, prereq (TM-30), PDF link

### TM-50 (Advanced Developer)
- Same six tracks as TM-40G–L but advanced level (TM-50G through TM-50L)
- Prereq: corresponding TM-40 track
- `note` callout: TM-50 is available only after completing corresponding TM-40

### DOCTRINE (Draft Publications)
- `warning` callout: DRAFT status, distribution restriction
- 3 document cards: DATA_LITERACY_technical_reference, DATA_LITERACY_senior_leaders, GLOSSARY_data_foundry
- Each card: audience, description, PDF link (`target="_blank"`)

### DOCUMENTS (All Publications)
- Complete master table: all publications grouped by category
- Categories: Quick Start, Core TM Series, WFF Tracks, Technical Tracks, Advanced Tracks, Syllabi, Exams, Exercises, Training Management, Doctrine
- Columns: Document Name, Type, Format (PDF), Link

### TASK INDEX
- "I want to…" task-based routing table
- Tasks mapped to TM number + section
- Dropdown quick-selectors for WFF tracks (A–F) and Technical tracks (G–L)

### QUICK REF (pinned)
- Role-to-track routing table (condensed, all rows)
- Dropdown selectors for WFF and Technical track routing (open PDF directly)
- Troubleshooting quick hits: 4–5 common issues + fixes
- Contact block: Help Desk and data steward routing

### SUPPORT
- `bluf` callout: know who to call before you have a problem
- `warning` callout: security incidents — report immediately, preserve screen state
- Contact routing table: Issue → Route To → Priority
  - Security incident row: **IMMEDIATE** priority
- "Before calling" info checklist (username, app name, error message, time, steps, browser)
- Prerequisites before first login (3 items)
- USAREUR-AF Data Team info cards: Location, Publications, Feedback
- `note` callout: distribution restriction

---

## REUSABLE UI COMPONENTS

### Section Header
```html
<div class="section-header">
  <span class="section-badge">BADGE</span>
  <span class="section-title">Panel Title</span>
  <span class="section-subtitle">Subtitle — right-aligned</span>
</div>
```
Styling: flex row, 2px gold-dark bottom border, 5px navy left border-left, badge = navy bg + gold text.

### Callout Boxes
```html
<div class="callout {variant}">
  <div class="callout-label">LABEL</div>
  <div class="callout-body">Content.</div>
</div>
```
Variants and left border colors:
- `warning` — red (`--warning-red`), icon prefix `⚠`
- `caution` — amber (`--caution-amber`), icon prefix `⚑`
- `note` — teal (`--note-teal`), icon prefix `●`
- `bluf` — navy (`--navy`), icon prefix `►`
- `info` — teal-light, icon prefix `ℹ`

Icons are added via CSS `::before` on `.callout-label`.

### Cards
```html
<div class="card-grid">
  <div class="card gold-top">
    <div class="card-label">LABEL</div>
    <div class="card-title">Title</div>
    <div class="card-body">Body text.</div>
  </div>
</div>
```
Variants: `.card` (navy top), `.card.gold-top`, `.card.red-top`, `.card.slate-top`.
Hover: `transform: translateY(-3px)`, deeper shadow, top border → gold.

### Track Cards (TM-40/50 panels)
```html
<div class="track-grid">
  <div class="track-card">
    <div class="track-card-hdr">
      <span class="track-tm">TM-40A — Intelligence</span>
      <span class="track-chip">TM-20 Req.</span>
    </div>
    <div class="track-body">
      <div class="track-name">Intelligence Warfighting Function</div>
      <div class="track-audience">G2/S2 • MI units • ISR analysts</div>
      <div class="track-prereq">Prereq: TM-20 • <a href="../pdf/TM_40A_INTELLIGENCE.pdf" target="_blank">Open PDF →</a></div>
    </div>
  </div>
</div>
```
Track card header: navy bg, 4px gold left border. Chip: gold-tinted pill. Grid: `repeat(auto-fill, minmax(320px, 1fr))`.

### Tables
```html
<div class="table-wrap">
  <table>
    <thead><tr><th>Col 1</th><th>Col 2</th></tr></thead>
    <tbody>
      <tr><td>...</td><td>...</td></tr>
    </tbody>
  </table>
</div>
```
`.table-wrap`: `overflow-x: auto`. `thead`: navy bg, gold text, small-caps, 11px.
Alternating rows: even rows get `--navy-pale` bg. Hover: `--navy-pale`.

### Chips
```html
<span class="chip chip-navy">TM-10</span>
<span class="chip chip-gold">TM-30</span>
<span class="chip chip-slate">PLANNED</span>
<span class="chip chip-gray">DRAFT</span>
```
Pill shape, uppercase, 10px, bold, tracked.

### Learning Path (vertical flow)
Alternating `.path-dot` + `.path-line` + `.path-content` in a flex column:
- Dot colors: gold (active) / gray (optional) / slate (planned)
- Lines: 2px solid gold-dark (solid = required) / dashed (optional branch)
- Content box: white card with TM label (gold-dark mono) + name + audience text
- `path-spacer` div separates branch groups

### Stack Diagram
```html
<div class="stack-diagram">
  <div class="stack-layer layer-1">Raw Data Layer</div>
  <div class="stack-arrow">↓</div>
  <div class="stack-layer layer-2">Dataset</div>
  <div class="stack-arrow">↓</div>
  <div class="stack-layer layer-3">Pipeline / Transform</div>
  <div class="stack-arrow">↓</div>
  <div class="stack-layer layer-4">Application / Workshop</div>
  <div class="stack-arrow">↓</div>
  <div class="stack-layer layer-5">User / Analyst</div>
</div>
```
Layers: `layer-1` = navy (darkest) → `layer-5` = gray-200. Max-width 380px, centered.

---

## JAVASCRIPT BEHAVIOR

All vanilla JS, no libraries, no frameworks.

```js
// ── Panel switching ────────────────────────────────────────────
function showPanel(id) {
  document.querySelectorAll('.panel').forEach(p => p.classList.remove('active'));
  document.getElementById('panel-' + id).classList.add('active');
  // Update sidebar active highlights
  document.querySelectorAll('[data-panel]').forEach(btn => {
    btn.classList.toggle('active', btn.getAttribute('data-panel') === id);
  });
  document.getElementById('main-content').scrollTop = 0;
}

// ── Sidebar collapse ───────────────────────────────────────────
document.getElementById('sidebar-toggle').addEventListener('click', () => {
  document.querySelector('.sidebar').classList.toggle('collapsed');
});

// ── Sidebar group expand/collapse ──────────────────────────────
document.querySelectorAll('.snav-group-hdr').forEach(hdr => {
  hdr.addEventListener('click', () => {
    hdr.parentElement.classList.toggle('open');
  });
});

// ── Splash dismiss ─────────────────────────────────────────────
document.getElementById('splash-enter').addEventListener('click', () => {
  const splash = document.getElementById('splash');
  splash.classList.add('fade-out');            // CSS: opacity 0, transition 0.8s
  setTimeout(() => { splash.style.display = 'none'; }, 850);
  showPanel('home');
});

// ── Star-field canvas ──────────────────────────────────────────
// Initialize ~140 stars: random x, y, radius (0.5–2px), velocity (slow drift)
// requestAnimationFrame loop: clear → move → wrap at edges → draw white circles
// Canvas fills full splash viewport

// ── QR dropdowns ───────────────────────────────────────────────
// Dropdown toggle button opens/closes .qr-dropdown-menu
// Clicking a .qr-dropdown-item[data-panel] calls showPanel() and closes menu
// Clicking outside closes all open dropdowns

// ── Panel fade-in (CSS) ────────────────────────────────────────
// @keyframes panelReveal { from { opacity:0; transform:translateY(8px) } to { opacity:1; transform:translateY(0) } }
// .panel.active { animation: panelReveal 0.28s ease forwards }
```

---

## TM-40 TRACK TABLE (authoritative)

| Code   | Track Name               | Prereq | Panel        |
|--------|--------------------------|--------|--------------|
| TM-40A | Intelligence WFF         | TM-20  | `specialists`|
| TM-40B | Fires WFF                | TM-20  | `specialists`|
| TM-40C | Movement & Maneuver WFF  | TM-20  | `specialists`|
| TM-40D | Sustainment WFF          | TM-20  | `specialists`|
| TM-40E | Protection WFF           | TM-20  | `specialists`|
| TM-40F | Mission Command WFF      | TM-20  | `specialists`|
| TM-40G | ORSA                     | TM-30  | `tm40`       |
| TM-40H | AI Engineer              | TM-30  | `tm40`       |
| TM-40I | ML Engineer              | TM-30  | `tm40`       |
| TM-40J | Program Manager          | TM-30  | `tm40`       |
| TM-40K | Knowledge Manager        | TM-30  | `tm40`       |
| TM-40L | Software Engineer        | TM-30  | `tm40`       |

**TM-50 is G–L only. There is NO TM-50A through TM-50F.**

---

## PDF LINK PATHS

All links: `../pdf/<FILENAME>.pdf` opened `target="_blank"`. Key filenames:

```
QUICK_START.pdf
TM_10_MAVEN_USER.pdf
TM_20_BUILDER.pdf
TM_30_ADVANCED_BUILDER.pdf
TM_40A_INTELLIGENCE.pdf       TM_40B_FIRES.pdf
TM_40C_MOVEMENT_MANEUVER.pdf  TM_40D_SUSTAINMENT.pdf
TM_40E_PROTECTION.pdf         TM_40F_MISSION_COMMAND.pdf
TM_40G_ORSA.pdf               TM_40H_AI_ENGINEER.pdf
TM_40I_ML_ENGINEER.pdf        TM_40J_PROGRAM_MANAGER.pdf
TM_40K_KNOWLEDGE_MANAGER.pdf  TM_40L_SOFTWARE_ENGINEER.pdf
TM_50G_ORSA_ADVANCED.pdf      TM_50H_AI_ENGINEER_ADVANCED.pdf
TM_50I_ML_ENGINEER_ADVANCED.pdf  TM_50J_PROGRAM_MANAGER_ADVANCED.pdf
TM_50K_KNOWLEDGE_MANAGER_ADVANCED.pdf  TM_50L_SOFTWARE_ENGINEER_ADVANCED.pdf
SYLLABUS_TM10.pdf   SYLLABUS_TM20.pdf   SYLLABUS_TM30.pdf
SYLLABUS_TM40A.pdf through SYLLABUS_TM40L.pdf
SYLLABUS_TM50G.pdf through SYLLABUS_TM50L.pdf
EXAM_TM10_PRE.pdf   EXAM_TM10_POST.pdf  (pattern repeats for all TM levels)
DATA_LITERACY_technical_reference.pdf
DATA_LITERACY_senior_leaders.pdf
GLOSSARY_data_foundry.pdf
MTP_MSS.pdf  POI_MSS.pdf  CAD_MSS.pdf  TEO_MSS.pdf
```

If deploying in Foundry with PDFs hosted as Media Set items, replace `../pdf/` with absolute Foundry Media Set URLs.

---

## ACCESSIBILITY & PRINT

- All interactive elements keyboard-focusable
- `focus-visible` outline: `2px solid var(--gold)`, offset 2px
- `prefers-reduced-motion`: all animations/transitions disabled
- Print stylesheet: hides splash, sidebar, header, nav; all panels `display:block`; black text on white; cards: no shadow, 1px gray border; footer: black on white

---

## FOUNDRY WORKSHOP DEPLOYMENT NOTES

- **HTML widget**: paste the full `index.html` into a custom HTML widget. No external dependencies required. Works as-is.
- **React/TSX custom widget**: replicate using `useState` for active panel, map CSS variables to a theme object, build each panel as a component.
- **No Foundry ontology dependencies**: purely static content. No OSDK calls, no dataset queries, no object types.
- **PDF hosting**: if PDFs are in a Foundry Media Set, update all `../pdf/` prefixes to the appropriate Media Set base URL.
- **Crest image**: `USAREUR_Insignia.svg` — must be available in the same directory or embedded as an inline SVG data URI.

---

## BUILD PRIORITY ORDER

1. CSS design tokens + reset
2. Header + UNCLASSIFIED banners
3. Sidebar nav shell (structure + toggle + collapse)
4. Panel system (`showPanel()`, active state, fade-in animation)
5. HOME panel content (routing table, learning path)
6. TM-10, TM-20, TM-30 panels (highest-traffic content)
7. Specialist Tracks panel + TM-40 + TM-50 panels
8. Remaining panels: Doctrine, Documents, Task Index, Quick Ref, Support, Schedule
9. Splash screen (cosmetic, last — does not affect app functionality)

---

## COMMON CHANGE TASKS

**Update a training date:**
`id="panel-schedule"` → find `<tr>` → update date cell.

**Add a new document:**
`id="panel-documents"` → add `<tr>` with: Document, Type, Format, PDF link.

**Change a prerequisite on a track card:**
Find the track card in `specialists` or `tm40` panel → update `.track-chip` text.

**Add a new TM-40 track:**
1. Add track card to `specialists` (WFF) or `tm40` (technical) panel.
2. Add PDF link entry.
3. Add row to routing table in `home` panel.
4. Add row to task index in `taskindex` panel.
5. Add sidebar nav entry if it gets its own panel.

---

*Reference implementation: see attached `index.html` — authoritative source for all content, exact wording, and layout. When in doubt, match the HTML exactly.*
