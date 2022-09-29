from app.worker.celery_worker import test_celery
from datetime import datetime, timedelta



eta = datetime.utcnow() + timedelta(seconds=60)
res = test_celery.apply_async([1000],eta=eta)
