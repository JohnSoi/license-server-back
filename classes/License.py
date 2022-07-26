from typing import List

from classes.BaseClass import BaseClass
from helpers.list_helpers import get_hierarchy_list
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
                query = query.where(cls.get_model().group_id == None)

        return query

    @classmethod
    def _prepare_result(cls, result: List[dict], filter_params):
        return get_hierarchy_list(result, 'license_id') if not filter_params.get('withoutHierarchy') and result else result
