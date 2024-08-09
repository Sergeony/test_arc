from pydantic import BaseModel


__all__ = [
    "ExtraModelRead",
]


class ExtraModelRead(BaseModel):
    some_field: str
