from app.worker.celery_app import celery_app
import time


@celery_app.task(acks_late=True)
def test_task(word: str) -> str:
    for _ in range(4):
        time.sleep(5)
        print(f"I am still working on {word}")
    return f"test task return {word}"
