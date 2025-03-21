import re

def parse_trade_message(text: str):
    pattern = (
        r'종목명\s*:\s*(.+?)\s*'
        r'종목코드\s*:\s*([A-Z]+)\s*'
        r'체결가격\s*:\s*([\d\.]+)\s*USD\s*'
        r'주문수량\s*:\s*(\d+)주\s*'
        r'체결수량\s*:\s*(\d+)주'
    )

    match = re.search(pattern, text.replace("\n", " "))
    if match:
        return {
            "ticker_name": match.group(1).strip(),
            "ticker_code": match.group(2),
            "price": float(match.group(3)),
            "order_qty": int(match.group(4)),
            "quantity": int(match.group(5)),
            "currency": "USD",
        }
    return None
