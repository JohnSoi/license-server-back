from models.Product import Product as ProductModel
from classes.BaseClass import BaseClass


class Product(BaseClass):
    @staticmethod
    def get_model(new_model: bool = False):
        return ProductModel() if new_model else ProductModel