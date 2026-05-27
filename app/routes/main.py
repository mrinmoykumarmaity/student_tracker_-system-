from flask import Blueprint, render_template, jsonify, session, redirect, url_for
from app.services.analytics_service import AnalyticsService
from app.services.streak_service import StreakService

main_bp = Blueprint('main', __name__)


def login_required():
    return 'user_id' in session


@main_bp.route('/')
def index():
    if not login_required():
        return redirect(url_for('auth.login_page'))
    return render_template('dashboard.html', username=session.get('username'))


@main_bp.route('/dashboard')
def dashboard():
    if not login_required():
        return redirect(url_for('auth.login_page'))
    return render_template('dashboard.html', username=session.get('username'))


@main_bp.route('/analytics')
def analytics():
    if not login_required():
        return redirect(url_for('auth.login_page'))
    return render_template('analytics.html', username=session.get('username'))


@main_bp.route('/api/dashboard-stats')
def dashboard_stats():
    if not login_required():
        return jsonify({'error': 'Not logged in'}), 401

    user_id = session['user_id']
    analytics = AnalyticsService(user_id=user_id)
    streak_service = StreakService(user_id=user_id)

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
