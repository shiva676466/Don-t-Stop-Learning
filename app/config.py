import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///instance/app.sqlite'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
