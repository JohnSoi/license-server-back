from app import engine
from classes.HttpQuery import HttpQueryHelpers
from classes.sql_templates.client import ACTIVITY_CLIENTS
from models.Client import Client as ClientModel
from classes.BaseClass import BaseClass


class Client(BaseClass):
    def __init__(self):
        self._additional_methods = {
            'ChartData': self.get_chart_data
        }
        super().__init__()

    @staticmethod
    def get_model(new_model: bool = False):
        return ClientModel() if new_model else ClientModel

    @classmethod
    def _prepare_query_filter(cls, query, filter_params):
        if filter_params:
            if filter_params.get('searchString'):
                query = query.where(cls.get_model().name.like(f'%{filter_params.get("searchString")}%'))
            if filter_params.get('dateStart'):
                query = query.where(cls.get_model().create_at > filter_params.get('dateStart'))
            if filter_params.get('dateEnd'):
                query = query.where(cls.get_model().create_at < filter_params.get('dateEnd'))
            if filter_params.get('isActive') is not None:
                query = query.where(cls.get_model().is_active == filter_params.get('isActive'))

        return query

    @classmethod
    def get_chart_data(cls, **kwargs):
        filters = kwargs.get('filter')

        data = engine.engine.execute(ACTIVITY_CLIENTS).fetchall()

        result = {
            'labels': [],
            'datasets': [
                {
                    'label': 'Активность клиентов',
                    'data': []
                }
            ]
        }

        for item in data:
            result.get('labels').append(item[1])
            result.get('datasets')[0].get('data').append(item[0])

        return HttpQueryHelpers.json_response(data=result)

