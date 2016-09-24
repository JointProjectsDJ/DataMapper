class MapMySql:
    server = None

    def __init__(self, pool):
        global server
        self.server = pool.get_mysql()

    def __del__(self):
        pass
