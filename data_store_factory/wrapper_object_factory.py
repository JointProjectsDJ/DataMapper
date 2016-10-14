from startup import Startup
from datasources import MapRedis, MapMySql, MapCassandra, MapMongo, MapActions


class WrapperFactory:
    def __init__(self):
        self.conn_pool = Startup.conn_pool
        self.server = None

    def set_server_object(self, source):
        if source == "cassandra":
            self.server = MapCassandra.MapCassandra(self.conn_pool).server
        elif source == "redis":
            self.server = MapRedis.MapRedis(self.conn_pool).server
        elif source == "mongo":
            self.server = MapMongo.MapMongo(self.conn_pool).server
        elif source == "mysql":
            self.server = MapMySql.MapMySql(self.conn_pool).server

    def invoke_mapper_action(self, payload, query_type):
        if query_type == "create":
            return MapActions.create(self.server, payload)
        elif query_type == "read":
            return MapActions.read(self.server, payload)
        elif query_type == "delete":
            return MapActions.delete(self.server, payload)
        elif query_type == "update":
            return MapActions.update(self.server, payload)

    def process(self,MapperEntity):
        self.set_server_object(MapperEntity.source)
        return self.invoke_mapper_action(MapperEntity.payload,MapperEntity.query_type)