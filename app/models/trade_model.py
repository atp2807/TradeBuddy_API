from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.sql import func
from app.db.session import Base

class Trade(Base):
    __tablename__ = "trades"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    symbol = Column(String, nullable=False)
    side = Column(String, nullable=False)  # buy/sell
    price = Column(Float, nullable=False)
    quantity = Column(Float, nullable=False)
    trade_time = Column(DateTime, nullable=False)
    created_at = Column(DateTime, server_default=func.now())
