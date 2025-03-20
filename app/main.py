from fastapi import FastAPI
from .routes import users, trades

app = FastAPI()

app.include_router(users.router, prefix="/users", tags=["Users"])
app.include_router(trades.router, prefix="/trades", tags=["Trades"])

@app.get("/")
def read_root():
    return {"message": "TradeBuddy API 서버가 실행 중입니다 🚀"}
