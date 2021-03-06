# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Calc.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='Calc.proto',
  package='calc',
  syntax='proto3',
  serialized_pb=_b('\n\nCalc.proto\x12\x04\x63\x61lc\"$\n\nAddRequest\x12\n\n\x02n1\x18\x01 \x01(\x05\x12\n\n\x02n2\x18\x02 \x01(\x05\"\x16\n\x08\x41\x64\x64Reply\x12\n\n\x02n1\x18\x01 \x01(\x05\")\n\x0fSubtractRequest\x12\n\n\x02n1\x18\x01 \x01(\x05\x12\n\n\x02n2\x18\x02 \x01(\x05\"\x1b\n\rSubtractReply\x12\n\n\x02n1\x18\x01 \x01(\x05\")\n\x0fMultiplyRequest\x12\n\n\x02n1\x18\x01 \x01(\x05\x12\n\n\x02n2\x18\x02 \x01(\x05\"\x1b\n\rMultiplyReply\x12\n\n\x02n1\x18\x01 \x01(\x05\"\'\n\rDivideRequest\x12\n\n\x02n1\x18\x01 \x01(\x05\x12\n\n\x02n2\x18\x02 \x01(\x05\"\x19\n\x0b\x44ivideReply\x12\n\n\x02\x66\x31\x18\x01 \x01(\x02\x32\xdf\x01\n\nCalculator\x12)\n\x03\x41\x64\x64\x12\x10.calc.AddRequest\x1a\x0e.calc.AddReply\"\x00\x12\x38\n\x08Subtract\x12\x15.calc.SubtractRequest\x1a\x13.calc.SubtractReply\"\x00\x12\x38\n\x08Multiply\x12\x15.calc.MultiplyRequest\x1a\x13.calc.MultiplyReply\"\x00\x12\x32\n\x06\x44ivide\x12\x13.calc.DivideRequest\x1a\x11.calc.DivideReply\"\x00\x62\x06proto3')
)




_ADDREQUEST = _descriptor.Descriptor(
  name='AddRequest',
  full_name='calc.AddRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='n1', full_name='calc.AddRequest.n1', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='n2', full_name='calc.AddRequest.n2', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=20,
  serialized_end=56,
)


_ADDREPLY = _descriptor.Descriptor(
  name='AddReply',
  full_name='calc.AddReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='n1', full_name='calc.AddReply.n1', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=58,
  serialized_end=80,
)


_SUBTRACTREQUEST = _descriptor.Descriptor(
  name='SubtractRequest',
  full_name='calc.SubtractRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='n1', full_name='calc.SubtractRequest.n1', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='n2', full_name='calc.SubtractRequest.n2', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=82,
  serialized_end=123,
)


_SUBTRACTREPLY = _descriptor.Descriptor(
  name='SubtractReply',
  full_name='calc.SubtractReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='n1', full_name='calc.SubtractReply.n1', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=125,
  serialized_end=152,
)


_MULTIPLYREQUEST = _descriptor.Descriptor(
  name='MultiplyRequest',
  full_name='calc.MultiplyRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='n1', full_name='calc.MultiplyRequest.n1', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='n2', full_name='calc.MultiplyRequest.n2', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=154,
  serialized_end=195,
)


_MULTIPLYREPLY = _descriptor.Descriptor(
  name='MultiplyReply',
  full_name='calc.MultiplyReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='n1', full_name='calc.MultiplyReply.n1', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=197,
  serialized_end=224,
)


_DIVIDEREQUEST = _descriptor.Descriptor(
  name='DivideRequest',
  full_name='calc.DivideRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='n1', full_name='calc.DivideRequest.n1', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='n2', full_name='calc.DivideRequest.n2', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=226,
  serialized_end=265,
)


_DIVIDEREPLY = _descriptor.Descriptor(
  name='DivideReply',
  full_name='calc.DivideReply',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='f1', full_name='calc.DivideReply.f1', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
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
  serialized_start=267,
  serialized_end=292,
)

