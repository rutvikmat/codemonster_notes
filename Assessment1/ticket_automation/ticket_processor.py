import csv
import os
import re
import uuid
from datetime import datetime, timedelta
from collections import defaultdict

# -----------------------------
# CONFIGURATION
# -----------------------------
INPUT_FILE = "input/tickets_input.csv"
OUTPUT_DIR = "output"

PROCESSED_FILE = os.path.join(OUTPUT_DIR, "processed_tickets.csv")
REJECTED_FILE = os.path.join(OUTPUT_DIR, "rejected_tickets.csv")
SUMMARY_FILE = os.path.join(OUTPUT_DIR, "summary_report.csv")

ALLOWED_PRIORITIES = {"low", "medium", "high"}

ISSUE_ROUTING = {
    "wifi": "Network",
    "login": "IT Support",
    "software": "Applications",
    "hardware": "Infrastructure",
    "other": "General"
}

SLA_HOURS = {
    "high": 4,
    "medium": 24,
    "low": 72
}

# -----------------------------
# HELPER FUNCTIONS
# -----------------------------
def normalize_text(text):
    if not text:
        return ""
    return text.strip().lower()

def validate_email(email):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return bool(re.match(pattern, email))

def generate_ticket_id():
    return str(uuid.uuid4())

def ensure_output_dir():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

# -----------------------------
# CORE PROCESSING FUNCTION
# -----------------------------
def process_tickets_from_csv():

    processed = []
    rejected = []

    seen_ticket_ids = set()
    recent_map = {}  # (email, issue) -> last_timestamp

    with open(INPUT_FILE, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        for row in reader:
            original_row = row.copy()

            try:
                # ---------------- Normalize ----------------
                email = normalize_text(row.get("email"))
                issue = normalize_text(row.get("issue_type"))
                priority = normalize_text(row.get("priority"))
                name = row.get("name", "").strip()
                description = row.get("description", "").strip()

                # ---------------- Validate ----------------
                if not validate_email(email):
                    raise ValueError("Invalid email format")

                if priority not in ALLOWED_PRIORITIES:
                    raise ValueError("Invalid priority value")

                if issue not in ISSUE_ROUTING:
                    raise ValueError("Unknown issue type")

                # ---------------- Timestamp ----------------
                ts = datetime.fromisoformat(row["timestamp"])

                # ---------------- Deduplication ----------------
                dedup_key = (email, issue)
                if dedup_key in recent_map:
                    last_ts = recent_map[dedup_key]
                    if abs((ts - last_ts).total_seconds()) <= 24 * 3600:
                        raise ValueError("Duplicate ticket within 24 hours")

                recent_map[dedup_key] = ts

                # ---------------- Ticket ID ----------------
                ticket_id = row.get("ticket_id")
                if not ticket_id or ticket_id in seen_ticket_ids:
                    ticket_id = generate_ticket_id()

                seen_ticket_ids.add(ticket_id)

                # ---------------- Routing ----------------
                assigned_team = ISSUE_ROUTING[issue]

                # ---------------- SLA ----------------
                sla_deadline = ts + timedelta(hours=SLA_HOURS[priority])

                processed.append({
                    "ticket_id": ticket_id,
                    "name": name,
                    "email": email,
                    "issue_type": issue,
                    "priority": priority,
                    "description": description,
                    "assigned_team": assigned_team,
                    "created_at": ts.isoformat(),
                    "sla_deadline": sla_deadline.isoformat()
                })

            except Exception as e:
                original_row["error_reason"] = str(e)
                rejected.append(original_row)

    return processed, rejected

# -----------------------------
# WRITE OUTPUT FILES
# -----------------------------
def write_processed_csv(processed):
    if not processed:
        return

    with open(PROCESSED_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=processed[0].keys())
        writer.writeheader()
        writer.writerows(processed)

def write_rejected_csv(rejected):
    if not rejected:
        return

    with open(REJECTED_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=rejected[0].keys())
        writer.writeheader()
        writer.writerows(rejected)

def write_summary_csv(processed, rejected):
    team_counts = defaultdict(int)
    for t in processed:
        team_counts[t["assigned_team"]] += 1

    summary_rows = [
        {"metric": "Total Tickets", "value": len(processed) + len(rejected)},
        {"metric": "Processed Tickets", "value": len(processed)},
        {"metric": "Rejected Tickets", "value": len(rejected)},
    ]

    for team, count in team_counts.items():
        summary_rows.append({"metric": f"Tickets - {team}", "value": count})

    with open(SUMMARY_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["metric", "value"])
        writer.writeheader()
        writer.writerows(summary_rows)

# -----------------------------
# MAIN TRIGGER
# -----------------------------
if __name__ == "__main__":
    print("Starting Ticket Automation Process...")

    ensure_output_dir()

    processed, rejected = process_tickets_from_csv()

    write_processed_csv(processed)
    write_rejected_csv(rejected)
    write_summary_csv(processed, rejected)

    print("Automation Completed.")
    print(f"Processed: {len(processed)}")
    print(f"Rejected: {len(rejected)}")
    print("Check output folder for results.")
