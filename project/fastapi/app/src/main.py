from fastapi import FastAPI

from src.consumption import router as consumption
from src.consumption.grpc_client import GRPCClient

app = FastAPI()

app.include_router(consumption.router)

@app.on_event("shutdown")
async def shutdown_event():
    client = GRPCClient()
    await client.close()
