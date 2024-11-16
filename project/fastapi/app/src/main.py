from fastapi import FastAPI

from src.consumption import router as consumption

app = FastAPI()

app.include_router(consumption.router)
