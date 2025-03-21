import re
from typing import Optional

def parse_nh_sms(message: str) -> Optional[dict]:
    pattern = r"\[(.*?)\] (.*?) (매수|매도) (\d+)주 (\d+,\d+)원 (\d{2}:\d{2})"
    match = re.search(pattern, message)
    if match:
        return {
            "stock_symbol": match.group(2),
            "trade_type": "BUY" if match.group(3) == "매수" else "SELL",
            "trade_quantity": int(match.group(4)),
            "trade_price": float(match.group(5).replace(",", "")),
            "trade_time": match.group(6)
        }
    return None
