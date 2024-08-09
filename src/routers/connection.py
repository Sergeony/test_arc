from services import AbstractConnections, Connections
from .response import Response

__all__ = [
    "ConnectionRouter",
]


class ConnectionRouter:
    @staticmethod
    def accept_connection(
            request: any,
            connection_id: int,
            connections_service: AbstractConnections = Connections(),
    ):
        # possibly make some stuf with cookies, headers, metadata, etc...
        request.do_smth()

        result = connections_service.accept_connection(connection_id=connection_id)

        # return a universal-way response
        return Response(data=result, status_code=200, error=None)

    @staticmethod
    def toggle_connection(
            request: any,
            connection_id: int,
            new_status: bool = None,
            connections_service: AbstractConnections = Connections(),
    ):
        result = connections_service.toggle_connection(connection_id=connection_id, new_status=new_status)

        return Response(data=result, status_code=200, error=None)
