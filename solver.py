"""
Integer Linear Program (ILP) roster solver.

PROBLEM FORMULATION
───────────────────
Given:
  D = set of directorates, each with eligible headcount h_d
  T = set of days in the quarter
  W = subset of T that are weekend or holiday ("hard" days)
  K = T \\ W  (weekday non-holiday days)

Decision variables:
  x[d][t] ∈ {0, 1}   — 1 if directorate d is assigned day t

Constraints:
  (C1) Coverage:    ∑_d x[d][t] = 1              ∀ t ∈ T
  (C2) Total quota: floor(q_d) ≤ ∑_t x[d][t] ≤ ceil(q_d)   ∀ d
                    where q_d = h_d / H * |T|,  H = ∑ h_d
  (C3) Hard-day quota (soft, penalised):
       ∑_{t ∈ W} x[d][t] close to w_d = h_d / H * |W|
  (C4) Cool-down: x[d][t] + x[d][t+1] ≤ 1       ∀ d, consecutive t
       No directorate is assigned back-to-back days (strict).
  (C5) Monthly spread (soft, penalised):
       For each directorate d and month m, the count of assigned days
       should be close to the proportional monthly target.  Deviation
       is penalised in the objective to encourage even month-to-month
       distribution and within-month spacing.

Objective:
  Minimise ∑_d (over_d + under_d) + α ∑_{d,m} (mo_over + mo_under)
  where over_d / under_d measure hard-day deviation,
  and mo_over / mo_under measure monthly deviation.

If the ILP is infeasible, the solver falls back to a greedy assignment
that still respects the cool-down constraint.

OUTPUT
──────
RosterSolution: {date → directorate_name}, plus summary statistics.
"""

from __future__ import annotations

import logging
import math
from collections import defaultdict
from dataclasses import dataclass, field
from datetime import date
from typing import Dict, List, Set, Tuple

import pulp

from .calendar_utils import HOLIDAY, WEEKEND, WEEKDAY, classify_day
from .config import RosterConfig

logger = logging.getLogger(__name__)


# ── Result dataclasses ────────────────────────────────────────────────────────

@dataclass
class DirectorateStats:
    name: str
    eligible: int
    total_days: int
    weekday_days: int
    weekend_days: int
    holiday_days: int

    @property
    def hard_days(self) -> int:
        """Weekend + holiday days (both require sacrifice of personal time)."""
        return self.weekend_days + self.holiday_days

    @property
    def hard_day_pct(self) -> float:
        if self.total_days == 0:
            return 0.0
        return self.hard_days / self.total_days


@dataclass
class RosterSolution:
    """Full solution for one role (SDNCO or SD_Runner)."""
    role: str
    assignment: Dict[date, str]          # date → directorate name
    stats: List[DirectorateStats]
    solver_status: str                   # "Optimal", "Feasible", "Fallback"

    # Fairness metrics (lower = more fair)
    total_day_gini: float = 0.0          # Gini of total days per directorate
    hard_day_gini: float  = 0.0          # Gini of hard days per directorate


# ── Solver ────────────────────────────────────────────────────────────────────

