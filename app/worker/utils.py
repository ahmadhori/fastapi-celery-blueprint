from celery.app.task import Task


def update_task_progress(
    task: Task, current: int, total: int, message: str, state: str = "PROGRESS"
):
    """
    Update task progress
    """
    task_result = task.AsyncResult(task.request.id).result
    logs = []
    if task_result and isinstance(task_result, dict) and "logs" in task_result:
        logs = task_result["logs"]
        logs.append(message)
    else:
        logs = [message]

    task.update_state(
        state=state,
        meta={"current": current, "total": total, "logs": logs},
    )
