from cassandra.cluster import Cluster
from redis import Redis, ConnectionPool
from mysql.connector.pooling import MySQLConnectionPool, CNX_POOL_MAXSIZE
from pymongo import MongoClient
from config.GetConfig import get_configs


# Pool initialization to be performed in startup script

class Pool:
    CASSANDRA = 'Cassandra'
    REDIS = 'Redis'
    MONGO = 'MongoDB'
    MYSQL = 'MySQL'
    HOST = 'host'
    PORT = 'port'
    USER = 'user'
    PASS = 'pass'
    DATABASE = 'database'
    KEYSPACE = 'keyspace'
    COMMA = ','
    configs = None
    redisPool = None
    mongoPool = None
    cassandraPool = None
    mysqlPool = None
    keyspace = None

    def __init__(self):
        # global configs
        self.configs = get_configs()
        self.create_cassandra()
        # self.create_redis()
        self.create_mongo()
        # self.create_mysql()

    def get_params(self, config):
        # global HOST, PORT, USER, PASS
        return config[self.HOST], config[self.PORT], config[self.USER], config[self.PASS]

    # perform exception handling with logging

    def create_cassandra(self):
        # global CASSANDRA, COMMA, KEYSPACE, cassandraPool, keyspace
        config = self.configs[self.CASSANDRA]
        hosts, port, user, password = self.get_params(config)
        hosts = hosts.strip().split(self.COMMA)
        self.keyspace = config[self.KEYSPACE]
        self.cassandraPool = Cluster(hosts, port)

    def create_redis(self):
        # global REDIS, redisPool
        config = self.configs[self.REDIS]
        hosts, port, user, password = self.get_params(config)
        self.redisPool = ConnectionPool(host=hosts, port=port)

    def create_mysql(self, database=None):
        # global MYSQL, DATABASE, mysqlPool
        config = self.configs[self.MYSQL]
        hosts, port, user, password = self.get_params(config)
        if not database:
            database = config[self.DATABASE]
        dbconfig = {'database': database,
                    'user': user,
                    'password': password,
                    'host': hosts,
                    'port': port}
        self.mysqlPool = MySQLConnectionPool(pool_size=CNX_POOL_MAXSIZE, pool_name='POOL', **dbconfig)

    def create_mongo(self):
        # global MONGO, mongoPool
        config = self.configs[self.MONGO]
        hosts, port, user, password = self.get_params(config)
        self.mongoPool = MongoClient(host=hosts, port=port)

    def get_redis(self):
        return Redis(connection_pool=self.redisPool)

    def get_cassandra(self):
        return self.cassandraPool.connect(self.keyspace)

    def get_mysql(self):
        return self.mysqlPool.get_connection()

    def get_mongo(self):
        return self.mongoPool

        # def __del__(self):
        #     global redisPool, mongoPool, mysqlPool, cassandraPool
        #     self.redisPool.disconnect()
        #     self.mongoPool.close()
        #     self.mysqlPool.close()
        #     self.cassandraPool.shutdown()
