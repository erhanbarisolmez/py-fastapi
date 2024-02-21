from sqlalchemy import create_engine # veritabanı bağlantısı için kullanılan fonksiyon
from sqlalchemy.ext.declarative import declarative_base #ORM tablolarının miras alacağı temel sınıfı sağlar
from sqlalchemy.orm import sessionmaker #veritabanı işlemlerini gerçekleştirmek için kullanılır.

# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/db"

engine = create_engine(
  SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()