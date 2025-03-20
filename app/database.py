from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://db-buddy.caziwauggngu.us-east-1.rds.amazonaws.com:35433/db_buddy"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# DB 세션을 생성하는 함수
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
