from sqlalchemy.orm import Session
from schemas.person_schema import PersonRequest
from services import person_service
from fastapi import UploadFile


def create_person_controller(
    db: Session, data: PersonRequest, photo: UploadFile | None
):
    return person_service.create_person(db, data, photo)
