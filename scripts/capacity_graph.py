#!/usr/bin/env python3
"""Training capacity projection graphs: current state vs instructor models.
   Generates two PNGs: 5-instructor (baseline) and 9-instructor (scale-up).
   Styled to match USAREUR-AF MSS Training Hub (navy + gold command palette).
"""

import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.patheffects as pe
import numpy as np
import sys

# --- Data ---
CURRENT_CAPACITY = 120
FIVE_INSTR_CAPACITY = 1004
NINE_INSTR_CAPACITY = 2008
PCS_RATE = 0.33

YEARS = ["FY26\n(Current)", "FY27\n(Year 1)", "FY28\n(Year 2)", "FY29\n(Year 3)"]

def compute_cumulative(annual_cap):
    trained = [0] * 4
    trained[0] = CURRENT_CAPACITY
    for i in range(1, 4):
        trained[i] = int(trained[i-1] * (1 - PCS_RATE) + annual_cap)
    return trained

curr_trained = compute_cumulative(CURRENT_CAPACITY)
five_trained = compute_cumulative(FIVE_INSTR_CAPACITY)
nine_trained = compute_cumulative(NINE_INSTR_CAPACITY)

OUTFILE_BASE = '/home/dale/Desktop/claude/capacity_projection.png'
OUTFILE_SCALEUP = '/home/dale/Desktop/claude/capacity_projection_scaleup.png'

# --- USAREUR-AF Command Palette ---
NAVY_DARK  = '#071628'
NAVY       = '#0C2340'
NAVY_LIGHT = '#163A6C'
NAVY_MID   = '#1E4A88'
NAVY_PALE  = '#EEF2FA'
GOLD       = '#C8971A'
GOLD_LIGHT = '#E0B840'
GOLD_DARK  = '#9A7010'
GOLD_PALE  = '#FDF5DC'
OFF_WHITE  = '#F3F5FA'
WHITE      = '#FFFFFF'
GRAY_50    = '#EFF1F8'
GRAY_100   = '#E0E4EF'
GRAY_200   = '#C4CAE0'
GRAY_400   = '#5E6E8E'
GRAY_600   = '#485878'
GRAY_900   = '#0A1628'
GREEN_OK   = '#1A5C28'

plt.rcParams.update({
    'font.family': 'sans-serif',
    'font.sans-serif': ['Inter', 'Arial', 'Helvetica', 'Verdana', 'DejaVu Sans'],
    'axes.facecolor': WHITE,
    'figure.facecolor': OFF_WHITE,
    'text.color': GRAY_900,
    'axes.labelcolor': GRAY_600,
    'xtick.color': GRAY_600,
    'ytick.color': GRAY_400,
    'axes.grid': True,
    'grid.color': GRAY_100,
    'grid.alpha': 0.8,
    'grid.linewidth': 0.5,
})


def make_header(fig):
    """Draw gold stripe + navy header band."""
    stripe = fig.add_axes([0, 0.96, 1, 0.008])
    stripe.set_xlim(0, 1); stripe.set_ylim(0, 1)
    stripe.axhspan(0, 1, color=GOLD)
    stripe.set_xticks([]); stripe.set_yticks([])
    for sp in stripe.spines.values(): sp.set_visible(False)

    hdr = fig.add_axes([0, 0.968, 1, 0.032])
    hdr.set_xlim(0, 1); hdr.set_ylim(0, 1)
    hdr.axhspan(0, 1, color=NAVY)
    hdr.set_xticks([]); hdr.set_yticks([])
    for sp in hdr.spines.values(): sp.set_visible(False)

    fig.text(0.5, 0.98, "MSS-TRMS  CAPACITY PROJECTION", ha='center', va='center',
             fontsize=14, fontweight='bold', color=WHITE,
             fontfamily=['Arial', 'Helvetica', 'sans-serif'])



def clean_axes(ax):
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color(GRAY_200); ax.spines['left'].set_linewidth(0.5)
    ax.spines['bottom'].set_color(GRAY_200); ax.spines['bottom'].set_linewidth(0.5)


def smooth_line(ax, x, y, color, lw, alpha=1.0):
    try:
        from scipy.interpolate import make_interp_spline
        xs = np.linspace(x[0], x[-1], 200)
        return make_interp_spline(x, y, k=2)(xs), xs
    except Exception:
        return np.array(y), x


