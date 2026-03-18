# Flask Online Bank Setup Guide

## Project Structure

Your project is now organized as a Flask application:

```
online bank/
├── main.py                 # Flask application (main entry point)
├── requirements.txt        # Python dependencies
├── templates/              # Flask templates (HTML pages)
│   ├── base.html          # Base template with layout & navigation
│   ├── index.html         # Home page
│   ├── services.html      # Services page (with modal functionality)
│   ├── login.html         # Login page
│   ├── signup.html        # Sign up page
│   ├── about.html         # About page
│   ├── contact.html       # Contact page
│   ├── profile.html       # profile page
    └── forgotpassword.html # Forgot password page
└── static/                 # Static files (CSS, JS, images)
    ├── css/
    │   ├── style.css      # Main styles for all pages
    │   └── services.css   # Services page specific styles
    └── js/
        └── main.js        # JavaScript for navigation & forms
```

## Setup Instructions

### 1. Install Dependencies

Run this command in your project directory:

```bash
pip install -r requirements.txt
```

Or if you're using a virtual environment:

```bash
python -m venv venv

# On Windows:
venv\Scripts\activate

# On Mac/Linux:
source venv/bin/activate

pip install -r requirements.txt
```

### 2. Run the Flask Application

```bash
python main.py
```

Or:

```bash
flask run
```

The application will be available at: **http://localhost:5000**

## What Changed

✅ **All HTML links**: Now use Flask's `url_for()` function for proper routing
  - Before: `href="services.html"`
  - After: `href="{{ url_for('services') }}"`

✅ **All CSS/JS links**: Now use Flask's `url_for()` with static files
  - Before: `<link rel="stylesheet" href="css/style.css">`
  - After: `<link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">`

✅ **Template inheritance**: All pages extend `base.html` for consistent layout
  - Reduces code duplication
  - Easy to update header/footer across all pages

✅ **Separated services.css**: Inline CSS from `services.html` is now in separate file
  - `static/css/services.css` for service page specific styles
  - Keeps CSS organized and maintainable

## Features Ready to Extend

The Flask app is ready for backend features:

- Add database connections (MySQL/SQLite)
- Implement form handling with POST routes
- Add user authentication
- Create API endpoints for banking operations

## Frontend Design Preserved

✨ The frontend design remains **exactly the same**. All styling, layout, and functionality work identically to the original design.

## Quick Testing

1. Visit **http://localhost:8000** → Home page with swiper slider
2. Click **Services** → Modal popups with forms work perfectly
3. Click **Login/Sign Up** → Form pages work as expected
4. All navigation links work properly throughout the site
5. Responsive design on mobile still works

- this project is still in complet , the rest of the features will coming soon , i working on it .. thankyou 
---


