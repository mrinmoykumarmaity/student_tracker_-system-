from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    database_url = os.environ.get('DATABASE_URL')
    is_production = bool(database_url)

    if database_url:
        # Normalize postgres:// -> postgresql://
        if database_url.startswith('postgres://'):
            database_url = database_url.replace('postgres://', 'postgresql://', 1)
        # Strip query params — psycopg2 doesn't accept them in the DSN
        database_url = database_url.split('?')[0]
        db_uri = database_url
        engine_options = {
            'pool_pre_ping': True,
            'pool_recycle': 300,
            'pool_size': 1,
            'max_overflow': 0,
        }
    else:
        base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
        db_dir = os.path.join(base_dir, 'database')
        os.makedirs(db_dir, exist_ok=True)
        db_path = os.path.join(db_dir, 'study_tracker.db')
        db_uri = f'sqlite:///{db_path}'
        engine_options = {}

    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key')
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_ENGINE_OPTIONS'] = engine_options

    db.init_app(app)

    from app.routes.main import main_bp
    from app.routes.sessions import sessions_bp
    from app.routes.goals import goals_bp
    from app.routes.auth import auth_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)
    app.register_blueprint(sessions_bp, url_prefix='/sessions')
    app.register_blueprint(goals_bp, url_prefix='/goals')

    # Only run create_all locally (SQLite). On Vercel/Supabase we create
    # tables via migration instead of at runtime.
    if not is_production:
        with app.app_context():
            db.create_all()

    return app
