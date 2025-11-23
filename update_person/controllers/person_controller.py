from sqlalchemy.orm import Session
from schemas.person_schema import PersonRequest
from services.person_service import update_person


def update_person_controller(db: Session, id_person: int, data: PersonRequest):
    return update_person(db, id_person, data)
