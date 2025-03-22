# app/config.py

import os
from dotenv import load_dotenv

# 기본적으로 .env 로드, 환경에 따라 다른 파일도 가능
env_file = os.getenv("ENV_FILE", ".env")
load_dotenv(dotenv_path=env_file)

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"