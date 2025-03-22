from sqlalchemy.orm import Session
from app.models.trade_model import Trade
from app.schemas.trade_schema import TradeCreate

def create_trade(db: Session, trade: TradeCreate):
    db_trade = Trade(**trade.model_dump())
    db.add(db_trade)
    db.commit()
    db.refresh(db_trade)
    return db_trade

def create_trade_bulk(db: Session, trades: list[TradeCreate]) -> int:
    trade_objs = [Trade(**trade.model_dump()) for trade in trades]
    db.bulk_save_objects(trade_objs)
    db.commit()
    return len(trade_objs)