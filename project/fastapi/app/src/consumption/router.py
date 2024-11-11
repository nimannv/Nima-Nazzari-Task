from fastapi import Depends, HTTPException, APIRouter
from ..consumption import dependencies, schemas, service

from datetime import datetime

router = APIRouter()

@router.get("/get_consumptions")
async def get_consumptions(start_time: datetime, end_time: datetime) -> schemas.get_consumptions_res:

        rRPC_response = await service.get_data_from_gRPC(start_time, end_time)

        res = []
        for dp in rRPC_response.data_points:
            res.append(
                schemas.data_point(
                    time=datetime.utcfromtimestamp(dp.time.seconds),
                    value=dp.value
                )
            )

        return schemas.get_consumptions_res(data_points=res)