__all__ = [
    "Response",
]


class Response(str):
    """ Just an example of universal-way reponse """
    def __init__(self, status_code: int, data: str, error):
        self.status_code = status_code
        self.data: str = data
        self.error: str = error

        self_response = {
            "data": self.data,
            "error": self.error,
            "status_code": self.status_code,
        }

        # possibly add some logging...

        super().__init__(self_response)
