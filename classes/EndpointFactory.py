from classes.User import User
from classes.License import License
from classes.TypePaid import TypePaid
from classes.Client import Client
from classes.Accrual import Accrual


class EndpointFactory:
    _ENDPOINT_MAP = {
        'User': User,
        'License': License,
        'Client': Client,
        'TypePaid': TypePaid,
        'Accrual': Accrual
    }

    def __init__(self, params: dict):
        self._check_params(params)

    def _check_params(self, params: dict):
        if not params:
            params = {}

        if not params.get('endpointName'):
            raise RuntimeError('Не передан класс для работы')

        self._endoint: str = params.get('endpointName')

        if self._endoint not in self._ENDPOINT_MAP:
            raise RuntimeError('Данная конечная точка не найдена')

        self._class = self._ENDPOINT_MAP[self._endoint]()

        if not params.get('method'):
            raise RuntimeError('Не передан метод')

        if params.get('method') not in self._class.methods_map:
            raise RuntimeError('Метод не найден в списке доступных')

        self._method = self._class.methods_map[params.get('method')]
        self._data = params.get('data')

    def process(self):
        return self._method(self._data)
