class MapMySql:
    server = None

    def __init__(self, pool):
        global server
        server = pool.create_mysql()

    def get_mysql(self):
        return server
