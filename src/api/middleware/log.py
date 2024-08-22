__all__ = [
    "log_middleware",
]


def log_middleware(request):
    ...
    result = request()
    ...

    return result
