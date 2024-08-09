from typing import Type

from consts import EcomPlatform
from repos import db
from . import base_repos, shopify, woocommerce


class ReposFactory:
    """ Provide Platform Repos depending on the merchant platform.
    """
    def __init__(
            self,
            merchant_id: int,
            get_db_repos_factory: Type[db.DBReposFactory] = db.DBReposFactory,
    ):
        db_repo_factory = get_db_repos_factory()

        db_merchant_repo = db_repo_factory.get_merchant_repo()

        self.platform = db_merchant_repo.get_platform(merchant_id=merchant_id)

        if not isinstance(self.platform, EcomPlatform):
            raise ValueError(f"Invalid ecom platform: {self.platform}")

    def get_location_repo(self) -> base_repos.CommonBaseRepo:
        match self.platform:
            case EcomPlatform.SHOPIFY:
                return shopify.LocationRepo
            case EcomPlatform.WOOCOMMERCE:
                return woocommerce.LocationRepo
            case EcomPlatform.MAGENTO:
                """ Raise an error is some platform's Repo is under development.
                """
                raise NotImplementedError(f"LocationRepo has not been implemented for {self.platform} yet.")
