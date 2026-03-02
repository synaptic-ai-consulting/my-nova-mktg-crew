import pandas as pd
import os
import glob

def load_and_explore():
    data_dir = '/home/italiano/projects/my-nova-mktg-crew/project-context/analysis/raw/cohorts/3'
    files = glob.glob(os.path.join(data_dir, '*.csv'))
    
    print(f"Found {len(files)} files.")
    
    dataframes = {}
    for f in files:
        name = os.path.basename(f)
        df = pd.read_csv(f)
        dataframes[name] = df
        print(f"\n--- {name} ---")
        print(f"Shape: {df.shape}")
        print(f"Columns: {df.columns.tolist()}")
        print(df.head(2))

    # Merge strategy:
    # maven_activity_by_student and maven_inactive_students seem to have the same schema.
    # module_item_view_detail is granular.
    # active_students_over_time and participating_students_over_time are temporal.
    
    activity_file = [f for f in files if 'maven_activity_by_student' in f][0]
    inactive_file = [f for f in files if 'maven_inactive_students' in f][0]
    
    df_activity = pd.read_csv(activity_file)
    df_inactive = pd.read_csv(inactive_file)
    
    # Combine active and inactive
    df_students = pd.concat([df_activity, df_inactive], ignore_index=True)
    df_students['Email'] = df_students['Email'].str.lower().str.strip()
    
    # Handle missing values in activity metrics
    metrics_cols = ['Module Item Views', 'Projects Submitted', 'Community Posts', 'Zoom Join Clicks', 'Events Attended']
    for col in metrics_cols:
        if col in df_students.columns:
            df_students[col] = df_students[col].fillna(0)
            
    print("\n--- Combined Student Data ---")
    print(df_students.info())
    
    # Save processed data for next step
    output_dir = '/home/italiano/projects/my-nova-mktg-crew/data/processed'
    os.makedirs(output_dir, exist_ok=True)
    df_students.to_csv(os.path.join(output_dir, 'cohort3_students_combined.csv'), index=False)
    
    # Also save the granular view detail for drill-down
    view_detail_file = [f for f in files if 'module_item_view_detail' in f][0]
    df_views = pd.read_csv(view_detail_file)
    df_views['Email'] = df_views['Email'].str.lower().str.strip()
    df_views.to_csv(os.path.join(output_dir, 'cohort3_view_details.csv'), index=False)

if __name__ == "__main__":
    load_and_explore()
