import re

def parse_trade_message(text: str):
    pattern = (
        r'종목명\s*:\s*(.+)\(([A-Z0-9]+)\)\s*'
        r'매매구분\s*:\s*(매수|매도)\s*'
        r'주문수량\s*:\s*(\d+)주\s*'
        r'체결수량\s*:\s*(\d+)주\s*'
        r'체결단가\s*:\s*([\d,]+)원'
    )

    match = re.search(pattern, text.replace("\n", " "))
    if match:
        return {
            "ticker_name": match.group(1).strip(),
            "ticker_code": match.group(2),
            "trade_type": match.group(3),
            "order_qty": int(match.group(4)),
            "quantity": int(match.group(5)),
            "price": int(match.group(6).replace(',', '')),
        }
    return None
