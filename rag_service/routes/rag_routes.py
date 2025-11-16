from fastapi import APIRouter
from controllers.rag_controller import (
    get_response_controller,
    update_vector_store_controller,
)
from schemas.rag_schema import QuerySchema
from schemas.person_schema import PersonResponse

router = APIRouter()


@router.post("/response")
def get_response(data: QuerySchema):
    return get_response_controller(data)


@router.post("/update")
def update_vector(data: PersonResponse):
    return update_vector_store_controller(data)
