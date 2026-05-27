from flask import Blueprint, render_template, request, jsonify, session, redirect, url_for
from app import db
from app.models.study_session import StudySession
from datetime import datetime

sessions_bp = Blueprint('sessions', __name__)


def login_required():
    if 'user_id' not in session:
        return False
    return True


@sessions_bp.route('/add', methods=['GET'])
def add_session_page():
    if not login_required():
        return redirect(url_for('auth.login_page'))
    return render_template('add_session.html')


@sessions_bp.route('/add', methods=['POST'])
def add_session():
    if not login_required():
        return jsonify({'success': False, 'message': 'Not logged in'}), 401
    try:
        data = request.get_json()
        sess = StudySession(
            user_id=session['user_id'],
            subject=data['subject'],
            duration=float(data['duration']),
            topic=data['topic'],
            study_date=datetime.strptime(data['study_date'], '%Y-%m-%d').date()
        )
        db.session.add(sess)
        db.session.commit()
        return jsonify({'success': True, 'message': 'Study session added successfully!', 'session': sess.to_dict()}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'message': f'Error adding session: {str(e)}'}), 400


@sessions_bp.route('/list', methods=['GET'])
def list_sessions():
    if not login_required():
        return jsonify({'success': False, 'message': 'Not logged in'}), 401
    try:
        sessions_list = StudySession.query.filter_by(
            user_id=session['user_id']
        ).order_by(StudySession.study_date.desc()).all()
        return jsonify({'success': True, 'sessions': [s.to_dict() for s in sessions_list]})
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 400


@sessions_bp.route('/delete/<int:session_id>', methods=['DELETE'])
def delete_session(session_id):
    if not login_required():
        return jsonify({'success': False, 'message': 'Not logged in'}), 401
    try:
        sess = StudySession.query.filter_by(id=session_id, user_id=session['user_id']).first_or_404()
        db.session.delete(sess)
        db.session.commit()
        return jsonify({'success': True, 'message': 'Session deleted successfully'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'message': str(e)}), 400
