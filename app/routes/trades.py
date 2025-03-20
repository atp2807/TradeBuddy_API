from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, schemas, database

router = APIRouter()

# 의존성 주입 (DB 세션)
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# 거래 데이터 저장
@router.post("/", response_model=schemas.TradeResponse)
def create_trade(trade: schemas.TradeCreate, user_id: int, db: Session = Depends(get_db)):
    return crud.create_trade(db, trade, user_id)

# 특정 사용자의 거래 내역 조회
@router.get("/{user_id}", response_model=list[schemas.TradeResponse])
def get_trades(user_id: int, db: Session = Depends(get_db)):
    return crud.get_trades(db, user_id)
