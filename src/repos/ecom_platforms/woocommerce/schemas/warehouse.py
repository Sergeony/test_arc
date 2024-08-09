from pydantic import BaseModel


__all__ = [
    "WarehouseCreate",
    "WarehouseRead",
]


class WarehouseCreate(BaseModel):
    name: str


class WarehouseRead(WarehouseCreate):
    warehouse_id: str
