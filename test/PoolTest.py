from connections import Pool

Pool.get_config()

assert type(Pool.get_redis()) == 'redis.client.Redis'
assert type(Pool.get_cassandra()) == 'cassandra.cluster.Session'
