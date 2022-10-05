from datetime import datetime, timedelta
import requests


# eta = datetime.utcnow() + timedelta(seconds=60)
# res = test_celery.apply_async([1000],eta=eta)

body = {
  "rrule": {
    "dtstart": 1664871700,
    "freq": 1,
    "interval": 1,
    "wkst": None,
    "until": 1664870390,
    "bysetpos": None,
    "bymonth": None,
    "bymonthday": None,
    "byyearday": None,
    "byweekno": None,
    "byweekday": None,
    "byhour": None,
    "byminute": None,
    "bysecond": None,
    "cache": None
},
  "word": "string",
  "auth":"lkfeo",
  "inserted_id": "jkdsiwjeoij"
}

headers = {
    'accept' : 'application/json',
    'Content-Type': 'application/json'
  }


req = requests.post(
            url="http://localhost:5000/tasks/remind_me",
            headers=headers,
            json=body
        )

print(req.content)

