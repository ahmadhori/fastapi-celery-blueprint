from app.core.config import settings

# Broker settings.
broker_url = settings.CELERY_BROKER_URL

# List of modules to import when celery starts.
imports = ("app.worker.tasks",)

# Using the database to store task state and results.
result_backend = settings.CELERY_RESULT_BACKEND

# Store all task meta-data in the database.
result_extended = True  # pylint: disable=invalid-name
