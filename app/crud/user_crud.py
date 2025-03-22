from typing import Optional
from sqlalchemy.orm import Session
from app.models.user_model import User
from app.schemas.user_schema import UserCreate

def create_user(db: Session, user: UserCreate) -> User:
    db_user = User(email=user.email, nickname=user.nickname or "SmartTraders")
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user(db: Session, user_id: int) -> Optional[User]:  # ✅ 여기!
    return db.query(User).filter(User.id == user_id).first()
