from sqlalchemy.orm import Session
from schemas.person_schema import PersonRequest
from services.person_service import update_person
from fastapi import UploadFile


def update_person_controller(
    db: Session, id_person: int, data: PersonRequest, photo: UploadFile | None
):
    return update_person(db, id_person, data, photo)
