from classes.HttpQuery import HttpQueryHelpers
from classes.sql_templates.client import ACTIVITY_CLIENTS, NEW_CLIENTS, TYPE_LICENSE_CLIENT
from helpers.ChartCreator import ChartCreator
from models.Client import Client as ClientModel
from classes.BaseClass import BaseClass


class Client(BaseClass):
    def __init__(self):
        self._additional_methods = {
            'ChartData': self.get_chart_data,
            'NewClients': self.get_chart_data_new_clients,
            'LicensesClient': self.get_licenses_clients
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

        return HttpQueryHelpers.json_response(data=ChartCreator(ACTIVITY_CLIENTS, 'Активность клиентов').process())

    @classmethod
    def get_chart_data_new_clients(cls, **kwargs):
        filters = kwargs.get('filter')

        return HttpQueryHelpers.json_response(data=ChartCreator(NEW_CLIENTS, 'Новые клиенты').process())

    @classmethod
    def get_licenses_clients(cls, **kwargs):
        filters = kwargs.get('filter')

        return HttpQueryHelpers.json_response(data=ChartCreator(TYPE_LICENSE_CLIENT, 'Типы лицензий').process())
