import os
from pydantic_settings import BaseSettings

class Config(BaseSettings):
    GRPC_ADDRESS: str = os.getenv("GRPC_URL", "localhost:50051")

settings = Config()