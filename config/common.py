"""Настройки приложения"""
from constants.database import LOGIN, PASSWORD, NAME

PRODUCTION = False

SECRET_KEY = 'gq1KJC]=YdL,D]&hNK|c[|ho&O:Msz#T^rlDBc6sk$ayUAf#a|LH$boOD[%Usnr'

SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_DATABASE_URI = f'postgresql+psycopg2://{LOGIN}:{PASSWORD}@localhost/{NAME}'
SQLALCHEMY_ECHO = True

MAX_CONTENT_LENGTH = 16 * 1024 * 1024
UPLOAD_FOLDER = 'uploads'
