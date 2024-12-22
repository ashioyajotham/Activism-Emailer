from flask import Blueprint, render_template, redirect, url_for, flash, abort, jsonify
from app.models import Campaign, db
from sqlalchemy.exc import SQLAlchemyError

main = Blueprint('main', __name__)

@main.route('/')
def index():
    try:
        campaigns = Campaign.query.all()
        return render_template('campaign.html', campaigns=campaigns)
    except SQLAlchemyError:
        flash('Unable to load campaigns. Please try again later.', 'error')
        return render_template('campaign.html', campaigns=[])

@main.route('/about')
def about():
    try:
        total_emails = db.session.query(db.func.sum(Campaign.total_emails)).scalar() or 0
        total_campaigns = Campaign.query.count()
        return render_template('about.html', 
                             total_emails=total_emails, 
                             total_campaigns=total_campaigns)
    except SQLAlchemyError:
        flash('Unable to load statistics. Please try again later.', 'error')
        return render_template('about.html', 
                             total_emails=0, 
                             total_campaigns=0)

@main.route('/record_email/<int:campaign_id>', methods=['POST'])
def record_email(campaign_id):
    try:
        campaign = Campaign.query.get_or_404(campaign_id)
        campaign.total_emails += 1
        db.session.commit()
        return '', 204
    except SQLAlchemyError:
        db.session.rollback()
        abort(500)

@main.route('/get_email_count')
def get_email_count():
    try:
        total_emails = db.session.query(db.func.sum(Campaign.total_emails)).scalar() or 0
        return jsonify({'total_emails': total_emails})
    except SQLAlchemyError:
        return jsonify({'error': 'Database error'}), 500

@main.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404

@main.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('errors/500.html'), 500