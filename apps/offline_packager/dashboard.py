"""Offline Package Builder — Streamlit dashboard.

Select TMs, exercises, syllabi, and PDFs from the maven_training corpus
and bundle them into a self-contained ZIP for disconnected/DDIL environments.
"""

from __future__ import annotations

import sys
from datetime import datetime, timezone
from pathlib import Path

_app_dir = Path(__file__).resolve().parent
if str(_app_dir.parent) not in sys.path:
    sys.path.insert(0, str(_app_dir.parent))

import streamlit as st
from theme import inject_branding, NAVY, GOLD, GOLD_PALE, NAVY_PALE, GRAY_400

from offline_packager.packager import (
    PREREQ_CHAIN,
    build_package,
    discover_content,
    estimate_size,
    get_all_tms_with_prereqs,
    resolve_dependencies,
)

# ---------------------------------------------------------------------------
# Page config — must be first Streamlit call
# ---------------------------------------------------------------------------
st.set_page_config(
    page_title="Offline Package Builder | MSS Training",
    page_icon="📦",
    layout="wide",
)
inject_branding("Offline Package Builder")

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------
# Default root path for maven_training content
_DEFAULT_ROOT = Path(__file__).resolve().parent.parent.parent / "maven_training"

# Preset bundles
PRESETS: dict[str, dict[str, list[str]]] = {
    "Foundation Package (SL 1/2/3)": {
        "tm": ["SL 1", "SL 2", "SL 3"],
    },
    "WFF Package (SL 4A-F)": {
        "tm": ["SL 4A", "SL 4B", "SL 4C", "SL 4D", "SL 4E", "SL 4F"],
    },
    "Specialist Package (SL 4G-M)": {
        "tm": ["SL 4G", "SL 4H", "SL 4M", "SL 4J", "SL 4K", "SL 4L"],
    },
    "Full Corpus": {
        "tm": list(PREREQ_CHAIN.keys()),
    },
}


# ---------------------------------------------------------------------------
# Session state initialization
# ---------------------------------------------------------------------------
if "package_history" not in st.session_state:
    st.session_state.package_history = []
if "inventory" not in st.session_state:
    st.session_state.inventory = None


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _format_size(kb: int) -> str:
    """Format KB as human-readable size string."""
    if kb < 1024:
        return f"{kb} KB"
    return f"{kb / 1024:.1f} MB"


def _tm_label(tm_id: str) -> str:
    """Friendly label for a TM identifier."""
    labels = {
        "SL 1": "SL 1 Operator",
        "SL 2": "SL 2 Builder",
        "SL 3": "SL 3 Advanced Builder",
        "SL 4A": "SL 4A Intelligence WFF",
        "SL 4B": "SL 4B Fires WFF",
        "SL 4C": "SL 4C Movement & Maneuver WFF",
        "SL 4D": "SL 4D Sustainment WFF",
        "SL 4E": "SL 4E Protection WFF",
        "SL 4F": "SL 4F Mission Command WFF",
        "SL 4G": "SL 4G ORSA",
        "SL 4H": "SL 4H AI Engineer",
        "SL 4M": "SL 4M ML Engineer",
        "SL 4J": "SL 4J Program Manager",
        "SL 4K": "SL 4K Knowledge Manager",
        "SL 4L": "SL 4L Software Engineer",
        "SL 5G": "SL 5G Advanced ORSA",
        "SL 5H": "SL 5H Advanced AI Engineer",
        "SL 5M": "SL 5M Advanced ML Engineer",
        "SL 5J": "SL 5J Advanced PM",
        "SL 5K": "SL 5K Advanced KM",
        "SL 5L": "SL 5L Advanced SWE",
    }
    return labels.get(tm_id, tm_id)


# ---------------------------------------------------------------------------
# Sidebar
# ---------------------------------------------------------------------------
with st.sidebar:
    st.markdown("---")
    st.markdown(
        "Bundle training content for **disconnected/DDIL** environments. "
        "Select content by category or use a preset, then build and download."
    )
    st.markdown("---")

    # Package history
    st.markdown("### Package History")
    if st.session_state.package_history:
        for entry in reversed(st.session_state.package_history[-10:]):
            st.markdown(
                f"**{entry['time']}** — {entry['items']} items, "
                f"{_format_size(entry['size_kb'])}"
            )
    else:
        st.caption("No packages built this session.")


# ---------------------------------------------------------------------------
# Load inventory
# ---------------------------------------------------------------------------
root_path = _DEFAULT_ROOT
if not root_path.is_dir():
    st.error(
        f"maven_training directory not found at `{root_path}`. "
        "Verify the repository structure."
    )
    st.stop()

# Cache inventory in session state to avoid repeated scans
if st.session_state.inventory is None:
    st.session_state.inventory = discover_content(root_path)

inventory = st.session_state.inventory

