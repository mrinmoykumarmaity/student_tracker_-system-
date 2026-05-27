from app.models.study_session import StudySession
from datetime import datetime, timedelta
from sqlalchemy import func


class AnalyticsService:

    def __init__(self, user_id):
        self.user_id = user_id

    def _base_query(self):
        return StudySession.query.filter_by(user_id=self.user_id)

    def get_total_study_hours(self):
        total = self._base_query().with_entities(func.sum(StudySession.duration)).scalar()
        return round(total or 0, 2)

    def get_today_study_hours(self):
        today = datetime.now().date()
        total = self._base_query().filter(
            StudySession.study_date == today
        ).with_entities(func.sum(StudySession.duration)).scalar()
        return round(total or 0, 2)

    def get_week_study_hours(self):
        today = datetime.now().date()
        week_start = today - timedelta(days=today.weekday())
        total = self._base_query().filter(
            StudySession.study_date >= week_start
        ).with_entities(func.sum(StudySession.duration)).scalar()
        return round(total or 0, 2)

    def get_subject_distribution(self):
        results = self._base_query().with_entities(
            StudySession.subject,
            func.sum(StudySession.duration).label('total_hours')
        ).group_by(StudySession.subject).all()
        return [{'subject': s, 'hours': round(h, 2)} for s, h in results]

    def get_daily_trend(self, days=7):
        end_date = datetime.now().date()
        start_date = end_date - timedelta(days=days - 1)
        results = self._base_query().filter(
            StudySession.study_date >= start_date,
            StudySession.study_date <= end_date
        ).with_entities(
            StudySession.study_date,
            func.sum(StudySession.duration).label('total_hours')
        ).group_by(StudySession.study_date).all()

        data_dict = {date: hours for date, hours in results}
        trend = []
        current_date = start_date
        while current_date <= end_date:
            trend.append({'date': current_date.strftime('%Y-%m-%d'), 'hours': round(data_dict.get(current_date, 0), 2)})
            current_date += timedelta(days=1)
        return trend

    def get_weekly_trend(self, weeks=4):
        end_date = datetime.now().date()
        start_date = end_date - timedelta(weeks=weeks)
        sessions = self._base_query().filter(StudySession.study_date >= start_date).all()

        weekly_data = {}
        for s in sessions:
            week_start = s.study_date - timedelta(days=s.study_date.weekday())
            week_key = week_start.strftime('%Y-%m-%d')
            weekly_data[week_key] = weekly_data.get(week_key, 0) + s.duration

        return [{'week': w, 'hours': round(h, 2)} for w, h in sorted(weekly_data.items())]

    def get_average_daily_hours(self):
        sessions = self._base_query().all()
        if not sessions:
            return 0
        dates = set(s.study_date for s in sessions)
        total_hours = sum(s.duration for s in sessions)
        return round(total_hours / len(dates), 2) if dates else 0
