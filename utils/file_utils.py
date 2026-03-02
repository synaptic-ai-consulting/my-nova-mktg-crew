import os
import pandas as pd
import glob
import re
from datetime import datetime

def get_latest_files(cohort_dir):
    """
    Identifies the files with the latest timestamp in the given cohort directory.
    Returns a dictionary mapping base filename (without timestamp) to the full path of the latest version.
    """
    if not os.path.exists(cohort_dir):
        return {}
    
    files = glob.glob(os.path.join(cohort_dir, '*.csv'))
    if not files:
        return {}
    
    # Pattern to extract base name and timestamp
    # Example: active_students_over_time_2026-02-27T08_04_41.636656052-05_00.csv
    # Base: active_students_over_time
    # Timestamp: 2026-02-27T08_04_41.636656052-05_00
    
    file_groups = {}
    for f in files:
        basename = os.path.basename(f)
        # Try to match the timestamp pattern
        match = re.search(r'^(.*)_(\d{4}-\d{2}-\d{2}T.*)\.csv$', basename)
        if match:
            prefix = match.group(1)
            timestamp_str = match.group(2)
            # We can compare timestamps as strings if they are ISO-like, 
            # or parse them. Since they are ISO-like, string comparison works for "latest".
            if prefix not in file_groups or timestamp_str > file_groups[prefix]['timestamp']:
                file_groups[prefix] = {'path': f, 'timestamp': timestamp_str}
        else:
            # Fallback for files without the expected timestamp pattern
            prefix = basename.replace('.csv', '')
            if prefix not in file_groups:
                file_groups[prefix] = {'path': f, 'timestamp': ''}
                
    return {prefix: data['path'] for prefix, data in file_groups.items()}

def list_cohorts(base_dir):
    """
    Lists available cohort subdirectories.
    """
    if not os.path.exists(base_dir):
        return []
    return [d for d in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, d))]

if __name__ == "__main__":
    base_cohorts_path = '/home/italiano/projects/my-nova-mktg-crew/project-context/analysis/raw/cohorts'
    cohorts = list_cohorts(base_cohorts_path)
    print(f"Available cohorts: {cohorts}")
    
    for cohort in cohorts:
        print(f"\nLatest files for Cohort {cohort}:")
        latest = get_latest_files(os.path.join(base_cohorts_path, cohort))
        for prefix, path in latest.items():
            print(f"  {prefix}: {os.path.basename(path)}")
