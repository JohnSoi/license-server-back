import uuid
from datetime import datetime

from sqlalchemy import Column, Text, Date, Boolean, DateTime
from sqlalchemy.dialects.postgresql import UUID

from classes.Password import Password
from models.BaseModel import BaseModel


class User(BaseModel):
    __tablename__ = 'users'

    _gurded = ['password']

    uuid = Column(UUID, unique=True)
    name = Column(Text, index=True)
    surname = Column(Text, index=True)
    second_name = Column(Text, nullable=True)
    photo_url = Column(Text)
    phone = Column(Text, nullable=True)
    email = Column(Text, nullable=True)
    login = Column(Text, index=True)
    password = Column(Text)
    date_birthday = Column(Date)
    last_active = Column(DateTime)
    is_active = Column(Boolean, default=True)
    telephone = Column(Text)

    def add_default_data(self):
        password_helpers = Password()

        self.session.add_all([
            User(
                uuid=str(uuid.uuid4()),
                login='default',
                password=password_helpers.get_hash('default'),
                name='default',
                surname='user',
                second_name='user',
                email='test@tes.ru',
                date_birthday=datetime.now().date(),
                is_active=True,
                create_at=datetime.now().date(),
                telephone='79999',
            )
        ])
        self.session.commit()

    def _manual_fillable_fields(self, record: dict):
        if not self.uuid:
            self.uuid = uuid.UUID()

    def _manual_response_fields(self, result: dict) -> None:
        if self.name and self.surname:
            result['full_name'] = f'{self.surname} {self.name[0]}.{self.second_name[0] if self.second_name else ""}'
