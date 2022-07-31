from sqlalchemy import Column, Text, Boolean, Integer, ForeignKey
from sqlalchemy.orm import relationship

from models.BaseModel import BaseModel
from models.Product import Product
from models.UserMixins import UserMixins
from sqlalchemy.dialects.postgresql import UUID


class Client(BaseModel, UserMixins):
    __tablename__ = 'clients'

    uuid = Column(UUID, unique=True)
    name = Column(Text, index=True)
    inn = Column(Text)
    kpp = Column(Text)
    is_active = Column(Boolean, default=True)
    photo = Column(Text)
    phone = Column(Text, nullable=True)
    email = Column(Text)
    license_id = Column(Integer, ForeignKey('licenses.id'))
    photo_url = Column(Text, nullable=True)

    license = relationship("License", lazy='joined', foreign_keys=[license_id])

    def _manual_response_fields(self, result: dict):
        license_data = self.license.to_dict() if self.license else None

        if result.get('is_active') is None:
            result['is_active'] = True

        if license_data:
            result['license_name'] = license_data.get('name')
            result['license'] = license_data
            product = self.session.query(Product).where(Product.license_id == license_data.get('license_id')).all()
            result['product'] = [item.to_dict() for item in product]
