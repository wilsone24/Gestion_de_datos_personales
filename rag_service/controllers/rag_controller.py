from requests import Session
from schemas.rag_schema import QuerySchema
from schemas.person_schema import PersonResponse
from services import rag_service


def get_response_controller(data: QuerySchema):
    return rag_service.get_response(data)


def update_vector_store_controller(data: PersonResponse):
    return rag_service.update_vector_store(data)


def ingest_data_controller(db: Session):
    return rag_service.ingest_data(db)
