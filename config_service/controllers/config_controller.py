from schemas.config_schema import ConfigRequest
from services import config_service


def get_container_status_controller(data: ConfigRequest):
    return config_service.get_container_status(data)


def stop_container_controller(data: ConfigRequest):
    return config_service.stop_container(data)


def start_container_controller(data: ConfigRequest):
    return config_service.start_container(data)
