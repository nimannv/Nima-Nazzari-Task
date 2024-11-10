# src.config
from pydantic_settings import BaseSettings


class Config(BaseSettings):
    GRPC_ADDRESS: str = ""

settings = Config()