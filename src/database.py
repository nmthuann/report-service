from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
# from databases import Database
from dotenv import load_dotenv
import os

# Load biến môi trường từ file .env
load_dotenv()

# Lấy giá trị của các biến môi trường
DATABASE_URL = os.getenv("DATABASE_URL")
DATABASE_NAME = os.getenv("DATABASE_NAME")
DATABASE_USERNAME = os.getenv("DATABASE_USERNAME")
DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")
SQL_TYPE = os.getenv("SQL_TYPE")

# # Kết nối đến SQL Server
# DATABASE_URL = f"mssql+pyodbc://{DATABASE_USERNAME}:{DATABASE_PASSWORD}@{DATABASE_URL}/{DATABASE_NAME}"
# database = Database(DATABASE_URL)


# Thay đổi đường dẫn kết nối để sử dụng SQL Server
# SQLALCHEMY_DATABASE_URL = f"{SQL_TYPE}+pyodbc://{DATABASE_USERNAME}:{DATABASE_PASSWORD}@{DATABASE_URL}/{DATABASE_NAME}"
# SQLALCHEMY_DATABASE_URL ='mssql+pyodbc://SA:123456@driver=ODBC+Driver+17+for+SQL+Server;server=localhost;port=1433;database=TTTN_DongHoOnline'
SQLALCHEMY_DATABASE_URL = "mssql+pyodbc://SA:123456@localhost:1433/TTTN_DongHoOnline?driver=ODBC+Driver+17+for+SQL+Server"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()