from sqlalchemy import Column, Integer, Text
from sqlalchemy.dialects.postgresql import ARRAY

from models.BaseModel import BaseModel


class Role(BaseModel):
    __tablename__ = 'roles'
    id = Column(Integer, primary_key=True)
    name = Column(Text, index=True)
    permissions_ids = Column(ARRAY(Integer))

    def from_object(self, record: dict):
        self.name = record.get('name')
        self.permissions_ids = record.get('permissions_ids')

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'permissions_ids': self.permissions_ids
        }

    @staticmethod
    def add_default_data():
        engine.session.add_all([
            Role(name='Суперпользователь', permissions_ids=[0]),
        ])

