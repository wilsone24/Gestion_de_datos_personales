from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from controllers.log_controller import create_log_controller, get_logs_controller
from schemas.log_schema import LogRequest, LogResponse

router = APIRouter()


@router.post("/create", response_model=LogResponse)
def create_log(log: LogRequest, db: Session = Depends(get_db)):
    return create_log_controller(db, log)


@router.get("/getlogs", response_model=list[LogResponse])
def get_logs(document_type: str, document_number: str, db: Session = Depends(get_db)):
    return get_logs_controller(db, document_type, document_number)
