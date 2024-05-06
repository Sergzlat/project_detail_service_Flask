import sys
import os

# Добавить путь к корневой директории вашего проекта в sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask, request, jsonify
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import Base
from sqlalchemy import DateTime
from sqlalchemy import Column, Integer, String, Boolean

Base.metadata.create_all(bind=engine)

app = Flask(__name__)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.route("/")
def index():
    return "PROJECT_DETAIL_SERVICE_FLASK"

class Bolt(Base):
    __tablename__ = 'bolts'
    __table_args__ = {'extend_existing': True}  # Добавьте эту строку

    id = Column(Integer, primary_key=True)
    size = Column(String)  # Размер болта, например "м-4", "м-10" и т.д.
    hex_head = Column(Boolean)  # Шестигранная головка: True или False


class Hut(Base):
    __tablename__ = 'nut'
    __table_args__ = {'extend_existing': True}  # Добавьте эту строку

    id = Column(Integer, primary_key=True)
    size = Column(String)  # Размер болта, например "м-4", "м-10" и т.д.
    hex_head = Column(Boolean)  # Шестигранная головка: True или False


class DetailL(Base):
    __tablename__ = 'detail_ls'
    __table_args__ = {'extend_existing': True}  # Добавьте эту строку

    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    middle_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    birth_date = Column(DateTime)
    email = Column(String, nullable=False)
    is_deleted = Column(Boolean, default=False)

@app.route("/token", methods=["POST"])
def login():
    # Обработка запроса на аутентификацию и выдачу токена доступа
    pass

@app.route("/nextdetails/", methods=["GET"])
def get_nextdetails():
    # Получение списка следующих деталей
    pass

@app.route("/nextdetails/<int:nextdetail_id>", methods=["GET"])
def get_nextdetail(nextdetail_id):
    # Получение информации о конкретном следующем детале
    pass

@app.route("/nextdetails/", methods=["POST"])
def create_nextdetail():
    # Создание нового следующего деталя
    pass

@app.route("/nextdetails/<int:nextdetail_id>", methods=["PUT"])
def update_nextdetail(nextdetail_id):
    # Обновление информации о следующем детале
    pass

@app.route("/nextdetails/<int:nextdetail_id>", methods=["DELETE"])
def delete_nextdetail(nextdetail_id):
    # Удаление следующего детале
    pass

if __name__ == "__main__":
    app.run(host="localhost", port=8000)