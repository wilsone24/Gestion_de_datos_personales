from fastapi import HTTPException
from sqlalchemy import text
from schemas.rag_schema import QuerySchema, UpdateVectorSchema
from utils.rag_functions import (
    query_vector_store,
    generate_answer,
    add_texts_to_vector_store,
    clear_vector_store,
)
from sqlalchemy.orm import Session


def get_response(data: QuerySchema):
    docs = query_vector_store(data.question, k=3)
    if not docs:
        return {"answer": "No encontré información relacionada en la base vectorial."}
    context = "\n\n".join([doc.page_content for doc in docs])
    answer = generate_answer(context, data.question)
    return {"answer": answer, "sources": [doc.metadata for doc in docs]}


def update_vector_store(data: UpdateVectorSchema):
    text_to_embed = f"{data.name}: {data.description}"
    metadata = {"id": data.id, "name": data.name}
    add_texts_to_vector_store([text_to_embed], [metadata])
    return {"message": "Registro agregado al vector store correctamente"}


def ingest_data(db: Session):
    query = text("SELECT * FROM persons")
    rows = db.execute(query).fetchall()
    if not rows:
        raise HTTPException(status_code=404, detail="No hay datos en la tabla persons")
    clear_vector_store()
    texts = []
    metadatas = []
    for row in rows:
        text_to_embed = f"{row.name}: {row.description}"
        meta = {"id": row.id, "name": row.name}
        texts.append(text_to_embed)
        metadatas.append(meta)
    add_texts_to_vector_store(texts, metadatas)
    return {"message": "Vector store actualizado correctamente", "cantidad": len(texts)}
