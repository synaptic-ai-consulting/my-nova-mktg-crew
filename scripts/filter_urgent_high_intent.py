#!/usr/bin/env python3
"""
Filter Urgent + High Intent leads from segmented waitlist and fill linkedin_url
from waitlist + cart data where possible.
Output: project-context/analysis/raw/segmentation/urgent_high_intent_YYYY-MM-DD.csv
"""
import csv
import os
import re

ROOT = os.path.join(os.path.dirname(__file__), "..")
RAW = os.path.join(ROOT, "project-context", "analysis", "raw")
SEG_DIR = os.path.join(RAW, "segmentation")
SEGMENTED_PATH = os.path.join(SEG_DIR, "waitlist_segmented_2026-02-21.csv")
CART_C3_PATH = os.path.join(RAW, "cart", "Become an Agentic Architect_3_38-contacts_2026-02-20.csv")
WAITLIST_PATH = os.path.join(RAW, "waitlist", "Become an Agentic Architect_waitlist_1904contacts_022026.csv")


def normalize_linkedin_url(s: str) -> str:
    """Return cleaned URL or empty string. Ensure https."""
    s = (s or "").strip()
    if not s or s.lower() in ("none", "na", "n/a", "--"):
        return ""
    s = s.strip()
    if re.match(r"^(https?://)?(www\.)?linkedin\.com/", s, re.I):
        if not s.startswith("http"):
            s = "https://" + s.replace("//", "/").replace("https:/", "https://")
        if s.startswith("http://"):
            s = "https://" + s[7:]
        return s
    if "linkedin.com" in s.lower():
        return "https://" + s if not s.startswith("http") else s
    return s


def build_email_to_linkedin(*sources):
    """Build map email -> best linkedin_url from list of (path, email_col, url_col)."""
    out = {}
    for path, email_key, url_key in sources:
        if not os.path.isfile(path):
            continue
        with open(path, newline="", encoding="utf-8") as f:
            r = csv.DictReader(f)
            for row in r:
                email = (row.get(email_key) or "").strip().lower()
                url = normalize_linkedin_url(row.get(url_key) or "")
                if not email:
                    continue
                if url and (email not in out or not out[email]):
                    out[email] = url
    return out


def main():
    # Build email -> linkedin from waitlist and cart (cart may have URL when waitlist doesn't)
    email_to_linkedin = build_email_to_linkedin(
        (WAITLIST_PATH, "email", "linkedin_url"),
        (CART_C3_PATH, "email", "linkedin_url"),
    )

    rows_out = []
    with open(SEGMENTED_PATH, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fieldnames = list(reader.fieldnames)
        for row in reader:
            seg = (row.get("segment") or "").strip()
            if seg not in ("Urgent", "High Intent"):
                continue
            email = (row.get("email") or "").strip().lower()
            current_url = (row.get("linkedin_url") or "").strip()
            current_normalized = normalize_linkedin_url(current_url)
            if not current_normalized and email in email_to_linkedin:
                row["linkedin_url"] = email_to_linkedin[email]
            elif current_normalized:
                row["linkedin_url"] = current_normalized
            rows_out.append(row)

    out_path = os.path.join(SEG_DIR, "urgent_high_intent_2026-02-21.csv")
    with open(out_path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(rows_out)

    filled = sum(1 for r in rows_out if (r.get("linkedin_url") or "").strip())
    print(f"Urgent + High Intent: {len(rows_out)} leads")
    print(f"With linkedin_url: {filled}")
    print(f"Written: {out_path}")
    return out_path


if __name__ == "__main__":
    main()
