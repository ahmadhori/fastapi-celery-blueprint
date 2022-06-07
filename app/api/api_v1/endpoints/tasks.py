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
    Get Active And Schedule Celery Tasks (Finished tasks are not included).
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


@router.get("/{task_id}", response_model=schemas.AsyncTask, status_code=200)
def get_task_per_id(task_id: str) -> Any:
    """
    Get Celery Task By Task ID.\n
    Result backend will be queried to get the results, and if
    the task is not found it will return a task in PENDING state.
    """
    task = celery_app.AsyncResult(task_id)
    return task
