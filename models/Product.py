from sqlalchemy.orm import relationship

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

    license = relationship("License", lazy='joined', foreign_keys=[license_id])

    def _manual_response_fields(self, record: dict) -> None:
        license_data = self.license.to_dict() if self.license else None
        if license_data:
            record['license_name'] = license_data.get('name')
            record['license'] = license_data
