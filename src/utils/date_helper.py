import datetime
import math

def get_cohort_week(start_date_str, current_date=None):
    """
    Calculates the current cohort week index (1-based) and progress percentage.
    
    Args:
        start_date_str (str): Start date of the cohort in 'YYYY-MM-DD' format.
        current_date (datetime.date, optional): The date to check against. Defaults to today.
        
    Returns:
        dict: {
            'week_index': int,
            'days_since_start': int,
            'expected_progress_pct': float,
            'is_active': bool
        }
    """
    start_date = datetime.datetime.strptime(start_date_str, '%Y-%m-%d').date()
    if current_date is None:
        current_date = datetime.date.today()
    
    delta = (current_date - start_date).days
    
    # If delta is negative, cohort hasn't started
    if delta < 0:
        return {
            'week_index': 0,
            'days_since_start': delta,
            'expected_progress_pct': 0.0,
            'is_active': False
        }
    
    # Week 1 is days 0-6, Week 2 is days 7-13, etc.
    week_index = (delta // 7) + 1
    
    # Progress within the week (assuming a 6-week course based on syllabus research)
    total_course_days = 6 * 7
    progress_pct = min(100.0, (delta / total_course_days) * 100)
    
    return {
        'week_index': week_index,
        'days_since_start': delta,
        'expected_progress_pct': round(progress_pct, 2),
        'is_active': week_index <= 6
    }

if __name__ == "__main__":
    # Test for Cohort 3: Feb 23, 2026
    # Current date is Feb 27, 2026
    test_date = datetime.date(2026, 2, 27)
    result = get_cohort_week('2026-02-23', current_date=test_date)
    print(f"Test Result for Feb 27: {result}")
    
    # Verify Week 1 logic
    assert result['week_index'] == 1
    print("Verification Successful: Correctly identified Week 1.")
