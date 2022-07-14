from models.Client import Client as ClientModel
from classes.BaseClass import BaseClass


class Client(BaseClass):
    @staticmethod
    def get_model(new_model: bool = False):
        return ClientModel() if new_model else ClientModel

    
