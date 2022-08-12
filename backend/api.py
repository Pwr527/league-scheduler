from flask import (
    g, Blueprint, render_template, request, abort
)
from backend.models import *
from backend import db
from sqlalchemy.exc import IntegrityError

bp = Blueprint("api", __name__, url_prefix="/api/v1")

def getApiResponse(data=None, status=None, error=None):
    return (
        ApiResponse(data=data, status=status, error=error).serialize(), 
        status if status else (400 if error else 200)
    )

@bp.route('/locations')
def locations():
    return getApiResponse(data=Location.query.all())

@bp.route('/teams')
def teams():
    return getApiResponse(data=Team.query.all())

@bp.route('/teams/<int:id>')
def team_detail(id:int):
    team = Team.query.get(id)
    if team:
        return getApiResponse(data=team)
    else:
        abort(404)


@bp.route('/locations/<int:id>')
def location_detail(id:int):
    location = Location.query.get(id)
    if location:
        return getApiResponse(data=location)
    else:
        abort(404)


@bp.route('/games')
def games():
    return getApiResponse(data=Game.query.all())

@bp.route('/teams', methods=['POST'])
def create_team():
    if 'name' in request.json:
        team = Team(request.json['name'])
        try:
            db.session.add(team)
            db.session.commit()
        except IntegrityError as e:
            return getApiResponse(error="duplicate", status=409)

        return getApiResponse(data=team)
    
    return getApiResponse(error="missing data", status=400)

@bp.route('/locations', methods=['POST'])
def create_location():
    print("got requestion", request.json)
    if 'name' in request.json:
        location = Location(request.json['name'], [x.strip() for x in request.json['available_times'].split(',')])
        try:
            db.session.add(location)
            db.session.commit()
        except IntegrityError as e:
            return getApiResponse(error=e)

        return getApiResponse(data=location)
   
    return getApiResponse(error="missing data", status=400)


@bp.route('/schedule', methods=['POST'])
def generate_schedule():

    requested_teams = request.json.getlist('team')
    requested_locations = request.json.getlist('location')
    locations = Location.query.filter(Location.id.in_(requested_locations))

    schedule=None

    scheduler = Scheduler(requested_teams, locations)
    try:
        schedule = scheduler.schedule_games()
    except Exception as e:
        return getApiResponse(error=e)
    
    if schedule:
        for game in schedule:
            game.team1 = Team.query.get(game.team1)
            game.team2 = Team.query.get(game.team2)

    return getApiResponse(data=schedule)
