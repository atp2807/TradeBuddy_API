from pydantic import BaseModel, Field

class UserCreate(BaseModel):
    username: str = Field(..., description="사용자 이름")
    email: str = Field(..., description="이메일 주소")

class UserResponse(UserCreate):
    id: int = Field(..., description="사용자 ID")
