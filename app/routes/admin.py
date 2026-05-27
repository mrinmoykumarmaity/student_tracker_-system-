from flask import Blueprint, render_template, request, jsonify, session, redirect, url_for
from app import db
from app.models.user import User
from app.models.study_session import StudySession
from app.models.goal import Goal
from sqlalchemy import func
import os

admin_bp = Blueprint('admin', __name__)

ADMIN_PASSWORD = os.environ.get('ADMIN_PASSWORD', 'admin@mrinmoy2024')


def admin_required():
    return session.get('is_admin') is True


@admin_bp.route('/admin', methods=['GET'])
def admin_page():
    if not admin_required():
        return redirect(url_for('admin.admin_login_page'))
    return render_template('admin.html')


@admin_bp.route('/admin/login', methods=['GET'])
def admin_login_page():
    return render_template('admin_login.html')


@admin_bp.route('/admin/login', methods=['POST'])
def admin_login():
    data = request.get_json()
    password = data.get('password', '')
    if password == ADMIN_PASSWORD:
        session['is_admin'] = True
        return jsonify({'success': True, 'redirect': '/admin'})
    return jsonify({'success': False, 'message': 'Wrong password'}), 401


@admin_bp.route('/admin/logout')
def admin_logout():
    session.pop('is_admin', None)
    return redirect(url_for('admin.admin_login_page'))


@admin_bp.route('/admin/api/stats')
def admin_stats():
    if not admin_required():
        return jsonify({'error': 'Unauthorized'}), 401

    # Total users
    total_users = User.query.count()

    # Total sessions
    total_sessions = StudySession.query.count()

    # Total study hours
    total_hours = db.session.query(func.sum(StudySession.duration)).scalar() or 0

    # Users list with their stats
    users = User.query.order_by(User.created_at.desc()).all()
    users_data = []
    for user in users:
        session_count = StudySession.query.filter_by(user_id=user.id).count()
        hours = db.session.query(func.sum(StudySession.duration)).filter(
            StudySession.user_id == user.id
        ).scalar() or 0
        last_session = StudySession.query.filter_by(user_id=user.id).order_by(
            StudySession.created_at.desc()
        ).first()
        users_data.append({
            'id': user.id,
            'name': user.username,
            'joined': user.created_at.strftime('%Y-%m-%d %H:%M'),
            'sessions': session_count,
            'hours': round(hours, 2),
            'last_active': last_session.created_at.strftime('%Y-%m-%d %H:%M') if last_session else 'Never',
        })

    return jsonify({
        'total_users': total_users,
        'total_sessions': total_sessions,
        'total_hours': round(total_hours, 2),
        'users': users_data
    })
