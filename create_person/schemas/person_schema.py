from pydantic import BaseModel


class PersonBase(BaseModel):
    document_type: str
    document_number: int
    first_name: str


class PersonRequest(PersonBase):
    pass


class PersonResponse(PersonBase):
    id_person: int

    class Config:
        from_attributes = True
