# app/crud/trade_crud.py
from sqlalchemy.orm import Session
from app.models.trade_model import Trade
from app.schemas.trade_schema import TradeCreate
from datetime import datetime

def create_trade(db: Session, trade: TradeCreate):
    db_trade = Trade(
        user_id=trade.user_id,
        stock_symbol=trade.stock_symbol,
        trade_time=trade.trade_time,
        trade_price=trade.trade_price,
        trade_quantity=trade.trade_quantity,
        trade_type=trade.trade_type,
        message_source=trade.message_source,
        trade_status=trade.trade_status,
        created_at=datetime.now()
    )
    db.add(db_trade)
    db.commit()
    db.refresh(db_trade)
    return db_trade
