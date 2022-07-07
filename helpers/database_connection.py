"""Организация рабоьы с БД"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config.common import SQLALCHEMY_DATABASE_URI


class EngineConnect:
    """Класс для подключения к БД"""
    engine = None
    session = None

    def __init__(self):
        self.engine = create_engine(SQLALCHEMY_DATABASE_URI)
        self.engine.connect()
        self.session = sessionmaker(bind=self.engine)()