def solve(
    config: RosterConfig,
    all_days: List[date],
    holiday_dates: Set[date],
) -> RosterSolution:
    """
    Build and solve the ILP, return a RosterSolution.

    Parameters
    ----------
    config        : RosterConfig with directorates and date range.
    all_days      : Ordered list of every calendar day in the quarter.
    holiday_dates : Set of dates classified as holidays.
    """
    dirs   = config.directorates
    H      = config.total_eligible
    T      = all_days
    n_days = len(T)

    # Partition days by type
    hard_days = [d for d in T if classify_day(d, holiday_dates) in (WEEKEND, HOLIDAY)]
    soft_days = [d for d in T if d not in hard_days]

    n_hard = len(hard_days)

    # ── Quotas ────────────────────────────────────────────────────────────────
    # Total day quota per directorate (proportional to eligible count)
    total_quota: Dict[str, Tuple[int, int]] = {}   # name → (floor, ceil)
    # Hard-day quota (proportional, used as soft target)
    hard_target: Dict[str, float] = {}

    for d in dirs:
        q     = d.eligible / H * n_days
        total_quota[d.name] = (math.floor(q), math.ceil(q))
        hard_target[d.name] = d.eligible / H * n_hard

    # ── Build ILP ────────────────────────────────────────────────────────────
    prob = pulp.LpProblem(f"StaffDuty_{config.role}", pulp.LpMinimize)

    dir_names = [d.name for d in dirs]
    t_indices = list(range(n_days))

    # Binary assignment variables
    x = pulp.LpVariable.dicts(
        "x",
        ((dn, ti) for dn in dir_names for ti in t_indices),
        cat="Binary",
    )

    # Deviation variables for hard-day fairness (continuous ≥ 0)
    over  = pulp.LpVariable.dicts("over",  dir_names, lowBound=0)
    under = pulp.LpVariable.dicts("under", dir_names, lowBound=0)

    # Objective placeholder — overwritten after C5 monthly spread vars are added

    # (C1) Each day covered by exactly one directorate
    for ti in t_indices:
        prob += pulp.lpSum(x[(dn, ti)] for dn in dir_names) == 1

    # (C2) Total quota bounds
    for d in dirs:
        lo, hi = total_quota[d.name]
        total_assigned = pulp.lpSum(x[(d.name, ti)] for ti in t_indices)
        prob += total_assigned >= lo
        prob += total_assigned <= hi

    # Index hard days by their position in T
    hard_indices = {T.index(hd) for hd in hard_days}

    # (C3) Hard-day deviation tracking
    for d in dirs:
        hard_assigned = pulp.lpSum(
            x[(d.name, ti)] for ti in hard_indices
        )
        target = hard_target[d.name]
        prob += hard_assigned - target <= over[d.name]
        prob += target - hard_assigned <= under[d.name]

    # (C4) Cool-down: no back-to-back days for any directorate (strict)
    for d in dirs:
        for ti in range(n_days - 1):
            prob += x[(d.name, ti)] + x[(d.name, ti + 1)] <= 1

    # (C5) Monthly spread: penalise deviation from monthly targets
    # Group day indices by (year, month)
    month_indices: Dict[Tuple[int, int], List[int]] = defaultdict(list)
    for ti, day in enumerate(T):
        month_indices[(day.year, day.month)].append(ti)

    # Weight for monthly deviation penalty (lower than hard-day penalty
    # so hard-day fairness takes priority, but enough to spread shifts)
    MONTHLY_PENALTY = 0.4

    mo_over = {}
    mo_under = {}
    for d in dirs:
        q_total = d.eligible / H * n_days  # total quota for this directorate
        for ym, indices in month_indices.items():
            month_share = len(indices) / n_days  # fraction of quarter in this month
            monthly_target = q_total * month_share
            key = (d.name, ym)
            mo_over[key]  = pulp.LpVariable(f"mo_over_{d.name}_{ym[0]}_{ym[1]}", lowBound=0)
            mo_under[key] = pulp.LpVariable(f"mo_under_{d.name}_{ym[0]}_{ym[1]}", lowBound=0)
            month_assigned = pulp.lpSum(x[(d.name, ti)] for ti in indices)
            prob += month_assigned - monthly_target <= mo_over[key]
            prob += monthly_target - month_assigned <= mo_under[key]

    # Update objective: hard-day deviation + monthly spread penalty
    prob += pulp.lpSum(over[dn] + under[dn] for dn in dir_names) + \
            MONTHLY_PENALTY * pulp.lpSum(mo_over[k] + mo_under[k] for k in mo_over)

    # ── Solve ─────────────────────────────────────────────────────────────────
    solver = pulp.PULP_CBC_CMD(msg=0)
    status_code = prob.solve(solver)
    status_str  = pulp.LpStatus[prob.status]
    logger.info("ILP solver status: %s", status_str)

    if status_code not in (1, -1):  # 1=Optimal, -1=Infeasible
        logger.warning(
            "ILP status '%s' — falling back to greedy assignment.", status_str
        )
        return _greedy_fallback(config, T, holiday_dates, hard_target, total_quota)

    if status_code == -1:
        logger.warning("ILP infeasible — falling back to greedy assignment.")
        return _greedy_fallback(config, T, holiday_dates, hard_target, total_quota)

    # ── Extract solution ──────────────────────────────────────────────────────
    assignment: Dict[date, str] = {}
    for ti, day in enumerate(T):
        for dn in dir_names:
            if pulp.value(x[(dn, ti)]) > 0.5:
                assignment[day] = dn
                break

    return _build_solution(config, assignment, holiday_dates, status_str)


