"""SharePoint Sync — Streamlit dashboard.

Tracks sync state between local maven_training/ content and
SharePoint/Cloudflare deployments.  Dashboard-only (port 8509).

Run: streamlit run apps/sharepoint_sync/dashboard.py --server.port 8509
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

import pandas as pd
import streamlit as st

# Ensure repo root is on sys.path so `apps.theme` resolves
_REPO_ROOT = Path(__file__).resolve().parent.parent.parent
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))

from apps.theme import (  # noqa: E402
    GOLD,
    GOLD_PALE,
    GREEN_OK,
    NAVY,
    NAVY_PALE,
    WARNING_RED,
    inject_branding,
)

from .db import SessionLocal, init_db  # noqa: E402
from .sync_engine import (  # noqa: E402
    SOURCE_ROOT,
    build_sync_package,
    compare_states,
    compute_file_hashes,
    generate_sync_manifest,
    get_sharepoint_variants,
    get_sync_history,
    load_sync_state,
    record_sync,
)

# ---------------------------------------------------------------------------
# Status color map
# ---------------------------------------------------------------------------
_STATUS_COLORS = {
    "UNCHANGED": GREEN_OK,
    "MODIFIED": GOLD,
    "ADDED": NAVY,
    "DELETED": WARNING_RED,
}

# File type icons (best-effort mapping by extension)
_FILE_ICONS = {
    ".md": "📄",
    ".html": "🌐",
    ".pdf": "📕",
    ".py": "🐍",
    ".json": "📋",
    ".csv": "📊",
    ".pptx": "📑",
    ".png": "🖼️",
    ".jpg": "🖼️",
    ".svg": "🖼️",
    ".txt": "📝",
    ".sh": "⚙️",
    ".yml": "⚙️",
    ".yaml": "⚙️",
    ".toml": "⚙️",
}


def _icon_for(path: str) -> str:
    """Return a file-type icon for the given path."""
    ext = Path(path).suffix.lower()
    return _FILE_ICONS.get(ext, "📁")


def _status_badge(status: str) -> str:
    """Return an HTML badge for a sync status."""
    color = _STATUS_COLORS.get(status, "#888")
    return (
        f'<span style="background:{color};color:#fff;padding:2px 8px;'
        f'border-radius:3px;font-size:11px;font-weight:bold;'
        f'letter-spacing:0.5px;">{status}</span>'
    )


# ---------------------------------------------------------------------------
# Page config + branding
# ---------------------------------------------------------------------------
st.set_page_config(
    page_title="SharePoint Sync | USAREUR-AF",
    page_icon="🔄",
    layout="wide",
)
inject_branding("SharePoint Sync")

init_db()

# ---------------------------------------------------------------------------
# Sidebar navigation
# ---------------------------------------------------------------------------
with st.sidebar:
    st.markdown("### Navigation")
    page = st.radio(
        "Select view",
        [
            "Sync Status",
            "File Diff Browser",
            "SharePoint Variants",
            "Generate Package",
            "Record Sync",
            "Sync History",
        ],
        label_visibility="collapsed",
    )

    st.divider()
    st.caption(f"Source: `{SOURCE_ROOT}`")

# ---------------------------------------------------------------------------
# Compute current state (cached per session to avoid repeated hashing)
# ---------------------------------------------------------------------------
@st.cache_data(ttl=60, show_spinner="Scanning maven_training/...")
def _scan_files() -> dict[str, str]:
    return compute_file_hashes(SOURCE_ROOT)


def _get_diff() -> dict[str, list[str]]:
    """Compute diff between current files and last sync."""
    current = _scan_files()
    db = SessionLocal()
    try:
        last = load_sync_state(db)
    finally:
        db.close()
    return compare_states(current, last)


# ---------------------------------------------------------------------------
# KPI row (always visible)
# ---------------------------------------------------------------------------
current_hashes = _scan_files()
diff = _get_diff()

kpi1, kpi2, kpi3, kpi4 = st.columns(4)
kpi1.metric("Total Files", f"{len(current_hashes):,}")
kpi2.metric("Added", len(diff["added"]), delta=None)
kpi3.metric("Modified", len(diff["modified"]), delta=None)
kpi4.metric("Deleted", len(diff["deleted"]), delta=None)

st.divider()

# ===================================================================
# PAGE: Sync Status
# ===================================================================
if page == "Sync Status":
    st.header("Sync Status")

    total_changed = len(diff["added"]) + len(diff["modified"]) + len(diff["deleted"])
    if total_changed == 0:
        st.success("All files are in sync with the last recorded baseline.")
    else:
        st.warning(
            f"**{total_changed}** file(s) changed since last sync: "
            f"{len(diff['added'])} added, {len(diff['modified'])} modified, "
            f"{len(diff['deleted'])} deleted."
        )

    # Breakdown by status
    if diff["added"]:
        st.markdown(f"**Added** ({len(diff['added'])})")
        for f in diff["added"][:50]:
            st.markdown(
                f"{_icon_for(f)} `{f}` {_status_badge('ADDED')}",
                unsafe_allow_html=True,
            )
        if len(diff["added"]) > 50:
            st.caption(f"...and {len(diff['added']) - 50} more")

    if diff["modified"]:
        st.markdown(f"**Modified** ({len(diff['modified'])})")
        for f in diff["modified"][:50]:
            st.markdown(
                f"{_icon_for(f)} `{f}` {_status_badge('MODIFIED')}",
                unsafe_allow_html=True,
            )
        if len(diff["modified"]) > 50:
            st.caption(f"...and {len(diff['modified']) - 50} more")

    if diff["deleted"]:
        st.markdown(f"**Deleted** ({len(diff['deleted'])})")
        for f in diff["deleted"][:50]:
            st.markdown(
                f"{_icon_for(f)} ~~`{f}`~~ {_status_badge('DELETED')}",
                unsafe_allow_html=True,
            )
        if len(diff["deleted"]) > 50:
            st.caption(f"...and {len(diff['deleted']) - 50} more")

# ===================================================================
# PAGE: File Diff Browser
# ===================================================================
elif page == "File Diff Browser":
    st.header("File Diff Browser")

    # Filter controls
    filter_col1, filter_col2 = st.columns([1, 3])
    with filter_col1:
        status_filter = st.multiselect(
            "Filter by status",
            ["ADDED", "MODIFIED", "DELETED", "UNCHANGED"],
            default=["ADDED", "MODIFIED", "DELETED"],
        )
    with filter_col2:
        path_filter = st.text_input(
            "Filter by path (contains)",
            placeholder="e.g., pdf/ or .html",
        )

    # Build file list
    all_files: list[dict] = []
    for status_key, status_label in [
        ("added", "ADDED"),
        ("modified", "MODIFIED"),
        ("deleted", "DELETED"),
        ("unchanged", "UNCHANGED"),
    ]:
        if status_label not in status_filter:
            continue
        for f in diff[status_key]:
            if path_filter and path_filter.lower() not in f.lower():
                continue
            all_files.append({
                "Icon": _icon_for(f),
                "File Path": f,
                "Status": status_label,
                "Extension": Path(f).suffix.lower() or "(none)",
            })

    st.caption(f"Showing {len(all_files)} file(s)")

    if all_files:
        # Show as expandable items grouped by directory
        dirs: dict[str, list[dict]] = {}
        for entry in all_files:
            parent = str(Path(entry["File Path"]).parent)
            dirs.setdefault(parent, []).append(entry)

        for dir_name in sorted(dirs.keys()):
            entries = dirs[dir_name]
            status_counts = {}
            for e in entries:
                status_counts[e["Status"]] = status_counts.get(e["Status"], 0) + 1
            count_str = ", ".join(f"{v} {k}" for k, v in sorted(status_counts.items()))

            with st.expander(f"📂 **{dir_name}/** — {count_str}", expanded=False):
                for e in sorted(entries, key=lambda x: x["File Path"]):
                    st.markdown(
                        f"{e['Icon']} `{Path(e['File Path']).name}` "
                        f"{_status_badge(e['Status'])}",
                        unsafe_allow_html=True,
                    )
    else:
        st.info("No files match the current filter.")

# ===================================================================
# PAGE: SharePoint Variants
# ===================================================================
elif page == "SharePoint Variants":
    st.header("SharePoint Variants")
    st.caption(
        "Files with `_sharepoint` suffix and their standard counterparts. "
        "Discrepancies may indicate the SharePoint variant needs updating."
    )

    variants = get_sharepoint_variants()

    if not variants:
        st.info("No SharePoint variant files found.")
    else:
        for v in variants:
            sp_exists = v["sharepoint_exists"] == "True"
            std_exists = v["standard_exists"] == "True"

            col1, col2, col3 = st.columns([4, 4, 2])
            with col1:
                label = "Standard"
                if std_exists:
                    st.markdown(f"✅ `{v['standard_path']}`")
                else:
                    st.markdown(f"❌ `{v['standard_path']}` **(MISSING)**")

            with col2:
                if sp_exists:
                    st.markdown(f"✅ `{v['sharepoint_path']}`")
                else:
                    st.markdown(f"❌ `{v['sharepoint_path']}` **(MISSING)**")

            with col3:
                # Check if both exist and compare hashes
                if sp_exists and std_exists:
                    sp_hash = current_hashes.get(v["sharepoint_path"], "")
                    std_hash = current_hashes.get(v["standard_path"], "")
                    if sp_hash and std_hash:
                        # These are intentionally different files, but flag
                        # if the standard was modified after last sync while
                        # SharePoint variant was not
                        std_modified = v["standard_path"] in diff["modified"]
                        sp_modified = v["sharepoint_path"] in diff["modified"]
                        if std_modified and not sp_modified:
                            st.markdown(
                                f'<span style="background:{WARNING_RED};color:#fff;'
                                f'padding:2px 8px;border-radius:3px;font-size:11px;'
                                f'font-weight:bold;">STALE</span>',
                                unsafe_allow_html=True,
                            )
                        else:
                            st.markdown(
                                f'<span style="background:{GREEN_OK};color:#fff;'
                                f'padding:2px 8px;border-radius:3px;font-size:11px;'
                                f'font-weight:bold;">OK</span>',
                                unsafe_allow_html=True,
                            )
                    else:
                        st.markdown("—")
                else:
                    st.markdown(
                        f'<span style="background:{WARNING_RED};color:#fff;'
                        f'padding:2px 8px;border-radius:3px;font-size:11px;'
                        f'font-weight:bold;">MISSING</span>',
                        unsafe_allow_html=True,
                    )

            st.divider()

# ===================================================================
# PAGE: Generate Package
# ===================================================================
elif page == "Generate Package":
    st.header("Generate Sync Package")

    total_changed = len(diff["added"]) + len(diff["modified"])

    pkg_col1, pkg_col2 = st.columns(2)
    with pkg_col1:
        st.subheader("Changes Only")
        st.markdown(
            f"ZIP containing **{total_changed}** added/modified file(s) "
            f"plus a `SYNC_MANIFEST.md`."
        )
        if total_changed == 0:
            st.info("No changes to package.")
        else:
            if st.button("Build Changes Package", key="pkg_changes"):
                with st.spinner("Building ZIP..."):
                    pkg_bytes = build_sync_package(SOURCE_ROOT, diff, include_all=False)
                st.download_button(
                    label=f"Download Changes ZIP ({len(pkg_bytes) / 1024 / 1024:.1f} MB)",
                    data=pkg_bytes,
                    file_name="sharepoint_sync_changes.zip",
                    mime="application/zip",
                )

    with pkg_col2:
        st.subheader("Full Content")
        st.markdown(
            f"ZIP containing **all {len(current_hashes):,}** current files "
            f"plus a `SYNC_MANIFEST.md`."
        )
        if st.button("Build Full Package", key="pkg_full"):
            with st.spinner("Building full ZIP..."):
                pkg_bytes = build_sync_package(SOURCE_ROOT, diff, include_all=True)
            st.download_button(
                label=f"Download Full ZIP ({len(pkg_bytes) / 1024 / 1024:.1f} MB)",
                data=pkg_bytes,
                file_name="sharepoint_sync_full.zip",
                mime="application/zip",
            )

    st.divider()
    st.subheader("Sync Manifest Preview")
    manifest_md = generate_sync_manifest(diff)
    with st.expander("View manifest", expanded=False):
        st.code(manifest_md, language="markdown")

# ===================================================================
# PAGE: Record Sync
# ===================================================================
elif page == "Record Sync":
    st.header("Record Sync")
    st.caption(
        "Mark the current file state as the new sync baseline. "
        "Do this after deploying to SharePoint/Cloudflare."
    )

    total_changed = len(diff["added"]) + len(diff["modified"]) + len(diff["deleted"])

    if total_changed == 0:
        st.success("Content is already in sync. No changes to record.")
    else:
        st.warning(
            f"**{total_changed}** change(s) will be recorded as synced: "
            f"{len(diff['added'])} added, {len(diff['modified'])} modified, "
            f"{len(diff['deleted'])} deleted."
        )

    notes = st.text_area(
        "Sync notes (optional)",
        placeholder="e.g., Deployed SL 4 updates to SharePoint + Cloudflare Pages",
        max_chars=500,
    )

    if st.button("Record Sync Baseline", type="primary"):
        db = SessionLocal()
        try:
            rec = record_sync(db, current_hashes, notes=notes, diff=diff)
            st.success(
                f"Sync recorded (ID: {rec.id}) — "
                f"{rec.total_files} files baselined at "
                f"{rec.timestamp:%Y-%m-%d %H:%M:%S} UTC."
            )
            # Clear cache so next load reflects new baseline
            _scan_files.clear()
        finally:
            db.close()

# ===================================================================
# PAGE: Sync History
# ===================================================================
elif page == "Sync History":
    st.header("Sync History")

    db = SessionLocal()
    try:
        history = get_sync_history(db)
    finally:
        db.close()

    if not history:
        st.info("No sync records yet. Use **Record Sync** to create the first baseline.")
    else:
        df = pd.DataFrame(history)
        df = df.rename(columns={
            "id": "ID",
            "timestamp": "Timestamp",
            "total_files": "Total Files",
            "added": "Added",
            "modified": "Modified",
            "deleted": "Deleted",
            "notes": "Notes",
        })

        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True,
            column_config={
                "ID": st.column_config.NumberColumn(width="small"),
                "Total Files": st.column_config.NumberColumn(format="%d"),
                "Added": st.column_config.NumberColumn(format="%d"),
                "Modified": st.column_config.NumberColumn(format="%d"),
                "Deleted": st.column_config.NumberColumn(format="%d"),
            },
        )

# ---------------------------------------------------------------------------
# Footer
# ---------------------------------------------------------------------------
st.markdown(
    '<div class="app-footer">'
    "USAREUR-AF Operational Data Team — SharePoint Sync Dashboard"
    "</div>",
    unsafe_allow_html=True,
)
