from sqlalchemy import Column, Integer, String, Date
from database import Base


class Person(Base):
    __tablename__ = "persons"

    id_person = Column(Integer, primary_key=True, index=True, autoincrement=True)
    document_type = Column(String(30), nullable=False)
    document_number = Column(String(10), unique=True, nullable=False)
    first_name = Column(String(30), nullable=False)
    second_name = Column(String(30), nullable=True)
    last_name = Column(String(60), nullable=False)
    birth_date = Column(Date, nullable=False)
    gender = Column(String(25), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    phone_number = Column(String(10), nullable=False)
    photo_url = Column(String(255), nullable=True)
