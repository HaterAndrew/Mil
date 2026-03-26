# ENVIRONMENT SETUP — EX_40N UI/UX Designer

**Track:** EX_40N — UI/UX Designer (SL 4N) | **Prerequisite:** SL 3 REQUIRED | **Continuation:** SL 5N — Advanced UI/UX Designer
**Companion exams:** EXAM_TM40N_PRE (administer before exercise), EXAM_TM40N_POST (administer after exercise)

## Environment Type

MSS with Workshop design access and external design tool (Figma or equivalent).

## Required Access

| Account | Permissions Required |
|---------|---------------------|
| Training accounts | MSS Builder access (Workshop view/edit), Ontology read access for data binding |
| Design tool | Figma (or equivalent) license — one per trainee |
| Evaluator account | Viewer on all participant Workshop designs |

## Pre-Load Instructions

### 1. Design Brief

Provide each trainee with a 1-page requirements brief from a simulated staff section. The brief should include:

| Attribute | Value |
|-----------|-------|
| Requesting unit | Simulated staff section (e.g., G3 Operations, G4 Sustainment) |
| Data domain | Operational data already available in the training Ontology (e.g., personnel readiness, equipment status, training completion) |
| Decision context | A specific decision the staff section needs to make using this data |
| User role | Rank range and MOS of the primary user population |
| Current process | How they currently get this information (e.g., Excel spreadsheet emailed weekly) |

**NOTE:** The brief should be intentionally incomplete — trainees must discover additional requirements through user research (Task 1).

### 2. Workshop Environment

Ensure the training MSS environment has:
- Workshop application creation permissions for each trainee
- At least one populated Ontology Object Type that trainees can bind to for Workshop layout exercises
- Example Workshop applications available for reference (read-only)

### 3. Role-Playing Partners

- Each trainee will be paired with another trainee for user research and usability testing
- Provide role-playing guidance cards: each "user" should have a defined role, rank, 3 tasks they do daily, and 2 frustrations with the current process
- Role-playing partners should NOT have seen the trainee's design before the usability test

### 4. Design Tools

- Confirm design tool access (Figma or equivalent) for each trainee
- Provide the **MSS Design System Template** (described below) to each trainee
- Provide the MSS accessibility checklist (SL 4N §6-2) as a printable handout

### 5. MSS Design System Template

The MSS Design System Template is a Figma (or equivalent) file that provides pre-built, reusable components aligned to MSS visual standards. Distribute one copy per trainee at the start of the exercise. The template contains:

| Component | Description |
|-----------|-------------|
| Classification banners | Top/bottom banners for UNCLASSIFIED, CUI, SECRET, and TS/SCI — correct colors, fonts, and placement per DoD 5200.48 |
| Color palette | MSS-approved primary, secondary, and semantic colors (success/warning/error/info) with WCAG AA contrast-compliant pairings |
| Typography scale | Heading and body text styles using the approved MSS typeface, sized for readability on standard-issue monitors |
| Status indicators | Badge and icon components for common states: active, inactive, pending, overdue, complete, alert |
| Data table patterns | Sortable table, card grid, and list view layouts pre-wired with placeholder data columns |
| Form controls | Input fields, dropdowns, date pickers, and toggle switches styled to MSS standards |
| Navigation shell | Sidebar and top-bar navigation frame matching the MSS application layout |
| Chart templates | Bar, line, donut, and KPI card components using the MSS color palette |

**NOTE:** The template enforces MSS visual consistency across trainee designs. Trainees may extend or compose components but should not override base styles (colors, classification banners, typography) during the exercise. Customization of base styles is covered in SL 5N (Advanced UI/UX Designer).
