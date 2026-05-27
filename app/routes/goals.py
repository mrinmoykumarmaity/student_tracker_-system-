from flask import Blueprint, request, jsonify, session
from app import db
from app.models.goal import Goal
from app.services.analytics_service import AnalyticsService
from datetime import datetime

goals_bp = Blueprint('goals', __name__)


def login_required():
    return 'user_id' in session


@goals_bp.route('/add', methods=['POST'])
def add_goal():
    if not login_required():
        return jsonify({'success': False, 'message': 'Not logged in'}), 401
    try:
        data = request.get_json()
        goal = Goal(
            user_id=session['user_id'],
            goal_type=data['goal_type'],
            target_hours=float(data['target_hours']),
            deadline=datetime.strptime(data['deadline'], '%Y-%m-%d').date()
        )
        db.session.add(goal)
        db.session.commit()
        return jsonify({'success': True, 'message': 'Goal created successfully!', 'goal': goal.to_dict()}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'message': f'Error creating goal: {str(e)}'}), 400


@goals_bp.route('/list', methods=['GET'])
def list_goals():
    if not login_required():
        return jsonify({'success': False, 'message': 'Not logged in'}), 401
    try:
        user_id = session['user_id']
        goals = Goal.query.filter_by(user_id=user_id, is_active=True).all()
        analytics = AnalyticsService(user_id=user_id)

        goals_data = []
        for goal in goals:
            goal_dict = goal.to_dict()
            hours = analytics.get_today_study_hours() if goal.goal_type == 'daily' else analytics.get_week_study_hours()
            progress = min((hours / goal.target_hours) * 100, 100) if goal.target_hours > 0 else 0
            goal_dict['current_hours'] = hours
            goal_dict['progress'] = round(progress, 1)
            goals_data.append(goal_dict)

        return jsonify({'success': True, 'goals': goals_data})
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 400


@goals_bp.route('/delete/<int:goal_id>', methods=['DELETE'])
def delete_goal(goal_id):
    if not login_required():
        return jsonify({'success': False, 'message': 'Not logged in'}), 401
    try:
        goal = Goal.query.filter_by(id=goal_id, user_id=session['user_id']).first_or_404()
        goal.is_active = False
        db.session.commit()
        return jsonify({'success': True, 'message': 'Goal deleted successfully'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'message': str(e)}), 400
