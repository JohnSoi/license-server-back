from sqlalchemy.orm import relationship

from models.BaseModel import BaseModel
from models.UserMixins import UserMixins

from sqlalchemy import Column, Integer, Float, ForeignKey
from sqlalchemy.dialects.postgresql import UUID


class Accrual(BaseModel, UserMixins):
    __tablename__ = 'accruals'

    uuid = Column(UUID, unique=True)
    sum = Column(Float, default=0)
    invoice_id = Column(Integer, index=True)
    client_id = Column(Integer, ForeignKey('clients.id'))
    license_id = Column(Integer, ForeignKey('licenses.id'))

    license = relationship("License", lazy='joined', foreign_keys=[license_id])
    client = relationship("Client", lazy='joined', foreign_keys=[client_id])

    def _manual_response_fields(self, record: dict) -> None:
        license_data = self.license.to_dict() if self.license else None
        client_data = self.client.to_dict() if self.client else None

        if license_data:
            record['license_name'] = license_data.get('name')
            record['license'] = license_data

        if client_data:
            record['client_name'] = client_data.get('name')
            record['client'] = client_data
