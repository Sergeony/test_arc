from .....core import models
from .....core.interfaces.data_access.ecom_platform.i_location_repo import ILocationRepo
from ..client import process_request


__all__ = [
    'LocationRepo',
]


class LocationRepo(ILocationRepo):
    def __init__(self):
        self._process_request = process_request

    def get_location(self, external_location_id):
        warehouse = self._process_request(
            url=f"https://woo/wharehouse.com/warehouses/{external_location_id},",
            method="GET",
            body={"warehouse_id": external_location_id},
        )

        return models.Location(
            id=warehouse.warehouse_id,
            name=warehouse.name,
        )
