from sqlalchemy.orm import Session
from . import models, schemas

# 사용자 생성
def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# 사용자 조회
def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

# 거래 데이터 저장
def create_trade(db: Session, trade: schemas.TradeCreate, user_id: int):
    db_trade = models.Trade(**trade.dict(), user_id=user_id)
    db.add(db_trade)
    db.commit()
    db.refresh(db_trade)
    return db_trade

# 특정 사용자의 거래 내역 조회
def get_trades(db: Session, user_id: int):
    return db.query(models.Trade).filter(models.Trade.user_id == user_id).all()
