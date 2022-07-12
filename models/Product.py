from models.BaseModel import BaseModel
from models.UserMixins import UserMixins

from sqlalchemy import Column, Text, Integer, ForeignKey
from sqlalchemy.dialects.postgresql import UUID


class Product(BaseModel, UserMixins):
    __tablename__ = 'products'

    name = Column(Text, index=True)
    description = Column(Text)
    license_id = Column(Integer, ForeignKey('licenses.id'))
    photo_url = Column(Text, nullable=True)
