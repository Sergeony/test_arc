from src.core.consts.ecom_platform import EcomPlatform
from src.data_access.ecom_platforms import shopify


__all__ = [
    "EcomPlatformReposFactory",
]


class EcomPlatformReposFactory:
    def __init__(self, platform_id: int):
        if platform_id not in list(map(int, EcomPlatform)):
            raise ValueError(f"Platform ID {platform_id} not in {EcomPlatform}")

        self._platform = platform_id

    def get_location_repo(self):
        match self._platform:
            case EcomPlatform.SHOPIFY:
                return shopify.LocationRepo
            case EcomPlatform.WOOCOMMERCE:
                raise NotImplementedError()
