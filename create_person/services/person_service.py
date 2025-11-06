from sqlalchemy.orm import Session
from models.person_model import Person
from schemas.person_schema import PersonRequest
from sqlalchemy.exc import SQLAlchemyError


def create_person(db: Session, data: PersonRequest):
    new_person = Person(
        document_type=data.document_type,
        document_number=data.document_number,
        first_name=data.first_name,
    )
    try:
        db.add(new_person)
        db.commit()
        db.refresh(new_person)
        return new_person
    except SQLAlchemyError as e:
        db.rollback()
        raise e
