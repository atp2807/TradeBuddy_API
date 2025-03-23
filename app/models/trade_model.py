from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.sql import func
from app.db.session import Base

class Trade(Base):
    __tablename__ = "trades"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    stock_symbol = Column(String, nullable=False)
    stock_name = Column(String, nullable=False)
    trade_time = Column(String, nullable=False)
    trade_price = Column(Float, nullable=False)
    trade_quantity = Column(Float, nullable=False)
    trade_type = Column(String, nullable=False)
    message_source = Column(String, nullable=False)
    trade_status = Column(String, nullable=False)
    created_at = Column(DateTime, server_default=func.now())
    market_type = Column(String(10))
