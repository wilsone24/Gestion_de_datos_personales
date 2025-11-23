from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from controllers.person_controller import update_person_controller
from schemas.person_schema import PersonRequest, PersonResponse
from utils.auth_dep import get_current_user

router = APIRouter()


@router.put(
    "/{id_person}",
    response_model=PersonResponse,
    dependencies=[Depends(get_current_user)],
)
def update_person(id_person: int, data: PersonRequest, db: Session = Depends(get_db)):
    return update_person_controller(db, id_person, data)
