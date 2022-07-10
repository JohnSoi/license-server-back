import uuid
from datetime import datetime

from sqlalchemy import Column, Integer, Text, Date, Boolean, ForeignKey, DateTime

from classes.Password import Password
from models.BaseModel import BaseModel
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
    date_birthday = Column(Date)
    last_active = Column(DateTime)
    is_active = Column(Boolean, default=True)

    def add_default_data(self):
        password_helpers = Password()

        self.engine.session.add_all([
            User(
                uuid=str(uuid.uuid4()),
                login='default',
                password=password_helpers.get_hash('default'),
                name='default',
                surname='user',
                second_name='user',
                date_birthday=datetime.now().date(),
                role=self.engine.session.query(Role).filter(Role.name == 'Суперпользователь').first(),
                is_active=True,
                date_create=datetime.now().date(),
            )
        ])
        self.engine.session.commit()
