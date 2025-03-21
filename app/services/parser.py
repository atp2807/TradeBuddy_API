import re
from datetime import datetime
from app.models import Trade
from sqlalchemy.orm import Session

# 거래 데이터 추출 함수
def parse_trade_message(message: str, user_id: int, db: Session):
    """
    메시지에서 종목, 거래시각, 수량, 매도/매수를 추출해서 trades 테이블에 저장
    """
    # 예제 메시지 패턴: "삼성전자 100주 매수 85,000원 2025-03-21 10:30"
    pattern = re.compile(r"(\w+)\s(\d+)주\s(매수|매도)\s([\d,]+)원\s([\d-]+\s[\d:]+)")
    match = pattern.search(message)

    if match:
        stock_symbol = match.group(1)
        trade_quantity = int(match.group(2))
        trade_type = "BUY" if match.group(3) == "매수" else "SELL"
        trade_price = float(match.group(4).replace(",", ""))
        trade_time = datetime.strptime(match.group(5), "%Y-%m-%d %H:%M")

        new_trade = Trade(
            user_id=user_id,
            stock_symbol=stock_symbol,
            trade_quantity=trade_quantity,
            trade_type=trade_type,
            trade_price=trade_price,
            trade_time=trade_time,
            message_source="KAKAO",  # 기본 메시지 소스
            trade_status="PENDING"  # 기본 상태는 PENDING
        )

        db.add(new_trade)
        db.commit()
        return new_trade
    else:
        return None
