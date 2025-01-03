from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from markupsafe import Markup
from config import Config
from datetime import datetime
from flask import render_template

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__, 
                static_folder='../static',
                static_url_path='/static')
    app.config.from_object(Config)
    
    db.init_app(app)
    migrate.init_app(app, db)
    
    # Register CLI commands
    from .cli import db_cli
    app.cli.add_command(db_cli)
    
    # Register template filters
    @app.template_filter('nl2br')
    def nl2br_filter(s):
        if not s:
            return ""
        return Markup(s.replace('\n', '<br>\n'))
    
    @app.template_filter('datetime')
    def format_datetime(value):
        if value is None:
            return ""
        return value.strftime('%B %d, %Y %H:%M')
    
    @app.context_processor
    def utility_processor():
        return dict(now=datetime.now())
    
    from .routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    @app.errorhandler(500)
    def internal_error(error):
        return render_template('errors/500.html'), 500

    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)