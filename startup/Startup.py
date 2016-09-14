# Start script for the app. All initializations to be performed here.
from connections.Pool import Pool
from datasources.MapMongo import MapMongo
from datasources.MapCassandra import MapCassandra
from datasources.MapRedis import MapRedis
from datasources.MapMySql import MapMySql

pool = Pool()
redis = MapRedis(pool).get_redis()
cass = MapCassandra(pool).get_cassandra()
mongo = MapMongo(pool).get_mongo()
mysql = MapMySql(pool).get_mysql()
