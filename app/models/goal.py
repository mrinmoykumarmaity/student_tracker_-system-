from app import db
from datetime import datetime


class Goal(db.Model):
    __tablename__ = 'goals'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    goal_type = db.Column(db.String(20), nullable=False)  # 'daily' or 'weekly'
    target_hours = db.Column(db.Float, nullable=False)
    deadline = db.Column(db.Date, nullable=False)
    progress = db.Column(db.Float, default=0.0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    is_active = db.Column(db.Boolean, default=True)

    def __repr__(self):
        return f'<Goal {self.goal_type} - {self.target_hours}h>'

    def to_dict(self):
        return {
            'id': self.id,
            'goal_type': self.goal_type,
            'target_hours': self.target_hours,
            'deadline': self.deadline.strftime('%Y-%m-%d'),
            'progress': self.progress,
            'is_active': self.is_active,
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S')
        }
