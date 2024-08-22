from src.core.interfaces.api_contracts.public.connection import ConnectionPostRequest, ConnectionPostResponse

__all__ = [
    "router",
]


router = object()


@router.post()
def create_connection(connection: ConnectionPostRequest) -> ConnectionPostResponse:
    ...
