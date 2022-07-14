from models.Accrual import Accrual as AccrualModel
from classes.BaseClass import BaseClass


class Accrual(BaseClass):
    @staticmethod
    def get_model(new_model: bool = False):
        return AccrualModel() if new_model else AccrualModel
