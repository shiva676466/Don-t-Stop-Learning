# app/models.py
from datetime import datetime
from app import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(60), nullable=False)
    roadmaps = db.relationship('Roadmap', backref='owner', lazy=True)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"

class Roadmap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    skill = db.Column(db.String(50), nullable=False)
    level = db.Column(db.String(20), nullable=False)      # beginner, intermediate, advanced
    goal = db.Column(db.Text, nullable=False)
    time_per_day = db.Column(db.String(20), nullable=False) # e.g. "1 hour", "2 hours"
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    tasks = db.relationship('Task', backref='roadmap', lazy=True, order_by="Task.order")

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=True)
    order = db.Column(db.Integer, nullable=False)
    is_completed = db.Column(db.Boolean, default=False)
    due_date = db.Column(db.String(30), nullable=True)    # "Week 1, Day 3"
    roadmap_id = db.Column(db.Integer, db.ForeignKey('roadmap.id'), nullable=False)