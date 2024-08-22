from requests import request

from .utils import celery_app


__all__ = [
    "process_order_task",
]


@celery_app.task
def process_order_task(some_payload: any):
    response = request.post(
        url="api/v1/internal/orders",
        data=some_payload,
    )
