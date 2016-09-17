# Start script for the app. All initializations to be performed here.
from connections.Pool import Pool

pool = Pool()
pool.create_cassandra()
pool.create_mongo()
pool.create_mysql()
pool.create_redis()
