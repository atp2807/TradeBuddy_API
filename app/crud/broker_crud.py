from sqlalchemy.orm import Session
from app.models.broker_model import Broker

def get_all_brokers(db: Session):
    return db.query(Broker).all()
