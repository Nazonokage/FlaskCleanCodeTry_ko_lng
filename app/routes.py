# routes.py
from flask import Blueprint, render_template
from app import db
from app.models import Log
from app.utils import login_required

routes_bp = Blueprint('routes', __name__)

@routes_bp.route('/')
def index():
    return render_template('index.html')

@routes_bp.route('/dashboard')
@login_required
def dashboard():
    logs = Log.query.order_by(Log.timestamp.desc()).all()
    return render_template('dashboard.html', logs=logs)

@routes_bp.route('/edit-profile')
@login_required
def edit_profile():
    return render_template('edit_profile.html')