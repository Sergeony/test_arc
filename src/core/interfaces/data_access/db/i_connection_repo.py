from abc import ABC, abstractmethod


__all__ = [
    "IConnectionRepo",
]


class IConnectionRepo(ABC):
    @abstractmethod
    def create(self, *args, **kwargs):
        ...
