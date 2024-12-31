from flask import Blueprint, render_template, redirect, url_for, flash, jsonify, current_app
from .models import Campaign, EmailTemplate
from urllib.parse import quote

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
    return render_template('campaign_details.html', campaign=campaign)

@main.route('/about')
def about():
    return render_template('about.html')

@main.route('/generate_email/<int:campaign_id>')
def generate_email(campaign_id):
    try:
        campaign = Campaign.query.get_or_404(campaign_id)
        recipients = ','.join(r.email for r in campaign.recipients)
        
        # Properly encode body and subject for mailto
        body = quote(campaign.template.body)
        subject = quote(campaign.template.subject)
        
        mailto_url = f"mailto:{recipients}?subject={subject}&body={body}"
        
        return jsonify({
            'status': 'success',
            'mailto': mailto_url,
            'recipients': recipients,
            'subject': campaign.template.subject,
            'body': campaign.template.body
        })
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500