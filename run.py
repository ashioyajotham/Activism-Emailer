from app import create_app, db
from app.models import Campaign

def init_test_data():
    app = create_app()
    with app.app_context():
        # Clear existing data
        db.drop_all()
        db.create_all()
        
        # Create test campaign
        test_campaign = Campaign(
            title="Save the Local Park",
            description="Support our campaign to protect the local park from development",
            target_email="citycouncil@example.com",
            email_template="""Dear City Council,

I am writing to express my concern about the proposed development of our local park.
This space is vital to our community's wellbeing and environmental health.

Please reject the current development proposal.

Sincerely,
[Your Name]""",
            goal=1000
        )

          # Animal Vaccination Campaign
        vaccination_campaign = Campaign(
            title="Stop Forced Animal Vaccination in Kenya",
            description="Campaign against the mandatory vaccination program affecting livestock farmers across Kenya. This initiative impacts smallholder farmers' livelihoods and requires proper consultation.",
            target_email="ps@agriculture.go.ke",
            email_template="""Dear Principal Secretary,

I am writing to express serious concerns about the mandatory livestock vaccination program.

Key issues:
- Economic burden on smallholder farmers
- Lack of proper stakeholder consultation
- Need for flexible implementation timeline
- Impact on traditional farming practices

We request:
1. Suspension of mandatory requirements
2. Public participation in policy development
3. Consider alternative approaches that respect farmer choices

Sincerely,
[Your Name]""",
            goal=500
        )

        # Agricultural Bills Campaign
        agri_bills_campaign = Campaign(
            title="Protect Kenya's Food Security",
            description="Opposition to proposed agricultural bills that threaten local farming practices and food security. These bills could impact small-scale farmers and local food production.",
            target_email="clerk@parliament.go.ke",
            email_template="""Dear Clerk of the National Assembly,

I am writing regarding the proposed agricultural bills currently under consideration.

Critical concerns:
- Threat to small-scale farming
- Impact on local food production
- Excessive regulation of traditional farming
- Risk to food sovereignty

We urge the National Assembly to:
1. Extend public participation period
2. Conduct impact assessment on small-scale farmers
3. Review provisions affecting traditional farming practices

Sincerely,
[Your Name]""",
            goal=1000
        )
        
        db.session.add(test_campaign)
        db.session.add(vaccination_campaign)
        db.session.add(agri_bills_campaign)
        db.session.commit()

app = create_app()

if __name__ == '__main__':
    init_test_data()
    app.run(debug=True)