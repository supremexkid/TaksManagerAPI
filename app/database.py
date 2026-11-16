# Engine: Объект, который знает, где лежит файл базы данных, и умеет с ним соединяться.
# SessionLocal: «Разговор» с базой данных. Каждый HTTP-запрос будет открывать свою сессию, делать запросы и закрывать её.
# Base: Класс, от которого будут наследоваться все ваши таблицы (модели). Это нужно, чтобы SQLAlchemy знал, какие таблицы ему нужно создать.
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import DeclarativeBase


engine = create_engine("sqlite:///database.db")

SessionLocal = sessionmaker(bind=engine, expire_on_commit=True)

class Base(DeclarativeBase):
    pass

def get_db():
    db = SessionLocal() # 1. Создаем сессию при поступлении запроса
    try:
        yield db         # 2. "Отдаем" сессию в эндпоинт для работы
    finally:
        db.close()      # 3. Гарантированно закрываем сессию ПОСЛЕ ответа

