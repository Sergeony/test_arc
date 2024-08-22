from .....core import models
from .....core.interfaces.data_access.ecom_platform.i_location_repo import ILocationRepo


__all__ = [
    'LocationRepo',
]


class LocationRepo(ILocationRepo):
    def __init__(self):
        ...

    def get_location(self, location_id):
        return models.Location(
            id=location_id,
        )