if st.sidebar.button("Refresh Inventory"):
    st.session_state.inventory = discover_content(root_path)
    inventory = st.session_state.inventory
    st.rerun()


# ---------------------------------------------------------------------------
# Main content
# ---------------------------------------------------------------------------
st.markdown(
    "Select training content by category or use a preset bundle, then build "
    "a self-contained ZIP for offline use."
)

# --- Preset bundles ---
st.markdown("### Preset Bundles")
preset_cols = st.columns(len(PRESETS))
preset_applied = None

for i, (preset_name, preset_sel) in enumerate(PRESETS.items()):
    with preset_cols[i]:
        if st.button(preset_name, use_container_width=True):
            preset_applied = preset_name

# ---------------------------------------------------------------------------
# Content selectors — organized by category in columns
# ---------------------------------------------------------------------------
st.markdown("---")
st.markdown("### Content Selection")

# Split TMs into groups for display
foundation_tms = ["SL 1", "SL 2", "SL 3"]
wff_tms = ["SL 4A", "SL 4B", "SL 4C", "SL 4D", "SL 4E", "SL 4F"]
specialist_tms = ["SL 4G", "SL 4H", "SL 4M", "SL 4J", "SL 4K", "SL 4L"]
advanced_tms = ["SL 5G", "SL 5H", "SL 5M", "SL 5J", "SL 5K", "SL 5L"]

# Determine defaults from preset
default_tms: list[str] = []
if preset_applied and preset_applied in PRESETS:
    default_tms = PRESETS[preset_applied].get("tm", [])

# --- TM Selection ---
col1, col2 = st.columns(2)

with col1:
    st.markdown("#### Technical Manuals")

    # Select-all buttons
    btn_cols = st.columns(4)
    with btn_cols[0]:
        select_all_tms = st.button("All TMs", key="all_tms")
    with btn_cols[1]:
        select_foundation = st.button("Foundation", key="sel_foundation")
    with btn_cols[2]:
        select_wff = st.button("All WFF", key="sel_wff")
    with btn_cols[3]:
        select_specialist = st.button("All Specialist", key="sel_specialist")

    # Compute effective defaults based on buttons
    if select_all_tms:
        default_tms = list(PREREQ_CHAIN.keys())
    elif select_foundation:
        default_tms = foundation_tms
    elif select_wff:
        default_tms = wff_tms
    elif select_specialist:
        default_tms = specialist_tms

    available_tms = [tm for tm in PREREQ_CHAIN if tm in inventory["tm"]]

    selected_tms = st.multiselect(
        "Select TMs",
        options=available_tms,
        default=[t for t in default_tms if t in available_tms],
        format_func=_tm_label,
        key="tm_select",
    )

with col2:
    st.markdown("#### Syllabi, Exercises & Exams")

    # Syllabi
    available_syllabi = sorted(inventory["syllabi"].keys())
    sel_all_syllabi = st.button("All Syllabi", key="all_syllabi")
    selected_syllabi = st.multiselect(
        "Syllabi",
        options=available_syllabi,
        default=available_syllabi if sel_all_syllabi else [],
        key="syllabi_select",
    )

    # Exercises
    available_exercises = sorted(inventory["exercises"].keys())
    sel_all_ex = st.button("All Exercises", key="all_ex")
    selected_exercises = st.multiselect(
        "Exercises",
        options=available_exercises,
        default=available_exercises if sel_all_ex else [],
        key="ex_select",
    )

    # Exams
    available_exams = sorted(inventory["exams"].keys())
    sel_all_exams = st.button("All Exams", key="all_exams")
    selected_exams = st.multiselect(
        "Exams",
        options=available_exams,
        default=available_exams if sel_all_exams else [],
        key="exam_select",
    )

# --- Doctrine, Quick Reference ---
st.markdown("---")
col3, col4 = st.columns(2)

with col3:
    st.markdown("#### Doctrine")
    available_doctrine = sorted(inventory["doctrine"].keys())
    sel_all_doctrine = st.button("All Doctrine", key="all_doctrine")
    selected_doctrine = st.multiselect(
        "Doctrine publications",
        options=available_doctrine,
        default=available_doctrine if sel_all_doctrine else [],
        key="doctrine_select",
    )

with col4:
    st.markdown("#### Quick Reference")
    available_qr = sorted(inventory["quick_reference"].keys())
    sel_all_qr = st.button("All Quick Ref", key="all_qr")
    selected_qr = st.multiselect(
        "Quick reference files",
        options=available_qr,
        default=available_qr if sel_all_qr else [],
        key="qr_select",
    )

# --- Options ---
st.markdown("---")
st.markdown("### Options")
opt_cols = st.columns(3)
with opt_cols[0]:
    include_pdfs = st.checkbox("Include PDFs", value=True, key="inc_pdfs")
with opt_cols[1]:
    include_exercises = st.checkbox("Include exercises & exams", value=True, key="inc_ex")
