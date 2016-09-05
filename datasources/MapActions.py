import redis
import cassandra
import pymongo
import mysql


def create(conn, payload):
    if isinstance(conn, redis.client.Redis):
        pass
    elif isinstance(conn, cassandra.cluster.Cassandra):
        pass
    elif isinstance(conn, pymongo.MongoClient):
        pass
    elif isinstance(conn, mysql.connector.connection.MySQLConnection):
        pass


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
