from redis.client import Redis
from cassandra.cluster import Session
from pymongo.mongo_client import MongoClient
from mysql.connector.pooling import PooledMySQLConnection
from startup.Startup import conn_pool


# TODO Add else clauses to all methods to return error message in case sent server message does not match any configured instance
# TODO Add error checking for all files
# TODO Add check for multiple queries to mysql and then add multi=True

def create(server, payload):
    """
    Create methods currently considered =>
    Redis: set, lpush and sadd.
    Mongo: insert_one, insert_many
    More to be added later. Goal is to cover all methods.
    """
    if isinstance(server, Redis):
        key = payload['key']
        value = payload['value']
        if isinstance(value, str):
            return server.set(key, value)
        elif isinstance(value, list):
            return server.lpush(key, value)
        elif isinstance(value, set):
            return server.sadd(key, value)
    elif isinstance(server, Session):
        query = payload['query']
        if 'params' in payload:
            params = payload['params']
            return server.execute(query, params)
        else:
            return server.execute(query)
    elif isinstance(server, MongoClient):
        collection = payload['collection']
        doc = payload['doc']
        if 'database' in payload:
            database = payload['database']
            db = server[database]
        else:
            database = conn_pool.configs['MongoDB']['database']
            db = server[database]
        col = db[collection]
        if isinstance(doc, list):
            return col.insert_many(doc).inserted_ids
        else:
            return col.insert_one(doc).inserted_id
    elif isinstance(server, PooledMySQLConnection):
        cursor = server.cursor(buffered=True)
        query = payload['query']
        if 'params' in payload:
            params = payload['params']
            cursor.execute(query, params)
            server.commit()
        else:
            cursor.execute(query)
            server.commit()
        cursor.close()
    else:
        pass


def read(server, payload):
    """
    Read methods currently considered =>
    Redis: get, lrange and smembers
    Mongo: find
    More to be added later. Goal is to cover all methods.
    """
    if isinstance(server, Redis):
        command = payload['command'].upper()
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
        query = payload['query']
        if 'params' in payload:
            params = payload['params']
            rs = [r for r in server.execute(query, params)]
        else:
            rs = [r for r in server.execute(query)]
        return rs
    elif isinstance(server, MongoClient):
        collection = payload['collection']
        filterm = payload['filter']
        if 'database' in payload:
            database = payload['database']
            db = server[database]
        else:
            database = conn_pool.configs['MongoDB']['database']
            db = server[database]
        col = db[collection]
        if len(filterm) == 0:
            rs = [doc for doc in col.find()]
            return rs
        else:
            rs = [doc for doc in col.find(filterm)]
            return rs
    elif isinstance(server, PooledMySQLConnection):
        cursor = server.cursor(buffered=True)
        query = payload['query']
        if 'params' in payload:
            params = payload['params']
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        rs = [r for r in cursor]
        cursor.close()
        return rs
    else:
        pass


def update(server, payload):
    """
    Update methods currently considered =>
    Redis: lset
    Mongo: update_many
    """
    if isinstance(server, Redis):
        command = payload['command'].upper()
        key = payload['key']
        if command == 'LSET':
            index = payload['index']
            value = ['value']
            return server.lset(key, index, value)
    elif isinstance(server, Session):
        query = payload['query']
        if 'params' in payload:
            params = payload['params']
            return server.execute(query, params)
        else:
            return server.execute(query)
    elif isinstance(server, MongoClient):
        collection = payload['collection']
        filterm = payload['filter']
        doc = payload['doc']
        if 'database' in payload:
            database = payload['database']
            db = server[database]
        else:
            database = conn_pool.configs['MongoDB']['database']
            db = server[database]
        col = db[collection]
        return col.update_many(filterm, doc).modified_count
    elif isinstance(server, PooledMySQLConnection):
        cursor = server.cursor(buffered=True)
        query = payload['query']
        if 'params' in payload:
            params = payload['params']
            cursor.execute(query, params)
            server.commit()
        else:
            cursor.execute(query)
            server.commit()
        cursor.close()
    else:
        pass


def delete(server, payload):
    """
    Delete methods currently considered =>
    Redis: del, lpop, srem, lrem
    Mongo: delete_many
    """
    if isinstance(server, Redis):
        command = payload['command'].upper()
        key = payload['key']
        if command == 'DEL':
            return server.delete(key)
        elif command == 'LPOP':
            return server.lpop(key)
        elif command == 'SREM':
            value = payload['value']
            return server.srem(key, value)
        elif command == 'LREM':
            value = payload['value']
            count = payload['count']
            return server.lrem(key, value, count)
    elif isinstance(server, Session):
        query = payload['query']
        if 'params' in payload:
            params = payload['params']
            return server.execute(query, params)
        else:
            return server.execute(query)
    elif isinstance(server, MongoClient):
        collection = payload['collection']
        filterm = payload['filter']
        if 'database' in payload:
            database = payload['database']
            db = server[database]
        else:
            database = conn_pool.configs['MongoDB']['database']
            db = server[database]
        col = db[collection]
        return col.delete_many(filterm).deleted_count
    elif isinstance(server, PooledMySQLConnection):
        cursor = server.cursor(buffered=True)
        query = payload['query']
        if 'params' in payload:
            params = payload['params']
            cursor.execute(query, params)
            server.commit()
        else:
            cursor.execute(query)
            server.commit()
        cursor.close()
    else:
        pass
