from app.models import EmailTemplate, Campaign

def test_index_page(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Hamasisho' in response.data

def test_campaign_details(client, init_database):
    template = EmailTemplate(subject='Test', body='Test')
    init_database.session.add(template)
    
    campaign = Campaign(
        title='Test Campaign',
        description='Test Description',
        template=template
    )
    init_database.session.add(campaign)
    init_database.session.commit()
    
    response = client.get(f'/campaign/{campaign.id}')
    assert response.status_code == 200
    assert b'Test Campaign' in response.data