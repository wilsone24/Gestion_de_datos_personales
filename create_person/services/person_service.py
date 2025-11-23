import datetime
import requests
import os
from sqlalchemy.orm import Session
from models.person_model import Person
from schemas.person_schema import PersonRequest
from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException, status, UploadFile
from utils.validate import validate_person_data
from datetime import timedelta, datetime, timezone

LOGS_SERVICE_URL = os.getenv(
    "LOGS_SERVICE_URL",
)


def create_person(db: Session, data: PersonRequest):
    try:
        validate_person_data(data.dict())
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=[{"msg": str(e)}],
        )

    existing_person = (
        db.query(Person).filter(Person.document_number == data.document_number).first()
    )

    if existing_person:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Ya existe una persona registrada con ese número de documento.",
        )

    existing_email = db.query(Person).filter(Person.email == data.email).first()
    if existing_email:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Ya existe una persona registrada con ese correo electrónico.",
        )

    new_person = Person(
        document_type=data.document_type,
        document_number=data.document_number,
        first_name=data.first_name,
        second_name=data.second_name,
        last_name=data.last_name,
        birth_date=data.birth_date,
        gender=data.gender,
        email=data.email,
        phone_number=data.phone_number,
        photo_url="photo_url",
    )

    try:
        db.add(new_person)
        db.commit()
        db.refresh(new_person)

        log_data = {
            "document_type": new_person.document_type,
            "document_number": new_person.document_number,
            "log_type": "Create Person",
            "description": f"Se creó una nueva persona: {new_person.first_name} {new_person.last_name}",
            "log_date": (datetime.now(timezone.utc) - timedelta(hours=5)).isoformat(),
            "log_user": "system",
        }
        print(f"[INFO] Enviando log: {log_data}")
        try:
            response = requests.post(LOGS_SERVICE_URL, json=log_data, timeout=5)
            response.raise_for_status()
            print(f"[INFO] Log registrado: {response.status_code}")
        except requests.RequestException as e:
            print(f"[WARN] No se pudo registrar el log: {e}")

        return new_person

    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al guardar la persona: {str(e)}",
        )