from sqlalchemy import Column, Integer, String, DateTime
from database import Base


class Log(Base):
    __tablename__ = "logs"

    id_log = Column(Integer, primary_key=True, index=True, autoincrement=True)
    document_type = Column(String(30), nullable=False)
    document_number = Column(String(10), nullable=False)
    log_type = Column(String(50), nullable=False)
    description = Column(String(255), nullable=False)
    log_date = Column(DateTime, nullable=False)