from app import db

class Campaign(db.Model):
    __tablename__ = 'campaigns'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    target_email = db.Column(db.String(120), nullable=False)
    email_template = db.Column(db.Text, nullable=False)
    total_emails = db.Column(db.Integer, default=0)
    goal = db.Column(db.Integer, default=100)