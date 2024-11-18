import grpc
from src.consumption.proto import metric_service_pb2_grpc

from src.config import settings

class GRPCClient:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(GRPCClient, cls).__new__(cls)
            cls._instance.channel = grpc.aio.insecure_channel(settings.GRPC_ADDRESS)
            cls._instance.stub = metric_service_pb2_grpc.MetricServiceStub(cls._instance.channel)
        return cls._instance

    async def close(self):
        await self.channel.close()
