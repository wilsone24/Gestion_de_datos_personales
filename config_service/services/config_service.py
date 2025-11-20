from schemas.config_schema import ConfigRequest
from fastapi import HTTPException, status
import docker
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
from utils.log_helper import send_log

client = docker.from_env()


def get_container_status(data: ConfigRequest):
    try:
        container = client.containers.get(data.containername)
        send_log(
            log_type="View Container Status",
            description=f"Se consultó el status del contenedor '{data.containername}'",
        )

        return {"container_name": data.containername, "status": container.status}

    except docker.errors.NotFound:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Container '{data.containername}' not found.",
        )


def stop_container(data: ConfigRequest):
    try:
        container = client.containers.get(data.containername)
        container.stop()

        send_log(
            log_type="Stop Container",
            description=f"Se detuvo el contenedor '{data.containername}'",
        )

        return {"container_name": data.containername, "status": "stopped"}

    except docker.errors.NotFound:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Container '{data.containername}' not found.",
        )


def start_container(data: ConfigRequest):
    try:
        container = client.containers.get(data.containername)
        container.start()

        send_log(
            log_type="Start Container",
            description=f"Se inició el contenedor '{data.containername}'",
        )

        return {"container_name": data.containername, "status": "running"}

    except docker.errors.NotFound:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Container '{data.containername}' not found.",
        )
