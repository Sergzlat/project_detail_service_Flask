from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
# project_detail_service/detail_service/models/nextdetail_db.py

from .database import Base


Base = declarative_base()

class Nextdetail(Base):
    __tablename__ = 'nextdetails'

    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    middle_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    birth_date = Column(DateTime)
    email = Column(String, nullable=False)
    is_deleted = Column(Boolean, default=False)

class Bolt(Base):
    __tablename__ = 'bolts'

    id = Column(Integer, primary_key=True)
    size = Column(String)  # Размер болта, например "м-4", "м-10" и т.д.
    hex_head = Column(Boolean)  # Шестигранная головка: True или False

class Nut(Base):
    __tablename__ = 'nuts'

    id = Column(Integer, primary_key=True)
    size = Column(String)  # Размер гайки, например "м-4", "м-10" и т.д.
    hex_form = Column(Boolean)  # Шестигранная форма: True или False

# Подключение к базе данных
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:password@localhost:5432/postgres"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Создание таблиц в базе данных
Base.metadata.create_all(bind=engine)