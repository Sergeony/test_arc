from abc import ABC, abstractmethod

__all__ = [
    "IConnectionService",
]


class IConnectionService(ABC):
    @abstractmethod
    def create_connection(self, ):
        ...
