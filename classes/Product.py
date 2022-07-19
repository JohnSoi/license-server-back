from classes.HttpQuery import HttpQueryHelpers

from models.Product import Product as ProductModel
from classes.BaseClass import BaseClass


class Product(BaseClass):
    @staticmethod
    def get_model(new_model: bool = False):
        return ProductModel() if new_model else ProductModel

    @classmethod
    def api_products_and_licenses(self, **kwargs):
        data = kwargs.get('data') or {}
        product = data.get('name')

        if not product:
            raise RuntimeError('Не передано название продукта')
        productList = self.list(filter={'product': product})
        return HttpQueryHelpers.json_response(productList, success=True)

