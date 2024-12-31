from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional
import json
from pathlib import Path
from flask_sqlalchemy import SQLAlchemy
from app import db
from flask import Blueprint, render_template, redirect, url_for

class Campaign(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(50), default='active')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    template_id = db.Column(db.Integer, db.ForeignKey('email_template.id'))
    template = db.relationship('EmailTemplate', backref='campaigns')
    recipients = db.relationship('Recipient', 
                               secondary='campaign_recipients',
                               backref=db.backref('campaigns', lazy='dynamic'))

class Recipient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    organization = db.Column(db.String(200))

class EmailTemplate(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(200), nullable=False)
    body = db.Column(db.Text, nullable=False)

# Junction table
campaign_recipients = db.Table('campaign_recipients',
    db.Column('campaign_id', db.Integer, db.ForeignKey('campaign.id'), primary_key=True),
    db.Column('recipient_id', db.Integer, db.ForeignKey('recipient.id'), primary_key=True)
)

from .models import Campaign, Recipient, EmailTemplate

main = Blueprint('main', __name__)

@main.route('/')
def index():
    campaigns = Campaign.query.all()  # Returns list of Campaign objects
    return render_template('index.html', campaigns=campaigns)