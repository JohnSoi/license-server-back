from models.BaseModel import BaseModel
from models.UserMixins import UserMixins

from sqlalchemy import Column, Text
from sqlalchemy.dialects.postgresql import UUID


class Product(BaseModel, UserMixins):
    __tablename__ = 'products'

    name = Column(Text)
    description = Column(Text)
    group_uuid = Column(UUID)