DESCRIPTOR.message_types_by_name['AddRequest'] = _ADDREQUEST
DESCRIPTOR.message_types_by_name['AddReply'] = _ADDREPLY
DESCRIPTOR.message_types_by_name['SubtractRequest'] = _SUBTRACTREQUEST
DESCRIPTOR.message_types_by_name['SubtractReply'] = _SUBTRACTREPLY
DESCRIPTOR.message_types_by_name['MultiplyRequest'] = _MULTIPLYREQUEST
DESCRIPTOR.message_types_by_name['MultiplyReply'] = _MULTIPLYREPLY
DESCRIPTOR.message_types_by_name['DivideRequest'] = _DIVIDEREQUEST
DESCRIPTOR.message_types_by_name['DivideReply'] = _DIVIDEREPLY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AddRequest = _reflection.GeneratedProtocolMessageType('AddRequest', (_message.Message,), dict(
  DESCRIPTOR = _ADDREQUEST,
  __module__ = 'Calc_pb2'
  # @@protoc_insertion_point(class_scope:calc.AddRequest)
  ))
_sym_db.RegisterMessage(AddRequest)

AddReply = _reflection.GeneratedProtocolMessageType('AddReply', (_message.Message,), dict(
  DESCRIPTOR = _ADDREPLY,
  __module__ = 'Calc_pb2'
  # @@protoc_insertion_point(class_scope:calc.AddReply)
  ))
_sym_db.RegisterMessage(AddReply)

SubtractRequest = _reflection.GeneratedProtocolMessageType('SubtractRequest', (_message.Message,), dict(
  DESCRIPTOR = _SUBTRACTREQUEST,
  __module__ = 'Calc_pb2'
  # @@protoc_insertion_point(class_scope:calc.SubtractRequest)
  ))
_sym_db.RegisterMessage(SubtractRequest)

SubtractReply = _reflection.GeneratedProtocolMessageType('SubtractReply', (_message.Message,), dict(
  DESCRIPTOR = _SUBTRACTREPLY,
  __module__ = 'Calc_pb2'
  # @@protoc_insertion_point(class_scope:calc.SubtractReply)
  ))
_sym_db.RegisterMessage(SubtractReply)

MultiplyRequest = _reflection.GeneratedProtocolMessageType('MultiplyRequest', (_message.Message,), dict(
  DESCRIPTOR = _MULTIPLYREQUEST,
  __module__ = 'Calc_pb2'
  # @@protoc_insertion_point(class_scope:calc.MultiplyRequest)
  ))
_sym_db.RegisterMessage(MultiplyRequest)

MultiplyReply = _reflection.GeneratedProtocolMessageType('MultiplyReply', (_message.Message,), dict(
  DESCRIPTOR = _MULTIPLYREPLY,
  __module__ = 'Calc_pb2'
  # @@protoc_insertion_point(class_scope:calc.MultiplyReply)
  ))
_sym_db.RegisterMessage(MultiplyReply)

DivideRequest = _reflection.GeneratedProtocolMessageType('DivideRequest', (_message.Message,), dict(
  DESCRIPTOR = _DIVIDEREQUEST,
  __module__ = 'Calc_pb2'
  # @@protoc_insertion_point(class_scope:calc.DivideRequest)
  ))
_sym_db.RegisterMessage(DivideRequest)

DivideReply = _reflection.GeneratedProtocolMessageType('DivideReply', (_message.Message,), dict(
  DESCRIPTOR = _DIVIDEREPLY,
  __module__ = 'Calc_pb2'
  # @@protoc_insertion_point(class_scope:calc.DivideReply)
  ))
_sym_db.RegisterMessage(DivideReply)



_CALCULATOR = _descriptor.ServiceDescriptor(
  name='Calculator',
  full_name='calc.Calculator',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=295,
  serialized_end=518,
  methods=[
  _descriptor.MethodDescriptor(
    name='Add',
    full_name='calc.Calculator.Add',
    index=0,
    containing_service=None,
    input_type=_ADDREQUEST,
    output_type=_ADDREPLY,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Subtract',
    full_name='calc.Calculator.Subtract',
    index=1,
    containing_service=None,
    input_type=_SUBTRACTREQUEST,
    output_type=_SUBTRACTREPLY,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Multiply',
    full_name='calc.Calculator.Multiply',
    index=2,
    containing_service=None,
    input_type=_MULTIPLYREQUEST,
    output_type=_MULTIPLYREPLY,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Divide',
    full_name='calc.Calculator.Divide',
    index=3,
    containing_service=None,
    input_type=_DIVIDEREQUEST,
    output_type=_DIVIDEREPLY,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_CALCULATOR)

DESCRIPTOR.services_by_name['Calculator'] = _CALCULATOR

# @@protoc_insertion_point(module_scope)
