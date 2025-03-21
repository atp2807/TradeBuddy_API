import re

def parse_trade_message(text: str):
    pattern = r'(\S+)\s고객님\s*\(계좌\s([\d-]+)\)\s(.+)\s(\d+)주\s(매수|매도)체결\s\(체결가\s([\d,]+)원.*?체결금액\s([\d,]+)원\)'
    match = re.search(pattern, text.replace("\n", " "))
    if match:
        return {
            "name": match.group(1),
            "account": match.group(2),
            "ticker_name": match.group(3).strip(),
            "quantity": int(match.group(4)),
            "trade_type": match.group(5),
            "price": int(match.group(6).replace(',', '')),
            "amount": int(match.group(7).replace(',', '')),
            "currency": "KRW"
        }
    return None
