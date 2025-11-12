import datetime
import requests
import os
from sqlalchemy.orm import Session
from models.person_model import Person
from fastapi import HTTPException, status

LOGS_SERVICE_URL = os.getenv(
    "LOGS_SERVICE_URL",
)


def get_person(db: Session, document_number: str):
    person = db.query(Person).filter(Person.document_number == document_number).first()

    if not person:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No existe una persona registrada con ese número de documento.",
        )

    log_data = {
        "document_type": person.document_type,
        "document_number": person.document_number,
        "log_type": "Get Person",
        "description": f"Se consultó una persona: {person.first_name} {person.last_name}",
        "log_date": datetime.datetime.now(datetime.timezone.utc).isoformat(),
    }

    try:
        response = requests.post(LOGS_SERVICE_URL, json=log_data, timeout=5)
        response.raise_for_status()
        print(f"[INFO] Log registrado: {response.status_code}")
    except requests.RequestException as e:
        print(f"[WARN] No se pudo registrar el log: {e}")

    return person


def get_all_persons(db: Session):
    persons = db.query(Person).all()

    if not persons:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No existen personas registradas en el sistema.",
        )

    log_data = {
        "document_type": "ALL",
        "document_number": "ALL",
        "log_type": "Get All Persons",
        "description": f"Se consultaron todas las personas registradas. Total: {len(persons)}",
        "log_date": datetime.datetime.now(datetime.timezone.utc).isoformat(),
    }

    try:
        response = requests.post(LOGS_SERVICE_URL, json=log_data, timeout=5)
        response.raise_for_status()
        print(f"[INFO] Log registrado: {response.status_code}")
    except requests.RequestException as e:
        print(f"[WARN] No se pudo registrar el log: {e}")

    return persons
