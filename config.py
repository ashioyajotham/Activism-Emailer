import os
import secrets

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///campaigns.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-key')
    
    # App settings
    DEBUG = True
    TEMPLATES_AUTO_RELOAD = True
    
    # Campaign settings
    CAMPAIGNS_FILE = 'campaigns.json'
    MAX_CAMPAIGNS = 100