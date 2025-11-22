from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from controllers.person_controller import delete_person_controller
from utils.auth_dep import get_current_user

router = APIRouter()


@router.delete("/delete/{person_id}", dependencies=[Depends(get_current_user)])
def delete_person(person_id: int, db: Session = Depends(get_db)):
    return delete_person_controller(db, person_id)
