# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from src.consumption.proto import metric_service_pb2 as src_dot_consumption_dot_proto_dot_metric__service__pb2

GRPC_GENERATED_VERSION = '1.67.1'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in src/consumption/proto/metric_service_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class MetricServiceStub(object):
    """Service definition
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetMetrics = channel.unary_unary(
                '/metric.MetricService/GetMetrics',
                request_serializer=src_dot_consumption_dot_proto_dot_metric__service__pb2.MetricRequest.SerializeToString,
                response_deserializer=src_dot_consumption_dot_proto_dot_metric__service__pb2.MetricResponse.FromString,
                _registered_method=True)


class MetricServiceServicer(object):
    """Service definition
    """

    def GetMetrics(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MetricServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetMetrics': grpc.unary_unary_rpc_method_handler(
                    servicer.GetMetrics,
                    request_deserializer=src_dot_consumption_dot_proto_dot_metric__service__pb2.MetricRequest.FromString,
                    response_serializer=src_dot_consumption_dot_proto_dot_metric__service__pb2.MetricResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'metric.MetricService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('metric.MetricService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class MetricService(object):
    """Service definition
    """

    @staticmethod
    def GetMetrics(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/metric.MetricService/GetMetrics',
            src_dot_consumption_dot_proto_dot_metric__service__pb2.MetricRequest.SerializeToString,
            src_dot_consumption_dot_proto_dot_metric__service__pb2.MetricResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
