from concurrent import futures
import grpc
from server.proto import metric_service_pb2_grpc
from server.service import MetricService
import logging


def serve(port: int):
    # Set up logging
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    try:
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        metric_service_pb2_grpc.add_MetricServiceServicer_to_server(MetricService(), server)
        server.add_insecure_port('[::]:' + str(port))
        logger.info("gRPC server is running on port " + str(port) + "...")
        server.start()
        server.wait_for_termination()
    except Exception as e:
        logger.error(f"Exception occurred: {e}", exc_info=True)



