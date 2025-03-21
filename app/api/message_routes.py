from fastapi import APIRouter, HTTPException
from app.database import get_db
from app.crud import trade_crud
from extractor.kr.nh import parse_nh_message

router = APIRouter()

@router.post("/parse-message")
def parse_message(message: str, db=Depends(get_db)):
    trade = parse_nh_message(message)
    if not trade:
        raise HTTPException(status_code=400, detail="메시지 파싱 실패")

    return trade_crud.create_trade(db, trade)
