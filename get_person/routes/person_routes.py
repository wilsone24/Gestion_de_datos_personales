from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from controllers.person_controller import (
    get_person_controller,
    get_all_persons_controller,
)
from schemas.person_schema import PersonResponse
from utils.auth_dep import get_current_user

router = APIRouter()


@router.get(
    "/getall",
    response_model=list[PersonResponse],
    dependencies=[Depends(get_current_user)],
)
def get_all_persons(db: Session = Depends(get_db)):
    return get_all_persons_controller(db)


@router.get(
    "/get{document_number}",
    response_model=PersonResponse,
    dependencies=[Depends(get_current_user)],
)
def get_person(document_number: str, db: Session = Depends(get_db)):
    return get_person_controller(db, document_number)
