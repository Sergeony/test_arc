from src.core.interfaces.services import IConnectionService


__all__ = [
    'ConnectionService',
]


class ConnectionService(IConnectionService):
    def create_connection(self):
        ...
