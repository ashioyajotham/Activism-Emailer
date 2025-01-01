import click
from flask.cli import with_appcontext
from flask import current_app
from . import db
from .seed_data import initialize_data
from flask_migrate import Migrate, upgrade as _upgrade, init, migrate

@click.group(name='db')
def db_cli():
    """Database management commands."""
    pass

@db_cli.command('init')
@with_appcontext
def init_db_command():
    """Initialize database tables and migrations."""
    init()
    db.create_all()
    click.echo('Database initialized.')

@db_cli.command('migrate')
@click.option('--message', '-m', help='Migration message')
@with_appcontext
def migrate_db_command(message):
    """Generate new migration."""
    migrate(message=message)
    click.echo('Migration created.')

@db_cli.command('upgrade')
@with_appcontext
def upgrade_db_command():
    """Apply all migrations."""
    _upgrade()
    click.echo('Database upgraded.')

@db_cli.command('seed')
@with_appcontext
def seed_db():
    """Seed the database."""
    db.drop_all()
    db.create_all()
    initialize_data()
    click.echo('Database seeded successfully.')

@db_cli.command('reset')
@with_appcontext
def reset_db_command():
    """Reset database and seed."""
    if click.confirm('This will delete all data. Continue?'):
        # Drop and recreate tables
        db.drop_all()
        db.create_all()
        
        # Initialize with seed data
        try:
            initialize_data()
            click.echo('Database reset and seeded successfully!')
        except Exception as e:
            click.echo(f'Error seeding database: {e}', err=True)
            db.session.rollback()

def init_app(app):
    app.cli.add_command(db_cli)