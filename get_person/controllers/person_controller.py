from sqlalchemy.orm import Session
from services import person_service


def get_person_controller(db: Session, data: str):
    return person_service.get_person(db, data)
