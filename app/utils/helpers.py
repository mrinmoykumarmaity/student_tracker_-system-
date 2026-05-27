from datetime import datetime, timedelta

def format_duration(hours):
    """Format duration in hours to readable format"""
    if hours < 1:
        minutes = int(hours * 60)
        return f"{minutes} min"
    return f"{hours:.1f} hrs"

def get_week_range():
    """Get start and end date of current week"""
    today = datetime.now().date()
    week_start = today - timedelta(days=today.weekday())
    week_end = week_start + timedelta(days=6)
    return week_start, week_end

def calculate_percentage(current, target):
    """Calculate percentage with safety check"""
    if target == 0:
        return 0
    return min((current / target) * 100, 100)
