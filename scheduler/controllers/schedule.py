
from flask import (
    g, Blueprint, render_template, request, session, url_for, current_app, flash
)
from scheduler.models import *
from scheduler import render_layout

bp = Blueprint("schedule", __name__, url_prefix="/schedules")

@bp.route('/')
def index():
    return render_layout()

@bp.route('/', methods=['POST'])
def view():

    teams = list(map(lambda team: Team(team.strip()), request.form['teams'].split(',')))
    schedule = list(map(lambda date: date.strip(), request.form['dates'].split(',')))
    places = list(map(lambda loc: Place(loc.strip(), schedule), request.form['places'].split(',')))

    scheduler = Scheduler(teams, places)
    try:
        schedule = scheduler.schedule_games()
    except Exception as e:
        flash(e)
    
    return render_layout(page="view", schedule=schedule, title="View schedule")

@bp.route('/create')
def create():
    return render_layout()