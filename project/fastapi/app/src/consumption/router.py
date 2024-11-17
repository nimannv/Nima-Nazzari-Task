from fastapi import Depends, HTTPException, APIRouter
from src.consumption import schemas, service, dependencies
from src.consumption.grpc_client import GRPCClient

from datetime import datetime

router = APIRouter()

@router.get("/get_consumptions")
async def get_consumptions(
    start_time: datetime,
    end_time: datetime,
    grpc_client: GRPCClient = Depends(dependencies.get_grpc_client)
    ) -> schemas.get_consumptions_res:

        # check time orders
        if end_time < start_time:
            raise HTTPException(status_code=400, detail="End time is before start time!")

        gRPC_response = await service.get_data_from_gRPC(grpc_client, start_time, end_time)

        res = []
        for dp in gRPC_response.data_points:
            res.append(
                schemas.data_point(
                    time=datetime.utcfromtimestamp(dp.time.seconds),
                    value=dp.value
                )
            )

        return schemas.get_consumptions_res(data_points=res)