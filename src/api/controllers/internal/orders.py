from fastapi import Depends, JsonResponse

from ....core import models
from ....core.interfaces import api
from ....services.order_service import OrderService
from ...middleware import auth


__all__ = [
    "order_router",
]


order_router = object(prefix=api.OrderEndpoint)


@order_router.post("/")
def create_order(
        payload: api.OrderPostRequestBody,
        user_id: Depends[auth.get_user_id_from_jwt],
        q: api.OrderPostRequestQueryParams,
        order_service: Depends[OrderService],
):
    """
    """
    result = order_service.create_order(
        _order=models.Order(**payload, **q, user_id=user_id)
    )

    if result is False:
        return JsonResponse(
            data=api.OrderPostFailedResponseBody,
            status=api.OrderPostFailedResponseCode,
        )

    body: api.OrderPostSuccessResponseBody = result.json()

    return JsonResponse(
        data=body,
        status=api.OrderPostSuccessResponseCode,
    )
