from schemas.rag_schema import QueryRequest
from utils.rag_functions import generate_response


def get_response(data: QueryRequest):
    return generate_response(data.question)