# ========================
# BASELINE: 2 bars, 2 lines
# ========================
def build_baseline():
    fig = plt.figure(figsize=(18, 9))
    make_header(fig)
    fig.text(0.5, 0.925, "Current State vs. 5-Instructor Model  \u2014  FY27 Implementation",
             ha='center', fontsize=12, color=GRAY_600, style='italic')

    ax1 = fig.add_axes([0.06, 0.13, 0.35, 0.72])
    ax2 = fig.add_axes([0.52, 0.13, 0.44, 0.72])

    # Bar chart
    ax1.set_axisbelow(True); ax1.grid(axis='x', visible=False); ax1.grid(axis='y', linewidth=0.4)
    ax1.bar([0, 1], [CURRENT_CAPACITY, FIVE_INSTR_CAPACITY], width=0.48,
            color=[GRAY_200, NAVY], edgecolor=[GRAY_400, NAVY_DARK], linewidth=0.8, zorder=3)
    ax1.set_xticks([0, 1])
    ax1.set_xticklabels(['Current', '5-Instructor\n(FY27 Schedule)'], fontsize=11, color=GRAY_600, linespacing=1.4)
    ax1.set_ylabel("Annual Training Seats", fontsize=11, fontweight='bold', labelpad=10, color=GRAY_600)
    ax1.set_title("ANNUAL THROUGHPUT", fontsize=13, fontweight='bold', pad=14, color=NAVY)
    ax1.set_ylim(0, NINE_INSTR_CAPACITY * 1.25); ax1.yaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))
    ax1.tick_params(axis='both', length=0)
    ax1.text(0, CURRENT_CAPACITY + 28, f"{CURRENT_CAPACITY:,}", ha='center', va='bottom', fontsize=15, fontweight='bold', color=GRAY_600)
    ax1.text(1, FIVE_INSTR_CAPACITY + 28, f"{FIVE_INSTR_CAPACITY:,}", ha='center', va='bottom', fontsize=15, fontweight='bold', color=NAVY)
    ax1.text(1, FIVE_INSTR_CAPACITY * 0.48, f"{FIVE_INSTR_CAPACITY/CURRENT_CAPACITY:.1f}\u00d7", ha='center', va='center',
             fontsize=20, fontweight='bold', color=NAVY_DARK,
             bbox=dict(boxstyle='round,pad=0.35', facecolor=GOLD_LIGHT, edgecolor=GOLD_DARK, alpha=0.92, linewidth=1.5))
    clean_axes(ax1)

    # Line chart
    ax2.set_axisbelow(True); ax2.grid(axis='x', visible=False)
    x = np.arange(len(YEARS))
    cs, xs = smooth_line(ax2, x, curr_trained, GRAY_400, 2)
    fs, _ = smooth_line(ax2, x, five_trained, NAVY, 2.5)
    ax2.fill_between(xs, cs, fs, alpha=0.08, color=NAVY, zorder=1)
    ax2.plot(xs, cs, color=GRAY_400, linewidth=2, alpha=0.7, zorder=2)
    ax2.plot(xs, fs, color=NAVY, linewidth=2.5, zorder=2)
    ax2.scatter(x, curr_trained, color=WHITE, edgecolor=GRAY_400, s=65, linewidth=2, zorder=4, label='Current Model')
    ax2.scatter(x, five_trained, color=GOLD_LIGHT, edgecolor=NAVY, s=80, linewidth=2, zorder=4, label='5-Instructor Model')
    for i, (c, f) in enumerate(zip(curr_trained, five_trained)):
        ax2.text(i, c - 60, f"{c:,}", ha='center', va='top', fontsize=10, color=GRAY_400, fontweight='bold')
        if i > 0:
            ax2.text(i, f + 55, f"{f:,}", ha='center', va='bottom', fontsize=11.5, fontweight='bold', color=NAVY)
    ax2.set_xticks(x); ax2.set_xticklabels(YEARS, fontsize=11, color=GRAY_600, linespacing=1.3)
    ax2.set_ylabel("Trained Personnel in Theater\n(accounting for ~33% annual PCS)", fontsize=11, fontweight='bold', labelpad=10, color=GRAY_600)
    ax2.set_title("CUMULATIVE TRAINED FORCE (WITH PCS TURNOVER)", fontsize=13, fontweight='bold', pad=14, color=NAVY)
    ax2.yaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))
    ax2.set_ylim(-50, max(nine_trained) * 1.18); ax2.tick_params(axis='both', length=0)
    leg = ax2.legend(loc='upper left', fontsize=11, frameon=True, framealpha=0.95, edgecolor=GRAY_200, fancybox=False, borderpad=0.8)
    leg.get_frame().set_linewidth(0.8)
    clean_axes(ax2)

    fig.text(0.5, 0.025,
             "~33% annual PCS turnover   \u2502   5 instructors (1 OIC + 2\u00d7ALPHA + 2\u00d7BRAVO)   \u2502   68 classes \u00b7 5 locations \u00b7 300 training days (OCT\u2013JUL)",
             ha='center', fontsize=9, color=GRAY_400, style='italic')
    fig.text(0.5, 0.005, "USAREUR-AF  \u2022  MSS Training & Readiness Management System",
             ha='center', fontsize=8, color=GRAY_200, fontweight='bold', fontfamily=['Arial', 'Helvetica', 'sans-serif'])

    plt.savefig(OUTFILE_BASE, dpi=180, bbox_inches='tight', facecolor=OFF_WHITE, pad_inches=0.3)
    print(f"Saved: {OUTFILE_BASE}")
    plt.close(fig)


