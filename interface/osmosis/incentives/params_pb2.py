# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: osmosis/incentives/params.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1fosmosis/incentives/params.proto\x12\x12osmosis.incentives\x1a\x14gogoproto/gogo.proto\"K\n\x06Params\x12\x41\n\x16\x64istr_epoch_identifier\x18\x01 \x01(\tB!\xf2\xde\x1f\x1dyaml:\"distr_epoch_identifier\"B4Z2github.com/osmosis-labs/osmosis/x/incentives/typesb\x06proto3')



_PARAMS = DESCRIPTOR.message_types_by_name['Params']
Params = _reflection.GeneratedProtocolMessageType('Params', (_message.Message,), {
  'DESCRIPTOR' : _PARAMS,
  '__module__' : 'osmosis.incentives.params_pb2'
  # @@protoc_insertion_point(class_scope:osmosis.incentives.Params)
  })
_sym_db.RegisterMessage(Params)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z2github.com/osmosis-labs/osmosis/x/incentives/types'
  _PARAMS.fields_by_name['distr_epoch_identifier']._options = None
  _PARAMS.fields_by_name['distr_epoch_identifier']._serialized_options = b'\362\336\037\035yaml:\"distr_epoch_identifier\"'
  _PARAMS._serialized_start=77
  _PARAMS._serialized_end=152
# @@protoc_insertion_point(module_scope)