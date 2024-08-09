from ..base_repos import ConnectionBaseRepo
from .common import CommonRepo


__all__ = [
    "ConnectionRepo",
]


class ConnectionRepo(CommonRepo, ConnectionBaseRepo):
    """ A Connection Repo implementation powered by SQLAlchemy.

    This guy inherits SQLAlchemyCommonRepo with all common queries
        and implements the specific for DBConnectionRepo ones.

    As we can see there is nothing left to implement.
    But it should exist for universal-way structure and simplified future extending.
    """
    ...
