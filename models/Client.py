from sqlalchemy import Column, Text, Boolean
from models.BaseModel import BaseModel
from models.UserMixins import UserMixins
from sqlalchemy.dialects.postgresql import UUID


class Client(BaseModel, UserMixins):
    __tablename__ = 'clients'

    uuid = Column(UUID, unique=True)
    name = Column(Text, nullable=False, index=True)
    inn = Column(Text, nullable=False)
    kpp = Column(Text, nullable=False)
    is_active = Column(Boolean, default=True)
    photo = Column(Text)
    phone = Column(Text, nullable=True)
    email = Column(Text, nullable=False)
    license_uuid = Column(UUID, nullable=True)

