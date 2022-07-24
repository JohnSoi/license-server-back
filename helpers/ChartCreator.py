"""Хелперы для работы с графикой"""
from copy import copy
from random import randint

from app import engine


class ChartCreator:
    """Класс для работы с графиками"""
    __using_color = []

    def __init__(self, sql_template: str, label: str = 'График'):
        """
        Конструктор

        :param sql_template: Шаблон для запроса данных
        """
        if not sql_template:
            raise RuntimeError('не передан шаблон запроса')

        self.__sql_template = sql_template
        self.__label = label

    def process(self):
        result = {
            'labels': [],
            'datasets': [
                {
                    'label': self.__label,
                    'data': [],
                    'backgroundColor': []
                }
            ]
        }
        data = engine.engine.execute(self.__sql_template).fetchall()

        for item in data:
            result.get('labels').append(item[1])
            result.get('datasets')[0].get('data').append(item[0])
            result.get('datasets')[0].get('backgroundColor').append(self.__get_random_color())

        return result

    def __get_random_color(self) -> str:
        result = '#%06X' % randint(0, 0xFFFFFF)

        if result in self.__using_color:
            return self.__get_random_color()

        return result
