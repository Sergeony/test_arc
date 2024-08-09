from enum import Enum


__all__ = [
    "DAL",
]


# DAL (Data Access Level) is the way we interact with DB
class DAL(Enum):
    SQLALCHEMY = "SQLALCHEMY"

    """ Here could also be other DALs

    The main purposes for it are:

        - We can easily move from one DAL to another.

            It might be helpful if a new non-backward compatible ORM version releases:
                SQLALCHEMY2 = "SQLALCHEMY2"

            Or if, at some point, we discover that raw SQL queries with PGSQL are more effective for us:
                PGSQL = "PGSQL"

            Of we gonna change to use some ODM for MongoDB or smth...
                MONGODB = "MONGODB"

        - It should exist to reach Dependency Inversion principle and make codebase easier to test.
    """
