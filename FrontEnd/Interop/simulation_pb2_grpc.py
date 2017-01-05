import grpc
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities

import simulation_pb2 as simulation__pb2
import simulation_pb2 as simulation__pb2


class FrontEndStub(object):

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.ExecuteMentalCommand = channel.unary_unary(
        '/front_end.FrontEnd/ExecuteMentalCommand',
        request_serializer=simulation__pb2.CommandRequest.SerializeToString,
        response_deserializer=simulation__pb2.StatusReply.FromString,
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
          request_deserializer=simulation__pb2.CommandRequest.FromString,
          response_serializer=simulation__pb2.StatusReply.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'front_end.FrontEnd', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))