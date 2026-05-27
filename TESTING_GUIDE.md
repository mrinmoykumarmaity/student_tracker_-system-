# Testing Guide - Student Study Tracker

## Quick Test Setup

### 1. Install and Run
```bash
cd study_tracker
python -m venv venv
venv\Scripts\activate  # Windows
pip install -r requirements.txt
python run.py
```

### 2. Seed Demo Data (Optional)
```bash
python seed_data.py
```

This will populate your database with 30 days of sample study sessions and goals.

## Manual Testing Checklist

### Dashboard Page (/)

#### Stats Cards
- [ ] Total Hours displays correctly
- [ ] Today's Hours updates when sessions added
- [ ] This Week's Hours shows current week total
- [ ] Current Streak shows consecutive study days

#### Goals Section
- [ ] Click "Add Goal" button opens modal
- [ ] Create daily goal (e.g., 3 hours)
- [ ] Create weekly goal (e.g., 20 hours)
- [ ] Progress bars update correctly
- [ ] Delete goal works

#### Charts
- [ ] Daily Trend Chart displays last 7 days
- [ ] Subject Distribution Chart shows pie chart
- [ ] Charts are responsive
- [ ] Hover shows data tooltips

#### Recent Sessions
- [ ] Shows last 5 sessions
- [ ] Displays date, subject, topic, duration
- [ ] Empty state shows when no sessions

### Add Session Page (/sessions/add)

#### Form Validation
- [ ] All fields are required
- [ ] Duration accepts decimal values (e.g., 2.5)
- [ ] Date picker works correctly
- [ ] Default date is today

#### Adding Sessions
- [ ] Fill form and submit
- [ ] Success toast notification appears
- [ ] Form resets after submission
- [ ] Session appears in Recent Sessions list

#### Recent Sessions List
- [ ] Shows newly added sessions
- [ ] Delete button works
- [ ] Confirmation dialog appears before delete
- [ ] List updates after deletion

### Analytics Page (/analytics)

#### Key Metrics
- [ ] Average Daily Hours calculated correctly
- [ ] Best Streak displays
- [ ] Total Sessions count accurate
- [ ] Most Studied Subject shows

#### Charts
- [ ] Weekly Trend Chart (4 weeks)
- [ ] Daily Pattern Chart (7 days)
- [ ] Subject Distribution Chart

#### Sessions Table
- [ ] All sessions displayed
- [ ] Search functionality works
- [ ] Subject filter works
- [ ] Delete button works
- [ ] Empty state when no results

### Dark Mode

#### Theme Toggle
- [ ] Click theme toggle in sidebar
- [ ] Page switches to dark mode
- [ ] All elements visible in dark mode
- [ ] Charts update colors
- [ ] Preference saved (refresh page)
- [ ] Toggle back to light mode works

### Responsive Design

#### Mobile View (< 768px)
- [ ] Hamburger menu appears
- [ ] Sidebar slides in/out
- [ ] Stats cards stack vertically
- [ ] Charts are responsive
- [ ] Forms are usable
- [ ] Tables scroll horizontally

#### Tablet View (768px - 1024px)
- [ ] Layout adjusts appropriately
- [ ] All features accessible
- [ ] Charts display correctly

## Feature Testing Scenarios

### Scenario 1: New User Experience
1. Open app for first time
2. See empty states on dashboard
3. Navigate to Add Session
4. Add first study session
5. Return to dashboard
6. Verify stats updated
7. Create a goal
8. Verify goal appears

### Scenario 2: Daily Usage
1. Add morning study session
2. Check dashboard stats
3. Add afternoon session
4. Verify daily total updates
5. Check goal progress
6. View analytics

### Scenario 3: Week Review
1. Navigate to Analytics
2. Review weekly trend
3. Check subject distribution
4. Search for specific topics
5. Filter by subject
6. Export data (future feature)

### Scenario 4: Goal Tracking
1. Create daily goal (3 hours)
2. Add 1.5 hour session
3. Check progress (50%)
4. Add another 1.5 hour session
5. Verify goal completion (100%)
6. Create new weekly goal

### Scenario 5: Streak Building
1. Add session today
2. Check current streak
3. Add sessions for consecutive days
4. Verify streak increases
5. Skip a day
6. Verify streak resets

## API Testing (Optional)

### Using curl or Postman

#### Get Dashboard Stats
```bash
curl http://localhost:5000/api/dashboard-stats
```

#### Add Study Session
```bash
curl -X POST http://localhost:5000/sessions/add \
  -H "Content-Type: application/json" \
  -d '{
    "subject": "Mathematics",
    "duration": 2.5,
    "topic": "Calculus",
    "study_date": "2026-05-27"
  }'
```

#### Get All Sessions
```bash
curl http://localhost:5000/sessions/list
```

#### Add Goal
```bash
curl -X POST http://localhost:5000/goals/add \
  -H "Content-Type: application/json" \
  -d '{
    "goal_type": "daily",
    "target_hours": 3.0,
    "deadline": "2026-05-28"
  }'
```

#### Get Goals
```bash
curl http://localhost:5000/goals/list
```

## Browser Compatibility

Test on:
- [ ] Chrome/Edge (latest)
- [ ] Firefox (latest)
- [ ] Safari (latest)
- [ ] Mobile browsers

## Performance Checks

- [ ] Page loads in < 2 seconds
- [ ] API responses < 500ms
- [ ] Charts render smoothly
- [ ] No console errors
- [ ] No memory leaks

## Known Limitations

1. **Single User**: No authentication system (future enhancement)
2. **Local Storage**: Database is local SQLite
3. **Export**: Export feature not yet implemented
4. **Notifications**: No reminder system yet

## Bug Reporting

If you find bugs, note:
1. Steps to reproduce
2. Expected behavior
3. Actual behavior
4. Browser and OS
5. Console errors (if any)

## Success Criteria

✅ All CRUD operations work
✅ Charts display correctly
✅ Dark mode functions properly
✅ Responsive on all devices
✅ No console errors
✅ Data persists after refresh
✅ Calculations are accurate

## Next Steps After Testing

1. Deploy to production (Heroku, Railway, etc.)
2. Add authentication
3. Implement export feature
4. Add email notifications
5. Create mobile app
6. Add social features

Happy Testing! 🚀
