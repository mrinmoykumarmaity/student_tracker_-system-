"""
Seed script to populate the database with sample data for testing
Run this after starting the app for the first time to see demo data
"""

from app import create_app, db
from app.models.study_session import StudySession
from app.models.goal import Goal
from datetime import datetime, timedelta
import random

def seed_database():
    app = create_app()
    
    with app.app_context():
        # Clear existing data
        print("Clearing existing data...")
        StudySession.query.delete()
        Goal.query.delete()
        db.session.commit()
        
        # Sample subjects and topics
        subjects_topics = {
            'Mathematics': ['Calculus', 'Linear Algebra', 'Statistics', 'Differential Equations'],
            'Physics': ['Mechanics', 'Thermodynamics', 'Electromagnetism', 'Quantum Physics'],
            'Computer Science': ['Data Structures', 'Algorithms', 'Web Development', 'Machine Learning'],
            'Chemistry': ['Organic Chemistry', 'Inorganic Chemistry', 'Physical Chemistry', 'Biochemistry'],
            'English': ['Literature', 'Grammar', 'Essay Writing', 'Poetry Analysis']
        }
        
        # Create study sessions for the last 30 days
        print("Creating study sessions...")
        today = datetime.now().date()
        
        for i in range(30):
            study_date = today - timedelta(days=i)
            
            # Random number of sessions per day (0-3)
            num_sessions = random.randint(0, 3)
            
            for _ in range(num_sessions):
                subject = random.choice(list(subjects_topics.keys()))
                topic = random.choice(subjects_topics[subject])
                duration = round(random.uniform(0.5, 4.0), 1)
                
                session = StudySession(
                    subject=subject,
                    duration=duration,
                    topic=topic,
                    study_date=study_date
                )
                db.session.add(session)
        
        # Create some goals
        print("Creating goals...")
        
        # Daily goal
        daily_goal = Goal(
            goal_type='daily',
            target_hours=3.0,
            deadline=today + timedelta(days=1)
        )
        db.session.add(daily_goal)
        
        # Weekly goal
        weekly_goal = Goal(
            goal_type='weekly',
            target_hours=20.0,
            deadline=today + timedelta(days=7)
        )
        db.session.add(weekly_goal)
        
        # Commit all changes
        db.session.commit()
        
        # Print statistics
        total_sessions = StudySession.query.count()
        total_goals = Goal.query.count()
        
        print(f"\n✅ Database seeded successfully!")
        print(f"📚 Created {total_sessions} study sessions")
        print(f"🎯 Created {total_goals} goals")
        print(f"\nYou can now run the app with: python run.py")

if __name__ == '__main__':
    seed_database()
