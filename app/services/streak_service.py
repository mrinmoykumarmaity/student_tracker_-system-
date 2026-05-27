from app.models.study_session import StudySession
from datetime import datetime, timedelta
from sqlalchemy import func

class StreakService:
    
    def get_current_streak(self):
        """Calculate current consecutive study days"""
        today = datetime.now().date()
        
        # Get all unique study dates, ordered descending
        dates = StudySession.query.with_entities(
            StudySession.study_date
        ).distinct().order_by(
            StudySession.study_date.desc()
        ).all()
        
        if not dates:
            return 0
        
        dates = [d[0] for d in dates]
        
        # Check if studied today or yesterday
        if dates[0] != today and dates[0] != today - timedelta(days=1):
            return 0
        
        streak = 0
        expected_date = today if dates[0] == today else today - timedelta(days=1)
        
        for date in dates:
            if date == expected_date:
                streak += 1
                expected_date -= timedelta(days=1)
            else:
                break
        
        return streak
    
    def get_best_streak(self):
        """Calculate best streak ever"""
        dates = StudySession.query.with_entities(
            StudySession.study_date
        ).distinct().order_by(
            StudySession.study_date.asc()
        ).all()
        
        if not dates:
            return 0
        
        dates = [d[0] for d in dates]
        
        max_streak = 1
        current_streak = 1
        
        for i in range(1, len(dates)):
            if dates[i] == dates[i-1] + timedelta(days=1):
                current_streak += 1
                max_streak = max(max_streak, current_streak)
            else:
                current_streak = 1
        
        return max_streak
