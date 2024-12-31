from flask import Blueprint, render_template, redirect, url_for, flash, jsonify
from .models import Campaign, EmailTemplate

main = Blueprint('main', __name__)

@main.route('/')
def index():
    try:
        campaigns = Campaign.query.all()
        return render_template('index.html', campaigns=campaigns)
    except Exception as e:
        flash(f'Error loading campaigns: {str(e)}', 'error')
        return render_template('index.html', campaigns=[])

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
    recipients = ','.join([r.email for r in campaign.recipients])
    mailto_link = f"mailto:{recipients}?subject={campaign.template.subject}&body={campaign.template.body}"
    return jsonify({
        'mailto': mailto_link,
        'subject': campaign.template.subject,
        'body': campaign.template.body
    })