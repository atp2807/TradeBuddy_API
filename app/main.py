# app/main.py

from fastapi import FastAPI
from app.api.trade_routes import router as trade_router
from app.api.user_routes import router as user_router
from app.api import fieldnames

from app.api.metadata_routes import router as metadata_router
from fastapi.middleware.cors import CORSMiddleware

from app.api.broker_routes import router as broker_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://mydeeptrack.com",
        "https://www.mydeeptrack.com"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_router, prefix="/users", tags=["Users"])
app.include_router(trade_router, prefix="/trades", tags=["Trades"])
app.include_router(metadata_router, prefix="/meta", tags=["Metadata"])
app.include_router(fieldnames.router)
app.include_router(broker_router, tags=["Brokers"])