# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: flwr/proto/message.proto
# Protobuf Python Version: 5.29.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    0,
    '',
    'flwr/proto/message.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from flwr.proto import error_pb2 as flwr_dot_proto_dot_error__pb2
from flwr.proto import recordset_pb2 as flwr_dot_proto_dot_recordset__pb2
from flwr.proto import transport_pb2 as flwr_dot_proto_dot_transport__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18\x66lwr/proto/message.proto\x12\nflwr.proto\x1a\x16\x66lwr/proto/error.proto\x1a\x1a\x66lwr/proto/recordset.proto\x1a\x1a\x66lwr/proto/transport.proto\"{\n\x07Message\x12&\n\x08metadata\x18\x01 \x01(\x0b\x32\x14.flwr.proto.Metadata\x12&\n\x07\x63ontent\x18\x02 \x01(\x0b\x32\x15.flwr.proto.RecordSet\x12 \n\x05\x65rror\x18\x03 \x01(\x0b\x32\x11.flwr.proto.Error\"\xcf\x02\n\x07\x43ontext\x12\x0e\n\x06run_id\x18\x01 \x01(\x04\x12\x0f\n\x07node_id\x18\x02 \x01(\x04\x12\x38\n\x0bnode_config\x18\x03 \x03(\x0b\x32#.flwr.proto.Context.NodeConfigEntry\x12$\n\x05state\x18\x04 \x01(\x0b\x32\x15.flwr.proto.RecordSet\x12\x36\n\nrun_config\x18\x05 \x03(\x0b\x32\".flwr.proto.Context.RunConfigEntry\x1a\x45\n\x0fNodeConfigEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12!\n\x05value\x18\x02 \x01(\x0b\x32\x12.flwr.proto.Scalar:\x02\x38\x01\x1a\x44\n\x0eRunConfigEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12!\n\x05value\x18\x02 \x01(\x0b\x32\x12.flwr.proto.Scalar:\x02\x38\x01\"\xbb\x01\n\x08Metadata\x12\x0e\n\x06run_id\x18\x01 \x01(\x04\x12\x12\n\nmessage_id\x18\x02 \x01(\t\x12\x13\n\x0bsrc_node_id\x18\x03 \x01(\x04\x12\x13\n\x0b\x64st_node_id\x18\x04 \x01(\x04\x12\x18\n\x10reply_to_message\x18\x05 \x01(\t\x12\x10\n\x08group_id\x18\x06 \x01(\t\x12\x0b\n\x03ttl\x18\x07 \x01(\x01\x12\x14\n\x0cmessage_type\x18\x08 \x01(\t\x12\x12\n\ncreated_at\x18\t \x01(\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'flwr.proto.message_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_CONTEXT_NODECONFIGENTRY']._loaded_options = None
  _globals['_CONTEXT_NODECONFIGENTRY']._serialized_options = b'8\001'
  _globals['_CONTEXT_RUNCONFIGENTRY']._loaded_options = None
  _globals['_CONTEXT_RUNCONFIGENTRY']._serialized_options = b'8\001'
  _globals['_MESSAGE']._serialized_start=120
  _globals['_MESSAGE']._serialized_end=243
  _globals['_CONTEXT']._serialized_start=246
  _globals['_CONTEXT']._serialized_end=581
  _globals['_CONTEXT_NODECONFIGENTRY']._serialized_start=442
  _globals['_CONTEXT_NODECONFIGENTRY']._serialized_end=511
  _globals['_CONTEXT_RUNCONFIGENTRY']._serialized_start=513
  _globals['_CONTEXT_RUNCONFIGENTRY']._serialized_end=581
  _globals['_METADATA']._serialized_start=584
  _globals['_METADATA']._serialized_end=771
# @@protoc_insertion_point(module_scope)
