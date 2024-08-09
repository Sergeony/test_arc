from typing import TypeVar, Generic
from abc import ABC, abstractmethod

from pydantic import BaseModel


__all__ = [
    "MainBaseRepo",
]


""" Very common generics used to define the interface for MainBaseRepo.

We just bound all (the arguments) and (return entities) for queries to be Pydantic Models.
"""
_GetByIdArgs = TypeVar("_GetByIdArgs", bound=BaseModel)
_CreateArgs = TypeVar("_CreateArgs", bound=BaseModel)
_UpdateArgs = TypeVar("_UpdateArgs", bound=BaseModel)
_Entity = TypeVar("_Entity", bound=BaseModel)


class MainBaseRepo(
    ABC,
    Generic[_GetByIdArgs, _CreateArgs, _UpdateArgs, _Entity],
):
    """ A Base Repo for all the DALs / External services.

    Main purposes for this Repo are:
        - Define the least possible, but useful interface:
            - define the least number of queries required for each future Repo.
            - define the least useful signature for each query.
    """
    @abstractmethod
    def get_all(self, skip: str | int = None, limit: str | int = None) -> list[_Entity]:
        """ Common query for all the Repos to get a list of entities with pagination. """

    @abstractmethod
    def get_by_id(self, args: _GetByIdArgs) -> _Entity | None:
        """ Common query for all the Repos to get an Entity by ID. """
        ...

    @abstractmethod
    def create(self, args: _CreateArgs) -> _Entity:
        """ Common query for all the Repos to create an Entity. """
        ...

    @abstractmethod
    def update(self, args: _UpdateArgs) -> bool:
        """ Common query for all the Repos to update an Entity. Better to return any, because
        different Repos will probably respond different.
        """
        ...

    @abstractmethod
    def delete(self, args: _GetByIdArgs) -> bool:
        """ Common query for all the Repos to delete an Entity by ID. Better to return any, because
        different Repos will probably respond different.
        """
        ...
