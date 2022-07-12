from config.common import PRODUCTION
from models.User import User


class DevScript:
    def __init__(self):
        if PRODUCTION:
            raise RuntimeError('Данный скрипт не доступен в режиме Production')

    @staticmethod
    def add_default_data():
        User().add_default_data()
