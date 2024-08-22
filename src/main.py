import uvicorn

from api import app
from tasks import celery_app
from config import ApiConfig, TasksConfig


if __name__ == '__main__':
    celery_app.main_worker([
        'worker',
        f'--loglevel={TasksConfig.LOG_LEVEL}',
        f"--concurrency={TasksConfig.CONCURRENCY}",
    ])

    uvicorn.run(app=app, host=ApiConfig.HOST, port=ApiConfig.PORT)
