# app/models/trade_model.py
from sqlalchemy import Column, Integer, String, DECIMAL, DateTime, ForeignKey
from sqlalchemy.sql import func
from app.database import Base

class Trade(Base):
    __tablename__ = "trades"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    stock_symbol = Column(String(20), nullable=False)
    trade_time = Column(DateTime, nullable=False)
    trade_price = Column(DECIMAL(10, 2), nullable=False)
    trade_quantity = Column(Integer, nullable=False)
    trade_type = Column(String(10), nullable=False)  # BUY or SELL
    message_source = Column(String(50))
    trade_status = Column(String(20), default="CONFIRMED")  # CONFIRMED, CANCELLED, PENDING
    created_at = Column(DateTime(timezone=True), server_default=func.now())
