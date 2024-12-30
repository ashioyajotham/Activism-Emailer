from app import db
from app.models import Campaign

def load_test_data():
    db.drop_all()
    db.create_all()
    
    campaigns = [
        Campaign(
            title="Save the Local Park",
            description="Support our campaign to protect the local park from development",
            target_email="info@nairobi.go.ke",
            email_template="""Dear City Council,

I am writing to express my concern about the proposed development of our local park.
This space is vital to our community's wellbeing and environmental health.

Please reject the current development proposal.

Sincerely,
[Your Name]"""
        ),

        Campaign(
            title="Support Missing Persons Investigations", 
            description="Help improve resources for missing persons cases",
            target_email="amnesty.kenya@amnesty.or.ke, ohchr-InfoDesk@un.org, thehague@fidh.org, info@frontlinedefenders.org, au-banjul@africa-union.org",
            email_template="""Hi,

I am writing to you as a deeply concerned citizen of Kenya to express my alarm regarding the increasing reports of state abductions in our country. This escalating human rights issue is causing widespread fear and instability, and I believe it is crucial to address it urgently.
I am particularly troubled by the apparent impunity with which these abductions are being carried out. The lack of accountability for perpetrators and the absence of transparent investigations are eroding public trust and creating a climate of fear.
As a concerned citizen, I want to contribute to efforts to stop these human rights abuses and ensure the safety and security of all Kenyans. I believe your organization plays a vital role in defending human rights and holding the government accountable.
I would be grateful if you could provide information on how ordinary citizens like myself can safely and effectively support your work in addressing this issue. Specifically, I am interested in learning more about:
How to report concerns or information about potential abductions while ensuring my safety.
Ways to support advocacy efforts aimed at raising awareness about state abductions and demanding accountability.
Any available resources or initiatives that empower citizens to protect themselves and their communities from these threats.
I understand the sensitivity of this issue and want to emphasize my commitment to acting responsibly and within the bounds of the law.

Thank you for your time, dedication. I look forward to hearing from you soon!

Sincerely,
A Concerned Kenyan Citizen"""
        )
    ]
    
    for campaign in campaigns:
        db.session.add(campaign)
    db.session.commit()