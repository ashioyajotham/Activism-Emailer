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
Concerned Kenyan citizen'''
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
Concerned Kenyan citizen'''
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
Concerned Kenyan citizen'''
        ),
        'icc_revival': EmailTemplate(
            subject='Urgent: Revive ICC Cases for Post-Election Violence Justice',
            body='''Dear Sir/Madam,

I am writing to urge the revival of ICC cases related to Kenya's 2007/2008 post-election violence, particularly those that were dropped due to witness interference.

Key Points:
1. Systematic witness interference led to case collapses
2. Victims still await justice
3. New evidence has emerged
4. Pattern of witness disappearances needs investigation

We request:
- Reopening of dropped cases
- Investigation of witness interference
- Protection mechanisms for witnesses
- Swift action for justice

Regards,
Concerned Kenyan citizen'''
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
            ),            
            Recipient(
                name='Volker Türk',
                email='unvfvt@ohchr.org',
                position='UN Commissioner for Human Rights'
            ),
            Recipient(
                name='WGEID',
                email='hrc-wg-eid@un.org',
                position='Working Group on Enforced Disappearances'
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
            ),
            Recipient(
                name='Office of the President',
                email='president@president.go.ke',
                position='President'
            )
        ],
        'icc': [
            Recipient(
                name='ICC Prosecutor',
                email='otp.informationdesk@icc-cpi.int',
                position='Office of the Prosecutor'
            ),
            Recipient(
                name='ICC Registry',
                email='registry@icc-cpi.int',
                position='Registry Division'
            ),
            Recipient(
                name='UN Human Rights Council',
                email='registry@ohchr.org',
                position='Office of the High Commissioner'
            ),
            Recipient(
                name='Kenya Human Rights Commission',
                email='admin@khrc.or.ke',
                position='Executive Director'
            ),
            Recipient(
                name='ICC Victims and Witnesses Unit',
                email='vwu@icc-cpi.int',
                position='Head of Unit'
            )
        ]
    }

def create_campaigns(templates, recipients):
    return [
        Campaign(
            title='Stop State Abductions',
            description='Campaign against state-sponsored abductions',
            background='Rising cases of unexplained disappearances by state security forces targeting activists and asylum seekers has risen alarmingly',
            impact='Creates climate of fear and undermines rights of citizens as well as asylum seekers as stipulated in the constitution and 1951 Refugee Convention',
            news_links=[
                {
                    'title': 'Amnesty Kenya Statement',
                    'url': 'https://www.amnestykenya.org/statement-on-the-abduction-and-disappearance-of-seven-turkish-asylum-seekers-for-immediate-release/',
                    'description': 'Statement on the abduction and disappearance of asylum seekers'
                },
                {
                    'title': 'Human Rights Watch Report',
                    'url': 'https://www.hrw.org/news/2024/11/06/kenya-security-forces-abducted-killed-protesters',
                    'description': 'Latest findings on state abductions'
                },
                {
                    'title': 'Abductions as a National Security Threat',
                    'url': 'https://www.dw.com/en/why-abductions-in-kenya-pose-a-threat-to-national-security/a-71191494',
                    'description': 'Analysis of abductions as a national security threat'
                }
            ],
            status='urgent',
            template=templates['abduction'],
            recipients=recipients['human_rights'],
            timeline=[
                {
                    'date': 'December 2024',
                    'description': 'Multiple new cases reported across different counties with Ruto promising to stop if citizens become "obedient"'
                },
                {
                    'date': 'November 2024',
                    'description': 'Kenya Kwanza "pauses" abductions but issues subtle threats'
                }
            ],
            key_issues=[
                'Rising number of enforced disappearances',
                'Targeting of activists and asylum seekers',
                'State denial and lack of accountability',
                'Violation of constitutional rights'
            ]
        ),
        Campaign(
            title='Fufua ICC',
            description='Campaign to push ICC to reopen 2007/8 PEV cases dropped due to witness interference',
            background='The 2007/2008 post-election violence cases at ICC were dropped after systematic witness interference, leaving victims without justice.',
            impact='Reopening these cases would address impunity and ensure justice for PEV victims.',
            news_links=[
                {
                    'title': 'ICC Witness Interference Report',
                    'url': 'https://www.icc-cpi.int/kenya',
                    'description': 'Documentation of witness interference patterns'
                },
                {
                    'title': '2007/8 PEV Perpetrators',
                    'url': 'https://drive.google.com/file/d/1B1kY4Cx3_1w_HXwD_ynTSu2dBLbIk8mT/view',
                    'description': 'List of known perpetrators and their current status'
                }
            ],
            status='urgent',
            template=templates['icc_revival'],
            recipients=recipients['icc'],
            timeline=[
                {
                    'date': 'December 2024',
                    'description': 'Memories are still fresh as victims commemorate 17th anniversary of PEV'
                },
                {
                    'date': 'December 2010',
                    'description': 'ICC prosecutor opens investigation into 2007/8 PEV cases'
                },
                {
                    'date': 'December 2007',
                    'description': 'Victims groups file petition for case reopening'
                }
            ],
            key_issues=[
                'Systematic witness interference',
                'Delayed justice for PEV victims',
                'Culture of impunity',
                'Need for witness protection'
            ]
        ),
        Campaign(
            title='Stop Forced Animal Vaccination',
            description='Campaign against dangerous forced animal vaccination programs',
            background='Recent reports of forced animal vaccination programs have raised concerns about the safety and transparency of the process.',
            impact='This poses a threat to animal welfare and public health, and undermines trust in veterinary services.',
            news_links=[
                {
                    'title': 'Veterinary Report',
                    'url': 'https://www.vetreport.org',
                    'description': 'Analysis of vaccination impacts'
                }
            ],
            status='active',
            template=templates['vaccination'],
            recipients=recipients['animal_welfare'],
            timeline=[
                {
                    'date': 'December 2024',
                    'description': 'New regulations proposed for mandatory vaccinations'
                },
                {
                    'date': 'November 2024',
                    'description': 'Animal welfare groups report adverse effects'
                }
            ],
            key_issues=[
                'Lack of proper testing protocols',
                'Animal welfare concerns',
                'Forced implementation',
                'Inadequate monitoring of side effects'
            ]
        ),
        Campaign(
            title='Stop Term Limits Extension',
            description='Opposition to unlawful extension of presidential term limits',
            background='Recent attempts to modify constitutional term limits...',
            impact='This undermines democratic principles and sets a dangerous precedent for future violations.',
            news_links=[
                {
                    'title': 'Constitutional Analysis',
                    'url': 'https://constitutionnet.org',
                    'description': 'Legal implications of term extensions'
                }
            ],
            status='archived',
            template=templates['term_limits'],
            recipients=recipients['governance'],
            timeline=[
                {
                    'date': 'November 2024',
                    'description': 'Parliament gathers public opinion on term extension'
                },
                {
                    'date': 'October - November 2024',
                    'description': "Twitter protests against term extension gain momentum after Cherargei's comments"
                }
            ]
        )
    ]
    db.session.add_all(campaigns)
    db.session.commit()
    return campaigns