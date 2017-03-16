import grpc
from grpc.framework.common import cardinality
from grpc.framework.interfaces.face import utilities as face_utilities

import back_end_pb2 as back__end__pb2
import shared_pb2 as shared__pb2
import back_end_pb2 as back__end__pb2
import shared_pb2 as shared__pb2
import back_end_pb2 as back__end__pb2
import shared_pb2 as shared__pb2
import back_end_pb2 as back__end__pb2
import shared_pb2 as shared__pb2
import back_end_pb2 as back__end__pb2
import shared_pb2 as shared__pb2
import back_end_pb2 as back__end__pb2
import shared_pb2 as shared__pb2
import back_end_pb2 as back__end__pb2
import shared_pb2 as shared__pb2
import back_end_pb2 as back__end__pb2
import back_end_pb2 as back__end__pb2
import back_end_pb2 as back__end__pb2
import back_end_pb2 as back__end__pb2
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
    self.ResetDataForCommand = channel.unary_unary(
        '/interop.BackEnd/ResetDataForCommand',
        request_serializer=back__end__pb2.ResetDataRequest.SerializeToString,
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
    self.StopRecognizion = channel.unary_unary(
        '/interop.BackEnd/StopRecognizion',
        request_serializer=back__end__pb2.EmptyRequest.SerializeToString,
        response_deserializer=shared__pb2.StatusReply.FromString,
        )
    self.CreateUserProfile = channel.unary_unary(
        '/interop.BackEnd/CreateUserProfile',
        request_serializer=back__end__pb2.UserProfileOperationRequest.SerializeToString,
        response_deserializer=shared__pb2.StatusReply.FromString,
        )
    self.DeleteUserProfile = channel.unary_unary(
        '/interop.BackEnd/DeleteUserProfile',
        request_serializer=back__end__pb2.UserProfileOperationRequest.SerializeToString,
        response_deserializer=shared__pb2.StatusReply.FromString,
        )
    self.GetUserProfile = channel.unary_unary(
        '/interop.BackEnd/GetUserProfile',
        request_serializer=back__end__pb2.UserProfileOperationRequest.SerializeToString,
        response_deserializer=back__end__pb2.ProfileDataReply.FromString,
        )
    self.GetUserProfiles = channel.unary_unary(
        '/interop.BackEnd/GetUserProfiles',
        request_serializer=back__end__pb2.EmptyRequest.SerializeToString,
        response_deserializer=back__end__pb2.ProfileListReply.FromString,
        )
    self.UpdateSensorData = channel.unary_unary(
        '/interop.BackEnd/UpdateSensorData',
        request_serializer=back__end__pb2.UpdateSensorDataRequest.SerializeToString,
        response_deserializer=shared__pb2.StatusReply.FromString,
        )
    self.DroneTakeoff = channel.unary_unary(
        '/interop.BackEnd/DroneTakeoff',
        request_serializer=back__end__pb2.EmptyRequest.SerializeToString,
        response_deserializer=shared__pb2.StatusReply.FromString,
        )
    self.DroneLand = channel.unary_unary(
        '/interop.BackEnd/DroneLand',
        request_serializer=back__end__pb2.EmptyRequest.SerializeToString,
        response_deserializer=shared__pb2.StatusReply.FromString,
        )


class BackEndServicer(object):

  def AcquireDataForCommand(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ResetDataForCommand(self, request, context):
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

  def StopRecognizion(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CreateUserProfile(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeleteUserProfile(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetUserProfile(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetUserProfiles(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdateSensorData(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DroneTakeoff(self, request, context):
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DroneLand(self, request, context):
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
      'ResetDataForCommand': grpc.unary_unary_rpc_method_handler(
          servicer.ResetDataForCommand,
          request_deserializer=back__end__pb2.ResetDataRequest.FromString,
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
      'StopRecognizion': grpc.unary_unary_rpc_method_handler(
          servicer.StopRecognizion,
          request_deserializer=back__end__pb2.EmptyRequest.FromString,
          response_serializer=shared__pb2.StatusReply.SerializeToString,
      ),
      'CreateUserProfile': grpc.unary_unary_rpc_method_handler(
          servicer.CreateUserProfile,
          request_deserializer=back__end__pb2.UserProfileOperationRequest.FromString,
          response_serializer=shared__pb2.StatusReply.SerializeToString,
      ),
      'DeleteUserProfile': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteUserProfile,
          request_deserializer=back__end__pb2.UserProfileOperationRequest.FromString,
          response_serializer=shared__pb2.StatusReply.SerializeToString,
      ),
      'GetUserProfile': grpc.unary_unary_rpc_method_handler(
          servicer.GetUserProfile,
          request_deserializer=back__end__pb2.UserProfileOperationRequest.FromString,
          response_serializer=back__end__pb2.ProfileDataReply.SerializeToString,
      ),
      'GetUserProfiles': grpc.unary_unary_rpc_method_handler(
          servicer.GetUserProfiles,
          request_deserializer=back__end__pb2.EmptyRequest.FromString,
          response_serializer=back__end__pb2.ProfileListReply.SerializeToString,
      ),
      'UpdateSensorData': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateSensorData,
          request_deserializer=back__end__pb2.UpdateSensorDataRequest.FromString,
          response_serializer=shared__pb2.StatusReply.SerializeToString,
      ),
      'DroneTakeoff': grpc.unary_unary_rpc_method_handler(
          servicer.DroneTakeoff,
          request_deserializer=back__end__pb2.EmptyRequest.FromString,
          response_serializer=shared__pb2.StatusReply.SerializeToString,
      ),
      'DroneLand': grpc.unary_unary_rpc_method_handler(
          servicer.DroneLand,
          request_deserializer=back__end__pb2.EmptyRequest.FromString,
          response_serializer=shared__pb2.StatusReply.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'interop.BackEnd', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
