from cassandra.cluster import Cluster
from redis import Redis
from mysql.connector.connection import MySQLConnection
from pymongo import MongoClient
from config.GetConfig import get_configs

CASSANDRA = 'Cassandra'
REDIS = 'Redis'
MONGO = 'MongoDB'
MYSQL = 'MySQL'
HOST = 'host'
PORT = 'port'
USER = 'user'
PASS = 'pass'
COMMA = ','
configs = None


# perhaps convert to constructor
def get_config():
    global configs
    configs = get_configs()
    # return config[datasource]


def get_cassandra():
    config = configs[CASSANDRA]
    hosts, port, user, password = get_params(config)
    hosts = hosts.strip().split(COMMA)
    cluster = Cluster(hosts, port)
    return cluster.connect()


def get_redis():
    config = configs[REDIS]
    hosts, port, user, password = get_params(config)
    if password:
        return Redis(hosts, password=password)
    else:
        return Redis(hosts)


def get_mysql(database):
    config = configs[MYSQL]
    hosts, port, user, password = get_params(config)
    return MySQLConnection(user=user, password=password, host=hosts, port=port, database=database)


def get_mongo():
    config = configs[MONGO]
    hosts, port, user, password = get_params(config)
    return MongoClient(host=hosts, port=port)


def get_params(config):
    return config[HOST], config[PORT], config[USER], config[PASS]
