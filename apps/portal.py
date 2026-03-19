"""MSS Training Analytics Portal — Unified landing page.

Connects all 15 apps with cross-app KPIs and navigation.
Run: streamlit run apps/portal.py --server.port 8500
"""

from __future__ import annotations

import logging
import os
import sys

logger = logging.getLogger(__name__)
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

from theme import (
    inject_branding, INSIGNIA_IMG, NAVY, NAVY_DARK, NAVY_LIGHT, NAVY_MID,
    GOLD, GOLD_LIGHT, GOLD_DARK, GRAY_400, GRAY_700, RAG_GREEN, RAG_AMBER,
    RAG_RED, WARNING_RED, CAUTION_AMBER, NOTE_TEAL,
)

inject_branding("MSS Training Analytics Portal")

# ---------------------------------------------------------------------------
# Load summary data from core analytics apps
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
    CORE_IMPORTS_OK = True
except ImportError:
    CORE_IMPORTS_OK = False

# Optional imports for extended apps — portal works even if some aren't ready
_ext_stats = {}

try:
    from progress_tracker.db import (
        SessionLocal as PT_Session, init_db as pt_init, Milestone,
    )
    pt_init()
    _db = PT_Session()
    _ext_stats["milestones"] = _db.query(Milestone).count()
    _ext_stats["overdue"] = _db.query(Milestone).filter(Milestone.status == "OVERDUE").count()
    _db.close()
except Exception:
    logger.warning("Failed to load progress_tracker stats", exc_info=True)

try:
    from mtt_scheduler.db import (
        SessionLocal as MTT_Session, init_db as mtt_init, Event, Enrollment,
    )
    mtt_init()
    _db = MTT_Session()
    _ext_stats["events"] = _db.query(Event).count()
    _ext_stats["enrollments"] = _db.query(Enrollment).count()
    _db.close()
except Exception:
    logger.warning("Failed to load mtt_scheduler stats", exc_info=True)

try:
    from data_quality.db import (
        SessionLocal as DQ_Session, init_db as dq_init, Pipeline, Alert,
    )
    dq_init()
    _db = DQ_Session()
    _ext_stats["pipelines"] = _db.query(Pipeline).count()
    _ext_stats["active_alerts"] = _db.query(Alert).filter(Alert.acknowledged == False).count()
    _db.close()
except Exception:
    logger.warning("Failed to load data_quality stats", exc_info=True)

try:
    from glossary_search.db import (
        SessionLocal as GS_Session, init_db as gs_init, Term,
    )
    gs_init()
    _db = GS_Session()
    _ext_stats["glossary_terms"] = _db.query(Term).count()
    _db.close()
except Exception:
    logger.warning("Failed to load glossary_search stats", exc_info=True)

try:
    from instructor_manager.db import (
        SessionLocal as IM_Session, init_db as im_init,
        Instructor, Certification, get_expiring_certifications, get_coverage_matrix,
    )
    im_init()
    _db = IM_Session()
    _ext_stats["instructors"] = _db.query(Instructor).filter(Instructor.status == "ACTIVE").count()
    _ext_stats["expiring_certs"] = len(get_expiring_certifications(30, _db))
    coverage = get_coverage_matrix(_db)
    _ext_stats["coverage_gaps"] = sum(1 for c in coverage if c["certified_count"] == 0)
    _db.close()
except Exception:
    logger.warning("Failed to load instructor_manager stats", exc_info=True)

try:
    from enrollment_manager.db import (
        SessionLocal as EM_Session, init_db as em_init, get_enrollment_stats,
    )
    em_init()
    _db = EM_Session()
    em_stats = get_enrollment_stats(_db)
    _ext_stats["classes"] = em_stats.get("total_classes", 0)
    _ext_stats["enrolled"] = em_stats.get("total_enrolled", 0)
    _ext_stats["waitlisted"] = em_stats.get("total_waitlisted", 0)
    _ext_stats["fill_rate"] = em_stats.get("avg_fill_rate", 0)
    _db.close()
except Exception:
    logger.warning("Failed to load enrollment_manager stats", exc_info=True)

try:
    from curriculum_tracker.db import (
        SessionLocal as CT_Session, init_db as ct_init,
        Document, get_overdue_reviews, get_stale_documents,
    )
    ct_init()
    _db = CT_Session()
    _ext_stats["tracked_docs"] = _db.query(Document).count()
    _ext_stats["overdue_reviews"] = len(get_overdue_reviews(_db))
    _ext_stats["stale_docs"] = len(get_stale_documents(90, _db))
    _db.close()
