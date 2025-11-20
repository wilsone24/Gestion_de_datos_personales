from requests import Session
from schemas.rag_schema import QueryRequest
from services import rag_service


def get_response_controller(data: QueryRequest):
    return rag_service.get_response(data)
