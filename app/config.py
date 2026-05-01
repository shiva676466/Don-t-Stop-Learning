# app/config.py
import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'a-very-secret-key-change-me')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///instance/site.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False