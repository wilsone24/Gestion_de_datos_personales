from sqlalchemy.orm import Session
from schemas.person_schema import PersonRequest
from services import person_service
from fastapi import UploadFile


def update_person_controller(
    db: Session, id_person: int, data: PersonRequest, photo: UploadFile | None
):
    return person_service.update_person(db, id_person, data, photo)
