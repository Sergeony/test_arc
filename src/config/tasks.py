from dataclasses import dataclass
from .env import env


__all__ = [
    "TasksConfig",
]


@dataclass
class TasksConfig:
    LOG_LEVEL: str = env("LOG_LEVEL", "INFO")
    CONCURRENCY: int = env("WORKERS_COUNT", 4)
