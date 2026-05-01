# app/main/routes.py
from flask import Blueprint, render_template
from flask_login import login_required, current_user

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('main/index.html')

@main.route('/dashboard')
@login_required
def dashboard():
    roadmaps = current_user.roadmaps
    return render_template('main/dashboard.html', roadmaps=roadmaps)