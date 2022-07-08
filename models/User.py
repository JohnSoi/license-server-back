import uuid
from datetime import datetime

from sqlalchemy import Column, Integer, Text, Date, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from app import BaseModel, engine
from classes.Password import Password
from models.Role import Role


class User(BaseModel):
    __tablename__ = 'users'

    uuid = Column(Text, unique=True)
    name = Column(Text, nullable=False, index=True)
    surname = Column(Text, nullable=False, index=True)
    second_name = Column(Text, nullable=True)
    role_id = Column(Integer, ForeignKey('roles.id'))
    photo_url = Column(Text)
    login = Column(Text, nullable=False, index=True)
    password = Column(Text, nullable=False)
    date_create = Column(DateTime)
    date_birthday = Column(Date)
    date_update = Column(DateTime)
    date_delete = Column(DateTime)
    last_active = Column(DateTime)
    is_active = Column(Boolean, default=True)

    role = relationship('Role', lazy='joined')

    def from_object(self, record: dict):
        password_helpers = Password()
        self.id = record.get('id')
        self.uuid = record.get('uuid') or str(uuid.uuid4())
        self.name = record.get('name')
        self.surname = record.get('surname')
        self.second_name = record.get('second_name')
        self.role_id = record.get('role_id')
        self.photo_url = record.get('photo_url')
        self.login = record.get('login')
        self.password = password_helpers.get_hash(record.get('password')) if record.get('password') else ''
        self.date_create = record.get('date_create') or datetime.now()
        self.date_update = datetime.now()
        self.date_delete = record.get('date_delete')
        self.date_birthday = record.get('date_birthday')
        self.last_active = record.get('last_active')
        self.is_active = record.get('is_active') if record.get('is_active') is not None else True

        return self

    def to_dict(self):
        return {
             'id': self.id,
             'uuid': self.uuid or '',
             'name': self.name,
             'surname': self.surname,
             'second_name': self.second_name,
             'role_id': self.role_id,
             'photo_url': self.photo_url,
             'login': self.login,
             'password': self.password,
             'date_create': self.date_create,
             'date_update': self.date_update,
             'date_delete': self.date_delete,
             'date_birthday': self.date_birthday,
             'last_active': self.last_active,
             'is_active': self.is_active,
             'role': self.role.to_dict() if self.role else None,
             'role_name': self.role.to_dict().get('name') if self.role and self.role.to_dict() else None,
             'full_name': '{} {}.{}'.format(self.surname or '',
                                            self.name[0] if self.name else '',
                                            self.second_name[0] if self.second_name else '')
        }

    @staticmethod
    def add_default_data():
        password_helpers = Password()
        engine.session.add_all([
            User(
                uuid=str(uuid.uuid4()),
                login='default',
                password=password_helpers.get_hash('default'),
                name='default',
                surname='user',
                second_name='user',
                date_birthday=datetime.now().date(),
                role=engine.session.query(Role).filter(Role.name == 'Суперпользователь').first(),
                is_active=True,
                date_create=datetime.now().date(),
            )
        ])
        engine.session.commit()