# ── Greedy fallback ───────────────────────────────────────────────────────────

def _greedy_fallback(
    config: RosterConfig,
    all_days: List[date],
    holiday_dates: Set[date],
    hard_target: Dict[str, float],
    total_quota: Dict[str, Tuple[int, int]],
) -> RosterSolution:
    """
    Greedy assignment when ILP fails.
    Sorts days so hard days are interspersed; assigns directorate with most
    remaining quota (breaking ties by most hard-day deficit).
    """
    dirs     = config.directorates
    dir_names = [d.name for d in dirs]

    remaining_total = {d.name: total_quota[d.name][1] for d in dirs}
    assigned_hard   = {d.name: 0 for d in dirs}
    assignment: Dict[date, str] = {}

    # Interleave hard and soft days so hard days are spread evenly
    hard_days = [d for d in all_days if classify_day(d, holiday_dates) in (WEEKEND, HOLIDAY)]
    soft_days = [d for d in all_days if d not in set(hard_days)]

    ordered_days = _interleave(hard_days, soft_days)

    prev_assigned: str | None = None  # track last-assigned directorate for cool-down

    for day in ordered_days:
        is_hard = classify_day(day, holiday_dates) in (WEEKEND, HOLIDAY)
        eligible = [dn for dn in dir_names if remaining_total[dn] > 0]
        if not eligible:
            eligible = dir_names

        # (C4) Cool-down: exclude the directorate assigned yesterday
        if prev_assigned and prev_assigned in eligible and len(eligible) > 1:
            eligible = [dn for dn in eligible if dn != prev_assigned]

        if is_hard:
            chosen = max(
                eligible,
                key=lambda dn: hard_target.get(dn, 0) - assigned_hard[dn],
            )
        else:
            chosen = max(eligible, key=lambda dn: remaining_total[dn])

        assignment[day] = chosen
        remaining_total[chosen] -= 1
        if is_hard:
            assigned_hard[chosen] += 1
        prev_assigned = chosen

    return _build_solution(config, assignment, holiday_dates, "Fallback")


def _interleave(a: list, b: list) -> list:
    """Interleave two lists as evenly as possible."""
    result, ai, bi = [], 0, 0
    while ai < len(a) or bi < len(b):
        ratio_a = ai / max(len(a), 1)
        ratio_b = bi / max(len(b), 1)
        if ai < len(a) and (bi >= len(b) or ratio_a <= ratio_b):
            result.append(a[ai]); ai += 1
        else:
            result.append(b[bi]); bi += 1
    return result


# ── Stats and fairness metrics ────────────────────────────────────────────────

def _build_solution(
    config: RosterConfig,
    assignment: Dict[date, str],
    holiday_dates: Set[date],
    status: str,
) -> RosterSolution:
    stats_list: List[DirectorateStats] = []

    for d in config.directorates:
        days_for_d = [day for day, dn in assignment.items() if dn == d.name]
        wd = sum(1 for day in days_for_d if classify_day(day, holiday_dates) == WEEKDAY)
        we = sum(1 for day in days_for_d if classify_day(day, holiday_dates) == WEEKEND)
        ho = sum(1 for day in days_for_d if classify_day(day, holiday_dates) == HOLIDAY)
        stats_list.append(
            DirectorateStats(
                name=d.name,
                eligible=d.eligible,
                total_days=len(days_for_d),
                weekday_days=wd,
                weekend_days=we,
                holiday_days=ho,
            )
        )

    total_vals = [s.total_days for s in stats_list]
    hard_vals  = [s.hard_days  for s in stats_list]

    return RosterSolution(
        role=config.role,
        assignment=assignment,
        stats=stats_list,
        solver_status=status,
        total_day_gini=_gini(total_vals),
        hard_day_gini=_gini(hard_vals),
    )


def _gini(values: list[int]) -> float:
    """
    Gini coefficient of a list of non-negative integers.
    0 = perfectly equal, 1 = maximally unequal.
    Used as a fairness metric on the dashboard.
    """
    if not values or sum(values) == 0:
        return 0.0
    n = len(values)
    s = sorted(values)
    cumsum = 0
    for i, v in enumerate(s):
        cumsum += (2 * (i + 1) - n - 1) * v
    return cumsum / (n * sum(values))
