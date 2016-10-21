from rest_api import app
from workers.invoke_workers import Workers

data = {
      "source": "mongo",
      "payload" : {'collection': 'test', 'filter': {}},
      "query_type" : "read"
}

mapper_entity = app.create_mapper_entity(data['source'], data['payload'], data['query_type'])
workers = Workers()
a = workers.invoke(mapper_entity)
print(a)