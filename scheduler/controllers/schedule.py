
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

    requested_teams = request.form.getlist('team')
    requested_locations = request.form.getlist('location')
    locations = Location.query.filter(Location.id.in_(requested_locations))

    schedule=None

    scheduler = Scheduler(requested_teams, locations)
    try:
        schedule = scheduler.schedule_games()
    except Exception as e:
        flash(e)
    
    for game in schedule:
        game.team1 = Team.query.get(game.team1)
        game.team2 = Team.query.get(game.team2)

    return render_layout(page="view", schedule=schedule, title="View schedule")

@bp.route('/create')
def create():
    teams = Team.query.all()
    locations = Location.query.all()
    return render_layout(teams=teams, locations=locations, title="Create schedule")