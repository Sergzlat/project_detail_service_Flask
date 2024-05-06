from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from detail_service.models import Base

# Подключение к базе данных
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:password@localhost:5432/postgres"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Создание таблиц
def create_tables():
    Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    # Инициализация базы данных и создание таблиц
    create_tables()