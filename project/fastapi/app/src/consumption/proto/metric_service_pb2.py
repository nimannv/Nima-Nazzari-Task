# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: src/consumption/proto/metric_service.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    2,
    '',
    'src/consumption/proto/metric_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n*src/consumption/proto/metric_service.proto\x12\x06metric\x1a\x1fgoogle/protobuf/timestamp.proto\"m\n\rMetricRequest\x12.\n\nstart_time\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12,\n\x08\x65nd_time\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"D\n\tDataPoint\x12(\n\x04time\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\r\n\x05value\x18\x02 \x01(\x01\"8\n\x0eMetricResponse\x12&\n\x0b\x64\x61ta_points\x18\x01 \x03(\x0b\x32\x11.metric.DataPoint2L\n\rMetricService\x12;\n\nGetMetrics\x12\x15.metric.MetricRequest\x1a\x16.metric.MetricResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'src.consumption.proto.metric_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_METRICREQUEST']._serialized_start=87
  _globals['_METRICREQUEST']._serialized_end=196
  _globals['_DATAPOINT']._serialized_start=198
  _globals['_DATAPOINT']._serialized_end=266
  _globals['_METRICRESPONSE']._serialized_start=268
  _globals['_METRICRESPONSE']._serialized_end=324
  _globals['_METRICSERVICE']._serialized_start=326
  _globals['_METRICSERVICE']._serialized_end=402
# @@protoc_insertion_point(module_scope)