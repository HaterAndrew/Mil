"""Generate realistic demo data for the Data Quality Monitor.

Run directly:  python -m apps.data_quality.seed
"""

from __future__ import annotations

import random
from datetime import datetime, timedelta, timezone

from .db import (
    AlertRow,
    MetricRow,
    PipelineRow,
    PipelineStatus,
    evaluate_metric,
    init_db,
    get_db,
)
from .models import AlertSeverity, MetricType

# Deterministic for reproducibility
random.seed(42)

# ---------------------------------------------------------------------------
# Pipeline definitions
# ---------------------------------------------------------------------------
PIPELINES = [
    {
        "name": "MSS Roster Sync",
        "description": "Synchronizes unit roster data from IPPS-A into Foundry for manning dashboards.",
        "owner": "SGT Martinez",
        "schedule": "daily 0600Z",
        "source_system": "IPPS-A",
        "target_system": "Foundry",
    },
    {
        "name": "Training Completion ETL",
        "description": "Extracts training completion records from DTMS and loads into the analytics pipeline.",
        "owner": "SSG Williams",
        "schedule": "daily 0800Z",
        "source_system": "DTMS",
        "target_system": "Foundry",
    },
    {
        "name": "SITREP Aggregation",
        "description": "Aggregates situation reports from subordinate units into the COP dataset.",
        "owner": "CPT Johnson",
        "schedule": "every 4h",
        "source_system": "CPOF",
        "target_system": "Foundry",
    },
    {
        "name": "Personnel Data Feed",
        "description": "Ingests personnel strength and readiness data for theater-level reporting.",
        "owner": "SFC Adams",
        "schedule": "daily 0200Z",
        "source_system": "eMILPO",
        "target_system": "Foundry",
    },
    {
        "name": "Equipment Readiness Pipeline",
        "description": "Pulls equipment readiness and maintenance data from GCSS-Army.",
        "owner": "CW2 Thompson",
        "schedule": "daily 0400Z",
        "source_system": "GCSS-Army",
        "target_system": "Foundry",
    },
    {
        "name": "Intelligence Fusion Feed",
        "description": "Fuses multi-source intelligence products for the operational picture.",
        "owner": "MAJ Davis",
        "schedule": "every 2h",
        "source_system": "DCGS-A",
        "target_system": "Foundry",
    },
]

# Profile defines how each pipeline's metrics behave over 90 days.
# base: nominal value; drift: per-day trend; noise: random spread; fail_window: (start_day, end_day) of degradation
PROFILES = {
    "MSS Roster Sync": {
        "quality": "healthy",
        MetricType.COMPLETENESS: {"base": 99.5, "threshold": 95.0, "noise": 0.5},
        MetricType.TIMELINESS: {"base": 120, "threshold": 300, "noise": 30},
        MetricType.ACCURACY: {"base": 99.8, "threshold": 98.0, "noise": 0.2},
        MetricType.VOLUME: {"base": 5000, "threshold": 4500, "noise": 300},
    },
    "Training Completion ETL": {
        "quality": "healthy",
        MetricType.COMPLETENESS: {"base": 98.0, "threshold": 95.0, "noise": 1.5},
        MetricType.TIMELINESS: {"base": 200, "threshold": 300, "noise": 40},
        MetricType.ACCURACY: {"base": 99.0, "threshold": 97.0, "noise": 0.5},
        MetricType.VOLUME: {"base": 12000, "threshold": 10000, "noise": 1500},
    },
    "SITREP Aggregation": {
        "quality": "degraded",
        MetricType.COMPLETENESS: {"base": 94.0, "threshold": 95.0, "noise": 3.0},
        MetricType.TIMELINESS: {"base": 280, "threshold": 300, "noise": 60},
        MetricType.FRESHNESS: {"base": 3.5, "threshold": 4.0, "noise": 1.0},
        MetricType.VOLUME: {"base": 800, "threshold": 750, "noise": 200},
    },
    "Personnel Data Feed": {
        "quality": "healthy",
        MetricType.COMPLETENESS: {"base": 99.0, "threshold": 95.0, "noise": 0.8},
        MetricType.TIMELINESS: {"base": 150, "threshold": 300, "noise": 25},
        MetricType.ACCURACY: {"base": 99.5, "threshold": 98.0, "noise": 0.3},
        MetricType.VOLUME: {"base": 25000, "threshold": 22000, "noise": 2000},
    },
    "Equipment Readiness Pipeline": {
        "quality": "degraded",
        MetricType.COMPLETENESS: {"base": 96.0, "threshold": 95.0, "noise": 2.5},
        MetricType.TIMELINESS: {"base": 250, "threshold": 300, "noise": 80},
        MetricType.ACCURACY: {"base": 97.5, "threshold": 98.0, "noise": 1.5},
        MetricType.VOLUME: {"base": 8000, "threshold": 7500, "noise": 1000},
    },
    "Intelligence Fusion Feed": {
        "quality": "failed",
        MetricType.COMPLETENESS: {"base": 88.0, "threshold": 95.0, "noise": 5.0},
        MetricType.TIMELINESS: {"base": 400, "threshold": 300, "noise": 100},
        MetricType.FRESHNESS: {"base": 5.0, "threshold": 2.0, "noise": 2.0},
        MetricType.VOLUME: {"base": 3000, "threshold": 5000, "noise": 1500},
    },
}


