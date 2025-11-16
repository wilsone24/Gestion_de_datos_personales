from fastapi import FastAPI
from database import get_db
from services.rag_service import ingest_data
from sqlalchemy.orm import Session
from routes import rag_routes
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    db: Session = next(get_db())
    ingest_data(db)
    yield


app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(rag_routes.router, prefix="/rag", tags=["config"])
