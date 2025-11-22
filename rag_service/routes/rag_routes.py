from fastapi import APIRouter, Depends
from controllers.rag_controller import get_response_controller
from schemas.rag_schema import QueryRequest
from utils.auth_dep import get_current_user

router = APIRouter()


@router.post("/response", dependencies=[Depends(get_current_user)])
def get_response(data: QueryRequest):
    return get_response_controller(data)
