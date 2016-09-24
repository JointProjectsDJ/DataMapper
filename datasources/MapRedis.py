class MapRedis:
    server = None

    def __init__(self, pool):
        global server
        self.server = pool.get_redis()

    def __del__(self):
        pass
