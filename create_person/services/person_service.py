from sqlalchemy.orm import Session
from models.person_model import Person
from schemas.person_schema import PersonRequest
from sqlalchemy.exc import SQLAlchemyError
from fastapi import HTTPException, status
from utils.validate import validate_person_data


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
        photo_url=data.photo_url,
    )

    try:
        db.add(new_person)
        db.commit()
        db.refresh(new_person)
        return new_person
    except SQLAlchemyError as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error al guardar la persona: {str(e)}",
        )
