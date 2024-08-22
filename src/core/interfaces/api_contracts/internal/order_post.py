__all__ = [
    "OrderEndpoint",

    "OrderPostRequestBody",
    "OrderPostRequestQueryParams",

    "OrderPostSuccessResponseBody",
    "OrderPostSuccessResponseCode",

    "OrderPostFailedResponseBody",
    "OrderPostFailedResponseCode",
]


# -------------------------- REQUEST --------------------------


OrderEndpoint = "/order"


OrderPostRequestBody = {
    "items": [
        {
            "variant_id": str,
            "quantity": int,
        },
    ],
    "price": float,
    "currency": str,
    "delivery_method": str,
}


OrderPostRequestQueryParams = {
    "order_id": str,
}


# -------------------------- RESPONSE --------------------------


OrderPostSuccessResponseBody = {}
OrderPostSuccessResponseCode = 201

OrderPostFailedResponseBody = OrderPostSuccessResponseBody
OrderPostFailedResponseCode = 400
