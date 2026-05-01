# app/config.py
import os

basedir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'a-very-secret-key-change-me')
    # Use an absolute path to the sqlite DB so SQLAlchemy can always open it
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or (
        'sqlite:///' + os.path.join(basedir, 'instance', 'site.db')
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False