from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from controllers.log_controller import create_log_controller
from schemas.log_schema import LogRequest, LogResponse

router = APIRouter()


@router.post("/create", response_model=LogResponse)
def create_log(log: LogRequest, db: Session = Depends(get_db)):
    return create_log_controller(db, log)
