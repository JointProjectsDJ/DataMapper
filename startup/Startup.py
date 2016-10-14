# Start script for the app. All initializations to be performed here.
from connections.ConnectionPool import ConnectionPool
# pool = None

# global pool
if __name__ == "__main__":
    conn_pool = ConnectionPool()

def get_connection_pool():
    return ConnectionPool()
# pool.create_cassandra()
# pool.create_mongo()
# pool.create_mysql()
# pool.create_redis()
