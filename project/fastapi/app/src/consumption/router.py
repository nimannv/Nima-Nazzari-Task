from fastapi import Depends, HTTPException, APIRouter
from ..consumption import dependencies, schemas
from ..config import settings

from datetime import datetime

import grpc
from ..consumption.proto import metric_service_pb2, metric_service_pb2_grpc

router = APIRouter()

@router.get("/get_consumptions")
async def get_consumptions(start_time: datetime, end_time: datetime) -> schemas.get_consumptions_res:

    with grpc.insecure_channel(settings.GRPC_ADDRESS) as channel:
        stub = metric_service_pb2_grpc.MetricServiceStub(channel)
        request = metric_service_pb2.MetricRequest(start_time=start_time, end_time=end_time)
        response = stub.GetMetrics(request)

        res = []
        for dp in response.data_points:
            res.append(
                schemas.data_point(
                    time=datetime.utcfromtimestamp(dp.time.seconds),
                    value=dp.value
                )
            )

        return schemas.get_consumptions_res(data_points=res)