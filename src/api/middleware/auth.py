__all__ = [
    "get_user_id_from_jwt",
]


def get_user_id_from_jwt(jwt: any):
    return jwt.decode.get("user_id")
