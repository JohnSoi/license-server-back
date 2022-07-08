"""Базовая реализация модели"""
from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from app import BaseModel as Model, engine


class BaseModel(Model):
    """Базовая модель"""
    session = engine.session()

    id = Column(Integer, primary_key=True)

    create_at = Column(DateTime)
    update_at = Column(DateTime, nullable=True)
    delete_at = Column(DateTime, nullable=True)

    create_user_id = Column(Integer, ForeignKey('users.id'))
    update_user_id = Column(Integer, ForeignKey('users.id'))
    delete_user_id = Column(Integer, ForeignKey('users.id'))

    create_user = relationship("User", lazy='joined')
    update_user = relationship("User", lazy='joined')
    delete_user = relationship("User", lazy='joined')

    def from_dict(self, record: dict) -> None:
        """
        Создание записи модели из объекта

        :param record:
        :return:
        """
        return

    def to_dict(self) -> dict:
        """
        Преобразование модели в словарь

        :return: Данные модели в виде словаря
        """
        return {}

    def add_default_data(self):
        """
        Добавлени начальных данных
        """
        pass
