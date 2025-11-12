from sqlalchemy.orm import Session
from services import person_service


def get_person_controller(db: Session, data: str):
    return person_service.get_person(db, data)


def get_all_persons_controller(db: Session):
    return person_service.get_all_persons(db)
