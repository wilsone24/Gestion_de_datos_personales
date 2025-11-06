from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from controllers.person_controller import create_person_controller
from schemas.person_schema import PersonRequest, PersonResponse

router = APIRouter()


@router.post("/create", response_model=PersonResponse)
def create_person(person: PersonRequest, db: Session = Depends(get_db)):
    return create_person_controller(db, person)
