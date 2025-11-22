import requests
from fastapi import HTTPException
import os
from dotenv import load_dotenv

load_dotenv()

AUTH_URL = os.getenv("AUTH_URL")


def get_current_user(token: str):
    response = requests.get(f"{AUTH_URL}?token={token}")

    if response.status_code != 200:
        raise HTTPException(status_code=401, detail="Token inválido")

    return response.json()
