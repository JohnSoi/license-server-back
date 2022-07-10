from sqlalchemy import Column, Text, Integer

from models.BaseModel import BaseModel


class HistoryService(BaseModel):
    __tablename__ = 'history_service'
    object_id = Column(Integer)
    type = Column(Text, index=True)
    area = Column(Text, index=True)
    text = Column(Text, index=True)
