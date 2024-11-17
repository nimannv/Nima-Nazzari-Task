from fastapi import Depends
from src.consumption.grpc_client import GRPCClient

async def get_grpc_client() -> GRPCClient:
    client = GRPCClient()
    return client