from sqlalchemy import Column, Integer, String, DateTime, Boolean, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from enum import Enum as PyEnum

Base = declarative_base()

class UserType(PyEnum):
    Unknown = 0
    Nextdetail = 1
    DetailL = 2
    Admin = 3

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    user_type = Column(Enum(UserType))
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)
    email = Column(String, nullable=False)

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