"""Streamlit dashboard for Glossary Search.

Provides a rich UI for searching, browsing, and exploring glossary terms
from the USAREUR-AF maven_training corpus.

Run:  streamlit run apps/glossary_search/dashboard.py --server.port 8507
"""

from __future__ import annotations

import sys
from pathlib import Path

import streamlit as st

# Ensure repo root is on the path for theme import
_REPO_ROOT = Path(__file__).resolve().parent.parent.parent
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))

from apps.theme import (
    GOLD,
    GOLD_DARK,
    GOLD_LIGHT,
    GOLD_PALE,
    GRAY_400,
    GRAY_600,
    NAVY,
    NAVY_DARK,
    NAVY_LIGHT,
    NAVY_PALE,
    WHITE,
    inject_branding,
)

from apps.glossary_search import db

# ---------------------------------------------------------------------------
# Page config
# ---------------------------------------------------------------------------
st.set_page_config(
    page_title="Glossary Search — USAREUR-AF",
    page_icon="\U0001F4D6",
    layout="wide",
    initial_sidebar_state="expanded",
)

inject_branding(
    title="Glossary Search",
    subtitle="USAREUR-AF Operational Data Team",
)

CORPUS_ROOT = Path("/home/dale/Desktop/claude/maven_training")

# ---------------------------------------------------------------------------
# Custom CSS for result cards
# ---------------------------------------------------------------------------
_CARD_CSS = f"""
<style>
.term-card {{
    background: {WHITE};
    border: 1px solid #e0e4ef;
    border-left: 4px solid {NAVY};
    border-radius: 0 4px 4px 0;
    padding: 14px 18px;
    margin-bottom: 10px;
    box-shadow: 0 1px 4px rgba(0,0,0,0.06);
}}
.term-card:hover {{
    border-left-color: {GOLD};
    box-shadow: 0 3px 10px rgba(12,35,64,0.10);
}}
.term-name {{
    font-family: Arial, Helvetica, sans-serif;
    font-size: 16px;
    font-weight: bold;
    color: {NAVY};
    margin-bottom: 4px;
}}
.term-badge {{
    display: inline-block;
    font-size: 10px;
    font-weight: bold;
    letter-spacing: 1px;
    text-transform: uppercase;
    padding: 2px 8px;
    border-radius: 3px;
    margin-left: 8px;
    vertical-align: middle;
}}
.badge-glossary {{ background: {GOLD_PALE}; color: {GOLD_DARK}; }}
.badge-doctrine {{ background: {NAVY_PALE}; color: {NAVY}; }}
.badge-acronym {{ background: #e8f5e9; color: #1a5c28; }}
.badge-concept {{ background: #f3e5f5; color: #502b85; }}
.term-def {{
    font-size: 14px;
    color: {GRAY_600};
    line-height: 1.6;
    margin-top: 6px;
}}
.term-source {{
    font-size: 11px;
    color: {GRAY_400};
    margin-top: 6px;
    font-family: monospace;
}}
mark {{
    background: {GOLD_PALE};
    color: {NAVY_DARK};
    padding: 0 2px;
    border-radius: 2px;
}}
.stat-bar {{
    background: {NAVY_PALE};
    border-radius: 3px;
    height: 20px;
    margin: 4px 0;
}}
.stat-fill {{
    background: linear-gradient(90deg, {NAVY} 0%, {NAVY_LIGHT} 100%);
    height: 100%;
    border-radius: 3px;
    min-width: 2px;
}}
</style>
"""
st.markdown(_CARD_CSS, unsafe_allow_html=True)

# ---------------------------------------------------------------------------
# Ensure DB is initialized
# ---------------------------------------------------------------------------
db.init_db()

# Check if index is populated; if not, prompt reindex
stats = db.get_stats()
if stats["total_terms"] == 0:
    st.info("Index is empty. Go to the **Reindex** tab to build the glossary index.")


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _badge_class(category: str) -> str:
    """Map category to CSS badge class."""
    return {
        "GLOSSARY": "badge-glossary",
        "DOCTRINE": "badge-doctrine",
        "ACRONYM": "badge-acronym",
        "CONCEPT": "badge-concept",
    }.get(category, "badge-concept")


def _highlight(text: str, query: str) -> str:
    """Highlight matching substrings in text (case-insensitive)."""
    if not query or len(query) < 2:
        return text
    # Escape HTML in text first, then inject mark tags
    import html
    safe_text = html.escape(text)
    # Case-insensitive replacement
    import re
    pattern = re.compile(re.escape(html.escape(query)), re.IGNORECASE)
    return pattern.sub(lambda m: f"<mark>{m.group(0)}</mark>", safe_text)


def _render_card(term, query: str = "") -> None:
    """Render a single term as a styled card."""
    badge = _badge_class(term.category)
    name_html = _highlight(term.term, query) if query else term.term
    # Truncate definition for display, keeping full text available
    defn_display = term.definition[:500]
    if len(term.definition) > 500:
        defn_display += "..."
    defn_html = _highlight(defn_display, query) if query else defn_display

    st.markdown(f"""
    <div class="term-card">
        <div class="term-name">
            {name_html}
            <span class="term-badge {badge}">{term.category}</span>
        </div>
        <div class="term-def">{defn_html}</div>
        <div class="term-source">{term.source_file} : line {term.source_line}</div>
    </div>
    """, unsafe_allow_html=True)


# ---------------------------------------------------------------------------
# Sidebar navigation
# ---------------------------------------------------------------------------

with st.sidebar:
    st.markdown("---")
    page = st.radio(
        "Navigation",
        ["Search", "Browse", "Statistics", "Reindex"],
        label_visibility="collapsed",
    )
    st.caption("GLOSSARY SEARCH v1.0")

