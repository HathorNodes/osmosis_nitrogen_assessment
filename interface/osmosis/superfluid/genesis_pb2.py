# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: osmosis/superfluid/genesis.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
from osmosis.superfluid import superfluid_pb2 as osmosis_dot_superfluid_dot_superfluid__pb2
from osmosis.superfluid import params_pb2 as osmosis_dot_superfluid_dot_params__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n osmosis/superfluid/genesis.proto\x12\x12osmosis.superfluid\x1a\x14gogoproto/gogo.proto\x1a#osmosis/superfluid/superfluid.proto\x1a\x1fosmosis/superfluid/params.proto\"\xbd\x02\n\x0cGenesisState\x12\x30\n\x06params\x18\x01 \x01(\x0b\x32\x1a.osmosis.superfluid.ParamsB\x04\xc8\xde\x1f\x00\x12\x44\n\x11superfluid_assets\x18\x02 \x03(\x0b\x32#.osmosis.superfluid.SuperfluidAssetB\x04\xc8\xde\x1f\x00\x12]\n\x1bosmo_equivalent_multipliers\x18\x03 \x03(\x0b\x32\x32.osmosis.superfluid.OsmoEquivalentMultiplierRecordB\x04\xc8\xde\x1f\x00\x12V\n\x15intermediary_accounts\x18\x04 \x03(\x0b\x32\x31.osmosis.superfluid.SuperfluidIntermediaryAccountB\x04\xc8\xde\x1f\x00\x42\x37Z5github.com/osmosis-labs/osmosis/v7/x/superfluid/typesb\x06proto3')



_GENESISSTATE = DESCRIPTOR.message_types_by_name['GenesisState']
GenesisState = _reflection.GeneratedProtocolMessageType('GenesisState', (_message.Message,), {
  'DESCRIPTOR' : _GENESISSTATE,
  '__module__' : 'osmosis.superfluid.genesis_pb2'
  # @@protoc_insertion_point(class_scope:osmosis.superfluid.GenesisState)
  })
_sym_db.RegisterMessage(GenesisState)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'Z5github.com/osmosis-labs/osmosis/v7/x/superfluid/types'
  _GENESISSTATE.fields_by_name['params']._options = None
  _GENESISSTATE.fields_by_name['params']._serialized_options = b'\310\336\037\000'
  _GENESISSTATE.fields_by_name['superfluid_assets']._options = None
  _GENESISSTATE.fields_by_name['superfluid_assets']._serialized_options = b'\310\336\037\000'
  _GENESISSTATE.fields_by_name['osmo_equivalent_multipliers']._options = None
  _GENESISSTATE.fields_by_name['osmo_equivalent_multipliers']._serialized_options = b'\310\336\037\000'
  _GENESISSTATE.fields_by_name['intermediary_accounts']._options = None
  _GENESISSTATE.fields_by_name['intermediary_accounts']._serialized_options = b'\310\336\037\000'
  _GENESISSTATE._serialized_start=149
  _GENESISSTATE._serialized_end=466
# @@protoc_insertion_point(module_scope)
