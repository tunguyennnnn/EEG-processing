# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: front_end.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import shared_pb2 as shared__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='front_end.proto',
  package='interop',
  syntax='proto3',
  serialized_pb=_b('\n\x0f\x66ront_end.proto\x12\x07interop\x1a\x0cshared.proto\"<\n\x0e\x43ommandRequest\x12*\n\x0c\x63ommand_type\x18\x01 \x01(\x0e\x32\x14.interop.CommandType\"7\n\x0e\x42\x43IDataRequest\x12%\n\x07\x42\x43IData\x18\x01 \x03(\x0b\x32\x14.interop.ChannelData\"\x1d\n\x0b\x43hannelData\x12\x0e\n\x06values\x18\x01 \x03(\x02\x32\x95\x01\n\x08\x46rontEnd\x12G\n\x14\x45xecuteMentalCommand\x12\x17.interop.CommandRequest\x1a\x14.interop.StatusReply\"\x00\x12@\n\rUpdateBCIData\x12\x17.interop.BCIDataRequest\x1a\x14.interop.StatusReply\"\x00\x62\x06proto3')
  ,
  dependencies=[shared__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_COMMANDREQUEST = _descriptor.Descriptor(
  name='CommandRequest',
  full_name='interop.CommandRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='command_type', full_name='interop.CommandRequest.command_type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=42,
  serialized_end=102,
)


_BCIDATAREQUEST = _descriptor.Descriptor(
  name='BCIDataRequest',
  full_name='interop.BCIDataRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='BCIData', full_name='interop.BCIDataRequest.BCIData', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=104,
  serialized_end=159,
)


_CHANNELDATA = _descriptor.Descriptor(
  name='ChannelData',
  full_name='interop.ChannelData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='values', full_name='interop.ChannelData.values', index=0,
      number=1, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=161,
  serialized_end=190,
)

_COMMANDREQUEST.fields_by_name['command_type'].enum_type = shared__pb2._COMMANDTYPE
_BCIDATAREQUEST.fields_by_name['BCIData'].message_type = _CHANNELDATA
DESCRIPTOR.message_types_by_name['CommandRequest'] = _COMMANDREQUEST
DESCRIPTOR.message_types_by_name['BCIDataRequest'] = _BCIDATAREQUEST
DESCRIPTOR.message_types_by_name['ChannelData'] = _CHANNELDATA

CommandRequest = _reflection.GeneratedProtocolMessageType('CommandRequest', (_message.Message,), dict(
  DESCRIPTOR = _COMMANDREQUEST,
  __module__ = 'front_end_pb2'
  # @@protoc_insertion_point(class_scope:interop.CommandRequest)
  ))
_sym_db.RegisterMessage(CommandRequest)

BCIDataRequest = _reflection.GeneratedProtocolMessageType('BCIDataRequest', (_message.Message,), dict(
  DESCRIPTOR = _BCIDATAREQUEST,
  __module__ = 'front_end_pb2'
  # @@protoc_insertion_point(class_scope:interop.BCIDataRequest)
  ))
_sym_db.RegisterMessage(BCIDataRequest)

ChannelData = _reflection.GeneratedProtocolMessageType('ChannelData', (_message.Message,), dict(
  DESCRIPTOR = _CHANNELDATA,
  __module__ = 'front_end_pb2'
  # @@protoc_insertion_point(class_scope:interop.ChannelData)
  ))
_sym_db.RegisterMessage(ChannelData)


try:
  # THESE ELEMENTS WILL BE DEPRECATED.
  # Please use the generated *_pb2_grpc.py files instead.
  import grpc
  from grpc.framework.common import cardinality
  from grpc.framework.interfaces.face import utilities as face_utilities
  from grpc.beta import implementations as beta_implementations
  from grpc.beta import interfaces as beta_interfaces


  class FrontEndStub(object):

    def __init__(self, channel):
      """Constructor.

      Args:
        channel: A grpc.Channel.
      """
      self.ExecuteMentalCommand = channel.unary_unary(
          '/interop.FrontEnd/ExecuteMentalCommand',
          request_serializer=CommandRequest.SerializeToString,
          response_deserializer=shared__pb2.StatusReply.FromString,
          )
      self.UpdateBCIData = channel.unary_unary(
          '/interop.FrontEnd/UpdateBCIData',
          request_serializer=BCIDataRequest.SerializeToString,
          response_deserializer=shared__pb2.StatusReply.FromString,
          )


  class FrontEndServicer(object):

    def ExecuteMentalCommand(self, request, context):
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')

    def UpdateBCIData(self, request, context):
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')


  def add_FrontEndServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'ExecuteMentalCommand': grpc.unary_unary_rpc_method_handler(
            servicer.ExecuteMentalCommand,
            request_deserializer=CommandRequest.FromString,
            response_serializer=shared__pb2.StatusReply.SerializeToString,
        ),
        'UpdateBCIData': grpc.unary_unary_rpc_method_handler(
            servicer.UpdateBCIData,
            request_deserializer=BCIDataRequest.FromString,
            response_serializer=shared__pb2.StatusReply.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'interop.FrontEnd', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


  class BetaFrontEndServicer(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    def ExecuteMentalCommand(self, request, context):
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def UpdateBCIData(self, request, context):
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)


  class BetaFrontEndStub(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    def ExecuteMentalCommand(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      raise NotImplementedError()
    ExecuteMentalCommand.future = None
    def UpdateBCIData(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      raise NotImplementedError()
    UpdateBCIData.future = None


  def beta_create_FrontEnd_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_deserializers = {
      ('interop.FrontEnd', 'ExecuteMentalCommand'): CommandRequest.FromString,
      ('interop.FrontEnd', 'UpdateBCIData'): BCIDataRequest.FromString,
    }
    response_serializers = {
      ('interop.FrontEnd', 'ExecuteMentalCommand'): shared__pb2.StatusReply.SerializeToString,
      ('interop.FrontEnd', 'UpdateBCIData'): shared__pb2.StatusReply.SerializeToString,
    }
    method_implementations = {
      ('interop.FrontEnd', 'ExecuteMentalCommand'): face_utilities.unary_unary_inline(servicer.ExecuteMentalCommand),
      ('interop.FrontEnd', 'UpdateBCIData'): face_utilities.unary_unary_inline(servicer.UpdateBCIData),
    }
    server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
    return beta_implementations.server(method_implementations, options=server_options)


  def beta_create_FrontEnd_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_serializers = {
      ('interop.FrontEnd', 'ExecuteMentalCommand'): CommandRequest.SerializeToString,
      ('interop.FrontEnd', 'UpdateBCIData'): BCIDataRequest.SerializeToString,
    }
    response_deserializers = {
      ('interop.FrontEnd', 'ExecuteMentalCommand'): shared__pb2.StatusReply.FromString,
      ('interop.FrontEnd', 'UpdateBCIData'): shared__pb2.StatusReply.FromString,
    }
    cardinalities = {
      'ExecuteMentalCommand': cardinality.Cardinality.UNARY_UNARY,
      'UpdateBCIData': cardinality.Cardinality.UNARY_UNARY,
    }
    stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
    return beta_implementations.dynamic_stub(channel, 'interop.FrontEnd', cardinalities, options=stub_options)
except ImportError:
  pass
# @@protoc_insertion_point(module_scope)
