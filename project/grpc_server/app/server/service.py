from server.proto import metric_service_pb2, metric_service_pb2_grpc

from google.protobuf.timestamp_pb2 import Timestamp

from datetime import datetime, timezone

from data.data_loader.data_loader_factory import DataLoaderFactory
from data.metric.metric import Metric


class MetricService(metric_service_pb2_grpc.MetricServiceServicer):
    def __init__(self):

        # CSV data_loader
        # data_loader = DataLoaderFactory.create_csv_loader('meterusage.csv')

        # Influx data_loader
        data_loader = DataLoaderFactory.create_influxdb_loader('http://influxdb:8086', 'mytoken', 'spectral')

        self.metric = Metric(data_loader)

    def GetMetrics(self, request, context):
        # Convert gRPC Timestamps to Python datetime objects
        
        start_time = datetime.utcfromtimestamp(request.start_time.seconds).replace(tzinfo=timezone.utc)
        end_time = datetime.utcfromtimestamp(request.end_time.seconds).replace(tzinfo=timezone.utc)

        # Fetch data points between start_time and end_time
        data_points = self.metric.get_data_between(start_time, end_time)

        # Convert data points to the response format
        response = metric_service_pb2.MetricResponse()
        for dp in data_points:
            timestamp = Timestamp()
            timestamp.FromDatetime(dp.time)
            response.data_points.add(time=timestamp, value=dp.value)
        
        return response