except Exception:
    logger.warning("Failed to load curriculum_tracker stats", exc_info=True)

try:
    from lessons_learned.db import (
        SessionLocal as LL_Session, init_db as ll_init,
        get_pipeline_stats, get_action_item_status,
    )
    ll_init()
    _db = LL_Session()
    ll_stats = get_pipeline_stats(_db)
    ai_status = get_action_item_status(_db)
    _ext_stats["lessons"] = ll_stats.get("total_lessons", 0)
    _ext_stats["open_actions"] = ai_status.get("OPEN", 0) + ai_status.get("IN_PROGRESS", 0)
    _db.close()
except Exception:
    logger.warning("Failed to load lessons_learned stats", exc_info=True)


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
                Operational Data Team &mdash; MSS Training Suite v4.0
            </p>
        </div>
        {_insignia_tag}
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("---")

if not CORE_IMPORTS_OK:
    st.error("Could not import core app modules. Run from repo root: `streamlit run apps/portal.py`")
    st.stop()

# ---------------------------------------------------------------------------
# Cross-app KPI banner
# ---------------------------------------------------------------------------
rt = load_rt_stats()
ea = load_ea_stats()
aar = load_aar_stats()

c1, c2, c3, c4, c5, c6, c7, c8 = st.columns(8)
c1.metric("Trainees", rt["total_trainees"])
c2.metric("GO Completions", rt["go_completions"])
c3.metric("Exam Pass Rate", f"{ea['pass_rate']}%")
c4.metric("AARs Filed", aar.get("total_aars", 0))
c5.metric("MTT Events", _ext_stats.get("events", "--"))
c6.metric("Pipelines", _ext_stats.get("pipelines", "--"))
c7.metric("Active Alerts", _ext_stats.get("active_alerts", "--"))
c8.metric("Glossary Terms", _ext_stats.get("glossary_terms", "--"))

# Second KPI row — new apps
d1, d2, d3, d4, d5, d6, d7 = st.columns(7)
d1.metric("Instructors", _ext_stats.get("instructors", "--"))
d2.metric("Certs Expiring", _ext_stats.get("expiring_certs", "--"))
d3.metric("Classes", _ext_stats.get("classes", "--"))
d4.metric("Waitlisted", _ext_stats.get("waitlisted", "--"))
d5.metric("Tracked Docs", _ext_stats.get("tracked_docs", "--"))
d6.metric("Lessons", _ext_stats.get("lessons", "--"))
d7.metric("Open Actions", _ext_stats.get("open_actions", "--"))

st.markdown("---")


