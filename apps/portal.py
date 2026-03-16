"""MSS Training Analytics Portal — Unified landing page.

Connects all 3 apps with cross-app KPIs and navigation.
Run: streamlit run apps/portal.py --server.port 8500
"""

from __future__ import annotations

import sys
from datetime import date
from pathlib import Path

# Ensure apps/ is on sys.path for imports
_app_dir = Path(__file__).resolve().parent
if str(_app_dir) not in sys.path:
    sys.path.insert(0, str(_app_dir))

import streamlit as st

st.set_page_config(
    page_title="MSS Training Analytics Portal",
    page_icon="\U0001F3DB",
    layout="wide",
    initial_sidebar_state="collapsed",
)

from theme import inject_branding, INSIGNIA_IMG, NAVY, NAVY_DARK, GOLD, GOLD_LIGHT, GOLD_DARK, GRAY_400, GRAY_700

inject_branding("MSS Training Analytics Portal")

# ---------------------------------------------------------------------------
# Load summary data from each app's DB directly
# ---------------------------------------------------------------------------
try:
    from readiness_tracker.db import (
        SessionLocal as RT_Session, Trainee, Completion, init_db as rt_init,
        get_funnel_data, get_unit_summary,
    )
    from exam_analytics.db import (
        SessionLocal as EA_Session, ExamSession, ExamResult,
        init_db as ea_init, cross_cohort_comparison,
    )
    from aar_aggregator.db import (
        SessionLocal as AAR_Session, AAR,
        init_db as aar_init, aar_summary_stats,
    )
    IMPORTS_OK = True
except ImportError:
    IMPORTS_OK = False


@st.cache_data(ttl=60)
def load_rt_stats():
    rt_init()
    db = RT_Session()
    try:
        total = db.query(Trainee).count()
        go_completions = db.query(Completion).filter(Completion.result == "GO").count()
        funnel = get_funnel_data(db)
        units = get_unit_summary(db)
        return {
            "total_trainees": total,
            "go_completions": go_completions,
            "units": len(units),
            "funnel": funnel,
        }
    finally:
        db.close()


@st.cache_data(ttl=60)
def load_ea_stats():
    ea_init()
    db = EA_Session()
    try:
        sessions = db.query(ExamSession).count()
        results = db.query(ExamResult).count()
        passing = db.query(ExamResult).filter(ExamResult.result == "PASS").count()
        pass_rate = round(passing / results * 100, 1) if results else 0
        return {
            "sessions": sessions,
            "results": results,
            "pass_rate": pass_rate,
        }
    finally:
        db.close()


@st.cache_data(ttl=60)
def load_aar_stats():
    aar_init()
    db = AAR_Session()
    try:
        return aar_summary_stats(db)
    finally:
        db.close()


