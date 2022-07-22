from sqlalchemy import Column, Text, Boolean
from models.BaseModel import BaseModel
from models.UserMixins import UserMixins
from sqlalchemy.dialects.postgresql import UUID


class Client(BaseModel, UserMixins):
    __tablename__ = 'clients'

    uuid = Column(UUID, unique=True)
    name = Column(Text, index=True)
    inn = Column(Text)
    kpp = Column(Text)
    is_active = Column(Boolean, default=True)
    photo = Column(Text)
    phone = Column(Text, nullable=True)
    email = Column(Text)
    license_uuid = Column(UUID, nullable=True, index=True)
    photo_url = Column(Text, nullable=True)

    def _is_active_default(self, result: dict):
        if result.get('is_active') is None:
            result['is_active'] = True
