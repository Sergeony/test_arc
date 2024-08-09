from enum import Enum


__all__ = [
    "DBConfig",
]


class DBConfig(Enum):
    PSQL_USER = ""
    PSQL_PASS = ""
    PSQL_HOST = ""
    PSQL_PORT = ""
    PSQL_DB = ""
