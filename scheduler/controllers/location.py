from flask import (
    g, Blueprint, render_template, request, session, url_for, redirect, flash
)
from scheduler.models import *
from scheduler import render_layout, db
from sqlalchemy.exc import IntegrityError

bp = Blueprint("location", __name__, url_prefix="/locations")

@bp.route('/')
def index():
    locations = Location.query.all()
    return render_layout(locations=locations)

@bp.route('/create', methods=['POST', 'GET'])
def create():
    if 'name' in request.form:
        location = Location(request.form['name'], [x.strip() for x in request.form['available_times'].split(',')])
        try:
            db.session.add(location)
            db.session.commit()
        except IntegrityError as e:
            flash(f"Location name already exists!")
            return render_layout()
        return redirect(url_for('location.index'))
    else:
        return render_layout(title="Create location")
