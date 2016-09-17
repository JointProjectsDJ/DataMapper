from redis.client import Redis
from cassandra.cluster import Session
from pymongo.mongo_client import MongoClient
from mysql.connector.pooling import PooledMySQLConnection


# TODO Add else clauses to all methods to return error message in case sent server message does not match any configured instance
# TODO Add error checking for all files

def create(server, payload):
    """
    Create methods currently considered =>
    Redis: set, lpush and sadd.
    More to be added later. Goal is to cover all methods.
    """
    if isinstance(server, Redis):
        key = payload['key']
        value = payload['value']
        if isinstance(value, str):
            server.set(key, value)
        elif isinstance(value, list):
            server.lpush(key, value)
        elif isinstance(value, set):
            server.sadd(key, value)
    elif isinstance(server, Session):
        pass
    elif isinstance(server, MongoClient):
        pass
    elif isinstance(server, PooledMySQLConnection):
        pass


def read(server, payload):
    """
    Read methods currently considered =>
    Redis: get, lrange and smembers
    More to be added later. Goal is to cover all methods.
    """
    if isinstance(server, Redis):
        command = payload['command']
        key = payload['key']
        if command == 'LRANGE':
            start = payload['start']
            end = payload['end']
            return server.lrange(key, start, end)
        elif command == 'GET':
            return server.get(key)
        elif command == 'SMEMBERS':
            return server.smembers(key)
    elif isinstance(server, Session):
        pass
    elif isinstance(server, MongoClient):
        pass
    elif isinstance(server, PooledMySQLConnection):
        pass


def update(server, payload):
    """
    Update methods currently considered =>
    Redis: lset
    """
    if isinstance(server, Redis):
        command = payload['command'].upper()
        key = payload['key']
        if command == 'LSET':
            index = payload['index']
            value = ['value']
            server.lset(key, index, value)
    elif isinstance(server, Session):
        pass
    elif isinstance(server, MongoClient):
        pass
    elif isinstance(server, PooledMySQLConnection):
        pass


def delete(server, payload):
    """
    Delete methods currently considered =>
    Redis: del, lpop, srem, lrem
    """
    if isinstance(server, Redis):
        command = payload['command'].upper()
        key = payload['key']
        if command == 'DEL':
            server.delete(key)
        elif command == 'LPOP':
            server.lpop(key)
        elif command == 'SREM':
            value = payload['value']
            server.srem(key, value)
        elif command == 'LREM':
            value = payload['value']
            count = payload['count']
            server.lrem(key, value, count)
    elif isinstance(server, Session):
        pass
    elif isinstance(server, MongoClient):
        pass
    elif isinstance(server, PooledMySQLConnection):
        pass
