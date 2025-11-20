from fastapi import APIRouter
from controllers.rag_controller import get_response_controller
from schemas.rag_schema import QueryRequest

router = APIRouter()


@router.post("/response")
def get_response(data: QueryRequest):
    return get_response_controller(data)
