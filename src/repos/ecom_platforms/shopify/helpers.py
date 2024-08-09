__all__ = [
    "read_query",
    "write_query",
    "custom_query",
]


# My point on this module is: make these graphQL queries with regular http requests
# would be easier to maintain.
# But it's not a big deal since it's encapsulated in one Ecom Repo package.


def read_query(credentials: dict, variables: dict = None, model: str = None, *args, **kwargs) -> any:
    ...


def write_query(credentials: dict, variables: dict = None, model: str = None, *args, **kwargs) -> any:
    ...


def custom_query(credentials: dict, variables: dict = None, model: str = None, *args, **kwargs) -> any:
    ...
