"""
Seed demo data for SITREP Tracker — dev/test use only.
Run: python seed_demo.py
"""

from db import init_db, insert_sitrep, insert_event, update_sitrep_status

DEMO_SITREPS = [
    {
        "dtg":         "091435Z MAR 26",
        "unit":        "2-34 AR",
        "location":    "YU 4512 8834",
        "status":      "OPEN",
        "situation":   "Element conducting screen operations along Phase Line IRON. No enemy contact in past 6 hrs. Weather: OVC, winds 12kts NW.",
        "personnel":   "All personnel accounted for. 0x KIA, 1x WIA (non-battle injury, returned to duty).",
        "equipment":   "3x M1A2 FMC. 1x M1A2 NMC (engine fault, recovery requested). 2x M2 FMC.",
        "sustainment": "Fuel at 60% — CLASS III resupply requested for 101800Z MAR 26. Rations adequate for 48 hrs.",
        "actions":     "Maintaining screen positions. Submitted recovery request for NMC M1A2 at 091200Z.",
        "next_sitrep": "092000Z MAR 26",
    },
    {
        "dtg":         "091800Z MAR 26",
        "unit":        "1-36 IN",
        "location":    "YU 3920 8201",
        "status":      "PENDING",
        "situation":   "Company in patrol base. 2x patrols departed 091700Z. REDFOR activity reported 4km E by 173rd IBCT.",
        "personnel":   "0x KIA, 0x WIA. 1x Soldier evacuated for medical (non-combat).",
        "equipment":   "All organic equipment FMC. 1x LMTV deadline (brake system, parts on order).",
        "sustainment": "CLASS I adequate. CLASS V resupply complete at 091500Z. CLASS IX parts request submitted.",
        "actions":     "Patrols active. Coordinating with 173rd IBCT on REDFOR activity to the east.",
        "next_sitrep": "100200Z MAR 26",
    },
    {
        "dtg":         "080600Z MAR 26",
        "unit":        "299th BSB",
        "location":    "YU 4800 9100",
        "status":      "CLOSED",
        "situation":   "Convoy MUSTANG 6 completed route BLUE resupply to fwd elements. No incidents en route.",
        "personnel":   "All personnel accounted for.",
        "equipment":   "All vehicles FMC.",
        "sustainment": "Delivered: 8,000 gal JP8, 42x MRE cases, 4x pallets CLASS IX to 2-34 AR and 1-36 IN.",
        "actions":     "Resupply complete. Convoy returned to BSA at 080545Z.",
        "next_sitrep": "091200Z MAR 26",
    },
]

DEMO_EVENTS = [
    (1, "091200Z MAR 26", "MOVEMENT", "2-34 AR element displaced screen position 200m E to improve observation."),
    (1, "091350Z MAR 26", "CONTACT", "Possible UAS observed bearing 070 at approx 3km. Lost contact after 4 min. No engagement."),
    (1, "091435Z MAR 26", "LOGSTAT",  "Recovery request submitted for NMC M1A2 SN 4432."),
    (2, "091715Z MAR 26", "MOVEMENT", "Patrol WOLF 1 departed patrol base, moving SE on AZM 135."),
    (2, "091720Z MAR 26", "MOVEMENT", "Patrol WOLF 2 departed patrol base, moving NE on AZM 045."),
]


def main():
    init_db()
    ids = []
    for s in DEMO_SITREPS:
        sid = insert_sitrep(s)
        ids.append(sid)
        print(f"Inserted SITREP ID={sid}  [{s['unit']}]")

    for (rel_id, dtg, etype, desc) in DEMO_EVENTS:
        actual_id = ids[rel_id - 1]
        insert_event(actual_id, dtg, etype, desc)
        print(f"  Event → SITREP {actual_id} [{etype}]")

    # Mark third SITREP closed
    update_sitrep_status(ids[2], "CLOSED")
    print(f"SITREP {ids[2]} marked CLOSED.")
    print("Demo seed complete.")


if __name__ == "__main__":
    main()
