from sqlalchemy.orm import Session
from schemas.log_schema import LogRequest
from services import log_service


def create_log_controller(db: Session, data: LogRequest):
    return log_service.create_log(db, data)


def get_logs_controller(db: Session, document_type: str, document_number: str):
    return log_service.get_logs(db, document_type, document_number)
