import time
from typing import Any

from app.worker.celery_app import celery_app


@celery_app.task(bind=True)
def test_task(self, word: str) -> Any:
    for i in range(10):
        self.update_state(
            state="PROGRESS",
            meta={"current": i, "total": 10, "status": f"currently in step {i}"},
        )
        time.sleep(5)
        print(f"I am still working on {word} in {i}")
    return {"status": "Import Partners Campaigns Job Completed"}
