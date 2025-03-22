from pydantic import BaseModel, EmailStr
from datetime import datetime

class UserCreate(BaseModel):
    email: EmailStr
    nickname: str = "SmartTraders"  # 기본값 설정

class UserResponse(BaseModel):
    id: int
    email: EmailStr
    nickname: str
    created_at: datetime

    class Config:
        from_attributes = True  # Pydantic v2용
