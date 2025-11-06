from sqlalchemy.orm import Session
from schemas.person_schema import PersonRequest
from services import person_service


def create_person_controller(db: Session, data: PersonRequest):
    return person_service.create_person(db, data)
