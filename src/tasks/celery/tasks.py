import aiohttp

from .utils import celery_app
from ...config import ApiConfig
from ...core.interfaces.api_contracts.internal import OrderEndpoint, OrderPostRequestBody


__all__ = [
    "process_order_task",
]


@celery_app.task
def process_order_task(some_payload: OrderPostRequestBody) -> None:
    """ This task just triggers order processing in the background.

    This way, celery can be even placed on a different server and call out main server api
    """
    aiohttp.post(
        url=f"{ApiConfig.HOST}:{ApiConfig.PORT}/{OrderEndpoint}",
        data=some_payload,
    )
