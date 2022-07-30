from models.Product import Product as ProductModel
from models.License import License

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
    def api_products_and_licenses(cls, data):
        """
        Возвращает список продуктов и лицензий по ним в виде json по id продукта
        """
        product_id = data.get('id')

        if product_id:
            query = cls.session.query(cls.list(data={cls.get_model().where(cls.get_model().license_id == data.get(License.license_id)).first()}))

            return HttpQueryHelpers.json_response(data=query.to_dict(), success=True)
        else:
            return HttpQueryHelpers.json_response(error_text='Не передан id продукта', success=False)
