"""Базовая реализация модели"""
from datetime import datetime
from typing import List

from sqlalchemy import Column, Integer, DateTime
from sqlalchemy.orm import declarative_mixin

from app import BaseModel as Model, engine


@declarative_mixin
class BaseModel(Model):
    """Базовая модель"""
    __abstract__ = True
    session = engine.session

    _gurded: List[str] = []
    _fillable: List[str] = []
    _manual_fillable: List[str] = []

    id = Column(Integer, primary_key=True)

    create_at = Column(DateTime)
    update_at = Column(DateTime, nullable=True)
    delete_at = Column(DateTime, nullable=True)

    def from_object(self, record: dict) -> int:
        """
        Создание записи модели из объекта

        :param record: Заполненая запись с начальными данными
        :return: Модель
        """
        fields = self._get_fillable_fields()
        
        for field in fields:
            if field in record:
                setattr(self, field, record.get(field))

        if not self.create_at:
            self.create_at = datetime.now()

        self.update_at = datetime.now()

        self._manual_fillable_fields(record)

        return self

    def to_dict(self) -> dict:
        """
        Преобразование модели в словарь

        :return: Данные модели в виде словаря
        """
        result = {}
        columns = self._get_columns()

        for column_name in columns:
            result[column_name] = getattr(self, column_name)

        self._manual_response_fields(result)
        
        return result

    def add_default_data(self):
        """
        Добавлени начальных данных
        """
        pass

    def _manual_fillable_fields(self, record: dict) -> None:
        pass

    def _manual_response_fields(self, result: dict) -> None:
        pass

    def _get_columns(self) -> List[str]:
        """
        Получение не защищенных колонок модели

        :return: Список доступных колонок
        """
        return self._get_columns_name(self._gurded)
    
    def _get_fillable_fields(self):
        """
        Получение списка заполняемых полей
        
        :return: Список заполняемых полей
        """
        return self._get_columns_name(self._manual_fillable)

    def _get_columns_name(self, skip_fields: List[str]) -> List[str]:
        """
        Получение спика полей за исключением переданного списка
        
        :param skip_fields: Список полей, которые пропускаются
        :return: Список доступных полей
        """
        result = []

        columns = self.metadata.tables.get(self.__tablename__).columns

        if columns:
            result = [column_name for column_name in columns.keys() if column_name not in skip_fields]

        return result