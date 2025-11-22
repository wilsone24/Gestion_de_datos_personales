from fastapi import HTTPException
from services.auth_service import verify_token_service


def get_current_user(auth: str):
    token = auth.replace("Bearer ", "")
    try:
        verify_token_service(token)
        return token
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid token")
