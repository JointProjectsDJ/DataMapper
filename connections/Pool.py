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
    COMMA = ','
    configs = None
    redisPool = None
    mongoPool = None
    cassandraPool = None
    mysqlPool = None

    def __init__(self):
        global configs
        configs = get_configs()
        self.create_cassandra()
        self.create_redis()
        self.create_mongo()
        self.create_mysql()

    def get_params(self, config):
        global HOST, PORT, USER, PASS
        return config[HOST], config[PORT], config[USER], config[PASS]

    # perform exception handling with logging

    def create_cassandra(self):
        global CASSANDRA, COMMA, cassandraPool
        config = configs[CASSANDRA]
        hosts, port, user, password = self.get_params(config)
        hosts = hosts.strip().split(COMMA)
        cassandraPool = Cluster(hosts, port)

    def create_redis(self):
        global REDIS, redisPool
        config = configs[REDIS]
        hosts, port, user, password = self.get_params(config)
        redisPool = ConnectionPool(host=hosts, port=port)

    def create_mysql(self, database=None):
        global MYSQL, DATABASE, mysqlPool
        config = configs[MYSQL]
        hosts, port, user, password = self.get_params(config)
        if not database:
            database = config[DATABASE]
        dbconfig = {'database': database,
                    'user': user,
                    'password': password,
                    'host': hosts,
                    'port': port}
        mysqlPool = MySQLConnectionPool(pool_size=CNX_POOL_MAXSIZE, pool_name='POOL', **dbconfig)

    def create_mongo(self):
        global MONGO, mongoPool
        config = configs[MONGO]
        hosts, port, user, password = self.get_params(config)
        mongoPool = MongoClient(host=hosts, port=port)

    def get_redis(self):
        return Redis(connection_pool=redisPool)

    def get_cassandra(self):
        return cassandraPool.connect()

    def get_mysql(self):
        return mysqlPool.get_connection()

    def get_mongo(self):
        return mongoPool

    def __del__(self):
        redisPool.disconnect()
        mongoPool.close()
        mysqlPool.close()
        cassandraPool.shutdown()
