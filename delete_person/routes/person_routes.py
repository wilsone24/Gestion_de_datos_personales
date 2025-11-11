from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from controllers.person_controller import delete_person_controller

router = APIRouter()


@router.delete("/delete/{id_person}")
def delete_person(person_id: int, db: Session = Depends(get_db)):
    return delete_person_controller(db, person_id)
