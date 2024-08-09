from pydantic import BaseModel

from .common import *


__all__ = [
    "LocationBase",
    "LocationEcom",
    "Location",
]


class LocationBase(BaseModel):
    name: str
    merchant_id: int


class LocationEcom(LocationBase, ExternalIdSchema):
    ...


class Location(LocationEcom, IdSchema):
    ...
