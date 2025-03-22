# app/api/trade_router.py

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.trade_schema import TradeCreate
from app.crud import trade_crud

router = APIRouter()

@router.post("/", response_model=dict)
def add_trade(trade: TradeCreate, db: Session = Depends(get_db)):
    # 파싱은 클라이언트 앱에서 처리된 상태
    created_trade = trade_crud.create_trade(db=db, trade=trade)

    return {
        "status": "success",
        "trade_id": created_trade.id,
        "stock": trade.stock_symbol,
        "price": trade.trade_price
    }
