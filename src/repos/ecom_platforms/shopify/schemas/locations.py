from pydantic import BaseModel


__all__ = [
    "LocationCreate",
    "LocationRead",
]


class LocationCreate(BaseModel):
    name: str


class LocationRead(LocationCreate):
    location_id: str
