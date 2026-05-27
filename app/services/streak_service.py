from app.models.study_session import StudySession
from datetime import datetime, timedelta


class StreakService:

    def __init__(self, user_id):
        self.user_id = user_id

    def _get_dates(self, ascending=False):
        order = StudySession.study_date.asc() if ascending else StudySession.study_date.desc()
        results = StudySession.query.filter_by(user_id=self.user_id).with_entities(
            StudySession.study_date
        ).distinct().order_by(order).all()
        return [d[0] for d in results]

    def get_current_streak(self):
        today = datetime.now().date()
        dates = self._get_dates(ascending=False)
        if not dates:
            return 0
        if dates[0] != today and dates[0] != today - timedelta(days=1):
            return 0

        streak = 0
        expected = today if dates[0] == today else today - timedelta(days=1)
        for date in dates:
            if date == expected:
                streak += 1
                expected -= timedelta(days=1)
            else:
                break
        return streak

    def get_best_streak(self):
        dates = self._get_dates(ascending=True)
        if not dates:
            return 0
        max_streak = current_streak = 1
        for i in range(1, len(dates)):
            if dates[i] == dates[i - 1] + timedelta(days=1):
                current_streak += 1
                max_streak = max(max_streak, current_streak)
            else:
                current_streak = 1
        return max_streak
