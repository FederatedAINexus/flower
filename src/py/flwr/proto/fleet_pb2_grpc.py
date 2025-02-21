# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from flwr.proto import fab_pb2 as flwr_dot_proto_dot_fab__pb2
from flwr.proto import fleet_pb2 as flwr_dot_proto_dot_fleet__pb2
from flwr.proto import run_pb2 as flwr_dot_proto_dot_run__pb2

GRPC_GENERATED_VERSION = '1.69.0'
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
        + f' but the generated code in flwr/proto/fleet_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class FleetStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateNode = channel.unary_unary(
                '/flwr.proto.Fleet/CreateNode',
                request_serializer=flwr_dot_proto_dot_fleet__pb2.CreateNodeRequest.SerializeToString,
                response_deserializer=flwr_dot_proto_dot_fleet__pb2.CreateNodeResponse.FromString,
                _registered_method=True)
        self.DeleteNode = channel.unary_unary(
                '/flwr.proto.Fleet/DeleteNode',
                request_serializer=flwr_dot_proto_dot_fleet__pb2.DeleteNodeRequest.SerializeToString,
                response_deserializer=flwr_dot_proto_dot_fleet__pb2.DeleteNodeResponse.FromString,
                _registered_method=True)
        self.Ping = channel.unary_unary(
                '/flwr.proto.Fleet/Ping',
                request_serializer=flwr_dot_proto_dot_fleet__pb2.PingRequest.SerializeToString,
                response_deserializer=flwr_dot_proto_dot_fleet__pb2.PingResponse.FromString,
                _registered_method=True)
        self.PullTaskIns = channel.unary_unary(
                '/flwr.proto.Fleet/PullTaskIns',
                request_serializer=flwr_dot_proto_dot_fleet__pb2.PullTaskInsRequest.SerializeToString,
                response_deserializer=flwr_dot_proto_dot_fleet__pb2.PullTaskInsResponse.FromString,
                _registered_method=True)
        self.PullMessages = channel.unary_unary(
                '/flwr.proto.Fleet/PullMessages',
                request_serializer=flwr_dot_proto_dot_fleet__pb2.PullMessagesRequest.SerializeToString,
                response_deserializer=flwr_dot_proto_dot_fleet__pb2.PullMessagesResponse.FromString,
                _registered_method=True)
        self.PushTaskRes = channel.unary_unary(
                '/flwr.proto.Fleet/PushTaskRes',
                request_serializer=flwr_dot_proto_dot_fleet__pb2.PushTaskResRequest.SerializeToString,
                response_deserializer=flwr_dot_proto_dot_fleet__pb2.PushTaskResResponse.FromString,
                _registered_method=True)
        self.PushMessages = channel.unary_unary(
                '/flwr.proto.Fleet/PushMessages',
                request_serializer=flwr_dot_proto_dot_fleet__pb2.PushMessagesRequest.SerializeToString,
                response_deserializer=flwr_dot_proto_dot_fleet__pb2.PushMessagesResponse.FromString,
                _registered_method=True)
        self.GetRun = channel.unary_unary(
                '/flwr.proto.Fleet/GetRun',
                request_serializer=flwr_dot_proto_dot_run__pb2.GetRunRequest.SerializeToString,
                response_deserializer=flwr_dot_proto_dot_run__pb2.GetRunResponse.FromString,
                _registered_method=True)
        self.GetFab = channel.unary_unary(
                '/flwr.proto.Fleet/GetFab',
                request_serializer=flwr_dot_proto_dot_fab__pb2.GetFabRequest.SerializeToString,
                response_deserializer=flwr_dot_proto_dot_fab__pb2.GetFabResponse.FromString,
                _registered_method=True)


class FleetServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CreateNode(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteNode(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Ping(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PullTaskIns(self, request, context):
        """Retrieve one or more tasks, if possible

        HTTP API path: /api/v1/fleet/pull-task-ins
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PullMessages(self, request, context):
        """HTTP API path: /api/v1/fleet/pull-messages
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PushTaskRes(self, request, context):
        """Complete one or more tasks, if possible

        HTTP API path: /api/v1/fleet/push-task-res
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PushMessages(self, request, context):
        """HTTP API path: /api/v1/fleet/push-messages
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetRun(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetFab(self, request, context):
        """Get FAB
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_FleetServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateNode': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateNode,
                    request_deserializer=flwr_dot_proto_dot_fleet__pb2.CreateNodeRequest.FromString,
                    response_serializer=flwr_dot_proto_dot_fleet__pb2.CreateNodeResponse.SerializeToString,
            ),
            'DeleteNode': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteNode,
                    request_deserializer=flwr_dot_proto_dot_fleet__pb2.DeleteNodeRequest.FromString,
                    response_serializer=flwr_dot_proto_dot_fleet__pb2.DeleteNodeResponse.SerializeToString,
            ),
            'Ping': grpc.unary_unary_rpc_method_handler(
                    servicer.Ping,
                    request_deserializer=flwr_dot_proto_dot_fleet__pb2.PingRequest.FromString,
                    response_serializer=flwr_dot_proto_dot_fleet__pb2.PingResponse.SerializeToString,
            ),
            'PullTaskIns': grpc.unary_unary_rpc_method_handler(
                    servicer.PullTaskIns,
                    request_deserializer=flwr_dot_proto_dot_fleet__pb2.PullTaskInsRequest.FromString,
                    response_serializer=flwr_dot_proto_dot_fleet__pb2.PullTaskInsResponse.SerializeToString,
            ),
            'PullMessages': grpc.unary_unary_rpc_method_handler(
                    servicer.PullMessages,
                    request_deserializer=flwr_dot_proto_dot_fleet__pb2.PullMessagesRequest.FromString,
                    response_serializer=flwr_dot_proto_dot_fleet__pb2.PullMessagesResponse.SerializeToString,
            ),
            'PushTaskRes': grpc.unary_unary_rpc_method_handler(
                    servicer.PushTaskRes,
                    request_deserializer=flwr_dot_proto_dot_fleet__pb2.PushTaskResRequest.FromString,
                    response_serializer=flwr_dot_proto_dot_fleet__pb2.PushTaskResResponse.SerializeToString,
            ),
            'PushMessages': grpc.unary_unary_rpc_method_handler(
                    servicer.PushMessages,
                    request_deserializer=flwr_dot_proto_dot_fleet__pb2.PushMessagesRequest.FromString,
                    response_serializer=flwr_dot_proto_dot_fleet__pb2.PushMessagesResponse.SerializeToString,
            ),
            'GetRun': grpc.unary_unary_rpc_method_handler(
                    servicer.GetRun,
                    request_deserializer=flwr_dot_proto_dot_run__pb2.GetRunRequest.FromString,
                    response_serializer=flwr_dot_proto_dot_run__pb2.GetRunResponse.SerializeToString,
            ),
            'GetFab': grpc.unary_unary_rpc_method_handler(
                    servicer.GetFab,
                    request_deserializer=flwr_dot_proto_dot_fab__pb2.GetFabRequest.FromString,
                    response_serializer=flwr_dot_proto_dot_fab__pb2.GetFabResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'flwr.proto.Fleet', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('flwr.proto.Fleet', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class Fleet(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CreateNode(request,
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
            '/flwr.proto.Fleet/CreateNode',
            flwr_dot_proto_dot_fleet__pb2.CreateNodeRequest.SerializeToString,
            flwr_dot_proto_dot_fleet__pb2.CreateNodeResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def DeleteNode(request,
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
            '/flwr.proto.Fleet/DeleteNode',
            flwr_dot_proto_dot_fleet__pb2.DeleteNodeRequest.SerializeToString,
            flwr_dot_proto_dot_fleet__pb2.DeleteNodeResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def Ping(request,
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
            '/flwr.proto.Fleet/Ping',
            flwr_dot_proto_dot_fleet__pb2.PingRequest.SerializeToString,
            flwr_dot_proto_dot_fleet__pb2.PingResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def PullTaskIns(request,
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
            '/flwr.proto.Fleet/PullTaskIns',
            flwr_dot_proto_dot_fleet__pb2.PullTaskInsRequest.SerializeToString,
            flwr_dot_proto_dot_fleet__pb2.PullTaskInsResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def PullMessages(request,
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
            '/flwr.proto.Fleet/PullMessages',
            flwr_dot_proto_dot_fleet__pb2.PullMessagesRequest.SerializeToString,
            flwr_dot_proto_dot_fleet__pb2.PullMessagesResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def PushTaskRes(request,
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
            '/flwr.proto.Fleet/PushTaskRes',
            flwr_dot_proto_dot_fleet__pb2.PushTaskResRequest.SerializeToString,
            flwr_dot_proto_dot_fleet__pb2.PushTaskResResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def PushMessages(request,
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
            '/flwr.proto.Fleet/PushMessages',
            flwr_dot_proto_dot_fleet__pb2.PushMessagesRequest.SerializeToString,
            flwr_dot_proto_dot_fleet__pb2.PushMessagesResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetRun(request,
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
            '/flwr.proto.Fleet/GetRun',
            flwr_dot_proto_dot_run__pb2.GetRunRequest.SerializeToString,
            flwr_dot_proto_dot_run__pb2.GetRunResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetFab(request,
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
            '/flwr.proto.Fleet/GetFab',
            flwr_dot_proto_dot_fab__pb2.GetFabRequest.SerializeToString,
            flwr_dot_proto_dot_fab__pb2.GetFabResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
