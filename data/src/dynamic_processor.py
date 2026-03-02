import pandas as pd
import os
import sys
from datetime import datetime

# Add project root to path to import utils
sys.path.append('/home/italiano/projects/my-nova-mktg-crew')
from utils.file_utils import get_latest_files

def process_cohort_data(cohort_id):
    """
    Processes raw cohort data for a given cohort ID and saves to processed directory.
    """
    raw_base_path = '/home/italiano/projects/my-nova-mktg-crew/project-context/analysis/raw/cohorts'
    processed_path = '/home/italiano/projects/my-nova-mktg-crew/data/processed'
    os.makedirs(processed_path, exist_ok=True)
    
    cohort_dir = os.path.join(raw_base_path, str(cohort_id))
    latest_files = get_latest_files(cohort_dir)
    
    if not latest_files:
        print(f"No files found for cohort {cohort_id}")
        return False
    
    # 1. Load Student Data
    activity_file = latest_files.get('maven_activity_by_student')
    inactive_file = latest_files.get('maven_inactive_students')
    
    if not activity_file:
        print(f"Missing activity file for cohort {cohort_id}")
        return False
        
    df_activity = pd.read_csv(activity_file)
    df_students = df_activity.copy()
    
    if inactive_file:
        df_inactive = pd.read_csv(inactive_file)
        df_students = pd.concat([df_students, df_inactive], ignore_index=True)
    
    df_students['Email'] = df_students['Email'].str.lower().str.strip()
    
    # Handle missing values
    metrics_cols = ['Module Item Views', 'Projects Submitted', 'Community Posts', 'Zoom Join Clicks', 'Events Attended']
    for col in metrics_cols:
        if col in df_students.columns:
            df_students[col] = df_students[col].fillna(0).astype(int)
    
    # 2. Calculate Engagement Score and Tier
    # Logic: Score = Views*1 + Projects*50 + Posts*10 + Zoom*5 + Events*20
    df_students['Engagement Score'] = (
        df_students['Module Item Views'] * 1 +
        df_students['Projects Submitted'] * 50 +
        df_students['Community Posts'] * 10 +
        df_students['Zoom Join Clicks'] * 5 +
        df_students['Events Attended'] * 20
    )
    
    # Points (same as Engagement Score)
    df_students['Points'] = df_students['Engagement Score']
    
    # Tiers
    def get_tier(score):
        if score > 100: return 'High'
        if score > 30: return 'Medium'
        return 'Low'
    
    df_students['Engagement Tier'] = df_students['Engagement Score'].apply(get_tier)
    
    # At-Risk Logic: Low tier OR 0 projects submitted
    df_students['At-Risk'] = (df_students['Engagement Tier'] == 'Low') | (df_students['Projects Submitted'] == 0)
    
    # 3. Process Trends
    trends_file = latest_files.get('active_students_over_time')
    if trends_file:
        df_trends = pd.read_csv(trends_file)
        # Rename columns for consistency in dashboard
        rename_map = {
            'CLIENT_EVENT_TIME: Week': 'Date',
            'Distinct values of USER_ID': 'View Count'
        }
        df_trends = df_trends.rename(columns=rename_map)
        df_trends.to_csv(os.path.join(processed_path, f'cohort{cohort_id}_daily_trends.csv'), index=False)
    
    # 4. Generate Syllabus Matrix
    views_file = latest_files.get('module_item_view_detail')
    df_matrix = None
    if views_file:
        df_views = pd.read_csv(views_file)
        df_views['Last Viewed'] = pd.to_datetime(df_views['Last Viewed'])
        
        syllabus_items = [
            {'name': 'Fundamentals Course', 'item': 'Agentic Architect Fundamentals Course', 'week': 0},
            {'name': 'Dev Env Setup', 'item': 'Complete your development environment setup', 'week': 0},
            {'name': 'Capstone Choice', 'item': 'Choose your Capstone Project', 'week': 1},
            {'name': 'MRD/PRD Publish', 'item': 'Publish your MRD and PRD', 'week': 1},
            {'name': 'SAD Publish', 'item': 'Publish your SAD', 'week': 2},
            {'name': 'Frontend Commit', 'item': 'Commit your Frontend code', 'week': 2},
            {'name': 'Backend Commit', 'item': 'Commit your Backend code', 'week': 3},
            {'name': 'Integration Commit', 'item': 'Commit the Integrated code', 'week': 4},
            {'name': 'Final Code Commit', 'item': 'Commit your final code', 'week': 5},
            {'name': 'Deployment', 'item': 'Deploy your full stack application', 'week': 5},
            {'name': 'Capstone Publish', 'item': 'Publish your Capstone Project', 'week': 6},
        ]
        
        cohort_start_dt = datetime(2026, 2, 23)
        current_time = datetime(2026, 2, 27, 23, 59)
        
        matrix_data = []
        students = df_students['Name'].unique()
        
        for student in students:
            row = {'Student': student}
            student_views = df_views[df_views['Name'] == student]
            
            for entry in syllabus_items:
                item_name = entry['item']
                col_name = f"W{entry['week']}: {entry['name']}"
                
                week_num = entry['week']
                if week_num == 0:
                    deadline = cohort_start_dt - pd.Timedelta(days=1)
                else:
                    deadline = cohort_start_dt + pd.Timedelta(weeks=week_num-1, days=6)
                
                deadline = deadline.replace(hour=23, minute=59, second=59)
                
                item_views = student_views[student_views['Module Item Title'] == item_name]
                
                if not item_views.empty:
                    first_view = item_views['Last Viewed'].min()
                    if first_view <= deadline:
                        row[col_name] = 'On-Time'
                    else:
                        row[col_name] = 'Late'
                else:
                    if current_time > deadline:
                        row[col_name] = 'Missing'
                    else:
                        row[col_name] = 'Pending'
            
            matrix_data.append(row)
            
        df_matrix = pd.DataFrame(matrix_data)
        
        # Merge with Points for sorting
        df_matrix = df_matrix.merge(df_students[['Name', 'Points']], left_on='Student', right_on='Name', how='left')
        df_matrix = df_matrix.sort_values(by='Points', ascending=False)
        df_matrix = df_matrix.drop(columns=['Name'])
        df_matrix.insert(0, 'No.', range(1, len(df_matrix) + 1))
        
        df_matrix.to_csv(os.path.join(processed_path, f'cohort{cohort_id}_syllabus_matrix.csv'), index=False)

    # 5. Calculate On-Track Status (Revised Logic)
    if df_matrix is not None:
        on_track_students = []
        for _, row in df_matrix.iterrows():
            # Student is 'Behind' ONLY if they have 'Missing' items.
            # 'Late' completions are acceptable for being 'On-Track'.
            is_missing = any(row[col] == 'Missing' for col in df_matrix.columns if col.startswith('W'))
            if not is_missing:
                on_track_students.append(row['Student'])
        
        df_students['On-Track'] = df_students['Name'].isin(on_track_students)
    else:
        # Fallback
        df_students['On-Track'] = df_students['Engagement Score'] > 20
    
    # Save Enriched Data (Final save with On-Track status)
    df_students.to_csv(os.path.join(processed_path, f'cohort{cohort_id}_students_enriched.csv'), index=False)
        
    return True

if __name__ == "__main__":
    if len(sys.argv) > 1:
        process_cohort_data(sys.argv[1])
    else:
        process_cohort_data('3')
