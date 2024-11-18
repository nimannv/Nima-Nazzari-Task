import logging

from concurrent import futures
import grpc

from src.config import settings
from src.server.proto import metric_service_pb2_grpc
from src.server.service import MetricService
from src.domain.data_loader.data_loader_factory import DataLoaderFactory
from src.domain.metric.metric_use_case import MetricUseCase


def serve(port: int):
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    try:
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

        if settings.DATA_LOADER_TYPE == "csv":
            logger.info("setting CSV data loader")
            data_loader = DataLoaderFactory.create_csv_loader(settings.CSV_FILE_ADDRESS)
        elif settings.DATA_LOADER_TYPE == "influxdb":
            logger.info("setting Influxdb data loader")
            data_loader = DataLoaderFactory.create_influxdb_loader(
                settings.INFLUXDB_URL,
                settings.INFLUXDB_TOKEN,
                settings.INFLUXDB_ORG
            )
        else:
            logger.error("Invalid DATA_LOADER_TYPE specified")
            raise ValueError('There is no valid DATA_LOADER_TYPE')

        metric_use_case = MetricUseCase(data_loader)
        metric_service = MetricService(metric_use_case)
        metric_service_pb2_grpc.add_MetricServiceServicer_to_server(metric_service, server)

        server.add_insecure_port('[::]:' + str(port))
        logger.info("gRPC server is running on port " + str(port) + "...")
        
        server.start()
        server.wait_for_termination()
    
    except ValueError as ve:
        logger.error(f"ValueError occurred: {ve}", exc_info=True)
    except grpc.RpcError as rpc_err:
        logger.error(f"gRPC error occurred: {rpc_err}", exc_info=True)
    except Exception as e:
        logger.error(f"Unexpected error occurred: {e}", exc_info=True)
    finally:
        server.stop(0)
        logger.info("Server has been stopped")
