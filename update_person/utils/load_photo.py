import uuid
import os
from fastapi import UploadFile, HTTPException
from dotenv import load_dotenv

load_dotenv()

MAX_IMAGE_SIZE = 2 * 1024 * 1024
ALLOWED_TYPES = ["image/jpeg", "image/png"]

UPLOAD_DIR = os.getenv("UPLOAD_DIR")
os.makedirs(UPLOAD_DIR, exist_ok=True)


def process_photo(photo: UploadFile):
    if photo is None:
        return None

    if photo.content_type not in ALLOWED_TYPES:
        raise HTTPException(
            status_code=400, detail="Formato de imagen inválido (solo jpeg, png)."
        )
    content = photo.file.read()
    if len(content) > MAX_IMAGE_SIZE:
        raise HTTPException(status_code=400, detail="La imagen supera los 2 MB.")
    extension = photo.filename.split(".")[-1]
    filename = f"{uuid.uuid4()}.{extension}"
    file_path = os.path.join(UPLOAD_DIR, filename)

    with open(file_path, "wb") as f:
        f.write(content)
    photo_url = f"/static/users/{filename}"

    return photo_url


def remove_photo(photo_url: str | None):
    if not photo_url:
        return
    try:
        filename = photo_url.split("/")[-1]
        file_path = os.path.join(UPLOAD_DIR, filename)
        if os.path.exists(file_path):
            os.remove(file_path)
    except Exception:
        pass
