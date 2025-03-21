from fastapi import APIRouter, Depends, BackgroundTasks
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Trade, HabitAnalysis
from datetime import datetime

router = APIRouter()

# 비동기 AI 분석 함수
def analyze_trades(db: Session):
    """
    PENDING 상태의 거래 내역을 분석 후 habit_analysis 테이블에 저장
    """
    pending_trades = db.query(Trade).filter(Trade.trade_status == "PENDING").all()
    
    for trade in pending_trades:
        risk_score = calculate_risk(trade)
        pattern = detect_pattern(trade)
        ai_feedback = generate_feedback(risk_score)

        new_analysis = HabitAnalysis(
            user_id=trade.user_id,
            trade_id=trade.id,
            risk_score=risk_score,
            pattern=pattern,
            ai_feedback=ai_feedback,
            created_at=datetime.now()
        )

        db.add(new_analysis)
        trade.trade_status = "CONFIRMED"  # 분석 완료된 거래는 CONFIRMED로 변경
    
    db.commit()

# 분석 요청 API (비동기 처리)
@router.post("/analyze")
def trigger_analysis(background_tasks: BackgroundTasks, db: Session = Depends(get_db)):
    background_tasks.add_task(analyze_trades, db)
    return {"message": "AI 분석이 시작되었습니다. 결과는 곧 반영됩니다."}
