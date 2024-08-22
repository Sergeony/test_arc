from abc import ABC, abstractmethod

from src.core.models import Order


__all__ = [
    "IOrderService",
]



class IOrderService(ABC):
    @abstractmethod
    def create_order(self, _order: Order) -> Order:
        ...
