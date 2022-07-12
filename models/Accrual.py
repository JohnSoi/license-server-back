from models.BaseModel import BaseModel
from models.UserMixins import UserMixins

from sqlalchemy import Column, Integer, Float, ForeignKey
from sqlalchemy.dialects.postgresql import UUID


class Accrual(BaseModel, UserMixins):
    __tablename__ = 'accruals'

    uuid = Column(UUID, unique=True)
    sum = Column(Float, default=0)
    invoice_id = Column(Integer, index=True)
    client_uuid = Column(Integer, ForeignKey('clients.id'))
    license_id = Column(Integer, ForeignKey('licenses.id'))


