from fastapi import HTTPException
from schemas.rag_schema import QuerySchema
from schemas.person_schema import PersonResponse
from utils.rag_functions import (
    query_vector_store,
    generate_answer,
    add_texts_to_vector_store,
    clear_vector_store,
)
from sqlalchemy.orm import Session
from models.person_model import Person


def get_response(data: QuerySchema):
    docs = query_vector_store(data.question, k=3)
    if not docs:
        return {"answer": "No encontré información relacionada en la base vectorial."}
    context = "\n\n".join([doc.page_content for doc in docs])
    answer = generate_answer(context, data.question)
    return {"answer": answer, "sources": [doc.metadata for doc in docs]}


def update_vector_store(data: PersonResponse):
    text_to_embed = (
        f"id_person (int): {data.id_person}\n"
        f"document_type (str): {data.document_type}\n"
        f"document_number (str): {data.document_number}\n"
        f"first_name (str): {data.first_name}\n"
        f"second_name (str|None): {data.second_name}\n"
        f"last_name (str): {data.last_name}\n"
        f"birth_date (date): {data.birth_date}\n"
        f"gender (str): {data.gender}\n"
        f"email (EmailStr): {data.email}\n"
        f"phone_number (str): {data.phone_number}\n"
        f"photo_url (str|None): {data.photo_url}"
    )
    metadata = {
        "id_person": data.id_person,
        "full_name": f"{data.first_name} {data.second_name or ''} {data.last_name}".strip(),
        "document_type": data.document_type,
        "document_number": data.document_number,
    }
    add_texts_to_vector_store([text_to_embed], [metadata])
    return {"message": "Registro agregado al vector store correctamente"}


def ingest_data(db: Session):
    rows = db.query(Person).all()
    if not rows:
        raise HTTPException(status_code=404, detail="No hay datos en la tabla persons")

    clear_vector_store()

    all_text = ""
    for row in rows:
        all_text += (
            f"id_person (int): {row.id_person}\n"
            f"document_type (str): {row.document_type}\n"
            f"document_number (str): {row.document_number}\n"
            f"first_name (str): {row.first_name}\n"
            f"second_name (str|None): {row.second_name}\n"
            f"last_name (str): {row.last_name}\n"
            f"birth_date (date): {row.birth_date}\n"
            f"gender (str): {row.gender}\n"
            f"email (str): {row.email}\n"
            f"phone_number (str): {row.phone_number}\n"
            f"photo_url (str|None): {row.photo_url}\n"
            "----------------------------------------\n"
        )

    # Metadata general del documento
    metadata = {
        "total_persons": len(rows),
        "description": "Información de todos los usuarios concatenada en un solo documento",
    }

    add_texts_to_vector_store([all_text], [metadata])

    return {
        "message": "Vector store actualizado correctamente con un solo documento",
        "cantidad": len(rows),
    }
