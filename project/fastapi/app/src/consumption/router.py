from fastapi import Depends, HTTPException, APIRouter
from ..consumption import dependencies, schemas
from ..config import settings

from datetime import datetime


router = APIRouter()

@router.get("/get_consumptions")
async def get_consumptions(start_time: datetime, end_time: datetime) -> schemas.get_consumptions_res:

        res = []
        for dp in range(5):
            res.append(
                schemas.data_point(
                    time=datetime.utcfromtimestamp(1731246688),
                    value=2.5
                )
            )

        return schemas.get_consumptions_res(data_points=res)