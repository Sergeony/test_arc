from typing import Generic, TypeVar
from abc import ABC, abstractmethod

import schemas
from repos.main_base_repo import MainBaseRepo


__all__ = [
    "CommonBaseRepo",
]


""" Specific generics used to define the interface for all the EcomPlatform Repos.

We bound arguments for queries to have external_id fields (see: schemas.ExternalIdSchema).
"""
_GetByExternalIdArgs = TypeVar('_GetByExternalIdArgs', bound=schemas.ExternalIdSchema)


class CommonBaseRepo(
    MainBaseRepo,
    ABC,
    Generic[_GetByExternalIdArgs],
):
    @abstractmethod
    def __init__(self, shop_url: str, api_key: str):
        self.shop_url = shop_url
        self.api_key = api_key

    @abstractmethod
    def get_all(self, skip: any = None, limit: any = None):
        """ Keep it as an interface to be implemented in actual EcomPlatform Repo. """
        ...

    @abstractmethod
    def get_by_id(self, args: _GetByExternalIdArgs):
        """ Keep it as an interface to be implemented in actual EcomPlatform Repo. """
        ...

    @abstractmethod
    def create(self, args):
        """ Keep it as an interface to be implemented in actual EcomPlatform Repo. """
        ...

    @abstractmethod
    def update(self, args: _GetByExternalIdArgs):
        """ Keep it as an interface to be implemented in actual EcomPlatform Repo. """
        ...

    @abstractmethod
    def delete(self, args):
        """ Keep it as an interface to be implemented in actual EcomPlatform Repo. """
        ...
