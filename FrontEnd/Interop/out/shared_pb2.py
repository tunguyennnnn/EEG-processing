# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: shared.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='shared.proto',
  package='interop',
  syntax='proto3',
  serialized_pb=_b('\n\x0cshared.proto\x12\x07interop\"\x1b\n\x0bStatusReply\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05*\x93\x01\n\x0b\x43ommandType\x12\x10\n\x0cMOVE_FORWARD\x10\x00\x12\r\n\tMOVE_BACK\x10\x01\x12\x0e\n\nMOVE_RIGHT\x10\x02\x12\r\n\tMOVE_LEFT\x10\x03\x12\x0b\n\x07MOVE_UP\x10\x04\x12\r\n\tMOVE_DOWN\x10\x05\x12\x0e\n\nTURN_RIGHT\x10\x06\x12\r\n\tTURN_LEFT\x10\x07\x12\t\n\x05RESET\x10\x08\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_COMMANDTYPE = _descriptor.EnumDescriptor(
  name='CommandType',
  full_name='interop.CommandType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='MOVE_FORWARD', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MOVE_BACK', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MOVE_RIGHT', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MOVE_LEFT', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MOVE_UP', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MOVE_DOWN', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TURN_RIGHT', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='TURN_LEFT', index=7, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RESET', index=8, number=8,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=55,
  serialized_end=202,
)
_sym_db.RegisterEnumDescriptor(_COMMANDTYPE)

CommandType = enum_type_wrapper.EnumTypeWrapper(_COMMANDTYPE)
MOVE_FORWARD = 0
MOVE_BACK = 1
MOVE_RIGHT = 2
MOVE_LEFT = 3
MOVE_UP = 4
MOVE_DOWN = 5
TURN_RIGHT = 6
TURN_LEFT = 7
RESET = 8



_STATUSREPLY = _descriptor.Descriptor(
  name='StatusReply',
  full_name='interop.StatusReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='interop.StatusReply.code', index=0,
      number=1, type=5, cpp_type=1, label=1,
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
  serialized_start=25,
  serialized_end=52,
)

DESCRIPTOR.message_types_by_name['StatusReply'] = _STATUSREPLY
DESCRIPTOR.enum_types_by_name['CommandType'] = _COMMANDTYPE

StatusReply = _reflection.GeneratedProtocolMessageType('StatusReply', (_message.Message,), dict(
  DESCRIPTOR = _STATUSREPLY,
  __module__ = 'shared_pb2'
  # @@protoc_insertion_point(class_scope:interop.StatusReply)
  ))
_sym_db.RegisterMessage(StatusReply)


try:
  # THESE ELEMENTS WILL BE DEPRECATED.
  # Please use the generated *_pb2_grpc.py files instead.
  import grpc
  from grpc.framework.common import cardinality
  from grpc.framework.interfaces.face import utilities as face_utilities
  from grpc.beta import implementations as beta_implementations
  from grpc.beta import interfaces as beta_interfaces
except ImportError:
  pass
# @@protoc_insertion_point(module_scope)