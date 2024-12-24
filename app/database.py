import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# URL подключения к бд
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:pwd123@db/tasks")

# Создание движка
engine = create_engine(DATABASE_URL, echo=True)

# Сессия для работы с базой данных
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Функция для получения сессии
def get_db():
    db = SessionLocal()
    try:
        # Создаем таблицы, если они еще не созданы
        Base.metadata.create_all(bind=engine)

        yield db
    finally:
        db.close()
