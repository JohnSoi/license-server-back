
from models.Client import Client as ClientModel
from classes.BaseClass import BaseClass


class Client(BaseClass):
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

