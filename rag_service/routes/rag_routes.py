from fastapi import APIRouter
from rags_service.controllers.rag_controller import (
    get_response_controller,
    update_vector_store_controller,
    ingest_data_controller,
)
from schemas.rag_schema import QuerySchema, UpdateVectorSchema

router = APIRouter()


@router.get("/response")
def get_response(data: QuerySchema):
    return get_response_controller(data)


@router.post("/ingest")
def ingest_data(data: UpdateVectorSchema):
    return ingest_data_controller(data)


@router.post("/update")
def update_vector(data: UpdateVectorSchema):
    return update_vector_store_controller(data)
