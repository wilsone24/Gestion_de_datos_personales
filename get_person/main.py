from fastapi import FastAPI
from routes import (
    person_routes,
)
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(person_routes.router, prefix="/getpersons", tags=["persons"])
