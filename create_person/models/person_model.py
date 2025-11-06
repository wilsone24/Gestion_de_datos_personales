from sqlalchemy import Column, Integer, String
from database import Base


class Person(Base):
    __tablename__ = "persons"

    id_person = Column(Integer, primary_key=True, index=True)
    document_type = Column(String(50), nullable=False)
    document_number = Column(String(50), unique=True, nullable=False)
    first_name = Column(String(100), nullable=False)
