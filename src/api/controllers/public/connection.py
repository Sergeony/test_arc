from src.core.interfaces.api.public.connection import ConnectionPostRequest, ConnectionPostResponse

__all__ = [
    "router",
]


router = object()


@router.post()
def create_connection(connection: ConnectionPostRequest) -> ConnectionPostResponse:
    ...
