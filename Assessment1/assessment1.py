import re
import uuid
from datetime import datetime, timedelta
from collections import defaultdict

# -----------------------------
# CONFIG
# -----------------------------
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
# UTILITIES
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

# -----------------------------
# CORE PROCESSING
# -----------------------------
def process_tickets(raw_tickets):
    processed = []
    rejected = []
    seen_ids = set()

    # For deduplication: (email, issue) -> last timestamp
    recent_map = {}

    for ticket in raw_tickets:
        try:
            original_ticket = ticket.copy()

            # -------- Normalize --------
            email = normalize_text(ticket.get("email"))
            issue = normalize_text(ticket.get("issue_type"))
            priority = normalize_text(ticket.get("priority"))
            name = ticket.get("name", "").strip()
            description = ticket.get("description", "").strip()

            # -------- Validate --------
            if not validate_email(email):
                raise ValueError("Invalid email format")

            if priority not in ALLOWED_PRIORITIES:
                raise ValueError("Invalid priority value")

            if issue not in ISSUE_ROUTING:
                raise ValueError("Unknown issue type")

            # -------- Timestamp --------
            ts = datetime.fromisoformat(ticket["timestamp"])

            # -------- Deduplication --------
            dedup_key = (email, issue)
            if dedup_key in recent_map:
                last_ts = recent_map[dedup_key]
                if abs((ts - last_ts).total_seconds()) <= 24 * 3600:
                    raise ValueError("Duplicate ticket within 24 hours")

            recent_map[dedup_key] = ts

            # -------- Ticket ID --------
            ticket_id = ticket.get("ticket_id")
            if not ticket_id or ticket_id in seen_ids:
                ticket_id = generate_ticket_id()

            seen_ids.add(ticket_id)

            # -------- Routing --------
            team = ISSUE_ROUTING[issue]

            # -------- SLA Deadline --------
            sla_deadline = ts + timedelta(hours=SLA_HOURS[priority])

            processed_ticket = {
                "ticket_id": ticket_id,
                "name": name,
                "email": email,
                "issue_type": issue,
                "priority": priority,
                "description": description,
                "assigned_team": team,
                "created_at": ts.isoformat(),
                "sla_deadline": sla_deadline.isoformat()
            }

            processed.append(processed_ticket)

        except Exception as e:
            rejected.append({
                "ticket": original_ticket,
                "reason": str(e)
            })

    return processed, rejected

# -----------------------------
# SUMMARY REPORT
# -----------------------------
def generate_summary(processed, rejected):
    report = {}
    report["total_received"] = len(processed) + len(rejected)
    report["processed"] = len(processed)
    report["rejected"] = len(rejected)

    team_counts = defaultdict(int)
    for t in processed:
        team_counts[t["assigned_team"]] += 1

    report["tickets_per_team"] = dict(team_counts)
    return report

# -----------------------------
# SAMPLE INPUT (Trigger)
# -----------------------------
if __name__ == "__main__":

    tickets = [
        {
            "ticket_id": "T1",
            "name": "Asha",
            "email": "asha@uni.edu",
            "issue_type": "WiFi",
            "priority": "High",
            "description": "Cannot connect",
            "timestamp": "2026-01-23T09:00:00"
        },
        {
            "ticket_id": "T1",  # duplicate ID
            "name": "Asha",
            "email": "asha@uni.edu",
            "issue_type": "wifi",
            "priority": "High",
            "description": "Still not working",
            "timestamp": "2026-01-23T10:00:00"
        },
        {
            "ticket_id": "",
            "name": "Rahul",
            "email": "rahuluni.edu",  # invalid email
            "issue_type": "login",
            "priority": "Medium",
            "description": "Login failed",
            "timestamp": "2026-01-23T11:00:00"
        },
        {
            "ticket_id": None,
            "name": "Meena",
            "email": "meena@uni.edu",
            "issue_type": "software",
            "priority": "Low",
            "description": "Need MS Office",
            "timestamp": "2026-01-23T12:00:00"
        }
    ]

    processed, rejected = process_tickets(tickets)
    summary = generate_summary(processed, rejected)

    print("\n--- PROCESSED TICKETS ---")
    for t in processed:
        print(t)

    print("\n--- REJECTED TICKETS ---")
    for r in rejected:
        print(r)

    print("\n--- SUMMARY REPORT ---")
    print(summary)