with opt_cols[2]:
    include_syllabi = st.checkbox("Include syllabi", value=True, key="inc_syl")


# ---------------------------------------------------------------------------
# Dependency resolution
# ---------------------------------------------------------------------------
auto_included: dict[str, list[str]] = {}
all_tms = selected_tms[:]

if selected_tms:
    auto_included = resolve_dependencies(selected_tms)
    all_tms = get_all_tms_with_prereqs(selected_tms)

    if auto_included:
        st.markdown("---")
        st.markdown("### Auto-Included Prerequisites")
        st.info(
            "The following TMs were automatically included to satisfy "
            "the prerequisite chain."
        )
        for tm, dependents in sorted(auto_included.items()):
            dep_str = ", ".join(dependents)
            st.markdown(
                f"- **{_tm_label(tm)}** — required by {dep_str}"
            )

# ---------------------------------------------------------------------------
# Build the final selection dict
# ---------------------------------------------------------------------------
final_selection: dict[str, list[str]] = {
    "tm": all_tms,
    "syllabi": selected_syllabi if include_syllabi else [],
    "exercises": selected_exercises if include_exercises else [],
    "exams": selected_exams if include_exercises else [],
    "doctrine": selected_doctrine,
    "quick_reference": selected_qr,
}

# Automatically match PDFs to selected TMs/syllabi/doctrine if PDFs are included
selected_pdfs: list[str] = []
if include_pdfs:
    all_pdfs = sorted(inventory["pdf"].keys())
    # Include all available PDFs that correspond to selected content
    selected_pdfs = all_pdfs  # Include full PDF set when PDFs are toggled on

final_selection["pdf"] = selected_pdfs

# ---------------------------------------------------------------------------
# Package preview
# ---------------------------------------------------------------------------
st.markdown("---")
st.markdown("### Package Preview")

total_items = sum(len(v) for v in final_selection.values())
est_kb = estimate_size(inventory, final_selection, include_pdfs)

metric_cols = st.columns(4)
with metric_cols[0]:
    st.metric("TMs", len(final_selection["tm"]))
with metric_cols[1]:
    st.metric("Support Files", len(final_selection["syllabi"]) +
              len(final_selection["exercises"]) + len(final_selection["exams"]))
with metric_cols[2]:
    st.metric("PDFs", len(final_selection["pdf"]))
with metric_cols[3]:
    st.metric("Est. Size", _format_size(est_kb))

# Detailed preview in expander
with st.expander("View full file list", expanded=False):
    category_labels = {
        "tm": "Technical Manuals",
        "syllabi": "Syllabi",
        "exercises": "Exercises",
        "exams": "Exams",
        "doctrine": "Doctrine",
        "pdf": "PDFs",
        "quick_reference": "Quick Reference",
    }
    for cat, items in final_selection.items():
        if not items:
            continue
        label = category_labels.get(cat, cat.title())
        st.markdown(f"**{label}** ({len(items)})")
        for item in sorted(items):
            meta = inventory.get(cat, {}).get(item, {})
            path = meta.get("path", item)
            size = meta.get("size_kb", 0)
            st.markdown(f"- `{path}` ({_format_size(size)})")

# ---------------------------------------------------------------------------
# Build & Download
# ---------------------------------------------------------------------------
st.markdown("---")

if total_items == 0:
    st.warning("No content selected. Use the selectors above to choose content.")
else:
    build_col, info_col = st.columns([1, 2])
    with build_col:
        build_pressed = st.button(
            f"BUILD PACKAGE ({_format_size(est_kb)})",
            type="primary",
            use_container_width=True,
        )

    if build_pressed:
        with st.spinner("Building offline package..."):
            zip_bytes = build_package(
                selected=final_selection,
                inventory=inventory,
                auto_included=auto_included,
                include_pdfs=include_pdfs,
                root_path=root_path,
            )

        now_str = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%Z")
        filename = f"mss_offline_package_{now_str}.zip"

        # Record to session history
        st.session_state.package_history.append({
            "time": datetime.now(timezone.utc).strftime("%H:%M UTC"),
            "items": total_items,
            "size_kb": len(zip_bytes) // 1024,
            "filename": filename,
        })

        st.success(
            f"Package built: **{filename}** "
            f"({_format_size(len(zip_bytes) // 1024)})"
        )

        st.download_button(
            label="DOWNLOAD ZIP",
            data=zip_bytes,
            file_name=filename,
            mime="application/zip",
            type="primary",
            use_container_width=True,
        )

# ---------------------------------------------------------------------------
# Footer
# ---------------------------------------------------------------------------
st.markdown(
    '<div class="app-footer">USAREUR-AF OPERATIONAL DATA TEAM '
    "— OFFLINE PACKAGE BUILDER</div>",
    unsafe_allow_html=True,
)
