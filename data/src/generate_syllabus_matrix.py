import pandas as pd
import os
from datetime import datetime, timedelta

def generate_syllabus_matrix():
    # Paths
    raw_path = '/home/italiano/projects/my-nova-mktg-crew/project-context/analysis/raw/cohorts/3'
    processed_path = '/home/italiano/projects/my-nova-mktg-crew/data/processed'
    os.makedirs(processed_path, exist_ok=True)
    
    # Load module item views
    views_file = os.path.join(raw_path, 'module_item_view_detail_2026-02-27T08_03_28.386548084-05_00.csv')
    df_views = pd.read_csv(views_file)
    
    # Fix date parsing
    df_views['Last Viewed'] = pd.to_datetime(df_views['Last Viewed'])
    
    # Define Syllabus Items and their Week
    # Logic: Sunday is the last day of the week.
    # Week 1: Feb 23 - March 1
    # Week 2: March 2 - March 8
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
    
    # Cohort Start Date (Monday)
    cohort_start_dt = datetime(2026, 2, 23)
    
    # Load all enrolled students from enriched dataset to ensure we have all 20
    enriched_file = os.path.join(processed_path, 'cohort3_students_enriched.csv')
    if os.path.exists(enriched_file):
        df_enriched = pd.read_csv(enriched_file)
        students = df_enriched['Name'].unique()
    else:
        students = df_views['Name'].unique()
    
    # Create Matrix
    matrix_data = []
    # Current simulation time: Friday Feb 27, 2026
    current_time = datetime(2026, 2, 27, 23, 59) 
    
    for student in students:
        row = {'Student': student}
        student_views = df_views[df_views['Name'] == student]
        
        for entry in syllabus_items:
            item_name = entry['item']
            col_name = f"W{entry['week']}: {entry['name']}"
            
            # Calculate Sunday Deadline for the week
            week_num = entry['week']
            if week_num == 0:
                # Week 0 ends the Sunday BEFORE the cohort starts
                deadline = cohort_start_dt - timedelta(days=1)
            else:
                # Week N ends on the Sunday of that week
                deadline = cohort_start_dt + timedelta(weeks=week_num-1, days=6)
            
            # Set deadline to end of day (23:59:59)
            deadline = deadline.replace(hour=23, minute=59, second=59)
            
            # Check if student viewed this specific item
            item_views = student_views[student_views['Module Item Title'] == item_name]
            
            if not item_views.empty:
                first_view = item_views['Last Viewed'].min()
                if first_view <= deadline:
                    row[col_name] = 'On-Time'
                else:
                    row[col_name] = 'Late'
            else:
                # If current time is past the Sunday deadline, it's Missing
                if current_time > deadline:
                    row[col_name] = 'Missing'
                else:
                    # If we haven't reached the Sunday deadline yet, it's Pending
                    row[col_name] = 'Pending'
        
        matrix_data.append(row)
    
    df_matrix = pd.DataFrame(matrix_data)
    
    # Sort by Points (Engagement Score * 1000)
    if os.path.exists(enriched_file):
        # Merge to get Points
        df_matrix = df_matrix.merge(df_enriched[['Name', 'Points']], left_on='Student', right_on='Name', how='left')
        # Sort by Points descending
        df_matrix = df_matrix.sort_values(by='Points', ascending=False)
        # Drop Name and keep Points for sorting verification if needed
        df_matrix = df_matrix.drop(columns=['Name'])
    
    # Add 'No.' column for 1-20 numbering
    df_matrix.insert(0, 'No.', range(1, len(df_matrix) + 1))
    
    # Output to cohort3_syllabus_matrix.csv as expected by dashboard.py
    df_matrix.to_csv(os.path.join(processed_path, 'cohort3_syllabus_matrix.csv'), index=False)
    print(f"Syllabus matrix generated with {len(df_matrix)} students and {len(syllabus_items)} items.")
    print(f"Logic updated: Sunday is the last day of the week. Week 1 deadline: {cohort_start_dt + timedelta(days=6)}")

if __name__ == "__main__":
    generate_syllabus_matrix()
