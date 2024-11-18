from datetime import datetime, timezone

import grpc
from src.server.proto import metric_service_pb2, metric_service_pb2_grpc

from google.protobuf.timestamp_pb2 import Timestamp


class MetricService(metric_service_pb2_grpc.MetricServiceServicer):
    def __init__(self, metric_use_case):
        self.metric_use_case = metric_use_case

    def GetMetrics(self, request, context):

        try:
            # Convert gRPC Timestamps to Python datetime objects
            start_time = datetime.utcfromtimestamp(request.start_time.seconds).replace(tzinfo=timezone.utc)
            end_time = datetime.utcfromtimestamp(request.end_time.seconds).replace(tzinfo=timezone.utc)

            data_points = self.metric_use_case.get_data_between(start_time, end_time)

            # Convert data points to the response format
            response = metric_service_pb2.MetricResponse()
            for dp in data_points:
                timestamp = Timestamp()
                timestamp.FromDatetime(dp.time)
                response.data_points.add(time=timestamp, value=dp.value)
            
            return response
            
        except Exception as e:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(f"An internal error occurred: {e}")
            return metric_service_pb2.MetricResponse()
