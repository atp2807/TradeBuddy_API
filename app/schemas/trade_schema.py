from pydantic import BaseModel
from datetime import datetime
from typing import Literal

class TradeCreate(BaseModel):
    stock_symbol: str
    trade_time: datetime
    trade_price: float
    trade_quantity: int
    trade_type: Literal["BUY", "SELL"]
    message_source: str
    trade_status: str

class TradeResponse(TradeCreate):
    id: int
    user_id: int
    created_at: datetime

    class Config:
        from_attributes = True  # Pydantic v2 대응