# ---------------------------------------------------------------------------
# App directory — all 15 apps as icon tiles on one page
# ---------------------------------------------------------------------------
_APPS = [
    {"icon": "\U0001F3AF", "name": "Readiness Tracker",       "desc": "Soldier/unit completion & RAG heatmap",   "url": os.environ.get("READINESS_TRACKER_APP_URL", "http://localhost:8501"), "api": os.environ.get("READINESS_TRACKER_API_URL", "http://localhost:8001") + "/docs"},
    {"icon": "\U0001F4DD", "name": "Exam Analytics",           "desc": "Pre/post scores, gain, item analysis",    "url": os.environ.get("EXAM_ANALYTICS_APP_URL", "http://localhost:8502"), "api": os.environ.get("EXAM_ANALYTICS_API_URL", "http://localhost:8002") + "/docs"},
    {"icon": "\U0001F4CB", "name": "AAR Aggregator",           "desc": "After-Action trends & systemic issues",   "url": os.environ.get("AAR_AGGREGATOR_APP_URL", "http://localhost:8503"), "api": os.environ.get("AAR_AGGREGATOR_API_URL", "http://localhost:8003") + "/docs"},
    {"icon": "\U0001F4C8", "name": "Progress Tracker",         "desc": "Individual timelines & stalled alerts",   "url": os.environ.get("PROGRESS_TRACKER_APP_URL", "http://localhost:8504"), "api": os.environ.get("PROGRESS_TRACKER_API_URL", "http://localhost:8004") + "/docs"},
    {"icon": "\U0001F4C5", "name": "MTT Scheduler",            "desc": "Mobile Training Team event calendar",     "url": os.environ.get("MTT_SCHEDULER_APP_URL", "http://localhost:8505"), "api": os.environ.get("MTT_SCHEDULER_API_URL", "http://localhost:8005") + "/docs"},
    {"icon": "\U0001F517", "name": "Cross-Ref Validator",      "desc": "Broken links, stale refs, prereq audit",  "url": os.environ.get("XREF_VALIDATOR_APP_URL", "http://localhost:8506"), "api": os.environ.get("XREF_VALIDATOR_API_URL", "http://localhost:8006") + "/docs"},
    {"icon": "\U0001F4D6", "name": "Glossary Search",          "desc": "Full-text term & doctrine search",        "url": os.environ.get("GLOSSARY_SEARCH_APP_URL", "http://localhost:8507"), "api": os.environ.get("GLOSSARY_SEARCH_API_URL", "http://localhost:8007") + "/docs"},
    {"icon": "\U0001F4E6", "name": "Offline Packager",         "desc": "ZIP bundles for DDIL environments",       "url": os.environ.get("OFFLINE_PACKAGER_APP_URL", "http://localhost:8508"), "api": os.environ.get("OFFLINE_PACKAGER_API_URL", "http://localhost:8008") + "/docs"},
    {"icon": "\U0001F504", "name": "SharePoint Sync",          "desc": "Change detection & sync packages",        "url": os.environ.get("SHAREPOINT_SYNC_APP_URL", "http://localhost:8509"), "api": os.environ.get("SHAREPOINT_SYNC_API_URL", "http://localhost:8009") + "/docs"},
    {"icon": "\U0001F6E1", "name": "Data Quality Monitor",     "desc": "Pipeline health, alerts & scorecards",    "url": os.environ.get("DATA_QUALITY_APP_URL", "http://localhost:8510"), "api": os.environ.get("DATA_QUALITY_API_URL", "http://localhost:8010") + "/docs"},
    {"icon": "\U0001F9D1\u200D\U0001F3EB", "name": "Instructor Manager", "desc": "Certs, coverage matrix & workload",  "url": os.environ.get("INSTRUCTOR_MANAGER_APP_URL", "http://localhost:8511"), "api": os.environ.get("INSTRUCTOR_MANAGER_API_URL", "http://localhost:8011") + "/docs"},
    {"icon": "\U0001F4CB", "name": "Enrollment Manager",       "desc": "Class rosters, waitlists & seat allocation", "url": os.environ.get("ENROLLMENT_MANAGER_APP_URL", "http://localhost:8512"), "api": os.environ.get("ENROLLMENT_MANAGER_API_URL", "http://localhost:8012") + "/docs"},
    {"icon": "\U0001F4DA", "name": "Curriculum Tracker",       "desc": "Doc versions, review cycles & freshness", "url": os.environ.get("CURRICULUM_TRACKER_APP_URL", "http://localhost:8513"), "api": os.environ.get("CURRICULUM_TRACKER_API_URL", "http://localhost:8013") + "/docs"},
    {"icon": "\U0001F4A1", "name": "Lessons Learned",          "desc": "TTP/WFF taxonomy & action items",         "url": os.environ.get("LESSONS_LEARNED_APP_URL", "http://localhost:8514"), "api": os.environ.get("LESSONS_LEARNED_API_URL", "http://localhost:8014") + "/docs"},
    {"icon": "\U00002B50", "name": "CG Training Metrics",      "desc": "Executive scorecard & risk register",     "url": os.environ.get("TRAINING_METRICS_APP_URL", "http://localhost:8515"), "api": os.environ.get("TRAINING_METRICS_API_URL", "http://localhost:8015") + "/docs"},
]

# Render icon tile grid — 5 columns x 3 rows
st.markdown(f"""
<h2 style="font-family:Arial,Helvetica,sans-serif; color:{NAVY}; border-bottom:2px solid {GOLD_DARK};
           padding-bottom:6px; font-size:18px;">Applications</h2>
""", unsafe_allow_html=True)

