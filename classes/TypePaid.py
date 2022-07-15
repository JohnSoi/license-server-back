from classes.BaseClass import BaseClass
from models.TypePaid import TypePaid as TypePaidModel


class TypePaid(BaseClass):
    @staticmethod
    def get_model(new_model: bool = False):
        return TypePaidModel() if new_model else TypePaidModel
