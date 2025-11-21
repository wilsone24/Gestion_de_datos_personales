import requests
from schemas.login_schema import LoginRequest
import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL")


def login_service(data: LoginRequest):
    url = f"{BASE_URL}/login"
    body = {"email": data.email, "password": data.password}
    response = requests.post(url, json=body)
    response.raise_for_status()
    return response.json()


def verify_token_service(token: str):
    url = f"{BASE_URL}/verify-token"
    headers = {"Authorization": f"Bearer {token}"}

    res = requests.get(url, headers=headers)
    res.raise_for_status()
    return res.json()


def logout_service(token: str):
    url = f"{BASE_URL}/logout"
    headers = {"Authorization": f"Bearer {token}"}
    res = requests.post(url, headers=headers)
    res.raise_for_status()
    return res.json()
