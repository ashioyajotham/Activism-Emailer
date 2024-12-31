import re
import json
import logging
from pathlib import Path
from typing import Dict, Any
from datetime import datetime
import hashlib
from urllib.parse import quote

def validate_email(email: str) -> bool:
    """Validate email address format"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

def generate_slug(text: str) -> str:
    """Convert text to URL-friendly slug"""
    text = text.lower().strip()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[-\s]+', '-', text)
    return text

def generate_campaign_id(title: str, timestamp: datetime) -> str:
    """Generate unique campaign ID"""
    string = f"{title}{timestamp.isoformat()}"
    return hashlib.md5(string.encode()).hexdigest()[:10]

def load_campaign_data(file_path: str) -> Dict[str, Any]:
    """Load campaign data from JSON file"""
    path = Path(file_path)
    if not path.exists():
        return {}
    try:
        with open(path, 'r') as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        logging.error(f"Error loading campaign data: {e}")
        return {}

def save_campaign_data(data: Dict[str, Any], file_path: str) -> bool:
    """Save campaign data to JSON file"""
    try:
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=2)
        return True
    except Exception as e:
        logging.error(f"Error saving campaign data: {e}")
        return False

def process_email_template(template: str, **kwargs) -> str:
    """Replace template placeholders with actual values"""
    for key, value in kwargs.items():
        template = template.replace(f"[{key}]", str(value))
    return template

def generate_mailto_link(to: str, subject: str, body: str) -> str:
    """Generate mailto link with encoded parameters"""
    return f"mailto:{to}?subject={quote(subject)}&body={quote(body)}"

def setup_logging():
    """Configure logging for the application"""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler('app.log'),
            logging.StreamHandler()
        ]
    )