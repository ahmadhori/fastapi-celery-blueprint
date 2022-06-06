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
    return task


@router.get("/", response_model=schemas.CeleryTasks, status_code=200)
def get_tasks() -> Any:
    """
    Get Active And Schedule Celery Tasks
    """
    i = celery_app.control.inspect()
    try:
        active_tasks = list(i.active().values())[0]
    except AttributeError:
        active_tasks = []

    try:
        scheduled_tasks = list(i.scheduled().values())[0]
    except AttributeError:
        scheduled_tasks = []

    try:
        reserved_tasks = list(i.reserved().values())[0]
    except AttributeError:
        reserved_tasks = []

    return {
        "scheduled": scheduled_tasks,
        "running": active_tasks,
        "reserved": reserved_tasks,
    }
