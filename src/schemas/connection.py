from pydantic import BaseModel

from .common import *


__all__ = [
    "ConnectionBase",
    "ConnectionToggle",
    "Connection",
]


class ConnectionBase(BaseModel):
    fulfiller_id: int
    seller_id: int
    is_active: bool


class ConnectionToggle(BaseModel):
    id: int
    is_active: bool


class Connection(ConnectionBase, IdSchema):
    ...
