from aiohttp import ClientSession


__all__ = [
    "request",
]


BASE_API_URL = "https://{shop_url}/api/{endpoint}"


# My suggestion is to move such things to CommonRepo of corresponding platform
# But it's not a big deal since it's encapsulated in one Ecom repo package


async def request(
        credentials: dict[str, str],
        endpoint: str,
        method: str = "POST",
        body: dict[str, any] | None = None,
) -> dict[str, any]:
    """ A Specific for WooCommerce API way to manage data access. """
    url = BASE_API_URL.format(shop_url=credentials.get("shop_url"), endpoint=endpoint)
    headers = {
        "Content-Type": "application/json",
        "Api-Key": credentials.get("api_key"),
    }
    async with ClientSession() as session:
        async with session.request(method=method, url=url, headers=headers, json=body) as response:
            response.raise_for_status()
            return await response.json()
