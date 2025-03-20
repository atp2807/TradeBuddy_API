from pydantic import BaseModel
from datetime import datetime
from typing import Optional

# 사용자 스키마
class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    pass

class UserResponse(UserBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True

# 거래 데이터 스키마
class TradeBase(BaseModel):
    stock_symbol: str
    trade_time: datetime
    price: float
    quantity: int

class TradeCreate(TradeBase):
    pass

class TradeResponse(TradeBase):
    id: int
    user_id: int

    class Config:
        from_attributes = True
