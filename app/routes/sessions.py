from flask import Blueprint, render_template, request, jsonify, redirect, url_for
from app import db
from app.models.study_session import StudySession
from datetime import datetime

sessions_bp = Blueprint('sessions', __name__)

@sessions_bp.route('/add', methods=['GET'])
def add_session_page():
    return render_template('add_session.html')

@sessions_bp.route('/add', methods=['POST'])
def add_session():
    try:
        data = request.get_json()
        
        session = StudySession(
            subject=data['subject'],
            duration=float(data['duration']),
            topic=data['topic'],
            study_date=datetime.strptime(data['study_date'], '%Y-%m-%d').date()
        )
        
        db.session.add(session)
        db.session.commit()
        
        return jsonify({
            'success': True,
            'message': 'Study session added successfully!',
            'session': session.to_dict()
        }), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({
            'success': False,
            'message': f'Error adding session: {str(e)}'
        }), 400

@sessions_bp.route('/list', methods=['GET'])
def list_sessions():
    try:
        sessions = StudySession.query.order_by(StudySession.study_date.desc()).all()
        return jsonify({
            'success': True,
            'sessions': [session.to_dict() for session in sessions]
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'message': str(e)
        }), 400

@sessions_bp.route('/delete/<int:session_id>', methods=['DELETE'])
def delete_session(session_id):
    try:
        session = StudySession.query.get_or_404(session_id)
        db.session.delete(session)
        db.session.commit()
        
        return jsonify({
            'success': True,
            'message': 'Session deleted successfully'
        })
    except Exception as e:
        db.session.rollback()
        return jsonify({
            'success': False,
            'message': str(e)
        }), 400
