from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.trade_schema import TradeCreate, TradeResponse, TradeBulkCreate
from app.crud.trade_crud import create_trade, create_trade_bulk

router = APIRouter()

# ✅ 단일 트레이드 업로드
@router.post("/", response_model=TradeResponse)
def upload_trade(trade: TradeCreate, db: Session = Depends(get_db)):
    return create_trade(db, trade)

# ✅ 여러 트레이드 bulk 업로드
@router.post("/trades/bulk")
def upload_bulk_trades(trades: TradeBulkCreate, db: Session = Depends(get_db)):
    try:
        result = create_trade_bulk(db, trades.trades)
        return {"message": f"✅ {result} trades uploaded successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
