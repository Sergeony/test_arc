from typing import Generic, TypeVar
from abc import ABC, abstractmethod

import schemas


__all__ = [
    "CommonBaseRepo",
]


""" Specific generics used to define the interface for all the EcomPlatform Repos.

We bound arguments for queries to have external_id fields (see: schemas.ExternalIdSchema).
"""
_UpdateArgs = TypeVar("_CreateArgs", bound=schemas.ExternalIdSchema)
_CreateArgs = TypeVar("_CreateArgs", bound=BaseSchema)
_Entity = TypeVar("_Entity", bound=schemas.ExternalIdSchema)


class CommonBaseRepo(
    ABC,
    Generic[_UpdateArgs, _CreateArgs, _Entity],
):
    @abstractmethod
    def __init__(self, shop_url: str, api_key: str):
        self.shop_url = shop_url
        self.api_key = api_key

    @abstractmethod
    def get_all(self, skip: any = None, limit: any = None) -> List[_Entity]:
        """ Keep it as an interface to be implemented in actual EcomPlatform Repo. """
        ...

    @abstractmethod
    def get_by_id(self, external_id: str) -> _Entity:
        """ Keep it as an interface to be implemented in actual EcomPlatform Repo. """
        ...

    @abstractmethod
    def create(self, args: _CreateArgs) -> _Entity:
        """ Keep it as an interface to be implemented in actual EcomPlatform Repo. """
        ...

    @abstractmethod
    def update(self, args: _UpdateArgs) -> bool:
        """ Keep it as an interface to be implemented in actual EcomPlatform Repo. """
        ...

    @abstractmethod
    def delete(self, external_id: str) -> bool:
        """ Keep it as an interface to be implemented in actual EcomPlatform Repo. """
        ...
