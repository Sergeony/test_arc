from fastapi import Depends

from ....tasks.celery import process_order_task


__all__ = [
    "order_create",
]


router = object(prefix="/order")


@router.post("/create")
def order_create(
        payload: any,
        order_create_task: Depends[process_order_task.delay],
):
    order_create_task(**payload)
    return 200
