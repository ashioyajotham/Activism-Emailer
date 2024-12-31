from flask import Blueprint, render_template, redirect, url_for
from .models import Campaign, EmailTemplate

main = Blueprint('main', __name__)

@main.route('/')
def index():
    campaigns = Campaign.query.all()
    return render_template('index.html', campaigns=campaigns)

@main.route('/campaign/<int:campaign_id>')
def campaign_details(campaign_id):
    campaign = Campaign.query.get_or_404(campaign_id)
    return render_template('campaign.html', campaign=campaign)

@main.route('/about')
def about():
    return render_template('about.html')

@main.route('/generate_email/<int:campaign_id>')
def generate_email(campaign_id):
    campaign = Campaign.query.get_or_404(campaign_id)
    # Email generation logic here
    return redirect(url_for('main.campaign_details', campaign_id=campaign_id))