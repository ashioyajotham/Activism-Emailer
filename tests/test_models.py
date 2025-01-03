import pytest
from app.models import Campaign, EmailTemplate, Recipient

def test_create_campaign(init_database):
    # Clear any existing data
    Campaign.query.delete()
    EmailTemplate.query.delete()
    init_database.session.commit()
    
    # Create test data
    template = EmailTemplate(
        subject='Test Subject',
        body='Test Body'
    )
    init_database.session.add(template)
    
    campaign = Campaign(
        title='Test Campaign',
        description='Test Description',
        background='Test Background',
        impact='Test Impact',
        status='active',
        template=template
    )
    init_database.session.add(campaign)
    init_database.session.commit()
    
    # Verify
    assert Campaign.query.count() == 1
    saved_campaign = Campaign.query.first()
    assert saved_campaign.title == 'Test Campaign'
    assert saved_campaign.template.subject == 'Test Subject'