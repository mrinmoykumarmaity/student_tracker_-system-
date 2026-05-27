from app.models.study_session import StudySession
from datetime import datetime, timedelta
from sqlalchemy import func

class AnalyticsService:
    
    def get_total_study_hours(self):
        """Get total study hours across all sessions"""
        total = StudySession.query.with_entities(
            func.sum(StudySession.duration)
        ).scalar()
        return round(total or 0, 2)
    
    def get_today_study_hours(self):
        """Get today's study hours"""
        today = datetime.now().date()
        total = StudySession.query.filter(
            StudySession.study_date == today
        ).with_entities(
            func.sum(StudySession.duration)
        ).scalar()
        return round(total or 0, 2)
    
    def get_week_study_hours(self):
        """Get current week's study hours"""
        today = datetime.now().date()
        week_start = today - timedelta(days=today.weekday())
        
        total = StudySession.query.filter(
            StudySession.study_date >= week_start
        ).with_entities(
            func.sum(StudySession.duration)
        ).scalar()
        return round(total or 0, 2)
    
    def get_subject_distribution(self):
        """Get study hours distribution by subject"""
        results = StudySession.query.with_entities(
            StudySession.subject,
            func.sum(StudySession.duration).label('total_hours')
        ).group_by(StudySession.subject).all()
        
        return [
            {'subject': subject, 'hours': round(hours, 2)}
            for subject, hours in results
        ]
    
    def get_daily_trend(self, days=7):
        """Get daily study trend for last N days"""
        end_date = datetime.now().date()
        start_date = end_date - timedelta(days=days-1)
        
        results = StudySession.query.filter(
            StudySession.study_date >= start_date,
            StudySession.study_date <= end_date
        ).with_entities(
            StudySession.study_date,
            func.sum(StudySession.duration).label('total_hours')
        ).group_by(StudySession.study_date).all()
        
        # Create a dict for easy lookup
        data_dict = {date: hours for date, hours in results}
        
        # Fill in missing dates with 0
        trend = []
        current_date = start_date
        while current_date <= end_date:
            trend.append({
                'date': current_date.strftime('%Y-%m-%d'),
                'hours': round(data_dict.get(current_date, 0), 2)
            })
            current_date += timedelta(days=1)
        
        return trend
    
    def get_weekly_trend(self, weeks=4):
        """Get weekly study trend for last N weeks"""
        end_date = datetime.now().date()
        start_date = end_date - timedelta(weeks=weeks)
        
        sessions = StudySession.query.filter(
            StudySession.study_date >= start_date
        ).all()
        
        weekly_data = {}
        for session in sessions:
            week_start = session.study_date - timedelta(days=session.study_date.weekday())
            week_key = week_start.strftime('%Y-%m-%d')
            
            if week_key not in weekly_data:
                weekly_data[week_key] = 0
            weekly_data[week_key] += session.duration
        
        return [
            {'week': week, 'hours': round(hours, 2)}
            for week, hours in sorted(weekly_data.items())
        ]
    
    def get_average_daily_hours(self):
        """Calculate average daily study hours"""
        sessions = StudySession.query.all()
        if not sessions:
            return 0
        
        dates = set(session.study_date for session in sessions)
        total_hours = sum(session.duration for session in sessions)
        
        return round(total_hours / len(dates), 2) if dates else 0
