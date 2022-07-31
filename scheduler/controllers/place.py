from flask import (
    g, Blueprint, render_template, request, session, url_for, redirect
)
from scheduler.models import *
from scheduler import render_layout, db

bp = Blueprint("place", __name__, url_prefix="/places")

@bp.route('/')
def index():
    places = Place.query.all()
    return render_layout(places=places)

@bp.route('/create', methods=['POST', 'GET'])
def create():
    if 'name' in request.form:
        place = Place(request.form['name'])
        db.session.add(place)
        db.session.commit()
        return redirect(url_for('place.index'))
    else:
        return render_layout()
