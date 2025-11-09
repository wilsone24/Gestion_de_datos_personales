from sqlalchemy.orm import Session
from schemas.log_schema import LogRequest
from services import log_service


def create_log_controller(db: Session, data: LogRequest):
    return log_service.create_log(db, data)
    