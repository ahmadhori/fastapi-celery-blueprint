from app.worker.celery_app import celery_app


@celery_app.task(acks_late=True)
def test_task(word: str) -> str:
    return f"test task return {word}"
