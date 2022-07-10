"""Работы с HTTP"""
import json

from flask import make_response


class HttpQueryHelpers:
    """Класс для работы с ответами HTTP"""
    @staticmethod
    def json_response(*, data=None, error_text: str = '', success: bool = True,
                      field_error: str = '', meta=None, navigation=None) -> json:
        """
        Создание HTTP ответа

        :param data: Данные для ответа
        :param error_text: Текст ошибки
        :param success: Успех операции
        :param field_error: Поле, в котором произошла ошибка
        :param meta: Метаданные
        :param navigation: Навигация
        :return: JSON ответа
        """
        if meta is None:
            meta = {}
        if data is None:
            data = {}

        return make_response({
            'success': success,
            'field_error': field_error,
            'error': error_text,
            'data': data,
            'meta': meta,
            'navigation': navigation
        })

    @staticmethod
    def scalar_response(value):
        return value
