# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import grpc_demo_pb2 as grpc__demo__pb2

GRPC_GENERATED_VERSION = '1.68.0'
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
        + f' but the generated code in grpc_demo_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class GrpcDemoStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.generate_seq = channel.unary_unary(
                '/grpc_demo.GrpcDemo/generate_seq',
                request_serializer=grpc__demo__pb2.String.SerializeToString,
                response_deserializer=grpc__demo__pb2.String.FromString,
                _registered_method=True)
        self.generate_seq_stream = channel.unary_stream(
                '/grpc_demo.GrpcDemo/generate_seq_stream',
                request_serializer=grpc__demo__pb2.String.SerializeToString,
                response_deserializer=grpc__demo__pb2.String.FromString,
                _registered_method=True)


class GrpcDemoServicer(object):
    """Missing associated documentation comment in .proto file."""

    def generate_seq(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def generate_seq_stream(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_GrpcDemoServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'generate_seq': grpc.unary_unary_rpc_method_handler(
                    servicer.generate_seq,
                    request_deserializer=grpc__demo__pb2.String.FromString,
                    response_serializer=grpc__demo__pb2.String.SerializeToString,
            ),
            'generate_seq_stream': grpc.unary_stream_rpc_method_handler(
                    servicer.generate_seq_stream,
                    request_deserializer=grpc__demo__pb2.String.FromString,
                    response_serializer=grpc__demo__pb2.String.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'grpc_demo.GrpcDemo', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('grpc_demo.GrpcDemo', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class GrpcDemo(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def generate_seq(request,
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
            '/grpc_demo.GrpcDemo/generate_seq',
            grpc__demo__pb2.String.SerializeToString,
            grpc__demo__pb2.String.FromString,
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
    def generate_seq_stream(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(
            request,
            target,
            '/grpc_demo.GrpcDemo/generate_seq_stream',
            grpc__demo__pb2.String.SerializeToString,
            grpc__demo__pb2.String.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
