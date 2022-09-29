from worker.celery_worker import test_celery
from datetime import datetime, timedelta



eta = datetime.utcnow() + timedelta(seconds=10)
res = test_celery.apply_async([10],eta=eta)
print(res.get(timeout=10))