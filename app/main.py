from fastapi import FastAPI
from app.api import user_routes, trade_routes, message_routes
from app.api.endpoints import trades

app = FastAPI()

app.include_router(user_routes.router, prefix="/users", tags=["Users"])
app.include_router(trade_routes.router, prefix="/trades", tags=["Trades"])
app.include_router(message_routes.router, prefix="/messages", tags=["Messages"])
app.include_router(trades.router, tags=["trades"])

@app.get("/")
def read_root():
    return {"message": "TradeBuddy API 서버가 실행 중입니다 🚀"}
