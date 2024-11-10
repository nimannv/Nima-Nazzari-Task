from typing import Union

from fastapi import FastAPI

from .consumption import router as consumption

app = FastAPI()

app.include_router(consumption.router)
