from flask import render_template, redirect, url_for, flash
from . import learning
from .generator import generate_roadmap


@learning.route('/onboarding')
def onboarding():
    return render_template('learning/onboarding.html')


@learning.route('/roadmap/<int:roadmap_id>')
def roadmap(roadmap_id):
    # placeholder: fetch roadmap by id
    roadmap = {'id': roadmap_id, 'title': f'Roadmap {roadmap_id}', 'tasks': []}
    return render_template('learning/roadmap.html', roadmap=roadmap)


@learning.route('/task/<int:task_id>/complete', methods=['POST'])
def complete_task(task_id):
    flash(f'Task {task_id} marked complete (placeholder).')
    return redirect(url_for('main.dashboard'))
