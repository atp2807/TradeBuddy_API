from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.schemas.broker_schema import BrokerOut
from app.crud.broker_crud import get_all_brokers

router = APIRouter()

@router.get("/brokers", response_model=list[BrokerOut])
def read_brokers(db: Session = Depends(get_db)):
    return get_all_brokers(db)
