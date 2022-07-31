from flask import (
    g, Blueprint, render_template, request, session, url_for, current_app, redirect
)
from scheduler.models import *
from scheduler import render_layout, db

bp = Blueprint("team", __name__, url_prefix="/teams")
  
@bp.route('/', methods=['GET'])
def index():
    return render_layout()

@bp.route('/<id>', methods=['GET'])
def view(id: int):
    places = Place.query.all()

@bp.route('/', methods=['POST'])
def create():
    if 'name' in request.form:
        team = Team(request.form['name'])
        db.session.add(team)
        db.session.commit()
        return redirect(url_for('team.index'))
    else:
        return render_layout()
