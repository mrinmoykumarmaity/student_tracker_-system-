# Student Study Tracker - Setup Guide

## Quick Start

### 1. Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### 2. Installation Steps

#### Step 1: Navigate to project directory
```bash
cd study_tracker
```

#### Step 2: Create virtual environment
```bash
python -m venv venv
```

#### Step 3: Activate virtual environment

**Windows:**
```bash
venv\Scripts\activate
```

**Mac/Linux:**
```bash
source venv/bin/activate
```

#### Step 4: Install dependencies
```bash
pip install -r requirements.txt
```

#### Step 5: Run the application
```bash
python run.py
```

#### Step 6: Open in browser
Navigate to: `http://localhost:5000`

## Features Overview

### Dashboard
- View total study hours
- Monitor daily and weekly progress
- Track study streaks
- Visualize subject distribution
- Set and monitor goals

### Add Session
- Log study sessions with subject, duration, topic, and date
- View recent sessions
- Delete sessions

### Analytics
- Detailed charts and graphs
- Weekly trends
- Subject-wise analysis
- Search and filter sessions

### Dark Mode
- Toggle between light and dark themes
- Preference saved automatically

## Project Structure

```
study_tracker/
│
├── app/
│   ├── __init__.py              # App initialization
│   ├── models/                  # Database models
│   │   ├── study_session.py     # Study session model
│   │   └── goal.py              # Goal model
│   ├── routes/                  # API routes
│   │   ├── main.py              # Main routes
│   │   ├── sessions.py          # Session routes
│   │   └── goals.py             # Goal routes
│   ├── services/                # Business logic
│   │   ├── analytics_service.py # Analytics calculations
│   │   └── streak_service.py    # Streak calculations
│   ├── static/                  # Static files
│   │   ├── css/style.css        # Styles
│   │   └── js/                  # JavaScript files
│   └── templates/               # HTML templates
│
├── database/                    # SQLite database (auto-created)
├── requirements.txt             # Python dependencies
├── run.py                       # Application entry point
└── README.md                    # Documentation
```

## API Endpoints

### Sessions
- `GET /sessions/add` - Add session page
- `POST /sessions/add` - Create new session
- `GET /sessions/list` - Get all sessions
- `DELETE /sessions/delete/<id>` - Delete session

### Goals
- `POST /goals/add` - Create new goal
- `GET /goals/list` - Get all goals
- `DELETE /goals/delete/<id>` - Delete goal

### Dashboard
- `GET /` - Dashboard page
- `GET /api/dashboard-stats` - Get dashboard statistics

## Database Schema

### StudySessions Table
| Column      | Type     | Description           |
|-------------|----------|-----------------------|
| id          | Integer  | Primary key           |
| subject     | String   | Study subject         |
| duration    | Float    | Duration in hours     |
| topic       | String   | Topic covered         |
| study_date  | Date     | Date of study         |
| created_at  | DateTime | Record creation time  |

### Goals Table
| Column        | Type     | Description           |
|---------------|----------|-----------------------|
| id            | Integer  | Primary key           |
| goal_type     | String   | 'daily' or 'weekly'   |
| target_hours  | Float    | Target study hours    |
| deadline      | Date     | Goal deadline         |
| progress      | Float    | Current progress %    |
| is_active     | Boolean  | Active status         |
| created_at    | DateTime | Record creation time  |

## Troubleshooting

### Port already in use
If port 5000 is already in use, modify `run.py`:
```python
app.run(debug=True, host='0.0.0.0', port=5001)
```

### Database errors
Delete the database file and restart:
```bash
rm database/study_tracker.db
python run.py
```

### Module not found errors
Ensure virtual environment is activated and dependencies are installed:
```bash
pip install -r requirements.txt
```

## Development

### Adding new features
1. Create model in `app/models/`
2. Create routes in `app/routes/`
3. Add business logic in `app/services/`
4. Create templates in `app/templates/`
5. Add styles in `app/static/css/`
6. Add JavaScript in `app/static/js/`

### Running in production
For production deployment, use a WSGI server like Gunicorn:
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 run:app
```

## Support

For issues or questions, please refer to the README.md file or create an issue in the repository.

## License

MIT License - Feel free to use this project for your portfolio or learning purposes.
