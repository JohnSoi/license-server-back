from classes.HttpQuery import HttpQueryHelpers
from classes.BaseClass import BaseClass
from classes.Password import Password
from models.User import User as UserModel


class User(BaseClass):
    def __init__(self):
        self._additional_methods = {
            'LoginCheck': self.check_login,
            'Login': self.login
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
