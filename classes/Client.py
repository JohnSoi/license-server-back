from classes.HttpQuery import HttpQueryHelpers
from classes.sql_templates.client import ACTIVITY_CLIENTS, NEW_CLIENTS
from helpers.ChartCreator import ChartCreator
from models.Client import Client as ClientModel
from models.License import License as LicenseModel
from models.Product import Product as ProductModel
from models.Accrual import Accrual as AccrualModel
from classes.BaseClass import BaseClass


class Client(BaseClass):
    def __init__(self):
        self._additional_methods = {
            'ChartData': self.get_chart_data,
            'NewClients': self.get_chart_data_new_clients,
            'getClientAccruals': self.get_client_accruals_by_UUID,
            'getClientLicenses': self.get_client_licenses_by_UUID,
            'getClientProducts': self.get_client_product_by_UUID,
            'getUUIDClient': self.get_client_uuid
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

    """
    Метод для получения UUID клиента
    """

    @classmethod
    def get_client_uuid(cls, **kwargs):
        if not kwargs.get('getUUIDClient'):
            raise KeyError('Не передан параметр "getUUIDClient"')
        client_uuid = cls.session.query(cls.get_model().uuid).where(
            cls.get_model().uuid == kwargs.get('getUUIDClient')).first()
        if not client_uuid:
            return HttpQueryHelpers.json_response(data=[])
        else:
            return client_uuid

    """
    Метод получения ID клиента
    """

    @classmethod
    def get_id_client_by_UUID(cls):
        client_uuid = cls.get_client_uuid()
        client_id = cls.session.query(cls.get_model().id).where(
            cls.get_model().uuid == client_uuid).first()
        return client_id

    """
    API метод для получения начислений по uuid клинета
    """

    @classmethod
    def get_client_accruals_by_UUID(cls, **kwargs):
        client_id = cls.get_id_client_by_UUID()
        if kwargs.get('getClientAccruals'):
            accruals_client = cls.session.query(cls.get_model(), AccrualModel()).join(AccrualModel()).filter(
                AccrualModel().client_id == client_id).all()
            return HttpQueryHelpers.json_response(data=accruals_client.to_dict())
        else:
            return HttpQueryHelpers.json_response(data=[])

    """
    API метод для получения лицензий по uuid клинета
    """

    @classmethod
    def get_client_licenses_by_UUID(cls, **kwargs):
        client_id = cls.get_id_client_by_UUID()
        if kwargs.get('getClientLicenses'):
            license_info = cls.session.query(LicenseModel()).where(
                cls.get_model().id == client_id and
                cls.get_model().license_id == LicenseModel().id).all()
            return HttpQueryHelpers.json_response(data=license_info.to_dict())
        else:
            return HttpQueryHelpers.json_response(data=[])

    """
    API метод для получения продуктов по uuid клинета
    """

    @classmethod
    def get_client_product_by_UUID(cls, **kwargs):
        client_id = cls.get_id_client_by_UUID()
        if kwargs.get('getClientProducts'):
            license_id = cls.session.query(LicenseModel().id).where(
                cls.get_model().id == client_id and
                cls.get_model().license_id == LicenseModel().id).first()
            products_client = cls.session.query(ProductModel()).where(
                ProductModel().license_id == license_id).all()
            return HttpQueryHelpers.json_response(data=products_client.to_dict())
        else:
            return HttpQueryHelpers.json_response(data=[])

    @classmethod
    def get_chart_data_new_clients(cls, **kwargs):
        filters = kwargs.get('filter')
        return HttpQueryHelpers.json_response(data=ChartCreator(NEW_CLIENTS, 'Новые клиенты').process())