# ========================
# SCALE-UP: 3 bars, 3 lines
# ========================
GOLD_BAR = '#C8971A'

def build_scaleup():
    fig = plt.figure(figsize=(18, 9))
    make_header(fig)
    fig.text(0.5, 0.925, "Current  vs.  5-Instructor (FY27)  vs.  9-Instructor Scale-Up (FY28)",
             ha='center', fontsize=12, color=GRAY_600, style='italic')

    ax1 = fig.add_axes([0.06, 0.13, 0.35, 0.72])
    ax2 = fig.add_axes([0.52, 0.13, 0.44, 0.72])

    # Bar chart — 3 bars
    ax1.set_axisbelow(True); ax1.grid(axis='x', visible=False); ax1.grid(axis='y', linewidth=0.4)
    bars_x = [0, 1, 2]
    bars_h = [CURRENT_CAPACITY, FIVE_INSTR_CAPACITY, NINE_INSTR_CAPACITY]
    bar_colors = [GRAY_200, NAVY, GOLD_BAR]
    bar_edges = [GRAY_400, NAVY_DARK, GOLD_DARK]
    bar_labels = ['Current', '5-Instructor\n(FY27)', '9-Instructor\n(Scale-Up)']

    ax1.bar(bars_x, bars_h, width=0.42, color=bar_colors, edgecolor=bar_edges, linewidth=0.8, zorder=3)
    ax1.set_xticks(bars_x)
    ax1.set_xticklabels(bar_labels, fontsize=10, color=GRAY_600, linespacing=1.4)
    ax1.set_ylabel("Annual Training Seats", fontsize=11, fontweight='bold', labelpad=10, color=GRAY_600)
    ax1.set_title("ANNUAL THROUGHPUT", fontsize=13, fontweight='bold', pad=14, color=NAVY)
    ax1.set_ylim(0, NINE_INSTR_CAPACITY * 1.25)
    ax1.yaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))
    ax1.tick_params(axis='both', length=0)

    ax1.text(0, CURRENT_CAPACITY + 28, f"{CURRENT_CAPACITY:,}", ha='center', va='bottom', fontsize=14, fontweight='bold', color=GRAY_600)
    ax1.text(1, FIVE_INSTR_CAPACITY + 28, f"{FIVE_INSTR_CAPACITY:,}", ha='center', va='bottom', fontsize=14, fontweight='bold', color=NAVY)
    ax1.text(2, NINE_INSTR_CAPACITY + 28, f"{NINE_INSTR_CAPACITY:,}", ha='center', va='bottom', fontsize=14, fontweight='bold', color=GOLD_DARK)

    # Multiplier badges
    ax1.text(1, FIVE_INSTR_CAPACITY * 0.48, f"{FIVE_INSTR_CAPACITY/CURRENT_CAPACITY:.1f}\u00d7", ha='center', va='center',
             fontsize=16, fontweight='bold', color=WHITE,
             bbox=dict(boxstyle='round,pad=0.3', facecolor=NAVY_LIGHT, edgecolor=NAVY_DARK, alpha=0.9, linewidth=1))
    ax1.text(2, NINE_INSTR_CAPACITY * 0.48, f"{NINE_INSTR_CAPACITY/CURRENT_CAPACITY:.1f}\u00d7", ha='center', va='center',
             fontsize=16, fontweight='bold', color=NAVY_DARK,
             bbox=dict(boxstyle='round,pad=0.3', facecolor=GOLD_LIGHT, edgecolor=GOLD_DARK, alpha=0.92, linewidth=1))
    clean_axes(ax1)

    # Line chart — 3 lines
    ax2.set_axisbelow(True); ax2.grid(axis='x', visible=False)
    x = np.arange(len(YEARS))
    cs, xs = smooth_line(ax2, x, curr_trained, GRAY_400, 2)
    fs, _ = smooth_line(ax2, x, five_trained, NAVY, 2.5)
    ns, _ = smooth_line(ax2, x, nine_trained, GOLD_BAR, 2.5)

    # Fill between current and 9-instructor
    ax2.fill_between(xs, cs, ns, alpha=0.06, color=GOLD_BAR, zorder=1)
    ax2.fill_between(xs, cs, fs, alpha=0.06, color=NAVY, zorder=1)

    ax2.plot(xs, cs, color=GRAY_400, linewidth=2, alpha=0.7, zorder=2)
    ax2.plot(xs, fs, color=NAVY, linewidth=2.5, zorder=2)
    ax2.plot(xs, ns, color=GOLD_BAR, linewidth=2.5, linestyle='-', zorder=2)

    ax2.scatter(x, curr_trained, color=WHITE, edgecolor=GRAY_400, s=65, linewidth=2, zorder=4, label='Current Model')
    ax2.scatter(x, five_trained, color=WHITE, edgecolor=NAVY, s=80, linewidth=2, zorder=4, label='5-Instructor Model')
    ax2.scatter(x, nine_trained, color=GOLD_LIGHT, edgecolor=GOLD_DARK, s=80, linewidth=2, zorder=4, label='9-Instructor Scale-Up')

    for i, c in enumerate(curr_trained):
        ax2.text(i, c - 70, f"{c:,}", ha='center', va='top', fontsize=9, color=GRAY_400, fontweight='bold')
    for i, f in enumerate(five_trained):
        if i > 0:
            ax2.text(i, f + 40, f"{f:,}", ha='center', va='bottom', fontsize=10, fontweight='bold', color=NAVY)
    for i, n in enumerate(nine_trained):
        if i > 0:
            ax2.text(i, n + 55, f"{n:,}", ha='center', va='bottom', fontsize=10.5, fontweight='bold', color=GOLD_DARK)

    ax2.set_xticks(x); ax2.set_xticklabels(YEARS, fontsize=11, color=GRAY_600, linespacing=1.3)
    ax2.set_ylabel("Trained Personnel in Theater\n(accounting for ~33% annual PCS)", fontsize=11, fontweight='bold', labelpad=10, color=GRAY_600)
    ax2.set_title("CUMULATIVE TRAINED FORCE (WITH PCS TURNOVER)", fontsize=13, fontweight='bold', pad=14, color=NAVY)
    ax2.yaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))
    ax2.set_ylim(-50, max(nine_trained) * 1.18); ax2.tick_params(axis='both', length=0)
    leg = ax2.legend(loc='upper left', fontsize=11, frameon=True, framealpha=0.95, edgecolor=GRAY_200, fancybox=False, borderpad=0.8)
    leg.get_frame().set_linewidth(0.8)
    clean_axes(ax2)

    fig.text(0.5, 0.025,
             "~33% annual PCS turnover   \u2502   9 instructors (1 OIC + 4 teams of 2)   \u2502   ~136 classes \u00b7 8 locations \u00b7 300 training days (OCT\u2013JUL)",
             ha='center', fontsize=9, color=GRAY_400, style='italic')
    fig.text(0.5, 0.005, "USAREUR-AF  \u2022  MSS Training & Readiness Management System",
             ha='center', fontsize=8, color=GRAY_200, fontweight='bold', fontfamily=['Arial', 'Helvetica', 'sans-serif'])

    plt.savefig(OUTFILE_SCALEUP, dpi=180, bbox_inches='tight', facecolor=OFF_WHITE, pad_inches=0.3)
    print(f"Saved: {OUTFILE_SCALEUP}")
    plt.close(fig)


build_baseline()
build_scaleup()
