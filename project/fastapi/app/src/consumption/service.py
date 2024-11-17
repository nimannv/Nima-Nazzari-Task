import logging
from datetime import datetime

import grpc
from src.consumption.proto import metric_service_pb2

from src.config import settings
from src.consumption.grpc_client import GRPCClient

async def get_data_from_gRPC(grpc_client: GRPCClient, start_time: datetime, end_time: datetime):
    try:
        request = metric_service_pb2.MetricRequest(start_time=start_time, end_time=end_time)
        response = await grpc_client.stub.GetMetrics(request)
        return response

    except grpc.RpcError as e:
        logging.error(f"gRPC call failed with error: {e.code()} - {e.details()}")
        raise