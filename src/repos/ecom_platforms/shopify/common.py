from ..base_repos import CommonBaseRepo


__all__ = [
    "CommonRepo",
]


class CommonRepo(CommonBaseRepo):
    def __init__(self, shop_url: str, api_key: str):
        """ Specific for Shopify Repo initialization. """
        super().__init__(shop_url, api_key)

        self.credentials = {
            "shop_url": shop_url,
            "api_key": api_key,
        }

    def get_all(self, skip=None, limit=None):
        raise NotImplementedError()

    def get_by_id(self, args):
        raise NotImplementedError()

    def create(self, args):
        raise NotImplementedError()

    def update(self, args):
        raise NotImplementedError()

    def delete(self, args):
        raise NotImplementedError()
