from pydantic import BaseModel
class QuerySchema(BaseModel):
    question: str
