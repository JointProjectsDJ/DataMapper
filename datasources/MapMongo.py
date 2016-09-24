class MapMongo:
    server = None

    def __init__(self, pool):
        global server
        self.server = pool.get_mongo()

    def __del__(self):
        pass
