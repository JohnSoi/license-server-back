"""Работа с историей действий в системе"""
from app import engine
from flask import request

from constants.history_service import HISTORY_ACTIONS_TYPE
from models import HistoryService as HistoryServiceModel
from models.User import User


class HistoryService:
    """Класс для работы с историей"""
    @staticmethod
    def get_model(new_model: bool = False):
        return HistoryServiceModel() if new_model else HistoryServiceModel

    @staticmethod
    def add(type_history_action: str, text: str, area: str, object_id: int):
        """
        Добавлени записи в историю действий

        :param type_history_action: Тип действия истории
        :param text: Текс истори
        :param area: Область истории
        :param object_id: ИД Объекта истории
        """
        if type_history_action not in HISTORY_ACTIONS_TYPE.values():
            raise KeyError('Данный тип опреации не поддерживается сервисом истории')

        model = HistoryService.get_model(True)
        user_uuid = request.headers.get('User-Auth-UUID')
        model.from_object({
            'type': type_history_action,
            'text': text,
            'object_id': object_id,
            'area': area,
            'user_id': engine.session.query(User).where(User.uuid == user_uuid).first().id
        })
        engine.session.add_all([model])
        engine.session.commit()
