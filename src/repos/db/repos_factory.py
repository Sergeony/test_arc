from typing import Optional

from sqlalchemy import Session as SQLAlchemySession

import models
import consts
from . import base_repos, sqlalchemy


__all__ = [
    "DBReposFactory",
]


class DBReposFactory:
    """ Factory class to create DBRepo objects depending on  DAL.

    Spaces to improve:

        - Make a universal method to get Model Repos.

        - Provide Interface for this Factory as well.
    """
    def __init__(self, dal: consts.DAL = consts.DAL.SQLALCHEMY):
        if not isinstance(dal, consts.DAL):
            raise ValueError(f"Invalid DAL provided: {dal}")

        self._dal = dal

    def get_connection_repo(
            self,
            session: Optional[SQLAlchemySession] = None,
    ) -> base_repos.ConnectionBaseRepo:
        """ Provide a Connection Repo depending on _dal.

        Optionally, provide session to make queries within one session.
        """
        match self._dal:
            case consts.DAL.SQLALCHEMY:
                return sqlalchemy.ConnectionRepo(_model=models.Connection, session=session)
            case _:
                raise NotImplementedError(
                    f"Connection Repo is not implemented for {self._dal} DAL yet.",
                )

    def get_merchant_repo(
            self,
            session: Optional[SQLAlchemySession] = None,
    ) -> base_repos.MerchantBaseRepo:
        """ Provide a Merchant Repo depending on _dal.

        Optionally, provide session to make queries within one session.
        """
        match self._dal:
            case consts.DAL.SQLALCHEMY:
                return sqlalchemy.MerchantRepo(_model=models.Merchant, session=session)
            case _:
                raise NotImplementedError(
                    f"Merchant Repo is not implemented for {self._dal} DAL yet.",
                )

    def get_location_repo(
            self,
            session: Optional[SQLAlchemySession] = None,
    ) -> base_repos.LocationBaseRepo:
        """ Provide a Location Repo depending on _dal.

        Optionally, provide session to make queries within one session.
        """
        match self._dal:
            case consts.DAL.SQLALCHEMY:
                return sqlalchemy.LocationRepo(_model=models.Location, session=session)
            case _:
                raise NotImplementedError(
                    f"Location Repo is not implemented for {self._dal} DAL yet.",
                )
