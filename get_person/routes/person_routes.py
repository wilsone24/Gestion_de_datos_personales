from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from controllers.person_controller import get_person_controller
from schemas.person_schema import PersonRequest, PersonResponse

router = APIRouter()


@router.get("/get{document_number}", response_model=PersonResponse)
def get_person(document_number: str, db: Session = Depends(get_db)):
    return get_person_controller(db, document_number)
