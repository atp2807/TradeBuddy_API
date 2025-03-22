from pydantic import BaseModel, Field
from datetime import datetime
from typing import Literal


# 1. API 요청용 스키마
class TradeCreate(BaseModel):
    user_id: int = Field(..., description="사용자 ID")
    broker: str = Field(..., description="증권사 이름")
    stock_symbol: str = Field(..., description="종목 코드 또는 티커")
    trade_type: Literal["BUY", "SELL"] = Field(..., description="매매 구분")
    trade_quantity: int = Field(..., description="체결 수량")
    trade_price: float = Field(..., description="체결 단가")
    trade_time: datetime = Field(..., description="거래 시간")
    message_source: str = Field(..., description="문자 or 카카오톡")
    trade_status: Literal["CONFIRMED", "CANCELLED", "PENDING"] = Field(..., description="거래 상태")


# 2. API 응답용 스키마
class TradeResponse(TradeCreate):
    id: int = Field(..., description="거래 ID")