def _gen_value(cfg: dict, day: int, total_days: int = 90) -> float:
    """Generate a metric value with noise and optional degradation."""
    base = cfg["base"]
    noise = cfg["noise"]
    val = base + random.gauss(0, noise)
    return round(val, 2)


def seed() -> None:
    """Populate the database with demo pipelines, metrics, and alerts."""
    init_db()

    with get_db() as db:
        # Clear existing data for idempotent re-seeding
        db.query(AlertRow).delete()
        db.query(MetricRow).delete()
        db.query(PipelineRow).delete()
        db.flush()

        now = datetime.now(timezone.utc)
        pipe_map: dict[str, PipelineRow] = {}

        # Create pipelines
        for pdef in PIPELINES:
            row = PipelineRow(**pdef)
            db.add(row)
            db.flush()
            db.refresh(row)
            pipe_map[pdef["name"]] = row

        # Generate 90 days of metric history per pipeline
        for pname, profile in PROFILES.items():
            pipe = pipe_map[pname]
            quality = profile["quality"]

            for day_offset in range(90, 0, -1):
                ts = now - timedelta(days=day_offset, hours=random.randint(0, 6))

                for mt in [MetricType.COMPLETENESS, MetricType.TIMELINESS,
                           MetricType.ACCURACY, MetricType.FRESHNESS, MetricType.VOLUME]:
                    if mt not in profile:
                        continue

                    cfg = profile[mt]
                    val = _gen_value(cfg, 90 - day_offset)

                    # Inject degradation patterns
                    if quality == "degraded" and day_offset <= 14:
                        # Recent degradation: shift metrics toward thresholds
                        val = val * 0.97 if mt in (MetricType.COMPLETENESS, MetricType.ACCURACY) else val * 1.15
                        val = round(val, 2)
                    elif quality == "failed" and day_offset <= 7:
                        # Active failure: push metrics well past thresholds
                        if mt in (MetricType.COMPLETENESS, MetricType.ACCURACY):
                            val = round(cfg["threshold"] * random.uniform(0.75, 0.90), 2)
                        elif mt in (MetricType.TIMELINESS, MetricType.FRESHNESS):
                            val = round(cfg["threshold"] * random.uniform(1.5, 2.5), 2)
                        elif mt == MetricType.VOLUME:
                            val = round(cfg["threshold"] * random.uniform(0.2, 0.45), 2)

                    threshold = cfg["threshold"]
                    status = evaluate_metric(val, threshold, mt.value)

                    metric = MetricRow(
                        pipeline_id=pipe.id,
                        metric_type=mt.value,
                        value=val,
                        threshold=threshold,
                        status=status.value,
                        timestamp=ts,
                    )
                    db.add(metric)

            # Update pipeline status based on quality profile
            if quality == "failed":
                pipe.status = PipelineStatus.FAILED.value
            elif quality == "degraded":
                pipe.status = PipelineStatus.DEGRADED.value
            else:
                pipe.status = PipelineStatus.HEALTHY.value

            # Set last_run / last_success
            pipe.last_run = now - timedelta(hours=random.randint(1, 12))
            if quality != "failed":
                pipe.last_success = pipe.last_run
            else:
                pipe.last_success = now - timedelta(days=3)

        db.flush()

        # Generate alerts — mix of severities across pipelines
        alert_configs = [
            # Intelligence Fusion Feed — recent failures
            ("Intelligence Fusion Feed", MetricType.COMPLETENESS, 82.3, 95.0, AlertSeverity.CRITICAL, 0.5),
            ("Intelligence Fusion Feed", MetricType.TIMELINESS, 650.0, 300.0, AlertSeverity.CRITICAL, 1.2),
            ("Intelligence Fusion Feed", MetricType.FRESHNESS, 5.8, 2.0, AlertSeverity.CRITICAL, 2.0),
            ("Intelligence Fusion Feed", MetricType.VOLUME, 1200.0, 5000.0, AlertSeverity.CRITICAL, 0.8),
            ("Intelligence Fusion Feed", MetricType.COMPLETENESS, 85.1, 95.0, AlertSeverity.CRITICAL, 3.5),
            # Equipment Readiness — degraded
            ("Equipment Readiness Pipeline", MetricType.ACCURACY, 96.8, 98.0, AlertSeverity.WARNING, 1.0),
            ("Equipment Readiness Pipeline", MetricType.TIMELINESS, 380.0, 300.0, AlertSeverity.WARNING, 2.5),
            ("Equipment Readiness Pipeline", MetricType.VOLUME, 3200.0, 7500.0, AlertSeverity.WARNING, 4.0),
            # SITREP Aggregation — intermittent issues
            ("SITREP Aggregation", MetricType.COMPLETENESS, 91.2, 95.0, AlertSeverity.WARNING, 1.5),
            ("SITREP Aggregation", MetricType.COMPLETENESS, 89.8, 95.0, AlertSeverity.CRITICAL, 5.0),
            ("SITREP Aggregation", MetricType.FRESHNESS, 4.5, 4.0, AlertSeverity.WARNING, 3.0),
            # MSS Roster Sync — one-off info alert
            ("MSS Roster Sync", MetricType.VOLUME, 7500.0, 4500.0, AlertSeverity.INFO, 6.0),
            # Training Completion — minor
            ("Training Completion ETL", MetricType.COMPLETENESS, 93.8, 95.0, AlertSeverity.WARNING, 8.0),
            ("Training Completion ETL", MetricType.TIMELINESS, 320.0, 300.0, AlertSeverity.INFO, 10.0),
            # Personnel Data Feed — volume spike
            ("Personnel Data Feed", MetricType.VOLUME, 38000.0, 22000.0, AlertSeverity.INFO, 2.0),
        ]

        for pname, mt, val, thresh, sev, hours_ago in alert_configs:
            pipe = pipe_map[pname]
            alert = AlertRow(
                pipeline_id=pipe.id,
                metric_type=mt.value,
                value=val,
                threshold=thresh,
                severity=sev.value,
                timestamp=now - timedelta(hours=hours_ago),
            )
            db.add(alert)

    print(f"Seeded {len(PIPELINES)} pipelines, ~{90 * 4 * len(PIPELINES)} metrics, {len(alert_configs)} alerts.")


if __name__ == "__main__":
    seed()
