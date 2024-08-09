from ..base_repos import LocationBaseRepo
from .common import CommonRepo


__all__ = [
    "LocationRepo",
]


class LocationRepo(CommonRepo, LocationBaseRepo):
    """ A Location Repo implementation powered by SQLAlchemy.

    This guy inherits SQLAlchemyCommonRepo with all common queries
        and implements the specific for DBLocationRepo ones.

    As we can see there is nothing left to implement.
    But it should exist for universal-way structure and simplified future extending.
    """
    ...
