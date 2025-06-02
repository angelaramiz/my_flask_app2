# config.py
import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'tu_clave_secreta_aqui'
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:22122000@localhost/mi_flask_app2'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
