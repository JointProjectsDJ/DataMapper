from connections import ConnectionPool

ConnectionPool.get_config()

print(type(ConnectionPool.get_redis()))
