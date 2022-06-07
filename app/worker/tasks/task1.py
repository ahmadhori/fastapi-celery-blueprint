import time

from app.schemas.celery import TaskResult
from app.worker.celery_app import celery_app
from app.worker.utils import update_task_progress


@celery_app.task(bind=True)
def test_task(self, job_to_do: str) -> dict:
    for i in range(10):
        message = f"I am still working on {job_to_do}, in loop number {i}"
        update_task_progress(self, current=i, total=10, message=message)

        time.sleep(5)
        print(message)

    task_result = self.AsyncResult(self.request.id).result
    return TaskResult(
        current=10,
        total=10,
        logs=task_result["logs"],
        final_status="task finished successfully",
    ).dict()
