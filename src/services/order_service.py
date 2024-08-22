from src.core.interfaces.services import IOrderService


__all__ = [
    'OrderService',
]


class OrderService(IOrderService):
    def create_order(self):
        ...
