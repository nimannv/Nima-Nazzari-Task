from config import settings
from concurrent import futures
import grpc
from server.proto import metric_service_pb2_grpc
from server.service import MetricService
import logging

from domain.data_loader.data_loader_factory import DataLoaderFactory
from domain.metric.metric_use_case import MetricUseCase


def serve(port: int):
    # Set up logging
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    try:
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))


        if settings.DATA_LOADER_TYPE == "csv":
            logger.info("setting CSV data loader")
            data_loader = DataLoaderFactory.create_csv_loader('meterusage.csv')
        elif settings.DATA_LOADER_TYPE == "influxdb":
            logger.info("setting Influxdb data loader")
            data_loader = DataLoaderFactory.create_influxdb_loader(
                settings.INFLUXDB_URL,
                settings.INFLUXDB_TOKEN,
                settings.INFLUXDB_ORG
            )
        else:
            raise Exception('There is no valid DATA_LOADER_TYPE')


        metric_use_case = MetricUseCase(data_loader)

        metric_service = MetricService(metric_use_case)
        metric_service_pb2_grpc.add_MetricServiceServicer_to_server(metric_service, server)
        server.add_insecure_port('[::]:' + str(port))
        logger.info("gRPC server is running on port " + str(port) + "...")
        server.start()
        server.wait_for_termination()
    except Exception as e:
        logger.error(f"Exception occurred: {e}", exc_info=True)



