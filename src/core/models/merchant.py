from ..consts.ecom_platform import EcomPlatform


__all__ = [
    "Merchant",
]


class Merchant:
    def create(self, *args, **kwargs):
        platform_id = kwargs.get("platform_id")
        if platform_id not in list(map(int, EcomPlatform)):
            return False

        self.platform = EcomPlatform[platform_id]
