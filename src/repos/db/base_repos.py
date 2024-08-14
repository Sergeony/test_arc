from abc import ABC, abstractmethod
from typing import Generic, TypeVar

import schemas
import consts


__all__ = [
    "CommonBaseRepo",
    "MerchantBaseRepo",
    "LocationBaseRepo",
    "ConnectionBaseRepo",
]


_GetByIdArgs = TypeVar("_GetByIdArgs", bound=schemas.IdSchema)
_UpdateArgs = TypeVar('_UpdateArgs', bound=schemas.IdSchema)
_Entity = TypeVar('_Entity', bound=schemas.IdSchema)


class CommonBaseRepo(
    ABC,
    Generic[_GetByIdArgs, _UpdateArgs, _Entity],
):
    """ A common DB Repository.

    Although it inherits BaseRepo, but it still remains an interface by inheriting ABC.

    The main goals for this repo are:
        - make interface more clear.
            We use generics as (args) and (return types), which are bounded by corresponding common DB schemas.
            We restrict some primitive (args) and (return types) as well (E.g.: we define that for DB repos
                we use integer IDs only).

        - reduce duplicating queries for different models leaving only specific ones to implement.
    """
    @abstractmethod
    def __init__(
            self,
            _model: any,
            session: any = None,
            _engine: any = None,
    ):
        """ Define required Repo attributes:

            - We need a DB model to use it in all the queries.

            - We need a session to make quires with it to DB.
                By default, session will be None, but we can provide it
                to process several queries within one atomic DB transaction for example.

            - We need an engine to build a session if it's not passed
                or for tests purposes.
         """
        ...

    def get_all(self, skip: int = None, limit: int = None) -> list[_Entity]:
        """ Restrict skip -> int, limit -> int and return type -> list[_ModelRead]. """
        ...

    def get_by_id(self, id: int | str) -> _Entity:
        """ Restrict _id -> int and return type -> _ModelRead. """
        ...

    def create(self, args: _CreateArgs) -> _Entity:
        """ Restrict obj -> _ModelCreate and return type -> _ModelRead. """
        ...

    def update(self, args: _UpdateArgs) -> bool:
        """ Restrict obj -> _ModelUpdate and return type -> _ModelRead | None. """
        ...

    def delete(self, id: int | str) -> bool:
        """ Restrict _id -> int and return type -> bool | None. """
        ...


class MerchantBaseRepo(CommonBaseRepo, ABC):
    """ All specific to the merchant model methods go here... """

    @abstractmethod
    def get_platform(self, merchant_id: int) -> consts.EcomPlatform:
        """ Get merchant's platform only, omitting all the other fields. """
        ...


class LocationBaseRepo(CommonBaseRepo, ABC):
    """ All specific to the location model methods go here... """
    ...


class ConnectionBaseRepo(CommonBaseRepo, ABC):
    """ All specific to the connection model methods go here... """
    ...
