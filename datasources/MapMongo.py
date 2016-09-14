class MapMongo:
    server = None

    def __init__(self, pool):
        global server
        server = pool.create_mongo()

    def get_mongo(self):
        return server
