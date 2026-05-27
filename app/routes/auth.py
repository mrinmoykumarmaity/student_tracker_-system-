from flask import Blueprint, render_template, request, jsonify, session, redirect, url_for
from app import db
from app.models.user import User

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/')
@auth_bp.route('/enter', methods=['GET'])
def enter_page():
    # If already has a name, go straight to dashboard
    if 'user_id' in session:
        return redirect(url_for('main.dashboard'))
    return render_template('auth.html')


@auth_bp.route('/enter', methods=['POST'])
def enter():
    try:
        data = request.get_json()
        name = data.get('name', '').strip()

        if not name or len(name) < 2:
            return jsonify({'success': False, 'message': 'Please enter a valid name (at least 2 characters)'}), 400

        # Find existing user by username or create a new one
        user = User.query.filter_by(username=name).first()
        if not user:
            # Create a new user with just a name — no email/password needed
            import secrets
            user = User(
                username=name,
                email=f"{name.lower().replace(' ', '_')}_{secrets.token_hex(4)}@guest.local",
                password_hash='no-password'
            )
            db.session.add(user)
            db.session.commit()

        session['user_id'] = user.id
        session['username'] = user.username
        session.permanent = True

        return jsonify({'success': True, 'redirect': '/dashboard'})

    except Exception as e:
        db.session.rollback()
        return jsonify({'success': False, 'message': str(e)}), 400


@auth_bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('auth.enter_page'))
