from pydantic_settings import BaseSettings


class Config(BaseSettings):
    GRPC_ADDRESS: str = "grpc_server:50051"

settings = Config()