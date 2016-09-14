class MapCassandra:
    server = None

    def __init__(self, pool):
        global server
        server = pool.create_cassandra()

    def get_cassandra(self):
        return server
