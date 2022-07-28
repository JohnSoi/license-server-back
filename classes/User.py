from classes.HttpQuery import HttpQueryHelpers
from classes.BaseClass import BaseClass
from classes.Password import Password
from models.User import User as UserModel
from app import engine


class User(BaseClass):
    def __init__(self):
        self._additional_methods = {
            'LoginCheck': self.check_login,
            'Login': self.login,
            'ChangePassword': self.reset_password
        }

        super().__init__()

    @staticmethod
    def get_model(new_model: bool = False):
        return UserModel() if new_model else UserModel

    def login(self, **kwargs):
        data = kwargs.get('data')
        login = data.get('login')
        password = data.get('password')

        employee = self.session.query(UserModel).filter(UserModel.login == login)
        if employee.count():
            employee = employee.first()

            if Password.check_hash(employee.password, password):
                return HttpQueryHelpers.json_response(data=employee.to_dict())
            else:
                return HttpQueryHelpers.json_response(error_text='Неверный пароль', success=False,
                                                      field_error='password')
        else:
            return HttpQueryHelpers.json_response(error_text='Пользователь не найден', success=False,
                                                  field_error='login')

    def check_login(self, **kwargs):
        data = kwargs.get('data')
        login = data.get('login')

        employee = self.session.query(UserModel).filter(UserModel.login == login)

        if employee.count():
            employee = employee.first()
            return HttpQueryHelpers.json_response(data=employee.to_dict())
        else:
            return HttpQueryHelpers.json_response(error_text='Логин не найден', success=False, field_error='login')

    @classmethod
    def reset_password(cls, **kwargs):
        data = kwargs.get('data')
        new_password = data.get('password')
        user_info = cls.session.query(cls.get_model().where(cls.get_model().id == data.get('id'))).first()

        if user_info:
            user_info.password = Password().get_hash(new_password)
            engine.session.add_all([user_info])
            engine.session.commit()
            return HttpQueryHelpers.json_response(data=True)
        else:
            return HttpQueryHelpers.json_response(error_text=f'Не удалось найти запись по '
                                                             f'указанному ID: {data.get("id")}',)

    @classmethod
    def _prepare_query_filter(cls, query, filter_params):
        if filter_params:
            if filter_params.get('searchString'):
                query = query.where(cls.get_model().name.like(f'%{filter_params.get("searchString")}%'))
            if filter_params.get('dateStart'):
                query = query.where(cls.get_model().create_at > filter_params.get('dateStart'))
            if filter_params.get('dateEnd'):
                query = query.where(cls.get_model().create_at < filter_params.get('dateEnd'))
        return query
