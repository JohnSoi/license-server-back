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
            if filter_params.get('summax'):
                query = query.where(cls.get_model().sum > filter_params.get('summax'))
            if filter_params.get('summin'):
                query = query.where(cls.get_model().sum < filter_params.get('summin'))
            if filter_params.get('dateStart'):
                query = query.where(cls.get_model().create_at > filter_params.get('dateStart'))
            if filter_params.get('dateEnd'):
                query = query.where(cls.get_model().create_at < filter_params.get('dateEnd'))

        return query
            if filter_params.get('searchString'):
                query = query.where(cls.get_model().name.like(f'%{filter_params.get("searchString")}%'))
            if filter_params.get('dateStart'):
                query = query.where(cls.get_model().create_at > filter_params.get('dateStart'))
            if filter_params.get('dateEnd'):
                query = query.where(cls.get_model().create_at < filter_params.get('dateEnd'))
            if filter_params.get('isActive') is not None:
                query = query.where(cls.get_model().is_active == filter_params.get('isActive'))
            return query

    @classmethod
    def api_create_accrual(cls, data):
        """
        API метод создания начислений
        """
        # data = kwargs.get('data') or {}
        client_uuid = data.get('clientUUID')
        sum = data.get('sum')
        license_uuid = data.get('licenseUUID')
        if not client_uuid:
            raise RuntimeError('Не передан UUID клиента')
        update = cls.create(data={'clientUUID': client_uuid, 'licenseUUID': license_uuid, 'sum': sum}, only_result=True)
        return cls.update(data=update)
