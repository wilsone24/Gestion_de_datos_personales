from sqlalchemy.orm import Session
from models.log_model import Log
from schemas.log_schema import LogRequest
from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException, status


def create_log(db: Session, data: LogRequest):
    new_log = Log(
        document_type=data.document_type,
        document_number=data.document_number,
        log_type=data.log_type,
        description=data.description,
        log_date=data.log_date,
    )

    try:
        db.add(new_log)
        db.commit()
        db.refresh(new_log)
        return new_log
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al guardar el log: {str(e)}",
        )
