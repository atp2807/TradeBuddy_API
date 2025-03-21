import re

def parse_trade_message(text: str):
    pattern = (
        r'현금(매수|매도)체결\s+(.+)\s+\((\d+)\)\s+'
        r'(\d+)주\s+([\d,]+)원'
    )

    match = re.search(pattern, text.replace("\n", " "))
    if match:
        return {
            "trade_type": match.group(1),
            "ticker_name": match.group(2).strip(),
            "ticker_code": match.group(3),
            "quantity": int(match.group(4)),
            "price": int(match.group(5).replace(',', '')),
            "currency": "KRW",
        }
    return None