# ---------------------------------------------------------------------------
# Header
# ---------------------------------------------------------------------------
_insignia_tag = INSIGNIA_IMG.format(
    'style="width:64px; height:auto; vertical-align:middle; margin-right:16px; '
    'filter: drop-shadow(0 2px 6px rgba(0,0,0,0.15));"'
)
st.markdown(f"""
<div style="text-align: center; padding: 1.5rem 0;">
    <div style="font-family: Arial, Helvetica, sans-serif; font-size: 10px; font-weight: bold;
                letter-spacing: 3px; color: {GOLD}; text-transform: uppercase; margin-bottom: 8px;">
        United States Army Europe and Africa
    </div>
    <div style="display: flex; align-items: center; justify-content: center; gap: 12px;">
        {_insignia_tag}
        <div>
            <h1 style="margin-bottom: 0; border: none; font-family: Arial, Helvetica, sans-serif;
                       color: {NAVY}; font-size: 28px; text-align: left;">MSS Training Analytics Portal</h1>
            <p style="color: {GRAY_400}; font-size: 12px; letter-spacing: 1px; text-transform: uppercase;
                      margin-top: 4px; text-align: left;">
                Operational Data Team &mdash; Training Readiness Suite v2.0
            </p>
        </div>
        {_insignia_tag}
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

if not IMPORTS_OK:
    st.error("Could not import app modules. Run from repo root: `streamlit run apps/portal.py`")
    st.stop()

# ---------------------------------------------------------------------------
# Cross-app KPI banner
# ---------------------------------------------------------------------------
rt = load_rt_stats()
ea = load_ea_stats()
aar = load_aar_stats()

c1, c2, c3, c4, c5, c6 = st.columns(6)
c1.metric("Trainees Tracked", rt["total_trainees"])
c2.metric("GO Completions", rt["go_completions"])
c3.metric("Exam Sessions", ea["sessions"])
c4.metric("Exam Pass Rate", f"{ea['pass_rate']}%")
c5.metric("AARs Filed", aar.get("total_aars", 0))
c6.metric("Overall GO Rate", f"{aar.get('overall_go_rate', 0)}%")

st.markdown("---")

# ---------------------------------------------------------------------------
# App cards
# ---------------------------------------------------------------------------
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    ### Training Readiness Tracker
    Track soldier/unit completion across the MSS TM-10 to TM-50L prereq chain.

    **Key Features:**
    - Commander's RAG heatmap
    - Training pipeline bottleneck analysis
    - Training progression funnel
    - Individual trainee lookup with prereq visualization
    - Unit drill-down with readiness scoring
    - CSV roster and completion upload
    """)
    st.markdown(f"**{rt['total_trainees']}** trainees across **{rt['units']}** units")
    st.link_button("Open Readiness Tracker", "http://localhost:8501", use_container_width=True)
    st.caption("API: http://localhost:8001/docs")

with col2:
    st.markdown("""
    ### Exam Analytics Dashboard
    Analyze pre/post exam results, compute gain scores, validate test items.

    **Key Features:**
    - Cross-cohort comparison with trend analysis
    - Normalized gain score computation
    - Item discrimination analysis (point-biserial)
    - Question-level improvement waterfall
    - Score distribution with box plots
    - Per-question difficulty ranking
    """)
    st.markdown(f"**{ea['sessions']}** sessions, **{ea['results']}** results, **{ea['pass_rate']}%** pass rate")
    st.link_button("Open Exam Analytics", "http://localhost:8502", use_container_width=True)
    st.caption("API: http://localhost:8002/docs")

with col3:
    st.markdown("""
    ### AAR Aggregator
    Ingest After-Action Reviews, surface trends, track systemic issues.

    **Key Features:**
    - Priority matrix (frequency x severity)
    - Keyword frequency analysis
    - GO/NO_GO rate tracking over time
    - WFF category co-occurrence analysis
    - Recurring issue detection
    - Curriculum discrepancy tracking
    """)
    total_aars = aar.get("total_aars", 0)
    total_trained = aar.get("total_students_trained", 0)
    st.markdown(f"**{total_aars}** AARs, **{total_trained}** students trained")
    st.link_button("Open AAR Aggregator", "http://localhost:8503", use_container_width=True)
    st.caption("API: http://localhost:8003/docs")

st.markdown("---")

# ---------------------------------------------------------------------------
# Quick-start instructions
# ---------------------------------------------------------------------------
with st.expander("Quick Start / Startup Commands"):
    st.code("""# From repo root:

# Seed all databases (first time only)
python -m apps.readiness_tracker.seed
python -m apps.exam_analytics.seed
python -m apps.aar_aggregator.seed

# Start APIs
uvicorn apps.readiness_tracker.api:app --port 8001 &
uvicorn apps.exam_analytics.api:app --port 8002 &
uvicorn apps.aar_aggregator.api:app --port 8003 &

# Start dashboards
streamlit run apps/readiness_tracker/dashboard.py --server.port 8501 &
streamlit run apps/exam_analytics/dashboard.py --server.port 8502 &
streamlit run apps/aar_aggregator/dashboard.py --server.port 8503 &

# Start this portal
streamlit run apps/portal.py --server.port 8500
""", language="bash")

st.caption(f"Portal generated {date.today().isoformat()} | MSS Training Analytics Suite v2.0")
