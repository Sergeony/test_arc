__all__ = [
    "process_request",
]


def process_request(url, method, body=None, query_params=None):
    with aiohttp.request(
            url=url,
            method=method,
            body=body,
            params=query_params,
    ) as response:
        match response.status_code:
            case 200:
                return response.json()
            case 400:
                return EcomBadRequestError(response)
            case 403:
                return EcomInvalidCredsError(response)
            case 404:
                return EcomEntityNotFoundError(response)
            case 503:
                return EcomIsUnavailableError(response)
            case _:
                return EcomUnrecognizedError(response)
