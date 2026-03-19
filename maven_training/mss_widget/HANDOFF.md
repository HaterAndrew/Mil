# MSS Training Hub — React/TSX Widget Handoff
**Date:** March 2026
**Owner:** USAREUR-AF Operational Data Team
**Deployment target:** Foundry Workshop custom widget

---

## What this is

A full React/TypeScript port of `mss_info_app/index.html`, built with Vite. All 13 panels are implemented. No iframes, no external CDN dependencies. Builds to a single JS bundle + CSS file.

---

## Build output

Run `npm run build` from `maven_training/mss_widget/`. Output goes to `dist/`:

| File | Size (gzip) |
|------|------------|
| `dist/index.html` | 0.3 kB |
| `dist/assets/index.js` | ~84 kB |
| `dist/assets/index.css` | ~6.5 kB |
| `dist/assets/USAREUR_Insignia.svg` | ~3 kB |

---

## PDF links

All PDFs resolve through the Foundry Media Set:

**Media Set RID:** `ri.mio.main.media-set.9c297238-56bf-46d4-881a-db21-dcee1c`
**Base URL:** `https://mss.data.mil/mio/api/mediaSet/<RID>/file/<FILENAME>.pdf`

All URLs are centralized in `src/constants/urls.ts`. To update a URL, change it there — it propagates everywhere.

**Authentication:** All PDFs require CAC/MSS login at mss.data.mil. Users must be authenticated before clicking links.

---

## Panels

| Panel ID | Component | Notes |
|----------|-----------|-------|
| `quickref` | `QuickRef.tsx` | Default landing panel |
| `home` | `Home.tsx` | Role-selection table, learning path |
| `schedule` | `Schedule.tsx` | Inlined — no iframe |
| `tm10` | `TM10.tsx` | |
| `tm20` | `TM20.tsx` | |
| `tm30` | `TM30.tsx` | |
| `specialists` | `Specialists.tsx` | WFF + specialist track overview |
| `tm40` | `TM40.tsx` | Specialist track cards |
| `tm50` | `TM50.tsx` | Advanced track cards |
| `doctrine` | `Doctrine.tsx` | Data Literacy publications |
| `documents` | `Documents.tsx` | Full document library |
| `taskindex` | `TaskIndex.tsx` | Search/filter — inlined, no iframe |
| `support` | `Support.tsx` | Contact routing |

---

## FDE integration steps

1. **Install deps:** `npm install` (Node 18+ required)
2. **Build:** `npm run build`
3. **Deploy `dist/` contents** to the Workshop custom widget package
4. Set the widget entry point to `dist/index.html`
5. Verify PDF links open (requires authenticated mss.data.mil session)

### If the Workshop SDK requires a specific entry point format

The app mounts at `<div id="root">` in `index.html`. Wrap accordingly per your SDK version.

---

## Updating content (dual-maintenance rule)

**Every content change must be applied to BOTH:**
1. `mss_info_app/index.html` — static HTML fallback (internal web server)
2. `mss_widget/src/panels/*.tsx` — React widget (Foundry Workshop)

After updating panels, rebuild: `npm run build`

---

## Updating the training schedule

Edit `src/panels/Schedule.tsx` directly — the table rows are plain JSX. No external file dependency.

---

## Known items for FDE

- `Documents.tsx` constructs a few PDF URLs inline (exams, WFF concepts guides not in `urls.ts`) using the same Media Set base pattern — these will work as long as the files are uploaded to the Media Set.
- The 6 missing PDFs from the original Media Set upload (135 of 141) should be uploaded before final deployment.
