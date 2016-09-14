import redis
import cassandra
import pymongo
import mysql

from datasources import MapCassandra
from datasources import MapRedis
from datasources import MapMySql
from datasources import MapMongo


def create(conn, payload):
    if isinstance(conn, redis.client.Redis):
        MapRedis()
    elif isinstance(conn, cassandra.cluster.Cassandra):
        MapCassandra()
    elif isinstance(conn, pymongo.MongoClient):
        MapMongo()
    elif isinstance(conn, mysql.connector.connection.MySQLConnection):
        MapMySql()


def read(conn, payload):
    if isinstance(conn, redis.client.Redis):
        pass
    elif isinstance(conn, cassandra.cluster.Cassandra):
        pass
    elif isinstance(conn, pymongo.MongoClient):
        pass
    elif isinstance(conn, mysql.connector.connection.MySQLConnection):
        pass


def update(conn, payload):
    if isinstance(conn, redis.client.Redis):
        pass
    elif isinstance(conn, cassandra.cluster.Cassandra):
        pass
    elif isinstance(conn, pymongo.MongoClient):
        pass
    elif isinstance(conn, mysql.connector.connection.MySQLConnection):
        pass


def delete(conn, payload):
    if isinstance(conn, redis.client.Redis):
        pass
    elif isinstance(conn, cassandra.cluster.Cassandra):
        pass
    elif isinstance(conn, pymongo.MongoClient):
        pass
    elif isinstance(conn, mysql.connector.connection.MySQLConnection):
        pass
