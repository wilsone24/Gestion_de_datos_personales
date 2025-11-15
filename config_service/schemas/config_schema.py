from pydantic import BaseModel


class ConfigBase(BaseModel):
    containername: str


class ConfigRequest(ConfigBase): ...
