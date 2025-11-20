import requests
from datetime import datetime, timezone, timedelta
import os

LOGS_SERVICE_URL = os.getenv("LOGS_SERVICE_URL")

def send_log(log_type: str, description: str, document_type="N/A", document_number="N/A", user="system"):
    log_data = {
        "document_type": document_type,
        "document_number": document_number,
        "log_type": log_type,
        "description": description,
        "log_date": (datetime.now(timezone.utc) - timedelta(hours=5)).isoformat(),
        "log_user": user,
    }

    print(f"[INFO] Enviando log: {log_data}")

    try:
        response = requests.post(LOGS_SERVICE_URL, json=log_data, timeout=5)
        response.raise_for_status()
        print(f"[INFO] Log registrado correctamente: {response.status_code}")
    except requests.RequestException as e:
        print(f"[WARN] No se pudo registrar el log: {e}")