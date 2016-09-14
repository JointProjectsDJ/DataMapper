class MapRedis:
    server = None

    def __init__(self, pool):
        global server
        server = pool.create_redis()

    def get_redis(self):
        return server
