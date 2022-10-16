# from datetime import datetime, timedelta
# import requests


# # eta = datetime.utcnow() + timedelta(seconds=60)
# # res = test_celery.apply_async([1000],eta=eta)

# body = {
#   "rrule": {
#     "dtstart": 1664871700,
#     "freq": 1,
#     "interval": 1,
#     "wkst": None,
#     "until": 1664870390,
#     "bysetpos": None,
#     "bymonth": None,
#     "bymonthday": None,
#     "byyearday": None,
#     "byweekno": None,
#     "byweekday": None,
#     "byhour": None,
#     "byminute": None,
#     "bysecond": None,
#     "cache": None
# },
#   "word": "string",
#   "auth":"lkfeo",
#   "inserted_id": ["jkdsiwjeoij"],
#   "classroom_id": "jkdsiwjeoij"

# }

# headers = {
#     'accept' : 'application/json',
#     'Content-Type': 'application/json'
#   }


# req = requests.post(
#             url="http://localhost:8000/tasks/remind_me",
#             headers=headers,
#             json=body
#         )

# print(req.content)


# #################################################################

from datetime import datetime
import time

mytime = time.time()
print(mytime+360)
print(datetime.utcfromtimestamp(mytime))


######################################################################

# kubectl get po
# kubectl logs web-5dbc755554-2jjtd --namespace=shruti
# kubectl apply -f kubemanifests.yaml --namespace=shruti
# kubectl proxy
# kubectl -n kube-system describe secret $(kubectl -n kube-system get secret | grep eks-admin | awk '{print $1}')
# kubectl create secret generic regcred --from-file=.dockerconfigjson=C:\Users\shruti\.docker\config.json --type=kubernetes.io/dockerconfigjson
# 127.0.0.1:8001/api/v1/namespaces/kubernetes-dashboard/services/https:kubernetes-dashboard:/proxy/#/overview?namespace=shruti

# VSCode live share :
# https://vscode.dev/liveshare/BB578078DC3603581B0936252867BCA4AF50