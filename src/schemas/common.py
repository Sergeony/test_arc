from pydantic import BaseModel


__all__ = [
    "IdSchema",
    "ExternalIdSchema",
]


class ExternalIdSchema(BaseModel):
    external_id: str


class IdSchema(BaseModel):
    id: int
