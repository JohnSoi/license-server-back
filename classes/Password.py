"""Работа с паролями"""
import hashlib
import uuid


class Password:
    """Класс для работы с паролями"""
    def __init__(self):
        self.salt = uuid.uuid4().hex

    def get_hash(self, password: str) -> str:
        """
        Создание хеша пароля

        :param password: Строка с паролем
        :return: Хеш пароль
        """
        return hashlib.sha256(self.salt.encode() + password.encode()).hexdigest() + ':' + self.salt

    @staticmethod
    def check_hash(hashed_password: str, user_password: str) -> bool:
        """
        Проверка пераданной строки с паролем

        :param hashed_password: Хеш пароля
        :param user_password: Строка пароля
        :return: Признак совпадения хеша и переданной строки
        """
        password, salt = hashed_password.split(':')
        return password == hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()
