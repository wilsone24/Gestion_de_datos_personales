from fastapi import APIRouter, Depends
from controllers.rag_controller import (
    get_response_controller,
    update_vector_store_controller,
    ingest_data_controller,
)
from schemas.rag_schema import QuerySchema
from schemas.person_schema import PersonResponse
from database import get_db
from sqlalchemy.orm import Session

router = APIRouter()


@router.post("/response")
def get_response(data: QuerySchema):
    return get_response_controller(data)


@router.post("/ingest")
def ingest_data(db: Session = Depends(get_db)):
    return ingest_data_controller(db)


@router.post("/update")
def update_vector(data: PersonResponse):
    return update_vector_store_controller(data)
