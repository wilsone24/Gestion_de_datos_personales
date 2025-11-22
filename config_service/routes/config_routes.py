from fastapi import APIRouter, Depends
from controllers.config_controller import (
    get_container_status_controller,
    stop_container_controller,
    start_container_controller,
)
from schemas.config_schema import ConfigRequest
from utils.auth_dep import get_current_user

router = APIRouter()


@router.post("/status", dependencies=[Depends(get_current_user)])
def get_container_status(data: ConfigRequest):
    return get_container_status_controller(data)


@router.post("/stop", dependencies=[Depends(get_current_user)])
def stop_container(data: ConfigRequest):
    return stop_container_controller(data)


@router.post("/start", dependencies=[Depends(get_current_user)])
def start_container(data: ConfigRequest):
    return start_container_controller(data)
