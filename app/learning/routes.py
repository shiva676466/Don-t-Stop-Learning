# app/learning/routes.py
from flask import Blueprint, render_template, redirect, url_for, flash, request, jsonify
from flask_login import login_required, current_user
from app import db
from app.models import Roadmap, Task
from app.learning.generator import generate_roadmap_tasks

learning = Blueprint('learning', __name__)

@learning.route('/onboarding', methods=['GET', 'POST'])
@login_required
def onboarding():
    if request.method == 'POST':
        skill = request.form.get('skill')
        level = request.form.get('level')
        goal = request.form.get('goal')
        time_per_day = request.form.get('time_per_day')

        if not all([skill, level, goal, time_per_day]):
            flash('Please fill in all fields.', 'danger')
            return render_template('learning/onboarding.html')

        # Create roadmap
        roadmap = Roadmap(
            skill=skill, level=level, goal=goal,
            time_per_day=time_per_day, user_id=current_user.id
        )
        db.session.add(roadmap)
        db.session.flush()  # to get roadmap.id

        # Generate tasks
        tasks_data = generate_roadmap_tasks(skill, level, time_per_day)
        for t in tasks_data:
            task = Task(
                title=t['title'],
                description=t['description'],
                order=t['order'],
                due_date=t['due_date'],
                roadmap_id=roadmap.id
            )
            db.session.add(task)

        db.session.commit()
        flash('Your personalized learning path is ready!', 'success')
        return redirect(url_for('learning.view_roadmap', roadmap_id=roadmap.id))

    return render_template('learning/onboarding.html')

@learning.route('/roadmap/<int:roadmap_id>')
@login_required
def view_roadmap(roadmap_id):
    roadmap = Roadmap.query.get_or_404(roadmap_id)
    if roadmap.user_id != current_user.id:
        flash('Access denied.', 'danger')
        return redirect(url_for('main.dashboard'))
    tasks = Task.query.filter_by(roadmap_id=roadmap.id).order_by(Task.order).all()
    return render_template('learning/roadmap.html', roadmap=roadmap, tasks=tasks)

@learning.route('/task/<int:task_id>/toggle', methods=['POST'])
@login_required
def toggle_task(task_id):
    task = Task.query.get_or_404(task_id)
    roadmap = Roadmap.query.get(task.roadmap_id)
    if roadmap.user_id != current_user.id:
        return jsonify({'success': False, 'error': 'Unauthorized'}), 403

    task.is_completed = not task.is_completed
    db.session.commit()
    return jsonify({'success': True, 'is_completed': task.is_completed})