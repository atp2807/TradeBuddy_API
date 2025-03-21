import re
from datetime import datetime
from app.schemas.trade_schema import TradeCreate

def parse_nh_message(message: str) -> TradeCreate | None:
    # 예시 메시지:
    # "[NH투자증권] 삼성전자 매수 10주 체결 68,000원 03/20 13:45"

    pattern = r"\[(.*?)\]\s+(.*?)\s+(매수|매도)\s+(\d+)주\s+체결\s+([\d,]+)원\s+(\d{2}/\d{2})\s+(\d{2}:\d{2})"
    match = re.search(pattern, message)

    if not match:
        return None

    broker, stock, trade_type, qty, price, date_str, time_str = match.groups()

    trade_datetime = datetime.strptime(f"2025/{date_str} {time_str}", "%Y/%m/%d %H:%M")

    return TradeCreate(
        user_id=1,  # 실제로는 사용자 매핑 필요
        stock_symbol=stock,
        trade_time=trade_datetime,
        trade_price=float(price.replace(",", "")),
        trade_quantity=int(qty),
        trade_type="BUY" if trade_type == "매수" else "SELL",
        message_source="SMS",
        trade_status="CONFIRMED"
    )
