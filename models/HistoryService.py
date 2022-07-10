from datetime import datetime

from sqlalchemy import Column, Text, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from app import BaseModel
from constants.history_service import HUMAN_AREA_NAME


class HistoryService(BaseModel):
    __tablename__ = 'history_service'
    id = Column(Integer, primary_key=True)
    object_id = Column(Integer)
    type = Column(Text, index=True)
    area = Column(Text, index=True)
    text = Column(Text, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    date = Column(DateTime)
    user_create = relationship("User", lazy='joined')

    def from_object(self, record: dict):
        self.type = record.get('type')
        self.area = record.get('area')
        self.object_id = record.get('object_id')
        self.text = record.get('text')
        self.user_id = record.get('user_id')
        self.date = datetime.now()

    def to_dict(self):
        return {
            'id': self.id,
            'type': self.type,
            'area': HUMAN_AREA_NAME[self.area] if self.area in HUMAN_AREA_NAME.keys() else self.area,
            'text': self.text,
            'date': self.date,
            'object_id': self.object_id,
            'user_id': self.user_id,
            'user_create': self.user_create.to_dict() if self.user_create else None
        }
