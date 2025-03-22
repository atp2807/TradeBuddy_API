from sqlalchemy import Column, Integer, String, DateTime, func
from app.db.session import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, nullable=False)
    nickname = Column(String, nullable=False, default="SmartTraders")  # 추가됨
    created_at = Column(DateTime(timezone=True), server_default=func.now())
