import pandas as pd
import numpy as np
import os
import sys

# Add project root to path for imports
sys.path.append('/home/italiano/projects/my-nova-mktg-crew')
from src.utils.date_helper import get_cohort_week

def engineer_metrics():
    input_dir = '/home/italiano/projects/my-nova-mktg-crew/data/processed'
    df = pd.read_csv(os.path.join(input_dir, 'cohort3_students_combined.csv'))
    
    # Cohort 3 Start Date
    COHORT_START = '2026-02-23'
    # Current date for analysis (Friday of Week 1)
    CURRENT_DATE = pd.to_datetime('2026-02-27').date()
    
    cohort_status = get_cohort_week(COHORT_START, current_date=CURRENT_DATE)
    week_index = cohort_status['week_index']
    
    # 1. Calculate Engagement Score
    metrics = {
        'Module Item Views': 0.2,
        'Projects Submitted': 0.4,
        'Community Posts': 0.2,
        'Zoom Join Clicks': 0.1,
        'Events Attended': 0.1
    }
    
    df['Engagement Score'] = 0
    for metric, weight in metrics.items():
        if metric in df.columns:
            max_val = df[metric].max()
            if max_val > 0:
                df[f'Norm_{metric}'] = df[metric] / max_val
            else:
                df[f'Norm_{metric}'] = 0
            df['Engagement Score'] += df[f'Norm_{metric}'] * weight

    # 2. Segment Students
    df['Engagement Tier'] = pd.qcut(df['Engagement Score'], q=[0, 0.3, 0.7, 1.0], labels=['Low', 'Medium', 'High'])
    
    # 3. Flag At-Risk Students
    df['At-Risk'] = (df['Engagement Score'] < 0.2) | ((df['Projects Submitted'] == 0) & (df['Module Item Views'] < 5))
    
    # 4. Calculate Points for Leaderboard
    df['Points'] = np.ceil(df['Engagement Score'] * 1000).astype(int)
    
    # 5. Syllabus-Aware 'On-Track' Status
    # Week 1 Milestone: At least 3 module views and 1 community post/zoom click
    if week_index == 1:
        df['On-Track'] = (df['Module Item Views'] >= 3) & ((df['Community Posts'] > 0) | (df['Zoom Join Clicks'] > 0))
    else:
        # Generic logic for other weeks
        expected_views = week_index * 5
        df['On-Track'] = (df['Module Item Views'] >= expected_views) & (df['Engagement Score'] > 0.4)

    # 6. Format activity metrics as integers (User Directive)
    cols_to_fix = ['Projects Submitted', 'Module Item Views', 'Community Posts']
    for col in cols_to_fix:
        if col in df.columns:
            df[col] = df[col].fillna(0).round().astype(int)

    # 7. Temporal Trends
    df_views = pd.read_csv(os.path.join(input_dir, 'cohort3_view_details.csv'))
    df_views['Last Viewed'] = pd.to_datetime(df_views['Last Viewed'])
    df_views['Date'] = df_views['Last Viewed'].dt.date
    
    daily_views = df_views.groupby('Date').size().reset_index(name='View Count')
    daily_views.to_csv(os.path.join(input_dir, 'cohort3_daily_trends.csv'), index=False)
    
    print("\n--- Metric Engineering Summary ---")
    print(df[['Name', 'Engagement Score', 'On-Track', 'At-Risk']].head())
    print(f"\nOn-Track Count: {df['On-Track'].sum()} / {len(df)}")
    
    # Save enriched data
    df.to_csv(os.path.join(input_dir, 'cohort3_students_enriched.csv'), index=False)
    
    # Update Documentation
    doc_content = f"""# Metrics Documentation - Cohort 3 Student Engagement

## Cohort Context
- **Start Date**: {COHORT_START}
- **Analysis Date**: {CURRENT_DATE}
- **Current Week**: {week_index}

## Calculated KPIs
1. **Engagement Score**: Weighted composite (0-1).
2. **On-Track Status**: Syllabus-aware progress tracking.
   - **Week 1 Criteria**: >= 3 Module Views AND (Community Post > 0 OR Zoom Click > 0).
3. **At-Risk Flag**: `Engagement Score < 0.2` OR (`Projects Submitted == 0` AND `Module Item Views < 5`).
"""
    with open('/home/italiano/projects/my-nova-mktg-crew/analysis/metrics_documentation.md', 'w') as f:
        f.write(doc_content)

if __name__ == "__main__":
    engineer_metrics()
