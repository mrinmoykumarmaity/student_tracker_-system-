from app import db
from datetime import datetime

class StudySession(db.Model):
    __tablename__ = 'study_sessions'
    
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(100), nullable=False)
    duration = db.Column(db.Float, nullable=False)  # in hours
    topic = db.Column(db.String(200), nullable=False)
    study_date = db.Column(db.Date, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<StudySession {self.subject} - {self.duration}h>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'subject': self.subject,
            'duration': self.duration,
            'topic': self.topic,
            'study_date': self.study_date.strftime('%Y-%m-%d'),
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S')
        }
