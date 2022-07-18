from models.Accrual import Accrual as AccrualModel
from classes.BaseClass import BaseClass


class Accrual(BaseClass):
    def __init__(self):
        self._additional_methods = {
            'GetAccrualsByClientId': self.get_accrual_by_client_id
        }

        super().__init__()

    @staticmethod
    def get_model(new_model: bool = False):
        return AccrualModel() if new_model else AccrualModel

    def get_accrual_by_client_id(self, **kwargs):
        """
        Возвращает начисление по UUID клиента
        """
        data = kwargs.get('data') or {}
        client_uuid = data.get('clientUUID')

        if not client_uuid:
            raise RuntimeError('Не передан UUID клиента')

        return self.list(filter={'clientUUID': client_uuid})

    @classmethod
    def _prepare_query_filter(cls, query, filter_params):
        if filter_params:
            if filter_params.get('clientUUID'):
                query = query.where(cls.get_model().client_uuid == filter_params.get('clientUUID'))

        return query

    @classmethod
    def create_accrual(self, **kwargs):
        data = kwargs.get('data') or {}
        client_uuid = data.get('clientUUID')
        sum = data.get('sum')
        if not client_uuid:
            raise RuntimeError('Не передан UUID клиента')
        return self.update({'sum': sum})
