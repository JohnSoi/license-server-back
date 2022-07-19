"""Базовая реализация CRUD"""
import json
from typing import List

from sqlalchemy import desc
from sqlalchemy.orm import Session

from classes.HttpQuery import HttpQueryHelpers
from classes.HistoryService import HistoryService

from constants.history_service import HISTORY_ACTIONS_TYPE

from models.BaseModel import BaseModel

from app import engine


class BaseClass:
    """Базовый класс"""
    USE_NAVIGATION: bool = True
    FIELD_ORDER: str = None
    AREA: str = 'BaseClass'

    session: Session = engine.session
    _additional_methods: dict = None

    def __init__(self):
        self.methods_map: dict = {
            'Create': self.create,
            'Get': self.get,
            'Delete': self.delete,
            'Update': self.update,
            'List': self.list
        }

        if self._additional_methods:
            self.methods_map.update(self._additional_methods)

    @staticmethod
    def get_model(new_model: bool = False):
        """
        Получение модели

        :param new_model: Признак создания новой модели
        :return: Модель сущности
        """
        return BaseModel() if new_model else BaseModel

    @classmethod
    def get(cls, **kwargs):
        """
        Получение записи по первичному ключу

        :return: Запись
        """
        key = kwargs.get('data')
        query = cls.session.query(cls.get_model()).get(key)
        if query:
            return HttpQueryHelpers.json_response(data=query.to_dict())
        else:
            return HttpQueryHelpers.json_response(success=False, error_text='Не найдена запись по ключу')

    @classmethod
    def list(cls, **kwargs):
        """
        Метод получения списка по навигации и сортировке

        :return: Список с записями сущности
        """
        navigation = kwargs.get('navigation')
        filter_params = kwargs.get('filter')
        result = cls._prepare_list_result(navigation, filter_params)

        result = cls._prepare_result(result, filter_params)

        return HttpQueryHelpers.json_response(data=result, navigation=navigation if cls.USE_NAVIGATION else {})

    @classmethod
    def create(cls, **kwargs):
        """
        Создание новой записи (не создает запись в БД, а только возвращает формат)

        :return: Запись в формате модели
        """
        model = cls.get_model(True)
        record = kwargs.get('data')

        if isinstance(record, str):
            record = json.loads(record)


        if not record:
            data = model.to_dict()
        else:
            data = model.from_object(record).to_dict()

        return HttpQueryHelpers.json_response(data=data) if not kwargs.get('only_result') else data

    @classmethod
    def update(cls, **kwargs):
        """
        Обновление или создание записи в БД

        :return: Запись из БД
        """
        record = kwargs.get('data')
        if not record:
            return HttpQueryHelpers.json_response(error_text='Нет данных для обновления', success=False)

        if isinstance(record, str):
            record = json.loads(record)

        if not record.get('id'):
            return cls._new(record)
        else:
            return cls._update(record)

    @classmethod
    def delete(cls, **kwargs):
        """
        Удаление записи в БД

        :return: Результат удаления
        """
        key = kwargs.get('data')
        query = cls.session.query(cls.get_model()).get(key)
        if query:
            cls.session.delete(query)
            cls.session.commit()
            return HttpQueryHelpers.json_response(success=True)
        else:
            return HttpQueryHelpers.json_response(success=False, error_text='Не найдена запись по ключу')

    @classmethod
    def _prepare_query_filter(cls, query, filter_params):
        """
        Подготовка фильтров основного запроса списка

        :param query: Запрос в БД
        :param filter_params: Параметры фильтрации
        :return: Запрос в БД с применнеными фильтрами
        """
        return query

    @classmethod
    def _prepare_list_result(cls, navigation: dict = None, filter_params: dict = None):
        """
        Подготовка основного запроса в БД для получения списка

        :param navigation: Навигация
        :param filter_params: Параметры фильтрации
        :return: Данные из БД
        """
        result = []
        if not navigation:
            navigation = {
                'page': 0,
                'pageSize': 100,
                'hasMore': False
            }

        query = cls._prepare_query_filter(cls.session.query(cls.get_model()), filter_params)

        if cls.USE_NAVIGATION:
            query = query.limit(navigation.get('pageSize')) \
                .offset(navigation.get('page') * navigation.get('pageSize'))

        if cls.FIELD_ORDER:
            query.order_by(desc(cls.FIELD_ORDER))

        if query and query.count():
            result = [item.to_dict() for item in query]
            if cls.USE_NAVIGATION:
                navigation['hasMore'] = query.count() > navigation.get('pageSize') or 0
                navigation['page'] = navigation.get('page') + 1

        return result

    @classmethod
    def _new(cls, record: dict):
        """
        Создание новой записи в БД

        :param record: Данные записи
        :return: Запись из БД
        """
        model = cls.get_model(True)
        model.from_object(record)
        cls.session.add_all([model])
        cls.session.commit()
        HistoryService.add(HISTORY_ACTIONS_TYPE['CREATE'], 'Создание новой карточки',
                           cls.AREA, model.id)
        return HttpQueryHelpers.json_response(data=model.to_dict())

    @classmethod
    def _update(cls, record: dict):
        """
        Обновление записи в БД

        :param record: Запись
        :return: Данные из БД
        """
        from app import engine
        model = engine.session.query(cls.get_model()).get(record.get('id'))
        if model:
            old_record = model.to_dict()
            model.from_object(record)
            engine.session.add_all([model])
            engine.session.commit()
            HistoryService.add(HISTORY_ACTIONS_TYPE['EDIT'], 'Изменение карточки №{}'.format(record.get('id')),
                               cls.AREA, model.id)
            return HttpQueryHelpers.json_response(data=model.to_dict())
        else:
            return HttpQueryHelpers.json_response(success=False,
                                                  error_text='Не найдена запись для обновления по id {}'
                                                  .format(record.get('id')))

    @classmethod
    def _prepare_result(cls, result: List[dict], filter_params: dict) -> List[dict]:
        """
        Пост обработка результатов

        :param result: Итоговый список данных
        :param filter_params: Параметры фильтрации
        :return: Постобработанный список
        """
        return result
