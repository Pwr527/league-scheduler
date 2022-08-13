import os
import click
from flask import Flask, render_template, current_app
from flask.cli import with_appcontext
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

db = SQLAlchemy()

def create_app():
    print(f"BASE PATH: {os.path.dirname(os.path.dirname(os.path.abspath(__file__)))}")
    app = Flask(__name__, static_folder="/app/frontend/build/static", template_folder="/app/frontend/build")
    cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

    app.config.from_mapping(
        SECRET_KEY='dev',
        SQLALCHEMY_DATABASE_URI = os.environ["DATABASE_URL"].replace('postgres://', 'postgresql://'),
        SQLALCHEMY_TRACK_MODIFICATIONS = False,
        LAYOUT =  "index.html",
        CORS_HEADERS = "Content-Type"

    )

    from . import api
    app.register_blueprint(api.bp)

    db.init_app(app)
   
    @app.before_first_request
    def init_db():
        try:
            print("creating tables")
            db.create_all()
        except Exception as e:
            print(f"Error creating tables: {e}")

    @app.route('/', defaults={'path': ''})
    @app.route('/<path:path>')
    def index(path):
        return render_template('index.html')

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
