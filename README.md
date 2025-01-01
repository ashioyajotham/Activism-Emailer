# Hamasisho - Digital Activism Platform

## Overview
Hamasisho is a digital activism platform that enables citizens to engage in social justice campaigns through coordinated email actions.  

## Features
- Campaign management and tracking
- Email template generation
- Campaign status monitoring
- Responsive design
- Search and filter capabilities

## Tech Stack
- Python/Flask
- SQLAlchemy
- SQLite
- HTML/CSS/JavaScript
- Vercel (Deployment)

## Installation

### Prerequisites
- Python 3.8+
- pip
- Git

### Setup
```bash
# Clone repository
git clone https://github.com/ashioyajotham/activism_emailer.git
cd activism_emailer

# Create virtual environment
python -m venv venv
.\venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Initialize database
flask db upgrade

# Run application
flask run
```