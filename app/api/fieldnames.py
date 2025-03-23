from fastapi import APIRouter
from sqlalchemy.inspection import inspect
from app.models.trade_model import Trade

router = APIRouter()

@router.get("/fieldnames")
def get_fieldnames():
    mapper = inspect(Trade)
    return {col.key: col.key for col in mapper.attrs}
