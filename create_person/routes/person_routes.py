from fastapi import APIRouter, Depends, Form
from sqlalchemy.orm import Session
from database import get_db
from controllers.person_controller import create_person_controller
from schemas.person_schema import PersonRequest, PersonResponse
from fastapi import File, UploadFile
from utils.auth_dep import get_current_user

router = APIRouter()


@router.post(
    "/create", response_model=PersonResponse, dependencies=[Depends(get_current_user)]
)
async def create_person(
    document_type: str = Form(...),
    document_number: str = Form(...),
    first_name: str = Form(...),
    second_name: str = Form(None),
    last_name: str = Form(...),
    birth_date: str = Form(...),
    gender: str = Form(...),
    email: str = Form(...),
    phone_number: str = Form(...),
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

    return create_person_controller(db, data, photo)
