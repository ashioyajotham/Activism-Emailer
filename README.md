# Hamasisho - Digital Activism Platform

## Overview
Hamasisho enables citizens to engage in social justice campaigns through coordinated email actions.

## Features
- Campaign management and tracking
- Email template generation
- Campaign status monitoring
- Responsive design
- Search and filter capabilities
- Vercel Speed Insights integration

## Tech Stack
- Python/Flask
- SQLAlchemy
- SQLite
- HTML/CSS/JavaScript
- Vercel (Deployment)

## Branches
- `main`: Production branch, auto-deploys to Vercel
- `development`: Development branch for new features

## Installation

### Prerequisites
- Python 3.8+
- pip
- Git

### Setup
```batch
# Clone repository
git clone https://github.com/ashioyajotham/activism_emailer.git
cd activism_emailer

# Switch to development branch
git checkout development

# Create virtual environment
python -m venv venv
.\venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Initialize database
flask db init
flask db upgrade
flask db seed
```

## Development Workflow
1. Create feature branch from development
2. Make changes and test locally
3. Push changes to feature branch
4. Create PR to development branch
5. Test in Vercel Preview
6. Merge to development
7. Create PR to main when ready
8. Deploy to production

## Configuration
Create a .env file:
```
FLASK_APP=wsgi.py
FLASK_ENV=development
SECRET_KEY=your-secret-key
```

## Project Structure
```
activism_emailer/
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│   └── templates/
├── static/
│   ├── css/
│   └── js/
├── tests/
├── .env
├── config.py
└── wsgi.py
```

## Deployment
- Production: Auto-deploys from main branch
- Preview: Available for PRs to development
- Analytics: Vercel Speed Insights enabled

## Contributing
1. Fork repository
2. Create feature branch from development
3. Make changes
4. Submit PR to development branch
5. Request review

## License
This project is licensed under the [Hamasisho Social Good License](LICENSE.md). Free for non-commercial use and social activism purposes.
