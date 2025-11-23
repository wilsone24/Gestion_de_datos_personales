from fastapi import APIRouter, Depends, Form
from sqlalchemy.orm import Session
from database import get_db
from controllers.person_controller import update_person_controller
from schemas.person_schema import PersonRequest, PersonResponse
from fastapi import File, UploadFile
from utils.auth_dep import get_current_user

router = APIRouter()


@router.put("/{id_person}", response_model=PersonResponse, dependencies=[Depends(get_current_user)])
async def update_person(
    id_person: int,
    document_type: str | None = Form(None),
    document_number: str | None = Form(None),
    first_name: str | None = Form(None),
    second_name: str | None = Form(None),
    last_name: str | None = Form(None),
    birth_date: str | None = Form(None),
    gender: str | None = Form(None),
    email: str | None = Form(None),
    phone_number: str | None = Form(None),
    photo: UploadFile = File(None),
    db: Session = Depends(get_db),
):
    data = PersonRequest(
        document_type=document_type,
        document_number=document_number,
        first_name=first_name,
        second_name=second_name,
        last_name=last_name,
        birth_date=birth_date,
        gender=gender,
        email=email,
        phone_number=phone_number,
    )

    return update_person_controller(db, id_person, data, photo)