# ---------------------------------------------------------------------------
# PAGE: Search
# ---------------------------------------------------------------------------

if page == "Search":
    st.markdown("# Glossary Search")
    st.caption("Full-text search across glossary terms, doctrine, and training definitions")

    col1, col2 = st.columns([3, 1])
    with col1:
        query = st.text_input(
            "Search terms and definitions",
            placeholder="e.g., OPDATA, ontology, pipeline, readiness...",
            label_visibility="collapsed",
        )
    with col2:
        cats = ["All Categories"] + [c["category"] for c in db.get_categories()]
        cat_filter = st.selectbox("Category", cats, label_visibility="collapsed")

    if query:
        cat_val = None if cat_filter == "All Categories" else cat_filter
        results, elapsed = db.search_terms(query=query, category=cat_val, limit=50)

        st.markdown(
            f"**{len(results)}** results in **{elapsed:.1f} ms**",
        )
        st.markdown("---")

        if not results:
            st.warning("No matching terms found. Try a different search query.")
        else:
            for t in results:
                _render_card(t, query)
    else:
        # Show recent / example searches
        st.markdown("---")
        st.markdown("### Quick Searches")
        example_terms = ["Ontology", "Pipeline", "SITREP", "AIP", "ETL", "Dashboard", "Object Type", "OSDK"]
        cols = st.columns(4)
        for i, ex in enumerate(example_terms):
            with cols[i % 4]:
                if st.button(ex, key=f"qs_{ex}", use_container_width=True):
                    st.session_state["search_query"] = ex
                    st.rerun()

# ---------------------------------------------------------------------------
# PAGE: Browse
# ---------------------------------------------------------------------------

elif page == "Browse":
    st.markdown("# Browse Terms")
    st.caption("Alphabetical term browser with category filtering")

    categories = db.get_categories()
    tab_names = ["All"] + [c["category"] for c in categories]
    tabs = st.tabs(tab_names)

    for i, tab in enumerate(tabs):
        with tab:
            cat_val = None if i == 0 else tab_names[i]
            terms = db.get_all_terms(category=cat_val)

            if not terms:
                st.info("No terms in this category. Run the indexer first.")
                continue

            st.markdown(f"**{len(terms)} terms**")
            st.markdown("---")

            # Alphabetical display with letter headers
            current_letter = ""
            for t in terms:
                first = t.term[0].upper() if t.term else "#"
                if not first.isalpha():
                    first = "#"
                if first != current_letter:
                    current_letter = first
                    st.markdown(f"### {current_letter}")
                _render_card(t)

# ---------------------------------------------------------------------------
# PAGE: Statistics
# ---------------------------------------------------------------------------

elif page == "Statistics":
    st.markdown("# Index Statistics")
    st.caption("Coverage metrics for the glossary index")

    stats = db.get_stats()

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Terms", stats["total_terms"])
    with col2:
        st.metric("Source Files", stats["source_files"])
    with col3:
        st.metric("Categories", len(stats["by_category"]))

    st.markdown("---")

    # Category breakdown
    st.markdown("### Terms by Category")
    if stats["by_category"]:
        max_count = max(c["count"] for c in stats["by_category"])
        for cat_info in stats["by_category"]:
            cat = cat_info["category"]
            cnt = cat_info["count"]
            pct = (cnt / max_count * 100) if max_count > 0 else 0
            badge = _badge_class(cat)

            col_a, col_b, col_c = st.columns([2, 5, 1])
            with col_a:
                st.markdown(
                    f'<span class="term-badge {badge}" style="font-size:12px">{cat}</span>',
                    unsafe_allow_html=True,
                )
            with col_b:
                st.markdown(
                    f'<div class="stat-bar"><div class="stat-fill" style="width:{pct}%"></div></div>',
                    unsafe_allow_html=True,
                )
            with col_c:
                st.markdown(f"**{cnt}**")

    st.markdown("---")

    # Top source files
    st.markdown("### Top Source Files")
    all_terms = db.get_all_terms()
    if all_terms:
        from collections import Counter
        file_counts = Counter(t.source_file for t in all_terms)
        for fname, cnt in file_counts.most_common(10):
            st.markdown(f"- `{fname}` — **{cnt}** terms")

# ---------------------------------------------------------------------------
# PAGE: Reindex
# ---------------------------------------------------------------------------

elif page == "Reindex":
    st.markdown("# Reindex Glossary")
    st.caption("Rebuild the search index from source markdown files")

    st.markdown(f"**Corpus root:** `{CORPUS_ROOT}`")

    current_stats = db.get_stats()
    st.markdown(f"**Current index:** {current_stats['total_terms']} terms from {current_stats['source_files']} files")

    st.markdown("---")

    if st.button("Rebuild Index", type="primary", use_container_width=True):
        if not CORPUS_ROOT.is_dir():
            st.error(f"Corpus root not found: {CORPUS_ROOT}")
        else:
            progress = st.progress(0, text="Clearing existing index...")
            progress.progress(10, text="Parsing markdown files...")

            count = db.reindex(CORPUS_ROOT)

            progress.progress(90, text="Finalizing...")
            progress.progress(100, text="Complete!")

            st.success(f"Indexed **{count}** terms from the maven_training corpus.")

            # Show updated stats
            new_stats = db.get_stats()
            col1, col2 = st.columns(2)
            with col1:
                st.metric("Total Terms", new_stats["total_terms"])
            with col2:
                st.metric("Source Files", new_stats["source_files"])

# ---------------------------------------------------------------------------
# Footer
# ---------------------------------------------------------------------------
st.markdown(
    '<div class="app-footer">USAREUR-AF OPERATIONAL DATA TEAM — GLOSSARY SEARCH</div>',
    unsafe_allow_html=True,
)
