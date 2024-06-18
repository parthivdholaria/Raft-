# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: raft.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nraft.proto\x12\x04raft\"\"\n\x0fServeClientArgs\x12\x0f\n\x07request\x18\x01 \x01(\t\"X\n\x10ServeClientReply\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\t\x12\x11\n\tleader_id\x18\x02 \x01(\x05\x12\x0f\n\x07success\x18\x03 \x01(\x08\x12\x12\n\nstatusCode\x18\x04 \x01(\x05\"\xba\x01\n\x11\x41ppendEntriesArgs\x12\x0c\n\x04term\x18\x01 \x01(\x05\x12\x11\n\tleader_id\x18\x02 \x01(\x05\x12\x16\n\x0eprev_log_index\x18\x03 \x01(\x05\x12\x15\n\rprev_log_term\x18\x04 \x01(\x05\x12\x1f\n\x07\x65ntries\x18\x05 \x03(\x0b\x32\x0e.raft.LogEntry\x12\x15\n\rleader_commit\x18\x06 \x01(\x05\x12\x1d\n\x15leader_lease_duration\x18\x07 \x01(\x01\"G\n\x12\x41ppendEntriesReply\x12\x0c\n\x04term\x18\x01 \x01(\x05\x12\x0f\n\x07success\x18\x02 \x01(\x08\x12\x12\n\nstatusCode\x18\x03 \x01(\x05\"~\n\x0fRequestVoteArgs\x12\x0c\n\x04term\x18\x01 \x01(\x05\x12\x14\n\x0c\x63\x61ndidate_id\x18\x02 \x01(\x05\x12\x16\n\x0elast_log_index\x18\x03 \x01(\x05\x12\x15\n\rlast_log_term\x18\x04 \x01(\x05\x12\x18\n\x10leader_lease_end\x18\x05 \x01(\x05\"d\n\x10RequestVoteReply\x12\x0c\n\x04term\x18\x01 \x01(\x05\x12\x14\n\x0cvote_granted\x18\x02 \x01(\x08\x12\x12\n\nstatusCode\x18\x03 \x01(\x05\x12\x18\n\x10leader_lease_end\x18\x04 \x01(\x01\")\n\x08LogEntry\x12\x0f\n\x07\x63ommand\x18\x01 \x01(\t\x12\x0c\n\x04term\x18\x02 \x01(\x05\x32\xd3\x01\n\x0bRaftService\x12>\n\x0bServeClient\x12\x15.raft.ServeClientArgs\x1a\x16.raft.ServeClientReply\"\x00\x12\x44\n\rAppendEntries\x12\x17.raft.AppendEntriesArgs\x1a\x18.raft.AppendEntriesReply\"\x00\x12>\n\x0bRequestVote\x12\x15.raft.RequestVoteArgs\x1a\x16.raft.RequestVoteReply\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'raft_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_SERVECLIENTARGS']._serialized_start=20
  _globals['_SERVECLIENTARGS']._serialized_end=54
  _globals['_SERVECLIENTREPLY']._serialized_start=56
  _globals['_SERVECLIENTREPLY']._serialized_end=144
  _globals['_APPENDENTRIESARGS']._serialized_start=147
  _globals['_APPENDENTRIESARGS']._serialized_end=333
  _globals['_APPENDENTRIESREPLY']._serialized_start=335
  _globals['_APPENDENTRIESREPLY']._serialized_end=406
  _globals['_REQUESTVOTEARGS']._serialized_start=408
  _globals['_REQUESTVOTEARGS']._serialized_end=534
  _globals['_REQUESTVOTEREPLY']._serialized_start=536
  _globals['_REQUESTVOTEREPLY']._serialized_end=636
  _globals['_LOGENTRY']._serialized_start=638
  _globals['_LOGENTRY']._serialized_end=679
  _globals['_RAFTSERVICE']._serialized_start=682
  _globals['_RAFTSERVICE']._serialized_end=893
# @@protoc_insertion_point(module_scope)