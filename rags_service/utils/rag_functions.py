import os
from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings, ChatOpenAI

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
VECTOR_DB_PATH = os.getenv("VECTOR_DB_PATH")

embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
llm = ChatOpenAI(model="gpt-4o-mini")


def get_vector_store():
    return Chroma(embedding_function=embeddings, persist_directory=VECTOR_DB_PATH)


def clear_vector_store():
    store = get_vector_store()
    store.delete_all()
    store.persist()


def add_texts_to_vector_store(texts, metadatas):
    store = get_vector_store()
    store.add_texts(texts=texts, metadatas=metadatas)
    store.persist()


def query_vector_store(question, k=3):
    store = get_vector_store()
    retriever = store.as_retriever(search_kwargs={"k": k})
    return retriever.invoke(question)


def generate_answer(context, question):
    prompt = f"""
    Eres un asistente experto. Responde usando únicamente el siguiente contexto.

    === CONTEXTO ===
    {context}

    === PREGUNTA ===
    {question}

    Si la respuesta no está en el contexto, di: "No tengo información suficiente".
    """
    response = llm.invoke(prompt)
    return response.content
