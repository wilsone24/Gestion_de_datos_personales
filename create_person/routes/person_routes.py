from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from controllers.person_controller import create_person_controller
from schemas.person_schema import PersonRequest, PersonResponse
from utils.auth_dep import get_current_user

router = APIRouter()


@router.post(
    "/create", response_model=PersonResponse, dependencies=[Depends(get_current_user)]
)
def create_person(data: PersonRequest, db: Session = Depends(get_db)):
    return create_person_controller(db, data)
