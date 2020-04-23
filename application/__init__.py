from flask import Flask
from application.views.user import user_page
from application.extension import db
import os
import click
from application.models import User
from werkzeug.security import generate_password_hash


def create_app(config_name=None):
    if config_name is None:
        config_name = os.getenv('FLASK_CONFIG', 'development')

    app = Flask('application')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.secret_key = "lalskskskskksksjsj"

    register_extensions(app)
    register_blueprints(app)
    register_commands(app)

    return app


def register_extensions(app):
    db.init_app(app)

def register_blueprints(app):
    app.register_blueprint(user_page)

def register_commands(app):
    @app.cli.command()
    def forge():
        """Generate fake data."""
        db.drop_all()
        db.create_all()

        hash_password = generate_password_hash('123456')
        user = User(username="admin", gender=0, email="admin@admin.com", password=hash_password)
        user1 = User(username="123455", gender=1, email="admin234@admin.com", password=hash_password)

        db.session.add(user)
        db.session.add(user1)
        db.session.commit()
        click.echo('Done.')

