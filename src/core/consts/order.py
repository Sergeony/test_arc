from enum import Enum


__all__ = [
    "OrderStatus"
]


class OrderStatus(Enum):
    PAYMENT_ACCEPTED = 1
    IN_PROGRESS = 2
    DELIVERED = 3
    RETURN_REQUESTED = 4

    ...
