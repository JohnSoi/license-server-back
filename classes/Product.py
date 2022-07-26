from sqlalchemy.orm import relationship

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
    def api_products_and_licenses(cls, query, **kwargs):
        """
        Возвращает список продуктов и лицензий по ним в виде json по uuid продукта
        """
        data = kwargs.get('data') or {}
        product_uuid = data.get('productuuID')

        if product_uuid:
            query = query.where(cls.get_model().license_id == relationship('licenses.id')).first()
            product_list = cls.list(data={'query': query})
        else:
            raise RuntimeError('Не передан id продукта')

        return HttpQueryHelpers.json_response(data=product_list.to_dict(), success=True)
