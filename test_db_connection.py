# test_db_connection.py

from app.db.session import SessionLocal
from sqlalchemy import text  # ✅ 수정된 부분

def test_db_connection():
    try:
        db = SessionLocal()
        db.execute(text("SELECT 1"))  # ✅ text()로 감싸기
        print("✅ DB 연결 성공!")
    except Exception as e:
        print("❌ DB 연결 실패:", e)
    finally:
        db.close()
        print("🔒 DB 세션 종료")

if __name__ == "__main__":
    test_db_connection()
