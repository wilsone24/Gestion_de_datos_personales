from fastapi import APIRouter
from controllers.config_controller import (
    get_container_status_controller,
    stop_container_controller,
    start_container_controller,
)
from schemas.config_schema import ConfigRequest

router = APIRouter()


@router.post("/status")
def get_container_status(data: ConfigRequest):
    return get_container_status_controller(data)


@router.post("/stop")
def stop_container(data: ConfigRequest):
    return stop_container_controller(data)


@router.post("/start")
def start_container(data: ConfigRequest):
    return start_container_controller(data)
