from abc import abstractmethod
from typing import Type

import schemas
from celery import shared_task

from repos import db, ecom_platforms


__all__ = [
    "AbstractConnections",
    "Connections",
]


SHARED_LOCATION_PATTERN = "Spaceshelf/{}"


class AbstractConnections:
    def __init__(
            self,
            db_repo_factory: Type[db.DBReposFactory] = db.DBReposFactory,
    ):
        self.db_repo_factory = db_repo_factory()

    @abstractmethod
    def accept_connection(
            self,
            connection_id: int,
    ) -> bool:
        raise NotImplementedError

    @abstractmethod
    def toggle_connection(
            self,
            connection_id: int,
            new_status: bool,
    ) -> bool:
        raise NotImplementedError


class Connections(AbstractConnections):

    @shared_task
    def accept_connection(
            self,
            connection_id,
            ecom_platform_factory: Type[ecom_platforms.ReposFactory] = ecom_platforms.ReposFactory,
    ):
        connection_repo = self.db_repo_factory.get_connection_repo()

        connection = connection_repo.get_by_id(args=connection_id)

        fulfiller_ecom_platform_factory = ecom_platform_factory(merchant_id=connection.fulfiller_id)
        fulfiller_location_repo = fulfiller_ecom_platform_factory.get_location_repo()

        ecom_location = fulfiller_location_repo.create(
            args=schemas.LocationBase(name=SHARED_LOCATION_PATTERN.format(connection.fulfiller.name)),
        )
        if ecom_location:
            db_location_repo = self.db_repo_factory.get_location_repo()
            db_location_repo.create(args=ecom_location)
        return False

    def toggle_connection(self, connection_id, new_status):
        connection_repo = self.db_repo_factory.get_connection_repo()

        return connection_repo.update(
            args=schemas.ConnectionToggle(
                id=connection_id,
                is_active=new_status,
            )
        )
