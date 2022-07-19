from models.Client import Client as ClientModel
from classes.BaseClass import BaseClass


class Client(BaseClass):
    @staticmethod
    def get_model(new_model: bool = False):
        return ClientModel() if new_model else ClientModel

    @classmethod
    def _prepare_query_filter(cls, query, filter_params):
        if filter_params:
            if filter_params.get('dateStart'):
                query = query.where(cls.get_model().create_at > filter_params.get('dateStart'))
            if filter_params.get('dateEnd'):
                query = query.where(cls.get_model().create_at < filter_params.get('dateEnd'))
            if filter_params.get('isActive') == False:
                query = query.where(cls.get_model().is_active == 0)
            if filter_params.get('isActive' == True):
                query = query.where(cls.get_model().is_active == 1)
            if filter_params.get('isPaid') == False:
                query = query.where(cls.get_model().license_uuid != None)
            if filter_params.get('isPaid') == True:
                query = query.where(cls.get_model().license_uuid == 0)
        return query