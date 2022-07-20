from sqlalchemy import Column, Text
from models.BaseModel import BaseModel
from models.UserMixins import UserMixins
from sqlalchemy.dialects.postgresql import UUID


class TypePaid(BaseModel, UserMixins):
    __tablename__ = 'type_paids'

    uuid = Column(UUID, unique=True)
    name = Column(Text, index=True)
