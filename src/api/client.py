from .controllers import *
from .middleware import *


__all__ = [
    "app",
]


app = object()


app.middleware = [
    log_middleware,
]


app.routers = [
    connection_router,
]
