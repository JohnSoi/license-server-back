from sqlalchemy import Column, Text, Float, JSON, Integer, ForeignKey
from sqlalchemy.dialects.postgresql import UUID

from models.BaseModel import BaseModel
from models.UserMixins import UserMixins


class License(BaseModel, UserMixins):
    __tablename__ = 'licenses'

    uuid = Column(UUID, unique=True)
    name = Column(Text, unique=True, index=True)
    cost = Column(Float)
    group_uuid = Column(Integer, ForeignKey('licenses.id'))
    limitation = Column(JSON)

    def _manual_response_fields(self, result: dict):
        if result.get('cost') is None:
            result['cost'] = 0
