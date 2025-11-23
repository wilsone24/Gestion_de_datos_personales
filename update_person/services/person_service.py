import datetime
import requests
import os
from sqlalchemy.orm import Session
from models.person_model import Person
from schemas.person_schema import PersonRequest
from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException, status
from utils.validate import validate_person_data
from datetime import timedelta, datetime, timezone

LOGS_SERVICE_URL = os.getenv(
    "LOGS_SERVICE_URL",
)


def _validate_update(data: PersonRequest):
    try:
        validate_person_data(data.dict(exclude_unset=True))
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=[{"msg": str(e)}],
        )


def _check_uniqueness(db: Session, data: PersonRequest, person: Person):
    if data.document_number and data.document_number != person.document_number:
        other = (
            db.query(Person)
            .filter(Person.document_number == data.document_number)
            .first()
        )
        if other:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Ya existe otra persona con ese número de documento.",
            )

    if data.email and data.email != person.email:
        other = db.query(Person).filter(Person.email == data.email).first()
        if other:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Ya existe otra persona con ese correo electrónico.",
            )


def _send_update_log(person: Person):
    log_data = {
        "document_type": person.document_type,
        "document_number": person.document_number,
        "log_type": "Update Person",
        "description": f"Se actualizó la persona: {person.first_name} {person.last_name}",
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


def update_person(db: Session, id_person: int, data: PersonRequest):
    _validate_update(data)

    person = db.query(Person).filter(Person.id_person == id_person).first()
    if not person:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Persona no encontrada."
        )
    _check_uniqueness(db, data, person)
    update_fields = data.dict(exclude_unset=True)
    for key, value in update_fields.items():
        setattr(person, key, value)

    try:
        db.add(person)
        db.commit()
        db.refresh(person)
        _send_update_log(person)
        return person

    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al actualizar la persona: {str(e)}",
        )
