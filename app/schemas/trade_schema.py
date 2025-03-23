from pydantic import BaseModel
from typing import List
from datetime import datetime

class TradeCreate(BaseModel):
    user_id: int
    stock_symbol: str
    stock_name: str
    trade_time: str
    trade_price: float
    trade_quantity: float
    trade_type: str
    message_source: str
    trade_status: str
    market_type: str

class TradeResponse(TradeCreate):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True  # Pydantic v2 호환

class TradeBulkCreate(BaseModel):
    trades: List[TradeCreate]