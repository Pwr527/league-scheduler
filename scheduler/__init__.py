import os
import click
from flask import Flask, render_template, current_app
from flask.cli import with_appcontext
from flask_sqlalchemy import SQLAlchemy
import importlib

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    app.config.from_mapping(
        SECRET_KEY='dev',
        SQLALCHEMY_DATABASE_URI = os.environ["DATABASE_URL"].replace('postgres://', 'postgresql://'),
        SQLALCHEMY_TRACK_MODIFICATIONS = False,
        LAYOUT = "_layout.html"
    )

    from .controllers import team, schedule, place, api
    
    app.register_blueprint(team.bp)
    app.register_blueprint(place.bp)
    app.register_blueprint(schedule.bp)
    app.register_blueprint(api.bp)

    db.init_app(app)
   
    @app.before_first_request
    def init_db():
        try:
            print("creating tables")
            db.create_all()
        except Exception as e:
            print(f"Error creating tables: {e}")

    @app.route('/')
    def index():
        return render_layout()

    @app.cli.command("drop-db")
    def drop_db():
        click.echo("drop db")
        db.drop_all()

    @app.cli.command("create-db")
    def create_db():
        click.echo("create db")
        db.create_all()

    return app

def render_layout(**kwargs):
    return render_template(current_app.config['LAYOUT'], **kwargs)
