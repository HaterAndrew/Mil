# MSS Training Hub — Deployment Guide

**Artifact:** `mss_info_app/index.html` + `pdf/` (~141 PDFs)
**Target:** mss.data.mil (Foundry stack)
**Owner:** USAREUR-AF Operational Data Team

---

## FDE Deployment Guide

### Prerequisites
- Code Repository access on the target Foundry stack
- `maven_training/` directory from the git repo
- Static site hosting enabled on the stack

### Steps

1. **Create a new Code Repository** in Foundry
   - Type: Static Website
   - Name: `mss-training-hub` (or per naming standards)

2. **Upload directory structure** — preserve layout exactly:
   ```
   maven_training/
   ├── mss_info_app/index.html   ← entry point
   └── pdf/                      ← ~141 PDFs (verify vs. repo size limit)
   ```
   Only these two directories are required for the hub to function.

3. **Set entry point** to `mss_info_app/index.html`

4. **Publish** and record the resulting URL

5. **Verify** by clicking 3–4 PDF links across different TM tracks

6. **Register the URL** in Workshop navigation or share directly with training coordinators

### Verification Checklist
- [ ] Index page loads with USAREUR-AF header
- [ ] At least one TM-10/20/30 PDF opens in new tab
- [ ] At least one TM-40 WFF PDF opens in new tab
- [ ] At least one TM-50 specialist PDF opens in new tab
- [ ] mss.data.mil account links are clickable

### Plan B — If Code Repository static hosting is unavailable or size-limited

**Use Foundry Media Set + Workshop HTML Widget**

1. Upload `maven_training/pdf/` to a Foundry Media Set
2. For each PDF, record its Media Set URL
3. Run the link-replacement script (see FDE Prompt section) to rewrite all `../pdf/` hrefs to absolute Media Set URLs
4. Embed the updated `index.html` as a **Workshop HTML widget** (raw HTML input)
5. PDFs open via Media Set viewer in new tab

**Trade-off:** ~141 URLs to map; one-time effort. Use a script to automate the rewrite.

---

## FDE Prompt

Use this prompt when tasking an FDE or AI assistant to set up the deployment:

```
I need to deploy a static HTML training hub on our Foundry stack (mss.data.mil).

The entry point is `mss_info_app/index.html`. It links to PDF files using relative
paths like `../pdf/TM_40A_INTELLIGENCE.pdf`. There are approximately 141 PDFs in
the `pdf/` directory.

Please set up a Code Repository (Static Website type) that hosts both directories
with the structure preserved so the relative paths resolve correctly. The entry
point should be `mss_info_app/index.html`.

Once deployed, the site should be accessible at a stable URL on mss.data.mil, and
clicking any PDF link should open that file in a new browser tab.
```

**Plan B prompt (if static hosting is unavailable or repo size limits are a problem):**

```
Upload the `pdf/` directory to a Foundry Media Set and provide me with a mapping
of filename → Media Set URL. I will use that mapping to rewrite the links in
index.html and then embed the updated HTML as a Workshop HTML widget.
```

---

## User Guide

**For:** Training Coordinators and Hub Owners

### Accessing the Hub

1. Navigate to the URL provided by your FDE
2. The Training Hub opens — use the navigation tabs at the top to move between sections
3. Click any **"Open PDF →"** button or document card to open that publication
4. PDFs open in a new browser tab — download or print from there

### If a Link Doesn't Work

- Confirm you are on the mss.data.mil network or VPN
- Hard refresh: `Ctrl+Shift+R`
- If a specific PDF is missing, notify your FDE — the file may not have been included in the deployment

### Updating the Hub (when new PDFs are published)

1. Rebuild PDFs locally: run `python scripts/build_pdfs.py` from repo root
2. Send updated `pdf/` files and any changed `index.html` to your FDE
3. FDE re-deploys to the Code Repository — URL does not change

### Plan B — If the main hub URL is unavailable

Your FDE will provide a **Workshop fallback link**. This version of the hub is embedded in a Foundry Workshop module — functionality is identical. Bookmark it as your backup.

If neither link works, PDFs are available directly from the Foundry Media Set. Contact your FDE or unit data steward for the Media Set location.
