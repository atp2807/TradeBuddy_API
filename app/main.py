# app/main.py

from fastapi import FastAPI
from app.api.trade_router import router as trade_router
from app.api.user_routes import router as user_router
from app.api import fieldnames

from app.api.metadata_routes import router as metadata_router

app = FastAPI()

app.include_router(user_router, prefix="/users", tags=["Users"])
app.include_router(trade_router, prefix="/trades", tags=["Trades"])

app.include_router(metadata_router, prefix="/meta", tags=["Metadata"])
app.include_router(fieldnames.router)