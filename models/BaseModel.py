"""Базовая реализация модели"""
from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship, declarative_mixin, declared_attr

from app import BaseModel as Model, engine


@declarative_mixin
class BaseModel(Model):
    """Базовая модель"""
    __abstract__ = True
    session = engine.session

    id = Column(Integer, primary_key=True)

    create_at = Column(DateTime)
    update_at = Column(DateTime, nullable=True)
    delete_at = Column(DateTime, nullable=True)

    @declared_attr
    def create_user_id(self):
        return Column(Integer, ForeignKey('users.id'))

    @declared_attr
    def update_user_id(self):
        Column(Integer, ForeignKey('users.id'))

    @declared_attr
    def delete_user_id(self):
        return Column(Integer, ForeignKey('users.id'))

    @declared_attr
    def create_user(self):
        return relationship("User", lazy='joined')

    @declared_attr
    def update_user(self):
        return relationship("User", lazy='joined')

    @declared_attr
    def delete_user(self):
        return relationship("User", lazy='joined')

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
