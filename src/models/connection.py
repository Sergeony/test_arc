from .merchant import Merchant


__all__ = [
    "Connection",
]


class Connection:
    id: int
    fulfiller_id: int
    seller_id: int
    fulfiller: Merchant
    is_active: bool
