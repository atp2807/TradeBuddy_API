import re
from datetime import datetime

def parse_nh_sms(message: str, user_id: int):
    result = {}

    result["broker_name"] = "NH투자증권"
    result["user_id"] = user_id
    result["message_source"] = "SMS"
    result["trade_time"] = datetime.now()

    trade_type_match = re.search(r"체결종류\s*:\s*(매수|매도)", message)
    stock_symbol_match = re.search(r"종목코드\s*:\s*(\d+)", message)
    stock_name_match = re.search(r"종\s*목\s*명\s*:\s*(\S+)", message)
    quantity_match = re.search(r"체결수량\s*:\s*([\d,]+)", message)
    price_match = re.search(r"체결단가\s*:\s*([\d,]+)", message)

    if trade_type_match:
        result["trade_type"] = trade_type_match.group(1)
    if stock_symbol_match:
        result["stock_symbol"] = stock_symbol_match.group(1)
    if stock_name_match:
        result["stock_name"] = stock_name_match.group(1)
    if quantity_match:
        result["trade_quantity"] = int(quantity_match.group(1).replace(",", ""))
    if price_match:
        result["trade_price"] = float(price_match.group(1).replace(",", ""))

    return result