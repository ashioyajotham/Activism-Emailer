from . import db
from .models import Campaign, EmailTemplate, Recipient
from datetime import datetime

def initialize_data():
    """Initialize database with seed data"""
    # Create templates first
    templates = create_templates()
    db.session.add_all(templates.values())
    db.session.commit()
    
    # Create recipients
    recipients = create_recipients()
    for group in recipients.values():
        db.session.add_all(group)
    db.session.commit()
    
    # Create campaigns
    campaigns = create_campaigns(templates, recipients)
    db.session.add_all(campaigns)
    db.session.commit()

def create_templates():
    return {
        'abduction': EmailTemplate(
            subject='Urgent: Concern Regarding State Abductions in Kenya',
            body='''Dear Sir/Madam,

I am writing as a deeply concerned citizen regarding the increasing reports of state abductions in Kenya. This escalating human rights issue demands immediate attention and action.

Key Concerns:
1. Rising number of unexplained disappearances
2. Lack of transparency in investigations
3. Limited accountability for perpetrators
4. Impact on families and communities

We urgently request:
- Immediate investigation of all reported cases
- Public disclosure of findings
- Protection for witnesses and families
- Implementation of preventive measures

Your immediate action on this matter is crucial.

Sincerely,
[Your Name]'''
        ),
        'vaccination': EmailTemplate(
            subject='Urgent: Stop Dangerous Forced Animal Vaccination Programs',
            body='''Dear Sir/Madam,

We, concerned citizens and animal welfare advocates, write regarding the forced vaccination program being implemented on animals.

Key Issues:
1. Safety concerns with untested vaccines
2. No proper consultation with stakeholders
3. Reports of adverse reactions in animals
4. Lack of transparent protocols

We demand:
- Immediate suspension of forced vaccination
- Public disclosure of vaccine safety data
- Stakeholder consultation process
- Optional vaccination policy

We await your urgent response.

Sincerely,
[Your Name]'''
        ),
        'term_limits': EmailTemplate(
            subject='Urgent: Opposition to Unlawful Extension of Presidential Term Limits',
            body='''Dear Sir/Madam,

I am writing to express grave concern regarding attempts to extend presidential term limits, which represents a serious threat to our democratic principles and constitutional order.

Key Issues:
1. Violation of constitutional term limits
2. Undermining democratic transitions
3. Risk of authoritarian consolidation
4. Precedent for future constitutional violations

We demand:
- Immediate cessation of term extension efforts
- Respect for constitutional term limits
- Protection of democratic processes
- Transparent succession planning

This matter requires immediate attention to preserve our democratic institutions.

Sincerely,
[Your Name]'''
        )
    }

def create_recipients():
    return {
        'human_rights': [
            Recipient(
                name='Amnesty International',
                email='amnestykenya@amnesty.org',
                organization='Amnesty International'
            ),
            Recipient(
                name='UNHRC',
                email='infodesk@ohchr.org',
                organization='UN Human Rights Council'
            ),
            Recipient(
                name='Front Line Defenders',
                email='info@frontlinedefenders.org',
                organization='Front Line Defenders'
            )
        ],
        'animal_welfare': [
            Recipient(
                name='Ministry of Agriculture',
                email='info@kilimo.go.ke',
                organization='Ministry of Agriculture, Kenya'
            ),
            Recipient(
                name='Kenya Veterinary Board',
                email='info@kenyavetboard.or.ke',
                organization='Kenya Veterinary Board'
            ),
            Recipient(
                name='Kenya Society for Protection of Animals',
                email='info@kspca.org',
                organization='KSPCA'
            )
        ],
        'governance': [
            Recipient(
                name='Law Society of Kenya',
                email='lsk@lsk.or.ke',
                organization='Law Society of Kenya'
            ),
            Recipient(
                name='Kenya National Commission on Human Rights',
                email='info@knchr.org',
                organization='KNCHR'
            ),
            Recipient(
                name='Transparency International Kenya',
                email='transparency@tikenya.org',
                organization='TI Kenya'
            )
        ]
    }

def create_campaigns(templates, recipients):
    return [
        Campaign(
            title='Stop State Abductions',
            description='Campaign against state-sponsored abductions',
            status='active',
            news_links=[
                {
                    'title': 'Human Rights Watch Report',
                    'url': 'https://www.hrw.org/kenya-abductions',
                    'description': 'Latest analysis on state abductions'
                },
                {
                    'title': 'Amnesty Report 2023',
                    'url': 'https://www.amnesty.org/kenya',
                    'description': 'Documentation of recent cases'
                }
            ],
            template=templates['abduction'],
            recipients=recipients['human_rights']  # Add recipients
        ),
        Campaign(
            title='Stop Term Limits Extension',
            description='Opposition to unlawful extension of presidential term limits',
            background='Recent attempts to modify constitutional term limits...',
            impact='This undermines democratic principles...',
            news_links=[
                {
                    'title': 'Constitutional Analysis',
                    'url': 'https://constitutionnet.org/country/kenya',
                    'description': 'Legal perspective on term limits'
                },
                {
                    'title': 'Democracy Watch Report',
                    'url': 'https://freedomhouse.org/country/kenya',
                    'description': 'Impact on democratic institutions'
                }
            ],
            status='urgent',
            template=templates['term_limits'],
            recipients=recipients['governance']  # Add recipients
        ),
        Campaign(
            title='Stop Forced Animal Vaccination',
            description='Campaign against dangerous forced animal vaccination programs',
            background='Recent reports of adverse reactions in animals...',
            impact='This poses a threat to animal welfare...',
            news_links=[
                {
                    'title': 'Animal Rights Report',
                    'url': 'https://animalrights.org/vaccination',
                    'description': 'Impact on animal health'
                },
                {
                    'title': 'Vet Association Statement',
                    'url': 'https://vetsociety.org/vaccination',
                    'description': 'Safety concerns with vaccines'
                }
            ],
            status='active',
            template=templates['vaccination'],
            recipients=recipients['animal_welfare']
        )
    ]