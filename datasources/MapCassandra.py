class MapCassandra:
    server = None

    def __init__(self, pool):
        global server
        server = pool.get_cassandra()

    def __del__(self):
        pass
