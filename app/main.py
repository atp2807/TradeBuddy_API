# app/main.py

from fastapi import FastAPI
from app.api.trade_router import router as trade_router
from app.api.user_routes import router as user_router

app = FastAPI()

app.include_router(user_router, prefix="/users", tags=["Users"])
app.include_router(trade_router, prefix="/trades", tags=["Trades"])
