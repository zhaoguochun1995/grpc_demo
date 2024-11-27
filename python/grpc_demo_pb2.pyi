from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class String(_message.Message):
    __slots__ = ("str",)
    STR_FIELD_NUMBER: _ClassVar[int]
    str: str
    def __init__(self, str: _Optional[str] = ...) -> None: ...
