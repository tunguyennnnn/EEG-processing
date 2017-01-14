import grpc
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities

import front_end_pb2 as front__end__pb2
import shared_pb2 as shared__pb2


class FrontEndStub(object):

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.ExecuteMentalCommand = channel.unary_unary(
        '/interop.FrontEnd/ExecuteMentalCommand',
        request_serializer=front__end__pb2.CommandRequest.SerializeToString,
        response_deserializer=shared__pb2.StatusReply.FromString,
        )


class FrontEndServicer(object):

  def ExecuteMentalCommand(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_FrontEndServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'ExecuteMentalCommand': grpc.unary_unary_rpc_method_handler(
          servicer.ExecuteMentalCommand,
          request_deserializer=front__end__pb2.CommandRequest.FromString,
          response_serializer=shared__pb2.StatusReply.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'interop.FrontEnd', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
