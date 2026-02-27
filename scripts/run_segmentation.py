#!/usr/bin/env python3
"""
HCP Score + Segmentation for Become an Agentic Architect waitlist.
Uses: project-context/plans/segmentation.md (formula and segment rules).
Inputs: waitlist CSV, cart C3 CSV, LL signups CSV, webhooks CSV (all under project-context/analysis/raw/).
Output: CSV with leads + hcp_score + segment → project-context/analysis/raw/segmentation/.
"""
import csv
import os
from collections import defaultdict
from datetime import datetime

# Paths (from repo root)
ROOT = os.path.join(os.path.dirname(__file__), "..")
RAW = os.path.join(ROOT, "project-context", "analysis", "raw")
SEG_DIR = os.path.join(RAW, "segmentation")
WAITLIST_PATH = os.path.join(RAW, "waitlist", "Become an Agentic Architect_waitlist_1904contacts_022026.csv")
CART_C3_PATH = os.path.join(RAW, "cart", "Become an Agentic Architect_3_38-contacts_2026-02-20.csv")
LL_SIGNUPS_PATH = os.path.join(RAW, "LL", "lightning_lessons_student_signups_2026-02-20T16_04_09.951679857-05_00.csv")
WEBHOOKS_PATH = os.path.join(RAW, "webhooks", "Maven Course Become an Agentic Architect - Maven Webhooks.csv")

# Reference date for "days since last activity" (Saturday Feb 21, 2026)
TODAY = datetime(2026, 2, 21).date()


def parse_ll_date(s: str):
    """Parse 'Fri, Feb 20, 2026' or 'Wed, Aug 13, 2025'."""
    s = (s or "").strip()
    if not s:
        return None
    try:
        return datetime.strptime(s, "%a, %b %d, %Y").date()
    except ValueError:
        return None


def parse_webhook_ts(s: str):
    """Parse '10/23/2025 17:14:07'."""
    s = (s or "").strip()
    if not s:
        return None
    try:
        return datetime.strptime(s, "%m/%d/%Y %H:%M:%S").date()
    except ValueError:
        return None


def load_ll_latest_dates():
    """Email -> most recent LL signup date."""
    out = {}
    with open(LL_SIGNUPS_PATH, newline="", encoding="utf-8") as f:
        r = csv.DictReader(f)
        for row in r:
            email = (row.get("Email") or "").strip().lower()
            if not email:
                continue
            d = parse_ll_date(row.get("Created At: Day") or "")
            if d and (email not in out or d > out[email]):
                out[email] = d
    return out


def load_cart_c3_emails():
    """Set of emails in C3 cart that are not enrolled (status != enrolled)."""
    emails = set()
    with open(CART_C3_PATH, newline="", encoding="utf-8") as f:
        r = csv.DictReader(f)
        for row in r:
            if (row.get("status") or "").strip().lower() == "enrolled":
                continue
            email = (row.get("email") or "").strip().lower()
            if email:
                emails.add(email)
    return emails


def load_webhooks():
    """unsubscribed set, and email -> latest event date."""
    unsubscribed = set()
    last_event = {}
    with open(WEBHOOKS_PATH, newline="", encoding="utf-8") as f:
        r = csv.DictReader(f)
        for row in r:
            email = (row.get("Email") or "").strip().lower()
            if not email:
                continue
            ev = (row.get("Event") or "").strip()
            if ev == "waitlist.unsubscribed":
                unsubscribed.add(email)
            ts = parse_webhook_ts(row.get("Timestamp") or "")
            if ts and (email not in last_event or ts > last_event[email]):
                last_event[email] = ts
    return unsubscribed, last_event


def email_engagement_pts(*_):
    """No per-lead opens/clicks in raw data → 0. Subtotal 0/55 → 0% of 35."""
    return 0.0


def behavioral_intent_pts(source: str, payment_initiated: bool) -> float:
    """Highest signal wins. Payment 40, Lead magnet 30, LL 15, Waitlist 10. Max 40."""
    if payment_initiated:
        return 40.0
    s = (source or "").strip().lower()
    if "started payment" in s or "payment" in s:
        return 40.0
    if "lead magnet" in s or "downloaded" in s:
        return 30.0
    if "lightning" in s or "lesson" in s:
        return 15.0
    if "waitlist" in s or s == "waitlist":
        return 10.0
    return 10.0  # default as waitlist


