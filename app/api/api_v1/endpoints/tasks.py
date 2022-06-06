from typing import Any

from fastapi import APIRouter

from app import schemas
from app.worker.celery_app import celery_app

router = APIRouter()


@router.post("/test-task/", response_model=schemas.AsyncTask, status_code=201)
def post_test_task(task_input: str) -> Any:
    """
    Post Test Task To Celery worker.
    """
    task = celery_app.send_task("app.worker.tasks.task1.test_task", args=[task_input])
    return {"msg": "Word received", "task_id": task.id}
