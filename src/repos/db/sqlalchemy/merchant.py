import models
from ..base_repos import MerchantBaseRepo
from .common import CommonRepo


__all__ = [
    "MerchantRepo",
]


class MerchantRepo(CommonRepo, MerchantBaseRepo):
    """ A Merchant Repo implementation powered by SQLAlchemy.

    This guy inherits SQLAlchemyCommonRepo with all common queries
        and implements the specific for DBMerchantRepo ones.
    """
    def get_platform(self, merchant_id):
        return self.session.query(models.Merchant.id == merchant_id).first()
