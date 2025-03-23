from sqlalchemy import Column, Integer, String
from app.db.session import Base

class Broker(Base):
    __tablename__ = "broker_info"

    id = Column(Integer, primary_key=True, index=True)
    country = Column(String, index=True)
    alias = Column(String, index=True)
    sms_number = Column(String, unique=True, index=True)
    kakao_channel_name = Column(String, unique=True, index=True)
