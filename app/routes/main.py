from flask import Blueprint, render_template, jsonify
from app.services.analytics_service import AnalyticsService
from app.services.streak_service import StreakService

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return render_template('dashboard.html')

@main_bp.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@main_bp.route('/analytics')
def analytics():
    return render_template('analytics.html')

@main_bp.route('/api/dashboard-stats')
def dashboard_stats():
    analytics = AnalyticsService()
    streak_service = StreakService()
    
    stats = {
        'total_hours': analytics.get_total_study_hours(),
        'today_hours': analytics.get_today_study_hours(),
        'week_hours': analytics.get_week_study_hours(),
        'current_streak': streak_service.get_current_streak(),
        'best_streak': streak_service.get_best_streak(),
        'subject_distribution': analytics.get_subject_distribution(),
        'daily_trend': analytics.get_daily_trend(days=7),
        'weekly_trend': analytics.get_weekly_trend(weeks=4)
    }
    
    return jsonify(stats)
