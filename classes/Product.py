from models.Product import Product as ProductModel

from classes.BaseClass import BaseClass
from classes.HttpQuery import HttpQueryHelpers


class Product(BaseClass):
    @staticmethod
    def get_model(new_model: bool = False):
        return ProductModel() if new_model else ProductModel

    @classmethod
    def _prepare_query_filter(cls, query, filter_params):
        if filter_params:
            if filter_params.get('searchString'):
                query = query.where(cls.get_model().name.like(f'%{filter_params.get("searchString")}%'))
            if filter_params.get('dateStart'):
                query = query.where(cls.get_model().create_at > filter_params.get('dateStart'))
            if filter_params.get('dateEnd'):
                query = query.where(cls.get_model().create_at < filter_params.get('dateEnd'))

        return query

    @classmethod
    def api_products_and_licenses(cls, **kwargs):
        """
        Возвращает список продуктов и лицензий по ним в виде json по group_uuid
        """
        data = kwargs.get('data') or {}
        group_uuid = data.get('group_uuid')

        if not group_uuid:
            raise RuntimeError('Не передан id группы лицензий')
        product_list = cls.list(filter={'group_uuid': group_uuid})
        return HttpQueryHelpers.json_response(product_list, success=True)
