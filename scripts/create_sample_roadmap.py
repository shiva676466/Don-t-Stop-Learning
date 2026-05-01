"""Utility script to create a sample user, roadmap and tasks for manual testing.

Run from the project root with the virtualenv activated:

python scripts/create_sample_roadmap.py

It will create a test user (if not exists), create a roadmap and tasks using the
learning generator, commit them to the DB, and print the Mermaid text and the
URL path you can visit (assuming the server runs on port 5002).
"""

from app import create_app, db
from app.models import User, Roadmap, Task
from app.learning.generator import generate_roadmap
import os

app = create_app()

TEST_USERNAME = os.environ.get('DSL_TEST_USER', 'tester')
TEST_EMAIL = os.environ.get('DSL_TEST_EMAIL', 'tester@example.com')
TEST_PASSWORD = os.environ.get('DSL_TEST_PW', 'password')

with app.app_context():
    # Ensure DB tables exist
    db.create_all()

    user = User.query.filter_by(username=TEST_USERNAME).first()
    if not user:
        user = User(username=TEST_USERNAME, email=TEST_EMAIL, password_hash=TEST_PASSWORD)
        db.session.add(user)
        db.session.commit()
        print('Created test user:', TEST_USERNAME)
    else:
        print('Test user exists:', TEST_USERNAME)

    # Create roadmap
    roadmap = Roadmap(skill='DSA', level='beginner', goal='Get comfortable with DS&A', time_per_day='1 hour', user_id=user.id)
    db.session.add(roadmap)
    db.session.flush()

    data = generate_roadmap('DSA', 'beginner', '1 hour', 'Get comfortable with DS&A')
    tasks = data['tasks']
    for t in tasks:
        task = Task(title=t['title'], description=t['description'], order=t['order'], due_date=t['due_date'], roadmap_id=roadmap.id)
        db.session.add(task)

    db.session.commit()

    print('\nRoadmap created:')
    print(' - id:', roadmap.id)
    print(' - visit (after running server): http://127.0.0.1:5002/roadmap/{}'.format(roadmap.id))
    print('\nMermaid text:\n')
    print(data['mermaid'])
