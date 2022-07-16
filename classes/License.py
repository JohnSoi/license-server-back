from classes.BaseClass import BaseClass
from models.License import License as LicenseModel


class License(BaseClass):
    @staticmethod
    def get_model(new_model: bool = False):
        return LicenseModel() if new_model else LicenseModel

    @classmethod
    def _prepare_query_filter(cls, query, filter_params):
        if filter_params:
            if filter_params.get('searchString'):
                query = query.where(cls.get_model().name.like(f'%{filter_params.get("searchString")}%'))
            if filter_params.get('dateStart'):
                query = query.where(cls.get_model().create_at > filter_params.get('dateStart'))
            if filter_params.get('dateEnd'):
                query = query.where(cls.get_model().create_at < filter_params.get('dateEnd'))
            if filter_params.get('onlyGroups'):
                query = query.where(cls.get_model().group_uuid == None)

        return query


