from pydantic import BaseModel, EmailStr
from datetime import date


class PersonBase(BaseModel):
    document_type: str
    document_number: str
    first_name: str
    second_name: str | None = None
    last_name: str
    birth_date: date
    gender: str
    email: EmailStr
    phone_number: str
    photo_url: str | None = None


class PersonRequest(PersonBase): ...


class PersonResponse(PersonBase):
    id_person: int

    class Config:
        from_attributes = True
