from pydantic import BaseModel
from datetime import datetime


class LogBase(BaseModel):
    document_type: str
    document_number: str
    log_type: str
    description: str
    log_date: datetime
    log_user: str


class LogRequest(LogBase): ...


class LogResponse(LogBase):
    id_log: int

    class Config:
        from_attributes = True
