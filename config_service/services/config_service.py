from schemas.config_schema import ConfigRequest
from fastapi import HTTPException, status
import docker


client = docker.from_env()


def get_container_status(data: ConfigRequest):
    try:
        container = client.containers.get(data.containername)
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
        return {"container_name": data.containername, "status": "running"}
    except docker.errors.NotFound:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Container '{data.containername}' not found.",
        )
