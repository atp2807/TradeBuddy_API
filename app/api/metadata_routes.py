# app/api/metadata_routes.py
from fastapi import APIRouter
from fastapi.responses import JSONResponse

router = APIRouter()

@router.get("/fieldnames")
def get_field_names():
    field_map = {
        "user_id": "user_id",
        "stock_symbol": "stock_symbol",
        "stock_name": "stock_name",
        "trade_time": "trade_time",
        "trade_price": "trade_price",
        "trade_quantity": "trade_quantity",
        "trade_type": "trade_type",
        "message_source": "message_source",
        "trade_status": "trade_status",
        "market_type": "market_type"
    }
    return JSONResponse(content=field_map)
