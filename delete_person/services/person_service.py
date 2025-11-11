import datetime
import requests
import os
from sqlalchemy.orm import Session
from models.person_model import Person
from fastapi import HTTPException, status
from sqlalchemy.exc import SQLAlchemyError

LOGS_SERVICE_URL = os.getenv("LOGS_SERVICE_URL")


def delete_person(df: Session, id_person: int):
    person = df.query(Person).filter(Person.id_person == id_person).first()
    if not person:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Persona no encontrada.",
        )

    try:
        df.delete(person)
        df.commit()

        log_data = {
            "document_type": person.document_type,
            "document_number": person.document_number,
            "log_type": "Delete Person",
            "description": f"Se eliminó una persona: {person.first_name} {person.last_name}",
            "log_date": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        }

        if LOGS_SERVICE_URL:
            try:
                response = requests.post(LOGS_SERVICE_URL, json=log_data, timeout=5)
                response.raise_for_status()
                print(f"[INFO] Log registrado: {response.status_code}")
            except requests.RequestException as e:
                print(f"[WARN] No se pudo registrar el log en {LOGS_SERVICE_URL}: {e}")
        else:
            print("[WARN] LOGS_SERVICE_URL no está configurada. No se enviará el log.")

        return {"detail": "Persona eliminada exitosamente."}

    except SQLAlchemyError as e:
        df.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al eliminar la persona: {str(e)}",
        )
