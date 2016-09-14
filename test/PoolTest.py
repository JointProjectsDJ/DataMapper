from connections import Pool

Pool.get_config()

print(type(Pool.get_redis()))
