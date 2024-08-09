from enum import Enum


__all__ = [
    "EcomPlatform",
]


class EcomPlatform(Enum):
    SHOPIFY = 1
    WOOCOMMERCE = 2
    MAGENTO = 3
