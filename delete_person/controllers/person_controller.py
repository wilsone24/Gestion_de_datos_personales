from sqlalchemy.orm import Session
from services import person_service


def delete_person_controller(db: Session, data: int):
    return person_service.delete_person(db, data)
