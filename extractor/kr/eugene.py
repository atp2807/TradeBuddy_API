import re

def parse_eugene_sms(text: str) -> dict:
    pattern = re.compile(
        r"종목\s*:\s*(?P<stock_name>.+?)\s*\[(?P<stock_symbol>[A-Z]+)\]\s*"
        r"구분\s*:\s*(?P<trade_type>매수체결|매도체결)\s*\[#(?P<order_id>\d+)\]\s*"
        r"가격\s*:\s*(?P<trade_price>[\d.]+)USD\s*"
        r"수량\s*:\s*(?P<trade_quantity>\d+)주"
    )
    match = pattern.search(text)
    if not match:
        return {}

    return {
        "stock_name": match.group("stock_name"),
        "stock_symbol": match.group("stock_symbol"),
        "trade_type": "BUY" if "매수" in match.group("trade_type") else "SELL",
        "trade_price": float(match.group("trade_price")),
        "trade_quantity": int(match.group("trade_quantity")),
        "order_id": match.group("order_id"),
        "currency": "USD",
        "broker": "Eugene",
        "message_source": "SMS"
    }
