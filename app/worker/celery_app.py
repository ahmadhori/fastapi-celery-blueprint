from celery import Celery


celery_app = Celery('app.worker')
DEFAULT_CONFIG = 'app.worker.celeryconfig'
celery_app.config_from_object(DEFAULT_CONFIG)
