from abc import ABC

from .... import models


__all__ = [
    'ILocationRepo',
]


class ILocationRepo(ABC):
    def get_by_id(self, location_id: int) -> models.Location:
        ...
