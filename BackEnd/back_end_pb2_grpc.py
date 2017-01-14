import grpc
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities

import back_end_pb2 as back__end__pb2
import shared_pb2 as shared__pb2
import back_end_pb2 as back__end__pb2
import shared_pb2 as shared__pb2
import back_end_pb2 as back__end__pb2
import shared_pb2 as shared__pb2


class BackEndStub(object):

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.AcquireDataForCommand = channel.unary_unary(
        '/interop.BackEnd/AcquireDataForCommand',
        request_serializer=back__end__pb2.AquireDataRequest.SerializeToString,
        response_deserializer=shared__pb2.StatusReply.FromString,
        )
    self.TrainClassifier = channel.unary_unary(
        '/interop.BackEnd/TrainClassifier',
        request_serializer=back__end__pb2.TrainClassifierRequest.SerializeToString,
        response_deserializer=shared__pb2.StatusReply.FromString,
        )
    self.RecognizeCommands = channel.unary_unary(
        '/interop.BackEnd/RecognizeCommands',
        request_serializer=back__end__pb2.RecognizeCommandsRequest.SerializeToString,
        response_deserializer=shared__pb2.StatusReply.FromString,
        )


class BackEndServicer(object):

  def AcquireDataForCommand(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def TrainClassifier(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def RecognizeCommands(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_BackEndServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'AcquireDataForCommand': grpc.unary_unary_rpc_method_handler(
          servicer.AcquireDataForCommand,
          request_deserializer=back__end__pb2.AquireDataRequest.FromString,
          response_serializer=shared__pb2.StatusReply.SerializeToString,
      ),
      'TrainClassifier': grpc.unary_unary_rpc_method_handler(
          servicer.TrainClassifier,
          request_deserializer=back__end__pb2.TrainClassifierRequest.FromString,
          response_serializer=shared__pb2.StatusReply.SerializeToString,
      ),
      'RecognizeCommands': grpc.unary_unary_rpc_method_handler(
          servicer.RecognizeCommands,
          request_deserializer=back__end__pb2.RecognizeCommandsRequest.FromString,
          response_serializer=shared__pb2.StatusReply.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'interop.BackEnd', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
