from concurrent import futures
import grpc
from server.proto import metric_service_pb2, metric_service_pb2_grpc

from data.data_loader.data_loader_factory import DataLoaderFactory
from data.metric.metric import Metric

from google.protobuf.timestamp_pb2 import Timestamp
from datetime import datetime


class MetricService(metric_service_pb2_grpc.MetricServiceServicer):
    def __init__(self):

        # Initialize a Metric object with a CSV data loader for demonstration
        data_loader = DataLoaderFactory.create_data_loader('csv', file_path='meterusage.csv')
        self.metric = Metric(data_loader)

    def GetMetrics(self, request, context):
        # Convert gRPC Timestamps to Python datetime objects
        start_time = datetime.utcfromtimestamp(request.start_time.seconds)
        end_time = datetime.utcfromtimestamp(request.end_time.seconds)

        # Fetch data points between start_time and end_time
        data_points = self.metric.get_data_between(start_time, end_time)

        # Convert data points to the response format
        response = metric_service_pb2.MetricResponse()
        for dp in data_points:
            timestamp = Timestamp()
            timestamp.FromDatetime(dp.time)
            response.data_points.add(time=timestamp, value=dp.value)
        
        return response

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    metric_service_pb2_grpc.add_MetricServiceServicer_to_server(MetricService(), server)
    server.add_insecure_port('[::]:50051')
    print("gRPC server is running on port 50051...")
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()








# # Build a Metric with an InfluxDB data loader without any filter
# influx_loader = DataLoaderFactory.create_data_loader(
#     'influxdb',
#     host='localhost', port=8086, database='mydatabase'
# )

# metric_influx = (metric_builder
#                  .set_data_loader(influx_loader)
#                  .build())

# influx_data = metric_influx.get_data_between(start_time, end_time)
# print(influx_data)

# # Build a Metric with a TimescaleDB data loader and a different filter
# timescale_loader = DataLoaderFactory.create_data_loader(
#     'timescale',
#     host='localhost', port=5432, database='mydatabase', user='user', password='password'
# )

# metric_timescale = (metric_builder
#                     .set_data_loader(timescale_loader)
#                     .set_filter(lambda dps: filter_by_value_threshold(dps, 100.0))
#                     .build())

# timescale_data = metric_timescale.get_data_between(start_time, end_time)
# print(timescale_data)
