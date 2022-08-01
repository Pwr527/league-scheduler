from flask import (
    g, Blueprint, render_template, request, session, url_for, redirect, jsonify
)
from scheduler.models import *
from scheduler import render_layout, db

bp = Blueprint("api", __name__, url_prefix="/api/v1")

@bp.route('/locations')
def locations():
    return jsonify(Location.query.all())

@bp.route('/teams')
def teams():
    return jsonify(Team.query.all())

@bp.route('/games')
def games():
    return jsonify(Game.query.all())