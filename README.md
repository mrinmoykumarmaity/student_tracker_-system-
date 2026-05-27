# Student Study Tracker

A modern web application to help students track their study sessions, monitor productivity, and achieve their learning goals.

## Features

- **Daily Study Logger**: Record study sessions with subject, duration, topic, and date
- **Productivity Dashboard**: Visualize study patterns with interactive charts
- **Goal Tracking**: Set and monitor daily/weekly study goals
- **Study Streak System**: Track consecutive study days
- **Analytics**: Comprehensive insights into study habits
- **Dark Mode**: Toggle between light and dark themes
- **Responsive Design**: Works seamlessly on all devices

## Tech Stack

- **Backend**: Python Flask
- **Database**: SQLite with SQLAlchemy ORM
- **Frontend**: HTML5, CSS3, JavaScript
- **Charts**: Chart.js
- **Architecture**: Modular MVC pattern

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd study_tracker
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
python run.py
```

5. Open your browser and navigate to:
```
http://localhost:5000
```

## Project Structure

```
study_tracker/
│
├── app/
│   ├── __init__.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── study_session.py
│   │   └── goal.py
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── main.py
│   │   ├── sessions.py
│   │   └── goals.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── analytics_service.py
│   │   └── streak_service.py
│   ├── utils/
│   │   ├── __init__.py
│   │   └── helpers.py
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css
│   │   └── js/
│   │       ├── main.js
│   │       ├── charts.js
│   │       └── darkmode.js
│   └── templates/
│       ├── base.html
│       ├── dashboard.html
│       ├── add_session.html
│       └── analytics.html
│
├── database/
│   └── study_tracker.db (auto-generated)
├── requirements.txt
├── run.py
└── README.md
```

## Usage

### Adding a Study Session
1. Navigate to "Add Session" from the sidebar
2. Fill in subject, duration, topic, and date
3. Click "Save Session"

### Viewing Dashboard
- See total study hours
- Monitor daily and weekly trends
- Track subject distribution
- View current study streak

### Setting Goals
1. Go to "Goals" section
2. Set daily or weekly targets
3. Monitor progress with visual indicators

### Analytics
- View detailed charts and graphs
- Analyze study patterns
- Export reports (coming soon)

## Database Schema

### StudySessions Table
- `id`: Primary key
- `subject`: Study subject
- `duration`: Duration in hours
- `topic`: Topic covered
- `study_date`: Date of study session
- `created_at`: Timestamp

### Goals Table
- `id`: Primary key
- `goal_type`: 'daily' or 'weekly'
- `target_hours`: Target study hours
- `deadline`: Goal deadline
- `progress`: Current progress percentage

## Features Roadmap

- [x] Daily study logging
- [x] Dashboard with analytics
- [x] Goal tracking
- [x] Study streak system
- [x] Dark mode
- [ ] Export study reports (PDF/CSV)
- [ ] Email notifications
- [ ] Mobile app
- [ ] Study reminders

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

MIT License

## Author

Built as a portfolio project demonstrating full-stack web development skills.
