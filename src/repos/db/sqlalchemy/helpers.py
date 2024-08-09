from sqlalchemy import create_engine

from config import DBConfig


__all__ = [
    "engine",
]


engine = create_engine(
    f'postgresql://'
    f'{DBConfig.PSQL_USER}:{DBConfig.PSQL_PASS}'
    f'@{DBConfig.PSQL_HOST}:{DBConfig.PSQL_PORT}/'
    f'{DBConfig.PSQL_DB}',
    pool_size=100,
    max_overflow=100,
)
