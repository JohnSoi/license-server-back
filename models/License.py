from sqlalchemy import Column, Text, Float, JSON
from sqlalchemy.dialects.postgresql import UUID

from models.BaseModel import BaseModel
from models.UserMixins import UserMixins


class License(BaseModel, UserMixins):
    __tablename__ = 'licenses'

    uuid = Column(UUID, unique=True)
    name = Column(Text, unique=True, index=True)
    cost = Column(Float)
    group_uuid = Column(UUID, nullable=True)
    limitation = Column(JSON)

    def _manual_response_fields(self, result: dict):
        result['cost'] = 0
