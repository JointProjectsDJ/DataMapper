class MapRedis:
    server = None

    def __init__(self, pool):
        global server
        server = pool.get_redis()

    def __del__(self):
        pass
