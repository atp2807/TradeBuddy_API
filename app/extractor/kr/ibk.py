import re

def parse_trade_message(text: str):
    pattern = r'(\S+)\s고객님,\s(.+)\((\d+)\)\s(\d+)주\s(매수|매도)\s체결.*?체결가\s([\d,]+)원.*?체결금액\s([\d,]+)원.*?계좌\s([\d-]+)'
    match = re.search(pattern, text.replace("\n", " "))
    if match:
        return {
            "name": match.group(1),
            "ticker_name": match.group(2).strip(),
            "ticker_code": match.group(3),
            "quantity": int(match.group(4)),
            "trade_type": match.group(5),
            "price": int(match.group(6).replace(',', '')),
            "amount": int(match.group(7).replace(',', '')),
            "account": match.group(8),
            "currency": "KRW"
        }
    return None
