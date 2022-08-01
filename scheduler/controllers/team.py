from flask import (
    g, Blueprint, render_template, request, session, url_for, current_app, redirect, flash
)
from scheduler.models import *
from scheduler import render_layout, db
from sqlalchemy.exc import IntegrityError

bp = Blueprint("team", __name__, url_prefix="/teams")
  
@bp.route('/', methods=['GET'])
def index():
    teams = Team.query.all()
    return render_layout(teams=teams)


@bp.route('/create', methods=['POST', 'GET'])
def create():
    if 'name' in request.form:
        team = Team(request.form['name'])
        try:
            db.session.add(team)
            db.session.commit()
        except IntegrityError as e:
            flash(f"Team name already exists!")
            return render_layout()
            
        return redirect(url_for('team.index'))

    return render_layout()


@bp.route('/<id>', methods=['GET'])
def view(id: int):
    locations = Location.query.all()
