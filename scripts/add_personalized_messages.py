#!/usr/bin/env python3
"""
Add personalized_message, channel, and email_subject to urgent_high_intent CSV.
Uses cohort3-10days-conversion-plan angles: Top 5 trending, Wall of Fame, deadline Sun Feb 22 noon.
"""
import csv
import re
from pathlib import Path

CSV_PATH = Path(__file__).resolve().parents[1] / "project-context/analysis/raw/segmentation/urgent_high_intent_2026-02-21.csv"
OUT_PATH = CSV_PATH  # overwrite in place

# Hard no per campaign plan — do not contact
DO_NOT_CONTACT_EMAILS = {"aryan.saurabhbhardwaj@gmail.com"}

def has_linkedin(row) -> bool:
    url = (row.get("linkedin_url") or "").strip().lower()
    return bool(url and url not in ("none", "na", ".", "n/a"))

def first_name(row) -> str:
    pref = (row.get("preferred_name") or "").strip()
    if pref:
        return pref.split()[0] if pref else ""
    full = (row.get("full_name") or "").strip()
    if full:
        return full.split()[0]
    return ""

def source_type(row) -> str:
    return (row.get("source") or "").strip()

def segment_type(row) -> str:
    return (row.get("segment") or "").strip()

def build_message(row: dict) -> tuple:
    """Returns (channel, email_subject, personalized_message)."""
    email = (row.get("email") or "").strip().lower()
    if email in DO_NOT_CONTACT_EMAILS:
        return (
            "Email",
            "",
            "[DO NOT CONTACT — Hard no per campaign plan; company rejected payment.]",
        )

    name = first_name(row)
    source = source_type(row)
    segment = segment_type(row)
    is_linkedin = has_linkedin(row)

    # Greeting + shared building blocks (warm, natural tone per your Phuc example)
    hi = f"Hi {name}," if name else "Hi,"
    deadline_ext = "we have extended enrollment to Sunday noon (Feb 22nd 15:00 UTC)."
    deadline_short = "Sunday noon (Feb 22nd 15:00 UTC)."
    top5 = "Become an Agentic Architect is now a Top 5 trending Engineering course on Maven."
    wof = "Cohort 2 just wrapped with 2 projects on the Wall of Fame."
    price = "This is the last cohort at $1,500: starting Monday the price for future cohorts will go to $1,995."
    cta = "https://maven.com/carmelo-iaria/agentic-architect?promoCode=LL25"
    cta_line = f"You can still enroll for $1,125 with 25% off here: {cta}"
    sign_off = "Happy to chat if you have questions.\n\nLooking forward to meet you in Cohort 3 next week!\nCarmelo"
    sign_off_short = "Happy to chat if you have questions. Looking forward to meet you in Cohort 3 next week!\nCarmelo"

    if is_linkedin:
        channel = "LinkedIn DM"
        subject = ""
        # LinkedIn: same warmth, shorter
        if source == "Started payment":
            msg = (
                f"{hi} I wanted to let you know {deadline_ext}\n\n"
                f"{top5} {wof}\n\n"
                f"{price}\n\n"
                f"{cta_line}\n\n"
                f"{sign_off_short}"
            )
        elif source == "Lightning Lesson":
            msg = (
                f"{hi} I wanted to let you know {deadline_ext}\n\n"
                f"{top5} {wof}\n\n"
                f"{price}\n\n"
                f"As a Lightning Lesson participant you can enroll for $1,125 (25% off) here: {cta}\n\n"
                f"{sign_off_short}"
            )
        elif source == "Waitlist":
            msg = (
                f"{hi} I wanted to let you know {deadline_ext}\n\n"
                f"{top5} {wof}\n\n"
                f"{price}\n\n"
                f"{cta_line}\n\n"
                f"{sign_off_short}"
            )
        else:
            msg = (
                f"{hi} I wanted to let you know {deadline_ext}\n\n"
                f"{top5} {wof}\n\n"
                f"{price}\n\n"
                f"{cta_line}\n\n"
                f"{sign_off_short}"
            )
    else:
        channel = "Email"
        # Email: full warm structure (opener → social proof → price → CTA → sign-off)
        if source == "Started payment":
            subject = "Quick question — enrollment closes Sunday"
            msg = (
                f"{hi} I noticed you started enrolling in Become an Agentic Architect. I wanted to let you know {deadline_ext}\n\n"
                f"{top5} {wof}\n\n"
                f"{price}\n\n"
                f"{cta_line}\n\n"
                f"{sign_off}"
            )
        elif source == "Lightning Lesson":
            subject = "Your 25% off — Cohort 3 closes Sunday"
            msg = (
                f"{hi} You attended one of our Lightning Lessons — I wanted to let you know {deadline_ext}\n\n"
                f"{top5} {wof}\n\n"
                f"{price}\n\n"
                f"As a Lightning Lesson participant you can enroll for $1,125 (25% off) here: {cta}\n\n"
                f"{sign_off}"
            )
        elif source == "Waitlist":
            subject = "We extended enrollment to Sunday — last chance at $1,500"
            msg = (
                f"{hi} I wanted to let you know {deadline_ext}\n\n"
                f"{top5} {wof}\n\n"
                f"{price}\n\n"
                f"{cta_line}\n\n"
                f"{sign_off}"
            )
        else:
            subject = "Last chance at $1,500 — Cohort 3 closes Sunday"
            msg = (
                f"{hi} You downloaded our lead magnet — I wanted to let you know {deadline_ext}\n\n"
                f"{top5} {wof}\n\n"
                f"{price}\n\n"
                f"{cta_line}\n\n"
                f"{sign_off}"
            )

    return (channel, subject, msg)

def main():
    rows = []
    with open(CSV_PATH, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fieldnames = list(reader.fieldnames)
        if "channel" not in fieldnames:
            fieldnames += ["channel", "email_subject", "personalized_message"]
        for row in reader:
            channel, subject, msg = build_message(row)
            row["channel"] = channel
            row["email_subject"] = subject
            row["personalized_message"] = msg
            rows.append(row)

    with open(OUT_PATH, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"Wrote {len(rows)} rows to {OUT_PATH}")
    linkedin_count = sum(1 for r in rows if r["channel"] == "LinkedIn DM")
    print(f"LinkedIn DM: {linkedin_count} | Email: {len(rows) - linkedin_count}")

if __name__ == "__main__":
    main()