def profile_completeness_pts(row: dict) -> float:
    """Name 3, Company 3, Job 2, LinkedIn 2. Max 10."""
    pts = 0.0
    if (row.get("full_name") or "").strip() or (row.get("preferred_name") or "").strip():
        pts += 3.0
    if (row.get("company") or "").strip():
        pts += 3.0
    if (row.get("job_title") or "").strip():
        pts += 2.0
    if (row.get("linkedin_url") or "").strip() and (row.get("linkedin_url") or "").strip().lower() not in ("none", "na", "n/a"):
        pts += 2.0
    return pts


def recency_pts(days_since_last_activity: int) -> float:
    """≤7 → 15, ≤14 → 10, ≤30 → 5, >30 → 0. Max 15."""
    if days_since_last_activity <= 7:
        return 15.0
    if days_since_last_activity <= 14:
        return 10.0
    if days_since_last_activity <= 30:
        return 5.0
    return 0.0


def hcp_score(
    source: str,
    payment_initiated: bool,
    row: dict,
    days_since: int,
    email_engagement_raw: float = 0.0,
) -> float:
    """HCP = (EmailEngagement/55*35) + BehavioralIntent + ProfileCompleteness + Recency. Max 100."""
    email_norm = (email_engagement_raw / 55.0) * 35.0 if email_engagement_raw else 0.0
    behavior = behavioral_intent_pts(source, payment_initiated)
    profile = profile_completeness_pts(row)
    recency = recency_pts(days_since)
    return round(email_norm + behavior + profile + recency, 1)


def assign_segment(
    hcp: float,
    payment_initiated: bool,
    lead_magnet_downloaded: bool,
    days_since_last_activity: int,
    unsubscribed: bool,
) -> str:
    if unsubscribed:
        return "Unsubscribed"
    if hcp > 80 or payment_initiated:
        return "Urgent"
    if hcp >= 60 or lead_magnet_downloaded:
        return "High Intent"
    if hcp >= 40 and days_since_last_activity <= 14:
        return "Engaged Nurture"
    if days_since_last_activity > 30:
        return "Reactivation"
    return "Cold Nurture"


def main():
    os.makedirs(SEG_DIR, exist_ok=True)

    ll_dates = load_ll_latest_dates()
    cart_emails = load_cart_c3_emails()
    unsubscribed, webhook_last = load_webhooks()

    rows_out = []
    with open(WAITLIST_PATH, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fieldnames = list(reader.fieldnames) + ["hcp_score", "segment", "days_since_last_activity"]
        for row in reader:
            email = (row.get("email") or "").strip().lower()
            if not email:
                continue
            status = (row.get("status") or "").strip().lower()
            source = (row.get("source") or "").strip()
            payment_initiated = email in cart_emails and status != "enrolled"
            lead_magnet = "lead magnet" in source.lower() or "downloaded" in source.lower()

            # Last activity date: max of LL signup, in-cart (use today), webhook event
            last_dt = None
            if email in ll_dates:
                last_dt = ll_dates[email]
            if email in cart_emails:
                if last_dt is None or TODAY > last_dt:
                    last_dt = TODAY
            if email in webhook_last:
                d = webhook_last[email]
                if last_dt is None or d > last_dt:
                    last_dt = d
            if last_dt is None:
                days_since = 999
            else:
                days_since = (TODAY - last_dt).days

            score = hcp_score(source, payment_initiated, row, days_since)
            segment = assign_segment(
                score,
                payment_initiated,
                lead_magnet,
                days_since,
                email in unsubscribed,
            )

            new_row = {k: row.get(k, "") for k in reader.fieldnames}
            new_row["hcp_score"] = score
            new_row["segment"] = segment
            new_row["days_since_last_activity"] = days_since if last_dt is not None else ""
            rows_out.append(new_row)

    out_path = os.path.join(SEG_DIR, "waitlist_segmented_2026-02-21.csv")
    with open(out_path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows_out)

    # Summary
    counts = defaultdict(int)
    for r in rows_out:
        counts[r["segment"]] += 1
    print("Segment counts:", dict(counts))
    print("Written:", out_path)
    return out_path


if __name__ == "__main__":
    main()
