import logging
from datetime import datetime

import grpc
from ..consumption.proto import metric_service_pb2, metric_service_pb2_grpc
from ..config import settings

async def get_data_from_gRPC(start_time: datetime, end_time: datetime):
    try:
        channel = grpc.aio.insecure_channel(settings.GRPC_ADDRESS)
        stub = metric_service_pb2_grpc.MetricServiceStub(channel)
        request = metric_service_pb2.MetricRequest(start_time=start_time, end_time=end_time)
        response = await stub.GetMetrics(request)
        await channel.close()
        return response

    except grpc.RpcError as e:
        logging.error(f"gRPC call failed with error: {e.code()} - {e.details()}")
        raise