from classes.BaseClass import BaseClass
from models.License import License as LicenseModel


class License(BaseClass):
    @staticmethod
    def get_model(new_model: bool = False):
        return LicenseModel() if new_model else LicenseModel


