import re

def parse_trade_message(text: str):
    pattern = (
        r'▶종목명:\s*(.+)\(([A-Z]+)\)\s*'
        r'▶(매수|매도)수량:\s*(\d+)주\s*'
        r'▶잔량:\s*\d+주\s*'
        r'▶체결단가:\s*USD\s*([\d\.]+)'
    )

    match = re.search(pattern, text.replace("\n", " "))
    if match:
        return {
            "ticker_name": match.group(1).strip(),
            "ticker_code": match.group(2),
            "trade_type": match.group(3),
            "quantity": int(match.group(4)),
            "price": float(match.group(5)),
            "currency": "USD",
        }
    return None
