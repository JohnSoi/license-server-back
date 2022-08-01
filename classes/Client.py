from sqlalchemy.orm import relationship

from classes.HttpQuery import HttpQueryHelpers
from classes.sql_templates.client import ACTIVITY_CLIENTS, NEW_CLIENTS, TYPE_LICENSE_CLIENT
from helpers.ChartCreator import ChartCreator
from models.Accrual import Accrual
from models.Client import Client as ClientModel
from classes.BaseClass import BaseClass
from models.License import License


class Client(BaseClass):
    def __init__(self):
        self._additional_methods = {
            'ChartData': self.get_chart_data,
            'NewClients': self.get_chart_data_new_clients,
            'LicensesClient': self.get_licenses_clients,
            'GetClientAccruals': self.get_accruals
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
    
    @classmethod
    def get_accruals(cls, **kwargs):
        filter_params = kwargs.get('filter') or {}
        client_id = filter_params.get('clientId')

        if not client_id:
            return HttpQueryHelpers.json_response(success=False, error_text='Не передан идентификатор клиента')

        query = cls.session.query(Accrual).where(Accrual.client_id == client_id).all() or []

        return HttpQueryHelpers.json_response(data=[item.to_dict() for item in query])

    @classmethod
    def api_products_and_licenses(cls, data):
        """
        Возвращает список продуктов и лицензий по ним в виде json по id продукта
        """
        client_uuid = data.get('clientUUID')

        if client_uuid:
            query = cls.session.query(cls.list(data={
                cls.get_model().where(cls.get_model().license_id == relationship(License)).first()}))

            return HttpQueryHelpers.json_response(data=query.to_dict(), success=True)
        else:
            return HttpQueryHelpers.json_response(error_text='Не передан id продукта', success=False)
