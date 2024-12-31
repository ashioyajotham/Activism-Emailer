from app import create_app, db
from app.models import Campaign, Recipient, EmailTemplate
import os

def init_db():
    app = create_app()
    
    with app.app_context():
        # Create database if it doesn't exist
        if not os.path.exists('instance'):
            os.makedirs('instance')
            
        # Initialize database structure
        db.create_all()
        print("Database structure created successfully!")

if __name__ == '__main__':
    init_db()