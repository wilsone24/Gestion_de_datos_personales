from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from controllers.person_controller import (
    get_person_controller,
    get_allp_persons_controller,
)
from schemas.person_schema import PersonResponse

router = APIRouter()


@router.get("/getall", response_model=list[PersonResponse])
def get_all_persons(db: Session = Depends(get_db)):
    return get_allp_persons_controller(db)


@router.get("/get{document_number}", response_model=PersonResponse)
def get_person(document_number: str, db: Session = Depends(get_db)):
    return get_person_controller(db, document_number)
