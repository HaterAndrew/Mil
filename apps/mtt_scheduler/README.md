# MTT Scheduler

Mobile Training Team scheduling tool for managing theater-wide MSS training events across the USAREUR-AF AOR.

## Purpose

Tracks MTT events, instructor assignments, venue/resource allocation, and student enrollment to support the MSS Training Cell's mission of delivering standardized Foundry/data training across the European and African theaters.

## Architecture

| Component | Port | Technology |
|-----------|------|------------|
| Dashboard | 8505 | Streamlit |
| API | 8005 | FastAPI |
| Database | — | SQLite (local) |

## Quick Start

```bash
# From the repo root (apps/ must be on PYTHONPATH)

# 1. Seed demo data
python -m mtt_scheduler.seed

# 2. Start the API
uvicorn mtt_scheduler.api:app --port 8005 --reload

# 3. Start the dashboard (separate terminal)
streamlit run apps/mtt_scheduler/dashboard.py --server.port 8505
```

## Dashboard Views

- **Event Calendar** — Gantt-style timeline of all events, color-coded by status
- **Event Manager** — CRUD for events, assign instructors and venues
- **Instructor Pool** — Instructor qualifications, availability, conflict detection
- **Enrollment** — Per-event student enrollment with capacity gauge
- **Venue Manager** — AOR venue inventory and utilization calendar
- **Capacity Dashboard** — Fill rates, location heatmap, course distribution

## Data Model

- **Events** — Training iterations with course type, location, dates, capacity, status
- **Instructors** — Qualified MTT cadre with availability windows and course qualifications (JSON)
- **Enrollments** — Student registrations linked to events (ENROLLED/COMPLETE/NO_SHOW/DROPPED)
- **Venues** — Physical training locations with network capability flags (NIPR/SIPR)
- **Event-Instructor** — Many-to-many assignment table

## Seed Data

`seed.py` generates realistic demo data (deterministic, `random.seed(42)`):

- 5 venues: Grafenwoehr, Vilseck, Wiesbaden, Vicenza, Poznan
- 8 instructors with varied TM-10 through TM-40 qualifications
- 12 events spanning Mar-Jun 2026 (COMPLETE, ACTIVE, PLANNED)
- 5-15 enrolled soldiers per event

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| GET | `/health` | Health check |
| POST | `/events` | Create event |
| GET | `/events` | List events (filter by status, location) |
| GET | `/events/{id}` | Get event detail |
| PUT | `/events/{id}` | Update event |
| PATCH | `/events/{id}/status` | Update event status |
| POST | `/events/{id}/instructors/{id}` | Assign instructor |
| DELETE | `/events/{id}/instructors/{id}` | Remove instructor |
| POST | `/instructors` | Create instructor |
| GET | `/instructors` | List instructors |
| DELETE | `/instructors/{id}` | Delete instructor |
| POST | `/enrollments` | Enroll student |
| GET | `/enrollments` | List enrollments |
| PATCH | `/enrollments/{id}/status` | Update enrollment status |
| POST | `/venues` | Create venue |
| GET | `/venues` | List venues |
| DELETE | `/venues/{id}` | Delete venue |
| GET | `/calendar` | Events in date range |
| GET | `/conflicts` | Instructor scheduling conflicts |
| GET | `/utilization` | Capacity utilization stats |
