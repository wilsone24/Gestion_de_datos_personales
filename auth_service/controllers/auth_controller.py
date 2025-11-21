from schemas.login_schema import LoginRequest
from services.auth_service import login_service, verify_token_service, logout_service


def login_controller(data: LoginRequest):
    return login_service(data)


def verify_token_controller(token: str):
    return verify_token_service(token)


def logout_controller(token: str):
    return logout_service(token)
