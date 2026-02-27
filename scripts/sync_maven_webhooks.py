#!/usr/bin/env python3
"""
Append new rows from the "Maven Webhooks" tab of the configured Google Sheet
to project-context/analysis/raw/webhooks/maven_webhooks_events.csv.

Uses a state file to remember the last ingested row count so only new events
are appended. Intended to be run via cron.

Required env:
  MAVEN_WEBHOOKS_SHEET_ID   — Google Sheet ID (from the sheet URL)
  GOOGLE_APPLICATION_CREDENTIALS — path to service account JSON key

Optional env:
  MAVEN_WEBHOOKS_OUTPUT_DIR — default: project-context/analysis/raw/webhooks
"""

import csv
import json
import os
import sys
from pathlib import Path

try:
    import gspread  # type: ignore[import-untyped]
except ImportError:
    print("Missing dependencies. Install with: pip install gspread google-auth", file=sys.stderr)
    sys.exit(1)


# Default: script lives in repo/scripts/, output in repo/project-context/analysis/raw/webhooks
REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_OUTPUT_DIR = REPO_ROOT / "project-context" / "analysis" / "raw" / "webhooks"
SHEET_TAB_NAME = "Maven Webhooks"
OUTPUT_CSV = "maven_webhooks_events.csv"
STATE_FILE = ".sync_state.json"


def get_output_dir() -> Path:
    out = os.environ.get("MAVEN_WEBHOOKS_OUTPUT_DIR")
    return Path(out) if out else DEFAULT_OUTPUT_DIR


def load_state(output_dir: Path) -> int:
    path = output_dir / STATE_FILE
    if not path.exists():
        return 0
    try:
        with open(path) as f:
            data = json.load(f)
        return int(data.get("last_ingested_row_count", 0))
    except (json.JSONDecodeError, ValueError):
        return 0


def save_state(output_dir: Path, last_ingested_row_count: int) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    path = output_dir / STATE_FILE
    with open(path, "w") as f:
        json.dump({"last_ingested_row_count": last_ingested_row_count}, f, indent=2)


def main() -> int:
    sheet_id = os.environ.get("MAVEN_WEBHOOKS_SHEET_ID")
    creds_path = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")
    if not sheet_id:
        print("Set MAVEN_WEBHOOKS_SHEET_ID to your Google Sheet ID.", file=sys.stderr)
        return 1
    if not creds_path or not Path(creds_path).exists():
        print("Set GOOGLE_APPLICATION_CREDENTIALS to the path of your service account JSON key.", file=sys.stderr)
        return 1

    output_dir = get_output_dir()
    output_dir.mkdir(parents=True, exist_ok=True)
    csv_path = output_dir / OUTPUT_CSV

    try:
        gc = gspread.service_account(filename=creds_path)
        sh = gc.open_by_key(sheet_id)
        ws = sh.worksheet(SHEET_TAB_NAME)
    except gspread.exceptions.APIError as e:
        print(f"Sheet API error: {e}", file=sys.stderr)
        return 1
    except Exception as e:
        print(f"Auth or unexpected error: {e}", file=sys.stderr)
        return 1

    all_rows = ws.get_all_values()
    if not all_rows:
        print("Sheet tab is empty.", file=sys.stderr)
        return 0

    header = all_rows[0]
    data_rows = all_rows[1:]
    total_data_rows = len(data_rows)
    last_ingested = load_state(output_dir)

    if last_ingested >= total_data_rows:
        # No new rows (or first run with empty data)
        if last_ingested == 0 and total_data_rows == 0:
            return 0
        print(f"No new rows (ingested {last_ingested}, sheet has {total_data_rows} data rows).")
        return 0

    new_rows = data_rows[last_ingested:]
    file_exists = csv_path.exists()

    with open(csv_path, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(header)
        writer.writerows(new_rows)

    new_count = len(new_rows)
    save_state(output_dir, total_data_rows)
    print(f"Appended {new_count} new row(s) to {csv_path} (total data rows now: {total_data_rows}).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
