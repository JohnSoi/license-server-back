from sqlalchemy import Column, Integer, Text, Boolean
from models.BaseModel import BaseModel
from models.UserMixins import UserMixins
from sqlalchemy.dialects.postgresql import UUID


class Client(BaseModel, UserMixins):
    __tablename__ = 'clients'

    uuid = Column(UUID, unique=True)
    name = Column(Text, nullable=False, index=True)
    inn = Column(Integer)
    kpp = Column(Integer)
    is_active = Column(Boolean, default=True)
    photo = Column(Text)
    license_uuid = Column(UUID, nullable=True)

