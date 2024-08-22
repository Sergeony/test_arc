from src.core.interfaces.repos.db import IConnectionRepo
from ....core import models
from .. import entities


__all__ = [
    "ConnectionRepo",
]


class ConnectionRepo(IConnectionRepo):
    def create(self, *args, **kwargs):
        connection_entity = entities.Connection(*args, **kwargs)
        return models.Connection(
            id=connection_entity.id,
            name=connection_entity.name,
        )
