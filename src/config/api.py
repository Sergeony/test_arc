from dataclasses import dataclass

from .env import env


@dataclass
class ApiConfig:
    PORT = env.get("API_PORT")
    DOMAIN = env.get("API_URL")
    HOST = env.get("API_HOST")