_COLS_PER_ROW = 5
for row_start in range(0, len(_APPS), _COLS_PER_ROW):
    row_apps = _APPS[row_start:row_start + _COLS_PER_ROW]
    cols = st.columns(_COLS_PER_ROW)
    for i, app in enumerate(row_apps):
        with cols[i]:
            st.markdown(f"""
            <a href="{app['url']}" target="_blank" style="text-decoration:none; display:block;">
                <div style="border:1px solid #e0e4ef; border-radius:6px; padding:18px 12px;
                            text-align:center; background:white; min-height:160px;
                            box-shadow:0 1px 5px rgba(0,0,0,0.06);
                            transition: box-shadow 0.15s, border-color 0.15s;">
                    <div style="font-size:36px; margin-bottom:8px;">{app['icon']}</div>
                    <div style="font-family:Arial,Helvetica,sans-serif; font-size:13px;
                                font-weight:bold; color:{NAVY}; margin-bottom:4px;">{app['name']}</div>
                    <div style="font-size:11px; color:{GRAY_400}; line-height:1.3;">{app['desc']}</div>
                </div>
            </a>
            """, unsafe_allow_html=True)
            # API docs link below the tile
            st.markdown(f"""
            <div style="text-align:center; margin-top:4px; margin-bottom:16px;">
                <a href="{app['api']}" target="_blank"
                   style="font-size:10px; color:{GRAY_400}; text-decoration:none;">API Docs</a>
            </div>
            """, unsafe_allow_html=True)

st.markdown("---")

# ---------------------------------------------------------------------------
# Quick-start instructions
# ---------------------------------------------------------------------------
with st.expander("Quick Start / Startup Commands"):
    st.code("""# From repo root:

# ============================================================
# Seed all databases (first time only)
# ============================================================
python -m apps.readiness_tracker.seed
python -m apps.exam_analytics.seed
python -m apps.aar_aggregator.seed
python -m apps.progress_tracker.seed
python -m apps.mtt_scheduler.seed
python -m apps.data_quality.seed
python -m apps.glossary_search.seed
python -m apps.xref_validator.seed
python -m apps.sharepoint_sync.seed
python -m apps.offline_packager.seed
python -m apps.instructor_manager.seed
python -m apps.enrollment_manager.seed
python -m apps.curriculum_tracker.seed
python -m apps.lessons_learned.seed
python -m apps.training_metrics.seed    # seed last — aggregates from others

# ============================================================
# Start APIs
# ============================================================
uvicorn apps.readiness_tracker.api:app --port 8001 &
uvicorn apps.exam_analytics.api:app --port 8002 &
uvicorn apps.aar_aggregator.api:app --port 8003 &
uvicorn apps.progress_tracker.api:app --port 8004 &
uvicorn apps.mtt_scheduler.api:app --port 8005 &
uvicorn apps.xref_validator.api:app --port 8006 &
uvicorn apps.glossary_search.api:app --port 8007 &
uvicorn apps.offline_packager.api:app --port 8008 &
uvicorn apps.sharepoint_sync.api:app --port 8009 &
uvicorn apps.data_quality.api:app --port 8010 &
uvicorn apps.instructor_manager.api:app --port 8011 &
uvicorn apps.enrollment_manager.api:app --port 8012 &
uvicorn apps.curriculum_tracker.api:app --port 8013 &
uvicorn apps.lessons_learned.api:app --port 8014 &
uvicorn apps.training_metrics.api:app --port 8015 &

# ============================================================
# Start dashboards
# ============================================================
streamlit run apps/readiness_tracker/dashboard.py --server.port 8501 &
streamlit run apps/exam_analytics/dashboard.py --server.port 8502 &
streamlit run apps/aar_aggregator/dashboard.py --server.port 8503 &
streamlit run apps/progress_tracker/dashboard.py --server.port 8504 &
streamlit run apps/mtt_scheduler/dashboard.py --server.port 8505 &
streamlit run apps/xref_validator/dashboard.py --server.port 8506 &
streamlit run apps/glossary_search/dashboard.py --server.port 8507 &
streamlit run apps/offline_packager/dashboard.py --server.port 8508 &
streamlit run apps/sharepoint_sync/dashboard.py --server.port 8509 &
streamlit run apps/data_quality/dashboard.py --server.port 8510 &
streamlit run apps/instructor_manager/dashboard.py --server.port 8511 &
streamlit run apps/enrollment_manager/dashboard.py --server.port 8512 &
streamlit run apps/curriculum_tracker/dashboard.py --server.port 8513 &
streamlit run apps/lessons_learned/dashboard.py --server.port 8514 &
streamlit run apps/training_metrics/dashboard.py --server.port 8515 &

# ============================================================
# Start this portal
# ============================================================
streamlit run apps/portal.py --server.port 8500
""", language="bash")

st.caption(f"Portal generated {date.today().isoformat()} | MSS Training Suite v4.0 — 15 apps")
