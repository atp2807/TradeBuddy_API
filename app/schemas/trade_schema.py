from pydantic import BaseModel
from datetime import datetime
from typing import List

class TradeCreate(BaseModel):
    user_id: int
    symbol: str
    side: str
    price: float
    quantity: float
    trade_time: datetime

class TradeResponse(TradeCreate):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True  # Pydantic v2 호환

class TradeBulkCreate(BaseModel):
    trades: List[TradeCreate]