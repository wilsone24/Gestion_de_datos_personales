from fastapi import APIRouter, HTTPException
from controllers.auth_controller import (
    login_controller,
    verify_token_controller,
    logout_controller,
)
from schemas.login_schema import LoginRequest

router = APIRouter()


@router.post("/login")
def login(data: LoginRequest):
    try:
        return login_controller(data)
    except Exception as e:
        raise HTTPException(status_code=401, detail=str(e))


@router.get("/verify-token")
def verify_token(token: str):
    token = token.replace("Bearer ", "")
    return verify_token_controller(token)


@router.post("/logout")
def logout(token: str):
    token = token.replace("Bearer ", "")
    return logout_controller(token)
