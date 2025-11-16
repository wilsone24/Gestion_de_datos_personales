from pydantic import BaseModel


class UpdateVectorSchema(BaseModel):
    id: int
    name: str
    description: str


class QuerySchema(BaseModel):
    question: str
