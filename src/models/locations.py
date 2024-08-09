from sqlalchemy.orm import DeclarativeBase

from .merchant import Merchant


__all__ = [
    "Location",
]


class Location(DeclarativeBase):
    id: int
    external_id: str
    name: str
    merchant: Merchant
    merchant_id: int
