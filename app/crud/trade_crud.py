from sqlalchemy.orm import Session
from app.models.trade_model import Trade
from app.schemas.trade_schema import TradeCreate
from datetime import datetime

def create_trade(db: Session, trade: TradeCreate):
    db_trade = Trade(**trade.model_dump())
    db.add(db_trade)
    db.commit()
    db.refresh(db_trade)
    return db_trade

def create_trade_bulk(db: Session, trades: list[TradeCreate]) -> int:
    trade_objs = []

    for trade in trades:
        trade_data = trade.model_dump()

        # ✅ 문자열로 들어온 trade_time을 datetime으로 변환
        trade_data["trade_time"] = datetime.fromisoformat(trade_data["trade_time"])

        trade_objs.append(Trade(**trade_data))

    db.bulk_save_objects(trade_objs)
    db.commit()
    return len(trade_objs)