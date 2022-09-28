from tasks import scheduler
from datetime import datetime, timedelta



eta = datetime.utcnow() + timedelta(seconds=10)
res = scheduler.apply_async((10,1),eta=eta)
print(res.get(timeout=10))